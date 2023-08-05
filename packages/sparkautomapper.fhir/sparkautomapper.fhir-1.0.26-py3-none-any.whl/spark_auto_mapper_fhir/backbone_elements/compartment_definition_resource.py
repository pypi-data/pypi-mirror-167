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
    # code (ResourceType)
    from spark_auto_mapper_fhir.value_sets.resource_type import ResourceTypeCode

    # param (string)
    # documentation (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CompartmentDefinitionResource(FhirBackboneElementBase):
    """
    CompartmentDefinition.Resource
        A compartment definition that defines how resources are accessed on a server.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        code: ResourceTypeCode,
        param: Optional[FhirList[FhirString]] = None,
        documentation: Optional[FhirString] = None,
    ) -> None:
        """
            A compartment definition that defines how resources are accessed on a server.

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
            :param code: The name of a resource supported by the server.
            :param param: The name of a search parameter that represents the link to the compartment.
        More than one may be listed because a resource may be linked to a compartment
        in more than one way,.
            :param documentation: Additional documentation about the resource and compartment.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            code=code,
            param=param,
            documentation=documentation,
        )
