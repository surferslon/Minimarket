FROM python:3.10

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV SECRET_KEY="django-insecure-rh&o9sp2)^t2_!c%xp$k753wow$s2^zm7fc@vvn-zl%+mkp1y"
ENV DEBUG=1

RUN python -m pip install django django-rest-framework

ADD minimarket /usr/app
ADD data.json /usr/app/data.json

WORKDIR /usr/app/

RUN python manage.py migrate \
  && python manage.py loaddata data.json

EXPOSE 8000

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=minimarket.settings"]
