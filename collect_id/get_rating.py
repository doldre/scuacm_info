import requests
import re
from bs4 import BeautifulSoup

def get_average(points):
    points = sorted(points,reverse = True)
    sum_points = 0
    num = 0
    for item in points:
        num += 1
        if num > 3:
            break
        sum_points += int(item)
    if num == 0:
        return 0
    if len(points) >= 3:
        average = sum_points / 3
    else:
        average = sum_points / num
    return average

def get_bc_rating(username):
    r = requests.get("http://bestcoder.hdu.edu.cn/recentContests.php?user=" + username)
    bsObj = BeautifulSoup(r.text,"html.parser")
    #print(r.text)
    points = []
    num = 0
    for item in bsObj.findAll("td"):
        text = item.get_text()
        #print(text)
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(text)
        if match:
            #print(text)
            num += 1
            if num % 3 == 0:
                points.append(text)
    average = get_average(points)
    average = int(average)
    return str(average)
def get_cf_rating(username):
    r = requests.get("http://codeforces.com/contests/with/"+username)
    bsObj = BeautifulSoup(r.text,"html.parser")
    #print(r.text)
    points = []
    num = 0
    for item in bsObj.find("div",{"id":"pageContent"}).findAll("td"):
        #print(item)
        text = item.get_text().strip()
        #print(text)
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(text)
        if match:
            #print(text)
            num += 1
            if num % 4 == 0:
                points.append(text)
    #print(points)
    average = get_average(points)
    average = int(average)
    return str(average)


if __name__ == "__main__":
    bc_username = input("please input bc_username:")
    cf_username = input("please input cf_username:")
    bc_rating = get_bc_rating("liujc")
    cf_rating = get_cf_rating("liujc")
    print(bc_username + "\'s bc_rating is " + bc_rating)
    print(cf_username + "\'s cf_rating is " + cf_rating)
