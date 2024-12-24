FROM python:3.12

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -e .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
