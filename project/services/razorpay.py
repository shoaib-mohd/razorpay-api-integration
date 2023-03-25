# -*- coding: utf-8 -*-
import json

import requests
from settings.logging import logger


class Payment:
    def __init__(self):
        self.payment_link = "https://api.razorpay.com/v1/payment_links"
        self.key_id = "rzp_test_DnwuSeunt0n5aa"
        self.key_secret = "p4uyvFH8t8Ktnmc0UHXunIAk"

    def create_link(self, req):
        '''
        {
            "amount": 1000,
            "customer": {
                "contact": "+91XXXXXXXXXX"
            },
            "notify": {
                "sms": true
            }
        }
        '''
        data = json.loads(req)

        if not data.get("amount"):
            return {"message": "amount not found"}, 400
        if not data.get("customer"):
            if not data.get("customer").get("contact"):
                return {"message": "customer contact not found"}, 400
            return {"message": "customer not found"}, 400

        headers = {
            "content-type": "application/json",
        }

        response = requests.post(
            url=self.payment_link, json=data,
            auth=(self.key_id, self.key_secret), headers=headers, timeout=30
        )

        res = json.loads(response.text)

        logger.info(
            "Razorpay response while creating payment link \
                url: %s payload: %s status code: %s response: %s headers: %s",
            self.payment_link,
            data,
            response.status_code,
            res,
            headers,
        )

        if response.status_code == 200:
            return res
        return {
            "message": res.get("error").get("description"),
            "status_code": response.status_code,
        }

    def get_status(self, id):

        url = f"{self.payment_link}/{id}"
        response = requests.get(url=url, auth=(
            self.key_id, self.key_secret), timeout=30)
        res = json.loads(response.text)
        return res
