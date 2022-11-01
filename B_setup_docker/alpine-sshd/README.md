### Docker-compose

[Docker-compose](https://docs.docker.com/compose/features-uses) is a tool set
for Docker to automate building, configuring and running containers from a single file:
[docker-compose.yaml](https://docs.docker.com/compose/compose-file) specification.

Containers are referred to as *services* in the Docker-compose specification.

When a specified image does not exist and the build-tag of a service refers to a
directory where the container can be built from a
[Dockerfile](https://docs.docker.com/engine/reference/builder) (must be in same
directory of `docker-compose.yaml`):
```
docker-compose up -d
```
will automatically perform these steps (`-d` starts container in background):
1. build the image from `Dockerfile`,
1. register the image locally,
1. create a new container from the image,
1. register the container locally and
1. start it.

Multilpe containers can be specified in a single `docker-compose.yaml` file and
started in a defined order expressed by dependencies (`depends_on`-tag, e.g. to
express that a database service must be started before an application service
that is depending on it).

To stop all services specified in a `docker-compose.yaml` file:
```
docker-compose stop
```

To (re-)start services and show their running states:
```
docker-compose start
docker-compose ps
```

The `alpine-sshd` container can therefore always fully be re-produced from the
specifications in this directory.

Images and containers should always be reproduceable. They can be deleted any
time and recovered from specifications.

Container specifications are therefore common in code repositories controlling
automated *build-* and *deployment*-processes.

The principle implies that state ("data" such as databases) should not be
stored in containers and rather reside on outside volumes that are
[mounted](https://docs.docker.com/storage/volumes)
into the container.

Build and start `alpine-sshd` container from scratch:
```
docker-compose up
[+] Running 0/1
 - alpine-sshd Error                                                       2.5s
[+] Building 0.3s (23/23) FINISHED
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 32B                                        0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/alpine:latest           0.0s
 => [ 1/18] FROM docker.io/library/alpine:latest                           0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 34B                                           0.0s
 => CACHED [ 2/18] RUN apk update                                          0.0s
 => CACHED [ 3/18] RUN apk add --no-cache openrc                           0.0s
 => CACHED [ 4/18] RUN apk add --update --no-cache openssh                 0.0s
 => CACHED [ 5/18] RUN apk add --no-cache sudo                             0.0s
 => CACHED [ 6/18] RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd  0.0s
 => CACHED [ 7/18] RUN echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_c  0.0s
 => CACHED [ 8/18] RUN echo 'IgnoreUserKnownHosts yes' >> /etc/ssh/sshd_c  0.0s
 => CACHED [ 9/18] RUN adduser -h /home/larry -s /bin/sh -D larry          0.0s
 => CACHED [10/18] RUN echo -n 'larry:' | chpasswd                         0.0s
 => CACHED [11/18] RUN mkdir -p /etc/sudoers.d                             0.0s
 => CACHED [12/18] RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudo  0.0s
 => CACHED [13/18] RUN adduser larry wheel                                 0.0s
 => CACHED [14/18] RUN ssh-keygen -A                                       0.0s
 => CACHED [15/18] RUN rc-update add sshd default                          0.0s
 => CACHED [16/18] RUN mkdir -p /run/openrc                                0.0s
 => CACHED [17/18] RUN touch /run/openrc/softlevel                         0.0s
 => CACHED [18/18] COPY entrypoint.sh /                                    0.0s
 => exporting to image                                                     0.1s
 => => exporting layers                                                    0.0s
 => => writing image sha256:5664d856423d679de32c4b58fc1bb55d5973acb62507d  0.0s
 => => naming to docker.io/library/alpine-sshd                             0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and l
earn how to fix them
[+] Running 2/2
 - Network alpine-sshd_default          C...                               0.1s
 - Container alpine-sshd-alpine-sshd-1  Created                            0.2s
Attaching to alpine-sshd-alpine-sshd-1
alpine-sshd-alpine-sshd-1  | Server listening on 0.0.0.0 port 22.
alpine-sshd-alpine-sshd-1  | Server listening on :: port 22.
```


Show running container:
```
docker-compose ps
NAME                        COMMAND           SERVICE       STATUS                PORTS
alpine-sshd-alpine-sshd-1   "/entrypoint.sh"  alpine-sshd  running   0.0.0.0:22->22/tcp
```


Log in as user *larry* that was configured when the container was built from
the `Dockerfile`:
```
ssh larry@localhost
```

Output:
```
ssh larry@localhost
The authenticity of host 'localhost (::1)' can't be established.
ED25519 key fingerprint is SHA256:5ZZ4bnRJh3DxlDaWJooC1qYjKj00U+pHCuNGEWZPVqA.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/cygdrive/c/Sven1/svgr/.ssh' (No such file or directory).
Failed to add the host to the list of known hosts (/cygdrive/c/Sven1/svgr/.ssh/known_hosts).
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <http://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

85dbbb7c316a:~$ ls -la
total 16
drwxr-sr-x    1 larry    larry         4096 Nov  1 12:48 .
drwxr-xr-x    1 root     root          4096 Oct  7 18:31 ..
-rw-------    1 larry    larry            7 Nov  1 12:48 .ash_history
85dbbb7c316a:~$ whoami
larry
85dbbb7c316a:~$ pwd
/home/larry
85dbbb7c316a:~$
```


Stop container:
```
docker-compose stop

 - Container alpine-sshd-alpine-sshd-1  Stopped                            0.3s

docker-compose ps
NAME                        COMMAND           SERVICE       STATUS
        PORTS
alpine-sshd-alpine-sshd-1   "/entrypoint.sh"  alpine-sshd   exited (0)
```


Restart same container:
```
docker-compose start
[+] Running 1/1
 - Container alpine-sshd-alpine-sshd-1  Started                            0.4s

docker-compose ps
NAME                        COMMAND           SERVICE       STATUS                PORTS
alpine-sshd-alpine-sshd-1   "/entrypoint.sh"  alpine-sshd  running   0.0.0.0:22->22/tcp

```
