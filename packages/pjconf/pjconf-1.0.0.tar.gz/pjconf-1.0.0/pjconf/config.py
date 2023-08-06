"""Object for handling configuration."""
import os
import json

class Config:

    """Configuration object."""

    def __init__(self):
        self._config = dict()


    def load(self, *filepaths, ignore_missing=False):
        """Load configuration from one or more filepaths.

        Args:
            *filepaths (str) : Filepaths for loading.
            ignore_missing (bool, optional): Ignore missing files. Defaults to True.

        Raises:
            FileNotFoundError: When a filepath doesn't exist and ignore_missing=False.
            ValueError: When the supplied filepaths result in an empty configuration object.
        """
        
        _config = dict()

        for filepath in filepaths:
            
            if os.path.isfile(filepath):
                __config = json.load(open(filepath, 'r'))
                _config.update(__config)
            
            elif ignore_missing != True:
                raise FileNotFoundError(f'File {filepath} not found. Add ignore_missing=True to skip loading.')

        # Empty config?
        if _config == False:
            raise ValueError('Supplied filepaths result in empty configuration.')

        self._config = _config


    def get(self, key, default=None, cast=None):
        """Get the configuration value out of the configuration, with an optional default if it is not set.

        Args:
            key (str): Key (can be dot-recursive).
            default (mixed, optional): Default value if not found. Defaults to None (throws KeyError if not found).
            cast (callable, optional): Optionally recast the data into another type at runtime.
        
        Returns:
            mixed: Value returned by addressing key.

        Raises:
            KeyError: If there is no configutation option reachable from the key.
            Exception: If data cannot be recast.

        """
        candidate = None
        
        try:
            
            # Loop through each sub-key
            for _key in key.split('.'):

                if candidate is None:
                    candidate = self._config[_key]
                else:
                    candidate = candidate[_key]
        
        except KeyError:

            if default is not None:
                candidate = default
            
            else:
                raise KeyError(f'No reachable configuration option assigned to "{key}".')
        
        # Optional recasting
        if cast:
            return cast(candidate)
        
        # Return as is
        return candidate