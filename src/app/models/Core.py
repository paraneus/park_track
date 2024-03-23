import enum
from sqlalchemy import Integer, String, UUID, Enum, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


class BaseModel(DeclarativeBase):
    pass

class BaseEnum(enum.Enum):
    def __str__(self):
        return self.name

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
