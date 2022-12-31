from flask import Flask
from bs4 import BeautifulSoup
import requests
import os
import time
#important secrets
token = os.environ['PASSWORD']
# funny imports
print(os.getenv("ASCII"))
#funny logo
url = "https://www.blockmango.com/#/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())


time.sleep(5)
print("Please use uptime robot and use your own project link! :D")
time.sleep(2)
print("looking for clan info")
# background task

app = Flask(__name__)
@app.route('/')
def index():
  return "I'm alive! :D"
if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True,port=8080)