FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server 


RUN useradd -m -s /bin/bash ctf
RUN echo 'ctf:ctf' | chpasswd

#COPY THE flag.txt FILE FROM LOCAL TO THE CONTAINER
COPY challenge/flag.txt /home/ctf/.flag.txt
COPY challenge/fake_flag.txt /home/ctf/fake_flag.txt

#WORKING DIRECTORY
WORKDIR /home/ctf

#PERMS OF READING THE FILE
RUN chown -R root:ctf /home/ctf 
RUN chmod 550 /home/ctf 
RUN chmod o-r /tmp/ /var/tmp/ 
#MAKE A LINK TO 
RUN ln -s /dev/null .bash_history

#LISTENING TO PORT 22
EXPOSE 22
#ALWAYS RUN ssh AND DISCARD STDOUT STDERR FROM AN OUTPUT
ENTRYPOINT service ssh start && tail -f /dev/null