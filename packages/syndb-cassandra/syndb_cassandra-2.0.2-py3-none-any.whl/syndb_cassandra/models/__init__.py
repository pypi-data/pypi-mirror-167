from syndb_cassandra.models.dendrite_axon import dendrite_axon_models
from syndb_cassandra.models.mesh import mesh_models
from syndb_cassandra.models.neuron import Neuron
from syndb_cassandra.models.organelle import organelle_models
from syndb_cassandra.utils.misc import get_class_names

MODIFY_ROLE_NAME: str = "moderator"
READ_ROLE_NAME: str = "reader"

SYNDB_NEURO_DATA_KEYSPACE: str = "syndb"

SYNDB_METADATA_KEYSPACE: str = "syndb_metadata"

SYNDB_OWNER_KEYSPACE: str = "syndb_owners"

structure_models = (Neuron, *dendrite_axon_models)
structure_model_names = organelle_model_names = get_class_names(structure_models)

daughter_models = (*dendrite_axon_models, *organelle_models)

brain_unit_models = (Neuron, *daughter_models)
brain_unit_model_names = get_class_names(brain_unit_models)

neuro_data_models = (*brain_unit_models, *mesh_models)
all_model_names = get_class_names(neuro_data_models)
model_name_to_model = dict(zip(all_model_names, neuro_data_models))

keyspace_to_models = {
    SYNDB_NEURO_DATA_KEYSPACE: neuro_data_models,
}
