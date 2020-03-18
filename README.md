# Django SQL Middleware

A simple middleware aimed to capture all queries in a request and provide basic SQL profiling such
as execution time, execution plan, and query traceback.

This package is only intended to run in development mode for non-sqlite database.

Currently, this package only tested in projects that uses psycopg2 (postgres) as default database engine.

## How To Install

1.  Get the package from pypi: `pip install django-sql-middleware`
2.  In `settings.py` add:

    ```
    INSTALLED_APPS = [
        # your other apps
        "sqlmiddleware"
    ]

    MIDDLEWARE = [
        # your other middlewares
    ]

    if DEBUG:
        MIDDLEWARE.append("sqlmiddleware.middlewares.LogSQLMiddleware")
    ```

3.  Register urls in `your_project/urls.py`:

    ```
    from django.urls import include, path

    urlpatterns = [
        # other urls,
        path("__sql/", include("sqlmiddleware.urls")),
    ]
    ```

4.  Run `collectstatic` to serve included css and js assets: `./manage.py collectstatic`
5.  Start the development server: `./manage.py runserver`
6.  you should be able to access `localhost:8000/__sql` in your browser.

## Screenshots

1. List of captured requests
   ![Alt text](/screenshots/main.png?raw=true)
2. List of database queries in selected request
   ![Alt text](/screenshots/detail.png?raw=true)
3. Query execution plan (EXPLAIN)
   ![Alt text](/screenshots/explain.png?raw=true)
4. Traceback showing your code only
   ![Alt text](/screenshots/mine.png?raw=true)
5. Full traceback
   ![Alt text](/screenshots/full.png?raw=true)
