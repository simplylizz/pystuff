"""
    wsgi
    ~~~~

    Deploy with apache2 wsgi.
"""


import sys, os, pwd

project = "pystuff"

# specify dev/production config
os.environ['%s_APP_CONFIG' % project.upper()] = ''
# http://code.google.com/p/modwsgi/wiki/ApplicationIssues#User_HOME_Environment_Variable
os.environ['HOME'] = pwd.getpwuid(os.getuid()).pw_dir

BASE_DIR = os.path.join(os.path.dirname(__file__))
# activate virtualenv
activate_this = os.path.join(BASE_DIR, ".venv/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# give wsgi the "application"
from pystuff import create_app
application = create_app()
