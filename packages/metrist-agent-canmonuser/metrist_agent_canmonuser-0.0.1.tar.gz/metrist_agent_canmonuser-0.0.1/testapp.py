import requests
import urllib3
import atexit

from metrist import MetristAgent

agent = MetristAgent()
agent.connect()


http = urllib3.PoolManager()
http.request('GET', 'https://www.google.com/test')

requests.get("https://www.google.com/test")

http = requests.Session()
response = http.get("https://www.google.com/")

