#!/usr/bin/python3
"""script that generates a tgz archive"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """function that generates tgz archive"""
    try:
        dir1 = "/versions/"
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        if not os.path.exists(dir1):
            local("mkdir versions")
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except Exception as e:
        return None
