#!/usr/bin/python3
<<<<<<< HEAD
"""Compress web static package
"""
from fabric.api import local
=======
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """


from fabric.api import *
>>>>>>> 42669bbb754c93258fe08819caa48b3c3ce04cc3
from datetime import datetime


def do_pack():
<<<<<<< HEAD
    """Function to compress directory

    Return: path to archive on success; None on fail
    """
    # Get current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check if archiving was successful
    if result.succeeded:
        return archive_path
    return None
=======
    """ Fabric script that generates a .tgz archive from the contents of the...
    ...web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
>>>>>>> 42669bbb754c93258fe08819caa48b3c3ce04cc3
