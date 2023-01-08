FROM python:3-alpine


RUN mkdir  /ctf/ 

COPY app /ctf/app

WORKDIR /ctf/app
 
RUN pip install -r requirements.txt
				   
EXPOSE 1337

USER nobody

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "-p", "1337"]
