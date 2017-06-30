#!/usr/bin/env python3

import digitalocean
import time


token_ = open('/home/kapil/token').read()
token_ = token_.rstrip()

manager = digitalocean.Manager(token=token_)
keys = manager.get_all_sshkeys()
key_name = 'public key'
public_key = [key for key in keys if key.name == key_name]


tag_name = input('\nEnter the tag for this batch of servers\n')


def get_ip():

    my_droplets = manager.get_all_droplets()
    ip_adds = [droplet.networks['v4'][1]['ip_address'] for droplet in my_droplets if tag_name in droplet.tags]
    return ip_adds


def get_name():

    my_droplets = manager.get_all_droplets()
    names = [droplet.name for droplet in my_droplets if tag_name in droplet.tags]
    return names


def create_droplet(i=99):

    droplet = digitalocean.Droplet(token=token_,
                                   name='pyDroplet_{}'.format(i),
                                   region='blr1',
                                   image='ubuntu-16-04-x64',
                                   size_slug='512mb',
                                   private_networking=True,
                                   tags=[tag_name],
                                   ssh_keys=public_key
                                   )
    droplet.create()
    return droplet


def create_multiple_droplets(n):
    for i in range(int(n)):
        i += 1
        droplet = create_droplet(i)

        while 1:
            if status_completed(droplet):
                print('DropletCompleted')
                break


def status_completed(droplet):

    actions = droplet.get_actions()
    return actions[0].status == 'completed'


def delete_droplet():
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        if tag_name in droplet.tags:
            droplet.destroy()



n = input("\nHow many droplets do you want to make?\n")
create_multiple_droplets(n)
#time.sleep(60)
#print(get_ip())
#print(get_name())

#delete_droplet()
#create_droplet()

#check_status()