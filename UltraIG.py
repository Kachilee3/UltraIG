import os
import platform
import webbrowser
os.system('termux-setup-storage')

os.system('git pull')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:os.system('mkdir Music')
except:pass
P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("UltraIG").license()
	else:
		print('Your Device Does Not Support This Tool')