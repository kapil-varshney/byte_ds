# Install Java

echo 'arshney' | sudo -S apt-get -y update

sudo apt-get install -y default-jdk


# Install Hadoop

wget http://www-eu.apache.org/dist/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz

#Verify

wget https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz.mds

shasum -a 256 hadoop-2.8.0.tar.gz

cat hadoop-2.8.0.tar.gz.mds

#Extract and move the files

tar -xzvf hadoop-2.8.0.tar.gz
sudo mv hadoop-2.8.0 /usr/local/hadoop


# Configure Hadoop
#sudo nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# Add the following line in the hadoop-env.sh file
sed -i 's/JAVA_HOME=.*/JAVA_HOME=$(readlink -f \/usr\/bin\/java | sed "s:bin\/java::")/' /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# Run Hadoop
/usr/local/hadoop/bin/hadoop
