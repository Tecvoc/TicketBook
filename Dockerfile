FROM python:3.8

RUN mkdir /home/work

COPY requirements.txt /home/work
COPY src /home/work

WORKDIR /home/work

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver"]
