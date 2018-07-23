import sys
import logging
from flask import Flask
from flask import request
from time import strftime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		ts = strftime('[%Y-%b-%d %H:%M]')
		app.logger.debug('%s %s', ts, request.url)
		if 'Accept' in request.headers:
			header = request.headers.get('Accept')
			if header == "application/json":
				return '{"message": "Good morning"}'
			else:
				return 'Accept header not set to application/json'
		else:
			return '<p>Hello, World</p>' 
	elif request.method == 'POST':
		ts = strftime('[%Y-%b-%d %H:%M]')
		app.logger.debug('%s %s', ts, request.url)
		return 'POST Request'

if __name__ == '__main__':
	debug_mode = False
	if (len(sys.argv) > 1) and (sys.argv[1] == 'True'):
		debug_mode = True
	app.run(debug=debug_mode, host='0.0.0.0')