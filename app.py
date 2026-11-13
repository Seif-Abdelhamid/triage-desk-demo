"""Deliberately vulnerable demo app for triage-desk. Do not deploy."""

import hashlib
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    out = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True, text=True)
    return out.stdout


@app.route("/about")
def about():
    body = "triage-desk demo"
    etag = hashlib.md5(body.encode()).hexdigest()  # HTTP cache key, not a security use
    return body, 200, {"ETag": etag}
