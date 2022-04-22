FROM python
RUN pip install flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  project4.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/project4.py
