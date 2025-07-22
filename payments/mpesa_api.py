import requests
import base64
from datetime import datetime
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class MpesaAPIClient:
    def __init__(self):
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET
        self.shortcode = settings.MPESA_SHORTCODE
        self.passkey = settings.MPESA_PASSKEY
        self.callback_url = settings.MPESA_CALLBACK_URL
        self.use_sandbox = settings.MPESA_USE_SANDBOX

        self.auth_url = settings.MPESA_AUTH_URL_SANDBOX if self.use_sandbox else settings.MPESA_AUTH_URL
        self.stk_push_url = settings.MPESA_STK_PUSH_URL_SANDBOX if self.use_sandbox else settings.MPESA_STK_PUSH_URL
        self.query_url = settings.MPESA_QUERY_URL_SANDBOX if self.use_sandbox else settings.MPESA_QUERY_URL

    def _get_access_token(self):
        try:
            auth_string = f"{self.consumer_key}:{self.consumer_secret}"
            headers = {
                'Authorization': f'Basic {base64.b64encode(auth_string.encode()).decode()}'
            }
            response = requests.get(self.auth_url, headers=headers)
            response.raise_for_status()
            return response.json()['access_token']
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting M-Pesa access token: {e}. Response: {e.response.text if e.response else 'N/A'}")
            raise

    def generate_password(self, timestamp):
        data_to_encode = f"{self.shortcode}{self.passkey}{timestamp}"
        encoded_data = base64.b64encode(data_to_encode.encode()).decode()
        return encoded_data

    def initiate_stk_push(self, phone_number, amount, reference, description):
        try:
            access_token = self._get_access_token()
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = self.generate_password(timestamp)

            payload = {
                "BusinessShortCode": self.shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline", 
                "Amount": int(amount),
                "PartyA": phone_number,
                "PartyB": self.shortcode,
                "PhoneNumber": phone_number,
                "CallBackURL": self.callback_url,
                "AccountReference": reference,
                "TransactionDesc": description
            }

            response = requests.post(self.stk_push_url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"STK Push initiated successfully. Response: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error initiating STK Push: {e}. Response: {e.response.text if e.response else 'N/A'}")
            raise

    def query_stk_push_status(self, checkout_request_id):
        try:
            access_token = self._get_access_token()
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = self.generate_password(timestamp)

            payload = {
                "BusinessShortCode": self.shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "CheckoutRequestID": checkout_request_id
            }

            response = requests.post(self.query_url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"STK Push status queried. Response: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying STK Push status: {e}. Response: {e.response.text if e.response else 'N/A'}")
            raise

