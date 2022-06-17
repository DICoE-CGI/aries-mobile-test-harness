from PIL import Image
from agent_factory.candy_uvp.pageobjects.webbasepage import WebBasePage
from selenium.webdriver.common.by import By

# These classes can inherit from a BasePage to do commone setup and functions
class IssuingCredentialPage(WebBasePage):
    """CANdy UVP Issuer Issuing Credential page object"""

    # Locators
    on_this_page_text_locator = "Issuing Credential"
    connected_text_locator = "Connected to the Issuer Agent"
    accepted_credential_text_locator = "You accepted the Credential Offer"
    credential_issued_text_locator = "Your Credential has been Issued"
    # connected_locator = (By.XPATH, '//*[@id="app"]/div/main/div/div/div/img')
    # accepted_credential_locator = (By.XPATH, '//*[@id="app"]/div/main/div/div/div/img')
    # credential_issued_locator = (By.XPATH, '//*[@id="app"]/div/main/div/div/div/img')


    def on_this_page(self):     
        return super().on_this_page(self.on_this_page_text_locator) 

    def connected(self):
        if self.on_this_page():
            return super().on_this_page(self.connected_text_locator)
    
    def credential_accepted(self):
        if self.on_this_page():
            return super().on_this_page(self.accepted_credential_text_locator)

    def credential_issued(self):
        if self.on_this_page():
            return super().on_this_page(self.credential_issued_text_locator)