chmod +x root_files/sshd_config.sh && ./root_files/sshd_config.sh
echo sshd_config success

chmod +x root_files/firewall_config.sh && ./root_files/firewall_config.sh
echo firewall_config success

chmod +x root_files/port_config.sh && ./root_files/port_config.sh
echo port_config success

chmod +x root_files/timezone_ntp_config.sh && ./root_files/timezone_ntp_config.sh
echo timezone_ntp_config success

chmod +x root_files/swap_memory_config.sh && ./root_files/swap_memory_config.sh
echo swap_memory_config success

chmod +x root_files/nginx_config.sh && ./root_files/nginx_config.sh
echo nginx_config success

chmod +x root_files/fail2ban_config.sh && ./root_files/fail2ban_config.sh
echo fail2ban_config success

cat /home/kapilv/.credentials | chpasswd
rm /home/kapilv/.credentials
