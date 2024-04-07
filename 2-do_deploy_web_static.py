#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, put, run
from os.path import exists

# Actual server IPs
env.hosts = ['54.144.149.138', '35.168.1.145']

def do_deploy(archive_path):
    """This script will upload the archive to the specified web servers, uncompress it,
    update the symbolic links, and ensure the deployment is successful."""
    if not exists(archive_path):
        return False

    archive_name = archive_path.split('/')[-1]
    archive_no_ext = archive_name.split('.')[0]

    try:
        put(archive_path, '/tmp/{}'.format(archive_name))
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, archive_no_ext))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_no_ext))
        return True
    except:
        return False
