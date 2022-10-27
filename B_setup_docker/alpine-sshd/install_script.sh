#######################################################################
# Steps to set up a bare Alpine container for ssh access.
#
# create and run bare Alpine container with name "alpine-ssh"
docker run --name alpine-ssh -p 22:22 -it alpine:latest

#######################################################################
# update package list and install all needed packages
#  - openrc, system services control system
#  - openssh, client- and server side ssh
#  - sudo, utility to enable root rights to users
#
apk update
apk add --no-cache openrc
apk add --update --no-cache openssh
apk add --no-cache sudo

# adjust sshd configuration
echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config
echo 'IgnoreUserKnownHosts yes' >> /etc/ssh/sshd_config

# add user larry with empty password
adduser -h /home/larry -s /bin/sh -D larry
echo -n 'larry:' | chpasswd

# add larry to sudo'ers list
mkdir -p /etc/sudoers.d
echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/wheel
adduser larry wheel

# generate host key in /etc/ssh, e.g. /etc/ssh/ssh_host_rsa_key.pub
ssh-keygen -A

# add sshd as service, start on boot [default], touch file to prevent error:
# "You are attempting to run an openrc service on a system which openrc did not boot."
# rc-update add sshd default
rc-update add sshd
mkdir -p /run/openrc
touch /run/openrc/softlevel

# start sshd - ssh larry@localhost now working
# /etc/init.d/sshd start
# service sshd start
# ---- exec prevents shell as parent process
# exec /usr/sbin/sshd -D -e &
exec /usr/sbin/sshd &
#
#######################################################################
#
# stop alpine-ssh container
docker stop alpine-ssh

# start alpine-ssh container, create root sh (exec requires a started container)
docker start alpine-ssh
docker exec -it alpine-ssh /bin/sh

# start sshd in container
/etc/init.d/sshd restart
service sshd restart

/etc/init.d/sshd status
service sshd status

#######################################################################
# build docker container "alpine-sshd" from Dockerfile, entrypoint.sh
# image file "alpine-sshd" is 18.5 MB

docker build -t alpine-sshd .

docker image ls
REPOSITORY      TAG       IMAGE ID       CREATED     SIZE
alpine-sshd     latest    0d286d424c80   1 min ago   18.5MB

docker run --name alpine-sshd -p 22:22 -it -d alpine-sshd:latest
docker start alpine-sshd
docker exec -it alpine-sshd /bin/sh
docker stop alpine-sshd

#######################################################################
# References:

# How to enable and start services on Alpine Linux
# https://www.cyberciti.biz/faq/how-to-enable-and-start-services-on-alpine-linux

# How to install OpenSSH server on Alpine Linux
# https://www.cyberciti.biz/faq/how-to-install-openssh-server-on-alpine-linux-including-docker
# https://wiki.alpinelinux.org/wiki/Setting_up_a_SSH_server

# How To Set Up a Firewall with Awall on Alpine Linux
# https://www.cyberciti.biz/faq/how-to-set-up-a-firewall-with-awall-on-alpine-linux/

# Add, Delete And Grant Sudo Privileges To Users In Alpine Linux
# https://ostechnix.com/add-delete-and-grant-sudo-privileges-to-users-in-alpine-linux/
#
#######################################################################
