def Stage7onpagePay():
     while (True):
        try:
            # browser.find_element_by_class_name('').click()
            print("Pay Success (Stage7)")
        except NoSuchElementException:
            print("NoSuchElementException (Stage7)")
            pass

def Stage6onpagePay():
     while (True):
        try:
            browser.find_element_by_class_name('credit-card-info-view').click()
            Stage7onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage6)")
            pass

def Stage5onpagePay():
     while (True):
        try:
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button').click()
            Stage6onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage5)")
            pass

def Stage4onpagePay():
     while (True):
        try:
            sleep(0.5)
            browser.find_element_by_class_name('_1n5Ut6').click()
            Stage5onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage4)")
            pass

def Stage3onpagePay():
    while (True):
        try:
            browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[2]/div/button[2]').click()
            # browser.refresh()
            print('pay success')
            Stage4onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage3)")
            pass

def Stage2onpagePay():
    while (True):
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(0.5)
            browser.find_element_by_class_name('_1uYE59').click()
            Stage3onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage2)")
            pass

def Stage1onpagePay():
    while (True):
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(1)
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]').click()
            Stage2onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage1)")
            pass