FROM python:3

ENV FLASK_APP "index.py"

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# RUN pip uninstall flask-bootstrap bootstrap-flask
RUN pip install bootstrap-flask
ADD . /code/
EXPOSE 5000

CMD flask run --host=0.0.0.0
