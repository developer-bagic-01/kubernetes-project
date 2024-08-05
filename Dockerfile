FROM python:latest

RUN pip install requests

COPY load_test.py /scripts/load_test.py

CMD ["python", "/scripts/load_test.py"]

