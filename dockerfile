FROM python:3.6

RUN pip3 install requests PyYAML

ADD opensyslog_helper.py opensyslog_syslog.py main_opensyslog.py /

CMD ["python", "./main_opensyslog.py"]
