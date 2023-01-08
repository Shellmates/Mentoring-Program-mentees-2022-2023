FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server sudo

RUN useradd -m -s /bin/bash ctf && \
    useradd --no-create-home ctf-cracked && \
    echo 'ctf:ctf' | chpasswd

WORKDIR /home/ctf

COPY challenge/flag.txt .
COPY challenge/perms /etc/sudoers.d/

RUN chown -R root:root . && chmod 555 . 
RUN chown ctf-cracked:ctf-cracked flag.txt && chmod 400 flag.txt

RUN ln -s /dev/null .bash_history
RUN chmod -r /tmp /var/tmp
RUN chmod go-rx /usr/bin/passwd
EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
