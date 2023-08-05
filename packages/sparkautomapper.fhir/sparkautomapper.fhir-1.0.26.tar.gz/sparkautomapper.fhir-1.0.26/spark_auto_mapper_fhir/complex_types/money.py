from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_fhir_schemas.r4.complex_types.money import MoneySchema


if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # value (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # currency (Currencies)
    from spark_auto_mapper_fhir.value_sets.currencies import CurrenciesCode


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Money(FhirComplexTypeBase):
    """
    Money
    fhir-base.xsd
        An amount of economic utility in some recognized currency.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[NestedExtensionItem]] = None,
        value: Optional[FhirDecimal] = None,
        currency: Optional[CurrenciesCode] = None,
    ) -> None:
        """
            An amount of economic utility in some recognized currency.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param value: Numerical value (with implicit precision).
            :param currency: ISO 4217 Currency Code.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            value=value,
            currency=currency,
        )
        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return MoneySchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
