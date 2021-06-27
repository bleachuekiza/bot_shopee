from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

browser = webdriver.Chrome('chromedriver')

#link open
# browser.get('https://shopee.co.th/product/40886114/1562678751/?')
#link close
browser.get('https://shopee.co.th/product/40886114/9338776629/?')

buy = False

#Click Select Language
BtnLang = browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse')
BtnLang.click()
#Click Select Language
# sleep(1)

while not buy:
    
    try:
        browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
        print('Btn Close')
        browser.refresh()
        # sleep(0.5)
    except NoSuchElementException:
        # print("NoSuchElementException")
        buy = False
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg')
        addToCartBtn.click()
        print('Btn Open')
        buy = True