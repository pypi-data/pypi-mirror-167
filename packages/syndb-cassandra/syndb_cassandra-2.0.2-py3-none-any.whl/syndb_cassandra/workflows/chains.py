from typing import Optional

from syndb_cassandra.settings import SyndbCassandraSettings, cassandra_settings_getter
from syndb_cassandra.workflows.rings import (
    create_materialized_views,
    create_roles,
    create_syndb_tables,
    drop_materialized_views,
)


def initialize(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()

    create_syndb_tables(settings)
    create_materialized_views(settings)
    create_roles(settings)


def rebuild_materialized_views(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()

    drop_materialized_views(settings)
    create_materialized_views(settings)
