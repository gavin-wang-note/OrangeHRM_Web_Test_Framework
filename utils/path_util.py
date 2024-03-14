"""  Path Util  """
import os

__all__ = ["get_config_path"]


def get_config_path():
    """
    获取config文件的路径.
    先获得当前的文件的路径，由于config和common同一级，把common替换为config即可.
    """
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.sep + "config" + os.sep


def get_report_path():
    """获取测试报告的路径,reports的路径应该在当前目录下"""
    report_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.sep + "reports" + os.sep
    return report_path