"""
UI views.
"""
import os

from flask import Blueprint
from flask import render_template
import jwt

from app.common.utils import generate_hash
from app.user.repositories import UserRepository
from app.user.utils import confirm_email


auth_views_bp = Blueprint('auth_view', __name__)


@auth_views_bp.route('/confirmation/<token>')
def email_confirmation(token: str):
    """
    Email confirmation route.
    """
    key = os.environ.get('SECRET_KEY')
    token_data = jwt.decode(token, key)
    user_id = token_data['user_id']
    user = UserRepository.get_one_by_id(user_id)
    if user:
        token_hash = generate_hash(email=user.email, user_id=user.id)
        if token_hash == token_data['hash']:
            confirm = {'email_confirmed': True}
            result = confirm_email(user.id, **confirm)
            if result.email_confirmed:
                return render_template('confirmed_email.html')

    return render_template('invalid_confirmation_token.html')
