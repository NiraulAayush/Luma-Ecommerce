from datas import login_data
from pages.register_page import LumaWebsite

URL = "https://magento.softwaretestingboard.com/"

def test_valid_credentials(driver):

    account = LumaWebsite(driver)


    account.load(URL)
    account.click_register()


    account.register(login_data.register_credentials["first_name"],
                     login_data.register_credentials["last_name"],
                     login_data.register_credentials["email"],
                     login_data.register_credentials["password"],
                     login_data.register_credentials["confirm_password"]
    )
