#!/usr/bin/env python

'''This module interacts with the digitalX Direct liquidity provision API located at https://api.direct.digitalx.com/v0.
   Please direct any questions or concerns to neel@digitalx.com'''

import httplib
import hashlib
import hmac
import json
import base64
import time


key = ""
secret = ""

def get_price():
    params = {}
    params['method'] = 'price'
    params['nonce'] = int(time.time())
    params['side'] = 'buy'

    p = base64.standard_b64encode(json.dumps(params))
    h = hmac.new(secret, p, hashlib.sha256)
    signature = h.hexdigest()

    headers = {        "X-DIGITALX-KEY": key,
                       "X-DIGITALX-SIGNATURE": signature,
                       "X-DIGITALX-PARAMS": p}

    conn = httplib.HTTPSConnection("api.direct.digitalx.com")
    conn.request("POST", "/v0/price", {}, headers)
    response = conn.getresponse()
    info = json.load(response)
    return info


def get_status():
    params = {}
    params['method'] = 'status'
    params['nonce'] = int(time.time())

    p = base64.standard_b64encode(json.dumps(params))
    h = hmac.new(secret, p, hashlib.sha256)
    signature = h.hexdigest()

    headers = {        "X-DIGITALX-KEY": key,
                       "X-DIGITALX-SIGNATURE": signature,
                       "X-DIGITALX-PARAMS": p}

    conn = httplib.HTTPSConnection("api.direct.digitalx.com")
    conn.request("POST", "/v0/status", {}, headers)
    response = conn.getresponse()
    info = json.load(response)
    return info


def order(price, amount):
    params = {}
    params['method'] = 'order'
    params['nonce'] = int(time.time())
    params['price'] = price
    params['amount'] = amount
    params['side'] = 'buy'

    p = base64.standard_b64encode(json.dumps(params))
    h = hmac.new(secret, p, hashlib.sha256)
    signature = h.hexdigest()

    headers = {        "X-DIGITALX-KEY": key,
                       "X-DIGITALX-SIGNATURE": signature,
                       "X-DIGITALX-PARAMS": p}

    conn = httplib.HTTPSConnection("api.direct.digitalx.com")
    conn.request("POST", "/v0/order", {}, headers)
    response = conn.getresponse()
    info = json.load(response)
    return info


def get_invoice():
    params = {}
    params['method'] = 'invoice'
    params['nonce'] = int(time.time())

    p = base64.standard_b64encode(json.dumps(params))
    h = hmac.new(secret, p, hashlib.sha256)
    signature = h.hexdigest()

    headers = {        "X-DIGITALX-KEY": key,
                       "X-DIGITALX-SIGNATURE": signature,
                       "X-DIGITALX-PARAMS": p}

    conn = httplib.HTTPSConnection("api.direct.digitalx.com")
    conn.request("POST", "/v0/invoice", {}, headers)
    response = conn.getresponse()
    info = json.load(response)
    return info

def get_transaction(name, tx_id):
    params = {}
    params['method'] = 'transaction'
    params['nonce'] = int(time.time())
    params['tx_id'] = tx_id

    p = base64.standard_b64encode(json.dumps(params))
    h = hmac.new(secret, p, hashlib.sha256)
    signature = h.hexdigest()

    headers = {        "X-DIGITALX-KEY": key,
                       "X-DIGITALX-SIGNATURE": signature,
                       "X-DIGITALX-PARAMS": p}

    conn = httplib.HTTPSConnection("api.direct.digitalx.com")
    conn.request("POST", "/v0/transaction", {}, headers)
    response = conn.getresponse()
    info = json.load(response)
    return info
