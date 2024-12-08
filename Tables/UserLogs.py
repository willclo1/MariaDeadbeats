import sqlalchemy as sa
from sqlalchemy import Column, SmallInteger, VARCHAR
import sqlalchemy.orm as so
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserLogs(Base):
    __tablename__ = 'user_logs'

    log_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    team_name = Column(VARCHAR(50), nullable=True)
    yearID = Column(SmallInteger, nullable=False)
    time_of_query: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )