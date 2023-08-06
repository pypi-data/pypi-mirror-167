"""Utils related to converting from and to pandas DataFrames"""
from collections.abc import Mapping

import pandas as pd

from mxdesign.utils.dict import to_dict

__all__ = [
    'to_frame',
    'from_frame',
]


def to_frame(data):
    """Converts values of variables to pandas DataFrame.

    Parameters
    ----------
    data: list[Value]
        Values as list.
    Returns
    -------
    df: pd.DataFrame
        A pandas DataFrame with data.
    """
    df = pd.DataFrame(to_dict(data, flatten=True))
    return df


def from_frame(df):
    """Converts a dataframe to values of variables (dictionary form).

    Parameters
    ----------
    df: pd.DataFrame
        Input DataFrame.
    Returns
    -------
    data: pd.DataFrame
        The data contained in df as dict compatible with Value struct.
    """
    data = []
    for name, step_value in df.to_dict().items():
        is_multistep = df.attrs.get('__mxd__', {}).get(name)
        if is_multistep is None:
            is_multistep = isinstance(step_value, Mapping)
        ns = name.split('.')
        if len(ns) == 1:
            namespace, key = None, ns[0]
        else:
            namespace, key = '.'.join(ns[:-1]), ns[-1]
        if is_multistep:
            for step, value in step_value.items():
                data.append(dict(key=key, value=value, namespace=namespace, step=step))
        else:
            value = step_value
            data.append(dict(key=key, value=value, namespace=namespace, step=None))
    return data
