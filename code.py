from flask import Flask, request,render_template, redirect
from ipaddress import IPv4Network,IPv4Address

app = Flask(__name__)

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

@app.route('/')
def index():
    return "Ip Converter. Try : /ip?convert=10.10.10.0/24"
@app.route('/ip')
def ip():
	if(type(request.args.get) is not None):
		ips=request.args.get('convert');
		if(',' in ips):
			toReturn=[]
			for ip in ips.split(','):
				toReturn.append(analyzer(ip))
			return ','.join(toReturn)
		else:
			return analyzer(request.args.get('convert'))

@app.errorhandler(404)
def error404(e):
	return "This page doesn't exist"

@app.errorhandler(500)
def error500(e):
	print(e)
	return "<html><body><b>RTFM</b>:) <ul><li>/ip?convert=10.10.10.0/24</li><li>/ip?convert=10.10.10.10-10.10.10.15</li><li>Do not set the <a href='http://wiki.linuxquestions.org/wiki/Host_bits'>hosts bits</a></ul></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=False)
