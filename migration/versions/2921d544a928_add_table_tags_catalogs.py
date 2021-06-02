"""add table tags_catalogs

Revision ID: 2921d544a928
Revises: cb15c442228f
Create Date: 2020-03-02 00:03:17.199299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2921d544a928'
down_revision = 'cb15c442228f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogs', schema=None) as batch_op:
        batch_op.drop_column('tag')

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(),
                                      primary_key=True, nullable=False, comment='主鍵'))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('catalogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', mysql.VARCHAR(
            length=50), nullable=True, comment='標籤'))

    # ### end Alembic commands ###