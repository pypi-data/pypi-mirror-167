# Logger Module X

Just logging python file !

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install loggermodule-X
```

## Usage

```python
from loggermodule_X import configLogger

log = configLogger(__name__, __file__, console_lv='INFO', file_lv='ERROR')

log.info('INFO')
log.debug('DEBUG')
log.error('ERROR')
log.warning('WARNING')

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Infoquest Limited](https://www.infoquest.co.th/)