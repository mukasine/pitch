"""second Migration

Revision ID: 2ed0b0185558
Revises: 31755de8d846
Create Date: 2019-02-28 09:16:31.699123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ed0b0185558'
down_revision = '31755de8d846'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitches_title', sa.String(), nullable=True),
    sa.Column('pitches_contents', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('lastname', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'lastname')
    op.drop_table('comments')
    op.drop_table('pitches')
    # ### end Alembic commands ###
