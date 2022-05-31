FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

# docker build -t fastapi_basic .
# docker run -d --name fastapi_container -p 80:80 fastapi_basic