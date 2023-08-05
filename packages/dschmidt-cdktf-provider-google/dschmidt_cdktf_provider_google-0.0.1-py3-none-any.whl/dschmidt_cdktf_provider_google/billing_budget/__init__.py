import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class BillingBudget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/billing_budget google_billing_budget}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        amount: typing.Union["BillingBudgetAmount", typing.Dict[str, typing.Any]],
        billing_account: builtins.str,
        all_updates_rule: typing.Optional[typing.Union["BillingBudgetAllUpdatesRule", typing.Dict[str, typing.Any]]] = None,
        budget_filter: typing.Optional[typing.Union["BillingBudgetBudgetFilter", typing.Dict[str, typing.Any]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        threshold_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BillingBudgetThresholdRules", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["BillingBudgetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/billing_budget google_billing_budget} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param amount: amount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#amount BillingBudget#amount}
        :param billing_account: ID of the billing account to set a budget on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#billing_account BillingBudget#billing_account}
        :param all_updates_rule: all_updates_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#all_updates_rule BillingBudget#all_updates_rule}
        :param budget_filter: budget_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#budget_filter BillingBudget#budget_filter}
        :param display_name: User data for display name in UI. Must be <= 60 chars. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#display_name BillingBudget#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#id BillingBudget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param threshold_rules: threshold_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#threshold_rules BillingBudget#threshold_rules}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#timeouts BillingBudget#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BillingBudgetConfig(
            amount=amount,
            billing_account=billing_account,
            all_updates_rule=all_updates_rule,
            budget_filter=budget_filter,
            display_name=display_name,
            id=id,
            threshold_rules=threshold_rules,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllUpdatesRule")
    def put_all_updates_rule(
        self,
        *,
        disable_default_iam_recipients: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitoring_notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        pubsub_topic: typing.Optional[builtins.str] = None,
        schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disable_default_iam_recipients: Boolean. When set to true, disables default notifications sent when a threshold is exceeded. Default recipients are those with Billing Account Administrators and Billing Account Users IAM roles for the target account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#disable_default_iam_recipients BillingBudget#disable_default_iam_recipients}
        :param monitoring_notification_channels: The full resource name of a monitoring notification channel in the form projects/{project_id}/notificationChannels/{channel_id}. A maximum of 5 channels are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#monitoring_notification_channels BillingBudget#monitoring_notification_channels}
        :param pubsub_topic: The name of the Cloud Pub/Sub topic where budget related messages will be published, in the form projects/{project_id}/topics/{topic_id}. Updates are sent at regular intervals to the topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#pubsub_topic BillingBudget#pubsub_topic}
        :param schema_version: The schema version of the notification. Only "1.0" is accepted. It represents the JSON schema as defined in https://cloud.google.com/billing/docs/how-to/budgets#notification_format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#schema_version BillingBudget#schema_version}
        '''
        value = BillingBudgetAllUpdatesRule(
            disable_default_iam_recipients=disable_default_iam_recipients,
            monitoring_notification_channels=monitoring_notification_channels,
            pubsub_topic=pubsub_topic,
            schema_version=schema_version,
        )

        return typing.cast(None, jsii.invoke(self, "putAllUpdatesRule", [value]))

    @jsii.member(jsii_name="putAmount")
    def put_amount(
        self,
        *,
        last_period_amount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        specified_amount: typing.Optional[typing.Union["BillingBudgetAmountSpecifiedAmount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param last_period_amount: Configures a budget amount that is automatically set to 100% of last period's spend. Boolean. Set value to true to use. Do not set to false, instead use the 'specified_amount' block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#last_period_amount BillingBudget#last_period_amount}
        :param specified_amount: specified_amount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#specified_amount BillingBudget#specified_amount}
        '''
        value = BillingBudgetAmount(
            last_period_amount=last_period_amount, specified_amount=specified_amount
        )

        return typing.cast(None, jsii.invoke(self, "putAmount", [value]))

    @jsii.member(jsii_name="putBudgetFilter")
    def put_budget_filter(
        self,
        *,
        calendar_period: typing.Optional[builtins.str] = None,
        credit_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        credit_types_treatment: typing.Optional[builtins.str] = None,
        custom_period: typing.Optional[typing.Union["BillingBudgetBudgetFilterCustomPeriod", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        projects: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        subaccounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param calendar_period: A CalendarPeriod represents the abstract concept of a recurring time period that has a canonical start. Grammatically, "the start of the current CalendarPeriod". All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8). Exactly one of 'calendar_period', 'custom_period' must be provided. Possible values: ["MONTH", "QUARTER", "YEAR", "CALENDAR_PERIOD_UNSPECIFIED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#calendar_period BillingBudget#calendar_period}
        :param credit_types: Optional. If creditTypesTreatment is INCLUDE_SPECIFIED_CREDITS, this is a list of credit types to be subtracted from gross cost to determine the spend for threshold calculations. See a list of acceptable credit type values. If creditTypesTreatment is not INCLUDE_SPECIFIED_CREDITS, this field must be empty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types BillingBudget#credit_types}
        :param credit_types_treatment: Specifies how credits should be treated when determining spend for threshold calculations. Default value: "INCLUDE_ALL_CREDITS" Possible values: ["INCLUDE_ALL_CREDITS", "EXCLUDE_ALL_CREDITS", "INCLUDE_SPECIFIED_CREDITS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types_treatment BillingBudget#credit_types_treatment}
        :param custom_period: custom_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#custom_period BillingBudget#custom_period}
        :param labels: A single label and value pair specifying that usage from only this set of labeled resources should be included in the budget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#labels BillingBudget#labels}
        :param projects: A set of projects of the form projects/{project_number}, specifying that usage from only this set of projects should be included in the budget. If omitted, the report will include all usage for the billing account, regardless of which project the usage occurred on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#projects BillingBudget#projects}
        :param services: A set of services of the form services/{service_id}, specifying that usage from only this set of services should be included in the budget. If omitted, the report will include usage for all the services. The service names are available through the Catalog API: https://cloud.google.com/billing/v1/how-tos/catalog-api. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#services BillingBudget#services}
        :param subaccounts: A set of subaccounts of the form billingAccounts/{account_id}, specifying that usage from only this set of subaccounts should be included in the budget. If a subaccount is set to the name of the parent account, usage from the parent account will be included. If the field is omitted, the report will include usage from the parent account and all subaccounts, if they exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#subaccounts BillingBudget#subaccounts}
        '''
        value = BillingBudgetBudgetFilter(
            calendar_period=calendar_period,
            credit_types=credit_types,
            credit_types_treatment=credit_types_treatment,
            custom_period=custom_period,
            labels=labels,
            projects=projects,
            services=services,
            subaccounts=subaccounts,
        )

        return typing.cast(None, jsii.invoke(self, "putBudgetFilter", [value]))

    @jsii.member(jsii_name="putThresholdRules")
    def put_threshold_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BillingBudgetThresholdRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudget.put_threshold_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThresholdRules", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#create BillingBudget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#delete BillingBudget#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#update BillingBudget#update}.
        '''
        value = BillingBudgetTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllUpdatesRule")
    def reset_all_updates_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllUpdatesRule", []))

    @jsii.member(jsii_name="resetBudgetFilter")
    def reset_budget_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBudgetFilter", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetThresholdRules")
    def reset_threshold_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdRules", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allUpdatesRule")
    def all_updates_rule(self) -> "BillingBudgetAllUpdatesRuleOutputReference":
        return typing.cast("BillingBudgetAllUpdatesRuleOutputReference", jsii.get(self, "allUpdatesRule"))

    @builtins.property
    @jsii.member(jsii_name="amount")
    def amount(self) -> "BillingBudgetAmountOutputReference":
        return typing.cast("BillingBudgetAmountOutputReference", jsii.get(self, "amount"))

    @builtins.property
    @jsii.member(jsii_name="budgetFilter")
    def budget_filter(self) -> "BillingBudgetBudgetFilterOutputReference":
        return typing.cast("BillingBudgetBudgetFilterOutputReference", jsii.get(self, "budgetFilter"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="thresholdRules")
    def threshold_rules(self) -> "BillingBudgetThresholdRulesList":
        return typing.cast("BillingBudgetThresholdRulesList", jsii.get(self, "thresholdRules"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BillingBudgetTimeoutsOutputReference":
        return typing.cast("BillingBudgetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allUpdatesRuleInput")
    def all_updates_rule_input(self) -> typing.Optional["BillingBudgetAllUpdatesRule"]:
        return typing.cast(typing.Optional["BillingBudgetAllUpdatesRule"], jsii.get(self, "allUpdatesRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="amountInput")
    def amount_input(self) -> typing.Optional["BillingBudgetAmount"]:
        return typing.cast(typing.Optional["BillingBudgetAmount"], jsii.get(self, "amountInput"))

    @builtins.property
    @jsii.member(jsii_name="billingAccountInput")
    def billing_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="budgetFilterInput")
    def budget_filter_input(self) -> typing.Optional["BillingBudgetBudgetFilter"]:
        return typing.cast(typing.Optional["BillingBudgetBudgetFilter"], jsii.get(self, "budgetFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdRulesInput")
    def threshold_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BillingBudgetThresholdRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BillingBudgetThresholdRules"]]], jsii.get(self, "thresholdRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BillingBudgetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BillingBudgetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="billingAccount")
    def billing_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "billingAccount"))

    @billing_account.setter
    def billing_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudget, "billing_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingAccount", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudget, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAllUpdatesRule",
    jsii_struct_bases=[],
    name_mapping={
        "disable_default_iam_recipients": "disableDefaultIamRecipients",
        "monitoring_notification_channels": "monitoringNotificationChannels",
        "pubsub_topic": "pubsubTopic",
        "schema_version": "schemaVersion",
    },
)
class BillingBudgetAllUpdatesRule:
    def __init__(
        self,
        *,
        disable_default_iam_recipients: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitoring_notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        pubsub_topic: typing.Optional[builtins.str] = None,
        schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disable_default_iam_recipients: Boolean. When set to true, disables default notifications sent when a threshold is exceeded. Default recipients are those with Billing Account Administrators and Billing Account Users IAM roles for the target account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#disable_default_iam_recipients BillingBudget#disable_default_iam_recipients}
        :param monitoring_notification_channels: The full resource name of a monitoring notification channel in the form projects/{project_id}/notificationChannels/{channel_id}. A maximum of 5 channels are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#monitoring_notification_channels BillingBudget#monitoring_notification_channels}
        :param pubsub_topic: The name of the Cloud Pub/Sub topic where budget related messages will be published, in the form projects/{project_id}/topics/{topic_id}. Updates are sent at regular intervals to the topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#pubsub_topic BillingBudget#pubsub_topic}
        :param schema_version: The schema version of the notification. Only "1.0" is accepted. It represents the JSON schema as defined in https://cloud.google.com/billing/docs/how-to/budgets#notification_format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#schema_version BillingBudget#schema_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAllUpdatesRule.__init__)
            check_type(argname="argument disable_default_iam_recipients", value=disable_default_iam_recipients, expected_type=type_hints["disable_default_iam_recipients"])
            check_type(argname="argument monitoring_notification_channels", value=monitoring_notification_channels, expected_type=type_hints["monitoring_notification_channels"])
            check_type(argname="argument pubsub_topic", value=pubsub_topic, expected_type=type_hints["pubsub_topic"])
            check_type(argname="argument schema_version", value=schema_version, expected_type=type_hints["schema_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_default_iam_recipients is not None:
            self._values["disable_default_iam_recipients"] = disable_default_iam_recipients
        if monitoring_notification_channels is not None:
            self._values["monitoring_notification_channels"] = monitoring_notification_channels
        if pubsub_topic is not None:
            self._values["pubsub_topic"] = pubsub_topic
        if schema_version is not None:
            self._values["schema_version"] = schema_version

    @builtins.property
    def disable_default_iam_recipients(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean.

        When set to true, disables default notifications sent
        when a threshold is exceeded. Default recipients are
        those with Billing Account Administrators and Billing
        Account Users IAM roles for the target account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#disable_default_iam_recipients BillingBudget#disable_default_iam_recipients}
        '''
        result = self._values.get("disable_default_iam_recipients")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def monitoring_notification_channels(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The full resource name of a monitoring notification channel in the form projects/{project_id}/notificationChannels/{channel_id}. A maximum of 5 channels are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#monitoring_notification_channels BillingBudget#monitoring_notification_channels}
        '''
        result = self._values.get("monitoring_notification_channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pubsub_topic(self) -> typing.Optional[builtins.str]:
        '''The name of the Cloud Pub/Sub topic where budget related messages will be published, in the form projects/{project_id}/topics/{topic_id}.

        Updates are sent
        at regular intervals to the topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#pubsub_topic BillingBudget#pubsub_topic}
        '''
        result = self._values.get("pubsub_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_version(self) -> typing.Optional[builtins.str]:
        '''The schema version of the notification. Only "1.0" is accepted. It represents the JSON schema as defined in https://cloud.google.com/billing/docs/how-to/budgets#notification_format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#schema_version BillingBudget#schema_version}
        '''
        result = self._values.get("schema_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetAllUpdatesRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetAllUpdatesRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAllUpdatesRuleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAllUpdatesRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisableDefaultIamRecipients")
    def reset_disable_default_iam_recipients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableDefaultIamRecipients", []))

    @jsii.member(jsii_name="resetMonitoringNotificationChannels")
    def reset_monitoring_notification_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringNotificationChannels", []))

    @jsii.member(jsii_name="resetPubsubTopic")
    def reset_pubsub_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubsubTopic", []))

    @jsii.member(jsii_name="resetSchemaVersion")
    def reset_schema_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaVersion", []))

    @builtins.property
    @jsii.member(jsii_name="disableDefaultIamRecipientsInput")
    def disable_default_iam_recipients_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableDefaultIamRecipientsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringNotificationChannelsInput")
    def monitoring_notification_channels_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monitoringNotificationChannelsInput"))

    @builtins.property
    @jsii.member(jsii_name="pubsubTopicInput")
    def pubsub_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pubsubTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaVersionInput")
    def schema_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableDefaultIamRecipients")
    def disable_default_iam_recipients(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableDefaultIamRecipients"))

    @disable_default_iam_recipients.setter
    def disable_default_iam_recipients(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAllUpdatesRuleOutputReference, "disable_default_iam_recipients").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableDefaultIamRecipients", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringNotificationChannels")
    def monitoring_notification_channels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitoringNotificationChannels"))

    @monitoring_notification_channels.setter
    def monitoring_notification_channels(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAllUpdatesRuleOutputReference, "monitoring_notification_channels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringNotificationChannels", value)

    @builtins.property
    @jsii.member(jsii_name="pubsubTopic")
    def pubsub_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pubsubTopic"))

    @pubsub_topic.setter
    def pubsub_topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAllUpdatesRuleOutputReference, "pubsub_topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pubsubTopic", value)

    @builtins.property
    @jsii.member(jsii_name="schemaVersion")
    def schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaVersion"))

    @schema_version.setter
    def schema_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAllUpdatesRuleOutputReference, "schema_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BillingBudgetAllUpdatesRule]:
        return typing.cast(typing.Optional[BillingBudgetAllUpdatesRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BillingBudgetAllUpdatesRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAllUpdatesRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAmount",
    jsii_struct_bases=[],
    name_mapping={
        "last_period_amount": "lastPeriodAmount",
        "specified_amount": "specifiedAmount",
    },
)
class BillingBudgetAmount:
    def __init__(
        self,
        *,
        last_period_amount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        specified_amount: typing.Optional[typing.Union["BillingBudgetAmountSpecifiedAmount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param last_period_amount: Configures a budget amount that is automatically set to 100% of last period's spend. Boolean. Set value to true to use. Do not set to false, instead use the 'specified_amount' block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#last_period_amount BillingBudget#last_period_amount}
        :param specified_amount: specified_amount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#specified_amount BillingBudget#specified_amount}
        '''
        if isinstance(specified_amount, dict):
            specified_amount = BillingBudgetAmountSpecifiedAmount(**specified_amount)
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAmount.__init__)
            check_type(argname="argument last_period_amount", value=last_period_amount, expected_type=type_hints["last_period_amount"])
            check_type(argname="argument specified_amount", value=specified_amount, expected_type=type_hints["specified_amount"])
        self._values: typing.Dict[str, typing.Any] = {}
        if last_period_amount is not None:
            self._values["last_period_amount"] = last_period_amount
        if specified_amount is not None:
            self._values["specified_amount"] = specified_amount

    @builtins.property
    def last_period_amount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Configures a budget amount that is automatically set to 100% of last period's spend.

        Boolean. Set value to true to use. Do not set to false, instead
        use the 'specified_amount' block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#last_period_amount BillingBudget#last_period_amount}
        '''
        result = self._values.get("last_period_amount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def specified_amount(self) -> typing.Optional["BillingBudgetAmountSpecifiedAmount"]:
        '''specified_amount block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#specified_amount BillingBudget#specified_amount}
        '''
        result = self._values.get("specified_amount")
        return typing.cast(typing.Optional["BillingBudgetAmountSpecifiedAmount"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetAmount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetAmountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAmountOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAmountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSpecifiedAmount")
    def put_specified_amount(
        self,
        *,
        currency_code: typing.Optional[builtins.str] = None,
        nanos: typing.Optional[jsii.Number] = None,
        units: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param currency_code: The 3-letter currency code defined in ISO 4217. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#currency_code BillingBudget#currency_code}
        :param nanos: Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If units is positive, nanos must be positive or zero. If units is zero, nanos can be positive, zero, or negative. If units is negative, nanos must be negative or zero. For example $-1.75 is represented as units=-1 and nanos=-750,000,000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#nanos BillingBudget#nanos}
        :param units: The whole units of the amount. For example if currencyCode is "USD", then 1 unit is one US dollar. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#units BillingBudget#units}
        '''
        value = BillingBudgetAmountSpecifiedAmount(
            currency_code=currency_code, nanos=nanos, units=units
        )

        return typing.cast(None, jsii.invoke(self, "putSpecifiedAmount", [value]))

    @jsii.member(jsii_name="resetLastPeriodAmount")
    def reset_last_period_amount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastPeriodAmount", []))

    @jsii.member(jsii_name="resetSpecifiedAmount")
    def reset_specified_amount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpecifiedAmount", []))

    @builtins.property
    @jsii.member(jsii_name="specifiedAmount")
    def specified_amount(self) -> "BillingBudgetAmountSpecifiedAmountOutputReference":
        return typing.cast("BillingBudgetAmountSpecifiedAmountOutputReference", jsii.get(self, "specifiedAmount"))

    @builtins.property
    @jsii.member(jsii_name="lastPeriodAmountInput")
    def last_period_amount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lastPeriodAmountInput"))

    @builtins.property
    @jsii.member(jsii_name="specifiedAmountInput")
    def specified_amount_input(
        self,
    ) -> typing.Optional["BillingBudgetAmountSpecifiedAmount"]:
        return typing.cast(typing.Optional["BillingBudgetAmountSpecifiedAmount"], jsii.get(self, "specifiedAmountInput"))

    @builtins.property
    @jsii.member(jsii_name="lastPeriodAmount")
    def last_period_amount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lastPeriodAmount"))

    @last_period_amount.setter
    def last_period_amount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountOutputReference, "last_period_amount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastPeriodAmount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BillingBudgetAmount]:
        return typing.cast(typing.Optional[BillingBudgetAmount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BillingBudgetAmount]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAmountSpecifiedAmount",
    jsii_struct_bases=[],
    name_mapping={"currency_code": "currencyCode", "nanos": "nanos", "units": "units"},
)
class BillingBudgetAmountSpecifiedAmount:
    def __init__(
        self,
        *,
        currency_code: typing.Optional[builtins.str] = None,
        nanos: typing.Optional[jsii.Number] = None,
        units: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param currency_code: The 3-letter currency code defined in ISO 4217. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#currency_code BillingBudget#currency_code}
        :param nanos: Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If units is positive, nanos must be positive or zero. If units is zero, nanos can be positive, zero, or negative. If units is negative, nanos must be negative or zero. For example $-1.75 is represented as units=-1 and nanos=-750,000,000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#nanos BillingBudget#nanos}
        :param units: The whole units of the amount. For example if currencyCode is "USD", then 1 unit is one US dollar. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#units BillingBudget#units}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAmountSpecifiedAmount.__init__)
            check_type(argname="argument currency_code", value=currency_code, expected_type=type_hints["currency_code"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
            check_type(argname="argument units", value=units, expected_type=type_hints["units"])
        self._values: typing.Dict[str, typing.Any] = {}
        if currency_code is not None:
            self._values["currency_code"] = currency_code
        if nanos is not None:
            self._values["nanos"] = nanos
        if units is not None:
            self._values["units"] = units

    @builtins.property
    def currency_code(self) -> typing.Optional[builtins.str]:
        '''The 3-letter currency code defined in ISO 4217.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#currency_code BillingBudget#currency_code}
        '''
        result = self._values.get("currency_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Number of nano (10^-9) units of the amount.

        The value must be between -999,999,999 and +999,999,999
        inclusive. If units is positive, nanos must be positive or
        zero. If units is zero, nanos can be positive, zero, or
        negative. If units is negative, nanos must be negative or
        zero. For example $-1.75 is represented as units=-1 and
        nanos=-750,000,000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#nanos BillingBudget#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def units(self) -> typing.Optional[builtins.str]:
        '''The whole units of the amount. For example if currencyCode is "USD", then 1 unit is one US dollar.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#units BillingBudget#units}
        '''
        result = self._values.get("units")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetAmountSpecifiedAmount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetAmountSpecifiedAmountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetAmountSpecifiedAmountOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetAmountSpecifiedAmountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCurrencyCode")
    def reset_currency_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurrencyCode", []))

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @jsii.member(jsii_name="resetUnits")
    def reset_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnits", []))

    @builtins.property
    @jsii.member(jsii_name="currencyCodeInput")
    def currency_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currencyCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="unitsInput")
    def units_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitsInput"))

    @builtins.property
    @jsii.member(jsii_name="currencyCode")
    def currency_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currencyCode"))

    @currency_code.setter
    def currency_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountSpecifiedAmountOutputReference, "currency_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currencyCode", value)

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountSpecifiedAmountOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="units")
    def units(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "units"))

    @units.setter
    def units(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountSpecifiedAmountOutputReference, "units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "units", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BillingBudgetAmountSpecifiedAmount]:
        return typing.cast(typing.Optional[BillingBudgetAmountSpecifiedAmount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BillingBudgetAmountSpecifiedAmount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetAmountSpecifiedAmountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilter",
    jsii_struct_bases=[],
    name_mapping={
        "calendar_period": "calendarPeriod",
        "credit_types": "creditTypes",
        "credit_types_treatment": "creditTypesTreatment",
        "custom_period": "customPeriod",
        "labels": "labels",
        "projects": "projects",
        "services": "services",
        "subaccounts": "subaccounts",
    },
)
class BillingBudgetBudgetFilter:
    def __init__(
        self,
        *,
        calendar_period: typing.Optional[builtins.str] = None,
        credit_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        credit_types_treatment: typing.Optional[builtins.str] = None,
        custom_period: typing.Optional[typing.Union["BillingBudgetBudgetFilterCustomPeriod", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        projects: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        subaccounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param calendar_period: A CalendarPeriod represents the abstract concept of a recurring time period that has a canonical start. Grammatically, "the start of the current CalendarPeriod". All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8). Exactly one of 'calendar_period', 'custom_period' must be provided. Possible values: ["MONTH", "QUARTER", "YEAR", "CALENDAR_PERIOD_UNSPECIFIED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#calendar_period BillingBudget#calendar_period}
        :param credit_types: Optional. If creditTypesTreatment is INCLUDE_SPECIFIED_CREDITS, this is a list of credit types to be subtracted from gross cost to determine the spend for threshold calculations. See a list of acceptable credit type values. If creditTypesTreatment is not INCLUDE_SPECIFIED_CREDITS, this field must be empty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types BillingBudget#credit_types}
        :param credit_types_treatment: Specifies how credits should be treated when determining spend for threshold calculations. Default value: "INCLUDE_ALL_CREDITS" Possible values: ["INCLUDE_ALL_CREDITS", "EXCLUDE_ALL_CREDITS", "INCLUDE_SPECIFIED_CREDITS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types_treatment BillingBudget#credit_types_treatment}
        :param custom_period: custom_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#custom_period BillingBudget#custom_period}
        :param labels: A single label and value pair specifying that usage from only this set of labeled resources should be included in the budget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#labels BillingBudget#labels}
        :param projects: A set of projects of the form projects/{project_number}, specifying that usage from only this set of projects should be included in the budget. If omitted, the report will include all usage for the billing account, regardless of which project the usage occurred on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#projects BillingBudget#projects}
        :param services: A set of services of the form services/{service_id}, specifying that usage from only this set of services should be included in the budget. If omitted, the report will include usage for all the services. The service names are available through the Catalog API: https://cloud.google.com/billing/v1/how-tos/catalog-api. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#services BillingBudget#services}
        :param subaccounts: A set of subaccounts of the form billingAccounts/{account_id}, specifying that usage from only this set of subaccounts should be included in the budget. If a subaccount is set to the name of the parent account, usage from the parent account will be included. If the field is omitted, the report will include usage from the parent account and all subaccounts, if they exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#subaccounts BillingBudget#subaccounts}
        '''
        if isinstance(custom_period, dict):
            custom_period = BillingBudgetBudgetFilterCustomPeriod(**custom_period)
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilter.__init__)
            check_type(argname="argument calendar_period", value=calendar_period, expected_type=type_hints["calendar_period"])
            check_type(argname="argument credit_types", value=credit_types, expected_type=type_hints["credit_types"])
            check_type(argname="argument credit_types_treatment", value=credit_types_treatment, expected_type=type_hints["credit_types_treatment"])
            check_type(argname="argument custom_period", value=custom_period, expected_type=type_hints["custom_period"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument projects", value=projects, expected_type=type_hints["projects"])
            check_type(argname="argument services", value=services, expected_type=type_hints["services"])
            check_type(argname="argument subaccounts", value=subaccounts, expected_type=type_hints["subaccounts"])
        self._values: typing.Dict[str, typing.Any] = {}
        if calendar_period is not None:
            self._values["calendar_period"] = calendar_period
        if credit_types is not None:
            self._values["credit_types"] = credit_types
        if credit_types_treatment is not None:
            self._values["credit_types_treatment"] = credit_types_treatment
        if custom_period is not None:
            self._values["custom_period"] = custom_period
        if labels is not None:
            self._values["labels"] = labels
        if projects is not None:
            self._values["projects"] = projects
        if services is not None:
            self._values["services"] = services
        if subaccounts is not None:
            self._values["subaccounts"] = subaccounts

    @builtins.property
    def calendar_period(self) -> typing.Optional[builtins.str]:
        '''A CalendarPeriod represents the abstract concept of a recurring time period that has a canonical start.

        Grammatically, "the start of the current CalendarPeriod".
        All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8).

        Exactly one of 'calendar_period', 'custom_period' must be provided. Possible values: ["MONTH", "QUARTER", "YEAR", "CALENDAR_PERIOD_UNSPECIFIED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#calendar_period BillingBudget#calendar_period}
        '''
        result = self._values.get("calendar_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credit_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        If creditTypesTreatment is INCLUDE_SPECIFIED_CREDITS,
        this is a list of credit types to be subtracted from gross cost to determine the spend for threshold calculations. See a list of acceptable credit type values.
        If creditTypesTreatment is not INCLUDE_SPECIFIED_CREDITS, this field must be empty.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types BillingBudget#credit_types}
        '''
        result = self._values.get("credit_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def credit_types_treatment(self) -> typing.Optional[builtins.str]:
        '''Specifies how credits should be treated when determining spend for threshold calculations. Default value: "INCLUDE_ALL_CREDITS" Possible values: ["INCLUDE_ALL_CREDITS", "EXCLUDE_ALL_CREDITS", "INCLUDE_SPECIFIED_CREDITS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#credit_types_treatment BillingBudget#credit_types_treatment}
        '''
        result = self._values.get("credit_types_treatment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_period(self) -> typing.Optional["BillingBudgetBudgetFilterCustomPeriod"]:
        '''custom_period block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#custom_period BillingBudget#custom_period}
        '''
        result = self._values.get("custom_period")
        return typing.cast(typing.Optional["BillingBudgetBudgetFilterCustomPeriod"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A single label and value pair specifying that usage from only this set of labeled resources should be included in the budget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#labels BillingBudget#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def projects(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of projects of the form projects/{project_number}, specifying that usage from only this set of projects should be included in the budget.

        If omitted, the report will include
        all usage for the billing account, regardless of which project
        the usage occurred on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#projects BillingBudget#projects}
        '''
        result = self._values.get("projects")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of services of the form services/{service_id}, specifying that usage from only this set of services should be included in the budget.

        If omitted, the report will include
        usage for all the services. The service names are available
        through the Catalog API:
        https://cloud.google.com/billing/v1/how-tos/catalog-api.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#services BillingBudget#services}
        '''
        result = self._values.get("services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subaccounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of subaccounts of the form billingAccounts/{account_id}, specifying that usage from only this set of subaccounts should be included in the budget.

        If a subaccount is set to the name of
        the parent account, usage from the parent account will be included.
        If the field is omitted, the report will include usage from the parent
        account and all subaccounts, if they exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#subaccounts BillingBudget#subaccounts}
        '''
        result = self._values.get("subaccounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetBudgetFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriod",
    jsii_struct_bases=[],
    name_mapping={"start_date": "startDate", "end_date": "endDate"},
)
class BillingBudgetBudgetFilterCustomPeriod:
    def __init__(
        self,
        *,
        start_date: typing.Union["BillingBudgetBudgetFilterCustomPeriodStartDate", typing.Dict[str, typing.Any]],
        end_date: typing.Optional[typing.Union["BillingBudgetBudgetFilterCustomPeriodEndDate", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param start_date: start_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#start_date BillingBudget#start_date}
        :param end_date: end_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#end_date BillingBudget#end_date}
        '''
        if isinstance(start_date, dict):
            start_date = BillingBudgetBudgetFilterCustomPeriodStartDate(**start_date)
        if isinstance(end_date, dict):
            end_date = BillingBudgetBudgetFilterCustomPeriodEndDate(**end_date)
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriod.__init__)
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "start_date": start_date,
        }
        if end_date is not None:
            self._values["end_date"] = end_date

    @builtins.property
    def start_date(self) -> "BillingBudgetBudgetFilterCustomPeriodStartDate":
        '''start_date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#start_date BillingBudget#start_date}
        '''
        result = self._values.get("start_date")
        assert result is not None, "Required property 'start_date' is missing"
        return typing.cast("BillingBudgetBudgetFilterCustomPeriodStartDate", result)

    @builtins.property
    def end_date(
        self,
    ) -> typing.Optional["BillingBudgetBudgetFilterCustomPeriodEndDate"]:
        '''end_date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#end_date BillingBudget#end_date}
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional["BillingBudgetBudgetFilterCustomPeriodEndDate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetBudgetFilterCustomPeriod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriodEndDate",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "month": "month", "year": "year"},
)
class BillingBudgetBudgetFilterCustomPeriodEndDate:
    def __init__(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of a month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        :param month: Month of a year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        :param year: Year of the date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriodEndDate.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument year", value=year, expected_type=type_hints["year"])
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "month": month,
            "year": year,
        }

    @builtins.property
    def day(self) -> jsii.Number:
        '''Day of a month. Must be from 1 to 31 and valid for the year and month.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        '''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def month(self) -> jsii.Number:
        '''Month of a year. Must be from 1 to 12.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        '''
        result = self._values.get("month")
        assert result is not None, "Required property 'month' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def year(self) -> jsii.Number:
        '''Year of the date. Must be from 1 to 9999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        result = self._values.get("year")
        assert result is not None, "Required property 'year' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetBudgetFilterCustomPeriodEndDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="monthInput")
    def month_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthInput"))

    @builtins.property
    @jsii.member(jsii_name="yearInput")
    def year_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "yearInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "day"))

    @day.setter
    def day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "month"))

    @month.setter
    def month(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference, "month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "year"))

    @year.setter
    def year(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference, "year").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "year", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BillingBudgetBudgetFilterCustomPeriodEndDate]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilterCustomPeriodEndDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BillingBudgetBudgetFilterCustomPeriodEndDate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BillingBudgetBudgetFilterCustomPeriodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEndDate")
    def put_end_date(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of a month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        :param month: Month of a year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        :param year: Year of the date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        value = BillingBudgetBudgetFilterCustomPeriodEndDate(
            day=day, month=month, year=year
        )

        return typing.cast(None, jsii.invoke(self, "putEndDate", [value]))

    @jsii.member(jsii_name="putStartDate")
    def put_start_date(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of a month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        :param month: Month of a year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        :param year: Year of the date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        value = BillingBudgetBudgetFilterCustomPeriodStartDate(
            day=day, month=month, year=year
        )

        return typing.cast(None, jsii.invoke(self, "putStartDate", [value]))

    @jsii.member(jsii_name="resetEndDate")
    def reset_end_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndDate", []))

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference:
        return typing.cast(BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference, jsii.get(self, "endDate"))

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(
        self,
    ) -> "BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference":
        return typing.cast("BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference", jsii.get(self, "startDate"))

    @builtins.property
    @jsii.member(jsii_name="endDateInput")
    def end_date_input(
        self,
    ) -> typing.Optional[BillingBudgetBudgetFilterCustomPeriodEndDate]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilterCustomPeriodEndDate], jsii.get(self, "endDateInput"))

    @builtins.property
    @jsii.member(jsii_name="startDateInput")
    def start_date_input(
        self,
    ) -> typing.Optional["BillingBudgetBudgetFilterCustomPeriodStartDate"]:
        return typing.cast(typing.Optional["BillingBudgetBudgetFilterCustomPeriodStartDate"], jsii.get(self, "startDateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BillingBudgetBudgetFilterCustomPeriod]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilterCustomPeriod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BillingBudgetBudgetFilterCustomPeriod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriodStartDate",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "month": "month", "year": "year"},
)
class BillingBudgetBudgetFilterCustomPeriodStartDate:
    def __init__(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of a month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        :param month: Month of a year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        :param year: Year of the date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriodStartDate.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument year", value=year, expected_type=type_hints["year"])
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "month": month,
            "year": year,
        }

    @builtins.property
    def day(self) -> jsii.Number:
        '''Day of a month. Must be from 1 to 31 and valid for the year and month.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#day BillingBudget#day}
        '''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def month(self) -> jsii.Number:
        '''Month of a year. Must be from 1 to 12.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#month BillingBudget#month}
        '''
        result = self._values.get("month")
        assert result is not None, "Required property 'month' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def year(self) -> jsii.Number:
        '''Year of the date. Must be from 1 to 9999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#year BillingBudget#year}
        '''
        result = self._values.get("year")
        assert result is not None, "Required property 'year' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetBudgetFilterCustomPeriodStartDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="monthInput")
    def month_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthInput"))

    @builtins.property
    @jsii.member(jsii_name="yearInput")
    def year_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "yearInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "day"))

    @day.setter
    def day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "month"))

    @month.setter
    def month(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference, "month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "year"))

    @year.setter
    def year(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference, "year").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "year", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BillingBudgetBudgetFilterCustomPeriodStartDate]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilterCustomPeriodStartDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BillingBudgetBudgetFilterCustomPeriodStartDate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BillingBudgetBudgetFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetBudgetFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetBudgetFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomPeriod")
    def put_custom_period(
        self,
        *,
        start_date: typing.Union[BillingBudgetBudgetFilterCustomPeriodStartDate, typing.Dict[str, typing.Any]],
        end_date: typing.Optional[typing.Union[BillingBudgetBudgetFilterCustomPeriodEndDate, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param start_date: start_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#start_date BillingBudget#start_date}
        :param end_date: end_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#end_date BillingBudget#end_date}
        '''
        value = BillingBudgetBudgetFilterCustomPeriod(
            start_date=start_date, end_date=end_date
        )

        return typing.cast(None, jsii.invoke(self, "putCustomPeriod", [value]))

    @jsii.member(jsii_name="resetCalendarPeriod")
    def reset_calendar_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCalendarPeriod", []))

    @jsii.member(jsii_name="resetCreditTypes")
    def reset_credit_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreditTypes", []))

    @jsii.member(jsii_name="resetCreditTypesTreatment")
    def reset_credit_types_treatment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreditTypesTreatment", []))

    @jsii.member(jsii_name="resetCustomPeriod")
    def reset_custom_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPeriod", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProjects")
    def reset_projects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjects", []))

    @jsii.member(jsii_name="resetServices")
    def reset_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServices", []))

    @jsii.member(jsii_name="resetSubaccounts")
    def reset_subaccounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubaccounts", []))

    @builtins.property
    @jsii.member(jsii_name="customPeriod")
    def custom_period(self) -> BillingBudgetBudgetFilterCustomPeriodOutputReference:
        return typing.cast(BillingBudgetBudgetFilterCustomPeriodOutputReference, jsii.get(self, "customPeriod"))

    @builtins.property
    @jsii.member(jsii_name="calendarPeriodInput")
    def calendar_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "calendarPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="creditTypesInput")
    def credit_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "creditTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="creditTypesTreatmentInput")
    def credit_types_treatment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creditTypesTreatmentInput"))

    @builtins.property
    @jsii.member(jsii_name="customPeriodInput")
    def custom_period_input(
        self,
    ) -> typing.Optional[BillingBudgetBudgetFilterCustomPeriod]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilterCustomPeriod], jsii.get(self, "customPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectsInput")
    def projects_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "projectsInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesInput")
    def services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "servicesInput"))

    @builtins.property
    @jsii.member(jsii_name="subaccountsInput")
    def subaccounts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subaccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="calendarPeriod")
    def calendar_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "calendarPeriod"))

    @calendar_period.setter
    def calendar_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "calendar_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calendarPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="creditTypes")
    def credit_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creditTypes"))

    @credit_types.setter
    def credit_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "credit_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creditTypes", value)

    @builtins.property
    @jsii.member(jsii_name="creditTypesTreatment")
    def credit_types_treatment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creditTypesTreatment"))

    @credit_types_treatment.setter
    def credit_types_treatment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "credit_types_treatment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creditTypesTreatment", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="projects")
    def projects(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "projects"))

    @projects.setter
    def projects(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "projects").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projects", value)

    @builtins.property
    @jsii.member(jsii_name="services")
    def services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "services"))

    @services.setter
    def services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "services", value)

    @builtins.property
    @jsii.member(jsii_name="subaccounts")
    def subaccounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subaccounts"))

    @subaccounts.setter
    def subaccounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "subaccounts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subaccounts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BillingBudgetBudgetFilter]:
        return typing.cast(typing.Optional[BillingBudgetBudgetFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BillingBudgetBudgetFilter]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetBudgetFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "amount": "amount",
        "billing_account": "billingAccount",
        "all_updates_rule": "allUpdatesRule",
        "budget_filter": "budgetFilter",
        "display_name": "displayName",
        "id": "id",
        "threshold_rules": "thresholdRules",
        "timeouts": "timeouts",
    },
)
class BillingBudgetConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        amount: typing.Union[BillingBudgetAmount, typing.Dict[str, typing.Any]],
        billing_account: builtins.str,
        all_updates_rule: typing.Optional[typing.Union[BillingBudgetAllUpdatesRule, typing.Dict[str, typing.Any]]] = None,
        budget_filter: typing.Optional[typing.Union[BillingBudgetBudgetFilter, typing.Dict[str, typing.Any]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        threshold_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BillingBudgetThresholdRules", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["BillingBudgetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param amount: amount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#amount BillingBudget#amount}
        :param billing_account: ID of the billing account to set a budget on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#billing_account BillingBudget#billing_account}
        :param all_updates_rule: all_updates_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#all_updates_rule BillingBudget#all_updates_rule}
        :param budget_filter: budget_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#budget_filter BillingBudget#budget_filter}
        :param display_name: User data for display name in UI. Must be <= 60 chars. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#display_name BillingBudget#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#id BillingBudget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param threshold_rules: threshold_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#threshold_rules BillingBudget#threshold_rules}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#timeouts BillingBudget#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(amount, dict):
            amount = BillingBudgetAmount(**amount)
        if isinstance(all_updates_rule, dict):
            all_updates_rule = BillingBudgetAllUpdatesRule(**all_updates_rule)
        if isinstance(budget_filter, dict):
            budget_filter = BillingBudgetBudgetFilter(**budget_filter)
        if isinstance(timeouts, dict):
            timeouts = BillingBudgetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
            check_type(argname="argument billing_account", value=billing_account, expected_type=type_hints["billing_account"])
            check_type(argname="argument all_updates_rule", value=all_updates_rule, expected_type=type_hints["all_updates_rule"])
            check_type(argname="argument budget_filter", value=budget_filter, expected_type=type_hints["budget_filter"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument threshold_rules", value=threshold_rules, expected_type=type_hints["threshold_rules"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "amount": amount,
            "billing_account": billing_account,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if all_updates_rule is not None:
            self._values["all_updates_rule"] = all_updates_rule
        if budget_filter is not None:
            self._values["budget_filter"] = budget_filter
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if threshold_rules is not None:
            self._values["threshold_rules"] = threshold_rules
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def amount(self) -> BillingBudgetAmount:
        '''amount block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#amount BillingBudget#amount}
        '''
        result = self._values.get("amount")
        assert result is not None, "Required property 'amount' is missing"
        return typing.cast(BillingBudgetAmount, result)

    @builtins.property
    def billing_account(self) -> builtins.str:
        '''ID of the billing account to set a budget on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#billing_account BillingBudget#billing_account}
        '''
        result = self._values.get("billing_account")
        assert result is not None, "Required property 'billing_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def all_updates_rule(self) -> typing.Optional[BillingBudgetAllUpdatesRule]:
        '''all_updates_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#all_updates_rule BillingBudget#all_updates_rule}
        '''
        result = self._values.get("all_updates_rule")
        return typing.cast(typing.Optional[BillingBudgetAllUpdatesRule], result)

    @builtins.property
    def budget_filter(self) -> typing.Optional[BillingBudgetBudgetFilter]:
        '''budget_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#budget_filter BillingBudget#budget_filter}
        '''
        result = self._values.get("budget_filter")
        return typing.cast(typing.Optional[BillingBudgetBudgetFilter], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''User data for display name in UI. Must be <= 60 chars.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#display_name BillingBudget#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#id BillingBudget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BillingBudgetThresholdRules"]]]:
        '''threshold_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#threshold_rules BillingBudget#threshold_rules}
        '''
        result = self._values.get("threshold_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BillingBudgetThresholdRules"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BillingBudgetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#timeouts BillingBudget#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BillingBudgetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetThresholdRules",
    jsii_struct_bases=[],
    name_mapping={
        "threshold_percent": "thresholdPercent",
        "spend_basis": "spendBasis",
    },
)
class BillingBudgetThresholdRules:
    def __init__(
        self,
        *,
        threshold_percent: jsii.Number,
        spend_basis: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold_percent: Send an alert when this threshold is exceeded. This is a 1.0-based percentage, so 0.5 = 50%. Must be >= 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#threshold_percent BillingBudget#threshold_percent}
        :param spend_basis: The type of basis used to determine if spend has passed the threshold. Default value: "CURRENT_SPEND" Possible values: ["CURRENT_SPEND", "FORECASTED_SPEND"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#spend_basis BillingBudget#spend_basis}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetThresholdRules.__init__)
            check_type(argname="argument threshold_percent", value=threshold_percent, expected_type=type_hints["threshold_percent"])
            check_type(argname="argument spend_basis", value=spend_basis, expected_type=type_hints["spend_basis"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold_percent": threshold_percent,
        }
        if spend_basis is not None:
            self._values["spend_basis"] = spend_basis

    @builtins.property
    def threshold_percent(self) -> jsii.Number:
        '''Send an alert when this threshold is exceeded.

        This is a
        1.0-based percentage, so 0.5 = 50%. Must be >= 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#threshold_percent BillingBudget#threshold_percent}
        '''
        result = self._values.get("threshold_percent")
        assert result is not None, "Required property 'threshold_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def spend_basis(self) -> typing.Optional[builtins.str]:
        '''The type of basis used to determine if spend has passed the threshold. Default value: "CURRENT_SPEND" Possible values: ["CURRENT_SPEND", "FORECASTED_SPEND"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#spend_basis BillingBudget#spend_basis}
        '''
        result = self._values.get("spend_basis")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetThresholdRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetThresholdRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetThresholdRulesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetThresholdRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BillingBudgetThresholdRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetThresholdRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BillingBudgetThresholdRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BillingBudgetThresholdRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BillingBudgetThresholdRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BillingBudgetThresholdRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BillingBudgetThresholdRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetThresholdRulesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetThresholdRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSpendBasis")
    def reset_spend_basis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpendBasis", []))

    @builtins.property
    @jsii.member(jsii_name="spendBasisInput")
    def spend_basis_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spendBasisInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdPercentInput")
    def threshold_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="spendBasis")
    def spend_basis(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spendBasis"))

    @spend_basis.setter
    def spend_basis(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesOutputReference, "spend_basis").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spendBasis", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdPercent")
    def threshold_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdPercent"))

    @threshold_percent.setter
    def threshold_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesOutputReference, "threshold_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdPercent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BillingBudgetThresholdRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BillingBudgetThresholdRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BillingBudgetThresholdRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetThresholdRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class BillingBudgetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#create BillingBudget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#delete BillingBudget#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#update BillingBudget#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#create BillingBudget#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#delete BillingBudget#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/billing_budget#update BillingBudget#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingBudgetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BillingBudgetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.billingBudget.BillingBudgetTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BillingBudgetTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BillingBudgetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BillingBudgetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BillingBudgetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BillingBudgetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BillingBudget",
    "BillingBudgetAllUpdatesRule",
    "BillingBudgetAllUpdatesRuleOutputReference",
    "BillingBudgetAmount",
    "BillingBudgetAmountOutputReference",
    "BillingBudgetAmountSpecifiedAmount",
    "BillingBudgetAmountSpecifiedAmountOutputReference",
    "BillingBudgetBudgetFilter",
    "BillingBudgetBudgetFilterCustomPeriod",
    "BillingBudgetBudgetFilterCustomPeriodEndDate",
    "BillingBudgetBudgetFilterCustomPeriodEndDateOutputReference",
    "BillingBudgetBudgetFilterCustomPeriodOutputReference",
    "BillingBudgetBudgetFilterCustomPeriodStartDate",
    "BillingBudgetBudgetFilterCustomPeriodStartDateOutputReference",
    "BillingBudgetBudgetFilterOutputReference",
    "BillingBudgetConfig",
    "BillingBudgetThresholdRules",
    "BillingBudgetThresholdRulesList",
    "BillingBudgetThresholdRulesOutputReference",
    "BillingBudgetTimeouts",
    "BillingBudgetTimeoutsOutputReference",
]

publication.publish()
