import requests

def get_if_dict(val, key):
    if key in val and isinstance(val[key], dict):
        return val[key]
    return val

def get_attr_v4(val, attr):
    if isinstance(val, requests.Response):
        val = val.json()

    if not isinstance(val, dict):
        raise TypeError('get_attr filter requires input of type requests.Response or dict.')

    if attr in val:
        return val[attr]

    # is it in data?
    val = get_if_dict(val, 'data')
    if attr in val:
        return val[attr]

    # is it in attributes?
    val = get_if_dict(val, 'attributes')
    if attr in val:
        return val[attr]

    return val.get(attr)

def get_user_v4(val, attr=None):
    if not isinstance(val, dict):
        return None

    _user = val.get('user')
    if attr is None or _user is None:
        return _user

    return _user.get(attr)
