# nano configuration

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 8" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'


#Adding user - create the same username as the credentials file

adduser --disabled-password --gecos "" kapilv

usermod -aG sudo kapilv

cp .nanorc /home/kapilv/

mkdir /etc/ssh/kapilv
