"""Utils related to converting values from and to dict"""

__all__ = [
    'to_dict',
]


def to_dict(data, flatten=False):
    """Converts values of variables to python dicts.

    Parameters
    ----------
    data: list[Value]
        Values as list.
    flatten: bool
        Whether to flatten the key structure.
    Returns
    -------
    data: dict
        A structured dict of names and values.
    """
    output = {}
    for item in data:
        namespace = str(item.variable.namespace)
        result = output
        if not flatten:
            if len(namespace) > 0:
                for partial in namespace.split('.'):
                    if partial not in result:
                        result[partial] = {}
                    result = result[partial]
            column = item.variable.name
        else:
            if len(namespace) > 0:
                column = '{}.{}'.format(namespace, item.variable.name)
            else:
                column = item.variable.name
        if item.variable.multistep:
            index = item.step
            if column not in result:
                result[column] = {}
            result[column][index] = item.value
        else:
            result[column] = item.value
    return output
