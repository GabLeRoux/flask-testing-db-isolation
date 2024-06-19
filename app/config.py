import logging
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/dev_db"
    )


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_TEST_URL", "postgresql://user:password@db:5432/test_db"
    )
    TESTING = True


logging.debug(f"TestingConfig: {TestingConfig.SQLALCHEMY_DATABASE_URI}")
