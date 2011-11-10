from flask import Blueprint, request, redirect

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/<username>')
def redirector(username=None):
    return redirect("http://www.google.com/?q=" + username)