import os
from application import create_app, database
from application.database import init_db, inserir_dados

app = create_app()

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
