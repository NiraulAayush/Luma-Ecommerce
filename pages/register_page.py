from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LumaWebsite:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.firstname_id = 'firstname'
        self.lastname_id = 'lastname'
        self.email_id = 'email_address'
        self.password_id = 'password'
        self.confirm_password_id = 'password-confirmation'
        self.register_btn_xpath = "//button[@type = 'submit' and @title = 'Create an Account']"
        self.register_link_xpath = "//a[@href = 'https://magento.softwaretestingboard.com/customer/account/create/']"

    def load(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.refresh()
        
    def click_register(self):


        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.register_link_xpath))
        ).click()

    def register(self, firstname, lastname, email, password, password_confirm):


        print(f'Generated Email: {email}')
        print(f'Generated password: {password}')
        """
        yo print vayena ra???
        """

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.firstname_id))
        ).send_keys(firstname)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.lastname_id))
        ).send_keys(lastname)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.email_id))
        ).send_keys(email)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.password_id))
        ).send_keys(password)


        self.wait.until(
            EC.presence_of_element_located((By.ID, self.confirm_password_id))
        ).send_keys(password_confirm)

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.register_btn_xpath))
        ).click()
