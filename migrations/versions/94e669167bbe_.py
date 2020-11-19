"""empty message

Revision ID: 94e669167bbe
Revises: beebc96c1a9a
Create Date: 2020-11-19 10:52:27.739882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '94e669167bbe'
down_revision = 'beebc96c1a9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permissions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('ptype', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v0', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v1', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v2', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v3', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v4', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('v5', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
