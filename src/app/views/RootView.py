import random
from typing import Union
from flask import render_template
from app.views.BaseView import BaseView
from app.models.Tracking import Tracking
from app.models.Core import db
import datetime

## Exploring python - Here be dragons

class RootView(BaseView):
    def generate_test_tracking_data(self, num_entries):
        # random entries for testing
        testtracking_data = []
        for _ in range(num_entries):
            start_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 50))
            end_time = start_time + datetime.timedelta(days=random.randint(1, 10))
            testtracking_data.append(Tracking(start_time=start_time, end_time=end_time))
        return testtracking_data

    def render_tracking_data(self, tracking_data, tracking_data_count, total_parking_days, testtracking_data, testtracking_data_count, test_total_parking_days):
        total_parking_days = sum((entry.end_time - entry.start_time).days + 1 for entry in tracking_data if entry.start_time >= datetime.datetime.now() - datetime.timedelta(days=30))
        tracking_data_count = len(tracking_data)

        return render_template('base.html', content='History', title='Fuck Parkon', tracking_data=tracking_data, tracking_data_count=tracking_data_count, total_parking_days=total_parking_days, testtracking_data=testtracking_data, testtracking_data_count=testtracking_data_count, test_total_parking_days=test_total_parking_days)

    def get_entries(self, since: Union[datetime.datetime, None] = None) -> list[Tracking]:
        import pdb
        return db.session.execute(
            db.select(Tracking).filter(Tracking.end_time >= since)
        ).scalars().all()

    def get(self):
        days_limit = datetime.datetime.now() - datetime.timedelta(days=31)    
        # dates out of the db
        tracking_data = db.session.execute(db.select(Tracking)).scalars().all()

        # count parkingdays and entries
        total_parking_days = sum(
            (entry.end_time - entry.start_time).days + 1 for entry in tracking_data if entry.start_time >= days_limit
        )
        tracking_data_count = len(tracking_data)

        
        # testing purposes (this is just test data to fill the template)
        testtracking_data = self.generate_test_tracking_data(3)

        test_total_parking_days = sum((entry.end_time - entry.start_time).days + 1 for entry in testtracking_data if entry.start_time >= datetime.datetime.now() - datetime.timedelta(days=30))
        testtracking_data_count = len(testtracking_data)

        # get template called 'base.html' and add parameters used in it
        return self.render_tracking_data(
            tracking_data,
            tracking_data_count,
            total_parking_days,
            testtracking_data,
            testtracking_data_count,
            test_total_parking_days
        )