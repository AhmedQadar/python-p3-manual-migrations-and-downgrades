"""Change column name

Revision ID: f92c0c6e7ae4
Revises: c4db9c072457
Create Date: 2023-12-29 17:40:27.716893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92c0c6e7ae4'
down_revision = 'c4db9c072457'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='scholar_name')


def downgrade() -> None:
    op.alter_column('scholars', 'scholar_name', new_column_name='name')
