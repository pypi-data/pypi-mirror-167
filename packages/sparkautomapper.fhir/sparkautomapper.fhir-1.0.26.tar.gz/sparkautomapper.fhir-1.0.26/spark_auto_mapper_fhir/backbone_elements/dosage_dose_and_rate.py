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
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.dose_and_rate_type import DoseAndRateTypeCode

    # End Import for CodeableConcept for type_
    # doseRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # doseQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # rateRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # rateRange (Range)
    # rateQuantity (Quantity)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DosageDoseAndRate(FhirBackboneElementBase):
    """
    Dosage.DoseAndRate
        Indicates how the medication is/was taken or should be taken by the patient.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[CodeableConcept[DoseAndRateTypeCode]] = None,
        doseRange: Optional[Range] = None,
        doseQuantity: Optional[Quantity] = None,
        rateRatio: Optional[Ratio] = None,
        rateRange: Optional[Range] = None,
        rateQuantity: Optional[Quantity] = None,
    ) -> None:
        """
            Indicates how the medication is/was taken or should be taken by the patient.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

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
            :param type_: The kind of dose or rate specified, for example, ordered or calculated.
            :param doseRange: None
            :param doseQuantity: None
            :param rateRatio: None
            :param rateRange: None
            :param rateQuantity: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            doseRange=doseRange,
            doseQuantity=doseQuantity,
            rateRatio=rateRatio,
            rateRange=rateRange,
            rateQuantity=rateQuantity,
        )
