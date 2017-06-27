# Setting the port

sed -i -e '/^Port/s/^.*$/Port 33333/' /etc/ssh/sshd_config

firewall-cmd --add-port 33333/tcp --permanent

firewall-cmd --reload

systemctl reload sshd

