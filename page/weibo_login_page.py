from base.base import BasePage

class WeiboLoginPage(BasePage):
    url = "https://weibo.com"

    def username_input(self,username):
        self.by_id("loginname").clear()
        self.by_id("loginname").send_keys(username)

    def password_input(self,password):
        self.by_name("password").clear()
        self.by_name("password").send_keys(password)


    def login_btn(self):
        self.by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

    def login(self,username,password):
        self.username_input(username)
        self.password_input(password)
        self.login_btn()
