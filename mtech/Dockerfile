FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY  ./ /app/
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "8001"]