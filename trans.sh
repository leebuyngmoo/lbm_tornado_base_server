#/bin/sh
cd ..
pwd
timestamp=`date +%Y%m%d%H%M`
echo "$timestamp"
file_name='local_data_gateway'$timestamp

echo "$file_name"




tar -czvf $file_name.tar.gz local_data_gateway

echo 'complete zip state'
echo 'start scp ' 
sshpass -p 'krobis!321' scp $file_name.tar.gz  pi@192.168.30.55:/home/pi/gateway

echo ' complete scp state '

