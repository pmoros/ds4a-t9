FROM python:3.7.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip uninstall --yes werkzeug
RUN pip install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.3.tar.gz

EXPOSE 8050

CMD ["python", "app.py"]