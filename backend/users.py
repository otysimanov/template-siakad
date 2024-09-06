from flask import Blueprint, render_template, redirect, url_for, jsonify, request

usersapp = Blueprint('usersapp', __name__)

@usersapp.route('/users')
def users():
    return render_template('users/index.html')