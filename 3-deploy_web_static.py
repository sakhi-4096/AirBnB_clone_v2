#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers.
"""
from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ['52.23.177.242', '18.235.248.114']
env.user = "ubuntu"


def do_pack():
    """
    Generate a .tgz archive from web_static folder.
    """
    try:
        local("mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_extension = archive_filename.split(".")[0]
        remote_folder = "/data/web_static/releases/{}".format(
            archive_no_extension)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(remote_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, remote_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(remote_folder, remote_folder))
        run("rm -rf {}/web_static".format(remote_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_folder))

        print("Deployment done")
        return True
    except Exception:
        return False


def deploy():
    """
    Create and distribute the archive to web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
