from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps

authapp = Blueprint('authapp', __name__)


# def login_required(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         if 'user' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Anda harus login', 'danger')
#             return redirect(url_for('authapp.login'))
#     return wrapper