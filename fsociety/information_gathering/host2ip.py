from socket import gethostbyname

from fsociety.core.utility import Utility
from fsociety.core.menu import set_readline
from fsociety.core.hosts import get_hosts, add_host


class Host2Ip(Utility):
    def run(self):
        hosts = get_hosts()
        set_readline(hosts)
        user_host = input("\nEnter a host: ").strip()
        if not user_host in hosts:
            add_host(user_host)
        ip = gethostbyname(user_host)
        print(f"\n{user_host} has the IP of {ip}")


host2ip = Host2Ip()
