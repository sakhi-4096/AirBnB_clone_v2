#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import local, run, env


env.hosts = ['52.23.177.242', '18.235.248.114']
env.user = "ubuntu"


def do_clean(number=0):
    """Delete out-of-date archives from the server."""
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)

    local("cd versions && ls -t | tail -n +{} | xargs -I {{}} rm {{}}"
          .format(number + 1))
    path = '/data/web_static/releases/'
    run("cd {} && ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}"
        .format(path, number + 1))
