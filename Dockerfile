FROM python:3.10-slim

COPY main.py /main.py

WORKDIR /
ENTRYPOINT ["python", "main.py"]
