FROM python:3.8

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install --use-feature=2020-resolver -r requirements.txt

CMD python /app/app_test_data.py



