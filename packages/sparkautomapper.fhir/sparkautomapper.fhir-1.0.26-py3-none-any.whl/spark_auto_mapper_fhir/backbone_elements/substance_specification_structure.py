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
    # stereochemistry (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for stereochemistry
    # Import for CodeableConcept for stereochemistry
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for stereochemistry
    # opticalActivity (CodeableConcept)
    # End Import for References for opticalActivity
    # Import for CodeableConcept for opticalActivity
    # End Import for CodeableConcept for opticalActivity
    # molecularFormula (string)
    # molecularFormulaByMoiety (string)
    # isotope (SubstanceSpecification.Isotope)
    from spark_auto_mapper_fhir.backbone_elements.substance_specification_isotope import (
        SubstanceSpecificationIsotope,
    )

    # molecularWeight (SubstanceSpecification.MolecularWeight)
    from spark_auto_mapper_fhir.backbone_elements.substance_specification_molecular_weight import (
        SubstanceSpecificationMolecularWeight,
    )

    # source (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # representation (SubstanceSpecification.Representation)
    from spark_auto_mapper_fhir.backbone_elements.substance_specification_representation import (
        SubstanceSpecificationRepresentation,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSpecificationStructure(FhirBackboneElementBase):
    """
    SubstanceSpecification.Structure
        The detailed description of a substance, typically at a level beyond what is used for prescribing.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        stereochemistry: Optional[CodeableConcept[GenericTypeCode]] = None,
        opticalActivity: Optional[CodeableConcept[GenericTypeCode]] = None,
        molecularFormula: Optional[FhirString] = None,
        molecularFormulaByMoiety: Optional[FhirString] = None,
        isotope: Optional[FhirList[SubstanceSpecificationIsotope]] = None,
        molecularWeight: Optional[SubstanceSpecificationMolecularWeight] = None,
        source: Optional[FhirList[Reference[DocumentReference]]] = None,
        representation: Optional[FhirList[SubstanceSpecificationRepresentation]] = None,
    ) -> None:
        """
            The detailed description of a substance, typically at a level beyond what is
        used for prescribing.

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
            :param stereochemistry: Stereochemistry type.
            :param opticalActivity: Optical activity type.
            :param molecularFormula: Molecular formula.
            :param molecularFormulaByMoiety: Specified per moiety according to the Hill system, i.e. first C, then H, then
        alphabetical, each moiety separated by a dot.
            :param isotope: Applicable for single substances that contain a radionuclide or a non-natural
        isotopic ratio.
            :param molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic
        acids).
            :param source: Supporting literature.
            :param representation: Molecular structural representation.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            stereochemistry=stereochemistry,
            opticalActivity=opticalActivity,
            molecularFormula=molecularFormula,
            molecularFormulaByMoiety=molecularFormulaByMoiety,
            isotope=isotope,
            molecularWeight=molecularWeight,
            source=source,
            representation=representation,
        )
