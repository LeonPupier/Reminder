# Dependencies
import os
import socket
import ctypes
import urllib.request
import urllib.parse
import json

from io import BytesIO
from bottle import route, run, template, request, error
from gtts import gTTS
from pygame import mixer
from tkinter import messagebox
from win10toast import ToastNotifier

# Internal dependencies
from webpages import WebPages

# DPI scaling
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Notification
toaster = ToastNotifier()

# Mixer
mixer.init()
nb_audio = 0

# Software informations
current_version = "v1.1.1"
os.environ["REMINDER_UPDATE"] = "False"

# Get the local ip of the machine
ip = socket.gethostbyname(socket.gethostname())

# When the script is launched
if not os.environ.get('BOTTLE_CHILD'):
	# Displays the server window
	messagebox.showinfo("Reminder information", f"The website to manage the software is accessible by entering http://{ip} in your internet browser.")

# Github repository informations
url = "https://api.github.com/repos/LeonPupier/Reminder/releases"
response = urllib.request.urlopen(url)
release_content = response.read().decode('UTF-8')
json_content = json.loads(release_content)
last_version = json_content[0]["tag_name"]
os.environ["NEW_VERSION"] = last_version

# Software updates
if last_version != current_version:
	os.environ["REMINDER_UPDATE"] = "True"


# Initialisation web pages class
page = WebPages()


# Home page
@route("/", method=("GET", "POST"))
def home():
	return template(page.home())


# Changelog page
@route("/changelog", method=("GET", "POST"))
def changelog():
	return template(page.changelog())


# Send the message
@route("/send_instruction", method="POST")
def send_instruction():
	global nb_audio

	# Get the message and the selected language by the user
	message = request.forms.get("content")
	language = request.forms.get("language")
	nb_reading = request.forms.get("nb_reading")

	# The value has not been provided by the user
	if nb_reading == "":
		nb_reading = 1
	else:
		nb_reading = int(nb_reading)

	try:
		# Provided to Google the message to read
		mp3_fp = BytesIO()
		record = gTTS(text=message, lang=language, slow=False)

		# Save the audio message on the disc
		record.save(f"C:/Windows/Temp/reminder_{nb_audio}.mp3")

		# Play the message
		mixer.music.load(f"C:/Windows/Temp/reminder_{nb_audio}.mp3")
		mixer.music.play(loops=nb_reading)
		nb_audio += 1

		# Display a notification with the message as content
		toaster.show_toast("Reminder: message", message, icon_path="Data/app.ico", duration=20, threaded=True)

		# Page: send data successfully
		return template(page.finish())

	except Exception as e:
		# Debug
		print(e)

		# Page: error in sending data
		return template(page.error())


@error(404)
def error404(error):
	return template(page.error404())


@error(405)
def error405(error):
	return template(page.error405())


# Launch the server
run(server="cheroot", host=ip, port=80, debug=False, reloader=True)

# Uninitialize the mixer after closing the server
mixer.quit()

# Delete all audio messages since the opening of the server
for nb_file in range(nb_audio):
	try:
		os.remove(f"C:/Windows/Temp/reminder_{nb_file}.mp3")
	except FileNotFoundError:
		pass
