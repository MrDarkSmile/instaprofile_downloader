import os
try:
  import instaloader
  from colorama import init , Fore
except:
  os.system("pip install instaloader colorama")
  import instaloader
  from colorama import init , Fore


#clear screen
os.system("clear")

#print about
banner = """
_           _                _
(_)_ __  ___| |_ __ _   _ __ (_) ___
| | '_ \/ __| __/ _` | | '_ \| |/ __|
| | | | \__ \ || (_| | | |_) | | (__
|_|_| |_|___/\__\__,_| | .__/|_|\___|
                       |_|
"""
print(Fore.LIGHTRED_EX+banner)
print(Fore.LIGHTMAGENTA_EX+"Created By: MrDarkSmile GitHub")


#get username
username = str(input(Fore.LIGHTCYAN_EX+"enter username : "+Fore.GREEN))
print(Fore.LIGHTYELLOW_EX+"loading...")

#download profile
loader = instaloader.Instaloader()
loader.download_profile(username, profile_pic_only = True)

#set name of file
img = [x for x in os.listdir(f'./{username}') if x.endswith('jpg')]
img = f'./{username}/{img[0]}'
with open(img,"rb") as f:
  data = f.read()
  with open(username+".jpg","wb") as file:
    file.write(data)
    
#clear cache
os.system(str(f"rm -rf {username}"))

#finish
print(Fore.LIGHTGREEN_EX+str(f"[~]profile with name : {username}.jpg was saved"))
