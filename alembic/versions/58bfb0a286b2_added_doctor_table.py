"""Added Doctor table

Revision ID: 58bfb0a286b2
Revises: 78d91ae686a7
Create Date: 2025-02-18 14:15:59.671800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58bfb0a286b2'
down_revision: Union[str, None] = '78d91ae686a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
