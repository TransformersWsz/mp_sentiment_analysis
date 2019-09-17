FROM python:3.6
RUN mkdir -p /opt/django_web
WORKDIR /opt/django_web
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /opt/django_web
RUN pip install -r /opt/django_web/requirements.txt
RUN rm -rf /opt/django_web
COPY . /opt/django_web
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8080"]