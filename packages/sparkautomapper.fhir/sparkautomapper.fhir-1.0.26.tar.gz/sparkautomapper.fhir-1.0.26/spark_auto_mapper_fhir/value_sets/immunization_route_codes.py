from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationRouteCodesCode(GenericTypeCode):
    """
    ImmunizationRouteCodes
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
        The value set to instantiate this attribute should be drawn from a
    terminologically robust code system that consists of or contains concepts to
    support describing the administrative routes used during vaccination. This
    value set is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"


class ImmunizationRouteCodesCodeValues:
    """
    Route of substance administration classified by administration method.
    From: http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration in v3-codesystems.xml
    """

    RouteByMethod = ImmunizationRouteCodesCode("_RouteByMethod")
    """
    Route of substance administration classified by site.
    From: http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration in v3-codesystems.xml
    """
    RouteBySite = ImmunizationRouteCodesCode("_RouteBySite")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Injection_Intradermal = ImmunizationRouteCodesCode("IDINJ")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Injection_Intramuscular = ImmunizationRouteCodesCode("IM")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Inhalation_Nasal = ImmunizationRouteCodesCode("NASINHLC")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Injection_Intravenous = ImmunizationRouteCodesCode("IVINJ")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Swallow_Oral = ImmunizationRouteCodesCode("PO")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Injection_Subcutaneous = ImmunizationRouteCodesCode("SQ")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-route in valuesets.xml
    """
    Transdermal = ImmunizationRouteCodesCode("TRNSDERM")
