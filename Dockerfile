FROM python:latest
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
WORKDIR /opt/app
CMD ["python", "main.py"]
