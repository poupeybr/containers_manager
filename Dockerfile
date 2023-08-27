FROM python:3.11.4
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
WORKDIR /opt/app
ENTRYPOINT ["python", "./app.py"]
