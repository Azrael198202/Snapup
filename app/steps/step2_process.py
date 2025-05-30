from steps.step3_login import WebsiteLogin
from config import WEB_LOGIN, WEB_LOGIN_AFTER

class DataProcessor:
    def __init__(self, logger, loader):
        self.logger = logger
        self.loader = loader

    def run(self):
        self.logger.info("Processing data...")
        
        login_url=WEB_LOGIN
        protected_url=WEB_LOGIN_AFTER

        for account in self.loader.accounts:
            self.logger.info(f"Account: {account['account']} -> PWD: {account['password']}")
            
        for card in self.loader.credit_cards:
            self.logger.info(f"Card Number: {card['card_number']} -> CSV: {card['cvc']}")
            
        for product in self.loader.products:
            self.logger.info(f"Product No: {product['sku']} -> Quantity: {product['quantity']}")
        
        for account in self.loader.accounts:  
            website = WebsiteLogin(login_url, protected_url, username_field='login_email', password_field='login_password')
            if website.login(account['account'], account['password']):
                page_content = website.get_protected_page()
                print(page_content)
