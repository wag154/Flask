from applications import db, app
from applications.models import TvShows

def create_database():
    with app.app_context():
        db.create_all()

def delete_database():
    with app.app_context():
        db.drop_all()

def add_entries():
    entry1 = TvShows(name="The Simpsons", rating="5", category="Comedy")
    entry2 = TvShows(name="Walking Dead", rating="3", category="Horror")
    entry3 = TvShows(name="The Last of Us", rating="4", category="Horror")
    with app.app_context():
        db.session.add(entry1)
        db.session.add(entry2)
        db.session.add(entry3)
        db.session.commit()

def see_db_entries():
    with app.app_context():
        entries = TvShows.query.all()
        for entry in entries:
            print(f"{entry.name}, {entry.rating}")
            
if __name__ == "__main__":
    delete_database()
    create_database()
    see_db_entries()
