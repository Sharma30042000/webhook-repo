from flask import Blueprint, json, request,render_template
from app.extensions import mongo
webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/',methods=['GET','POST'])
def home():
    male = mongo.db.contacts.find({"gender": 'male'})
    return render_template('home.html',data=male) 

@webhook.route('/receiver', methods=["POST"])
def receiver():
    return {}, 200
