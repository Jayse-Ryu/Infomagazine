FROM python:3.7

COPY . ./home

WORKDIR /home

RUN pip install --upgrade pip

RUN pip install pipenv

RUN pipenv install --system

RUN apt-get update && apt-get install -y uwsgi-plugin-python3 \
    && apt-get install -y uwsgi-plugin-python && apt-get install -y vim \
    && apt-get install -y git

RUN pip install uwsgi && pip install git+https://github.com/Supervisor/supervisor

RUN chmod +x /home/docker/prod/config/run.sh

CMD /home/docker/prod/config/run.sh