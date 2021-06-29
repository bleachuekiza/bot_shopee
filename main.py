from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

browser = webdriver.Chrome('chromedriver')

#link open
# browser.get('https://shopee.co.th/product/40886114/1562678751/?')
#link close
browser.get('https://shopee.co.th/product/40886114/9338776629/?')

onclickbtn = False

#Click Select Language
sleep(1)
browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse').click()
# BtnLang
#Click Select Language
# sleep(1)

# while not buy:

# onclickbtn = False
# while (True):
#     if onclickbtn == False:
#         try:
#             browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
#             print('Btn Close')
#             browser.refresh()
#             # sleep(0.5)
#         except NoSuchElementException:
#             # print(exc)
#             # print("NoSuchElementException")
#             pass
#         except:
#             browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()
#             print('Btn Open')
#             onclickbtn = True

onclickbtn = False
while (True):
    if onclickbtn == False:
        try:
            try:
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
                print('Btn Close')
                browser.refresh()
                # sleep(0.5)
            except:
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()
                print('Btn Open')
                onclickbtn = True
        except NoSuchElementException:
            print("NoSuchElementException")
            