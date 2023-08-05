from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SNOMED_CTCode(GenericTypeCode):
    """
    SNOMED_CT
    From: http://snomed.info/sct in valuesets.xml
        SNOMED CT is the most comprehensive and precise clinical health terminology
    product in the world, owned and distributed around the world by The
    International Health Terminology Standards Development Organisation (IHTSDO).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"
