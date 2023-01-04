"""add memo to t_category

Revision ID: 6f684b324977
Revises: a82b89ad4982
Create Date: 2023-01-04 16:28:47.449180

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6f684b324977"
down_revision = "a82b89ad4982"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("category", schema=None) as batch_op:
        batch_op.add_column(sa.Column("memo", sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("category", schema=None) as batch_op:
        batch_op.drop_column("memo")

    # ### end Alembic commands ###
