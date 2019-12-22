#coding=utf-8
from secondpack import Yoyo
login_url="http://127.0.0.1:81/t18bbs/forum.php"
class LoginPage(Yoyo):
    username_loc=("id","ls_username")
    password_loc=("id","ls_password")
    submit_loc=("xpath",".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button")
    remember_loc=("xpath",".//*[@id='lsform']/div/div/table/tbody/tr[1]/td[3]/label")
    retrieve_loc=("link text","忘记登录用户名")
    reset_loc=("link text","找回密码")
    register_loc=("link text","立即注册")
#    feedback_loc=("link text","")
    def input_username(self,username):
        self.send_keys(self.username_loc,username)
        
    def input_password(self,password):
        self.send_keys(self.password_loc,password)
        
    def click_submit(self):
        self.click(self.submit_loc)
        
    def click_remember_live(self):
        self.click(self.remember_loc)
        
    def click_retrieve(self):
        self.click(self.retrieve_loc)
        
    def click_reset(self):
        self.click(self.reset_loc)
        
    def click_register(self):
        self.click(self.register_loc)
        
    def login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_submit()