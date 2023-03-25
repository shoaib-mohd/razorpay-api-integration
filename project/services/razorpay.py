# -*- coding: utf-8 -*-
import json

import requests
from settings.logging import logger


class Payment:
    def __init__(self):
        self.payment_link = "https://api.razorpay.com/v1/payment_links"
        self.key_id = "rzp_test_DnwuSeunt0n5aa"
        self.key_secret = "p4uyvFH8t8Ktnmc0UHXunIAk"
        # for more information: https://razorpay.com/docs/api/

    def create_link(self, payload):
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
        data = json.loads(payload)

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


class Payout:
    def __init__(self):
        self.contact_url = "https://api.razorpay.com/v1/contacts"
        self.fund_account_url = "https://api.razorpay.com/v1/fund_accounts"
        self.payout_url = "https://api.razorpay.com/v1/payouts"
        self.key_id = "rzp_test_DnwuSeunt0n5aa"
        self.key_secret = "p4uyvFH8t8Ktnmc0UHXunIAk"

        self.headers = {
            "content-type": "application/json",
        }

    def create_contact(self, payload):
        '''
        {
            "name": "John Smith",
            }
        '''

        data = json.loads(payload)

        if not data.get("name"):
            return {"message": "name not found"}, 400

        response = requests.post(
            url=self.contact_url,
            json=data,
            auth=(self.key_id, self.key_secret),
            headers=self.headers,
            timeout=5,
        )
        res = response.json()

        logger.info(
            "Razorpay response while creating account \
                url: %s payload: %s status code: %s response: %s headers: %s",
            self.contact_url,
            data,
            response.status_code,
            res,
            self.headers,
        )

        if response.status_code in (200, 201):
            return res
        return {
            "message": res.get("error").get("description"),
            "status_code": response.status_code,
        }

    def get_account(self, account_id):
        url = f"{self.contact_url}/{account_id}/"
        response = requests.get(
            url=url, auth=(self.key_id, self.key_secret), timeout=30
        )
        res = json.loads(response.text)
        logger.info("Razorpay get account by id response: %s", res)
        return res

    def create_fund_account(self, payload):
        '''
        {
            "contact_id": "cont_LVl51VT2L1IYUF",
            "account_type": "bank_account",
            "bank_account": {
                "name": "Gaurav Kumar",
                "ifsc": "HDFC0000053",
                "account_number": "765432123456789"
            }
        }
        '''

        data = json.loads(payload)
        if not data.get("contact_id"):
            return {"message": "Contact id not found"}, 400
        if not data.get("account_type"):
            return {"message": "Account type not found"}, 400

        if not data.get("bank_account"):
            if not data.get("name"):
                return {"message": "Name not found"}, 400
            if not data.get("ifsc"):
                return {"message": "IFSC not found"}, 400
            if not data.get("account_number"):
                return {"message": "Account Number not found"}, 400
            return {"message": "Bank account not found"}, 400

        response = requests.post(
            url=self.fund_account_url,
            json=data,
            auth=(self.key_id, self.key_secret),
            headers=self.headers,
            timeout=5,
        )
        res = response.json()

        logger.info(
            "Razorpay response while creating fund account \
                url: %s payload: %s status code: %s response: %s headers: %s",
            self.fund_account_url,
            data,
            response.status_code,
            res,
            self.headers,
        )
        return res

    def create_payout(self, payload):
        '''
        {
            "account_number": "2323230000078232",
            "fund_account_id": "fa_LVl79XlxWGA8io",
            "amount": 100,
            "currency": "INR",
            "mode": "IMPS",
            "purpose": "refund"
        }
        '''

        data = json.loads(payload)
        if not data.get("account_number"):
            return {"message": "Account number not found"}, 400
        if not data.get("fund_account_id"):
            return {"message": "Fund account id not found"}, 400

        if not data.get("amount"):
            return {"message": "Amount not found"}, 400
        if not data.get("currency"):
            return {"message": "Currency not found"}, 400
        if not data.get("mode"):
            return {"message": "Mode not found"}, 400
        if not data.get("purpose"):
            return {"message": "Purpose not found"}, 400

        response = requests.post(
            url=self.payout_url,
            json=data,
            auth=(self.key_id, self.key_secret),
            headers=self.headers,
            timeout=5,
        )
        res = response.json()

        logger.info(
            "Razorpay response while creating payout \
                url: %s payload: %s status code: %s response: %s headers: %s",
            self.payout_url,
            data,
            response.status_code,
            res,
            self.headers,
        )
        return res

    def get_payouts_by_id(self, payout_id):
        url = f"{self.payout_url}/{payout_id}"
        response = requests.get(url=url, auth=(
            self.key_id, self.key_secret), timeout=3)
        res = json.loads(response.text)
        return res
