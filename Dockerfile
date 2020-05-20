FROM python:3.7-alpine
COPY . /fsociety
WORKDIR /fsociety
RUN apk --update add git
RUN pip install -e .
CMD fsociety