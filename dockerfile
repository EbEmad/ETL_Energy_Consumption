FROM python:3.8


WORKDIR /app

COPY reqirements.txt reqirements.txt 
RUN pip install -r reqirements.txt 

COPY etl/ /etl

COPY data/ /data

ENTRYPOINT [ "python","/etl/load.py" ]
