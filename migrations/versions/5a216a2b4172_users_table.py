"""users table

Revision ID: 5a216a2b4172
Revises: 
Create Date: 2020-02-16 02:12:52.905653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a216a2b4172'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('listing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('listing_name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_listing_listing_name'), 'listing', ['listing_name'], unique=False)
    op.create_index(op.f('ix_listing_price'), 'listing', ['price'], unique=True)
    op.create_index(op.f('ix_listing_timestamp'), 'listing', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_listing_timestamp'), table_name='listing')
    op.drop_index(op.f('ix_listing_price'), table_name='listing')
    op.drop_index(op.f('ix_listing_listing_name'), table_name='listing')
    op.drop_table('listing')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
