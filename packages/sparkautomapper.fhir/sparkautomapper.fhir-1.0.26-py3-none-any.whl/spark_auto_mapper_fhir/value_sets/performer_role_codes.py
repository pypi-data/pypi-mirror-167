from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PerformerRoleCodesCode(GenericTypeCode):
    """
    PerformerRoleCodes
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
        This value set includes sample Performer Role codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/consentperformer
    """
    codeset: FhirUri = "http://hl7.org/fhir/consentperformer"


class PerformerRoleCodesCodeValues:
    """
    An entity or an entity's delegatee who is the grantee in an agreement such as
    a consent for services, advanced directive, or a privacy consent directive in
    accordance with jurisdictional, organizational, or patient policy.
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
    """

    Consenter = PerformerRoleCodesCode("consenter")
    """
    An entity which accepts certain rights or authority from a grantor.
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
    """
    Grantee = PerformerRoleCodesCode("grantee")
    """
    An entity which agrees to confer certain rights or authority to a grantee.
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
    """
    Grantor = PerformerRoleCodesCode("grantor")
    """
    A party to whom some right or authority is granted by a delegator.
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
    """
    Delegatee = PerformerRoleCodesCode("delegatee")
    """
    A party that grants all or some portion its right or authority to another
    party.
    From: http://hl7.org/fhir/consentperformer in valuesets.xml
    """
    Delegator = PerformerRoleCodesCode("delegator")
