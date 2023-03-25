# Razorpay API Integration


## About

In this project, you can use Razorpay API's to pay and collect the payments with anyone easily.

- APIS
    - Root URL: /razorpay/status/

Payments API's
    - Root URL: /razorpay/link/
    - Root URL: /razorpay/status/<id>/

Payout API's
    - Root URL: /razorpay/contact/
    - Root URL: /razorpay/contact/<id>/
    - Root URL: /razorpay/fund-account/
    - Root URL: /razorpay/payout/
    - Root URL: /razorpay/account/<id>/


## Paylod

```json
{
    "amount": "integer Amount to be paid using the Payment Link. Must be in the smallest unit of the currency. For example, if you want to receive a payment of ₹300.00, you must enter the value 30000.",
    "customer": {
        "contact": "string The customer's phone number."
    },
    "notify": {
        "sms": "boolean Defines who handles the SMS notification. true - Razorpay handles the notification. false - You handle the notification."
    }
}
```

### Project Start Guide:

- First of all, clone the project
- Install the dependencies by using ""pip install -r requirements.txt" command
- "python project/app.py" command to start the project
- Then you can use the project api's and integrate in your project as well.
