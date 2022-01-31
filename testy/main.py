import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/")
    
    def test_A_regiser(self):
        self.regisersite = self.driver.find_element(By.NAME, "Register")
        self.regisersite.click()
        
        self.input_username = self.driver.find_element(By.NAME, "username")
        self.input_username.send_keys("UnitTest")
        self.input_email = self.driver.find_element(By.NAME, "email")
        self.input_email.send_keys("254477@student.pwr.edu.pl")
        self.input_password = self.driver.find_element(By.NAME, "password1")
        self.input_password.send_keys("BezpieczneHaslo123")
        self.input_password_confirmation = self.driver.find_element(By.NAME, "password2")
        self.input_password_confirmation.send_keys("BezpieczneHaslo123")
        self.register = self.driver.find_element(By.CLASS_NAME, "w3-btn")
        self.register.click()

    def test_B_loginandorder(self):
        self.loginsite = self.driver.find_element(By.NAME, "Login")
        self.loginsite.click()
        
        self.input_username = self.driver.find_element(By.NAME, "username")
        self.input_username.send_keys("UnitTest")
        self.input_password = self.driver.find_element(By.NAME, "password")
        self.input_password.send_keys("BezpieczneHaslo123")
        self.submit_button = self.driver.find_element(By.CLASS_NAME, "w3-btn")
        self.submit_button.click()
        
        self.restaurant = self.driver.find_element(By.CLASS_NAME, "card-image")
        self.restaurant.click()
        
        self.order = self.driver.find_element(By.CLASS_NAME, "add-to-cart")
        self.order.click()
        
        self.order_check = self.driver.find_element(By.CLASS_NAME, "fa")
        self.order_check.click()
        
        self.order_order = self.driver.find_element(By.CLASS_NAME, "btn-success")
        self.order_order.click()
        
        self.input_street = self.driver.find_element(By.NAME, "street")
        self.input_street.send_keys("Jana Pawła")
        self.input_buildingnumber = self.driver.find_element(By.NAME, "building_number")
        self.input_buildingnumber.send_keys("420")
        self.input_localnumber = self.driver.find_element(By.NAME, "local_number")
        self.input_localnumber.send_keys("69")
        self.input_city = self.driver.find_element(By.NAME, "city")
        self.input_city.send_keys("Jelenia Góra")
        self.input_passcode = self.driver.find_element(By.NAME, "pass_code")
        self.input_passcode.send_keys("58500")
        self.orderandpay = self.driver.find_element(By.CLASS_NAME, "btn-success")
        self.orderandpay.click()
        
        self.pay = self.driver.find_element(By.CLASS_NAME, "btn")
        self.pay.click()

    def test_C_createrestaurant(self):
        #logowanie
        self.loginsite = self.driver.find_element(By.NAME, "Login")
        self.loginsite.click()
        
        self.input_username = self.driver.find_element(By.NAME, "username")
        self.input_username.send_keys("UnitTest")
        self.input_password = self.driver.find_element(By.NAME, "password")
        self.input_password.send_keys("BezpieczneHaslo123")
        self.submit_button = self.driver.find_element(By.CLASS_NAME, "w3-btn")
        self.submit_button.click()


        self.create = self.driver.find_element(By.ID, "create_restaurant")
        self.create.click()

        self.input_name = self.driver.find_element(By.NAME, "name")
        self.input_name.send_keys("Poslkie jadło")

        self.input_kitchen = self.driver.find_element(By.NAME, "kitchen_type")
        self.input_kitchen.send_keys("Polska")

        self.input_img = self.driver.find_element(By.NAME, "img_path")
        self.input_img.send_keys("test.png")






        
    def test_D_deletetestuser(self):
        self.driver.get("http://localhost:8000/admin/login/?next=/admin/auth/user/")
        self.input_username = self.driver.find_element(By.NAME, "username")
        self.input_username.send_keys("root")
        self.input_password = self.driver.find_element(By.NAME, "password")
        self.input_password.send_keys("root")
        self.login_button = self.driver.find_element(By.XPATH, "//input[@value='Log in']")
        self.login_button.click()
        self.users = self.driver.find_element(By.LINK_TEXT, "Users")
        self.users.click()
        self.unittestuser = self.driver.find_element(By.LINK_TEXT, "UnitTest")
        self.unittestuser.click()
        self.userdelete = self.driver.find_element(By.CLASS_NAME, "deletelink")
        self.userdelete.click()
        self.yesimsure = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        self.yesimsure.click()
        
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()