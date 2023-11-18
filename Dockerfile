FROM python:3.8-slim-buster

RUN apt update -y && \
    apt install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt \
    --upgrade accelerate \
    && pip uninstall -y transformers accelerate \
    && pip install transformers accelerate

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache

CMD ["python", "app.py"]