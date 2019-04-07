# -*- coding: utf-8 -*-
# Import all the models, so that Base has them before being
# imported by Alembic
from shopbox.db.base_class import Base  # noqa
from shopbox.db_models.project import Project  # noqa
