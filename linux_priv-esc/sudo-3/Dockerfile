FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install openssh-server sudo cron cowsay && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash ctf && \
    useradd --no-create-home ctf-cracked && \
    echo 'ctf:ctf' | chpasswd 

COPY challenge/flag.txt /flag.txt

RUN chown -R root:root /home/ctf/ && chmod 555 /home/ctf/
RUN chown root:ctf-cracked /flag.txt && chmod 440 /flag.txt

COPY challenge/perms /etc/sudoers.d/

RUN ln -s /dev/null /home/ctf/.bash_history 
RUN echo "*/15 * * * * root	rm -rf /tmp/*" >> /etc/crontab 
RUN chmod -r /tmp /var/tmp /run/lock
RUN chmod go-rx /usr/bin/passwd
ENTRYPOINT service cron start \
	    && service ssh start \
	    && tail -f /dev/null

