"""Countries

Revision ID: 2dea2aac9a79
Revises: 610c40e9f352
Create Date: 2025-06-25 13:44:28.494676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dea2aac9a79'
down_revision = '610c40e9f352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('hasSubzone', sa.Boolean(), nullable=False),
    sa.Column('isEUMember', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('countries')
    # ### end Alembic commands ###
