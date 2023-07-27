FROM python:3.7.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /gain_miles_online_test
RUN apt-get update && apt-get install -y vim dos2unix
COPY requirements.txt /gain_miles_online_test/
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y default-mysql-client
RUN pip install -r requirements.txt
COPY . /gain_miles_online_test/
COPY entrypoint.sh /gain_miles_online_test/entrypoint.sh
RUN dos2unix /gain_miles_online_test/entrypoint.sh
RUN chmod +x /gain_miles_online_test/entrypoint.sh
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/gain_miles_online_test/entrypoint.sh"]
EXPOSE 8000
