"""add new column 'fullname' in table catalogs

Revision ID: 63c6cb4fe25b
Revises: 8d6527111230
Create Date: 2020-02-01 19:02:22.128546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '63c6cb4fe25b'
down_revision = '8d6527111230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fullname', sa.String(length=50), nullable=False, comment='評書人'))
        batch_op.alter_column('review',
               existing_type=mysql.FLOAT(),
               type_=sa.Float(precision=1),
               existing_comment='評分',
               existing_nullable=True)

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('review',
               existing_type=mysql.FLOAT(),
               type_=sa.Float(precision=1),
               existing_comment='評分',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('review',
               existing_type=sa.Float(precision=1),
               type_=mysql.FLOAT(),
               existing_comment='評分',
               existing_nullable=True)

    with op.batch_alter_table('catalogs', schema=None) as batch_op:
        batch_op.alter_column('review',
               existing_type=sa.Float(precision=1),
               type_=mysql.FLOAT(),
               existing_comment='評分',
               existing_nullable=True)
        batch_op.drop_column('fullname')

    # ### end Alembic commands ###
