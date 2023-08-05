from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConditionalDeleteStatusCode(GenericTypeCode):
    """
    ConditionalDeleteStatus
    From: http://hl7.org/fhir/conditional-delete-status in valuesets.xml
        A code that indicates how the server supports conditional delete.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/conditional-delete-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/conditional-delete-status"


class ConditionalDeleteStatusCodeValues:
    """
    No support for conditional deletes.
    From: http://hl7.org/fhir/conditional-delete-status in valuesets.xml
    """

    NotSupported = ConditionalDeleteStatusCode("not-supported")
    """
    Conditional deletes are supported, but only single resources at a time.
    From: http://hl7.org/fhir/conditional-delete-status in valuesets.xml
    """
    SingleDeletesSupported = ConditionalDeleteStatusCode("single")
    """
    Conditional deletes are supported, and multiple resources can be deleted in a
    single interaction.
    From: http://hl7.org/fhir/conditional-delete-status in valuesets.xml
    """
    MultipleDeletesSupported = ConditionalDeleteStatusCode("multiple")
