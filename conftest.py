import os
import pytest
import logging

@pytest.fixture(scope='package', autouse=True)
def testsuite_setup_teardown():
    logging.info('------------------------------- Start to run test case ----------------------------\n')
    yield
    logging.info('------------------------------- End to run test case -------------------------------')


@pytest.fixture(scope='function', autouse=True)
def testcase_setup_teardown():
    case_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]

    logging.info('------------------------------- Begin ------------------------------------')
    logging.info('Current test case name : (%s)', case_name)
    yield
    logging.info('------------------------------- End --------------------------------------\n')