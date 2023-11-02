"""empty message

Revision ID: f8407fbd80ce
Revises: eb5da8b6b8f5
Create Date: 2023-10-25 13:11:46.330902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8407fbd80ce'
down_revision = 'eb5da8b6b8f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_user_email'), type_='unique')

    # ### end Alembic commands ###
