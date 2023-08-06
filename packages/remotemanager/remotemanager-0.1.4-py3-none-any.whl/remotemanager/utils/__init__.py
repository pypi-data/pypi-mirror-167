import os
import math
import time

# need __version__, is there a better way than importing the whole package?
import remotemanager


def ensure_list(inp=None):
    if inp is None:
        return []
    elif isinstance(inp, (list, tuple, set)):
        return list(inp)
    elif isinstance(inp, str):
        return [inp]
    return list(inp)


def ensure_filetype(file, target_type):
    """
    Ensure that `file` is of type `type`
    Args:
        file (str):
            filename
        target_type (str):
            filetype to enforce

    Returns (str):
        filename of type `type`
    """
    fname, ftype = os.path.splitext(file)

    target_type = target_type.strip('.')

    return f'{fname}.{target_type}'


def ensure_dir(dir):
    """
    Ensure that string path to `dir` is correctly formatted
    ONLY ensures that the folder name ends with a "/", does not produce an
    abspath

    Args:
        dir (str):
            path to dir

    Returns (str):
        ensured dir path

    """
    if not isinstance(dir, str):
        dir = str(dir)

    return os.path.join(dir, ' ').strip()


def safe_divide(a, b):
    """
    always-fit division. Rounds up after division, always returns >= 1
    """
    if b == 0:
        return 1
    r = math.ceil(a / b)
    return max(r, 1)


def get_version():
    return remotemanager.__version__


def recursive_dict_update(d1: dict,
                          d2: dict) -> dict:
    """
    Update d1 with all the keys of d2
    Args:
        d1 (dict):
            dictionary to be updated
        d2 (dict):
            dictionary to update with

    Returns (dict):
        updated d1

    """

    for k, v in d2.items():
        if isinstance(v, dict) and k in d1:
            d1[k] = recursive_dict_update(d1[k], d2[k])
        else:
            d1[k] = v

    return d1


def reverse_index(inplist, term):
    """
    return index of last occurrence of `term` in `inplist`
    Args:
        inplist (list):
            list to index
        term:
            object to index

    Returns (int):
        forward index of item

    """
    return len(inplist) - inplist[::-1].index(term) - 1


def integer_time_wait(offset: float = 0.0) -> None:
    """
    wait for an integer unix time + offset

    This function exists to increase the reproducibility of the tests

    Args:
        offset (float):
            extra offset to wait for
    """

    t0 = time.time()

    wait = 1 - math.fmod(t0, 1)

    time.sleep(wait + offset)

    return
