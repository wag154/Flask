from applications import app,db
from flask import render_template,flash,redirect,url_for,get_flashed_messages
from applications.models import TvShows
from applications.form import UserDataForm



@app.route("/")
def index():
    entries = TvShows.query.order_by(TvShows.date.desc()).all()
    return render_template('index.html', title = 'index', entries = entries)


@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = TvShows.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry Deleted", "success")
    return redirect(url_for("index"))
    
@app.route('/layout')
def layout():
    return render_template('layout.html', title='layout')

@app.route("/add", methods = ["GET","POST"])
def add_tv_show():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = TvShows(name = form.name.data, rating = form.rating.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful entry", 'success')
        return redirect(url_for('index'))
    return render_template("add.html", title = "add", form = form)
