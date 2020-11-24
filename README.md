# Carparts

## Gettings started

1. Modify docker-compose.yml with username and password for database
1. Run `docker-compose up`
1. Modify `App/DB/alembic.ini` with username and password for database
1. Run `alembic upgrade head`
1. Modify `App/DB/db_settings/__init__.py` with username and password for database
1. Execute `Database/carparts_data.sql` to load test data into database
1. Run `main.py`


## Todo / Improvements

1. Update & Delete cascade 
1. Errors handling
1. Edit view all fuction (table name), and make it nice presentation. 