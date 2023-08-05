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
    # type_ (InvoicePriceComponentType)
    from spark_auto_mapper_fhir.value_sets.invoice_price_component_type import (
        InvoicePriceComponentTypeCode,
    )

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # factor (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # amount (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InvoicePriceComponent(FhirBackboneElementBase):
    """
    Invoice.PriceComponent
        Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: InvoicePriceComponentTypeCode,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        factor: Optional[FhirDecimal] = None,
        amount: Optional[Money] = None,
    ) -> None:
        """
            Invoice containing collected ChargeItems from an Account with calculated
        individual and total price for Billing purpose.

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
            :param type_: This code identifies the type of the component.
            :param code: A code that identifies the component. Codes may be used to differentiate
        between kinds of taxes, surcharges, discounts etc.
            :param factor: The factor that has been applied on the base price for calculating this
        component.
            :param amount: The amount calculated for this component.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            code=code,
            factor=factor,
            amount=amount,
        )
