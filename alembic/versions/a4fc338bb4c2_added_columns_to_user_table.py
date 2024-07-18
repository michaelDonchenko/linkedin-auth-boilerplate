"""added columns to user table

Revision ID: a4fc338bb4c2
Revises: ba1582187d9f
Create Date: 2024-07-18 13:32:44.096200

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a4fc338bb4c2"
down_revision: Union[str, None] = "ba1582187d9f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("created", sa.DateTime))
    op.add_column("user", sa.Column("last_active", sa.DateTime))


def downgrade() -> None:
    op.drop_column("user", "created")
    op.drop_column("user", "last_active")
