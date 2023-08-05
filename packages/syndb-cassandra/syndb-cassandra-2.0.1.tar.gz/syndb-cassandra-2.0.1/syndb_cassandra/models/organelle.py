import uuid

from cassandra.cqlengine import ValidationError, columns
from cassandra.cqlengine.models import Model
from syndb_cassandra.utils.misc import get_class_names

# neurotransmitters_to_names = orjson.loads(pkgutil.get_data("syndb_cassandra", "assets/neurotransmitters.json"))


def validate_structure_model(first_parent_id, first_parent_table_name):
    from syndb_cassandra.models import structure_model_names

    if first_parent_id or first_parent_table_name:
        return True

    if not (first_parent_id and first_parent_table_name):
        msg = "first_parent_id and first_parent_table_name must be defined together"
        raise ValidationError(msg)

    if first_parent_table_name not in structure_model_names:
        msg = (
            f"{first_parent_table_name} is not a structure model. Make sure that the characters are lowercase, "
            f"and that the model, {first_parent_table_name}, is in:\n{', '.join(structure_model_names)}"
        )
        raise ValidationError(msg)


class Mitochondria(Model):
    __table_name__ = "mitochondria"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

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

    def validate(self):
        super().validate()
        validate_structure_model(self.first_parent_id, self.first_parent_table_name)


class Vesicle(Model):
    __table_name__ = "vesicle"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

    neurotransmitter = columns.Ascii(default="undefined", max_length=65, primary_key=True)
    distance_to_active_zone = columns.Float(primary_key=True)

    # ==================================================================================================================

    volume = columns.Float()
    average_radius = columns.Float()
    minimum_normal_length = columns.Float()
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

    def validate(self):
        super().validate()
        validate_structure_model(self.first_parent_id, self.first_parent_table_name)


class EndoplasmicReticulum(Model):
    __table_name__ = "endoplasmic_reticulum"

    dataset_id = columns.UUID(primary_key=True)
    animal = columns.Text(primary_key=True, max_length=65)
    brain_structure = columns.Ascii(primary_key=True, max_length=65)

    # Placement for model-specific clustering keys =====================================================================

    ribosome_count = columns.Integer()

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

    def validate(self):
        super().validate()
        validate_structure_model(self.first_parent_id, self.first_parent_table_name)


organelle_models = (Mitochondria, Vesicle, EndoplasmicReticulum)
organelle_model_names = get_class_names(organelle_models)
