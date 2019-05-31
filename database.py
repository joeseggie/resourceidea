from flask_sqlalchemy import SQLAlchemy

from app.common.sqlalchemy_extensions import CustomBaseQuery


db = SQLAlchemy(query_class=CustomBaseQuery)
