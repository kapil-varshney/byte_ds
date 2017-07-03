#!/usr/bin/env python3

import digitalocean
import os

token_ = open('/home/kapil/token').read()
token_ = token_.rstrip()

manager = digitalocean.Manager(token=token_)
keys = manager.get_all_sshkeys()
key_name = 'pub_key'
public_key = [key for key in keys if key.name == key_name]


def get_ip(tag_name='testing'):

    my_droplets = manager.get_all_droplets()
    ip_adds = [droplet.networks['v4'][1]['ip_address'] for droplet in my_droplets if tag_name in droplet.tags]
    print(ip_adds)
    return ip_adds


def get_name(tag_name='testing'):

    my_droplets = manager.get_all_droplets()
    names = [droplet.name for droplet in my_droplets if tag_name in droplet.tags]
    print(names)
    return names


def create_droplet(i=0, tag_name='testing'):

    droplet = digitalocean.Droplet(token=token_,
                                   name='pydroplet-{}'.format(i),
                                   region='blr1',
                                   image='ubuntu-16-04-x64',
                                   size_slug='512mb',
                                   private_networking=True,
                                   tags=[tag_name],
                                   ssh_keys=public_key
                                   )
    print('\nCreating Droplet...')
    droplet.create()
    return droplet


def status_completed(droplet):

    actions = droplet.get_actions()
    return actions[0].status == 'completed'


def delete_droplet(tag_name='testing'):
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        if tag_name in droplet.tags:
            droplet.destroy()
            print('Droplet destroyed')


def build_server(server_ip, server_name, username, password, ssh_port):

    #build_comm = "./VPS_script/run.sh 139.59.60.79 pydroplet-1 kapilv arshney 23232"
    print(server_ip, server_name, username, password, ssh_port)
    build_comm = "./VPS_script/run.sh {} {} {} {} {}".format(server_ip, server_name, username, password, ssh_port)
    print(build_comm)
    os.system(build_comm)
    print("Build complete")


def create_multiple_droplets(n):

    tag_name = input('\nEnter the tag for this batch of servers\n')

    for i in range(int(n)):
        i += 1
        droplet = create_droplet(i, tag_name)

        while 1:
            if status_completed(droplet):
                print('Droplet Created')
                break

    droplet = create_droplet(0, 'to_delete')
    while 1:
        if status_completed(droplet):
            print('Droplet Created')
            break

    vps_ip = get_ip(tag_name)
    vps_name = get_name(tag_name)
    username = 'kapilv'
    password = 'arshney'
    ssh_port = 14000

    print(vps_ip)
    print(vps_name)

    for j in range(int(n)):
        ssh_port += 1
        print(vps_ip[j], vps_name[j], username, password, ssh_port)
        build_server(vps_ip[j], vps_name[j], username, password, ssh_port)


if __name__ == '__main__':

    #delete_droplet('to_delete')
    n = input("\nHow many droplets do you want to make?\n")
    create_multiple_droplets(n)
    delete_droplet('to_delete')

#abc = get_ip()
#print(abc)
#print(get_name())

#delete_droplet()
#create_droplet()

#check_status()

#build_server('139.59.39.3', 'pydroplet-1', 'kapilv', 'arshney', '14001')