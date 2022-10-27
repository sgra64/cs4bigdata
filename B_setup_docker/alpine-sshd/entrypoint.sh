#!/bin/sh
# ssh-keygen -A
exec /usr/sbin/sshd -D -e "$@"
# /etc/init.d/sshd start
# service sshd restart
