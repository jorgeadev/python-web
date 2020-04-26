class Config:
	SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
	DEBUG = True

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}