FROM python:3.5-alpine

LABEL maintainer="erenguven0@gmail.com"

WORKDIR /root

COPY README.md requirements.txt requirements-test.txt setup.py ./
RUN pip install -r requirements-test.txt

COPY secrets2env.py ./
RUN python setup.py install

CMD ["secrets2env"]
