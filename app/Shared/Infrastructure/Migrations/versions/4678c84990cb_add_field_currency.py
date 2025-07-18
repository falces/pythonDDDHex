"""add field currency

Revision ID: 4678c84990cb
Revises: 211692d69853
Create Date: 2025-07-17 11:53:16.742701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4678c84990cb'
down_revision = '211692d69853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency', sa.String(length=3), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.drop_column('currency')

    # ### end Alembic commands ###
