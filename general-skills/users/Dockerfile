FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server

RUN useradd -m -s /bin/bash ctf
RUN useradd -M shellmates{gg_Y0u_F0Und_M3} 
RUN echo "ctf:ctf" | chpasswd

RUN chown -R root:ctf /home/ctf 
RUN chmod 550 /home/ctf 
RUN chmod o-r /tmp/ /var/tmp/ 

WORKDIR /home/ctf

RUN ln -s /dev/null .bash_history
EXPOSE 22

ENTRYPOINT service ssh start && tail -f /dev/null
