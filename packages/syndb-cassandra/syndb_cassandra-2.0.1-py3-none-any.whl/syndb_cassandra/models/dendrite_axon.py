import uuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from syndb_cassandra.utils.misc import get_class_names


class Dendrite(Model):
    __table_name__ = "dendrite"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

    post_synaptic_terminal_count = columns.Integer()

    # ==================================================================================================================

    volume = columns.Float()
    average_radius = columns.Float()
    surface_area = columns.Float()
    area_volume_ratio = columns.Float()
    sphericity = columns.Float()

    centroid_z = columns.Float()
    centroid_x = columns.Float()
    centroid_y = columns.Float()

    first_parent_id = columns.UUID()
    first_parent_table_name = columns.Ascii()

    cid = columns.UUID(default=uuid.uuid4())
    neuron_id = columns.UUID()


class Axon(Model):
    __table_name__ = "axon"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

    terminal_count = columns.Integer()

    # ==================================================================================================================

    volume = columns.Float()
    average_radius = columns.Float()
    surface_area = columns.Float()
    area_volume_ratio = columns.Float()
    sphericity = columns.Float()

    centroid_z = columns.Float()
    centroid_x = columns.Float()
    centroid_y = columns.Float()

    first_parent_id = columns.UUID()
    first_parent_table_name = columns.Ascii()

    cid = columns.UUID(default=uuid.uuid4())
    neuron_id = columns.UUID()


class Terminal(Model):
    __table_name__ = "terminal"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

    is_pre_synaptic = columns.Boolean(primary_key=True)

    # ==================================================================================================================

    volume = columns.Float()
    mitochondria_count = columns.Integer()
    total_mitochondria_volume = columns.Float()

    vesicle_count = columns.Integer()
    total_vesicle_volume = columns.Float()

    average_radius = columns.Float()
    surface_area = columns.Float()
    area_volume_ratio = columns.Float()
    sphericity = columns.Float()

    centroid_z = columns.Float()
    centroid_x = columns.Float()
    centroid_y = columns.Float()

    first_parent_id = columns.UUID()
    first_parent_table_name = columns.Ascii()

    cid = columns.UUID(default=uuid.uuid4())
    neuron_id = columns.UUID()


dendrite_axon_models = (
    Dendrite,
    Axon,
    Terminal,
)
dendrite_axon_model_names = get_class_names(dendrite_axon_models)
