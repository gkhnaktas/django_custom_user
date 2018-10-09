from appconf import AppConf
from django.conf import settings
from datetime import datetime


class UsersAppConf(AppConf):
    VERIFY_EMAIL = False
    CREATE_SUPERUSER = settings.DEBUG
    SUPERUSER_EMAIL = 'mail@test.com'
    SUPERUSER_PASSWORD = '1907'
    EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
    SPAM_PROTECTION = True
    REGISTRATION_OPEN = True
    AUTO_LOGIN_ON_ACTIVATION = True
    AUTO_LOGIN_AFTER_REGISTRATION = False
    PASSWORD_MIN_LENGTH = 5
    PASSWORD_MAX_LENGTH = None
    CHECK_PASSWORD_COMPLEXITY = True
    PASSWORD_POLICY = {
        'UPPER': 0,       # Uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'LOWER': 0,       # Lowercase 'abcdefghijklmnopqrstuvwxyz'
        'DIGITS': 0,      # Digits '0123456789'
        'PUNCTUATION': 0  # Punctuation """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    }
    VALIDATE_EMAIL_DOMAIN = True
    EMAIL_DOMAINS_BLACKLIST = []
    EMAIL_DOMAINS_WHITELIST = []

    class Meta:
        prefix = 'users'


UID_START_DATE = datetime(2008, 4, 19)
UID_ALPHABET = ['y', 'L', 'J', 'a', 's', '6', 'E', '7',
                'I', 'e', 'U', 'H', 'A', '1', 'b', 'R',
                'Y', '8', 'k', 'g', 'r', 'o', 'T', 'p',
                'G', '4', 'P', '0', '5', 't', 'M', 'j',
                'i', 'f', '9', 'F', 'D', 'x', 'c', 'N',
                'O', 'C', 'n', 'q', 'u', '2', 'B', 'z',
                'v', 'Q', 'h', 'w', 'S', 'm', 'X', 'V',
                'Z', 'K', '3', 'W', 'd', 'l']
