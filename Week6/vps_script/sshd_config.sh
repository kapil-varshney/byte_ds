chown -R kapilv:kapilv /etc/ssh/kapilv

# Permissions- user: rwx, group: r-x, world: r-x
chmod 755 /etc/ssh/kapilv

# Permissions- user: rw-, group: r--, world: r--
chmod 644 /etc/ssh/kapilv/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/kapilv\/authorized_keys/' /etc/ssh/sshd_config

sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "# Added by Katabasis build process" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers kapilv" >> /etc/ssh/sshd_config'

systemctl reload sshd

