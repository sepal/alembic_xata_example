"""Add team table

Revision ID: 418d220712cc
Revises: 
Create Date: 2024-09-12 12:57:13.115656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '418d220712cc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("website_url", sa.String(length=255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("team")
