#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers and deploys it.
"""
from fabric.api import local, put, run, env
from os.path import exists
from datetime import datetime

env.hosts = ['52.23.177.242', '18.235.248.114']
env.user = "ubuntu"


def do_pack():
    """Generate a .tgz archive from web_static folder."""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(datetime.now().
                                                   strftime("%Y%m%d%H%M%S"))
    except Exception:
        return None


def do_deploy(archive_path):
    """Distribute and deploy the archive to web servers."""
    if exists(archive_path):
        archive_filename = archive_path.split("/")[-1]
        archive_no_extension = archive_filename.split(".")[0]
        new_version_dir = "/data/web_static/releases/" + archive_no_extension

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(new_version_dir))
        run("tar -xzf /tmp/{} -C {}/".format(
            archive_filename, new_version_dir))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(new_version_dir, new_version_dir))
        run("rm -rf {}/web_static".format(new_version_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_version_dir))

        print("New version deployed!")
        return True

    return False
