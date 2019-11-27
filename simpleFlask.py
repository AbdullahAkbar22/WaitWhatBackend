from flask import request, Flask
from requests import get

parseTestApp = Flask(__name__)

@parseTestApp.route('/')
def hello_world():
	return 'Reddit test running'
	
if __name__ == '__main__':
	parseTestApp.run(host='0.0.0.0', port=8080)