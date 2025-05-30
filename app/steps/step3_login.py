import requests

class WebsiteLogin:
    def __init__(self, login_url, protected_url, username_field='username', password_field='password'):
        """
        :param login_url: login url
        :param protected_url: login success to access url
        :param username_field: username field name in the form
        :param password_field: password field name in the form
        """
        self.session = requests.Session()
        self.login_url = login_url
        self.protected_url = protected_url
        self.username_field = username_field
        self.password_field = password_field

    def login(self, username, password):
        payload = {
            self.username_field: username,
            self.password_field: password
        }

        response = self.session.post(self.login_url, data=payload)

        if response.status_code == 200 and response.url != self.login_url:
            print("login scuccess")
            return True
        else:
            print("login failed, please check your username and password.")
            return False

    def get_protected_page(self):
        response = self.session.get(self.protected_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"this page is protected, stats code：{response.status_code}")
            return None