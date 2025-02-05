import requests

url = "https://jsonip.com/"
r=requests.get(url)
if r.status_code == requests.codes.ok:
    print(f'{r.headers}')
    print(f'{r.content}')
    res = r.json()
    print(f'Your IP is {res["ip"]}')
