import requests
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Get your IP address')
    parser.add_argument('-u', '--url', type=str, help='URL to get the IP address')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print the headers')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    r=None
    if args.url:
        r=requests.get(args.url)
        if r.status_code == requests.codes.ok:
            res = r.json()
            print(f'Your IP is {res["ip"]}')
    if args.verbose:
        print(f'{r.headers}')
        print(f'{r.content}')
        
