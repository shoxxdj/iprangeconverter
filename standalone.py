import sys
from ipaddress import IPv4Network,IPv4Address

def rangeFormat(ip):
        results=[]
import sys
from ipaddress import IPv4Network,IPv4Address

def rangeFormat(ip):
        results=[]
        for addr in IPv4Network(ip):
                results.append(str(addr))
        return ','.join(results)

def listFormat(iplist):
        results=[]
        iplist=iplist.split('-')
        lowIp=iplist[0]
        highIp=iplist[1]
        lowValue=int(IPv4Address(lowIp))
        highValue=int(IPv4Address(highIp))

        for value in range(lowValue,highValue+1):
                results.append(str(IPv4Address(value)))
        return ','.join(results)

def analyzer(ip):
        if "/" in ip:
                return rangeFormat(ip)
        elif "-" in ip:
                return listFormat(ip)
        else:
                return ip

if __name__ == '__main__':
    if(len(sys.argv)>1):
        print(analyzer(sys.argv[1]))
