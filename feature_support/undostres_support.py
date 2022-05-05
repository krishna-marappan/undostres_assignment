from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Data.Xpath import *
from Data.Data import *

screenshotcount = 1

def capture_screenshot(self):
    global screenshotcount
    path =  Data.scr_path + str(screenshotcount) + ".png"
    self.save_screenshot(path)
    screenshotcount += 1


class undostres_support():

    def recarga_celular_details(self, operator, number, amount):
        self.find_element(By.XPATH, Xpath.input_operator).click()
        res = Xpath.choose_Operador.replace("replace", operator)
        self.find_element(By.XPATH, res).click()
        text_area = self.find_element(By.XPATH, Xpath.input_number)
        text_area.send_keys(number)
        self.find_element(By.XPATH, Xpath.input_amount).click()
        res = Xpath.choose_amount.replace("replace", amount)
        self.find_element(By.XPATH, res).click()
        sleep(2)
        capture_screenshot(self)
        res = self.find_element(By.XPATH, Xpath.sign_button)
        res.click()

    def payment_screen_verify(self):
        res = self.find_element(By.XPATH, Xpath.payment_screen)
        status = res.is_displayed()
        capture_screenshot(self)
        return status

    def payment_details(self, Cardnumber, month, year, ccv, email):
        self.find_element(By.XPATH, Xpath.Payment_tarjeta).click()
        sleep(1)
        self.find_element(By.XPATH, Xpath.user_nueva).click()
        self.find_element(By.XPATH, Xpath.user_nueva).click()
        res = Xpath.input_name.replace("replace", "cardno")
        self.find_element(By.XPATH, res).send_keys(Cardnumber)
        res = Xpath.input_name.replace("replace", "expmonth")
        self.find_element(By.XPATH, res).send_keys(month)
        res = Xpath.input_name.replace("replace", "expyear")
        self.find_element(By.XPATH, res).send_keys(year)
        res = Xpath.input_name.replace("replace", "cvvno")
        self.find_element(By.XPATH, res).send_keys(ccv)
        self.find_element(By.XPATH, Xpath.input_email).send_keys(email)
        sleep(1)
        capture_screenshot(self)
        self.find_element(By.XPATH, Xpath.Payment_button).click()
        sleep(2)

    def access_with_email(self, email, Password):
        self.find_element(By.XPATH, Xpath.email_field).send_keys(email)
        sleep(1)
        self.find_element(By.XPATH, Xpath.password_field).send_keys(Password)
        res = self.find_element(By.XPATH, Xpath.captchaframe)
        self.switch_to.frame(res)
        self.find_element(By.XPATH, Xpath.captcha).click()
        sleep(3)
        capture_screenshot(self)
        self.switch_to.default_content()
        self.find_element(By.XPATH, Xpath.acceso).click()

    def success_message_verify(self):
        element = WebDriverWait(self, 20).until(EC.visibility_of_element_located((By.XPATH, Xpath.success_message)))
        status = element.is_displayed()
        capture_screenshot(self)
        return status

