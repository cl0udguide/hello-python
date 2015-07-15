import os			# import os-specific commands
import uuid			# uuid module - generating unique ids
from flask import Flask		# framework for quickly and easily building websites
app = Flask(__name__)		# initialize web server
my_uuid = str(uuid.uuid1())	# create new unique id each time
BLUE = "#0000FF"		# const color code blue
GREEN = "#33CC33"
counter = 0

COLOR = BLUE

@app.route('/')			# lines 11-23 - function; if webserver receives root, then handle that with this function
def hello():
	global counter
	counter = counter+1

	return """
	<html>
	<body bgcolor="{}">

	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
	<br/>
	Count: {}
	</center>

	</body>
	</html>
	""".format(COLOR,my_uuid,counter)

if __name__ == "__main__":	# "pythinism" not required
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))	# run webserver, listen on every address on the port env def port or 5000 if cannot find it
