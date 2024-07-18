"""create-user-table

Revision ID: ba1582187d9f
Revises: 
Create Date: 2024-07-14 16:55:48.429014

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ba1582187d9f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=True),
        sa.Column("email", sa.String, unique=True),
        sa.Column("picture", sa.String, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("user")
