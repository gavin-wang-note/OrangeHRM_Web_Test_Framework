from utils.common import generate_full_name
from pages.employee_page import EmployeePage


class TestAddEmployee(EmployeePage):
    full_name, first_name, last_name = generate_full_name()
    def test_add_an_employee(self):
        """Add an employee"""
        self.add_employee(firstname=self.first_name, lastname=self.last_name)
        self.navigate_to_employees_list()
        self.search_new_employee(self.full_name)
        self.verify_search_result(self.first_name, self.last_name)