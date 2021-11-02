from bs4 import BeautifulSoup as bs
import requests
url = "https://www.geeksforgeeks.org/must-coding-questions-company-wise/"
page = requests.get(url)    
data = page.text
soup = bs(data)
s=[]
for link in soup.find_all('a'):
    b=link.get('href')
    try:
         if'problems' in b:
                s.append(b)
    except Exception as e:
        print(e)
file={}
file['data']=[]
def ques(url):
    r=requests.get(url)
    soup=bs(r.content)
    s1=[]
    for p in soup.find_all('p'):
        s1.append(p.text)
        if len(s1)>=6:
            break
    try:
        s1[4].replace("\xa0","")
        x={
            "link":url,
            "text":s1[4]
        }
        
        file['data'].append(x)
    except Exception as e:
        print(e)
for i in range(len(s)):
    ques(s[i])
with open("coding_qustion.json", "w") as outfile:
    json.dump(file,outfile,indent = 4)