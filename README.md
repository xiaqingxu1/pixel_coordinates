# Pixel Coordinates Finder
Simple Flask app that allows finding pixel coordinates based on user-defined image dimension and corners through HTTP requests. This web server can handle normal FORM HTTP requests to [http://localhost:5000/](http://localhost:5000/). 


## Usage:
The easier way to run this web service is to run it through a Docker container. The web service is packed in a Docker container, which can be found [here](https://hub.docker.com/r/xuxiaqing2011/pixels). In order to be able to pull and run a Docker container, you'll need [Docker](https://docs.docker.com/get-docker/) installed if you haven't already done so.

## Commands
#### Pull down container 
```bash
docker pull xuxiaqing2011/pixels
```
#### Run container in port 5000 and detached mode(optional)
```bash
docker run -p 5000:5000 -d xuxiaqing2011/pixels
```
#### Now GET/POST request can be sent to [http://localhost:5000](http://localhost:5000)
* ###### GET request
```bash
curl http://localhost:5000
```
* ###### POST request
```bash
curl -d "r=3&c=3&x1=1&y1=1&x2=3&y2=3&x3=1&y3=3&x4=3&y4=1" -X POST http://127.0.0.1:5000 
```
Note: Content-Type: application/x-www-form-urlencoded

In addition, if you have previously run the container in detached mode, the web service then can be accesed through your browser. Navigate to http://localhost:5000 .   

A GET request renders the form where image dimension and corner coordinates can be entered and submitted, so that a POST request can do the calculation and display the result. 





