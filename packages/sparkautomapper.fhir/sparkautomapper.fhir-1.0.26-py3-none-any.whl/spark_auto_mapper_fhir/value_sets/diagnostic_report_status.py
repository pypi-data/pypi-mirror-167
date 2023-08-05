from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DiagnosticReportStatusCode(GenericTypeCode):
    """
    DiagnosticReportStatus
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
        The status of the diagnostic report.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/diagnostic-report-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/diagnostic-report-status"


class DiagnosticReportStatusCodeValues:
    """
    The existence of the report is registered, but there is nothing yet available.
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """

    Registered = DiagnosticReportStatusCode("registered")
    """
    This is a partial (e.g. initial, interim or preliminary) report: data in the
    report may be incomplete or unverified.
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    Partial = DiagnosticReportStatusCode("partial")
    """
    The report is complete and verified by an authorized person.
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    Final = DiagnosticReportStatusCode("final")
    """
    Subsequent to being final, the report has been modified.  This includes any
    change in the results, diagnosis, narrative text, or other content of a report
    that has been issued.
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    Amended = DiagnosticReportStatusCode("amended")
    """
    The report is unavailable because the measurement was not started or not
    completed (also sometimes called "aborted").
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    Cancelled = DiagnosticReportStatusCode("cancelled")
    """
    The report has been withdrawn following a previous final release.  This
    electronic record should never have existed, though it is possible that real-
    world decisions were based on it. (If real-world activity has occurred, the
    status should be "cancelled" rather than "entered-in-error".).
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    EnteredInError = DiagnosticReportStatusCode("entered-in-error")
    """
    The authoring/source system does not know which of the status values currently
    applies for this observation. Note: This concept is not to be used for "other"
    - one of the listed statuses is presumed to apply, but the authoring/source
    system does not know which.
    From: http://hl7.org/fhir/diagnostic-report-status in valuesets.xml
    """
    Unknown = DiagnosticReportStatusCode("unknown")
