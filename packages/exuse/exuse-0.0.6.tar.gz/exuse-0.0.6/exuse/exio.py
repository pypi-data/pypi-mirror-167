"""utils to load some file"""

import logging
from glob import glob

EXT_PREFERENCES = ['json', 'toml', 'yaml']


def glob_list(patterns: list[str]):
    results = []
    for x in patterns:
        for r in glob(x):
            results.append(r)
    return results


def get_config_path(name: str, dirs: list[str]):
    for dir in dirs:
        r = glob_list([f'{dir}/{name}.*', f'{dir}/**/{name}.*'])
        if len(r) == 1:
            return r[0]
        elif len(r) > 1:
            target = r[0]
            Q = {x.split('.')[-1]: i for i, x in enumerate(r)}
            for k in EXT_PREFERENCES:
                if Q.get(k) is not None:
                    target = r[Q[k]]
                    break
            logging.warning(
                f'Multiple files found in {dir} for {name}, loading {target}')
            return target
    raise FileNotFoundError(name)


def load_config_file(fp: str):
    """read some file to dict object"""
    if fp.endswith('toml'):
        import toml
        return toml.load(fp)
    elif fp.endswith('yaml'):
        import yaml
        with open(fp) as r:
            return yaml.load(r)
    elif fp.endswith('json'):
        import json
        with open(fp) as r:
            return json.load(r)
    else:
        raise ValueError(f"Unsupported file extension: {fp.split('.')[-1]}")
