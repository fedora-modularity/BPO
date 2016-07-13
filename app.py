from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return "Hello, I am a Flask app running in Docker on Fedora 24. I have been accessed {hits} times.".format(hits=redis.get('hits'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
