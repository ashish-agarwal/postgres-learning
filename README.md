# Tournament

Tournament project is about learning relational database by designing database for swiss round matches and implementing it using python and psql.

### Setup
The project setup involved two steps:
  - Python: This project uses python to create site. Head to [python-installation] link to setup it on your system.
  - Source Code: It is available on [github]. You can clone the project using ```git clone``` command or if you want to contribute to it then fork the project.
```bash
  $ git clone https://github.com/ashish-agarwal/learning-postgres
```

### Running
You need to write `SQL` in the `tournament.sql` file to create database and tables.
Run below commands to see what tests are failing. We are here using `test-driven` approach
of software development.
```python
    $ python tournament_test.py
```
This will show all the test which are failing and now move on the `tournament.py` file where you need to implement the require methods to completely pass the tests.

### Modules
There are three modules in the projects
  - ```tournament.py:``` This is module where all the queries related to database has been called using python `psycopg2` API.
  - ```tournament.sql```: This is the `SQL` file for creating tables for the tournament app.
  - ```tournament_test.py```: Unit test file to test all the


[python-installation]: <https://docs.python.org/2/using>
[github]: <https://github.com/ashish-agarwal/learning-postgres>