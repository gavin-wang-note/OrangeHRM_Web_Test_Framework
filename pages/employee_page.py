# -*- coding:UTF-8 -*-
import time
import allure
import logging

from pages.base_page import BasePage
from config.config import GetConfig as config
from utils.common import generate_full_name, remove_duplicates_and_empty

from selenium.webdriver.common.by import By

class EmployeePage(BasePage):
    ADD_EMPLOYEE_URL = config.add_employee_url
    LIST_EMPLOYEE_URL = config.list_employee_url
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CLASS_NAME, "orangehrm-left-space")
    SEARCH_EMPLOYEE = (By.CSS_SELECTOR, 'input[data-v-75e744cd]')
    SEARCH_BUTTOM = (By.CLASS_NAME, "orangehrm-left-space")
    SEARCH_RESULT = (By.CLASS_NAME, "oxd-padding-cell")
    full_name, first_name, last_name = generate_full_name()

    def add_employee(self, firstname=None, moddlename=None, lastname=None):
        firstname = self.first_name if firstname is None else firstname
        lastname = self.last_name if lastname is None else lastname
        logging.info(f"开始添加员工：firsname：（{firstname}）， lastname：（{lastname}）, " \
                      "full_name : ({self.full_name})")
        with allure.step("切换到‘添加员工’页面，并添加员工"):
            self.get_url(self.ADD_EMPLOYEE_URL)
            self.input_text(self.FIRST_NAME, firstname)
            # self.input_text(self.MIDDLE_NAME, moddlename)
            self.input_text(self.LAST_NAME, lastname)
            self.click_element(self.SAVE_BUTTON)
            time.sleep(1)
            logging.info(f"[Success]  完成员工{firstname} {lastname}的添加")

    def navigate_to_employees_list(self):
        with allure.step("跳转页面，跳转到员工列表页面"):
            self.driver.get(self.LIST_EMPLOYEE_URL)
            time.sleep(1)

    def search_new_employee(self, full_name):
        with allure.step("搜索新增加的员工信息"):
            self.input_text(self.SEARCH_EMPLOYEE, full_name)
            self.click_element(self.SEARCH_BUTTOM)
            time.sleep(1) # 等待搜索结果加载

    def verify_search_result(self, first_name, last_name):
        with allure.step("检查搜索结果是否正确"):
            elements = self.find_elements(self.SEARCH_RESULT)
            assert len(elements) > 0, "[ERROR]  没有查询到任何员工信息"
            # 查询到的elements中element.txt内容去重和删除空元素
            search_result = []
            for each_element in elements:
                search_result.append(each_element.text)
            end_result = remove_duplicates_and_empty(search_result)
            search_last_name = end_result[-1]
            search_first_name = end_result[-2]
            assert search_last_name == last_name, f"[ERROR]  没有过滤到{last_name}"
            assert search_first_name == first_name, f"[ERROR]  没有过滤到{first_name}"
            logging.info("[Success]  成功完成账号添加后的检查")