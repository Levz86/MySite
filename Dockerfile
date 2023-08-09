FROM pypy:latest
WORKDIR /mySite
COPY . .
CMD python manage.py