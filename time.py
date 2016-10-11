from flask import Flask
app = Flask(__name__)
from app import views
from datetime import datetime

@app.route('/')
@app.route('/time')

def time():
    utcTime = datetime.utcnow()
    return (str((utcTime-datetime(1970,1,1)).total_seconds()) + " seconds have passed since January 1, 1970!")

if __name__ == "__main__":
    app.run()

#References
#http://stackoverflow.com/questions/15940280/how-to-get-utc-time-in-python
