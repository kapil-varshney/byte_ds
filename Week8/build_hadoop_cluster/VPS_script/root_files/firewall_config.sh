# Install firewalld (RedHat)

apt-get -y install firewalld

systemctl start firewalld

firewall-cmd --reload

systemctl enable firewalld

