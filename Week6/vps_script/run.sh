scp -r VPS_script/root_files root@139.59.7.109:
ssh root@139.59.7.109 'chmod +x root_files/add_user.sh && .root_files/add_user.sh'

scp .ssh/id_rsa.pub root@139.59.7.109:/etc/ssh/kapilv/authorized_keys
scp .credentials root@139.59.7.109:/home/kapilv/

ssh root@139.59.7.109 'chmod +x root_files/run_at_root.sh && ./root_files/run_at_root.sh && rm -rf root_files'

