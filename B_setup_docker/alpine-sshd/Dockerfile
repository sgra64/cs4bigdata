#######################################################################
# Dockerfile to build image for Alpine container that has sshd daemon.
#
# Use bare Alpine image and install all needed packages:
#  - openrc, system services control system
#  - openssh, client- and server side ssh
#  - sudo, utility to enable root rights to users
#
FROM alpine:latest

RUN apk update
RUN apk add --no-cache openrc
RUN apk add --update --no-cache openssh
RUN apk add --no-cache sudo

# adjust sshd configuration
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config
RUN echo 'IgnoreUserKnownHosts yes' >> /etc/ssh/sshd_config

# add user larry with empty password
RUN adduser -h /home/larry -s /bin/sh -D larry
RUN echo -n 'larry:' | chpasswd

# add larry to sudo'ers list
RUN mkdir -p /etc/sudoers.d
RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/wheel
RUN adduser larry wheel

# generate host key
RUN ssh-keygen -A

# add sshd as service, start on boot [default], touch file to prevent error:
# "You are attempting to run an openrc service on a system which openrc did not boot."
RUN rc-update add sshd default
RUN mkdir -p /run/openrc
RUN touch /run/openrc/softlevel

# sshd is started in /entrypoint.sh
#
#######################################################################

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /
