import os
import shutil
import logging
from os import path


class DirExistsError(FileExistsError):
    ...


class PathNotExistsError(Exception):
    ...


def create_dir(*args, clean_up=True, report_error=False):
    _path = path.join(*args)

    if path.isdir(_path):
        if report_error:
            raise DirExistsError(_path)
        if clean_up:
            logging.debug(f'remove and remake {_path}')
            shutil.rmtree(_path)
            os.mkdir(_path)
    else:
        logging.debug(f'make {_path}')
        os.mkdir(_path)

    return _path


def path_should_exist(_path: str):
    if not path.exists(_path):
        raise PathNotExistsError(_path)
    return _path
