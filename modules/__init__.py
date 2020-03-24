#
# Specific Imports
#

from http.client import HTTPSConnection, HTTPConnection
from urllib.parse import unquote, quote
from base64 import b64encode as btoa
from base64 import b64decode as atob
from hashlib import scrypt, sha256
from html import unescape, escape

#
# General Imports
#

import sqlite3
import random
import socket
import struct
import hmac
import lzma
import time
import sys
import os

#
# Global Module Functions
#

getType = lambda value: str(type(value)).split('\'')[1].lower()
safeEncode = lambda s:  btoa(s).decode().replace('/', '-').replace('+', '_').replace('=', '')
safeDecode = lambda s:  atob(f'{s.replace("-", "/").replace("_", "+")}{"===="[0:len(s) % 4]}')

#
# Custom Imports
#

from .security import PasswordHashClass as PasswordHash