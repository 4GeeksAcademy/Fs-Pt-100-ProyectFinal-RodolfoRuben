"""empty message

<<<<<<<< HEAD:migrations/versions/4571e5c04db8_.py
Revision ID: 4571e5c04db8
Revises: 
Create Date: 2025-05-28 15:00:43.642457
========
Revision ID: ef38555d3163
Revises: 
Create Date: 2025-05-29 11:33:42.054952
>>>>>>>> 1d2299660448833f67ca420b140ab24d64e13baf:migrations/versions/ef38555d3163_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/4571e5c04db8_.py
revision = '4571e5c04db8'
========
revision = 'ef38555d3163'
>>>>>>>> 1d2299660448833f67ca420b140ab24d64e13baf:migrations/versions/ef38555d3163_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onlinegames',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('difficulty_levels', sa.String(length=40), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=350), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=90), nullable=True),
    sa.Column('dateofbirth', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('avatar_image', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user1_id', sa.Integer(), nullable=False),
    sa.Column('user2_id', sa.Integer(), nullable=True),
    sa.Column('onlinegame_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['onlinegame_id'], ['onlinegames.id'], ),
    sa.ForeignKeyConstraint(['user1_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user2_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('iasessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('genre', sa.String(length=60), nullable=True),
    sa.Column('difficulty_levels', sa.String(length=60), nullable=True),
    sa.Column('character_name', sa.String(length=60), nullable=False),
    sa.Column('character_class', sa.String(length=60), nullable=False),
    sa.Column('experience_gained', sa.Integer(), nullable=True),
    sa.Column('story_branch', sa.String(length=200), nullable=True),
    sa.Column('result', sa.String(length=60), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=False),
    sa.Column('ended_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onlinestats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sessions_played', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.Column('stalemate', sa.Integer(), nullable=False),
    sa.Column('losses', sa.Integer(), nullable=False),
    sa.Column('last_played', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('online_game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['online_game_id'], ['onlinegames.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('payment_method', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('purchased_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usercontacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('contact_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('iaevents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chapter_number', sa.Integer(), nullable=True),
    sa.Column('decision', sa.String(length=400), nullable=False),
    sa.Column('description', sa.String(length=400), nullable=False),
    sa.Column('outcome', sa.String(length=400), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('sessions_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sessions_id'], ['iasessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iaevents')
    op.drop_table('usercontacts')
    op.drop_table('purchases')
    op.drop_table('onlinestats')
    op.drop_table('iasessions')
    op.drop_table('favorites')
    op.drop_table('users')
    op.drop_table('onlinegames')
    # ### end Alembic commands ###
