"""“add_shop_and_product”

Revision ID: 9abc9d5ccc53
Revises: 
Create Date: 2022-06-01 14:01:10.448052

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '9abc9d5ccc53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shop'))
    )
    op.create_table('product',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], name=op.f('fk_product_shop_id_shop')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('shop')
    # ### end Alembic commands ###
