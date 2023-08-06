# pjconf

A simple configuration interface to use JSON files as configuration files.

## Installation

PJC is installed via pip.

```shell
pip install pjconf
```

## Usage

Loading configuration is straightforward, just import and point to your json file.

```python
import pjconf as pjc

# Load a json file as a configuration dictionary.
config = pjc.load_config('config.json')

# or, load a configuration file with an optional default set of configuration elsewhere
config = pjc.load_config('defaults.json', 'config.json', ignore_missing=True)
```

Configuration files are loaded in a cascading sequence, multiple positional filepaths are loaded and override/update the previous keys. Setting `ignore_missing=True` will allow for a flexible resolve of optional configuration; disabling it will raise a `FileNotFoundError` on the first file it can't find.

Accessing configuration uses a ``get()`` method, with a cool dot-recursive syntax, optional defaults and runtime type-casting.

Let's assume the following configuration file.

```json
{
    "opt1": true
    "opt2": 0.1
    "opt3": {
        "subopt1": "hello"
    } 
}
```

You can use the following syntax to access your configuration.

```python

# Access a simple option
opt1 = config.get('opt1')
# True

# Access a recursive (nested) option
subopt1 = config.get('opt3.subopt1')
# "hello"

# Try to access a missing option, but provide a default
missing_opt = config.get('missing', default=True)
# True

# Runtime type-casting
opt2asint = config.get('opt2', cast=int)
# 0
```

For the last example, the ``cast`` argument takes a callable with a single parameter - you can be as simple or as complicated (i.e. lambdas or defined functions) as you like.