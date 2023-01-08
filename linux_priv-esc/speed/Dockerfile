FROM python:3.10

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server sudo systemd rsyslog cron psmisc

RUN useradd -M -s /bin/bash ctf-cracked

RUN useradd -M -s /bin/bash ctf

RUN echo 'ctf:ctf' | chpasswd

RUN usermod -aG sudo ctf

RUN mkdir /challenge

WORKDIR /challenge

COPY challenge/ .

RUN chown root:ctf-cracked flag.txt read.py
RUN chmod 440 flag.txt
RUN chmod 554 read.py

COPY challenge/sudoers /etc/sudoers
COPY challenge/sshd_config /etc/ssh/sshd_config
RUN echo "* * * * * root	rm -rf /tmp/*" >> /etc/crontab 
RUN echo "*/30 * * * * root	killall -u ctf && killall -u ctf-cracked" >> /etc/crontab

RUN find -perm /o=w -exec chmod '-r' '{}' \;
RUN chmod go-rx /usr/bin/passwd
ENTRYPOINT service cron start \
	    && service rsyslog start \
	    && service ssh start \
	    && tail -f --retry /var/log/auth.log
