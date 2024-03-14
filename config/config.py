from configobj import ConfigObj
from utils.path_util import get_config_path


class GetConfig(object):
    """从config.ini文件中获取配置信息"""
    config = ConfigObj(get_config_path() + "config.ini")

    # 获取登录相关配置信息
    login_url = config['orangehrm']['url']
    username = config['orangehrm']['username']
    password = config['orangehrm']['password']

    # 添加员工配置信息
    add_employee_url = config['employee']['add_employee_url']

    # 搜索添加的员工
    list_employee_url = config['employee']['list_employee_url']

