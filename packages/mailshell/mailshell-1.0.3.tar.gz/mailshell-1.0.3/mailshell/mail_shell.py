import sys, os
import requests
from . import helper
from . import email_logo
import smtplib, socket
import csv, re, imghdr
from pathlib import Path
from os.path import exists
from os.path import basename
from getpass import getuser
from subprocess import call
from . import mail_checker as mc
from email.message import EmailMessage
from tempfile import NamedTemporaryFile


PORT = 465
SMTP_SERVER = "smtp.gmail.com"
CREDENTIALS_FILE = (Path(__file__).parent / "credentials.csv")
MESSAGE_STR = " Your message ".center(14 + 15 * 2, '=')
EMAIL_PATTERN = r"^\s*[\w\._%+-]+@[\w\.-]+\.\w+\s*$"
SEND_TO_STR = r"//↓↓↓↓ Send to ↓↓↓↓\\"


def update_warning():
	response = requests.get("https://pypi.org/pypi/mailshell/json")
	current_vertion = response.json()['info']['version']
	if helper.VERSION == current_vertion:
		return ''
	warning = f"\n\x1b[33mWARNING: new version available [{current_version}]\n"
	warning += "run 'pip3 install -U mailshell' to update.\x1b[0m"
	return warning

def validate_email(address):
	response = requests.get('https://isitarealemail.com/api/email/validate', params={ 'email': address })
	status = response.json()['status']
	if status == "valid": 
		return True
	return False

def dispaly_logo():
	print(email_logo.LOGO)

def folder_ls(folder='.'):
	for f in os.listdir(folder):
		if f.startswith('.'): continue
		if os.path.isdir(folder + '/' + f): f += '/'
		print(f, end='   ')
	print()

def print_work_directory():
	print(os.getcwd())

clear = lambda: os.system('clear')

class User(object):
	def __init__(self, address=None, password=None):
		self.address = address
		self.app_password = password

class Mailshell():
	def __init__(self):
		self.user = None
		self.message = None
		self.contacts = {}
		self.commands = {
			"logo": dispaly_logo,
			"login": self.log_in,
			"logout": self.log_out,
			"cred": self.credentials,
			"new": self.new_message,
			"edit": self.edit_message,
			"content": self.show_content,
			"send": self.send_message,
			"to": self.message_to,
			"get": self.get_text,
			"add": self.add_file,
			"rm": self.remove_file,
			"check": self.check_mail_box,
			"sch": self.display_sc,
			"ls": folder_ls,
			"pwd": print_work_directory,
			"clear": clear,
			"help": helper.shell_commands,
			"version": helper.get_version,
			"exit": sys.exit
		}

	def __error_login_first(self):
		print("\nLogin first: type 'login' to start create and send your massages.\n")

	def __error_app_password(self):
		print(
			"\nERROR: Gmail app password is incorrect:\nsee how to create and use gmail app password on:\n    " + 
			"\x1b[33mhttps://support.google.com/accounts/answer/185833?hl=en#app-passwords\x1b[0m\n")

	def __error_create_message(self):
		print("\nYou didn't create a message: type 'new' to create a new massage..\n")
	
	def __error_file_not_found(self, filename):
		print(f"\nERROR: '{filename}' does not exists: " +
			   "type 'ls' to see files and folders in your current directory.\n")

	def __error_connection(self):
		print("\nConnection error: please check your network!\n")

	def __get_multiline_input(self, prefix=''):
		with NamedTemporaryFile(mode='w') as f:
			f.write(prefix)
			f.flush()
			os.fsync(f.fileno())
			with open(f.name, 'r') as tmp:
				call(['nano', tmp.name])
				return tmp.read()

	def log_in(self):
		print('Log in:')
		address = input("Email address: ").strip()
		password = input("App password: ").strip()
		try:
			if validate_email(address):
				try:
					with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
						smtp.login(address, password)
				except smtplib.SMTPAuthenticationError:
					self.__error_app_password()
					return
			else:
				print(f"ERROR: '{address}' does not exist.")
				return
			print(update_warning())
		except Exception:
			self.__error_connection()
			return

		saveIt = input("Do you want to save it [y/n]? ").strip().lower()
		if saveIt == 'y' or saveIt == 'yes':
			with open(CREDENTIALS_FILE, 'w') as f:
				file_writer = csv.writer(f)
				file_writer.writerow([address, password])

		self.user = User(address, password)
		print("\x1b[32mYou have been successfully logged in.\x1b[0m")

	def log_out(self):
		if not self.user:
			print("\nERROR: you have not login yet!\n")
			return
		self.user = None
		os.remove(CREDENTIALS_FILE)
		print("You have logged out.")

	def credentials(self):
		if not self.user:
			self.__error_login_first()
			return
		print("Email address: " + self.user.address)
		print("Email app password: " + self.user.app_password)

	def new_message(self):
		if not self.user:
			self.__error_create_message()
			return
		print("Creating new message:")
		self.message = EmailMessage()
		self.message['Subject'] = input('Subject: ').strip()
		self.message['From'] = self.user.address
		self.message.set_content('')

	def edit_message(self):
		if not self.message:
			self.__error_create_message()
			return
		content = self.message.get_payload()
		if type(content) != str: content = content[0].get_content()
		new_content = self.__get_multiline_input(content)
		if type(self.message.get_payload()) != str:
			self.message.get_payload()[0].set_content(new_content)
			return
		self.message.set_content(new_content)
	
	def get_text(self, file_path=''):
		if not self.message:
			self.__error_create_message()
			return
		if exists(file_path):
			if '.txt' not in basename(file_path):
				print(f"'{file_path}' is not .txt file")
				return
			with open(file_path, 'r') as f:
				content = self.message.get_payload()
				if type(content) != str: 
					content = content[0].get_content()
					self.message.get_payload()[0].set_content(content + f.read())
					return
				self.message.set_content(content + f.read())
		else: 
			__error_file_not_found(file_path)

	def add_file(self, file_path=''):
		if not self.message:
			self.__error_create_message()
			return
		if exists(file_path):
			if os.path.isdir(file_path):
				print(f"\n{file_path} is a folder not file.\n")
				return			
			if imghdr.what(file_path):
				mtype, stype = 'image', imghdr.what(file_path)
			else:
				mtype, stype = 'application', 'octet-stream'
		
			with open(file_path, 'rb') as f:
				self.message.add_attachment(
        			f.read(),
        			maintype=mtype,
        			subtype=stype,
        			filename=basename(f.name)
    			)
		else:
			__error_file_not_found(file_path)

	def remove_file(self, filename=''):
		if not self.message:
			self.__error_create_message()
			return
		if filename:
			for idx, att in enumerate(self.message.get_payload()):
				if att.get_filename() == filename:
					del self.message.get_payload()[idx]
					print(att.get_filename(), "is removed.")
					return
		print(f"ERROR: '{filename}' is not in your message.")

	def show_content(self):
		if not self.message:
			self.__error_create_message()
			return
		content = MESSAGE_STR + '\n'
		content += "Subject: " + self.message['Subject'] + '\n'
		content += "From: " + self.message['From'] + '\n'
		text = self.message.get_payload()
		if type(text) != str: text = text[0].get_content()
		content += text + '\n'
		attachments = list(self.message.iter_attachments())
		if len(attachments):
			content += "- includes:\n"
			for att in attachments: content += '\x1b[33m    ' + att.get_filename() + '\x1b[0m' + '\n'
		content += '-' * len(MESSAGE_STR)
		print(content)
		print("type 'send' to send your message.")

	def check_mail_box(self):
		if not self.user:
			self.__error_login_first()
			return
		try:
			mc.check(self.user)
			print(update_warning())
		except socket.gaierror:
			self.__error_connection()

	def display_sc(self):
		with NamedTemporaryFile(mode='w') as tmp:
			tmp.write(helper.IMAP_CRITERIAS)
			tmp.flush()
			os.fsync(tmp.fileno())
			call(['less', tmp.name])

	def message_to(self):
		pre = SEND_TO_STR + '\n'
		for user in self.contacts: pre += user + '\n'
		result = self.__get_multiline_input(pre)
		matches = re.findall(EMAIL_PATTERN, result, re.MULTILINE)
		if matches:
			self.contacts = set(map(lambda x: x.strip(), matches))
		  
	def send_message(self):
		if not self.message:
			self.__error_create_message()
			return
		self.message_to()
		if not self.contacts:
			print("You have no receivers: type 'to' to set your contacts.")
			return
		try:
			print("Connecting..")
			with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
				smtp.login(self.user.address, self.user.app_password)
				for user in self.contacts:
					print(f"Sending to {user}..")
					if not validate_email(user):
						print(f"\x1b[31m    Error: {user} is not exist.\x1b[0m")
						continue
					self.message['To'] = user
					smtp.send_message(self.message)
					print("\x1b[32m    Email is successfully sent\x1b[0m")
			print(update_warning())
		except socket.gaierror:
			self.__error_connection()
		
	def __getitem__(self, command):
		if command:
			keys = re.split('\s+', command)
			if len(keys) == 1 and keys[0] in self.commands: 
				self.commands[keys[0]]()
				return
			elif keys[0] in ['ls', 'get', 'add', 'rm']: self.commands[keys[0]](keys[1])
			else: print(f"{command}: command not found.")

def shell_line(user):
	if not user: address = ""
	else: address = f"\x1b[31m@\x1b[0m{user.address}"
	username = "\x1b[33m" + getuser()
	return username + address + '\x1b[31m>> \x1b[0m'
	

def run():
	# Startup
	clear()
	dispaly_logo()
	print(f"\x1b[4mWelcome {getuser()}\x1b[0m")
	print("type 'help' to see your available commands.\n")

	SHELL = Mailshell()

	# get the data
	if exists(CREDENTIALS_FILE):
		with open(CREDENTIALS_FILE, 'r') as f:
			credentials = next(csv.reader(f))
			SHELL.user = User(*credentials)

	while True: SHELL[input(shell_line(SHELL.user)).strip()]

