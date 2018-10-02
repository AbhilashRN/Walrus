from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
import json
import urllib.request




def get_soup(url,header):
    request = urllib.request.Request(url, headers=header)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    return BeautifulSoup(response,'html.parser')


query = input("query image")# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


print('Wooho')

ActualImages=[]# contains the link for Large original images, type of  image
for ind, a in enumerate(soup.find_all("div",{"class":"rg_meta"})):
    if ind > 0:
        break
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))


if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images

(img, Type) = ActualImages[0]
print(img)
urllib.request.urlretrieve(img, "abcd.jpg")

print('GGGGG')

'''
for i , (img , Type) in enumerate( ActualImages):
    try:
        
        print(img)
        urllib.request.urlretrieve(img, "abcd.jpg")
        


        request = urllib.request.Request(img, {'User-Agent' : header})
        opener = urllib.request.build_opener()

        print(opener)
        response = opener.open(request)
        raw_img = ''
        print(raw_img)

        print(type(raw_img))
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print(cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : "+img)
        print(e)

'''