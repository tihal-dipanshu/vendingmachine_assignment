FROM python:3.8-slim

COPY gen-py/ /gen-py/
COPY src/BeveragePreferenceService/beverage_service.py /

RUN pip install thrift

ENV PYTHONPATH=/

EXPOSE 9092

CMD ["python", "./beverage_service.py"] 