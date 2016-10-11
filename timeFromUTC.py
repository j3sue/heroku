from flask import Flask
import sys
app = Flask(__name__)
from datetime import datetime

@app.route('/')
def timeFromUTC():
    utcTime = datetime.utcnow()
    return (str((utcTime-datetime(1970,1,1)).total_seconds()) + " seconds have passed since January 1, 1970!")

if __name__ == "__main__":
    app.run(port = sys.argv[1])

#References
#http://stackoverflow.com/questions/15940280/how-to-get-utc-time-in-python
