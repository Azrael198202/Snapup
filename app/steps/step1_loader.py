import os
import pandas as pd
from config import DATA_DIR

class ExcelLoader:
    def __init__(self, logger):
        self.logger = logger
        self.accounts = []
        self.credit_cards = []
        self.products = []

    def load_accounts(self):
        path = os.path.join(DATA_DIR, 'accounts.xlsx')
        df = pd.read_excel(path, header=None)
        self.accounts = [
            {'account': row[0], 
             'password': row[1]}
            for _, row in df.iterrows()
        ]
        self.logger.info(f"Loaded {len(self.accounts)} accounts.")

    def load_credit_cards(self):
        path = os.path.join(DATA_DIR, 'credit_cards.xlsx')
        df = pd.read_excel(path, header=None)
        self.credit_cards = [
            {
                'card_number': row[0],
                'cvc': row[1], 
                'expiry': row[2], 
                'name': row[3]
            }
            for _, row in df.iterrows()
        ]
        self.logger.info(f"Loaded {len(self.credit_cards)} credit cards.")

    def load_products(self):
        path = os.path.join(DATA_DIR, 'products.xlsx')
        df = pd.read_excel(path, header=None)
        self.products = [
            {
                'sku': row[0], 
                'quantity': row[1],
                'color': row[2],
                'price': row[3]
            }
            for _, row in df.iterrows()
        ]
        self.logger.info(f"Loaded {len(self.products)} products.")

    def load_all(self):
        self.load_accounts()
        self.load_credit_cards()
        self.load_products()
