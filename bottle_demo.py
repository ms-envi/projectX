from bottle import get, post, request, run

@get('/hello')
def hello():
    return {"Hellloooo":1,
            "Helo":2}

run(host='localhost', port=8000, debug=True)
