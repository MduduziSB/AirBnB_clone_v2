#!/usr/bin/python3
"""
This script distributes an archive to your web servers,
using the function do_deploy
"""


from fabric.api import local, put, run, env
from os.path import exists


env.hosts = ['54.90.56.157', '100.25.192.254']


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ on the remote server
        put(archive_path, '/tmp')

        # Extract the archive to a new folder in /data/web_static/releases
        archive_filename = archive_path.split('/')[-1]
        release_path = f"/data/web_static/releases/{archive_filename[:-4]}"
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Remove the archive from the remote server
        run("rm /tmp/{}".format(archive_filename))

        # Create or update the symbolic link to the new version
        current_path = "/data/web_static/current"
        run("rm -f {}".format(current_path))
        run("ln -s {} {}".format(release_path, current_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
