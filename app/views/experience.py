from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from ..forms import ExperienceForm, CommentForm
from ..models import Experience, Comment, Like
from .. import db

bp = Blueprint('experience', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/experiences')
def list_experiences():
    experiences = Experience.query.all()
    return render_template('experience/list.html', experiences=experiences)

@bp.route('/experience/<int:id>', methods=['GET', 'POST'])
def experience_detail(id):
    experience = Experience.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.comment.data, author=current_user, experience=experience)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted.')
        return redirect(url_for('experience.experience_detail', id=experience.id))
    return render_template('experience/detail.html', experience=experience, form=form)

@bp.route('/experience/new', methods=['GET', 'POST'])
@login_required
def create_experience():
    form = ExperienceForm()
    if form.validate_on_submit():
        image = form.image.data
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            experience = Experience(
                title=form.title.data,
                description=form.description.data,
                price=form.price.data,
                image_filename=filename,
                author=current_user
            )
            db.session.add(experience)
            db.session.commit()
            flash('Experience created successfully.')
            return redirect(url_for('experience.list_experiences'))
        else:
            flash('Invalid image format. Allowed formats are: png, jpg, jpeg, gif.')
    return render_template('experience/create.html', title='Create Experience', form=form)

@bp.route('/experience/<int:id>/like', methods=['POST'])
@login_required
def like_experience(id):
    experience = Experience.query.get_or_404(id)
    if current_user in [like.user for like in experience.likes]:
        flash('You have already liked this experience.')
        return redirect(url_for('experience.experience_detail', id=id))
    like = Like(user_id=current_user.id, experience_id=id)
    db.session.add(like)
    db.session.commit()
    flash('You liked this experience.')
    return redirect(url_for('experience.experience_detail', id=id))

@bp.route('/experience/<int:id>/show_interest', methods=['POST'])
@login_required
def show_interest(id):
    # Implement the logic for showing interest, similar to the like feature.
    flash('You have shown interest in this experience.')
    return red
