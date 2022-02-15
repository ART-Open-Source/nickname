import requests
import uuid
guuid = uuid.uuid4()


r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"
W = f"{w}\033[1;47m"
B = f"{w}\033[1;44m"
space = "         "
lines = space + "-"*44
pn = f"""
  █████▒ ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██   ▒▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒████ ░░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░▓█▒  ░  ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
░▒█░   ▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
 ▒ ░   ▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
 ░     ░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ░ ░   ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
             ░                  ░ ░      ░ ░      ░  ░      ░  
                     {w}[ FS6.PW ]{b}
                  {d}Tool to change name{w}
               {d}     Author by {w}{r}@u929{w}
"""
ng = "+"	
print(b+pn)
print(f"                {b}print {r}Enter {b}to start{b}")
Username = input(r+"Username: "+g)
Password = input(r+"Password: "+g)
Name = input(r+"Name: "+g)
headers = {
                                "Host": "i.instagram.com",
                                "User-Agent": "Instagram 134.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
                                "Accept": "*/*",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-US",
                                "X-IG-Capabilities": "3brTvw==",
                                "X-IG-Connection-Type": "WIFI",
                                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                'Connection': 'keep-alive'
                        }
d = {
                                'uuid': guuid,
                                'password': Password,
                                'username': Username,
                                'device_id': guuid,
                                'from_reg': 'false',
                                '_csrftoken': 'missing',
                                'login_attempt_countn': '0'
                        }
u = 'https://i.instagram.com/api/v1/accounts/login/'
req = requests.post(u, headers=headers, data=d)
if req.status_code == 200:
                                cookies = req.cookies
                                url = print(f"Login Done @{Username}.")
                                

                                data = {
                                        "first_name": Name
                                        
                                }
                                req = requests.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/", data=data, headers=headers, cookies=cookies).text
                                if 'ok' in req:
                                        print(f"{space}{B} DONE {w} Done Change Your Name")
                                else:
                                        print(f"{space}{B} DONE {r} Error Change Your Name")


