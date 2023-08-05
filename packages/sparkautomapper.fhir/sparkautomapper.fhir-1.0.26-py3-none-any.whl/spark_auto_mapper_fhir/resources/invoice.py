from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.invoice import InvoiceSchema

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

    # status (InvoiceStatus)
    from spark_auto_mapper_fhir.value_sets.invoice_status import InvoiceStatusCode

    # cancelledReason (string)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for type_
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # recipient (Reference)
    # Imports for References for recipient
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # date (dateTime)
    # participant (Invoice.Participant)
    from spark_auto_mapper_fhir.backbone_elements.invoice_participant import (
        InvoiceParticipant,
    )

    # issuer (Reference)
    # Imports for References for issuer
    # account (Reference)
    # Imports for References for account
    from spark_auto_mapper_fhir.resources.account import Account

    # lineItem (Invoice.LineItem)
    from spark_auto_mapper_fhir.backbone_elements.invoice_line_item import (
        InvoiceLineItem,
    )

    # totalPriceComponent (Invoice.PriceComponent)
    from spark_auto_mapper_fhir.backbone_elements.invoice_price_component import (
        InvoicePriceComponent,
    )

    # totalNet (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # totalGross (Money)
    # paymentTerms (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Invoice(FhirResourceBase):
    """
    Invoice
    invoice.xsd
        Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
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
        status: InvoiceStatusCode,
        cancelledReason: Optional[FhirString] = None,
        type_: Optional[CodeableConcept[GenericTypeCode]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        recipient: Optional[
            Reference[Union[Organization, Patient, RelatedPerson]]
        ] = None,
        date: Optional[FhirDateTime] = None,
        participant: Optional[FhirList[InvoiceParticipant]] = None,
        issuer: Optional[Reference[Organization]] = None,
        account: Optional[Reference[Account]] = None,
        lineItem: Optional[FhirList[InvoiceLineItem]] = None,
        totalPriceComponent: Optional[FhirList[InvoicePriceComponent]] = None,
        totalNet: Optional[Money] = None,
        totalGross: Optional[Money] = None,
        paymentTerms: Optional[FhirMarkdown] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            Invoice containing collected ChargeItems from an Account with calculated
        individual and total price for Billing purpose.
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
            :param identifier: Identifier of this Invoice, often used for reference in correspondence about
        this invoice or for tracking of payments.
            :param status: The current state of the Invoice.
            :param cancelledReason: In case of Invoice cancellation a reason must be given (entered in error,
        superseded by corrected invoice etc.).
            :param type_: Type of Invoice depending on domain, realm an usage (e.g. internal/external,
        dental, preliminary).
            :param subject: The individual or set of individuals receiving the goods and services billed
        in this invoice.
            :param recipient: The individual or Organization responsible for balancing of this invoice.
            :param date: Date/time(s) of when this Invoice was posted.
            :param participant: Indicates who or what performed or participated in the charged service.
            :param issuer: The organizationissuing the Invoice.
            :param account: Account which is supposed to be balanced with this Invoice.
            :param lineItem: Each line item represents one charge for goods and services rendered. Details
        such as date, code and amount are found in the referenced ChargeItem resource.
            :param totalPriceComponent: The total amount for the Invoice may be calculated as the sum of the line
        items with surcharges/deductions that apply in certain conditions.  The
        priceComponent element can be used to offer transparency to the recipient of
        the Invoice of how the total price was calculated.
            :param totalNet: Invoice total , taxes excluded.
            :param totalGross: Invoice total, tax included.
            :param paymentTerms: Payment details such as banking details, period of payment, deductibles,
        methods of payment.
            :param note: Comments made about the invoice by the issuer, subject, or other participants.
        """
        super().__init__(
            resourceType="Invoice",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            cancelledReason=cancelledReason,
            type_=type_,
            subject=subject,
            recipient=recipient,
            date=date,
            participant=participant,
            issuer=issuer,
            account=account,
            lineItem=lineItem,
            totalPriceComponent=totalPriceComponent,
            totalNet=totalNet,
            totalGross=totalGross,
            paymentTerms=paymentTerms,
            note=note,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return InvoiceSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
