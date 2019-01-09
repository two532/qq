import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = 'a9087FFJFF9nnvc2@#$%FSD'

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost:3306/cc'

	SQLALCHEMY_TRACK_MODIFICATIONS = False