FROM python:3.11
WORKDIR /geoly
COPY requirements.txt /geoly//
RUN pip install -r requirements.txt
COPY . /geoly
CMD python bot/geoly.py