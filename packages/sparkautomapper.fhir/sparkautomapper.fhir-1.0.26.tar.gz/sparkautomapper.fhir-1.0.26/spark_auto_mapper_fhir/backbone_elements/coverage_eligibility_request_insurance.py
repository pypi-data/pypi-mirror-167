from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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
    # focal (boolean)
    # coverage (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for coverage
    from spark_auto_mapper_fhir.resources.coverage import Coverage

    # businessArrangement (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageEligibilityRequestInsurance(FhirBackboneElementBase):
    """
    CoverageEligibilityRequest.Insurance
        The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        focal: Optional[FhirBoolean] = None,
        coverage: Reference[Coverage],
        businessArrangement: Optional[FhirString] = None,
    ) -> None:
        """
            The CoverageEligibilityRequest provides patient and insurance coverage
        information to an insurer for them to respond, in the form of an
        CoverageEligibilityResponse, with information regarding whether the stated
        coverage is valid and in-force and optionally to provide the insurance details
        of the policy.

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
            :param focal: A flag to indicate that this Coverage is to be used for evaluation of this
        request when set to true.
            :param coverage: Reference to the insurance card level information contained in the Coverage
        resource. The coverage issuing insurer will use these details to locate the
        patient's actual coverage within the insurer's information system.
            :param businessArrangement: A business agreement number established between the provider and the insurer
        for special business processing purposes.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            focal=focal,
            coverage=coverage,
            businessArrangement=businessArrangement,
        )
