FROM python:3-alpine

WORKDIR /app

COPY . /app

# RUN pip3 install -r requirements.txt
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt && pip3 install gunicorn

COPY entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

CMD ["/entrypoint"]
