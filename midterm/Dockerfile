FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "house_price_model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "—bind 0.0.0.0.:9696", "predict-test::app"]