import webbrowser, sys, pyperclip
pyperclip.copy('hello, it\'s me')
if len(sys.argv) > 1:
	address = '+'.join(sys.argv[1:])
else:
	address = pyperclip.paste()
webbrowser.open('https://www.google.com')
webbrowser.open('https://www.youtube.com')
webbrowser.open_new('https://mail.google.com')
webbrowser.open('https://www.fxp.co.il')
webbrowser.get('mozzila')
webbrowser.open('https://www.google.com')


webbrowser.open('https://www.facebook.com')