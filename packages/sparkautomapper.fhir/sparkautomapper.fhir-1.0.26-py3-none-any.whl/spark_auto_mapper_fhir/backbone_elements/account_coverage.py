from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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

    # priority (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AccountCoverage(FhirBackboneElementBase):
    """
    Account.Coverage
        A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        coverage: Reference[Coverage],
        priority: Optional[FhirPositiveInt] = None,
    ) -> None:
        """
            A financial tool for tracking value accrued for a particular purpose.  In the
        healthcare field, used to track charges for a patient, cost centers, etc.

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
            :param coverage: The party(s) that contribute to payment (or part of) of the charges applied to
        this account (including self-pay).

        A coverage may only be responsible for specific types of charges, and the
        sequence of the coverages in the account could be important when processing
        billing.
            :param priority: The priority of the coverage in the context of this account.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            coverage=coverage,
            priority=priority,
        )
