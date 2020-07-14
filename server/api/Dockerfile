FROM python

ENV PYTHONUBUFFERED 1
ENV PATH /home/api/.local/bin:$PATH

RUN useradd -m api; pip install --upgrade pip;

WORKDIR /home/api

ADD requirements.txt .

ADD main.sh .

RUN chmod +x main.sh;

USER api

RUN pip install -r requirements.txt --user;

COPY . .