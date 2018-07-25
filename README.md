Python RESTful Web Service
-------------
Building a RESTful web service for data processing using Python
   
This example web service comes with some core features considered important for hosting web service in the public cloud:
- *Security* - Secure and restrict access by enabling **SSL** and **HTTP authentication**
- *Logging* - **File and console logging** for diagnostic purposes, supports different logging level
- *Deployment* - Simple build and run scripts for setting up the web service to run inside **Docker**
- *JSON request* - Processing **JSON data in HTTP request/response** with CherryPy
After checking out this project and run a few commands, you will have a web service running in Docker.

#### Requirements
- Linux (e.g. Ubuntu 16.04)
- Docker CE or EE installed
- Postman installed (use for testing)
<br/>

## Dockerfile explained
``` 
From python:3.6.4-slim-jessie
```
<br />

``` 
RUN pip install cherrypy==11.0
RUN pip install pandas==0.20.3
RUN pip install numpy==1.13.1
```
- The above commands install the required Python packages.  Cherrypy is the web framework for serving the web service and the other are some common packages used for data manipulations.
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
- Finally, the ENTRYPOINT defines the command to run when the container starts up - i.e. python /ws/ws.py.  The subsequent CMD command defines the default arguments to be passed into ws.py, e.g. set log level to INFO.  These parameters can be overwritten in the docker run command (Refer to the ssl example later in this README file).

## Installation: 
### Build Docker image
- Clone this project
- This web service uses HTTP basic authentication.  Edit *ws.py* and change the username and password stored in the MY_USERS variable:
```
MY_USERS = {'myuser': 'password_for_myuser'}
```
- [Optional] To enable SSL, put the certificate and private key into the project directory and name them as *cert.pem* and *privkey.pem*

- Navigate to project directory and build the docker image with a tag:
```
docker build -t cherrypy-ws .
```
<br/>

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
Open Postman.  Select GET request and enter this URL:
```
http://localhost:8080/
```
Select the Authorization tab, choose 'Basic Auth' and enter your username and password. Click 'Send', the request should return a 'Hello' message as depicted below:
![postman_test](https://user-images.githubusercontent.com/30487789/31473845-5fa1cf98-af3a-11e7-8990-90bff866fc41.png)

## Consume Web Service
- Open Postman.  Select POST request and enter this URL:
```
http://localhost:8080/ml
```
- Select the Authorization tab, choose 'Basic Auth' and enter your username and password
- Select Body tab.  Ensure the 'raw' option if not checked.   Click the drop-down on the right and choose 'application/json' and put this JSON string in the text area  - {"num1" : [1, 2, 3], "num2":[4, 5, 6]}:

- The dataset will be extracted from the HTTP request, passed to MyProcessor.py, finally the results will be returned as a JSON string:
```
"{\"num1\":{\"mean\":2.0,\"min\":1.0,\"max\":3.0},\"num2\":{\"mean\":5.0,\"min\":4.0,\"max\":6.0}}"
```
![postman_json](https://user-images.githubusercontent.com/30487789/31473847-62221ebc-af3a-11e7-86d3-f8383375a448.png)


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
