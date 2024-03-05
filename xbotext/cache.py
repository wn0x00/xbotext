import os
import json


def get_xbot_cache_path(mode="app", name="") -> str:
    """创建本地缓存文件夹, 缓存目录"""
    local_appdata_path = os.getenv('LOCALAPPDATA')
    xbot_app_cache_path = os.path.join(local_appdata_path, "xbot_app")

    if not os.path.exists(xbot_app_cache_path):
        os.makedirs(xbot_app_cache_path)

    return xbot_app_cache_path


