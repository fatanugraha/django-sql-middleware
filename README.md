# Django SQL Middleware

A simple middleware aimed to capture all queries in a request and provide basic SQL profiling such
as execution time, execution plan, and query traceback.

This package is only intended to run in development mode.

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
