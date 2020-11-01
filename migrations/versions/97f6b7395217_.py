"""empty message

Revision ID: 97f6b7395217
Revises: 67a90a0a7ce2
Create Date: 2020-10-30 18:04:58.331669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f6b7395217'
down_revision = '67a90a0a7ce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal_photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link_to_photo', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('atype', sa.Enum('cat', 'dog', name='types'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animal_type_atype'), 'animal_type', ['atype'], unique=False)
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('link_to_document', sa.String(length=2000), nullable=False),
    sa.Column('animal', sa.Integer(), nullable=False),
    sa.Column('document_type', sa.Enum('kal', 'shmal', 'onal', name='documents'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_document_animal'), 'document', ['animal'], unique=False)
    op.create_index(op.f('ix_document_date'), 'document', ['date'], unique=False)
    op.create_index(op.f('ix_document_document_type'), 'document', ['document_type'], unique=False)
    op.create_table('shelter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal_breed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(length=48), nullable=False),
    sa.Column('animal_type', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['animal_type'], ['animal_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=45), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('surname', sa.String(length=45), nullable=False),
    sa.Column('role', sa.Enum('user', 'admin', name='roles'), nullable=True),
    sa.Column('shelter', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shelter'], ['shelter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    op.create_index(op.f('ix_users_surname'), 'users', ['surname'], unique=False)
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=45), nullable=False),
    sa.Column('male', sa.Integer(), nullable=False),
    sa.Column('special_signs', sa.String(length=250), nullable=True),
    sa.Column('size', sa.Enum('cat', 'dog', name='types'), nullable=True),
    sa.Column('character', sa.String(length=45), nullable=True),
    sa.Column('animal_type', sa.Integer(), nullable=False),
    sa.Column('animal_breed', sa.Integer(), nullable=False),
    sa.Column('shelter', sa.Integer(), nullable=False),
    sa.Column('ready', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['animal_breed'], ['animal_breed.id'], ),
    sa.ForeignKeyConstraint(['animal_type'], ['animal_type.id'], ),
    sa.ForeignKeyConstraint(['shelter'], ['shelter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animal_age'), 'animal', ['age'], unique=False)
    op.create_index(op.f('ix_animal_male'), 'animal', ['male'], unique=False)
    op.create_index(op.f('ix_animal_nickname'), 'animal', ['nickname'], unique=False)
    op.create_index(op.f('ix_animal_ready'), 'animal', ['ready'], unique=False)
    op.create_table('pet_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=False),
    sa.Column('animal', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['animal'], ['animal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pet_request_name'), 'pet_request', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pet_request_name'), table_name='pet_request')
    op.drop_table('pet_request')
    op.drop_index(op.f('ix_animal_ready'), table_name='animal')
    op.drop_index(op.f('ix_animal_nickname'), table_name='animal')
    op.drop_index(op.f('ix_animal_male'), table_name='animal')
    op.drop_index(op.f('ix_animal_age'), table_name='animal')
    op.drop_table('animal')
    op.drop_index(op.f('ix_users_surname'), table_name='users')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_table('users')
    op.drop_table('animal_breed')
    op.drop_table('shelter')
    op.drop_index(op.f('ix_document_document_type'), table_name='document')
    op.drop_index(op.f('ix_document_date'), table_name='document')
    op.drop_index(op.f('ix_document_animal'), table_name='document')
    op.drop_table('document')
    op.drop_index(op.f('ix_animal_type_atype'), table_name='animal_type')
    op.drop_table('animal_type')
    op.drop_table('animal_photo')
    # ### end Alembic commands ###
