#Setup machine alias in host file

sudo nano /etc/hosts
## Add the private ip and alias
# 10.139.176.4 NameNode


#Setup SSH Server
sudo apt-get install openssh-server

ssh-keygen -t rsa -P ""

cat .ssh/id_rsa.pub >> .ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys


