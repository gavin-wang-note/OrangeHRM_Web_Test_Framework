#  -*- coding:UTF-8 -*-

import random
import logging
import datetime
from faker import Faker

fake = Faker()

def get_date_time(**kwargs):
    """返回格式化为年月日小时分秒的日期时间字符串"""
    date_time = (datetime.datetime.now() + datetime.timedelta(**kwargs)).strftime('%Y-%m-%d %H:%M:%S')
    logging.debug("Current date time is : (%s)", date_time)
    return date_time

def get_time_stamp(**kwargs):
    """返回当前的Unix时间戳"""
    return datetime.datetime.now().timestamp()

def remove_duplicates_and_empty(lst):
    """列表去重和删除空元素"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen and item:
            seen.add(item)
            result.append(item)
    return result

def generate_full_name():
    """随机生成英文全名、firstname、lastname"""
    first_name = fake.first_name()
    last_name = fake.last_name()
    full_name =  first_name + ' ' + last_name
    return full_name, first_name, last_name

def generate_gender():
    """随机生成性别"""
    return fake.random_element(elements=('Male', 'Female', 'Non-binary'))

def generate_landline_phone():
    """  随机生成座机（固定电话）号码。"""
    area_codes = ['010', '021', '022', '023', '024', '025']
    area_code = random.choice(area_codes)
    number = ''.join(random.choices('0123456789', k=7))  # 随机生成7位数字
    return f"{area_code}-{number}"

def generate_mobile_phone():
    """随机生成11位移动电话号码"""
    # 常见的手机前缀，这里只列举了一部分，可根据需要添加更多
    prefixes = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
                '150', '151', '152', '153', '155', '156', '157', '158', '159',
                '176', '177', '178', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189']
    prefix = random.choice(prefixes)
    suffix = ''.join(random.choices('0123456789', k=8))  # 随机生成8位数字
    return f"{prefix}{suffix}"

def generate_nationality():
    """随机生成国籍"""
    return fake.country()

def generate_address():
    """随机生成家庭住址"""
    return fake.address()

def generate_marital_status():
    """随机生成婚姻状况"""
    return fake.random_element(elements=('Married', 'Single', 'Divorced', 'Widowed'))

def generate_birth_date():
    """随机生成出生年月"""
    return fake.date_of_birth(minimum_age=21, maximum_age=61).isoformat()

def generate_age(min_age=18, max_age=60):
    """生成随机年龄，默认范围18至60岁"""
    return random.randint(min_age, max_age)

def generate_postal_code():
    """随机生成邮编号码"""
    return fake.postcode()

def generate_relation():
    """随机生成人员关系"""
    return fake.random_element(elements=('Spouse', 'Parent', 'Sibling', 'Relative', 'Guardian'))

if __name__ == "__main__":
    print("Full Name (Full, First, Last):", generate_full_name())
    print("Gender:", generate_gender())
    print("Random telephone number:", generate_landline_phone())
    print("Phone Number:", generate_mobile_phone())
    print("Nationality:", generate_nationality())
    print("Address:", generate_address())
    print("Marital Status:", generate_marital_status())
    print("Birth Date:", generate_birth_date())
    print("Postal Code:", generate_postal_code())
    print("Relation:", generate_relation())