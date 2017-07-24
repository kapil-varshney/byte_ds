# Setting the port

sed -i -e "/^Port/s/^.*$/Port $DEFINED_SSH_PORT/" /etc/ssh/sshd_config

firewall-cmd --add-port $DEFINED_SSH_PORT/tcp --permanent

firewall-cmd --reload

systemctl reload sshd

