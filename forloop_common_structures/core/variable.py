from dataclasses import dataclass
from numbers import Number
from typing import Optional, Union

import numpy as np
import pandas as pd

VariableValueTypes = Union[str, Number, pd.DataFrame, list, dict]


@dataclass
class BaseVariable:
    """Base class for variable and initial_variable objects with common initialization logic."""

    name: str
    value: VariableValueTypes
    type: Optional[str] = None
    size: Optional[int] = None
    is_result: bool = False
    project_uid: str = "0"
    uid: Optional[str] = None

    def __post_init__(self) -> None:
        if self.type is None:
            self.type = type(self.value).__name__

        if self.size is None:
            if self.value is None:
                self.size = 0
            elif isinstance(self.value, (pd.DataFrame, pd.Series, np.ndarray)):
                self.size = self.value.size
            else:
                try:
                    self.size = len(self.value)
                except TypeError:
                    self.size = 1

    def __str__(self) -> str:
        return f"{self.value}"

    # Misleading repr looking like a simple data type when debugging
    # retained as the Platform might depend on it
    def __repr__(self) -> str:
        return f"{self.value}"

    def __len__(self) -> int:
        return self.size

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key in vars(self).keys():
                setattr(self, key, value)
            else:
                raise AttributeError(f"Attribute '{key}' cannot be updated, as it does not exist")


@dataclass
class Variable(BaseVariable):
    """
    Class containing Dataframes, Lists, Dicts (JSON) - objects visible and possible to manipulate.
    """

    pipeline_job_uid: str = "0"
            
@dataclass
class InitialVariable(BaseVariable):
    """Class containing Dataframes, Lists, Dicts (JSON) - objects visible and possible to manipulate."""

    pipeline_uid: str = "0"
