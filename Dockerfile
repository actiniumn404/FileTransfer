FROM python:3.8-buster
WORKDIR /opt/app/FileTransfer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8008
CMD ["python", "main.py"]