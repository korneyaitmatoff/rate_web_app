"""Database creation

Revision ID: 0d9ceaac1c0c
Revises: 
Create Date: 2023-11-18 22:38:08.098686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0d9ceaac1c0c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sites',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=True),
                    sa.Column('description', sa.VARCHAR(), nullable=True),
                    sa.Column('url', sa.VARCHAR(), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=True),
                    sa.Column('login', sa.VARCHAR(), nullable=True),
                    sa.Column('password', sa.VARCHAR(), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('sites')
    # ### end Alembic commands ###