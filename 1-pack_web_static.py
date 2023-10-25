#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compress the web_static folder into a .tgz archive
    """
    try:
        local("mkdir -p versions")

        time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(archive_filename))
        if local("test -e {}".format(archive_filename)).succeeded:
            return archive_filename
        else:
            return None
    except Exception as e:
        return None
