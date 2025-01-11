from app import create_app,db
from sqlalchemy.ext.declarative import declarative_base

app = create_app()


with app.app_context():
    Base = declarative_base()
    target_metadata = db.metadata
    db.create_all()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)