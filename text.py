from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

browser = webdriver.Chrome('chromedriver')
browser.get('https://shopee.co.th/product/186721812/8317899487')
sleep(1)
browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse').click()
sleep(1)
browser.find_element_by_xpath('//div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[12]').click() ## XPath
browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()