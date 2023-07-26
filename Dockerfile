FROM python:3.11.4
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
WORKDIR /opt/app
CMD python3 -m flask run --host=0.0.0.0 --port 7500