from infrastructure.db.database import SessionLocal
from contextlib import contextmanager

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise Exception("Cannot connect to database")
    finally:
        db.close()