Welcome to the Qoute_app basics on django Python. Down here is info how to use it:
1.In directory 'qoutes' you need to create file '.env' that must contains next settings according to your 'docker_compose.yml' and 'quotes/settings.py' setups.
  Here is how it should to be looks like:
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_PORT=
2.Run a Docker container according to 'docker_compose.yml' and make MongoDB container that have to contains at least 'localhost:27017'
3.You need fill the MongoDB with running 'utils/add_quotes_to_mongo.py'
4.You need to migrate all of the info from MongoDB to PostgreSQL. For it go to the directory quotes where 'manage.py' is, open a 'utils.migration.py' and run the command in terminal 'py -m utils.migration'.
5.Make the internal migration using 'python manage.py makemigrations' in terminal and than external migration 'python manage.py migrate' in terminal as well.
6.After it u can run the server and observe the project using 'python manage.py runserver' in terminal and open the follow the link 'http://127.0.0.1:8000/' in your browser.
