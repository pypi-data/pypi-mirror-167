from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # sequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # provider (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # responsible (boolean)
    # role (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for role
    # Import for CodeableConcept for role
    from spark_auto_mapper_fhir.value_sets.claim_care_team_role_codes import (
        ClaimCareTeamRoleCodesCode,
    )

    # End Import for CodeableConcept for role
    # qualification (CodeableConcept)
    # End Import for References for qualification
    # Import for CodeableConcept for qualification
    from spark_auto_mapper_fhir.value_sets.example_provider_qualification_codes import (
        ExampleProviderQualificationCodesCode,
    )

    # End Import for CodeableConcept for qualification


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimCareTeam(FhirBackboneElementBase):
    """
    Claim.CareTeam
        A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        sequence: FhirPositiveInt,
        provider: Reference[Union[Practitioner, PractitionerRole, Organization]],
        responsible: Optional[FhirBoolean] = None,
        role: Optional[CodeableConcept[ClaimCareTeamRoleCodesCode]] = None,
        qualification: Optional[
            CodeableConcept[ExampleProviderQualificationCodesCode]
        ] = None,
    ) -> None:
        """
            A provider issued list of professional services and products which have been
        provided, or are to be provided, to a patient which is sent to an insurer for
        reimbursement.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param sequence: A number to uniquely identify care team entries.
            :param provider: Member of the team who provided the product or service.
            :param responsible: The party who is billing and/or responsible for the claimed products or
        services.
            :param role: The lead, assisting or supervising practitioner and their discipline if a
        multidisciplinary team.
            :param qualification: The qualification of the practitioner which is applicable for this service.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            sequence=sequence,
            provider=provider,
            responsible=responsible,
            role=role,
            qualification=qualification,
        )
