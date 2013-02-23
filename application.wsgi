import os, sys

PROJECT_DIR = "/www/helloflask.enigmeta.com/helloflask"
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from helloflask import app as application