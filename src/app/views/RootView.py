import datetime
from pprint import pprint
from flask import render_template, redirect, request
from app.views.BaseView import BaseView
from app.models.Tracking import Tracking
from app.models.Core import db

class RootView(BaseView):
    # HINT
    # i've added a few tracking entries to the DB via a cli hook:
    # flask -A  main:application backfill --days 100
    # you can do the same.
    def get(self):
        # define the cutoff time
        cutoff = datetime.datetime.now() - datetime.timedelta(days=30)

        # get all records, sorted in descending order (newest first)
        tracking = db.session.execute(
            db.select(Tracking).order_by(Tracking.start_time.desc())
        ).scalars().all()

        # figure out which ones are within the cutoff period
        tracking_since_cutoff = [entry for entry in tracking if entry.end_time and entry.end_time >= cutoff]

        # put everything in the template and send it to client
        return render_template(
            'base.html',
            title='Parking History',
            tracking_cutoff=tracking_since_cutoff,  # all trackings within the relelvant period
            accountable_days=sum([entry.period for entry in tracking_since_cutoff]),  # sum of the days parked inside the relevant period
            tracking_total=[entry for entry in tracking if entry.period],  # all trackings that are finished
            days_total=sum([entry.period for entry in tracking if entry.period]),  # sum of days parked over entire history
            current_trackings=[entry for entry in tracking if not entry.period]  # currently running trackings
        )

    def post(self):
        data = request.form.to_dict()
        data = {k: v for k, v in data.items()}
        pprint(data)

        # this is sort of an abuse case, no idea if this is the way to handle it
        # but we'll see.
        pressed = [k for k in data.keys() if data[k] == 'pressed']
        if len(pressed) > 1:
            print(f'{request} multiple buttons pressed: {pressed}')
            return redirect('/')

        if data['track_id'] == '':
            # create a  new tracking
            tracking = Tracking(start_time = datetime.datetime.now())
            db.session.add(tracking)
            db.session.commit()
        elif data['track_id'] != '' and 'stop' in data.keys() and data['stop'] == 'pressed':
            tracking = db.get_or_404(Tracking, data['track_id'])
            tracking.end_time = datetime.datetime.now()
            db.session.commit()
        elif data['track_id'] != '' and 'delete' in data.keys() and data['delete'] == 'pressed':
            tracking = db.get_or_404(Tracking, data['track_id'])
            db.session.delete(tracking)
            db.session.commit()
        else:
            # haven't implemented anything other that stop
            # existing buttons, other that "stop" are just an example
            print(f'unimplemented button press: {data}')
            return redirect('/')

        return redirect('/')
