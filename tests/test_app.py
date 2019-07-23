from flask import Flask, request

app = Flask(__name__)


with app.test_request_context('/pessoas', method='GET'):
    assert request.path == '/pessoas'
    assert request.method == 'GET'

