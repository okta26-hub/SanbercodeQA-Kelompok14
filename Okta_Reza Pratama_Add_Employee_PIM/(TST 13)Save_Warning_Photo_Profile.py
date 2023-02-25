import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#  Warning Photo Profil by Okta Reza#

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin") # isi email
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1)    
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click() # button login
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "firstName").send_keys("asus") # isi nama first name
        time.sleep(1)
        self.driver.find_element(By.NAME, "middleName").send_keys("tuf") # isi nama first name
        time.sleep(1)
        self.driver.find_element(By.NAME, "lastName").send_keys("a15") # isi nama first name
        time.sleep(1)

        # Klik tombol untuk upload foto
        upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.oxd-icon-button.employee-image-action')))
        upload_button.click()
        time.sleep(3)

        # Klik tombol untuk upload foto
        pyautogui.typewrite(r"C:\Users\asus\Desktop\IMG_2166.JPG")#sesuaikan folder foto itu berada
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary").click() #klik save
        time.sleep(8)
       

    # assertion dan pesan
        self.assertEqual(self.driver.title, "OrangeHRM", msg="Gagal untuk testing")

    def tearDown(self):
        self.driver.quit()
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

if __name__ == "__main__":
    unittest.main()
