from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationOriginCodesCode(GenericTypeCode):
    """
    ImmunizationOriginCodes
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
        The value set to instantiate this attribute should be drawn from a
    terminologically robust code system that consists of or contains concepts to
    support describing the source of the data when the report of the immunization
    event is not based on information from the person, entity or organization who
    administered the vaccine. This value set is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/immunization-origin
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/immunization-origin"


class ImmunizationOriginCodesCodeValues:
    """
    The data for the immunization event originated with another provider.
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
    """

    OtherProvider = ImmunizationOriginCodesCode("provider")
    """
    The data for the immunization event originated with a written record for the
    patient.
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
    """
    WrittenRecord = ImmunizationOriginCodesCode("record")
    """
    The data for the immunization event originated from the recollection of the
    patient or parent/guardian of the patient.
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
    """
    Parent_Guardian_PatientRecall = ImmunizationOriginCodesCode("recall")
    """
    The data for the immunization event originated with a school record for the
    patient.
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
    """
    SchoolRecord = ImmunizationOriginCodesCode("school")
    """
    The data for the immunization event originated with an immunization
    information system (IIS) or registry operating within the jurisdiction.
    From: http://terminology.hl7.org/CodeSystem/immunization-origin in valuesets.xml
    """
    JurisdictionalIIS = ImmunizationOriginCodesCode("jurisdiction")
