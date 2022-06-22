# Dependencies
import os


class WebPages:
	def __init__(self):
		# header
		self.start = ['''
		<!doctype html>
		<html lang="fr">
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=0.86, maximum-scale=0.86, minimum-scale=0.86">
			<link rel="stylesheet" href="css/A.ionicons.min.css+style.css,Mcc.YiYFYaEqvX.css.pagespeed.cf.68ze2mrKvq.css" />
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300&display=swap" rel="stylesheet">
		</head>
		
		<link rel="icon" type="image/png" href="https://cdn-icons-png.flaticon.com/512/1059/1059167.png"/>
		<title>Reminder</title>
		
		<style>		
		html, body {
			overflow-x: hidden;
		}
		
		body {
			background-image: url('https://images.hdqwalls.com/download/clubber-abstract-4k-6e-1920x1080.jpg');
			background-repeat: no-repeat;
			background-attachment: fixed;
			background-size: 100% 100%;
		}
		
		h1, h2, p, a {
			font-family: 'Nunito', sans-serif;
		}
		
		h1, h2, h3 {
			color: white;
			text-shadow: 1px 1px 2px black;
		}
		
		.center {
			position:absolute;
			top:30%;
			right:0;
			left:0;
		}
		
		button, .button {
			font-family: 'Nunito', sans-serif;
			display: inline-block;
			outline: 0;
			cursor: pointer;
			border: none;
			padding: 0 10px;
			height: 40px;
			line-height: 40px;
			border-radius: 7px;
			background-color: #1648CD;
			color: white;
			font-weight: 400;
			font-size: 15px;
			transition: background 0.2s ease,color 0.2s ease,box-shadow 0.2s ease;
		}
			
		button:hover, .button:hover{
			box-shadow: 0 6px 20px #1648CD;
		}
		
		.button_changelog {
			position: absolute;
		}
		</style>
		
		<a href="/changelog">
			<button type="button" class="button_changelog">📜 News</button>
		</a>
		''']

		self.start.append('''
		<center>
		<h1>- Reminder -</h1>
		
		<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script>
		<script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#1648CD', 'V7V5C9VK8');kofiwidget2.draw();</script>
		''')

		if os.environ["REMINDER_UPDATE"] == "True":
			self.start.append(f'''
			<p style="color: white; font-size:2vh;">
			🌐
			<a style="color: #8532A9;" href="https://github.com/LeonPupier/Reminder/releases/latest">
			<b>A new update is available ({os.environ["NEW_VERSION"]}).
			</b></a></p>
			''')

		self.start = ''.join(self.start)

		# Footer
		self.end = '''
		</center>
		
		<style>
		.credits{
			position:absolute;
			width:100%;
			bottom:0;
			text-align:center;
		}
		</style>
		
		<div class="credits">
			<p style="color: #D5D5D5;">
			<a style="color: #1648CD;" href="https://leonpupier.fr">leonpupier.fr</a> • <a style="color: #1648CD;" href="https://github.com/LeonPupier/Reminder">github.com</a>
			<br>
			Developed by <i>Léon Pupier</i> - v1.1.1 - All rights reserved.
			</p>
		</div>
		'''

	def home(self):
		# Content of the page
		html = '''
		<style>
		textarea {
			resize: none;
			background-color: rgba(255,255,255,0.9);;
			color: #666666;
			padding: 1em;
			border-radius: 10px;
			border: 2px solid transparent;
			outline: none;
			font-family: "Heebo", sans-serif;
			font-weight: 500;
			font-size: 16px;
			line-height: 1.4;
			transition: all 0.2s;
		}
		
		.number {
			border: 2px solid transparent;
			outline: none;
			border-radius: 5px;
		}
			
		textarea:hover {
			cursor: pointer;
			background-color: #eeeeee;
		}
			
		textarea:focus {
			cursor: text;
			color: #333333;
			background-color: white;
			border-color: #333333;
		}
		
		select {
			border: 1px solid var(--select-border);
			border-radius: 0.25em;
			padding: 0.25em 0.5em;
			font-size: 10;
			cursor: pointer;
			line-height: 1.1;
		}
		</style>
		
		<form class="center" action="send_instruction" accept-charset="ISO-8859-1" method="POST">
			<h2 style="font-size:2vh;">💬 Please provide the message to be transmitted:</h2>
			<textarea name="content" rows="5" cols="45" placeholder="Enter a message..." required></textarea>
			
			</br>
			
			<p style="color: #D5D5D5;">🚩 Voice accent:
			<select name="language"">
				<option value="en">English</option>
				<option value="fr">Français</option>
				<option value="es">Español</option>
				<option value="de">Deutsch</option>
				<option value="ru">Русский</option>
				<option value="zh">中国</option>
				<option value="ja">やまと</option>
			</select>
			🔁 Read:
			<input type="number" class="number" name="nb_reading" min="1" max="10" placeholder="1">
			time(s)
			</p>
			
			<input class="button" type="submit" value="Send the message 📨">
		</form>
		'''

		# Returns a string in the format of an html file
		return ''.join([self.start, html, self.end])

	def finish(self):
		html = '''
		<form class="center" action="/" method="GET">
			<h2>Your instruction has been successfully transmitted.</h2>
			<p style="color: #D5D5D5;">The voice reading of your message has just started.</p>
			
			<br><input class="button" type="submit" value="Return to home page 🏠">
		</form>
		'''

		return ''.join([self.start, html, self.end])

	def changelog(self):
		html = '''
		<style>
		p {
			color: #D5D5D5;
		}
		 
		.myBlock {
			text-align: left;
			border: none;
			padding: 5px;
			font-family: 'Nunito', sans-serif;
			width: 400px;
			height: 350px;
			overflow-y: scroll;
		}
		
		::-webkit-scrollbar {
			width: 15px;
			height: 15px;
		}
		
		::-webkit-scrollbar-track {
			border: 1px solid #1648CD;
			border-radius: 15px;
		}
		
		::-webkit-scrollbar-thumb {
			background: #1648CD;  
			border-radius: 15px;
		}
		
		::-webkit-scrollbar-thumb:hover {
			background: #1648CD;  
		}
		</style>
		
		<h2>📜 Changelog</h2>		
		<div class="myBlock">
			<h3><b>v1.1.1</b></h3>
			<p>
			- Fixed a problem in the detection of updates <br>
			- Corrected application notification icon <br>
			- Fixed server error during notification display <br>
			</p>
			
			<h3><b>v1.1.0</b></h3>
			<p>
			- Added function to replay a given number of times the message <br>
			- Switch to "cheroot" backend to increase performance <br>
			- Detection if a new update is available <br>
			- Change background image <br>
			- Notifications will remain displayed longer, depending on the system configuration <br>
			- The notifications will be visible in the Windows Notifications panel to read them later and keep them in memory <br>
			- Changing the opacity of the text area <br>
			- Minor visual changes <br>
			- Removal of highlighted information <br>
			</p>
			
			<h3><b>v1.0.1</b></h3>
			<p>
			- Addition of a message advising the use of the administrator rights during a problem of sending on the website <br>
			</p>
			
			<h3><b>v1.0.0</b></h3>
			<p>
			- Official launch of the "Reminder" service <br>
			- Added message sending between client and server <br>
			- Messages are transcribed verbally to the recipient <br>
			- Addition of the changelog page <br>
			- Server under "paste" to improve performance <br>
			- 404 and 405 error handling supported <br>
			- Support with Ko-Fi widget <br>
			- Added language accents for: English, French, Spanish, German, Russian, Chinese, Japanese <br>
			- A notification is now displayed when a message arrives <br>
			</p>
		</div>
		
		<br>
		<a href="/">
			<button class="button">Return to home page 🏠</button>
		</a>
		'''

		return ''.join([self.start, html, self.end])

	def error(self):
		html = '''
		<form class="center" action="/" method="GET">
			<h2>❌ An error occurred while sending your instruction...</h2>
			<p style="color: #D5D5D5;">Please try again or check that your message is not empty.</p>
			<p style="color: #D5D5D5;">⚠️ If you still encounter problems, please <b>launch the software in administrator mode</b>.</p>
			<p style="color: #D5D5D5;">The server may also have been turned off...</p>

			<br><input class="button" type="submit" value="Return to home page 🏠">
		</form>
		'''

		return ''.join([self.start, html, self.end])

	def error404(self):
		html = '''
		<form class="center" action="/" method="GET">
			<h2>❌ This page does not exist on the website...</h2>
			<p style="color: #D5D5D5;">You are quite curious to leave the initial path ;)</p>
			<br>
			<input class="button" type="submit" value="Return to home page 🏠">
		</form>
		'''

		return ''.join([self.start, html, self.end])

	def error405(self):
		html = '''
		<form class="center" action="/" method="GET">
			<h2>❌ The method used is not correct...</h2>
			<p style="color: #D5D5D5;">You are trying to access pages managed by the server, I have my eye on you 👀</p>
			<br>
			<input class="button" type="submit" value="Return to home page 🏠">
		</form>
		'''

		return ''.join([self.start, html, self.end])
