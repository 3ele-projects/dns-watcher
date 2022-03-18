from pynotifier import Notification
import argparse
from dnswatcher import DNSChecker 


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

    parser.add_argument('list', nargs='?', metavar='l', type=int,
                        help='list')

    args = parser.parse_args()

    runner = DNSChecker(args.refresh, args.threshold)
    if(runner.check_domain(args.domain, args.ip)):
        Notification(
    title='DNS Resolved' + args.domain,
    description='DNS Resolved' + args.domain + ' ' +args.ip,
 #   icon_path='/absolute/path/to/image/icon.png', # On Windows .ico is required, on Linux - .png
    duration=120,                                   # Duration in seconds
    urgency='normal').send()

                                