from typing import List

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class LogTransformer(BaseEstimator, TransformerMixin):
    """Log Transformer"""

    def __init__(self, variables: List[str], reference_variable: List[str]):

        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # we need this step to fit the sklearn pipeline
        return self


    def transform(self, X: pd.DataFrame) -> pd.DataFrame:

        X = X.copy()

        for column in X[X.columns.intersection(self.reference_variable).tolist()].columns:
            try:
                X[column] = np.log10(X[column])
            except (ValueError, AttributeError):
                pass

        return X
