#!/usr/bin/python3
"""fabric script that deletes out-of-date archives
using the function do_clean"""

from fabric.api import *
import os

env.hosts = ["54.172.184.51", "52.90.22.219"]


def do_clean(number=0):
    """deletes out-of-date archives"""

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
