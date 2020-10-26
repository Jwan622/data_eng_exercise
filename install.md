**To run the app**

1. `brew install pipenv`
2. `docker build docker/postgres -t jwan622/hinge-hw`
3. `docker run --rm -p 8000:5432 jwan622/hinge-hw`
- the above command forwards requests to port 8000 to 5432 internal to the docker containe which is where postgres running. 




__To access the database:__
- `psql -h localhost -p 8000 -U postgres --password`
