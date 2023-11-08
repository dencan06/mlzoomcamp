FROM python:3.10-slim

RUN pip install pipenv==2023.10.24 bind

WORKDIR ./app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict_app.py", "predict_test.py", "house_price_model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "predict2:app", "--bind", "0.0.0.0:9696"]