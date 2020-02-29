"""add users's updatedAt

Revision ID: cb15c442228f
Revises: af1ae124ad2b
Create Date: 2020-02-29 15:40:27.565255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb15c442228f'
down_revision = 'af1ae124ad2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_comment='留言者',
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新時間'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('updatedAt')

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=100),
               existing_comment='留言者',
               existing_nullable=False)

    # ### end Alembic commands ###
