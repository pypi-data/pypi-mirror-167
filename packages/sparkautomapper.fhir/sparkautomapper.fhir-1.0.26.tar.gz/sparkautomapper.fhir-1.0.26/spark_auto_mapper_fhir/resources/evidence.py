from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.evidence import EvidenceSchema

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
    # shortTitle (string)
    # subtitle (string)
    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
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

    # exposureBackground (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for exposureBackground
    from spark_auto_mapper_fhir.resources.evidence_variable import EvidenceVariable

    # exposureVariant (Reference)
    # Imports for References for exposureVariant
    # outcome (Reference)
    # Imports for References for outcome


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Evidence(FhirResourceBase):
    """
    Evidence
    evidence.xsd
        The Evidence resource describes the conditional state (population and any
    exposures being compared within the population) and outcome (if specified)
    that the knowledge (evidence, assertion, recommendation) is about.
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
        shortTitle: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        status: PublicationStatusCode,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        note: Optional[FhirList[Annotation]] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
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
        exposureBackground: Reference[EvidenceVariable],
        exposureVariant: Optional[FhirList[Reference[EvidenceVariable]]] = None,
        outcome: Optional[FhirList[Reference[EvidenceVariable]]] = None,
    ) -> None:
        """
            The Evidence resource describes the conditional state (population and any
        exposures being compared within the population) and outcome (if specified)
        that the knowledge (evidence, assertion, recommendation) is about.
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
            :param url: An absolute URI that is used to identify this evidence when it is referenced
        in a specification, model, design or an instance; also called its canonical
        identifier. This SHOULD be globally unique and SHOULD be a literal address at
        which at which an authoritative instance of this evidence is (or will be)
        published. This URL can be the target of a canonical reference. It SHALL
        remain the same when the evidence is stored on different servers.
            :param identifier: A formal identifier that is used to identify this evidence when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance.
            :param version: The identifier that is used to identify this version of the evidence when it
        is referenced in a specification, model, design or instance. This is an
        arbitrary value managed by the evidence author and is not expected to be
        globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
        managed version is not available. There is also no expectation that versions
        can be placed in a lexicographical sequence. To provide a version consistent
        with the Decision Support Service specification, use the format
        Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
        knowledge assets, refer to the Decision Support Service specification. Note
        that a version is required for non-experimental active artifacts.
            :param name: A natural language name identifying the evidence. This name should be usable
        as an identifier for the module by machine processing applications such as
        code generation.
            :param title: A short, descriptive, user-friendly title for the evidence.
            :param shortTitle: The short title provides an alternate title for use in informal descriptive
        contexts where the full, formal title is not necessary.
            :param subtitle: An explanatory or alternate title for the Evidence giving additional
        information about its content.
            :param status: The status of this evidence. Enables tracking the life-cycle of the content.
            :param date: The date  (and optionally time) when the evidence was published. The date must
        change when the business version changes and it must change if the status code
        changes. In addition, it should change when the substantive content of the
        evidence changes.
            :param publisher: The name of the organization or individual that published the evidence.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the evidence from a consumer's
        perspective.
            :param note: A human-readable string to clarify or explain concepts about the resource.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate evidence
        instances.
            :param jurisdiction: A legal or geographic region in which the evidence is intended to be used.
            :param copyright: A copyright statement relating to the evidence and/or its contents. Copyright
        statements are generally legal restrictions on the use and publishing of the
        evidence.
            :param approvalDate: The date on which the resource content was approved by the publisher. Approval
        happens once when the content is officially approved for usage.
            :param lastReviewDate: The date on which the resource content was last reviewed. Review happens
        periodically after approval but does not change the original approval date.
            :param effectivePeriod: The period during which the evidence content was or is planned to be in active
        use.
            :param topic: Descriptive topics related to the content of the Evidence. Topics provide a
        high-level categorization grouping types of Evidences that can be useful for
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
            :param exposureBackground: A reference to a EvidenceVariable resource that defines the population for the
        research.
            :param exposureVariant: A reference to a EvidenceVariable resource that defines the exposure for the
        research.
            :param outcome: A reference to a EvidenceVariable resomece that defines the outcome for the
        research.
        """
        super().__init__(
            resourceType="Evidence",
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
            shortTitle=shortTitle,
            subtitle=subtitle,
            status=status,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            note=note,
            useContext=useContext,
            jurisdiction=jurisdiction,
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
            exposureBackground=exposureBackground,
            exposureVariant=exposureVariant,
            outcome=outcome,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return EvidenceSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
