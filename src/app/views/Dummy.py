from flask import request, jsonify
from pprint import pprint
from flasgger import SwaggerView


# https://flask.palletsprojects.com/en/3.0.x/views/
class DummyView(SwaggerView):
    def __init__(self, *args, **kwargs):
        pass

    def get(self, id=None):
        """
        This endpoint is purely meant as an example.
        It will return a simple message with some request information. That is it.
        You may send parameter `id` if you like.
        ---
        tags:
            - dummy
        parameters:
            - in: path
              name: id
              description: Some ID that will be contained in the response
              schema:
                type: string
                format: uuid
        responses:
            200:
                description: Ok
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/DummyResponse'
        """
        return {
            'message': f'Handling request with id {id} on request {request.url_root} with method {request.method}'
        }

    def post(self, id=None):
        """
        Does nothing wubwubw
        ---
        tags:
            - dummy
        """
        return {
            'message': f'Handling request with id {id} on request {request.url_root} with method {request.method}'
        }

    def patch(self, id=None):
        """
        Does nothing
        ---
        tags:
            - dummy
        """
        return {
            'message': f'Handling request with id {id} on request {request.url_root} with method {request.method}'
        }

    def delete(self, id=None):
        """
        Does nothing
        ---
        tags:
            - dummy
        """
        return {
            'message': f'Handling request with id {id} on request {request.url_root} with method {request.method}'
        }
