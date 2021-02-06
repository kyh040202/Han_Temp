import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
webpage = requests.get("https://hangang.life/", headers = headers)
soup = BeautifulSoup(webpage.content, "html.parser")
temp = soup.b.text


print('오늘의 한강 수온은 '+temp+'입니다.')