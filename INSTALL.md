##To run the app

1. `brew install pipenv`
2. `pipenv install`
3. `docker build docker/postgres -t jwan622/hinge-hw`
4. `docker run --rm -p 8000:5432 jwan622/hinge-hw`
in another terminal, `cd` into the project folder and:
5. `pipenv shell`
6. inside the shell run: `python3 runner.py`
- the above command forwards requests to port 8000 to 5432 internal to the postgres docker container. 
- running the docker container will execute the `CreateTables.sql` script in the container.
- running the `pyehon3 runner.py` command will populate the tables with rows.

### To access the database:
- `psql -h localhost -p 8000 -d postgres -U postgres --password`
password: `password`

If you've successfully run the `runner.py` script, you should be able to run:
`select count(*) from ad_events; select count(*) from user_events;`
and see:
```sql
 count
-------
  7186
(1 row)

 count
-------
  7186
(1 row)
```

###To run tests:

`pytest -vv`
- note all tests are in the tests folder
- the tests rely on some % of the dataset, including some error cases.



### Explanation of some decisions
- the loader returns a list of tuples as the data. If the data to be inserted is given as a list of tuples like in
```
data = [(1,'x'), (2,'y')]
``` 
then it is already in the exact required format as the values syntax of the insert clause expects a list of records as in:
```
insert into t (a, b) values (1, 'x'),(2, 'y')
```
So that's the driving motivation behind the `writer.py` code:
```python

    insert_query = f"insert into {RECORD_KEY_TO_TABLE_NAME[key]} {RECORD_KEY_TO_COLUMNS[key]} values {records_list_template}"
    connection = connect()
    try:
        cursor = connection.cursor()
        print(f"Inserting records into {RECORD_KEY_TO_TABLE_NAME[key]} table")
        cursor.execute(insert_query, records)
```

When cleaning the data, I got rid of rows that didn't have complete data since there was only one row. It appears in one of the files, there was a NUL byte which I got rid of:

```python
def clean_records(file):
    return csv.DictReader((line.replace('\0', '') for line in file))
```


and I get rid of rows without complete data (missing columns)
```python
for row in csv_reader:
    if validate_record(key, row):
        record = generate_record(key, row)
```

That's it. Thanks for the take home!
