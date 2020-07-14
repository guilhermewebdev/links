FROM python

ENV PYTHONUBUFFERED 1

RUN adduser -DmU api; 
USER api

ADD requirements.txt ~

RUN pip install -r requirements.txt --user;

COPY . ~