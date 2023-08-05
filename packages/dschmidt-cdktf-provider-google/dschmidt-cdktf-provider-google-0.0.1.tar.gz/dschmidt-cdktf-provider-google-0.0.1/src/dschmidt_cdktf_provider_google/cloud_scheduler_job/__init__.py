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


class CloudSchedulerJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job google_cloud_scheduler_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        app_engine_http_target: typing.Optional[typing.Union["CloudSchedulerJobAppEngineHttpTarget", typing.Dict[str, typing.Any]]] = None,
        attempt_deadline: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudSchedulerJobHttpTarget", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        paused: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_target: typing.Optional[typing.Union["CloudSchedulerJobPubsubTarget", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        retry_config: typing.Optional[typing.Union["CloudSchedulerJobRetryConfig", typing.Dict[str, typing.Any]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudSchedulerJobTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job google_cloud_scheduler_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#name CloudSchedulerJob#name}
        :param app_engine_http_target: app_engine_http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_http_target CloudSchedulerJob#app_engine_http_target}
        :param attempt_deadline: The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: For HTTP targets, between 15 seconds and 30 minutes. For App Engine HTTP targets, between 15 seconds and 24 hours. **Note**: For PubSub targets, this field is ignored - setting it will introduce an unresolvable diff. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attempt_deadline CloudSchedulerJob#attempt_deadline}
        :param description: A human-readable description for the job. This string must not contain more than 500 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#description CloudSchedulerJob#description}
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_target CloudSchedulerJob#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#id CloudSchedulerJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param paused: Sets the job to a paused state. Jobs default to being enabled when this property is not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#paused CloudSchedulerJob#paused}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#project CloudSchedulerJob#project}.
        :param pubsub_target: pubsub_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#pubsub_target CloudSchedulerJob#pubsub_target}
        :param region: Region where the scheduler job resides. If it is not provided, Terraform will use the provider default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#region CloudSchedulerJob#region}
        :param retry_config: retry_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_config CloudSchedulerJob#retry_config}
        :param schedule: Describes the schedule on which the job will be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#schedule CloudSchedulerJob#schedule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#timeouts CloudSchedulerJob#timeouts}
        :param time_zone: Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the tz database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#time_zone CloudSchedulerJob#time_zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudSchedulerJobConfig(
            name=name,
            app_engine_http_target=app_engine_http_target,
            attempt_deadline=attempt_deadline,
            description=description,
            http_target=http_target,
            id=id,
            paused=paused,
            project=project,
            pubsub_target=pubsub_target,
            region=region,
            retry_config=retry_config,
            schedule=schedule,
            timeouts=timeouts,
            time_zone=time_zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAppEngineHttpTarget")
    def put_app_engine_http_target(
        self,
        *,
        relative_uri: builtins.str,
        app_engine_routing: typing.Optional[typing.Union["CloudSchedulerJobAppEngineHttpTargetAppEngineRouting", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param relative_uri: The relative URI. The relative URL must begin with "/" and must be a valid HTTP relative URL. It can contain a path, query string arguments, and # fragments. If the relative URL is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#relative_uri CloudSchedulerJob#relative_uri}
        :param app_engine_routing: app_engine_routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_routing CloudSchedulerJob#app_engine_routing}
        :param body: HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible HttpMethod. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        :param headers: HTTP request headers. This map contains the header field names and values. Headers can be set when the job is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        :param http_method: Which HTTP method to use for the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        '''
        value = CloudSchedulerJobAppEngineHttpTarget(
            relative_uri=relative_uri,
            app_engine_routing=app_engine_routing,
            body=body,
            headers=headers,
            http_method=http_method,
        )

        return typing.cast(None, jsii.invoke(self, "putAppEngineHttpTarget", [value]))

    @jsii.member(jsii_name="putHttpTarget")
    def put_http_target(
        self,
        *,
        uri: builtins.str,
        body: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[typing.Union["CloudSchedulerJobHttpTargetOauthToken", typing.Dict[str, typing.Any]]] = None,
        oidc_token: typing.Optional[typing.Union["CloudSchedulerJobHttpTargetOidcToken", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param uri: The full URI path that the request will be sent to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#uri CloudSchedulerJob#uri}
        :param body: HTTP request body. A request body is allowed only if the HTTP method is POST, PUT, or PATCH. It is an error to set body on a job with an incompatible HttpMethod. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        :param headers: This map contains the header field names and values. Repeated headers are not supported, but a header value can contain commas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        :param http_method: Which HTTP method to use for the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        :param oauth_token: oauth_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oauth_token CloudSchedulerJob#oauth_token}
        :param oidc_token: oidc_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oidc_token CloudSchedulerJob#oidc_token}
        '''
        value = CloudSchedulerJobHttpTarget(
            uri=uri,
            body=body,
            headers=headers,
            http_method=http_method,
            oauth_token=oauth_token,
            oidc_token=oidc_token,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpTarget", [value]))

    @jsii.member(jsii_name="putPubsubTarget")
    def put_pubsub_target(
        self,
        *,
        topic_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param topic_name: The full resource name for the Cloud Pub/Sub topic to which messages will be published when a job is delivered. ~>**NOTE:** The topic name must be in the same format as required by PubSub's PublishRequest.name, e.g. 'projects/my-project/topics/my-topic'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#topic_name CloudSchedulerJob#topic_name}
        :param attributes: Attributes for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attributes CloudSchedulerJob#attributes}
        :param data: The message payload for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#data CloudSchedulerJob#data}
        '''
        value = CloudSchedulerJobPubsubTarget(
            topic_name=topic_name, attributes=attributes, data=data
        )

        return typing.cast(None, jsii.invoke(self, "putPubsubTarget", [value]))

    @jsii.member(jsii_name="putRetryConfig")
    def put_retry_config(
        self,
        *,
        max_backoff_duration: typing.Optional[builtins.str] = None,
        max_doublings: typing.Optional[jsii.Number] = None,
        max_retry_duration: typing.Optional[builtins.str] = None,
        min_backoff_duration: typing.Optional[builtins.str] = None,
        retry_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_backoff_duration: The maximum amount of time to wait before retrying a job after it fails. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_backoff_duration CloudSchedulerJob#max_backoff_duration}
        :param max_doublings: The time between retries will double maxDoublings times. A job's retry interval starts at minBackoffDuration, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoffDuration up to retryCount times. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_doublings CloudSchedulerJob#max_doublings}
        :param max_retry_duration: The time limit for retrying a failed job, measured from time when an execution was first attempted. If specified with retryCount, the job will be retried until both limits are reached. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_retry_duration CloudSchedulerJob#max_retry_duration}
        :param min_backoff_duration: The minimum amount of time to wait before retrying a job after it fails. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#min_backoff_duration CloudSchedulerJob#min_backoff_duration}
        :param retry_count: The number of attempts that the system will make to run a job using the exponential backoff procedure described by maxDoublings. Values greater than 5 and negative values are not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_count CloudSchedulerJob#retry_count}
        '''
        value = CloudSchedulerJobRetryConfig(
            max_backoff_duration=max_backoff_duration,
            max_doublings=max_doublings,
            max_retry_duration=max_retry_duration,
            min_backoff_duration=min_backoff_duration,
            retry_count=retry_count,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#create CloudSchedulerJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#delete CloudSchedulerJob#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#update CloudSchedulerJob#update}.
        '''
        value = CloudSchedulerJobTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAppEngineHttpTarget")
    def reset_app_engine_http_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppEngineHttpTarget", []))

    @jsii.member(jsii_name="resetAttemptDeadline")
    def reset_attempt_deadline(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttemptDeadline", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHttpTarget")
    def reset_http_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTarget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPaused")
    def reset_paused(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaused", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPubsubTarget")
    def reset_pubsub_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubsubTarget", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRetryConfig")
    def reset_retry_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConfig", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="appEngineHttpTarget")
    def app_engine_http_target(
        self,
    ) -> "CloudSchedulerJobAppEngineHttpTargetOutputReference":
        return typing.cast("CloudSchedulerJobAppEngineHttpTargetOutputReference", jsii.get(self, "appEngineHttpTarget"))

    @builtins.property
    @jsii.member(jsii_name="httpTarget")
    def http_target(self) -> "CloudSchedulerJobHttpTargetOutputReference":
        return typing.cast("CloudSchedulerJobHttpTargetOutputReference", jsii.get(self, "httpTarget"))

    @builtins.property
    @jsii.member(jsii_name="pubsubTarget")
    def pubsub_target(self) -> "CloudSchedulerJobPubsubTargetOutputReference":
        return typing.cast("CloudSchedulerJobPubsubTargetOutputReference", jsii.get(self, "pubsubTarget"))

    @builtins.property
    @jsii.member(jsii_name="retryConfig")
    def retry_config(self) -> "CloudSchedulerJobRetryConfigOutputReference":
        return typing.cast("CloudSchedulerJobRetryConfigOutputReference", jsii.get(self, "retryConfig"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CloudSchedulerJobTimeoutsOutputReference":
        return typing.cast("CloudSchedulerJobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appEngineHttpTargetInput")
    def app_engine_http_target_input(
        self,
    ) -> typing.Optional["CloudSchedulerJobAppEngineHttpTarget"]:
        return typing.cast(typing.Optional["CloudSchedulerJobAppEngineHttpTarget"], jsii.get(self, "appEngineHttpTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="attemptDeadlineInput")
    def attempt_deadline_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attemptDeadlineInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTargetInput")
    def http_target_input(self) -> typing.Optional["CloudSchedulerJobHttpTarget"]:
        return typing.cast(typing.Optional["CloudSchedulerJobHttpTarget"], jsii.get(self, "httpTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pausedInput")
    def paused_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pausedInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pubsubTargetInput")
    def pubsub_target_input(self) -> typing.Optional["CloudSchedulerJobPubsubTarget"]:
        return typing.cast(typing.Optional["CloudSchedulerJobPubsubTarget"], jsii.get(self, "pubsubTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConfigInput")
    def retry_config_input(self) -> typing.Optional["CloudSchedulerJobRetryConfig"]:
        return typing.cast(typing.Optional["CloudSchedulerJobRetryConfig"], jsii.get(self, "retryConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CloudSchedulerJobTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CloudSchedulerJobTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="attemptDeadline")
    def attempt_deadline(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attemptDeadline"))

    @attempt_deadline.setter
    def attempt_deadline(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "attempt_deadline").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attemptDeadline", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="paused")
    def paused(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "paused"))

    @paused.setter
    def paused(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "paused").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paused", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJob, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobAppEngineHttpTarget",
    jsii_struct_bases=[],
    name_mapping={
        "relative_uri": "relativeUri",
        "app_engine_routing": "appEngineRouting",
        "body": "body",
        "headers": "headers",
        "http_method": "httpMethod",
    },
)
class CloudSchedulerJobAppEngineHttpTarget:
    def __init__(
        self,
        *,
        relative_uri: builtins.str,
        app_engine_routing: typing.Optional[typing.Union["CloudSchedulerJobAppEngineHttpTargetAppEngineRouting", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param relative_uri: The relative URI. The relative URL must begin with "/" and must be a valid HTTP relative URL. It can contain a path, query string arguments, and # fragments. If the relative URL is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#relative_uri CloudSchedulerJob#relative_uri}
        :param app_engine_routing: app_engine_routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_routing CloudSchedulerJob#app_engine_routing}
        :param body: HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible HttpMethod. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        :param headers: HTTP request headers. This map contains the header field names and values. Headers can be set when the job is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        :param http_method: Which HTTP method to use for the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        '''
        if isinstance(app_engine_routing, dict):
            app_engine_routing = CloudSchedulerJobAppEngineHttpTargetAppEngineRouting(**app_engine_routing)
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobAppEngineHttpTarget.__init__)
            check_type(argname="argument relative_uri", value=relative_uri, expected_type=type_hints["relative_uri"])
            check_type(argname="argument app_engine_routing", value=app_engine_routing, expected_type=type_hints["app_engine_routing"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
        self._values: typing.Dict[str, typing.Any] = {
            "relative_uri": relative_uri,
        }
        if app_engine_routing is not None:
            self._values["app_engine_routing"] = app_engine_routing
        if body is not None:
            self._values["body"] = body
        if headers is not None:
            self._values["headers"] = headers
        if http_method is not None:
            self._values["http_method"] = http_method

    @builtins.property
    def relative_uri(self) -> builtins.str:
        '''The relative URI.

        The relative URL must begin with "/" and must be a valid HTTP relative URL.
        It can contain a path, query string arguments, and # fragments.
        If the relative URL is empty, then the root path "/" will be used.
        No spaces are allowed, and the maximum length allowed is 2083 characters

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#relative_uri CloudSchedulerJob#relative_uri}
        '''
        result = self._values.get("relative_uri")
        assert result is not None, "Required property 'relative_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_engine_routing(
        self,
    ) -> typing.Optional["CloudSchedulerJobAppEngineHttpTargetAppEngineRouting"]:
        '''app_engine_routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_routing CloudSchedulerJob#app_engine_routing}
        '''
        result = self._values.get("app_engine_routing")
        return typing.cast(typing.Optional["CloudSchedulerJobAppEngineHttpTargetAppEngineRouting"], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''HTTP request body.

        A request body is allowed only if the HTTP method is POST or PUT.
        It will result in invalid argument error to set a body on a job with an incompatible HttpMethod.

        A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''HTTP request headers.

        This map contains the header field names and values.
        Headers can be set when the job is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''Which HTTP method to use for the request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobAppEngineHttpTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobAppEngineHttpTargetAppEngineRouting",
    jsii_struct_bases=[],
    name_mapping={"instance": "instance", "service": "service", "version": "version"},
)
class CloudSchedulerJobAppEngineHttpTargetAppEngineRouting:
    def __init__(
        self,
        *,
        instance: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance: App instance. By default, the job is sent to an instance which is available when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#instance CloudSchedulerJob#instance}
        :param service: App service. By default, the job is sent to the service which is the default service when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service CloudSchedulerJob#service}
        :param version: App version. By default, the job is sent to the version which is the default version when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#version CloudSchedulerJob#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobAppEngineHttpTargetAppEngineRouting.__init__)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance is not None:
            self._values["instance"] = instance
        if service is not None:
            self._values["service"] = service
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def instance(self) -> typing.Optional[builtins.str]:
        '''App instance. By default, the job is sent to an instance which is available when the job is attempted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#instance CloudSchedulerJob#instance}
        '''
        result = self._values.get("instance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''App service.

        By default, the job is sent to the service which is the default service when the job is attempted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service CloudSchedulerJob#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''App version.

        By default, the job is sent to the version which is the default version when the job is attempted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#version CloudSchedulerJob#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobAppEngineHttpTargetAppEngineRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstance")
    def reset_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstance", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="instanceInput")
    def instance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @instance.setter
    def instance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference, "instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instance", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudSchedulerJobAppEngineHttpTargetAppEngineRouting]:
        return typing.cast(typing.Optional[CloudSchedulerJobAppEngineHttpTargetAppEngineRouting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobAppEngineHttpTargetAppEngineRouting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudSchedulerJobAppEngineHttpTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobAppEngineHttpTargetOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobAppEngineHttpTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAppEngineRouting")
    def put_app_engine_routing(
        self,
        *,
        instance: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance: App instance. By default, the job is sent to an instance which is available when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#instance CloudSchedulerJob#instance}
        :param service: App service. By default, the job is sent to the service which is the default service when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service CloudSchedulerJob#service}
        :param version: App version. By default, the job is sent to the version which is the default version when the job is attempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#version CloudSchedulerJob#version}
        '''
        value = CloudSchedulerJobAppEngineHttpTargetAppEngineRouting(
            instance=instance, service=service, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putAppEngineRouting", [value]))

    @jsii.member(jsii_name="resetAppEngineRouting")
    def reset_app_engine_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppEngineRouting", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @builtins.property
    @jsii.member(jsii_name="appEngineRouting")
    def app_engine_routing(
        self,
    ) -> CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference:
        return typing.cast(CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference, jsii.get(self, "appEngineRouting"))

    @builtins.property
    @jsii.member(jsii_name="appEngineRoutingInput")
    def app_engine_routing_input(
        self,
    ) -> typing.Optional[CloudSchedulerJobAppEngineHttpTargetAppEngineRouting]:
        return typing.cast(typing.Optional[CloudSchedulerJobAppEngineHttpTargetAppEngineRouting], jsii.get(self, "appEngineRoutingInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeUriInput")
    def relative_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeUriInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetOutputReference, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="relativeUri")
    def relative_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeUri"))

    @relative_uri.setter
    def relative_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetOutputReference, "relative_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobAppEngineHttpTarget]:
        return typing.cast(typing.Optional[CloudSchedulerJobAppEngineHttpTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobAppEngineHttpTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobAppEngineHttpTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "app_engine_http_target": "appEngineHttpTarget",
        "attempt_deadline": "attemptDeadline",
        "description": "description",
        "http_target": "httpTarget",
        "id": "id",
        "paused": "paused",
        "project": "project",
        "pubsub_target": "pubsubTarget",
        "region": "region",
        "retry_config": "retryConfig",
        "schedule": "schedule",
        "timeouts": "timeouts",
        "time_zone": "timeZone",
    },
)
class CloudSchedulerJobConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        app_engine_http_target: typing.Optional[typing.Union[CloudSchedulerJobAppEngineHttpTarget, typing.Dict[str, typing.Any]]] = None,
        attempt_deadline: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudSchedulerJobHttpTarget", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        paused: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_target: typing.Optional[typing.Union["CloudSchedulerJobPubsubTarget", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        retry_config: typing.Optional[typing.Union["CloudSchedulerJobRetryConfig", typing.Dict[str, typing.Any]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudSchedulerJobTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#name CloudSchedulerJob#name}
        :param app_engine_http_target: app_engine_http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_http_target CloudSchedulerJob#app_engine_http_target}
        :param attempt_deadline: The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: For HTTP targets, between 15 seconds and 30 minutes. For App Engine HTTP targets, between 15 seconds and 24 hours. **Note**: For PubSub targets, this field is ignored - setting it will introduce an unresolvable diff. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attempt_deadline CloudSchedulerJob#attempt_deadline}
        :param description: A human-readable description for the job. This string must not contain more than 500 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#description CloudSchedulerJob#description}
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_target CloudSchedulerJob#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#id CloudSchedulerJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param paused: Sets the job to a paused state. Jobs default to being enabled when this property is not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#paused CloudSchedulerJob#paused}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#project CloudSchedulerJob#project}.
        :param pubsub_target: pubsub_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#pubsub_target CloudSchedulerJob#pubsub_target}
        :param region: Region where the scheduler job resides. If it is not provided, Terraform will use the provider default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#region CloudSchedulerJob#region}
        :param retry_config: retry_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_config CloudSchedulerJob#retry_config}
        :param schedule: Describes the schedule on which the job will be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#schedule CloudSchedulerJob#schedule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#timeouts CloudSchedulerJob#timeouts}
        :param time_zone: Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the tz database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#time_zone CloudSchedulerJob#time_zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(app_engine_http_target, dict):
            app_engine_http_target = CloudSchedulerJobAppEngineHttpTarget(**app_engine_http_target)
        if isinstance(http_target, dict):
            http_target = CloudSchedulerJobHttpTarget(**http_target)
        if isinstance(pubsub_target, dict):
            pubsub_target = CloudSchedulerJobPubsubTarget(**pubsub_target)
        if isinstance(retry_config, dict):
            retry_config = CloudSchedulerJobRetryConfig(**retry_config)
        if isinstance(timeouts, dict):
            timeouts = CloudSchedulerJobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument app_engine_http_target", value=app_engine_http_target, expected_type=type_hints["app_engine_http_target"])
            check_type(argname="argument attempt_deadline", value=attempt_deadline, expected_type=type_hints["attempt_deadline"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument http_target", value=http_target, expected_type=type_hints["http_target"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument paused", value=paused, expected_type=type_hints["paused"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument pubsub_target", value=pubsub_target, expected_type=type_hints["pubsub_target"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument retry_config", value=retry_config, expected_type=type_hints["retry_config"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if app_engine_http_target is not None:
            self._values["app_engine_http_target"] = app_engine_http_target
        if attempt_deadline is not None:
            self._values["attempt_deadline"] = attempt_deadline
        if description is not None:
            self._values["description"] = description
        if http_target is not None:
            self._values["http_target"] = http_target
        if id is not None:
            self._values["id"] = id
        if paused is not None:
            self._values["paused"] = paused
        if project is not None:
            self._values["project"] = project
        if pubsub_target is not None:
            self._values["pubsub_target"] = pubsub_target
        if region is not None:
            self._values["region"] = region
        if retry_config is not None:
            self._values["retry_config"] = retry_config
        if schedule is not None:
            self._values["schedule"] = schedule
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if time_zone is not None:
            self._values["time_zone"] = time_zone

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
    def name(self) -> builtins.str:
        '''The name of the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#name CloudSchedulerJob#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_engine_http_target(
        self,
    ) -> typing.Optional[CloudSchedulerJobAppEngineHttpTarget]:
        '''app_engine_http_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#app_engine_http_target CloudSchedulerJob#app_engine_http_target}
        '''
        result = self._values.get("app_engine_http_target")
        return typing.cast(typing.Optional[CloudSchedulerJobAppEngineHttpTarget], result)

    @builtins.property
    def attempt_deadline(self) -> typing.Optional[builtins.str]:
        '''The deadline for job attempts.

        If the request handler does not respond by this deadline then the request is
        cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
        execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
        The allowed duration for this deadline is:
        For HTTP targets, between 15 seconds and 30 minutes.
        For App Engine HTTP targets, between 15 seconds and 24 hours.
        **Note**: For PubSub targets, this field is ignored - setting it will introduce an unresolvable diff.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attempt_deadline CloudSchedulerJob#attempt_deadline}
        '''
        result = self._values.get("attempt_deadline")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the job.  This string must not contain more than 500 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#description CloudSchedulerJob#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_target(self) -> typing.Optional["CloudSchedulerJobHttpTarget"]:
        '''http_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_target CloudSchedulerJob#http_target}
        '''
        result = self._values.get("http_target")
        return typing.cast(typing.Optional["CloudSchedulerJobHttpTarget"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#id CloudSchedulerJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paused(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Sets the job to a paused state. Jobs default to being enabled when this property is not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#paused CloudSchedulerJob#paused}
        '''
        result = self._values.get("paused")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#project CloudSchedulerJob#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pubsub_target(self) -> typing.Optional["CloudSchedulerJobPubsubTarget"]:
        '''pubsub_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#pubsub_target CloudSchedulerJob#pubsub_target}
        '''
        result = self._values.get("pubsub_target")
        return typing.cast(typing.Optional["CloudSchedulerJobPubsubTarget"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the scheduler job resides. If it is not provided, Terraform will use the provider default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#region CloudSchedulerJob#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_config(self) -> typing.Optional["CloudSchedulerJobRetryConfig"]:
        '''retry_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_config CloudSchedulerJob#retry_config}
        '''
        result = self._values.get("retry_config")
        return typing.cast(typing.Optional["CloudSchedulerJobRetryConfig"], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Describes the schedule on which the job will be executed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#schedule CloudSchedulerJob#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CloudSchedulerJobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#timeouts CloudSchedulerJob#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CloudSchedulerJobTimeouts"], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Specifies the time zone to be used in interpreting schedule.

        The value of this field must be a time zone name from the tz database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#time_zone CloudSchedulerJob#time_zone}
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTarget",
    jsii_struct_bases=[],
    name_mapping={
        "uri": "uri",
        "body": "body",
        "headers": "headers",
        "http_method": "httpMethod",
        "oauth_token": "oauthToken",
        "oidc_token": "oidcToken",
    },
)
class CloudSchedulerJobHttpTarget:
    def __init__(
        self,
        *,
        uri: builtins.str,
        body: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[typing.Union["CloudSchedulerJobHttpTargetOauthToken", typing.Dict[str, typing.Any]]] = None,
        oidc_token: typing.Optional[typing.Union["CloudSchedulerJobHttpTargetOidcToken", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param uri: The full URI path that the request will be sent to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#uri CloudSchedulerJob#uri}
        :param body: HTTP request body. A request body is allowed only if the HTTP method is POST, PUT, or PATCH. It is an error to set body on a job with an incompatible HttpMethod. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        :param headers: This map contains the header field names and values. Repeated headers are not supported, but a header value can contain commas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        :param http_method: Which HTTP method to use for the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        :param oauth_token: oauth_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oauth_token CloudSchedulerJob#oauth_token}
        :param oidc_token: oidc_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oidc_token CloudSchedulerJob#oidc_token}
        '''
        if isinstance(oauth_token, dict):
            oauth_token = CloudSchedulerJobHttpTargetOauthToken(**oauth_token)
        if isinstance(oidc_token, dict):
            oidc_token = CloudSchedulerJobHttpTargetOidcToken(**oidc_token)
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTarget.__init__)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument oauth_token", value=oauth_token, expected_type=type_hints["oauth_token"])
            check_type(argname="argument oidc_token", value=oidc_token, expected_type=type_hints["oidc_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }
        if body is not None:
            self._values["body"] = body
        if headers is not None:
            self._values["headers"] = headers
        if http_method is not None:
            self._values["http_method"] = http_method
        if oauth_token is not None:
            self._values["oauth_token"] = oauth_token
        if oidc_token is not None:
            self._values["oidc_token"] = oidc_token

    @builtins.property
    def uri(self) -> builtins.str:
        '''The full URI path that the request will be sent to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#uri CloudSchedulerJob#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''HTTP request body.

        A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
        It is an error to set body on a job with an incompatible HttpMethod.

        A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#body CloudSchedulerJob#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''This map contains the header field names and values.

        Repeated headers are not supported, but a header value can contain commas.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#headers CloudSchedulerJob#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''Which HTTP method to use for the request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#http_method CloudSchedulerJob#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_token(self) -> typing.Optional["CloudSchedulerJobHttpTargetOauthToken"]:
        '''oauth_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oauth_token CloudSchedulerJob#oauth_token}
        '''
        result = self._values.get("oauth_token")
        return typing.cast(typing.Optional["CloudSchedulerJobHttpTargetOauthToken"], result)

    @builtins.property
    def oidc_token(self) -> typing.Optional["CloudSchedulerJobHttpTargetOidcToken"]:
        '''oidc_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#oidc_token CloudSchedulerJob#oidc_token}
        '''
        result = self._values.get("oidc_token")
        return typing.cast(typing.Optional["CloudSchedulerJobHttpTargetOidcToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobHttpTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTargetOauthToken",
    jsii_struct_bases=[],
    name_mapping={"service_account_email": "serviceAccountEmail", "scope": "scope"},
)
class CloudSchedulerJobHttpTargetOauthToken:
    def __init__(
        self,
        *,
        service_account_email: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating OAuth token. The service account must be within the same project as the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        :param scope: OAuth scope to be used for generating OAuth access token. If not specified, "https://www.googleapis.com/auth/cloud-platform" will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#scope CloudSchedulerJob#scope}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTargetOauthToken.__init__)
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_account_email": service_account_email,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def service_account_email(self) -> builtins.str:
        '''Service account email to be used for generating OAuth token.

        The service account must be within the same project as the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        '''
        result = self._values.get("service_account_email")
        assert result is not None, "Required property 'service_account_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''OAuth scope to be used for generating OAuth access token. If not specified, "https://www.googleapis.com/auth/cloud-platform" will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#scope CloudSchedulerJob#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobHttpTargetOauthToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobHttpTargetOauthTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTargetOauthTokenOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTargetOauthTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOauthTokenOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOauthTokenOutputReference, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobHttpTargetOauthToken]:
        return typing.cast(typing.Optional[CloudSchedulerJobHttpTargetOauthToken], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobHttpTargetOauthToken],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOauthTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTargetOidcToken",
    jsii_struct_bases=[],
    name_mapping={
        "service_account_email": "serviceAccountEmail",
        "audience": "audience",
    },
)
class CloudSchedulerJobHttpTargetOidcToken:
    def __init__(
        self,
        *,
        service_account_email: builtins.str,
        audience: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating OAuth token. The service account must be within the same project as the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        :param audience: Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#audience CloudSchedulerJob#audience}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTargetOidcToken.__init__)
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
            check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_account_email": service_account_email,
        }
        if audience is not None:
            self._values["audience"] = audience

    @builtins.property
    def service_account_email(self) -> builtins.str:
        '''Service account email to be used for generating OAuth token.

        The service account must be within the same project as the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        '''
        result = self._values.get("service_account_email")
        assert result is not None, "Required property 'service_account_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audience(self) -> typing.Optional[builtins.str]:
        '''Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#audience CloudSchedulerJob#audience}
        '''
        result = self._values.get("audience")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobHttpTargetOidcToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobHttpTargetOidcTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTargetOidcTokenOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTargetOidcTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudience")
    def reset_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudience", []))

    @builtins.property
    @jsii.member(jsii_name="audienceInput")
    def audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audienceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="audience")
    def audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audience"))

    @audience.setter
    def audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOidcTokenOutputReference, "audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audience", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOidcTokenOutputReference, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobHttpTargetOidcToken]:
        return typing.cast(typing.Optional[CloudSchedulerJobHttpTargetOidcToken], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobHttpTargetOidcToken],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOidcTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudSchedulerJobHttpTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobHttpTargetOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobHttpTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthToken")
    def put_oauth_token(
        self,
        *,
        service_account_email: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating OAuth token. The service account must be within the same project as the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        :param scope: OAuth scope to be used for generating OAuth access token. If not specified, "https://www.googleapis.com/auth/cloud-platform" will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#scope CloudSchedulerJob#scope}
        '''
        value = CloudSchedulerJobHttpTargetOauthToken(
            service_account_email=service_account_email, scope=scope
        )

        return typing.cast(None, jsii.invoke(self, "putOauthToken", [value]))

    @jsii.member(jsii_name="putOidcToken")
    def put_oidc_token(
        self,
        *,
        service_account_email: builtins.str,
        audience: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating OAuth token. The service account must be within the same project as the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#service_account_email CloudSchedulerJob#service_account_email}
        :param audience: Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#audience CloudSchedulerJob#audience}
        '''
        value = CloudSchedulerJobHttpTargetOidcToken(
            service_account_email=service_account_email, audience=audience
        )

        return typing.cast(None, jsii.invoke(self, "putOidcToken", [value]))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetOauthToken")
    def reset_oauth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthToken", []))

    @jsii.member(jsii_name="resetOidcToken")
    def reset_oidc_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthToken")
    def oauth_token(self) -> CloudSchedulerJobHttpTargetOauthTokenOutputReference:
        return typing.cast(CloudSchedulerJobHttpTargetOauthTokenOutputReference, jsii.get(self, "oauthToken"))

    @builtins.property
    @jsii.member(jsii_name="oidcToken")
    def oidc_token(self) -> CloudSchedulerJobHttpTargetOidcTokenOutputReference:
        return typing.cast(CloudSchedulerJobHttpTargetOidcTokenOutputReference, jsii.get(self, "oidcToken"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenInput")
    def oauth_token_input(
        self,
    ) -> typing.Optional[CloudSchedulerJobHttpTargetOauthToken]:
        return typing.cast(typing.Optional[CloudSchedulerJobHttpTargetOauthToken], jsii.get(self, "oauthTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcTokenInput")
    def oidc_token_input(self) -> typing.Optional[CloudSchedulerJobHttpTargetOidcToken]:
        return typing.cast(typing.Optional[CloudSchedulerJobHttpTargetOidcToken], jsii.get(self, "oidcTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOutputReference, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobHttpTarget]:
        return typing.cast(typing.Optional[CloudSchedulerJobHttpTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobHttpTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobHttpTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobPubsubTarget",
    jsii_struct_bases=[],
    name_mapping={
        "topic_name": "topicName",
        "attributes": "attributes",
        "data": "data",
    },
)
class CloudSchedulerJobPubsubTarget:
    def __init__(
        self,
        *,
        topic_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param topic_name: The full resource name for the Cloud Pub/Sub topic to which messages will be published when a job is delivered. ~>**NOTE:** The topic name must be in the same format as required by PubSub's PublishRequest.name, e.g. 'projects/my-project/topics/my-topic'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#topic_name CloudSchedulerJob#topic_name}
        :param attributes: Attributes for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attributes CloudSchedulerJob#attributes}
        :param data: The message payload for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#data CloudSchedulerJob#data}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobPubsubTarget.__init__)
            check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        self._values: typing.Dict[str, typing.Any] = {
            "topic_name": topic_name,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if data is not None:
            self._values["data"] = data

    @builtins.property
    def topic_name(self) -> builtins.str:
        '''The full resource name for the Cloud Pub/Sub topic to which messages will be published when a job is delivered.

        ~>**NOTE:**
        The topic name must be in the same format as required by PubSub's
        PublishRequest.name, e.g. 'projects/my-project/topics/my-topic'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#topic_name CloudSchedulerJob#topic_name}
        '''
        result = self._values.get("topic_name")
        assert result is not None, "Required property 'topic_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Attributes for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#attributes CloudSchedulerJob#attributes}
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''The message payload for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute.

        A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#data CloudSchedulerJob#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobPubsubTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobPubsubTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobPubsubTargetOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobPubsubTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="topicNameInput")
    def topic_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobPubsubTargetOutputReference, "attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobPubsubTargetOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topicName"))

    @topic_name.setter
    def topic_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobPubsubTargetOutputReference, "topic_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobPubsubTarget]:
        return typing.cast(typing.Optional[CloudSchedulerJobPubsubTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobPubsubTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobPubsubTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobRetryConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_backoff_duration": "maxBackoffDuration",
        "max_doublings": "maxDoublings",
        "max_retry_duration": "maxRetryDuration",
        "min_backoff_duration": "minBackoffDuration",
        "retry_count": "retryCount",
    },
)
class CloudSchedulerJobRetryConfig:
    def __init__(
        self,
        *,
        max_backoff_duration: typing.Optional[builtins.str] = None,
        max_doublings: typing.Optional[jsii.Number] = None,
        max_retry_duration: typing.Optional[builtins.str] = None,
        min_backoff_duration: typing.Optional[builtins.str] = None,
        retry_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_backoff_duration: The maximum amount of time to wait before retrying a job after it fails. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_backoff_duration CloudSchedulerJob#max_backoff_duration}
        :param max_doublings: The time between retries will double maxDoublings times. A job's retry interval starts at minBackoffDuration, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoffDuration up to retryCount times. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_doublings CloudSchedulerJob#max_doublings}
        :param max_retry_duration: The time limit for retrying a failed job, measured from time when an execution was first attempted. If specified with retryCount, the job will be retried until both limits are reached. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_retry_duration CloudSchedulerJob#max_retry_duration}
        :param min_backoff_duration: The minimum amount of time to wait before retrying a job after it fails. A duration in seconds with up to nine fractional digits, terminated by 's'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#min_backoff_duration CloudSchedulerJob#min_backoff_duration}
        :param retry_count: The number of attempts that the system will make to run a job using the exponential backoff procedure described by maxDoublings. Values greater than 5 and negative values are not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_count CloudSchedulerJob#retry_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobRetryConfig.__init__)
            check_type(argname="argument max_backoff_duration", value=max_backoff_duration, expected_type=type_hints["max_backoff_duration"])
            check_type(argname="argument max_doublings", value=max_doublings, expected_type=type_hints["max_doublings"])
            check_type(argname="argument max_retry_duration", value=max_retry_duration, expected_type=type_hints["max_retry_duration"])
            check_type(argname="argument min_backoff_duration", value=min_backoff_duration, expected_type=type_hints["min_backoff_duration"])
            check_type(argname="argument retry_count", value=retry_count, expected_type=type_hints["retry_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_backoff_duration is not None:
            self._values["max_backoff_duration"] = max_backoff_duration
        if max_doublings is not None:
            self._values["max_doublings"] = max_doublings
        if max_retry_duration is not None:
            self._values["max_retry_duration"] = max_retry_duration
        if min_backoff_duration is not None:
            self._values["min_backoff_duration"] = min_backoff_duration
        if retry_count is not None:
            self._values["retry_count"] = retry_count

    @builtins.property
    def max_backoff_duration(self) -> typing.Optional[builtins.str]:
        '''The maximum amount of time to wait before retrying a job after it fails.

        A duration in seconds with up to nine fractional digits, terminated by 's'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_backoff_duration CloudSchedulerJob#max_backoff_duration}
        '''
        result = self._values.get("max_backoff_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_doublings(self) -> typing.Optional[jsii.Number]:
        '''The time between retries will double maxDoublings times.

        A job's retry interval starts at minBackoffDuration,
        then doubles maxDoublings times, then increases linearly,
        and finally retries retries at intervals of maxBackoffDuration up to retryCount times.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_doublings CloudSchedulerJob#max_doublings}
        '''
        result = self._values.get("max_doublings")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retry_duration(self) -> typing.Optional[builtins.str]:
        '''The time limit for retrying a failed job, measured from time when an execution was first attempted.

        If specified with retryCount, the job will be retried until both limits are reached.
        A duration in seconds with up to nine fractional digits, terminated by 's'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#max_retry_duration CloudSchedulerJob#max_retry_duration}
        '''
        result = self._values.get("max_retry_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_backoff_duration(self) -> typing.Optional[builtins.str]:
        '''The minimum amount of time to wait before retrying a job after it fails.

        A duration in seconds with up to nine fractional digits, terminated by 's'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#min_backoff_duration CloudSchedulerJob#min_backoff_duration}
        '''
        result = self._values.get("min_backoff_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_count(self) -> typing.Optional[jsii.Number]:
        '''The number of attempts that the system will make to run a  job using the exponential backoff procedure described by maxDoublings.

        Values greater than 5 and negative values are not allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#retry_count CloudSchedulerJob#retry_count}
        '''
        result = self._values.get("retry_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobRetryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobRetryConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobRetryConfigOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobRetryConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxBackoffDuration")
    def reset_max_backoff_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBackoffDuration", []))

    @jsii.member(jsii_name="resetMaxDoublings")
    def reset_max_doublings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDoublings", []))

    @jsii.member(jsii_name="resetMaxRetryDuration")
    def reset_max_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetryDuration", []))

    @jsii.member(jsii_name="resetMinBackoffDuration")
    def reset_min_backoff_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinBackoffDuration", []))

    @jsii.member(jsii_name="resetRetryCount")
    def reset_retry_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryCount", []))

    @builtins.property
    @jsii.member(jsii_name="maxBackoffDurationInput")
    def max_backoff_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxBackoffDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDoublingsInput")
    def max_doublings_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDoublingsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetryDurationInput")
    def max_retry_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxRetryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="minBackoffDurationInput")
    def min_backoff_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minBackoffDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryCountInput")
    def retry_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBackoffDuration")
    def max_backoff_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxBackoffDuration"))

    @max_backoff_duration.setter
    def max_backoff_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "max_backoff_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBackoffDuration", value)

    @builtins.property
    @jsii.member(jsii_name="maxDoublings")
    def max_doublings(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDoublings"))

    @max_doublings.setter
    def max_doublings(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "max_doublings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDoublings", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetryDuration")
    def max_retry_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxRetryDuration"))

    @max_retry_duration.setter
    def max_retry_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "max_retry_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="minBackoffDuration")
    def min_backoff_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minBackoffDuration"))

    @min_backoff_duration.setter
    def min_backoff_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "min_backoff_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minBackoffDuration", value)

    @builtins.property
    @jsii.member(jsii_name="retryCount")
    def retry_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryCount"))

    @retry_count.setter
    def retry_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "retry_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudSchedulerJobRetryConfig]:
        return typing.cast(typing.Optional[CloudSchedulerJobRetryConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudSchedulerJobRetryConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobRetryConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class CloudSchedulerJobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#create CloudSchedulerJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#delete CloudSchedulerJob#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#update CloudSchedulerJob#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudSchedulerJobTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#create CloudSchedulerJob#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#delete CloudSchedulerJob#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/cloud_scheduler_job#update CloudSchedulerJob#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudSchedulerJobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudSchedulerJobTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.cloudSchedulerJob.CloudSchedulerJobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CloudSchedulerJobTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudSchedulerJobTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudSchedulerJobTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudSchedulerJobTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudSchedulerJobTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudSchedulerJob",
    "CloudSchedulerJobAppEngineHttpTarget",
    "CloudSchedulerJobAppEngineHttpTargetAppEngineRouting",
    "CloudSchedulerJobAppEngineHttpTargetAppEngineRoutingOutputReference",
    "CloudSchedulerJobAppEngineHttpTargetOutputReference",
    "CloudSchedulerJobConfig",
    "CloudSchedulerJobHttpTarget",
    "CloudSchedulerJobHttpTargetOauthToken",
    "CloudSchedulerJobHttpTargetOauthTokenOutputReference",
    "CloudSchedulerJobHttpTargetOidcToken",
    "CloudSchedulerJobHttpTargetOidcTokenOutputReference",
    "CloudSchedulerJobHttpTargetOutputReference",
    "CloudSchedulerJobPubsubTarget",
    "CloudSchedulerJobPubsubTargetOutputReference",
    "CloudSchedulerJobRetryConfig",
    "CloudSchedulerJobRetryConfigOutputReference",
    "CloudSchedulerJobTimeouts",
    "CloudSchedulerJobTimeoutsOutputReference",
]

publication.publish()
