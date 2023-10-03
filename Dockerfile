FROM python:3.9

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src


WORKDIR src


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]