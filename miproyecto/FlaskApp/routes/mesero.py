from flask import Blueprint

mesero_bp = Blueprint('mesero',__name__)
@mesero_bp.route('/mesero')

@login_required
def mesero():
    from flask import render_template
    return render_template('mesero.html')