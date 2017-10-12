{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf810
{\fonttbl\f0\fnil\fcharset204 PTSans-Regular;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Bold;
}
{\colortbl;\red255\green255\blue255;\red72\green72\blue72;\red251\green251\blue251;\red109\green109\blue109;
\red109\green109\blue109;\red39\green39\blue39;\red16\green60\blue192;}
{\*\expandedcolortbl;;\cssrgb\c35294\c35294\c35294;\cssrgb\c98824\c98824\c98824;\cssrgb\c50196\c50196\c50196\c60000;
\cssrgb\c50196\c50196\c50196\c40000;\cssrgb\c20392\c20392\c20392;\cssrgb\c6667\c33333\c80000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11100\viewh8700\viewkind0
\deftab720
\pard\pardeftab720\sl540\partightenfactor0

\f0\b\fs50\fsmilli25200 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 RESTful API for data processing using Python CherryPy\
-------------
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 This project is designed to be a starting point for those building a RESTful API for data processing using python.  Providers like Amazon and Azure do offer some common machine learning tools and libraries at users' convenience but there are times when you need to implement your own python code solve complex problems.  \
\
After checking out the code and run a few commands, you will have a web service running in Docker.   This example API comes with some core features considered important for hosting a data processing API in the public cloud:\
\pard\pardeftab720\sl460\partightenfactor0

\i \cf4 \strokec4 *\cf2 \strokec2 Security\cf4 \strokec4 *
\i0 \cf2 \strokec2  - Secure and restrict access to API by enabling 
\b \cf4 \strokec4 **\cf2 \strokec2 SSL\cf4 \strokec4 **
\b0 \cf2 \strokec2  and 
\b \cf4 \strokec4 **\cf2 \strokec2 HTTP authentication\cf4 \strokec4 **
\b0 \cf2 \strokec2 \

\i \cf4 \strokec4 *\cf2 \strokec2 Data Transfer\cf4 \strokec4 *
\i0 \cf2 \strokec2  - Processing csv files in 
\b \cf4 \strokec4 **\cf2 \strokec2 HTTP multipart request\cf4 \strokec4 **
\b0 \cf2 \strokec2 \

\i \cf4 \strokec4 *\cf2 \strokec2 Logging\cf4 \strokec4 *
\i0 \cf2 \strokec2  - Enable 
\b \cf4 \strokec4 **\cf2 \strokec2 file and console logging\cf4 \strokec4 **
\b0 \cf2 \strokec2 , ability to customise logging level at startup \

\i \cf4 \strokec4 *\cf2 \strokec2 Deployment\cf4 \strokec4 *
\i0 \cf2 \strokec2  - Simple build and run scripts for setting up the web service to run inside 
\b \cf4 \strokec4 **\cf2 \strokec2 Docker\cf4 \strokec4 **
\b0 \cf2 \strokec2 \
*JSON request* - Processing **JSON data in HTTP request/response** with CherryPy\
\
\pard\pardeftab720\sl420\partightenfactor0

\fs39\fsmilli19800 \cf5 \strokec5 ####
\b \cf2 \strokec2 Requirements
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 OS: Linux (e.g. Ubuntu 16.04)\
\cf4 \strokec4 - \cf2 \strokec2 Docker CE installed\
\cf4 \strokec4 - \cf2 \strokec2 Postman installed (use for testing the API)\
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\f1\b0\fs32\fsmilli16200 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl540\partightenfactor0

\fs50\fsmilli25200 \cf5 \strokec5 ##
\b \cf2 \strokec2  Dockerfile
\b0\fs36 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6  \
From continuumio/miniconda3\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 This docker image is using continuumio/miniconda3 as the base image with python 3 pre-installed.  You can choose to start with other Linux images and install python 3 on top.\
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\fs32\fsmilli16200  
\f1\b0 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6  \
RUN pip install cherrypy==11.0\
RUN pip install pandas==0.20.3\
RUN pip install numpy==1.13.1\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Install cherrypy and other packages required for data processing \
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\fs32\fsmilli16200  
\f1\b0 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6  \
WORKDIR /ws\
ADD ws.py .\
RUN mkdir logs\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Create a working directory called 
\i \cf4 \strokec4 *\cf2 \strokec2 ws\cf4 \strokec4 *
\i0 \cf2 \strokec2  for storing the python script, data files and log files\
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\fs32\fsmilli16200  
\f1\b0 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
ENTRYPOINT ["python", "/ws/ws.py"]\
CMD ["--logLevel", "INFO"]\
\cf4 \strokec4 ```\cf6 \strokec6  
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 The ENTRYPOINT command defines the command to run when container starts up - i.e. python /ws/ws.py.  The subsequent CMD command defined the default arguments to be passed into ws.py.  You can override these default parameters when using the docker run, this will be discussed later.\
\
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\f1\b0\fs32\fsmilli16200 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl540\partightenfactor0

\fs50\fsmilli25200 \cf5 \strokec5 ##
\b \cf2 \strokec2  Installation: \
### Build Docker image
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Clone this project\
\cf4 \strokec4 - This API uses HTTP basic authentication to authenticate the HTTP request.  \cf2 \strokec2 Open file 
\i \cf4 \strokec4 *\cf2 \strokec2 ws.py\cf4 \strokec4 *
\i0 \cf2 \strokec2  and change the username and password stored in the MY_USERS variable:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
MY_USERS = \{'myuser': 'password_for_myuser'\}\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 [Optional] To enable SSL, put the certificate and private key into the project directory and named them as 
\i \cf4 \strokec4 *\cf2 \strokec2 cert.pem\cf4 \strokec4 *
\i0 \cf2 \strokec2  and 
\i \cf4 \strokec4 *\cf2 \strokec2 privkey.pem\cf4 \strokec4 *
\i0 \cf2 \strokec2  respectively\
\
\cf4 \strokec4 - \cf2 \strokec2 Navigate to project directory and build the docker image with a tag:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
docker build -t cherrypy-ws .\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 This will build a docker image and with tag 
\i \cf4 \strokec4 *\cf2 \strokec2 cherrypy-ws\cf4 \strokec4 *
\i0 \cf2 \strokec2 .\
\pard\pardeftab720\sl340\partightenfactor0

\f1\fs29\fsmilli14580 \cf6 \strokec6 <
\f2\b br
\f1\b0\fs32\fsmilli16200 />
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl540\partightenfactor0

\fs50\fsmilli25200 \cf5 \strokec5 ##
\b \cf2 \strokec2 # Start web service
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Run docker container:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6   \
docker run -p 8080:8080 cherrypy-ws:latest\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 If the web service starts successfully, these logging statements should appear in the console:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
[10/Oct/2017:10:33:29] ENGINE Listening for SIGTERM.\
[10/Oct/2017:10:33:29] ENGINE Listening for SIGHUP.\
[10/Oct/2017:10:33:29] ENGINE Listening for SIGUSR1.\
[10/Oct/2017:10:33:29] ENGINE Bus STARTING\
[10/Oct/2017:10:33:29] ENGINE Started monitor thread 'Autoreloader'.\
[10/Oct/2017:10:33:29] ENGINE Started monitor thread '_TimeoutMonitor'.\
[10/Oct/2017:10:33:29] ENGINE Serving on {\field{\*\fldinst{HYPERLINK "http://0.0.0.0:8080/"}}{\fldrslt \cf7 \ul \ulc7 \strokec7 http://0.0.0.0:8080}}\
[10/Oct/2017:10:33:29] ENGINE Bus STARTED\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - 
\b **\cf2 \strokec2 Test Web Service is running\cf4 \strokec4 **
\b0 \cf2 \strokec2  \
Open Postman.  Select GET request and enter this as the url:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
\pard\pardeftab720\sl360\partightenfactor0
{\field{\*\fldinst{HYPERLINK "http://localhost:8080/"}}{\fldrslt \cf7 \ul \ulc7 \strokec7 http://localhost:8080/}}\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 Select the Authorization tab, choose 'Basic Auth' and enter your username and password. Click 'Send', the request should return a 'Hello' message as depicted below:\
![postman_test](https://user-images.githubusercontent.com/30487789/31473845-5fa1cf98-af3a-11e7-8990-90bff866fc41.png)\
\
\pard\pardeftab720\sl540\partightenfactor0

\fs50\fsmilli25200 \cf5 \strokec5 ##
\b \cf2 \strokec2  Consume API
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Open Postman.  Select POST request and enter this as the url:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
\pard\pardeftab720\sl360\partightenfactor0
{\field{\*\fldinst{HYPERLINK "http://localhost:8080/ml"}}{\fldrslt \cf7 \ul \ulc7 \strokec7 http://localhost:8080/ml}}\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Select the Authorization tab, choose 'Basic Auth' and enter your username and password\
\cf4 \strokec4 - \cf2 \strokec2 Select Body tab, check the 'raw' option if not checked.   Click the drop-down on the right and choose 'application/json' and put this JSON string in the text area  - \{"num1" : [1, 2, 3], "num2":[4, 5, 6]\}:\
\
\cf4 \strokec4 - The dataset will be extracted from the HTTP request, passed to MyProcessor.py, finally the results will be returned as a JSON string:\cf2 \strokec2 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
"\{\\"num1\\":\{\\"mean\\":2.0,\\"min\\":1.0,\\"max\\":3.0\},\\"num2\\":\{\\"mean\\":5.0,\\"min\\":4.0,\\"max\\":6.0\}\}"\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 ![postman_json](https://user-images.githubusercontent.com/30487789/31473847-62221ebc-af3a-11e7-86d3-f8383375a448.png)\
\pard\pardeftab720\sl540\partightenfactor0

\fs50\fsmilli25200 \cf5 \strokec5 ##
\b \cf2 \strokec2  Code Explained
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \strokec4 - \cf2 \strokec2 Coming soon\
\
\pard\pardeftab720\sl460\partightenfactor0

\fs43\fsmilli21600 \cf5 \strokec5 ###
\b \cf2 \strokec2  Run options
\b0\fs36 \
\pard\pardeftab720\sl420\partightenfactor0

\fs39\fsmilli19800 \cf5 \strokec5 ####
\b \cf2 \strokec2 Run with SSL enabled
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 Append --ssl to the docker command:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
docker run cherrypy-ws:latest --ssl\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \
\pard\pardeftab720\sl420\partightenfactor0

\fs39\fsmilli19800 \cf5 \strokec5 ####
\b \cf2 \strokec2 Run in detached mode
\b0\fs36 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 Add -d flag:\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32\fsmilli16200 \cf4 \strokec4 ```\cf6 \strokec6 \
docker run -d cherrypy-ws:latest\
\cf4 \strokec4 ```
\f0\fs36 \cf2 \strokec2 \
}