"""Atualizar mfa

Revision ID: 94638d811d0e
Revises: bf718290be2f
Create Date: 2024-03-31 07:10:39.965261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '94638d811d0e'
down_revision = 'bf718290be2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('on_waiting_list', sa.Boolean(), nullable=True))
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.drop_column('username')
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', mysql.VARCHAR(length=256), nullable=True))
        batch_op.add_column(sa.Column('username', mysql.VARCHAR(length=64), nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_email'))
        batch_op.create_index('ix_user_username', ['username'], unique=True)
        batch_op.drop_column('on_waiting_list')
        batch_op.drop_column('is_approved')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
