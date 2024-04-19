from typing import Optional, List, Type, Union
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

    def get_days(self) -> Union[float, None]:
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()/86400

        return None

    def exceeds_consecutive_period(self):
        delta = self.get_days()
        if not delta:
            return False

        return delta > 3

    period = property(get_days)
