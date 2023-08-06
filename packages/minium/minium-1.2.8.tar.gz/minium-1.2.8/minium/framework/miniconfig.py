#!/usr/bin/env python3
# Created by xiazeng on 2019-05-22
import os
import json
import logging
import yaml

logger = logging.getLogger("minium")

class Path(str):
    pass

default_config = {
    "base_dir": os.path.abspath(os.getcwd()),   # 如果没有配置, 默认工作目录, 如果通过文件生成则为文件所在目录
    "platform": "ide",                          # 平台: ide, android, ios
    "app": "wx",                                # 承载的app: wx
    "debug_mode": "debug",                      # 日志级别
    "close_ide": False,                         # 是否关闭IDE
    "assert_capture": True,                     # 断言时是否截图
    "auto_relaunch": True,                      # case开始时是否回到主页
    "device_desire": {},                        # 真机调试配置
    "account_info": {},                         # 账号配置
    "report_usage": True,                       # 是否需要报告
    "remote_connect_timeout": 180,              # 真机调试中小程序在真机上打开的等待时间
    "request_timeout": 60,                      # 自动化控制指令请求超时时间
    "use_push": True,                           # 真机调试中是否使用推送形式打开小程序, false则需要扫调试二维码
    "full_reset": False,                        # 每个测试class结束，是否释放调试链接
    "outputs": None,                            # 测试产物输出路径
    "enable_app_log": False,                    # 记录小程序日志
    "enable_network_panel": False,              # 记录小程序网络请求
    "project_path": None,                       # 小程序项目路径
    "dev_tool_path": None,                      # 开发者工具命令行工具路径
    "test_port": 9420,                          # 小程序自动化测试调试端口
    "mock_native_modal": None,                  # 仅在IDE生效, mock所有会有原生弹窗的接口
    "mock_request": [],                         # mock request接口，item结构为{rule: {}, success or fail}, 同app.mock_request参数
    "auto_authorize": False,                    # 自动处理授权弹窗
    "audits": None,                             # 开启体验评分，仅在IDE生效, None为不改变
    "teardown_snapshot": False,                 # teardown快照，纪录page.data & page.wxml
    "mock_images_dir": Path(""),                # 需要进行"上传"操作的图片放置的目录
    "mock_images": {},                          # 需要进行"上传"操作的图片, key为图片名(标识用), value为base64格式的图片数据
}


def get_log_level(debug_mode):
    return {
        "info": logging.INFO,
        "debug": logging.DEBUG,
        "warn": logging.WARNING,
        "error": logging.ERROR,
    }.get(debug_mode, logging.INFO)


class MiniConfig(dict):
    def __init__(self, from_dict=None):
        for k, v in default_config.items():
            setattr(self, k, v)
        if isinstance(from_dict, dict):
            for k, v in from_dict.items():
                if k in default_config and isinstance(default_config[k], Path):  # 路径类配置
                    if os.path.isabs(v):
                        v = Path(v)
                    else:
                        v = Path(os.path.abspath(os.path.join(
                            from_dict.get("base_dir") or default_config["base_dir"],
                            v
                        )))
                setattr(self, k, v)
        super(MiniConfig, self).__init__(self.__dict__)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            return None

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def from_file(cls, filename):
        logger.info("load config from %s", filename)
        _, ext = os.path.splitext(filename)
        f = open(filename, "rb")
        if ext == ".json":
            json_dict = json.load(f)
        elif ext == ".yml" or ext == ".yaml":
            json_dict = yaml.load(f)
        else:
            raise RuntimeError(f"unknown extension {ext} for {filename}")
        f.close()
        if isinstance(json_dict, list):
            config_list = list()
            for c in json_dict:
                if not c.get("base_dir"):
                    c["base_dir"] = os.path.dirname(os.path.abspath(filename))
                config_list.append(MiniConfig(c))
            return config_list
        if not json_dict.get("base_dir"):
            json_dict["base_dir"] = os.path.dirname(os.path.abspath(filename))
        return MiniConfig(json_dict)


if __name__ == "__main__":
    a = MiniConfig({"outputs": "xxxx"})
    print(a.outputs)
    print(a.sss)
