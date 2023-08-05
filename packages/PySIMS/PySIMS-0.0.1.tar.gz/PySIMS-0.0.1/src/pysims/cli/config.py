r"""The config command and configuration constants.

Functionality related to reading and writing the program's configuration.
"""

# Standard Library
import logging
from pathlib import Path

# Third Party

# Local


logger = logging.getLogger(__name__)


# Context settings to apply to the main function of the click application
CONTEXT_SETTINGS: dict = dict(help_option_names=['-h', '--help'], max_content_width=600)

# Name of the program
PROG_NAME: str = 'pysims'

# The name of the program displayed in help texts
PROG_NAME_DISPLAY: str = 'pysims'

# The home directory of the program
PROG_DIR = Path.home() / f'.{PROG_NAME}'

# The name of the configuration file
CONFIG_FILENAME = f'.{PROG_NAME}.toml'

# The full path to the configuration file
CONFIG_FILE_PATH: Path = PROG_DIR / CONFIG_FILENAME

# The default path to the SQLite database
SQLITE_DB_PATH: Path = PROG_DIR / f'{PROG_NAME}.db'
