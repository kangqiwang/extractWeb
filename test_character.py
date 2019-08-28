from bs4 import BeautifulSoup, Comment
import re

with open("web.html","r") as f:
    text=f.read()
    f.close()
    
#print(text)

soup = BeautifulSoup(text, 'html.parser')
comments=soup.find_all(string=lambda text:isinstance(text,Comment))
print(comments)

for j in soup.find_all(string=lambda text:isinstance(text,Comment)):
    j.extract()

for i in soup.find_all(['script','link','style']):
    i.decompose()
#for comment in soup.find_all(text=lambda text:isinstance(text, Comment))
#print(soup.prettify())

file = open("wirete.html","w")
file.write(soup.prettify())
file.close()

with open("wirete.html","r") as f:
    text=f.readlines()
    f.close()

lines = []
for (index, line) in enumerate(text):
    line.splitlines()
    #print(line)
    result=re.findall("Silver Cross Simplifix Car Seat Base",line)
    if(len(result)):
        print('LINE NUMBER :',index,'        ',len(result))
    
    



#print(lines)


#print(soup.prettify())

