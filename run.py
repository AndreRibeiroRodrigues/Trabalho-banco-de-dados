from application import create_app, database
from application.database import init_db

app = create_app()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
