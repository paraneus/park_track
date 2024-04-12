from typing import Any
from flask import request, jsonify
from flask.views import MethodView
from pprint import pprint

class BaseView(MethodView):
    def get(self) -> Any:
        pass

    def patch(self) -> Any:
        pass

    def post(self) -> Any:
        pass

    def delete(self) -> Any:
        pass
