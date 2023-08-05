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
    # coverage (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for coverage
    from spark_auto_mapper_fhir.resources.coverage import Coverage

    # inforce (boolean)
    # benefitPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # item (CoverageEligibilityResponse.Item)
    from spark_auto_mapper_fhir.backbone_elements.coverage_eligibility_response_item import (
        CoverageEligibilityResponseItem,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageEligibilityResponseInsurance(FhirBackboneElementBase):
    """
    CoverageEligibilityResponse.Insurance
        This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        coverage: Reference[Coverage],
        inforce: Optional[FhirBoolean] = None,
        benefitPeriod: Optional[Period] = None,
        item: Optional[FhirList[CoverageEligibilityResponseItem]] = None,
    ) -> None:
        """
            This resource provides eligibility and plan details from the processing of an
        CoverageEligibilityRequest resource.

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
            :param coverage: Reference to the insurance card level information contained in the Coverage
        resource. The coverage issuing insurer will use these details to locate the
        patient's actual coverage within the insurer's information system.
            :param inforce: Flag indicating if the coverage provided is inforce currently if no service
        date(s) specified or for the whole duration of the service dates.
            :param benefitPeriod: The term of the benefits documented in this response.
            :param item: Benefits and optionally current balances, and authorization details by
        category or service.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            coverage=coverage,
            inforce=inforce,
            benefitPeriod=benefitPeriod,
            item=item,
        )
