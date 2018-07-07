#Load up the app
from organdonationwebapp import app

# Launching server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
