#!/usr/bin/python3
"""
This script distributes an archive to your web servers,
using the function do_deploy
"""


from fabric.api import *
from os.path import exists


env.hosts = ['54.90.56.157', '100.25.192.254']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return

    filename = archive_path.split('/')[-1]
    # Extract the filename from the full archive path

    release_folder = '/data/web_static/releases/{}'.format(filename.split('.')[0])
    # Create the release folder path

    # Upload the archive to the /tmp/ directory on the web server
    if put(archive_path, "/tmp/").failed:
        return False

    # Uncompress the archive to the release folder on the web server
    if run("mkdir -p {}/".format(release_folder)).failed:
        return False
    if run("tar -xzf /tmp/{filename} -C {release_folder}/").failed:
        return False

    # Cleanup - remove the archive and move files
    if run("rm /tmp/{}".format(filename)).failed:
        return False
    if run("mv {release_folder}/web_static/* {release_folder}/").failed:
        return False
    if run("rm -rf {}/web_static".format(release_folder)).failed:
        return False

    # Update the symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run(f"ln -s {release_folder} /data/web_static/current").failed:
        return False

    return True
