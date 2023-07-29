from bottle import route, run

@route('/')
def home():
    return "Hello from the Python application V2"

run(host='0.0.0.0', port=8081)