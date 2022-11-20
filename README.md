# Docker_Task
# Docker final task
In this task we have 3 sections:
-  Create a Python APP (Flask Based).
-  Dockerize the applications (Create Dockerfile).
-  Create a Jenkinsfile for CI/CD that creates and pushes the generated Docker image to Docker Hub.


## ✨Python APP- Features:
1-  Presents the Current Bitcoin Price in USD.

2-  Presents the Average Price for the last 10 minutes.


>This is a flask App that requires flask and requests packages to be installed.


<img width="763" alt="113" src="https://user-images.githubusercontent.com/72957443/202928441-9d3651dc-4512-4fd5-ad2c-f45ffb4ab2b3.png">

## Run the app
1-install python 3.10. 

2-install the requirements 
```sh
pip install -r requirements.txt
```
3- Clone and run the app:

```sh
git clone https://github.com/SewarDarawshe/DockerFinalTask.git

python ./main.py
```

now you can access the app using : http://localhost:3000/  .

![Screenshot]



## ✨Dockerize the applications:
 import python: 
```sh
FROM python:3.10.0-alpine3.13
```
 copy the requirements.txt: 
```sh
COPY ./requirements.txt requirements.txt
```
install the required packages:
```sh
RUN pip install -r requirements.txt
```
 Copy: lets us copy a file (or files) from the host system into the image: 
```sh
COPY . .
```
 Expose the port of the flask app: 
```sh
EXPOSE 3000
```
 Run: 
```sh
CMD [ "python", "./main.py" ]
```

> In order to successfully push the generated Docker image to
Docker Hub using Jenkins, a repository was created in the Docker hub :
<img width="1017" alt="11" src="https://user-images.githubusercontent.com/72957443/202928319-0c89f2ff-04e9-49ad-b993-792d6a39c11a.png">





## ✨Jenkinsfile & Dockerhub :

>Docker must be installed on the Jenkins server, for more info use this link : https://docs.docker.com/engine/install/ubuntu/

>you must also link and add your Docker credentials in Jenkins.
(your dockerhub username and one of the  Access Tokens as password).

This is a Master job pipeline, that clones my repository from Github, builds an image, and pushes it to the douckerhub.


## 
##





