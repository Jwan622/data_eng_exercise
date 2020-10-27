**To run the app**

1. `brew install pipenv`
2. `docker build docker/postgres -t jwan622/hinge-hw`
3. `docker run --rm -p 8000:5432 jwan622/hinge-hw`
- the above command forwards requests to port 8000 to 5432 internal to the postgres docker container. 
- running the docker container will execute the `CreateTables.sql` script in the container.

__To access the database:__
- `psql -h localhost -p 8000 -U postgres --password`


**To run tests**
`pytest -vv`
- note all tests are in the tests folder
- the tests rely on some % of the dataset, including some error cases.



**Explanation of some decisions**
- the loader returns a list of tuples as the data. If the data to be inserted is given as a list of tuples like in
```
data = [(1,'x'), (2,'y')]
``` 
then it is already in the exact required format as the values syntax of the insert clause expects a list of records as in:
```
insert into t (a, b) values (1, 'x'),(2, 'y')
```
