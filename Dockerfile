FROM python:3.11-slim

WORKDIR /app

RUN pip install aider-chat

EXPOSE 8080

CMD ["aider", "--help"]
