"""Renaming Students to Scholars

Revision ID: c4db9c072457
Revises: 791279dd0760
Create Date: 2023-12-29 17:02:36.909410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4db9c072457'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
