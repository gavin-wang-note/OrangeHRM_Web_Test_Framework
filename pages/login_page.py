# -*- coding:UTF-8 -*-
import logging

from pages.base_page import BasePage
from config.config import GetConfig as config

from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    URL = config.login_url
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "orangehrm-login-action")
    INVALID_FAILED = (By.CLASS_NAME, "oxd-alert-content-text")
    LOGIN_SUCCESS = (By.CLASS_NAME, "oxd-main-menu-item--name")
    MUST_INPUT = (By.CLASS_NAME, "oxd-input-group__message")
    LOGOUT_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-icon")
    LOGOUT = (By.CLASS_NAME, "oxd-userdropdown-link")

    def login(self, username=None, password=None, login_success=True):
        self.get_url(self.URL)
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        # Get element text info
        if login_success:
            logging.info("登录成功后页面元素校验")
            assert '管理员' in self.get_element_text(self.LOGIN_SUCCESS),\
                "[ERROR]  成功登录后，页面没有发现'管理员'字样"
        else:
            if len(username) and len(password):
                logging.info("因输入错误的用户名或密码导致登录失败后的页面元素校验")
                cre_flag = 'Invalid credentials' in self.get_element_text(self.INVALID_FAILED)
                assert cre_flag, \
                    "[ERROR] 输入错误的用户名或密码后，页面缺失'Invalid credentials'字样"
            else:
                logging.info("因输入空的用户名或密码导致登录失败后的页面元素校验")
                need_flag = '需要' in self.get_element_text(self.MUST_INPUT)
                assert need_flag, "[ERROR]  输入空的用户名或密码后，页面缺失'需要'字样"

    def logout(self):
        """
        登出页面，因为conftest.py中定义了一个登录fixture，所以测试登录相关用例的时候，要先登出，此时不quit
        """
        # 点击头像右侧箭头，弹出下拉列表
        self.click_element(self.LOGOUT_DROPDOWN)
        # Get all of elements
        elements = self.find_elements(self.LOGOUT)
        if elements:
            # 有4个元素，分别是关于、Support、更改密码和登出，登出是最后一个
            last_element = elements[-1]
            # self.click_element(last_element)
            last_element.click()
