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
    # operation (TestReport.Operation)
    from spark_auto_mapper_fhir.backbone_elements.test_report_operation import (
        TestReportOperation,
    )

    # assert_ (TestReport.Assert)
    from spark_auto_mapper_fhir.backbone_elements.test_report_assert import (
        TestReportAssert,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestReportAction(FhirBackboneElementBase):
    """
    TestReport.Action
        A summary of information based on the results of executing a TestScript.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        operation: Optional[TestReportOperation] = None,
        assert_: Optional[TestReportAssert] = None,
    ) -> None:
        """
            A summary of information based on the results of executing a TestScript.

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
            :param operation: The operation performed.
            :param assert_: The results of the assertion performed on the previous operations.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            operation=operation,
            assert_=assert_,
        )
