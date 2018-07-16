# WebDevExercise
Exercise for Web Development Course

1. Tal Bokobza
2. Tehilla Or

# Notes:
* In case of Invalid Input in the request we set the display to ="Invalid Input".
* In case of error in the request we set the display to ="Error".
* Supporting on Float numbers calculations (for example "6.2/4").

# Overview:
* This project was written in python 3.6.4
* Used tornado server as our HTTP server
* Used unittest and tornado.testsing for our unit and integration tests

# Run:
* Clone the project
* CD project root dir
* run "docker-compose up -d" 
* run "docker ps" to check all 5 containers are up
* find the external port of the backend container, browse to localhost:port. 

# Test:
-	for unittets run "docker exec -it currency-calculator python unittests.py"
-	for integration tets run "docker exec -it currency-calculator python integration_tests.py"
