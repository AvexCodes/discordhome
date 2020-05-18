# https://api.ksoft.si/images/random-meme
import os
import requests

class KSoft(object):
    api_url = "https://api.ksoft.si"

    @staticmethod
    def meme():
        url = f"{KSoft.api_url}/images/random-meme"
        headers = {'Authorization': 'Bearer {}'.format(os.getenv("ksoftToken"))}
        r = requests.get(url=url, headers=headers)
        r_json = r.json()
        return r_json

    @staticmethod
    def wikihow():
        url = f"{KSoft.api_url}/images/random-wikihow"
        headers = {'Authorization': 'Bearer {}'.format(os.getenv("ksoftToken"))}
        r = requests.get(url=url, headers=headers)
        r_json = r.json()
        return r_json
    
    @staticmethod
    def aww():
        url = f"{KSoft.api_url}/images/random-aww"
        headers = {'Authorization': 'Bearer {}'.format(os.getenv("ksoftToken"))}
        r = requests.get(url=url, headers=headers)
        r_json = r.json()
        return r_json

    @staticmethod
    def convert(to, frm, amount):
        url = f"{KSoft.api_url}/kumo/currency?to={to}&from={frm}&value={amount}"
        headers = {'Authorization': 'Bearer {}'.format(os.getenv("ksoftToken"))}
        r = requests.get(url=url, headers=headers)
        r_json = r.json()
        if r_json.get('pretty') is None:
            return "invalid"
        return r_json

    