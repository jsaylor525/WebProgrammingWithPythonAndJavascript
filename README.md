# Homework Repository for the CS50 course on [edX](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/)

## [Project 0](project0/index.html)
Simple HTML & CSS project using some SASS and bootstrap

[Online URL](https://jsaylor525.github.io/WebProgrammingWithPythonAndJavascript/)

# SQL

Everyway SQL keywords are in all caps, ex. ```SELECT * FROM table``` where "SELECT" and "FROM" are keywords. However,
while playing around in the psql environment it was case insensitive for these keywords. 

## Postgres

Nightmare... no details on how to create a local database. Took 3 hours to figure this shit out.

---

```postgres
createdb.exe -U postgres -O jsaylor lecture4
```
Creates a database with the postgres superuser (manditory on Windows 10) and transfers ownership to user.

* createdb.exe the postgres binary to create a database for Postgres 10.0
* -U the user to create the database; in this case postgres
* -O the owner username; in this case jsaylor
* lecture4 is the name of the database 

In windows powershell the input is not echoed... not sure how to fix this but it is super annoying.

Update: Seems like this was only in VS Code terminal... Launching Powershell from Winodws Env character echo works fine.

---

Seriousally this class is wasting so much time trying to figure out all the deltas on Windows. No where did it say
who to login to database with no password, which without that detail makes create.py is useless.

```bat
REM These settings are required for create.py to work, the PG variables
REM are needed in windows. If they don't exist we can't create the db via python
SET DATABASE_URL=postgres://localhost/lecture4
SET PGUSER=jsaylor
SET PGPASSWORD=password
````
