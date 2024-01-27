from pathlib import Path
from urllib.parse import urljoin

# Определение базового каталога приложения
BASE_DIR = Path(__file__).parent

# Основные URL для документации Python
MAIN_DOC_URL = 'https://docs.python.org/3/'
WHATS_NEW_URL = urljoin(MAIN_DOC_URL, 'whatsnew/')
DOWNLOAD_DOC_URL = urljoin(MAIN_DOC_URL, 'download.html')

# Настройки логирования
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / 'parser.log'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

# URL для документации PEPs Python
PEPS_PYTHON_URL = 'https://peps.python.org/'

# Формат даты и времени
DR_FORMAT = '%d.%m.%Y %H:%M:%S'

# Статусы PEPs и их описания
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}

# Константы для определения формата вывода
PRETTY_OUTPUT = 'pretty'
FILE_OUTPUT = 'file'
DEFAULT_OUTPUT = None
DOWNLOADS = 'downloads'
RESULTS = 'results'
