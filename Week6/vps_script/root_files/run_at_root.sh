export VPS_NAME="$1"
export USERNAME="$2"
export PASSWORD="$3"
export DEFINED_SSH_PORT="$4"

apt-get -y update

./root_files/sshd_config.sh
echo sshd_config success

./root_files/firewall_config.sh
echo firewall_config success

./root_files/port_config.sh
echo port_config success

./root_files/timezone_ntp_config.sh
echo timezone_ntp_config success

./root_files/swap_memory_config.sh
echo swap_memory_config success

./root_files/nginx_config.sh
echo nginx_config success

./root_files/fail2ban_config.sh
echo fail2ban_config success

cat /home/$USERNAME/.credentials | chpasswd
cat /home/$USERNAME/.credentials
rm /home/$USERNAME/.credentials
