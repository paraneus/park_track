import pdb
import pytest
import uuid
import datetime
from app.models.Core import db
from app.models.Tracking import Tracking

class TestTrackingModel():
    def test_add_model_to_database(self, app):
        track = Tracking(
            start_time = datetime.datetime.now(),
            end_time = datetime.datetime.now() + datetime.timedelta(days=7)
        )

        db.session.add(track)
        db.session.commit()

        result = db.session.execute(
            db.select(Tracking)
        ).scalars().all()

        assert result
        assert len(result) == 1
        assert isinstance(result, list)
        assert hasattr(result[0], 'id')
        assert hasattr(result[0], 'start_time')
        assert hasattr(result[0], 'end_time')
        assert result[0].id is not None
        assert isinstance(result[0].id, uuid.UUID)
        assert isinstance(result[0].start_time, datetime.datetime)
        assert isinstance(result[0].end_time, datetime.datetime)

    def test_remove_model_from_database(self, app, tracking_model):
        db.session.delete(tracking_model)
        db.session.commit()


        result = db.session.execute(
            db.select(Tracking)
        ).scalars().all()

        assert not result

    @pytest.mark.parametrize('param', ('start_time', 'end_time'))
    def test_edit_tracking_object(self, app, tracking_model, param):
        new_time = datetime.datetime.now() + datetime.timedelta(seconds=500)
        setattr(tracking_model, param, new_time)
        db.session.commit()

        result = db.session.execute(
            db.select(Tracking)
        ).scalars().all()

        assert result
        assert len(result) == 1
        assert isinstance(result, list)
        assert hasattr(result[0], 'id')
        assert hasattr(result[0], 'start_time')
        assert hasattr(result[0], 'end_time')
        assert result[0].id is not None
        assert isinstance(result[0].id, uuid.UUID)
        assert isinstance(result[0].start_time, datetime.datetime)
        assert isinstance(result[0].end_time, datetime.datetime)
        assert getattr(result[0], param) == new_time

    def test_retrieve_a_tracking_entry(self, tracking_model):
        result = db.session.execute(
            db.select(Tracking).filter_by(end_time = tracking_model.end_time)
        ).scalars().all()

        assert result
        assert len(result) == 1

    def test_retrieve_conditional(self, tracking_model):
        result = db.session.execute(
            db.select(Tracking).filter(
                Tracking.end_time >= tracking_model.end_time - datetime.timedelta(seconds=20)
            )
        ).scalars().all()

        assert result
        assert len(result) == 1
