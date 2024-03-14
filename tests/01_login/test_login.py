import pytest

from pages.login_page import LoginPage
from config.config import GetConfig as config


class TestLoginPage(LoginPage):
    # 因为conftest.py 定义的fixture已经被调用，成功登录了，所以先测试“登出”功能
    def test_logout(self):
        self.logout()

    @pytest.mark.parametrize("login_data", [
        # 正确的用户名和错误的密码
        (config.username, "wrong_password"),
        # 错误的用户名和正确的密码
        ("wrong_username", config.password),
        # 错误的用户名和错误的密码
        ("wrong_username", "wrong_password"),
        # 省略用户名
        ("", config.password),
        # 省略密码
        (config.username, ""),
    ])
    def test_failed_login(self, login_data):
        """Login OrangeHRM Web Failure with different credentials"""
        username, password = login_data
        self.login(username, password, login_success=False)

    @pytest.mark.login
    def test_successful_login(self):
        """Login OrangeHRM Web Success"""
        self.login(username=config.username, password=config.password)