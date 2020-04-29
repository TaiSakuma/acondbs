from pathlib import Path
import threading
import shutil

import pytest
import unittest.mock as mock

from acondbs import create_app

##__________________________________________________________________||
from .constants import SAMPLE_DIR

##__________________________________________________________________||
@pytest.fixture
def database_uri(tmpdir_factory):
    """the database URI for a temporarily copy of the test data

    The fixture copies the test data `product.sqlite3` to a
    temporarily folder and returns the URI for the copy.

    """
    org_database_path = Path(SAMPLE_DIR, 'product.sqlite3')
    tmpdir = str(tmpdir_factory.mktemp('instance'))
    tmp_database_path = Path(tmpdir, 'product.sqlite3')
    shutil.copy2(org_database_path, tmp_database_path)
    ret = 'sqlite:///{}'.format(tmp_database_path)
    yield ret

##__________________________________________________________________||
@pytest.fixture
def app(database_uri):
    """a test Flask application

    The `app` is an instance of `Flask`. Its API is described in the
    Flask documentation at
    https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask

    The `app` is initialized for the SQLAlchemy DB with URI at
    `database_uri`.

    Yields
    ------
    Flask

    """
    config_path = Path(SAMPLE_DIR, 'config.py')
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    yield app

##__________________________________________________________________||
@pytest.fixture
def client(app):
    """a test client of the Flask application

    The test client, an instance of `FlaskClient`, can emulate HTTP
    requests, e.g, GET, POST. For example::

        response = client.get('/')

    The response object (`Response`) can be examined for tests

    More in the Flask documentation:
    `FlaskClient`: https://flask.palletsprojects.com/en/1.1.x/api/#test-client
    `Response`: https://flask.palletsprojects.com/en/1.1.x/api/#response-objects
    `test_client()`: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client


    Yields
    ------
    FlaskClient

    """
    yield app.test_client()

##__________________________________________________________________||
@pytest.fixture
def runner(app):
    """a test CLI runner of the Flask application

    The runner (`FlaskCliRunner`) is used to test custom click
    commands.

    More in the Flask documentation:
    `FlaskCliRunner`: https://flask.palletsprojects.com/en/1.1.x/api/#test-cli-runner
    `Result`: https://click.palletsprojects.com/en/7.x/api/#click.testing.Result
    `test_cli_runner()`: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_cli_runner

    Yields
    ------
    FlaskCliRunner

    """
    yield app.test_cli_runner()

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def db_backup_global_variables(monkeypatch):
    from acondbs.db import backup
    monkeypatch.setattr(backup, '_lock', threading.Lock())
    monkeypatch.setattr(backup, '_capped_backup_func', None)
    yield
    backup.end_backup_thread()

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_request_backup_db(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.map_.request_backup_db", y)
    yield y

##__________________________________________________________________||
