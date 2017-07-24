VPS_IP="$1"
VPS_NAME="$2"
USERNAME="$3"
PASSWORD="$4"
DEFINED_SSH_PORT="$5"

scp -r -o StrictHostKeyChecking=no VPS_script/root_files root@$VPS_IP:
ssh root@$VPS_IP chmod -R +x root_files

ssh root@$VPS_IP ./root_files/add_user.sh $USERNAME

scp /home/kapil/.ssh/id_rsa.pub root@$VPS_IP:/etc/ssh/$USERNAME/authorized_keys
scp /home/kapil/.credentials root@$VPS_IP:/home/$USERNAME/

ssh root@$VPS_IP ./root_files/run_at_root.sh $VPS_NAME $USERNAME $PASSWORD $DEFINED_SSH_PORT
# && rm -rf root_files
