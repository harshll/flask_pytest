FROM alpine:latest

WORKDIR /flask_pytest
COPY . .

# RUN pip3 install -r requirements.txt
RUN export FLASK_APP=sample.py
# RUN flask run

ENTRYPOINT [ "python" ]
CMD [ "/flask_pytest/sample.py" ]
