SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secret@park_db/park_tracking'

# This is needed in order for flasgger to behave sort of like we want to.
SWAGGER = {
    'openapi': '3.0.2',
    'uiversion': 3
}

DEBUG = True
