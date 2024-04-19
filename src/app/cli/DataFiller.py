import click
import datetime
import random
from flask.cli import FlaskGroup
from app.models.Core import db
from app.models.Tracking import Tracking

data_filler = FlaskGroup(name="DataFiller")
@data_filler.command('backfill')
@click.option('--days', help='Number of days to backfill', type=int)
def fill_trackingt_data(days=100):
    index = 0
    while index < days:
        duration = random.randint(1, 5)

        start = datetime.datetime.now() - datetime.timedelta(days=days-index)
        end = start + datetime.timedelta(days=duration)
        tracking = Tracking(start_time=start, end_time=end)

        db.session.add(tracking)
        db.session.commit()

        index += duration+1
        click.echo(f'Added: {tracking} start: {tracking.start_time} end: {tracking.end_time} - period: {tracking.period}')
