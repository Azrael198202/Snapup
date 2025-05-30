import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(PARENT_DIR, 'data')
LOG_DIR = os.path.join(PARENT_DIR, 'logs')

WEB_LOGIN = 'https://www.isseymiyake.com/account/login?redirect_to=myaccount'

WEB_LOGIN_AFTER = 'https://www.isseymiyake.com/account'