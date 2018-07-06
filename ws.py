import argparse
import cherrypy
import pandas as pd
import logging.config

import myprocessor

LOCAL_DIR = '/ws/'
LOG_DIR = LOCAL_DIR + 'logs/'
MY_USERS = {'myuser': 'password_for_myuser'}
PORT = 8080

parser = argparse.ArgumentParser()
parser.add_argument('--logLevel', default='INFO', help='Update log level, default level is INFO')
parser.add_argument('--ssl', action='store_true', help='Enable SSL', default=False)
args = parser.parse_args()
LOG_LEVEL = args.logLevel

# Log Configuration for CherryPy Server log only, storing cherrypy logs in LOG_DIR
logging.config.dictConfig(
    {
    'version' : 1,

    'formatters': {
        'void': {
            'format': ''
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_console': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'void',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_access': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': LOG_DIR + 'cp_access.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'cherrypy_error': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': LOG_DIR + 'cp_errors.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': LOG_LEVEL
        },
        'db': {
            'handlers': ['default'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'cherrypy.access': {
            'handlers': ['cherrypy_access'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'cherrypy.error': {
            'handlers': ['cherrypy_console', 'cherrypy_error'],
            'level': LOG_LEVEL,
            'propagate': False
        },
    }
})

p = myprocessor.MyProcessor()


def validate_password(realm, username, password):
    if username in MY_USERS and MY_USERS[username] == password:
       return True
    return False


@cherrypy.expose
class MyGreetingsWebService(object):
    def GET(self):
        return 'Hello.'

@cherrypy.expose
@cherrypy.tools.json_out()
@cherrypy.tools.json_in()
class MyDummyMachineLearningWebService(object):

    def POST(self):
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = p.run(df)
        return output.to_json()

if __name__ == '__main__':

    # Global config
    cherrypy.config.update({'server.socket_port': PORT,
                            'server.socket_host': '0.0.0.0'})

    # Enable SSL
    if args.ssl :
        cherrypy.config.update({'server.ssl_module' : 'builtin',
                            'server.ssl_certificate' : LOCAL_DIR + 'cert.pem',
                            'server.ssl_private_key' : LOCAL_DIR + 'privkey.pem'})

    # Web Service config
    conf = {
        '/': {
            'response.timeout': 6000,
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],

            # Basic Authentication
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'om',
            'tools.auth_basic.checkpassword': validate_password
        }
    }

    root = MyGreetingsWebService()
    root.ml = MyDummyMachineLearningWebService()
    cherrypy.quickstart(root, config=conf)
