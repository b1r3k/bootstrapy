import os
from logging import basicConfig
from logging.config import dictConfig
import logging
import yaml


def setup_logging(
        default_path='logging.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        print('Loading logger config from: {}'.format(path))
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        dictConfig(config)
    else:
        print('Using basicConfig for logger, could not open file {}'.format(path))
        basicConfig(level=default_level)
