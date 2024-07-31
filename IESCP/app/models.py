from . import db
from flask_login import UserMixin
class User(UserMixin, db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(150), unique=True, nullable=False)
email = db.Column(db.String(150), unique=True, nullable=False)
password = db.Column(db.String(150), nullable=False)
role = db.Column(db.String(50), nullable=False)  # "admin", "sponsor", "influencer"
class Campaign(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(150), nullable=False)
description = db.Column(db.Text, nullable=False)
start_date = db.Column(db.Date, nullable=False)
end_date = db.Column(db.Date, nullable=False)
budget = db.Column(db.Float, nullable=False)
visibility = db.Column(db.String(50), nullable=False)  # "public", "private"
goals = db.Column(db.Text, nullable=False)
sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
class AdRequest(db.Model):
id = db.Column(db.Integer, primary_key=True)
campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
messages = db.Column(db.Text, nullable=True)
requirements = db.Column(db.Text, nullable=False)
payment_amount = db.Column(db.Float, nullable=False)
status = db.Column(db.String(50), nullable=False)  # "Pending", "Accepted", "Rejected"
class InfluencerProfile(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
name = db.Column(db.String(150), nullable=False)
category = db.Column(db.String(150), nullable=False)
niche = db.Column(db.String(150), nullable=False)
reach = db.Column(db.Integer, nullable=False)
