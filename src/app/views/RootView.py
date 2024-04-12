from flask import render_template
from app.views.BaseView import BaseView
from app.models.Tracking import Tracking
import datetime

class RootView(BaseView):
    def get(self):
        # this is just test data to fill the template
        # nothing is added to the db here
        tracking = [
            Tracking(
                start_time = datetime.datetime.now()-datetime.timedelta(days=12),
                end_time = datetime.datetime.now()-datetime.timedelta(days=19)
            ),
            Tracking(
                start_time = datetime.datetime.now()-datetime.timedelta(days=6),
                end_time = datetime.datetime.now()-datetime.timedelta(days=5)
            ),
        ]

        # get template called 'base.html' and add parameters used in it
        return render_template('base.html', content='Test', title='Test Title', tracking_data=tracking)
