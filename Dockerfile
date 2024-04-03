FROM python:3.11.7

# WORKDIR /db
# COPY ./db/UdemyNlayerDb.db /db/

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

#RUN apt-get install sqlite3

EXPOSE 5000
CMD python ./main.py 