from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdmitSourceCode(GenericTypeCode):
    """
    AdmitSource
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
        This value set defines a set of codes that can be used to indicate from where
    the patient came in.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/admit-source
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/admit-source"


class AdmitSourceCodeValues:
    """
    The Patient has been transferred from another hospital for this encounter.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """

    TransferredFromOtherHospital = AdmitSourceCode("hosp-trans")
    """
    The patient has been transferred from the emergency department within the
    hospital. This is typically used in the transition to an inpatient encounter
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    FromAccident_emergencyDepartment = AdmitSourceCode("emd")
    """
    The patient has been transferred from an outpatient department within the
    hospital.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    FromOutpatientDepartment = AdmitSourceCode("outp")
    """
    The patient is a newborn and the encounter will track the baby related
    activities (as opposed to the Mothers encounter - that may be associated using
    the newborn encounters partof property)
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    BornInHospital = AdmitSourceCode("born")
    """
    The patient has been admitted due to a referred from a General Practitioner.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    GeneralPractitionerReferral = AdmitSourceCode("gp")
    """
    The patient has been admitted due to a referred from a Specialist (as opposed
    to a General Practitioner).
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    MedicalPractitioner_physicianReferral = AdmitSourceCode("mp")
    """
    The patient has been transferred from a nursing home.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    FromNursingHome = AdmitSourceCode("nursing")
    """
    The patient has been transferred from a psychiatric facility.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    FromPsychiatricHospital = AdmitSourceCode("psych")
    """
    The patient has been transferred from a rehabilitation facility or clinic.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    FromRehabilitationFacility = AdmitSourceCode("rehab")
    """
    The patient has been admitted from a source otherwise not specified here.
    From: http://terminology.hl7.org/CodeSystem/admit-source in valuesets.xml
    """
    Other = AdmitSourceCode("other")
