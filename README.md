Python RESTful API
-------------
This project is designed to be a starting point for those building a RESTful API for data processing using python.  Providers like Amazon (and many others) do offer some common machine learning APIs at users' convenience but there are times when you need to implement your own methods for solving specific problems.

After checking out the code and run a few commands, you will have a web service running in Docker.   This example API comes with some core features considered important for hosting data processing API in the public cloud:
- *Security* - Secure and restrict access to API by enabling **SSL** and **HTTP authentication**
- *Logging* - **File and console logging** for diagnostic purposes, supports different logging level
- *Deployment* - Simple build and run scripts for setting up the web service to run inside **Docker**
- *JSON request* - Processing **JSON data in HTTP request/response** with CherryPy

#### Requirements
- OS: Linux (e.g. Ubuntu 16.04)
- Docker CE installed
- Postman installed (use for testing the API)
<br/>

## Dockerfile explained
``` 
From python:3.6.4-slim-jessie
```
- The docker image built for this API is based on the published python 3.6.4 docker image.
<br />

``` 
RUN pip install cherrypy==11.0
RUN pip install pandas==0.20.3
RUN pip install numpy==1.13.1
```
- First, some python packages need to be installed. Cherrypy is required for running the web service, plus other packages required for data processing.
<br />

``` 
WORKDIR /ws
ADD ws.py .
RUN mkdir logs
```
- Next, a working directory called *ws* is created for storing the python script, data files and log files
<br />

```
ENTRYPOINT ["python", "/ws/ws.py"]
CMD ["--logLevel", "INFO"]
``` 
- Finally, the ENTRYPOINT defines the command to run when the container starts up - i.e. python /ws/ws.py.  The subsequent CMD command defined the default arguments to be passed into ws.py, here the log level is default to INFO.  You can override these default parameters when using the docker run - an example would be to enable ssl using the --ssl parameter, the full command is provided later in this post.

## Installation: 
### Build Docker image
- Clone this project
- This API uses HTTP basic authentication to authenticate the HTTP request.  Open file *ws.py* and change the username and password stored in the MY_USERS variable:
```
MY_USERS = {'myuser': 'password_for_myuser'}
```
- [Optional] To enable SSL, put the certificate and private key into the project directory and named them as *cert.pem* and *privkey.pem* respectively

- Navigate to project directory and build the docker image with a tag specified:
```
docker build -t cherrypy-ws .
```
<br/>

## Web Service python script explained
Cherrypy

### Start web service
- Run docker container:
```  
docker run -p 8080:8080 cherrypy-ws:latest
```
If the web service starts successfully, these logging statements should appear in the console:
```
[10/Oct/2017:10:33:29] ENGINE Listening for SIGTERM.
[10/Oct/2017:10:33:29] ENGINE Listening for SIGHUP.
[10/Oct/2017:10:33:29] ENGINE Listening for SIGUSR1.
[10/Oct/2017:10:33:29] ENGINE Bus STARTING
[10/Oct/2017:10:33:29] ENGINE Started monitor thread 'Autoreloader'.
[10/Oct/2017:10:33:29] ENGINE Started monitor thread '_TimeoutMonitor'.
[10/Oct/2017:10:33:29] ENGINE Serving on http://0.0.0.0:8080
[10/Oct/2017:10:33:29] ENGINE Bus STARTED
```
- **Test Web Service is running** 
Open Postman.  Select GET request and enter this as the url:
```
http://localhost:8080/
```
Select the Authorization tab, choose 'Basic Auth' and enter your username and password. Click 'Send', the request should return a 'Hello' message as depicted below:
![postman_test](https://user-images.githubusercontent.com/30487789/31473845-5fa1cf98-af3a-11e7-8990-90bff866fc41.png)

## Consume API
- Open Postman.  Select POST request and enter this as the url:
```
http://localhost:8080/ml
```
- Select the Authorization tab, choose 'Basic Auth' and enter your username and password
- Select Body tab, check the 'raw' option if not checked.   Click the drop-down on the right and choose 'application/json' and put this JSON string in the text area  - {"num1" : [1, 2, 3], "num2":[4, 5, 6]}:

- The dataset will be extracted from the HTTP request, passed to MyProcessor.py, finally the results will be returned as a JSON string:
```
"{\"num1\":{\"mean\":2.0,\"min\":1.0,\"max\":3.0},\"num2\":{\"mean\":5.0,\"min\":4.0,\"max\":6.0}}"
```
![postman_json](https://user-images.githubusercontent.com/30487789/31473847-62221ebc-af3a-11e7-86d3-f8383375a448.png)
## Code Explained
- Coming soon

### Run options
#### Run with SSL enabled
Append --ssl to the docker command:
```
docker run cherrypy-ws:latest --ssl
```

#### Run in detached mode
Add -d flag:
```
docker run -d cherrypy-ws:latest
```
