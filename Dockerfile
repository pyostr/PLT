FROM python:3.10

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

RUN mkdir /plt

WORKDIR /plt

COPY req.txt /plt/

RUN pip install --upgrade pip && pip install -r req.txt

ADD . /plt/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]