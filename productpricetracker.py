import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
# getting data from website
header={



    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}



response1=requests.get(url="https://www.amazon.com/HP-Pavilion-i7-11370H-Micro-Edge-Anti-Glare/dp/B09NL8JTB6",headers=header)
content=response1.text


soup=BeautifulSoup(content,'html.parser')

print(soup.title)
sd=soup.find(name="span",class_="olpWrappera-size-small")
print(sd)

#converting it to float datatype
curpr=1000
# setting smtplib connection
if curpr<100:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user="ypur mail", password="your app password")
        connection.sendmail(from_addr="your desired mail", to_addrs="user mail",
                            msg=f"subject:alert!\n\n prize drop to your product at {curpr}$ hurry up")









