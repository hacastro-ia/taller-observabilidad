from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)
visits = Counter('webapp_visits_total', 'Total visits to the homepage')
active_users = Gauge('webapp_active_users', 'Simulated active users')

@app.route("/")
def hello():
    visits.inc()
    active_users.set(random.randint(1, 50))
    return "Hello, Prometheus!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
