from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json

f = open('config.json', encoding="utf8")
data = json.load(f)
username = data["username"]
password = data["password"]
url = data["url"]
delayLogin = data["delayLogin"]
f.close()

browser = webdriver.Chrome('chromedriver')

browser.get('https://shopee.co.th/buyer/login')
sleep(1)
# ปุ่มเลือกภาษา
browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse').click()
usernamebox = browser.find_element_by_name('loginKey')
usernamebox.send_keys(username)
passwdbox = browser.find_element_by_name('password')
passwdbox.send_keys(password)
sleep(1)
# ปุ่มกดล็อคอิน
Btnlogin = browser.find_element_by_class_name('_1ruZ5a._3Nrkgj._3kANJY._1IRuK_.hh2rFL._3_offS').click()
# ดีเลย์ใส่ OTP (20 วิเปลื่อนได้ แต่ถ้าไม่มี OTP ก็ปิดเลย ใส่ # หน้าบรรทัด)
sleep(delayLogin)

#link open
browser.get(url)
# browser.get('https://shopee.co.th/product/40886114/1562678751/?')
# link close
# browser.get('https://shopee.co.th/product/40886114/9338776629/?')
sleep(0.5)
#Local Web
# browser.get('file:///C:/Users/Zachtix/Desktop/ZexKode/project_bot_shopee/web-test/Shopee%20Thailand.html')

# def

def ChangeDeliveryonpagePay():
    onclickbtnChangeDelivery = False
    while (True):
        if onclickbtnChangeDelivery == False:
            try:
                # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
                sleep(1)
                browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]').click()
                sleep(0.5)
                browser.find_element_by_class_name('_1uYE59').click()
                browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[2]/div/button[2]').click()
                # browser.refresh()
                sleep(0.5)
                browser.find_element_by_class_name('_1n5Ut6').click()
                browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button').click()
                browser.find_element_by_class_name('credit-card-info-view').click()
                # browser.find_element_by_class_name('').click()
                # browser.find_element_by_class_name('').click()
                # browser.find_element_by_class_name('').click()
                print('pay success')
                # onclickbtnChangeDelivery= True
            except NoSuchElementException:
                print("NoSuchElementException")
                pass

def pageCart():
    onclickbtnpageCart = False
    while (True):
        if onclickbtnpageCart == False:
            try:
                # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
                sleep(0.5)
                browser.find_element_by_tag_name('body').click()
                browser.find_element_by_class_name('shopee-button-solid.shopee-button-solid--primary').click()
                print('Open Pay Page')
                onclickbtnpageCart = True
                ChangeDeliveryonpagePay()
            except NoSuchElementException:
                print("NoSuchElementException")
                pass

def pageProduct():
    onclickbtnpageProduct = False
    while (True):
        if onclickbtnpageProduct == False:
            try:
                try:
                    # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
                    sleep(0.5)
                    # ถ้ามันมีให่้เลือกสีหรืออะไร เปิดโค้ดบรรทัด ด้านล่าง ถ้ามี ให้เลือก 2 อย่าง ก็ก๊อปโค้ดวางเพิ่มอีกบรรทัดแล้วก๊อป XPath จาก browser
                    # วิธีหา Xpath อ่าน README.md
                    # browser.find_element_by_xpath('//div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[12]').click()
                    # browser.find_element_by_xpath(xpath1).click()
                    browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
                    print('Btn Close')
                    browser.refresh()
                except:
                    browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()
                    print('Btn Open')
                    onclickbtnpageProduct = True
                    pageCart()
            except NoSuchElementException:
                print("NoSuchElementException")
                pass

pageProduct()
