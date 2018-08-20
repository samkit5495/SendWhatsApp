from selenium import webdriver

driver = webdriver.Chrome()

class WhatsApp:

    def __init__(self):
        driver.get('https://web.whatsapp.com/')
        
    def get_qr_code(self):
        try:
            return driver.find_element_by_class_name('_2EZ_m').find_element_by_tag_name("img").get_attribute('src')
        except:
            return None

    def send_message(self, name, msg):
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_2S1VP')
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        button.click()