import time
from selenium import webdriver
import time
import random

username=input("Enter Username: ")

error="https://www.instagram.com/challenge"
insta="https://www.instagram.com/"

driver=webdriver.Chrome()

a = open('acc.txt', "r").readlines()
file = [s.rstrip()for s in a]
file.reverse()

user = []
passw = []


for lines in file:
    file = lines.split(":")

    un = file[0]
    pw = file[1]
    user.append(un)
    passw.append(pw)

for i in range(0,len(user)-1):
    n=random.randint(0,len(user)-1)
    uname=user[n]
    pas=passw[n]
    driver=webdriver.Chrome()
    driver.get(insta)
    time.sleep(2)
    user_name=driver.find_element_by_xpath("//*/div/div[1]/div/label/input")
    user_name.click()
    user_name.send_keys(uname)
    password=driver.find_element_by_xpath("//*/div/div[2]/div/label/input")
    password.click()
    password.send_keys(pas)
    time.sleep(1)
    login=driver.find_element_by_xpath("//*/div/div[3]/button/div")
    login.click()
    time.sleep(7)

    if error in driver.current_url:

        time.sleep(2)
        driver.quit()
        continue

    else:

        try:
            error2=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p").is_displayed()          
            if error2 is True:
                driver.quit()

        except :
            pop=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            pop.click()
            search=driver.find_element_by_xpath("//*/section/nav/div[2]/div/div/div[2]/div")
            search.click()
            time.sleep(4)
            text=driver.find_element_by_xpath("//*/section/nav/div[2]/div/div/div[2]/input")
            text.send_keys(username)
            time.sleep(5)
            ent=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
            ent.click()
            time.sleep(3)
            follow=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
            follow.click()
            time.sleep(10)
            driver.quit()
            continue
