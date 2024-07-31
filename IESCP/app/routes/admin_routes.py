from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User, Campaign, AdRequest
from app import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('auth.login'))

    users = User.query.all()
    campaigns = Campaign.query.all()
    ad_requests = AdRequest.query.all()

    return render_template('admin_dashboard.html', users=users, campaigns=campaigns, ad_requests=ad_requests)
