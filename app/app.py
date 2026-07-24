from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP Request Duration"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()

    start = time.time()

    time.sleep(random.uniform(0.1, 0.5))

    REQUEST_LATENCY.observe(time.time() - start)

    return "Monitoring Platform is Running"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
