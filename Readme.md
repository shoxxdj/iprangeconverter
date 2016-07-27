----------
## Ip Range Converter##

A little web service to convert IP range to IP list


----------
How to:

 - Use the docker service :
	 - `docker build -t iprangeconverter .`
	`docker run --rm -it -p 5000:5000 iprangeconverter`
		http://localhost:5000/ip?convert=10.10.10.0/24
 - Use the app directly:
	 - `pip3 install flask ipaddress`
	 - `python3 code.py`
		 http://localhost:5000/ip?convert=10.10.10.0-10.11.10.0
 - Use it as a simple python tool:
	 - `python3 standalone.py 10.10.10.10-10.10.10.15` 

