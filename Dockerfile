
FROM debian:bullseye-slim as  base

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3 python3-pip python3-gi

RUN pip3 install --upgrade pip

COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-u", "main.py"]
