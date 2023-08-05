from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.goal import GoalSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # lifecycleStatus (GoalLifecycleStatus)
    from spark_auto_mapper_fhir.value_sets.goal_lifecycle_status import (
        GoalLifecycleStatusCode,
    )

    # achievementStatus (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for achievementStatus
    from spark_auto_mapper_fhir.value_sets.goal_achievement_status import (
        GoalAchievementStatusCode,
    )

    # End Import for CodeableConcept for achievementStatus
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.goal_category import GoalCategoryCode

    # End Import for CodeableConcept for category
    # priority (CodeableConcept)
    # Import for CodeableConcept for priority
    from spark_auto_mapper_fhir.value_sets.goal_priority import GoalPriorityCode

    # End Import for CodeableConcept for priority
    # description (CodeableConcept)
    # Import for CodeableConcept for description
    from spark_auto_mapper_fhir.value_sets.snomedct_clinical_findings import (
        SNOMEDCTClinicalFindingsCode,
    )

    # End Import for CodeableConcept for description
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.organization import Organization

    # startDate (date)
    # startCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for startCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for startCodeableConcept
    # target (Goal.Target)
    from spark_auto_mapper_fhir.backbone_elements.goal_target import GoalTarget

    # statusDate (date)
    # statusReason (string)
    # expressedBy (Reference)
    # Imports for References for expressedBy
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # addresses (Reference)
    # Imports for References for addresses
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.medication_statement import (
        MedicationStatement,
    )
    from spark_auto_mapper_fhir.resources.nutrition_order import NutritionOrder
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.resources.risk_assessment import RiskAssessment

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # outcomeCode (CodeableConcept)
    # Import for CodeableConcept for outcomeCode
    # End Import for CodeableConcept for outcomeCode
    # outcomeReference (Reference)
    # Imports for References for outcomeReference


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Goal(FhirResourceBase):
    """
    Goal
    goal.xsd
        Describes the intended objective(s) for a patient, group or organization care,
    for example, weight loss, restoring an activity of daily living, obtaining
    herd immunity via immunization, meeting a process improvement objective, etc.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        lifecycleStatus: GoalLifecycleStatusCode,
        achievementStatus: Optional[CodeableConcept[GoalAchievementStatusCode]] = None,
        category: Optional[FhirList[CodeableConcept[GoalCategoryCode]]] = None,
        priority: Optional[CodeableConcept[GoalPriorityCode]] = None,
        description: CodeableConcept[SNOMEDCTClinicalFindingsCode],
        subject: Reference[Union[Patient, Group, Organization]],
        startDate: Optional[FhirDate] = None,
        startCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        target: Optional[FhirList[GoalTarget]] = None,
        statusDate: Optional[FhirDate] = None,
        statusReason: Optional[FhirString] = None,
        expressedBy: Optional[
            Reference[Union[Patient, Practitioner, PractitionerRole, RelatedPerson]]
        ] = None,
        addresses: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        MedicationStatement,
                        NutritionOrder,
                        ServiceRequest,
                        RiskAssessment,
                    ]
                ]
            ]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        outcomeCode: Optional[
            FhirList[CodeableConcept[SNOMEDCTClinicalFindingsCode]]
        ] = None,
        outcomeReference: Optional[FhirList[Reference[Observation]]] = None,
    ) -> None:
        """
            Describes the intended objective(s) for a patient, group or organization care,
        for example, weight loss, restoring an activity of daily living, obtaining
        herd immunity via immunization, meeting a process improvement objective, etc.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: Business identifiers assigned to this goal by the performer or other systems
        which remain constant as the resource is updated and propagates from server to
        server.
            :param lifecycleStatus: The state of the goal throughout its lifecycle.
            :param achievementStatus: Describes the progression, or lack thereof, towards the goal against the
        target.
            :param category: Indicates a category the goal falls within.
            :param priority: Identifies the mutually agreed level of importance associated with
        reaching/sustaining the goal.
            :param description: Human-readable and/or coded description of a specific desired objective of
        care, such as "control blood pressure" or "negotiate an obstacle course" or
        "dance with child at wedding".
            :param subject: Identifies the patient, group or organization for whom the goal is being
        established.
            :param startDate: None
            :param startCodeableConcept: None
            :param target: Indicates what should be done by when.
            :param statusDate: Identifies when the current status.  I.e. When initially created, when
        achieved, when cancelled, etc.
            :param statusReason: Captures the reason for the current status.
            :param expressedBy: Indicates whose goal this is - patient goal, practitioner goal, etc.
            :param addresses: The identified conditions and other health record elements that are intended
        to be addressed by the goal.
            :param note: Any comments related to the goal.
            :param outcomeCode: Identifies the change (or lack of change) at the point when the status of the
        goal is assessed.
            :param outcomeReference: Details of what's changed (or not changed).
        """
        super().__init__(
            resourceType="Goal",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            lifecycleStatus=lifecycleStatus,
            achievementStatus=achievementStatus,
            category=category,
            priority=priority,
            description=description,
            subject=subject,
            startDate=startDate,
            startCodeableConcept=startCodeableConcept,
            target=target,
            statusDate=statusDate,
            statusReason=statusReason,
            expressedBy=expressedBy,
            addresses=addresses,
            note=note,
            outcomeCode=outcomeCode,
            outcomeReference=outcomeReference,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return GoalSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
