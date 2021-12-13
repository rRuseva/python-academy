# serial reading config
SERAIL_PORT = '/dev/ttyACM0'
SERIAL_BAUDRAT  = 9600
# parity =
# stopbits =
# bytesize =
SERAIL_WRITE_TIMEOUT = 1

import os
ROOT_DIR = os.path.abspath(os.curdir)
DATA_PATH = os.path.join(ROOT_DIR, 'data')
DEFAULT_GARDEN_NAME = "Home garden"
DB_FILE_EXT = "json"

ASSETS_PATH = os.path.join(ROOT_DIR,'assets')

ENCODING = 'UTF-8'
