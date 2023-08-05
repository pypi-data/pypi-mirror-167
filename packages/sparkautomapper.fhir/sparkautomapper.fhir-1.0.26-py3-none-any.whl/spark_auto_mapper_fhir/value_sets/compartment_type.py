from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CompartmentTypeCode(GenericTypeCode):
    """
    CompartmentType
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
        Which type a compartment definition describes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/compartment-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/compartment-type"


class CompartmentTypeCodeValues:
    """
    The compartment definition is for the patient compartment.
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
    """

    Patient = CompartmentTypeCode("Patient")
    """
    The compartment definition is for the encounter compartment.
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
    """
    Encounter = CompartmentTypeCode("Encounter")
    """
    The compartment definition is for the related-person compartment.
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
    """
    RelatedPerson = CompartmentTypeCode("RelatedPerson")
    """
    The compartment definition is for the practitioner compartment.
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
    """
    Practitioner = CompartmentTypeCode("Practitioner")
    """
    The compartment definition is for the device compartment.
    From: http://hl7.org/fhir/compartment-type in valuesets.xml
    """
    Device = CompartmentTypeCode("Device")
