from ._io import pickle_dump, pickle_load
from ..logging import get_logger
import os
from inspect import getmembers, isfunction, getfullargspec, ismodule, signature as s_

log = get_logger(__name__)

def cache_results(_cache_fp, _refresh=False):
    r""" a decorator to cache data-loader
    @reference: FastNLP::core::utils
    
    :param str `_cache_fp`:     where to read the cache from
    :param bool `_refresh`:     whether to regenerate cache

    >>> @cache_results('/tmp/cache.pkl')
    ... def load_data():
        # some time-comsuming process
        return processed_data
    """

    def wrapper_(func):
        signature = s_(func)

        def wrapper(*args, **kwargs):
            cache_filepath = kwargs.pop('_cache_fp', _cache_fp)
            refresh = kwargs.pop('_refresh', _refresh)
            refresh_flag = True

            if cache_filepath is not None and refresh is False:
                if os.path.exists(cache_filepath):
                    results = pickle_load(cache_filepath)
                    refresh_flag = False

            if refresh_flag:
                results = func(*args, **kwargs)
                if cache_filepath is not None:
                    if results is None:
                        raise RuntimeError("The return value is None. Delete the decorator.")
                    _prepare_cache_filepath(cache_filepath)
                    pickle_dump(results, cache_filepath)
                    log.info("Save cache to {}.".format(cache_filepath))

            return results

        return wrapper

    return wrapper_

def _prepare_cache_filepath(filepath):
    _cache_filepath = os.path.abspath(filepath)
    if os.path.isdir(_cache_filepath):
        raise RuntimeError("The cache_file_path must be a file, not a directory.")
    cache_dir = os.path.dirname(_cache_filepath)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir, exist_ok=True)