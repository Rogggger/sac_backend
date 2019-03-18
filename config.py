# coding: utf-8

SECRET_KEY = 'no SecRet, No pAssWORd'

# configs for sqlalchemy
SQLALCHEMY_DATABASE_URI = 'mysql://sac:sac_password@yuanw.wang/sac?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# configs for SSL cert
SSL_CERT = '/etc/letsencrypt/live/yuanw.wang/fullchain.pem'
SSL_KEY = '/etc/letsencrypt/live/yuanw.wang/privkey.pem'
