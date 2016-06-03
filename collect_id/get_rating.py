import requests
from bs4 import BeautifulSoup

def get_bc_rating(username):
    r = requests.get("http://bestcoder.hdu.edu.cn/rating.php?user=" + username)
    bsObj = BeautifulSoup(r.text,"lxml")
    #print(r.text)
    num = 0
    for item in bsObj.findAll("span",{"class":"bigggger"}):
        num += 1
        if num == 1:
            continue
        return item.get_text()
    return "0"
def get_cf_rating(username):
    r = requests.get("http://codeforces.com/profile/"+username)
    bsObj = BeautifulSoup(r.text,"lxml")
    #print(r.text)
    for item in bsObj.findAll("span",{"style":"font-weight:bold;"}):
        return item.get_text()
    return "0"


if __name__ == "__main__":
    bc_username = input("please input bc_username:")
    cf_username = input("please input cf_username:")
    bc_rating = get_bc_rating(bc_username)
    cf_rating = get_cf_rating(cf_username)
    print(bc_username + "\'s bc_rating is " + bc_rating)
    print(cf_username + "\'s cf_rating is " + cf_rating)