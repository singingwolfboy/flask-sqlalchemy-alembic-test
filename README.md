# Example: Flask-SQLAlchemy and Flask-Alembic CLI Support

This repository is an example of how Flask-Alembic and Flask-SQLAlchemy
could work together regarding CLI support. In
[mitsuhiko/flask-sqlalchemy#520](https://github.com/mitsuhiko/flask-sqlalchemy/pull/520),
I proposed adding support for `flask db create` and `flask db drop`
to Flask-SQLAlchemy. This project shows how Flask-Alembic could override
one or both of those commands.

To test this, clone this repository, make a new virtualenv for it, and run
`pip install -r requirements.txt`. That will install versions of
Flask-SQLAlchemy and Flask-Alembic that both support `flask db create`.
Specifically, the code is here:

* [Flask-SQLAlchemy](https://github.com/singingwolfboy/flask-sqlalchemy/blob/cli/flask_sqlalchemy/cli.py#L42-L49)
* [Flask-Alembic](https://bitbucket.org/singingwolfboy/flask-alembic/src/e80429936c1f0242913026fadb56d75871ffcba9/flask_alembic/cli/click.py?at=override-sqlalchemy-cli&fileviewer=file-view-default#click.py-128:135)

Set the `FLASK_APP` enviornment variable, and run `flask db create`. You'll
notice that it creates and applies an initial Alembic migration.

Delete the `test.sqlite3` file and the `migrations` directory to undo everything.
Comment out the lines in `app.py` that refer to Flask-Alembic, and run
`flask db create` again. This time, it will create the database tables
without handling migrations.

I haven't yet figured out what to do about `flask db drop`. Is it worth
re-implementing it in Flask-Alembic, for consistency? If so, I'm not sure
the best way to do that.
