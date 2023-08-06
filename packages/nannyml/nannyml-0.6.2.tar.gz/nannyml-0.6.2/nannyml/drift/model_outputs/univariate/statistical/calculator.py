#  Author:   Niels Nuyttens  <niels@nannyml.com>
#
#  License: Apache Software License 2.0

"""Calculates drift for model predictions and model outputs using statistical tests."""

from typing import Any, Dict, List, Optional, Union

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, ks_2samp

from nannyml._typing import ModelOutputsType, ProblemType, model_output_column_names
from nannyml.base import AbstractCalculator, _column_is_categorical, _list_missing
from nannyml.chunk import Chunker
from nannyml.drift.model_outputs.univariate.statistical.results import UnivariateDriftResult
from nannyml.exceptions import InvalidArgumentsException

ALERT_THRESHOLD_P_VALUE = 0.05


class StatisticalOutputDriftCalculator(AbstractCalculator):
    """Calculates drift for model predictions and model outputs using statistical tests."""

    def __init__(
        self,
        y_pred: str,
        problem_type: Union[str, ProblemType],
        y_pred_proba: ModelOutputsType = None,
        timestamp_column_name: str = None,
        chunk_size: int = None,
        chunk_number: int = None,
        chunk_period: str = None,
        chunker: Chunker = None,
    ):
        """Creates a new StatisticalOutputDriftCalculator.

        Parameters
        ----------
        y_pred_proba: ModelOutputsType
            Name(s) of the column(s) containing your model output.
            Pass a single string when there is only a single model output column, e.g. in binary classification cases.
            Pass a dictionary when working with multiple output columns, e.g. in multiclass classification cases.
            The dictionary maps a class/label string to the column name containing model outputs for that class/label.
        y_pred: str
            The name of the column containing your model predictions.
        timestamp_column_name: str, default=None
            The name of the column containing the timestamp of the model prediction.
        chunk_size: int, default=None
            Splits the data into chunks containing `chunks_size` observations.
            Only one of `chunk_size`, `chunk_number` or `chunk_period` should be given.
        chunk_number: int, default=None
            Splits the data into `chunk_number` pieces.
            Only one of `chunk_size`, `chunk_number` or `chunk_period` should be given.
        chunk_period: str, default=None
            Splits the data according to the given period.
            Only one of `chunk_size`, `chunk_number` or `chunk_period` should be given.
        chunker : Chunker, default=None
            The `Chunker` used to split the data sets into a lists of chunks.

        Examples
        --------
        >>> import nannyml as nml
        >>>
        >>> reference_df, analysis_df, _ = nml.load_synthetic_binary_classification_dataset()
        >>>
        >>> calc = nml.StatisticalOutputDriftCalculator(
        >>>     y_pred_proba='y_pred_proba',
        >>>     y_pred='y_pred',
        >>>     timestamp_column_name='timestamp'
        >>> )
        >>> calc.fit(reference_df)
        >>> results = calc.calculate(analysis_df)
        >>>
        >>> print(results.data)  # check the numbers
                     key  start_index  ...  y_pred_proba_alert y_pred_proba_threshold
        0       [0:4999]            0  ...                True                   0.05
        1    [5000:9999]         5000  ...               False                   0.05
        2  [10000:14999]        10000  ...               False                   0.05
        3  [15000:19999]        15000  ...               False                   0.05
        4  [20000:24999]        20000  ...               False                   0.05
        5  [25000:29999]        25000  ...                True                   0.05
        6  [30000:34999]        30000  ...                True                   0.05
        7  [35000:39999]        35000  ...                True                   0.05
        8  [40000:44999]        40000  ...                True                   0.05
        9  [45000:49999]        45000  ...                True                   0.05
        >>>
        >>> results.plot(kind='score_drift', metric='p_value', plot_reference=True).show()
        >>> results.plot(kind='score_distribution', plot_reference=True).show()
        >>> results.plot(kind='prediction_drift', plot_reference=True).show()
        >>> results.plot(kind='prediction_distribution', plot_reference=True).show()
        """
        super(StatisticalOutputDriftCalculator, self).__init__(
            chunk_size, chunk_number, chunk_period, chunker, timestamp_column_name
        )

        self.y_pred_proba = y_pred_proba
        self.y_pred = y_pred

        if isinstance(problem_type, str):
            problem_type = ProblemType.parse(problem_type)
        self.problem_type: ProblemType = problem_type  # type: ignore

        if self.problem_type is not ProblemType.REGRESSION and self.y_pred_proba is None:
            raise InvalidArgumentsException(
                f"'y_pred_proba' can not be 'None' for " f"problem type {self.problem_type.value}"
            )

        self.previous_reference_data: Optional[pd.DataFrame] = None
        self.previous_reference_results: Optional[pd.DataFrame] = None
        self.previous_analysis_data: Optional[pd.DataFrame] = None

    def _fit(self, reference_data: pd.DataFrame, *args, **kwargs):
        """Fits the drift calculator using a set of reference data."""
        if reference_data.empty:
            raise InvalidArgumentsException('data contains no rows. Please provide a valid data set.')

        if self.y_pred_proba:
            _list_missing([self.y_pred] + model_output_column_names(self.y_pred_proba), reference_data)
        else:
            _list_missing([self.y_pred], reference_data)

        self.previous_reference_data = reference_data.copy()

        # Force categorical columns to be set to 'category' pandas dtype
        # TODO: we should try to get rid of this
        if _column_is_categorical(reference_data[self.y_pred]):
            reference_data[self.y_pred] = reference_data[self.y_pred].astype('category')

        # Reference stability
        self._reference_stability = 0  # TODO: Jakub

        self.previous_reference_results = self._calculate(reference_data).data

        return self

    def _calculate(self, data: pd.DataFrame, *args, **kwargs) -> UnivariateDriftResult:
        """Calculates the data reconstruction drift for a given data set."""
        if data.empty:
            raise InvalidArgumentsException('data contains no rows. Please provide a valid data set.')

        if self.y_pred_proba:
            _list_missing([self.y_pred] + model_output_column_names(self.y_pred_proba), data)
        else:
            _list_missing([self.y_pred], data)

        continuous_columns: List[str] = []
        categorical_columns: List[str] = []
        if self.problem_type == ProblemType.CLASSIFICATION_BINARY:
            if isinstance(self.y_pred_proba, str):
                continuous_columns += [self.y_pred_proba]
            categorical_columns += [self.y_pred]
        elif self.problem_type == ProblemType.CLASSIFICATION_MULTICLASS:
            if self.y_pred_proba is not None:
                continuous_columns += model_output_column_names(self.y_pred_proba)
            categorical_columns += [self.y_pred]
        elif self.problem_type == ProblemType.REGRESSION:
            continuous_columns += [self.y_pred]

        chunks = self.chunker.split(data, columns=continuous_columns + categorical_columns)
        chunk_drifts = []
        # Calculate chunk-wise drift statistics.
        # Append all into resulting DataFrame indexed by chunk key.
        for chunk in chunks:
            chunk_drift: Dict[str, Any] = {
                'key': chunk.key,
                'chunk_index': chunk.chunk_index,
                'start_index': chunk.start_index,
                'end_index': chunk.end_index,
                'start_date': chunk.start_datetime,
                'end_date': chunk.end_datetime,
            }

            for column in categorical_columns:
                statistic, p_value, _, _ = chi2_contingency(
                    pd.concat(
                        [
                            self.previous_reference_data[column].value_counts(),  # type: ignore
                            chunk.data[column].value_counts(),
                        ],
                        axis=1,
                    ).fillna(0)
                )
                chunk_drift[f'{column}_chi2'] = statistic
                chunk_drift[f'{column}_p_value'] = np.round(p_value, decimals=3)
                chunk_drift[f'{column}_alert'] = p_value < ALERT_THRESHOLD_P_VALUE
                chunk_drift[f'{column}_threshold'] = ALERT_THRESHOLD_P_VALUE

            for column in continuous_columns:
                statistic, p_value = ks_2samp(self.previous_reference_data[column], chunk.data[column])  # type: ignore
                chunk_drift[f'{column}_dstat'] = statistic
                chunk_drift[f'{column}_p_value'] = np.round(p_value, decimals=3)
                chunk_drift[f'{column}_alert'] = p_value < ALERT_THRESHOLD_P_VALUE
                chunk_drift[f'{column}_threshold'] = ALERT_THRESHOLD_P_VALUE

            chunk_drifts.append(chunk_drift)

        res = pd.DataFrame.from_records(chunk_drifts)
        res = res.reset_index(drop=True)

        self.previous_analysis_data = data.copy()

        return UnivariateDriftResult(results_data=res, calculator=self)
