from functools import wraps
from flask_login import current_user
from app.libs.http import error_jsonify
from app.const.errors import PermissionDenied


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_admin:
            return error_jsonify(PermissionDenied)
        return func(*args, **kwargs)

    return decorated_view
