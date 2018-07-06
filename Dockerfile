From python:3.6.4-slim-jessie

RUN pip install cherrypy==11.0

# Example commands for installing other python packages required for your python code
RUN pip install pandas==0.20.3
RUN pip install numpy==1.13.1

WORKDIR /ws
ADD ws.py .
ADD myprocessor.py .
RUN mkdir logs

# Start web service
ENTRYPOINT ["python", "/ws/ws.py"]
CMD ["--logLevel", "INFO"]
