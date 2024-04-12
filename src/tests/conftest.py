import os
import datetime
import pytest
import pathlib
from app import app_factory
from app.models.Core import db
from app.models.Tracking import Tracking


@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    os.environ['FLASK_ENV'] = 'testing'
    app = app_factory.create_app()
    app.config['TESTING'] = True
    ctx = app.app_context()
    ctx.push()

    db.create_all()

    yield app

    db.session.close()
    db.drop_all()

@pytest.fixture
def static_file(app):
    file = pathlib.Path('app/static/static_file_for_test')
    file.touch()

    yield file

    os.remove(file)

@pytest.fixture
def test_client(app):
    return app.test_client()

@pytest.fixture()
def tracking_model():
    tracking = Tracking(
        start_time = datetime.datetime.now(),
        end_time = datetime.datetime.now() + datetime.timedelta(days=7)
    )

    db.session.add(tracking)
    db.session.commit()

    yield tracking
