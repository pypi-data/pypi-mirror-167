import os
import imaplib, email

def check(user):
	IMAP_SERVER = "imap.gmail.com"

	print("Connecting..")
	with imaplib.IMAP4_SSL(IMAP_SERVER) as imap:
		imap.login(user.address, user.app_password)
		box = input("mailbox: ").strip().title()
		for b in imap.list()[1]:
			if box == 'Inbox': break
			b = b.decode().split(' "/" ')
			if box in b[1]:
				box = b[1] 
				break
		else:
			print("This box does not exist!")
			return

		imap.select(box)
		CRI = input("Search command: ").strip()
		try:
			_, msgnums = imap.search(None, CRI)
		except Exception:
			print("\nInvalid command: type 'sch' to see the email search commands.\n")
			return
		if not msgnums[0]:
			print("No search results in this mail box.")
			return
		for num in msgnums[0].split():
			_, data = imap.fetch(num, "(RFC822)")
			message = email.message_from_bytes(data[0][1])
			print("\nFrom:", message.get('From'))
			print("To:", message.get('To'))
			print("Date:", message.get('Date'))
			body = "\n"
			if message.is_multipart():
				for part in message.walk():
					ctype = part.get_content_type()
					cdispo = str(part.get('Content-Disposition'))
					if ctype == 'text/plain' and 'attachment' not in cdispo:
						body += part.get_payload(decode=False)
						break
			else:
				body += message.get_payload(decode=False)
			print(body)
			print(f"\x1b[33m{'-' * 50}\x1b[0m")


