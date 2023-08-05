import requests
import time

def get(url, params={}, headers=None, session=None):
    try:
        response = None
        if headers != None:
            if session == None:
                response = requests.get(url=url, params=params, headers=headers, timeout=120)
            else:
                response = session.get(url=url, params=params, headers=headers, timeout=120)
        else:
            if session == None:
                response = requests.get(url=url, params=params, timeout=120)
            else:
                response = session.get(url=url, params=params, timeout=120)
        if response.status_code != 200:
            print("Warning! response.status_code:", response.status_code, "- will retry")
            return get(url, params, headers, session)
        return response
    except requests.exceptions.ConnectionError as e:
        print("requests.exceptions.ConnectionError")
        print(e)
        print(session)
        print(url)
        print(params)
        print(headers)
        print("sleeping and retrying, WTF")
        time.sleep(60)
        return get(url, params, headers, session)
    except requests.exceptions.ReadTimeout as e:
        print(requests.exceptions.ReadTimeout)
        time.sleep(60)
        return get(url, params, headers, session)
    raise "impossible"

def post(url, params={}, headers=None, session=None):
    try:
        response = None
        if headers != None:
            if session == None:
                response = requests.post(url=url, data=params, headers=headers, timeout=120)
            else:
                response = session.post(url=url, data=params, headers=headers, timeout=120)
        else:
            if session == None:
                response = requests.post(url=url, data=params, timeout=120)
            else:
                response = session.post(url=url, data=params, timeout=120)
        if response.status_code != 200:
            print("Warning! response.status_code:", response.status_code, "- will retry")
            return post(url, params, headers, session)
        return response
    except requests.exceptions.ConnectionError as e:
        print("requests.exceptions.ConnectionError")
        print(e)
        print(session)
        print(url)
        print(params)
        print(headers)
        print("sleeping and retrying, WTF")
        time.sleep(60)
        return post(url, params, headers, session)
    except requests.exceptions.ReadTimeout as e:
        print(requests.exceptions.ReadTimeout)
        time.sleep(60)
        return post(url, params, headers, session)
    raise "impossible"

