from flask import Blueprint

from counter.models import Counter

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
	return 'Counter App'
