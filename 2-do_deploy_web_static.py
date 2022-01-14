#!/usr/bin/python3
"""script that deploy archive!"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """function that generates tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("mkdir -p versions")
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except Exception as e:
        return None

def do_deploy(archive_path):
    """function that distributes an archive to your web servers, using the function do_deploy"""
    try:
        filename=archive_path.split("/")[-1]
        onlyname=filename.split(".")[0]
        uncompress_path="/data/web_static/releases/{}".formal(onlyname)
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}').format(uncompress_path)
        run('sudo tar -xzf /tmp/{} {}'.format(filename, uncompress_path))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {}/web_static/* {}/'.format(uncompress_path))
        run('sudo rm -rf {}/web_static'.format(uncompress_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(uncompress_path))
        print('New version deployed!')
        return True
    except BaseException:
        return False
