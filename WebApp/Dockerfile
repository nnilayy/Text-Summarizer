FROM python
COPY requirements.txt /requirements.txt
WORKDIR /usr/src/myapp
RUN pip install -r /requirements.txt
COPY . /usr/src/myapp
# EXPOSE 5000
CMD ["python","app.py"]
