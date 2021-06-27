from selenium import webdriver
from time import sleep
import timeit


browser = webdriver.Chrome('chromedriver')

browser.get('https://shopee.co.th/buyer/login')
sleep(1)
start = timeit.default_timer()
BtnLang = browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse')
BtnLang.click()
# sleep(1)
username = browser.find_element_by_name('loginKey')
username.send_keys('bleachuekiza')
passwd = browser.find_element_by_name('password')
passwd.send_keys('Freddie18622089')
sleep(.2)
Btnlogin = browser.find_element_by_class_name('_1ruZ5a._3Nrkgj._3kANJY._1IRuK_.hh2rFL._3_offS')
Btnlogin.click()
sleep()

stop = timeit.default_timer()
print('Time: ', stop - start)