"""empty message

Revision ID: 107546170251
Revises: d03cee13863f
Create Date: 2024-09-25 12:11:58.573814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '107546170251'
down_revision: Union[str, None] = 'd03cee13863f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
