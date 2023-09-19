# Host Response Checker v1.0 by Wannazid 
import ssl
import requests
import argparse
import socket
import random
import os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

class HostResponse:
    def __init__(self, target, user_agent, proxy, is_multi=False):
        self.target = target
        self.user_agent = user_agent
        self.proxy = proxy
        self.is_multi = is_multi
        self.Result()

    def Subdomain(self):
        try:
            Agents = {'User-Agent': self.user_agent}
            api = f'https://rapiddns.io/subdomain/{self.target}?full=1&down=0'
            r = requests.get(api, headers=Agents).text
            bs = BeautifulSoup(r, 'html.parser')
            tbody = bs.find('tbody')
            if tbody:
                _tr = tbody.find_all('tr')
                rd = set()
                for pilla in _tr:
                    results = pilla.find('td').text
                    lists = results.split()
                    rd.update(lists)
                ls = list(rd)
                for end in ls:
                    open('domain.txt', 'a').write(end + '\n')
        except Exception as e:
            print(f'[!] Error: {e}')

    def Serverheader(self, domain):
        try:
            proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
            if not domain.startswith('https://'):
                domain = "https://" + domain
            req = requests.get(domain, timeout=4, headers={'User-Agent': self.user_agent}, proxies=proxies)
            server = req.headers.get('Server')
            return server
        except:
            pass

    def Statusheader(self, domain):
        try:
            proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
            if not domain.startswith('https://'):
                domain = "https://" + domain
            req = requests.get(domain, timeout=4, headers={'User-Agent': self.user_agent}, proxies=proxies)
            scode = req.status_code
            return scode
        except:
            pass

    def OpenPort(self, domain, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((domain, port))
            return result == 0
        except Exception:
            return False

    def Protocol(self, domain):
        try:
            with socket.create_connection((domain, 443), timeout=4) as sock:
                with ssl.create_default_context().wrap_socket(sock, server_hostname=domain) as sni_socket:
                    protocol_version = sni_socket.version()
                    return protocol_version
        except:
            pass

    def Result(self):
        subdo = self.Subdomain()
        files = open('domain.txt', 'r').read().splitlines()
        for data in files:
            server = self.Serverheader(data)
            status = self.Statusheader(data)
            protocol = self.Protocol(data)
            ports_to_try = [80, 443]
            open_ports = []
            for port in ports_to_try:
                if self.OpenPort(data, port):
                    open_ports.append(str(port))
            open_ports_str = ','.join(open_ports)
            result = f"{data}|{status}|{server}|{open_ports_str}|{protocol}|"
            print(f"[*] {result}")
            open(args.result, 'a').write(result + '\n')
        os.remove('domain.txt')

class Agent:
    def __init__(self):
        self.useragent()

    def useragent(self):
        ua = open('user-agents.txt', 'r').read().splitlines()
        return random.choice(ua)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='[!] Bug Host Checker - Help you find the bug provider')
    parser.add_argument('-s', '--single', metavar='', type=str, help='Single target / domain / ip')
    parser.add_argument('-m', '--multi', metavar='', type=str, help='Multi target / domain / ip')
    parser.add_argument('-r', '--result', metavar='', type=str, help='Save bug result in files txt')
    parser.add_argument('-proxy', '--proxy', metavar='', type=str, help='Proxy')
    args = parser.parse_args()
    if args.single:
    	message = f"single target site: {args.single}"
    elif args.multi:
    	message = f"multi target files: {args.multi}"
    	
    if args.proxy:
    	messages = f"Use proxy {args.proxy}"
    else:
    	messages = f"Not use proxy"
    banner = f'''

   __ __         __    ___                                
  / // /__  ___ / /_  / _ \___ ___ ___  ___  ___  ___ ___ 
 / _  / _ \(_-</ __/ / , _/ -_|_-</ _ \/ _ \/ _ \(_-</ -_)
/_//_/\___/___/\__/ /_/|_|\__/___/ .__/\___/_//_/___/\__/ 
                                /_/             V.1.0
    
         By : Wannazid
         Github : github.com/wannazid
         Blog : www.malastech.my.id
         
    [!] Checking {message}
    [!] Proxy : {messages}
    [!] Saving files : {args.result}
    '''
    print(banner)
    try:
        if args.single:
            target = args.single
            agent = Agent()
            user_agent = agent.useragent()
            proxy = args.proxy if args.proxy else None
            with ThreadPoolExecutor(max_workers=int(50)) as t:
            	t.submit(HostResponse(target, user_agent, proxy))
        elif args.multi:
            target_list = open(args.multi, 'r').read().splitlines()
            agent = Agent()
            user_agent = agent.useragent()
            proxy = args.proxy if args.proxy else None
            with ThreadPoolExecutor(max_workers=int(50)) as t:
            	[t.submit(HostResponse(target, user_agent, proxy, is_multi=True))for target in target_list]
    except Exception as e:
        print(f'Error: {e}')
