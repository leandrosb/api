FROM python:3.7-alpine

COPY README.md CHANGELOG.md 
RUN addgroup -S flask & adduser -S flask -g flask
COPY ./microbot /microbot
RUN chmod -R 775 /microbot
USER flask
WORKDIR /microbot
RUN pip install -r requirements.txt --user



CMD ["/bin/bash", "-c", "python3 -m main"]
