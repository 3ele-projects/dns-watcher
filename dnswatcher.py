import dns.resolver
import urllib.request
from time import sleep

import argparse
class DNSChecker():
    def __init__(self,refresh, threshold) :
        global my_resolver
        global nameserver
        target_url = 'https://public-dns.info/nameservers.txt'
        data = urllib.request.urlopen(target_url)
        self.nameserver = []
        self.refresh = refresh
        self.threshold = threshold
        for l in data.read().splitlines():
            
            try:
                dns.resolver.Resolver().nameservers = [l.decode('utf-8')]
                self.nameserver.append(l.decode('utf-8'))
               
            except:
                pass
    
    def check_domain(self, domain, ip):
        c_nameserver = len(self.nameserver)
        t = 0
        while True:
            i = 0
            
            for nameserver in self.nameserver:
                
                dns.resolver.Resolver().nameservers = [nameserver]
                answer = dns.resolver.Resolver().resolve(domain)
                for a in answer:
                #    print (str(i) +'/' +str(c_nameserver))
                    new_ip = a.to_text()
                    if(ip == new_ip):
                        #return True
                        t = t +1
                        if ( t / (c_nameserver / 100) >  self.threshold):
                            return True 

                      #  if((t / (c_nameserver / 100) )
                    #else:
                i = i+1
            sleep(self.refresh)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='root_path')
    parser.add_argument('domain', metavar='d',nargs='?', type=str,
                        help='domain')
    parser.add_argument('ip', nargs='?', metavar='i', type=str,
                        help='ip')

    parser.add_argument('refresh', nargs='?', metavar='r', type=int,
                        help='refresh')

    parser.add_argument('threshold', nargs='?', metavar='t', type=int,
                        help='threshold')

    args = parser.parse_args()
    runner = DNSChecker(args.refresh, args.threshold)
    print (runner.check_domain(args.domain, args.ip))

#Example:
#python3 check_dns_change.py example.org example.org 10 80
