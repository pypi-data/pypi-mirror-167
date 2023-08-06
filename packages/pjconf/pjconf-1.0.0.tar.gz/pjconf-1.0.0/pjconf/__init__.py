"""pjconf main module."""
from importlib.metadata import version
from pjconf.config import Config

# Version handle
__version__ = version('pjconf')


def load_config(*filepaths, ignore_missing=False):
    """Shortcut to instantiate and load a configuration object.

    Args:
        *filepaths (str): Multiple possible filepaths that will be loaded in sequence.
        ignore_missing (bool, optional): Ignore files that do not exist
    
    Returns:
        pjconf.config.Config : Configuration object
    """
    config = Config()
    config.load(*filepaths, ignore_missing=ignore_missing)
    return config