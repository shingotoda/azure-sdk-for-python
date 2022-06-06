# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ApplicationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of application being monitored.
    """

    WEB = "web"
    OTHER = "other"

class FlowType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Used by the Application Insights system to determine what kind of flow this component was
    created by. This is to be set to 'Bluefield' when creating/updating a component via the REST
    API.
    """

    BLUEFIELD = "Bluefield"

class IngestionMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the flow of the ingestion.
    """

    APPLICATION_INSIGHTS = "ApplicationInsights"
    APPLICATION_INSIGHTS_WITH_DIAGNOSTIC_SETTINGS = "ApplicationInsightsWithDiagnosticSettings"
    LOG_ANALYTICS = "LogAnalytics"

class PublicNetworkAccessType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The network access type for operating on the Application Insights Component. By default it is
    Enabled
    """

    #: Enables connectivity to Application Insights through public DNS.
    ENABLED = "Enabled"
    #: Disables public connectivity to Application Insights through public DNS.
    DISABLED = "Disabled"

class PurgeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the operation represented by the requested Id.
    """

    PENDING = "pending"
    COMPLETED = "completed"

class RequestSource(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes what tool created this Application Insights component. Customers using this API
    should set this to the default 'rest'.
    """

    REST = "rest"