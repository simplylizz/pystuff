DEBUG = True

SECRET_KEY = 'asdJKHI(*^gvjvb xusat67^&%^R%UFGJH)(8 0cio xchi*&^'

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

SOCIAL_TWITTER = {
    'consumer_key': '',
    'consumer_secret': '',
}

SOCIAL_FACEBOOK = {
    'consumer_key': '',
    'consumer_secret': '',
}

SECURITY_URL_PREFIX = '/accounts/security'

#SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_PASSWORD_SALT = 'JKHUIYghsd(*&y0'
#SECURITY_EMAIL_SENDER

SECURITY_REGISTERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True

#SECURITY_POST_LOGIN = '/profile/'

SOCIAL_URL_PREFIX = '/accounts/social'
SOCIAL_APP_URL = 'http://example.com/'
