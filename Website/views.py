from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .models import Note2
from .models import Note3
from .models import Note4
from .models import Note5
from .models import Note6
from .models import Note7
from .models import Note8



views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
@views.route('/Maths', methods=['GET', 'POST'])
def maths():
    if request.method == 'POST': 
        note2 = request.form.get('note')#Gets the note from the HTML 

        if len(note2) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note2 = Note2(data=note2, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note2) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("Maths.html", user=current_user)

@views.route('/Physics', methods=['GET', 'POST'])
def Physics():
    if request.method == 'POST': 
        note3 = request.form.get('note')#Gets the note from the HTML 

        if len(note3) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note3 = Note3(data=note3, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note3) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("Physics.html", user=current_user)

@views.route('/Computing', methods=['GET', 'POST'])
def Computing():
    if request.method == 'POST': 
        note4 = request.form.get('note')#Gets the note from the HTML 

        if len(note4) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note4 = Note4(data=note4, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note4) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("Computing.html", user=current_user)
@views.route('/GeneralPaper', methods=['GET', 'POST'])
def GeneralPaper():
    if request.method == 'POST': 
        note5 = request.form.get('note')#Gets the note from the HTML 

        if len(note5) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note5 = Note5(data=note5, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note5) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("GeneralPaper.html", user=current_user)

@views.route('/Economics', methods=['GET', 'POST'])
def Economics():
    if request.method == 'POST': 
        note6 = request.form.get('note')#Gets the note from the HTML 

        if len(note6) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note6 = Note6(data=note6, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note6) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("Economics.html", user=current_user)

@views.route('/PW', methods=['GET', 'POST'])
def PW():
    if request.method == 'POST': 
        note7 = request.form.get('note')#Gets the note from the HTML 

        if len(note7) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note7 = Note7(data=note7, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note7) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("PW.html", user=current_user)
@views.route('/MTL', methods=['GET', 'POST'])
def MTL():
    if request.method == 'POST': 
        note8 = request.form.get('note')#Gets the note from the HTML 

        if len(note8) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note8 = Note8(data=note8, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note8) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("MTL.html", user=current_user)
