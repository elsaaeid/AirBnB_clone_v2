#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists
# do_pack = __import__('1-pack_web_static').do_pack
# do_deploy = __import__('2-do_deploy_web_static').do_deploy

# Actual server IPs
env.hosts = ['54.144.149.138', '35.168.1.145']

def do_pack():
    """A fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack"""

    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """This script will upload the archive to the specified web servers, uncompress it,
    update the symbolic links, and ensure the deployment is successful."""
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    archive_no_ext = file_name.split('.')[0]

    try:
        put(archive_path, '/tmp/{}'.format(file_name))
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, archive_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_no_ext))
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    result = do_deploy(archive_path)
    return result
