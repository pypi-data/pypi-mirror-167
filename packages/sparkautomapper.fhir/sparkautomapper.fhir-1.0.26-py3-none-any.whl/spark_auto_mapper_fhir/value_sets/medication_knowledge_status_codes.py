from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledgeStatusCodesCode(GenericTypeCode):
    """
    MedicationKnowledge Status Codes
    From: http://terminology.hl7.org/CodeSystem/medicationknowledge-status in valuesets.xml
        MedicationKnowledge Status Codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/medicationknowledge-status
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/medicationknowledge-status"
    )


class MedicationKnowledgeStatusCodesCodeValues:
    """
    The medication is available for use.
    From: http://terminology.hl7.org/CodeSystem/medicationknowledge-status in valuesets.xml
    """

    Active = MedicationKnowledgeStatusCodesCode("active")
    """
    The medication is not available for use.
    From: http://terminology.hl7.org/CodeSystem/medicationknowledge-status in valuesets.xml
    """
    Inactive = MedicationKnowledgeStatusCodesCode("inactive")
    """
    The medication was entered in error.
    From: http://terminology.hl7.org/CodeSystem/medicationknowledge-status in valuesets.xml
    """
    EnteredInError = MedicationKnowledgeStatusCodesCode("entered-in-error")
