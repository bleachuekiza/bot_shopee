def Stage7onpagePay():#กดจ่ายเงิน
     while (True):
        try:
            # browser.find_element_by_class_name('').click()
            print("Pay Success (Stage7)")
        except NoSuchElementException:
            print("NoSuchElementException (Stage7)")
            pass

def Stage6onpagePay():#กดเลือกบัตร
     while (True):
        try:
            browser.find_element_by_class_name('credit-card-info-view').click()
            print("Pay Success (Stage6)")
            Stage7onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage6)")
            pass

def Stage5onpagePay():#เลือกเป็นจ่ายผ่านบัตร
     while (True):
        try:
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button').click()
            print("Pay Success (Stage5)")
            Stage6onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage5)")
            pass

def Stage4onpagePay():#กดปุ่มเปลี่ยนวิธีชำระ
     while (True):
        try:
            sleep(0.5)
            browser.find_element_by_class_name('_1n5Ut6').click()
            print("Pay Success (Stage4)")
            Stage5onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage4)")
            pass

def Stage3onpagePay():#กดปุ่มยืนยันเวลาส่ง
    while (True):
        try:
            browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[2]/div/button[2]').click()
            print("Pay Success (Stage3)")
            # browser.refresh()
            print('pay success')
            Stage4onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage3)")
            pass

def Stage2onpagePay():#กดปุ่มเลือกเวลา
    while (True):
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(0.5)
            browser.find_element_by_class_name('_1uYE59').click()
            print("Pay Success (Stage2)")
            Stage3onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage2)")
            pass

def Stage1onpagePay():# กดเปลี่ยนเวลาจัดส่ง
    while (True):
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(1)
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]').click()
            print("Pay Success (Stage1)")
            Stage2onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage1)")
            pass