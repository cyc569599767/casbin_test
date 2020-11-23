"""empty message

Revision ID: 748a8321e003
Revises: 1038b7b8bede
Create Date: 2020-11-20 11:30:49.535577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748a8321e003'
down_revision = '1038b7b8bede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###