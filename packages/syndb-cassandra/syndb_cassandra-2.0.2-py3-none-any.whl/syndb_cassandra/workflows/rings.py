from functools import partial
from typing import Optional

from cassandra.cqlengine.management import (
    create_keyspace_simple,
    drop_keyspace,
    sync_table,
)
from syndb_cassandra import IN_PRODUCTION
from syndb_cassandra.models import (
    MODIFY_ROLE_NAME,
    READ_ROLE_NAME,
    SYNDB_NEURO_DATA_KEYSPACE,
    keyspace_to_models,
    model_name_to_model,
    neuro_data_models,
)
from syndb_cassandra.settings import SyndbCassandraSettings, cassandra_settings_getter
from syndb_cassandra.utils.create_materialized_view import create_materialized_view
from syndb_cassandra.utils.misc import (
    materialized_view_name_from_table_name_and_partition_key,
    read_materialized_view_map,
)


def create_syndb_tables(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()

    if settings.remove_pre_existing_syndb:
        if IN_PRODUCTION:
            msg = "This should never be run in production!"
            raise ValueError(msg)
        drop_keyspace(
            SYNDB_NEURO_DATA_KEYSPACE,
            connections=[settings.cassandra_connection_name],
        )

    # create_syndb_tables ==============================================================================================

    for keyspace, models in keyspace_to_models.items():
        create_keyspace_simple(
            keyspace,
            replication_factor=1,
            connections=[settings.cassandra_connection_name],
        )

        for model in models:
            sync_table(
                model,
                keyspaces=(keyspace,),
                connections=(settings.cassandra_connection_name,),
            )


def create_materialized_views(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()
    cassandra_session = settings.cassandra_connection()

    partial_mv = partial(create_materialized_view, cassandra_session, SYNDB_NEURO_DATA_KEYSPACE)

    for model_name in neuro_data_models:
        partial_mv(
            model_name_to_model[model_name],
            ("animal", "brain_structure"),
        )

    for (
        model_name,
        second_partition_fields,
    ) in read_materialized_view_map().items():
        for second_partition_field in second_partition_fields:
            partial_mv(
                model_name_to_model[model_name],
                ("animal", "brain_structure", second_partition_field),
            )


def create_roles(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()
    cassandra_session = settings.cassandra_connection()

    cassandra_session.execute(f"CREATE ROLE IF NOT EXISTS {MODIFY_ROLE_NAME}")
    cassandra_session.execute(f"GRANT ALTER ON KEYSPACE {SYNDB_NEURO_DATA_KEYSPACE} TO {MODIFY_ROLE_NAME}")
    cassandra_session.execute(f"GRANT SELECT ON KEYSPACE {SYNDB_NEURO_DATA_KEYSPACE} TO {MODIFY_ROLE_NAME}")

    cassandra_session.execute(f"CREATE ROLE IF NOT EXISTS {READ_ROLE_NAME}")
    for keyspace in keyspace_to_models:
        cassandra_session.execute(f"GRANT SELECT ON KEYSPACE {keyspace} TO {READ_ROLE_NAME}")


def drop_materialized_views(settings: Optional[SyndbCassandraSettings] = None) -> None:
    settings = settings or cassandra_settings_getter()()
    cassandra_session = settings.cassandra_connection()

    mv_names = []
    for model_name in neuro_data_models:
        mv_names.append(
            materialized_view_name_from_table_name_and_partition_key(
                model_name_to_model[model_name], ("animal", "brain_structure")
            )
        )

    for (
        model_name,
        second_partition_fields,
    ) in read_materialized_view_map().items():
        mv_names.append(
            materialized_view_name_from_table_name_and_partition_key(
                model_name_to_model[model_name], ("animal", "brain_structure")
            )
        )

    for mv_name in mv_names:
        cassandra_session.execute(f"DROP MATERIALIZED VIEW IF EXISTS {SYNDB_NEURO_DATA_KEYSPACE}.{mv_name}")
