USERNAME="$1"

echo $USERNAME

# nano configuration

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 8" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'


#Adding user - create the same username as the credentials file

adduser --disabled-password --gecos "" $USERNAME

usermod -aG sudo $USERNAME

cp .nanorc /home/$USERNAME/

mkdir /etc/ssh/$USERNAME
