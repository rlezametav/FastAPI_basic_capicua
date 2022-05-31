# Basic Capicua with FastAPI and Docker

In your virtual env install  
<code> pip inatall fastapi </code>

To build use this  
<code> docker build -t fastapi_basic . </code>  
<code> docker run -d --name fastapi_container -p 80:80 fastapi_basic </code>