# -*- coding: utf-8 -*-
import argparse

from flask import Flask, request
from services.razorpay import Payment, Payout

app = Flask(__name__)


@app.route("/razorpay/status/", methods=["GET"])
def status():
    return "Up & running...", 200


@app.route("/razorpay/link/", methods=["POST"])
def razorpay_create_link():
    return Payment().create_link(request.data)


@app.route("/razorpay/link/<id>/", methods=["GET"])
def payment_status(id):
    return Payment().get_status(id)


@app.route("/razorpay/contact/", methods=["POST"])
def razorpay_create_contact():
    return Payout().create_contact(request.data)


@app.route("/razorpay/account/<id>/", methods=["GET"])
def razorpay_get_account(id):
    return Payout().get_account(id)


@app.route("/razorpay/fund-account/", methods=["POST"])
def razorpay_create_fund_contact():
    return Payout().create_fund_account(request.data)


@app.route("/razorpay/payout/", methods=["POST"])
def razorpay_create_payout():
    return Payout().create_payout(request.data)


@app.route("/razorpay/account/<id>/", methods=["GET"])
def razorpay_get_payout(id):
    return Payout().get_payouts_by_id(id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="Port Number to run the server on, default=5000"
    )
    args = vars(parser.parse_args())
    app.run(debug=True, port=args["port"] or 5000)
