#importing modules
from bs4 import BeautifulSoup, ResultSet
import requests
import urllib.request
import urllib.parse
import PIL
from PIL import Image
from lxml import html
from io import BytesIO

link_used = requests.get('https://www.guru99.com/must-know-linux-commands.html')
page_contents = link_used.text
doc = BeautifulSoup(page_contents, 'html.parser')
ads= doc.find_all('div', {'class': 'sponsorship-message'})
for ad in ads:
    text_ads = ad.find('div', {'class': 'blurb'}).text
    # print(text_ads)
    action_button = ad.find('a', {'class': 'btn btn-primary'}).text
    # print(action_button)
    ad_title = ad.find('div', {'class': 'title'}).text
    # print(ad_title)
    img = ad.div.a.img['data-lazy-src']
    # print(img)
    urllib.request.urlretrieve(
    img,
     "ad_img.png")
    img = Image.open("ad_img.png")
    img.show()



    print(f'''
    Title of Ad: {ad_title}
    Text inside the Ad: {text_ads}
    Call to action Button: {action_button}
    Logo of Ad: **opened in system image viewer**



    ''')





