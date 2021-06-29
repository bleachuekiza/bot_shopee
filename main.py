from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import timeit

browser = webdriver.Chrome('chromedriver')

start = timeit.default_timer()
browser.get('https://shopee.co.th/buyer/login')
sleep(1)
# ปุ่มเลือกภาษา
browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse').click()
username = browser.find_element_by_name('loginKey')
# Username คำแนะนำห้ามใช้เป็นเบอร์ เพราะมันจะต้องใช้ otp
username.send_keys('bleachuekiza')
passwd = browser.find_element_by_name('password')
passwd.send_keys('Freddie18622089')
sleep(0.2)
# ปุ่มกดล็อคอิน
Btnlogin = browser.find_element_by_class_name('_1ruZ5a._3Nrkgj._3kANJY._1IRuK_.hh2rFL._3_offS').click()

stop = timeit.default_timer()
print('Login Time: ', stop - start)

#link open
# browser.get('https://shopee.co.th/product/40886114/1562678751/?')
# link close
browser.get('https://shopee.co.th/product/40886114/9338776629/?')
sleep(0.5)
#Local Web
# browser.get('file:///C:/Users/Zachtix/Desktop/ZexKode/project_bot_shopee/web-test/Shopee%20Thailand.html')

onclickbtn = False

onclickbtn = False
while (True):
    if onclickbtn == False:
        try:
            try:
                sleep(0.5)
                # ถ้ามันมีให่้เลือกสีหรืออะไร เปิดโค้ดบรรทัด ด้านล่าง ถ้ามี ให้เลือก 2 อย่าง ก็ก๊อปโค้ดวางเพิ่มอีกบรรทัดแล้วก๊อป XPath จาก browser
                # วิธีหา Xpath อ่าน README.md
                # browser.find_element_by_xpath('//div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[12]').click()
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
                print('Btn Close')
                browser.refresh()
            except:
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()
                print('Btn Open')
                onclickbtn = True
        except NoSuchElementException:
            print("NoSuchElementException")
            pass
            