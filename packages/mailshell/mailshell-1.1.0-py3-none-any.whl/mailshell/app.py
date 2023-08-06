import sys
from . import helper
from . import mail_shell as mshell


def main():
	ARGS = sys.argv
	if '--version' in ARGS:
		helper.get_version()
	elif '--help' in ARGS or '-h' in ARGS:
		helper.shell_commands()
	else:
		try: mshell.run()
		except KeyboardInterrupt:
			return


if __name__ == '__main__':
	main()

