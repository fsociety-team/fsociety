FROM python:3.7-alpine
COPY . /fsociety
WORKDIR /fsociety
RUN apk --update add git nmap
RUN pip install -e .
CMD fsociety --info