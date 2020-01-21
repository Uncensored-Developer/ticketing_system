import os


class Config:
    """Base Configurations."""


class ProdConfig:
    """Production Configuration."""
    ENV = 'production'
    DEBUG = False


class DevConfig:
    """Development Configuration."""
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
