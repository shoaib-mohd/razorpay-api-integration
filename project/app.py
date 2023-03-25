# -*- coding: utf-8 -*-
import argparse

from flask import Flask, request
from services.razorpay import Payment

app = Flask(__name__)


@app.route("/razorpay/status/", methods=["GET"])
def status():
    return "Up & running...", 200


@app.route("/razorpay/link/", methods=["POST"])
def razorpay_create_link():
    return Payment().create_link(request.data)


@app.route("/razorpay/status/<id>/", methods=["GET"])
def payment_status(id):
    return Payment().get_status(id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="Port Number to run the server on, default=5000"
    )
    args = vars(parser.parse_args())
    app.run(debug=True, port=args["port"] or 5000)
