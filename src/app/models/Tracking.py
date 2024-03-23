from typing import Optional, List, Type
from app.models.Core import BaseModel
from sqlalchemy.orm import  mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY, VARCHAR
import pdb
import uuid
import datetime


class Tracking(BaseModel):
    __tablename__ = 'tracking'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    start_time: Mapped[Optional[datetime.datetime]]
    end_time: Mapped[Optional[datetime.datetime]]
