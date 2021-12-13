import hashlib
import itertools
import urllib.request
import re
# pool of characters to search
charpool : str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# target hash
target = ""
with open("../data/targethash.txt", "r") as fp:
    target = fp.readlines()[0].replace("\n","")

# all possible combinations with repetition
pwd_length = 4
prod = itertools.product(charpool, repeat=pwd_length)
result = ''
for i in prod:
    t_str = "".join(i)
    if hashlib.md5(t_str.encode("ascii")).hexdigest() == target:
        result = t_str
        break

tinylink = f'https://tiny.utk.edu/{result}'

# we'll get the final url, to get a bit of info about where the data comes from
urlafterredirect = urllib.request.urlopen(tinylink).geturl()
print(urlafterredirect)
# get the html from the webpage and save it
sitehtml = urllib.request.urlretrieve(tinylink, "../data/htmlresult.html")
# open that as a string, saves a bit of encode decode headache
sitehtmlstr = ''
with open("../data/htmlresult.html", "r") as fp:
    sitehtmlstr = ".".join(fp.readlines())
# seems it's a gist, regex to find the raw path
downloadpath = urlafterredirect + "/" + re.findall("href=.+/(raw.+?)\"", sitehtmlstr)[0]

print(downloadpath)
# download and save the data
rawdat = urllib.request.urlretrieve(downloadpath, "../data/FourVectorTest.csv")