from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.measure import MeasureSchema

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
    # url (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # version (string)
    # name (string)
    # title (string)
    # subtitle (string)
    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # subjectCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for subjectCodeableConcept
    from spark_auto_mapper_fhir.value_sets.subject_type import SubjectTypeCode

    # End Import for CodeableConcept for subjectCodeableConcept
    # subjectReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subjectReference
    from spark_auto_mapper_fhir.resources.group import Group

    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # usage (string)
    # copyright (markdown)
    # approvalDate (date)
    # lastReviewDate (date)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # topic (CodeableConcept)
    # Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.value_sets.definition_topic import DefinitionTopicCode

    # End Import for CodeableConcept for topic
    # author (ContactDetail)
    # editor (ContactDetail)
    # reviewer (ContactDetail)
    # endorser (ContactDetail)
    # relatedArtifact (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # library (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # disclaimer (markdown)
    # scoring (CodeableConcept)
    # Import for CodeableConcept for scoring
    from spark_auto_mapper_fhir.value_sets.measure_scoring import MeasureScoringCode

    # End Import for CodeableConcept for scoring
    # compositeScoring (CodeableConcept)
    # Import for CodeableConcept for compositeScoring
    from spark_auto_mapper_fhir.value_sets.composite_measure_scoring import (
        CompositeMeasureScoringCode,
    )

    # End Import for CodeableConcept for compositeScoring
    # type_ (CodeableConcept)
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.measure_type import MeasureTypeCode

    # End Import for CodeableConcept for type_
    # riskAdjustment (string)
    # rateAggregation (string)
    # rationale (markdown)
    # clinicalRecommendationStatement (markdown)
    # improvementNotation (CodeableConcept)
    # Import for CodeableConcept for improvementNotation
    from spark_auto_mapper_fhir.value_sets.measure_improvement_notation import (
        MeasureImprovementNotationCode,
    )

    # End Import for CodeableConcept for improvementNotation
    # definition (markdown)
    # guidance (markdown)
    # group (Measure.Group)
    from spark_auto_mapper_fhir.backbone_elements.measure_group import MeasureGroup

    # supplementalData (Measure.SupplementalData)
    from spark_auto_mapper_fhir.backbone_elements.measure_supplemental_data import (
        MeasureSupplementalData,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Measure(FhirResourceBase):
    """
    Measure
    measure.xsd
        The Measure resource provides the definition of a quality measure.
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
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        usage: Optional[FhirString] = None,
        copyright: Optional[FhirMarkdown] = None,
        approvalDate: Optional[FhirDate] = None,
        lastReviewDate: Optional[FhirDate] = None,
        effectivePeriod: Optional[Period] = None,
        topic: Optional[FhirList[CodeableConcept[DefinitionTopicCode]]] = None,
        author: Optional[FhirList[ContactDetail]] = None,
        editor: Optional[FhirList[ContactDetail]] = None,
        reviewer: Optional[FhirList[ContactDetail]] = None,
        endorser: Optional[FhirList[ContactDetail]] = None,
        relatedArtifact: Optional[FhirList[RelatedArtifact]] = None,
        library: Optional[FhirList[FhirCanonical]] = None,
        disclaimer: Optional[FhirMarkdown] = None,
        scoring: Optional[CodeableConcept[MeasureScoringCode]] = None,
        compositeScoring: Optional[CodeableConcept[CompositeMeasureScoringCode]] = None,
        type_: Optional[FhirList[CodeableConcept[MeasureTypeCode]]] = None,
        riskAdjustment: Optional[FhirString] = None,
        rateAggregation: Optional[FhirString] = None,
        rationale: Optional[FhirMarkdown] = None,
        clinicalRecommendationStatement: Optional[FhirMarkdown] = None,
        improvementNotation: Optional[
            CodeableConcept[MeasureImprovementNotationCode]
        ] = None,
        definition: Optional[FhirList[FhirMarkdown]] = None,
        guidance: Optional[FhirMarkdown] = None,
        group: Optional[FhirList[MeasureGroup]] = None,
        supplementalData: Optional[FhirList[MeasureSupplementalData]] = None,
    ) -> None:
        """
            The Measure resource provides the definition of a quality measure.
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
            :param url: An absolute URI that is used to identify this measure when it is referenced in
        a specification, model, design or an instance; also called its canonical
        identifier. This SHOULD be globally unique and SHOULD be a literal address at
        which at which an authoritative instance of this measure is (or will be)
        published. This URL can be the target of a canonical reference. It SHALL
        remain the same when the measure is stored on different servers.
            :param identifier: A formal identifier that is used to identify this measure when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance.
            :param version: The identifier that is used to identify this version of the measure when it is
        referenced in a specification, model, design or instance. This is an arbitrary
        value managed by the measure author and is not expected to be globally unique.
        For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
        not available. There is also no expectation that versions can be placed in a
        lexicographical sequence. To provide a version consistent with the Decision
        Support Service specification, use the format Major.Minor.Revision (e.g.
        1.0.0). For more information on versioning knowledge assets, refer to the
        Decision Support Service specification. Note that a version is required for
        non-experimental active artifacts.
            :param name: A natural language name identifying the measure. This name should be usable as
        an identifier for the module by machine processing applications such as code
        generation.
            :param title: A short, descriptive, user-friendly title for the measure.
            :param subtitle: An explanatory or alternate title for the measure giving additional
        information about its content.
            :param status: The status of this measure. Enables tracking the life-cycle of the content.
            :param experimental: A Boolean value to indicate that this measure is authored for testing purposes
        (or education/evaluation/marketing) and is not intended to be used for genuine
        usage.
            :param subjectCodeableConcept: None
            :param subjectReference: None
            :param date: The date  (and optionally time) when the measure was published. The date must
        change when the business version changes and it must change if the status code
        changes. In addition, it should change when the substantive content of the
        measure changes.
            :param publisher: The name of the organization or individual that published the measure.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the measure from a consumer's
        perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate measure
        instances.
            :param jurisdiction: A legal or geographic region in which the measure is intended to be used.
            :param purpose: Explanation of why this measure is needed and why it has been designed as it
        has.
            :param usage: A detailed description, from a clinical perspective, of how the measure is
        used.
            :param copyright: A copyright statement relating to the measure and/or its contents. Copyright
        statements are generally legal restrictions on the use and publishing of the
        measure.
            :param approvalDate: The date on which the resource content was approved by the publisher. Approval
        happens once when the content is officially approved for usage.
            :param lastReviewDate: The date on which the resource content was last reviewed. Review happens
        periodically after approval but does not change the original approval date.
            :param effectivePeriod: The period during which the measure content was or is planned to be in active
        use.
            :param topic: Descriptive topics related to the content of the measure. Topics provide a
        high-level categorization grouping types of measures that can be useful for
        filtering and searching.
            :param author: An individiual or organization primarily involved in the creation and
        maintenance of the content.
            :param editor: An individual or organization primarily responsible for internal coherence of
        the content.
            :param reviewer: An individual or organization primarily responsible for review of some aspect
        of the content.
            :param endorser: An individual or organization responsible for officially endorsing the content
        for use in some setting.
            :param relatedArtifact: Related artifacts such as additional documentation, justification, or
        bibliographic references.
            :param library: A reference to a Library resource containing the formal logic used by the
        measure.
            :param disclaimer: Notices and disclaimers regarding the use of the measure or related to
        intellectual property (such as code systems) referenced by the measure.
            :param scoring: Indicates how the calculation is performed for the measure, including
        proportion, ratio, continuous-variable, and cohort. The value set is
        extensible, allowing additional measure scoring types to be represented.
            :param compositeScoring: If this is a composite measure, the scoring method used to combine the
        component measures to determine the composite score.
            :param type_: Indicates whether the measure is used to examine a process, an outcome over
        time, a patient-reported outcome, or a structure measure such as utilization.
            :param riskAdjustment: A description of the risk adjustment factors that may impact the resulting
        score for the measure and how they may be accounted for when computing and
        reporting measure results.
            :param rateAggregation: Describes how to combine the information calculated, based on logic in each of
        several populations, into one summarized result.
            :param rationale: Provides a succinct statement of the need for the measure. Usually includes
        statements pertaining to importance criterion: impact, gap in care, and
        evidence.
            :param clinicalRecommendationStatement: Provides a summary of relevant clinical guidelines or other clinical
        recommendations supporting the measure.
            :param improvementNotation: Information on whether an increase or decrease in score is the preferred
        result (e.g., a higher score indicates better quality OR a lower score
        indicates better quality OR quality is within a range).
            :param definition: Provides a description of an individual term used within the measure.
            :param guidance: Additional guidance for the measure including how it can be used in a clinical
        context, and the intent of the measure.
            :param group: A group of population criteria for the measure.
            :param supplementalData: The supplemental data criteria for the measure report, specified as either the
        name of a valid CQL expression within a referenced library, or a valid FHIR
        Resource Path.
        """
        super().__init__(
            resourceType="Measure",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            subtitle=subtitle,
            status=status,
            experimental=experimental,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            usage=usage,
            copyright=copyright,
            approvalDate=approvalDate,
            lastReviewDate=lastReviewDate,
            effectivePeriod=effectivePeriod,
            topic=topic,
            author=author,
            editor=editor,
            reviewer=reviewer,
            endorser=endorser,
            relatedArtifact=relatedArtifact,
            library=library,
            disclaimer=disclaimer,
            scoring=scoring,
            compositeScoring=compositeScoring,
            type_=type_,
            riskAdjustment=riskAdjustment,
            rateAggregation=rateAggregation,
            rationale=rationale,
            clinicalRecommendationStatement=clinicalRecommendationStatement,
            improvementNotation=improvementNotation,
            definition=definition,
            guidance=guidance,
            group=group,
            supplementalData=supplementalData,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return MeasureSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
