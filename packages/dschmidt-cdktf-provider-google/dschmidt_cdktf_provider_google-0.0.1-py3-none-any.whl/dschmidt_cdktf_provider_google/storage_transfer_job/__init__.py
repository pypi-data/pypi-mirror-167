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


class StorageTransferJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job google_storage_transfer_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        transfer_spec: typing.Union["StorageTransferJobTransferSpec", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["StorageTransferJobSchedule", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job google_storage_transfer_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Unique description to identify the Transfer Job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#description StorageTransferJob#description}
        :param transfer_spec: transfer_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_spec StorageTransferJob#transfer_spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#id StorageTransferJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#project StorageTransferJob#project}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule StorageTransferJob#schedule}
        :param status: Status of the job. Default: ENABLED. NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#status StorageTransferJob#status}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageTransferJobConfig(
            description=description,
            transfer_spec=transfer_spec,
            id=id,
            project=project,
            schedule=schedule,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        schedule_start_date: typing.Union["StorageTransferJobScheduleScheduleStartDate", typing.Dict[str, typing.Any]],
        repeat_interval: typing.Optional[builtins.str] = None,
        schedule_end_date: typing.Optional[typing.Union["StorageTransferJobScheduleScheduleEndDate", typing.Dict[str, typing.Any]]] = None,
        start_time_of_day: typing.Optional[typing.Union["StorageTransferJobScheduleStartTimeOfDay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param schedule_start_date: schedule_start_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_start_date StorageTransferJob#schedule_start_date}
        :param repeat_interval: Interval between the start of each scheduled transfer. If unspecified, the default value is 24 hours. This value may not be less than 1 hour. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#repeat_interval StorageTransferJob#repeat_interval}
        :param schedule_end_date: schedule_end_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_end_date StorageTransferJob#schedule_end_date}
        :param start_time_of_day: start_time_of_day block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#start_time_of_day StorageTransferJob#start_time_of_day}
        '''
        value = StorageTransferJobSchedule(
            schedule_start_date=schedule_start_date,
            repeat_interval=repeat_interval,
            schedule_end_date=schedule_end_date,
            start_time_of_day=start_time_of_day,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="putTransferSpec")
    def put_transfer_spec(
        self,
        *,
        aws_s3_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecAwsS3DataSource", typing.Dict[str, typing.Any]]] = None,
        azure_blob_storage_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecAzureBlobStorageDataSource", typing.Dict[str, typing.Any]]] = None,
        gcs_data_sink: typing.Optional[typing.Union["StorageTransferJobTransferSpecGcsDataSink", typing.Dict[str, typing.Any]]] = None,
        gcs_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecGcsDataSource", typing.Dict[str, typing.Any]]] = None,
        http_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecHttpDataSource", typing.Dict[str, typing.Any]]] = None,
        object_conditions: typing.Optional[typing.Union["StorageTransferJobTransferSpecObjectConditions", typing.Dict[str, typing.Any]]] = None,
        posix_data_sink: typing.Optional[typing.Union["StorageTransferJobTransferSpecPosixDataSink", typing.Dict[str, typing.Any]]] = None,
        posix_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecPosixDataSource", typing.Dict[str, typing.Any]]] = None,
        transfer_options: typing.Optional[typing.Union["StorageTransferJobTransferSpecTransferOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_s3_data_source: aws_s3_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_s3_data_source StorageTransferJob#aws_s3_data_source}
        :param azure_blob_storage_data_source: azure_blob_storage_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_blob_storage_data_source StorageTransferJob#azure_blob_storage_data_source}
        :param gcs_data_sink: gcs_data_sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_sink StorageTransferJob#gcs_data_sink}
        :param gcs_data_source: gcs_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_source StorageTransferJob#gcs_data_source}
        :param http_data_source: http_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#http_data_source StorageTransferJob#http_data_source}
        :param object_conditions: object_conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#object_conditions StorageTransferJob#object_conditions}
        :param posix_data_sink: posix_data_sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_sink StorageTransferJob#posix_data_sink}
        :param posix_data_source: posix_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_source StorageTransferJob#posix_data_source}
        :param transfer_options: transfer_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_options StorageTransferJob#transfer_options}
        '''
        value = StorageTransferJobTransferSpec(
            aws_s3_data_source=aws_s3_data_source,
            azure_blob_storage_data_source=azure_blob_storage_data_source,
            gcs_data_sink=gcs_data_sink,
            gcs_data_source=gcs_data_source,
            http_data_source=http_data_source,
            object_conditions=object_conditions,
            posix_data_sink=posix_data_sink,
            posix_data_source=posix_data_source,
            transfer_options=transfer_options,
        )

        return typing.cast(None, jsii.invoke(self, "putTransferSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="deletionTime")
    def deletion_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deletionTime"))

    @builtins.property
    @jsii.member(jsii_name="lastModificationTime")
    def last_modification_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "StorageTransferJobScheduleOutputReference":
        return typing.cast("StorageTransferJobScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="transferSpec")
    def transfer_spec(self) -> "StorageTransferJobTransferSpecOutputReference":
        return typing.cast("StorageTransferJobTransferSpecOutputReference", jsii.get(self, "transferSpec"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["StorageTransferJobSchedule"]:
        return typing.cast(typing.Optional["StorageTransferJobSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="transferSpecInput")
    def transfer_spec_input(self) -> typing.Optional["StorageTransferJobTransferSpec"]:
        return typing.cast(typing.Optional["StorageTransferJobTransferSpec"], jsii.get(self, "transferSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJob, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJob, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJob, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "transfer_spec": "transferSpec",
        "id": "id",
        "project": "project",
        "schedule": "schedule",
        "status": "status",
    },
)
class StorageTransferJobConfig(cdktf.TerraformMetaArguments):
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
        description: builtins.str,
        transfer_spec: typing.Union["StorageTransferJobTransferSpec", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["StorageTransferJobSchedule", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param description: Unique description to identify the Transfer Job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#description StorageTransferJob#description}
        :param transfer_spec: transfer_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_spec StorageTransferJob#transfer_spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#id StorageTransferJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#project StorageTransferJob#project}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule StorageTransferJob#schedule}
        :param status: Status of the job. Default: ENABLED. NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#status StorageTransferJob#status}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(transfer_spec, dict):
            transfer_spec = StorageTransferJobTransferSpec(**transfer_spec)
        if isinstance(schedule, dict):
            schedule = StorageTransferJobSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument transfer_spec", value=transfer_spec, expected_type=type_hints["transfer_spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "transfer_spec": transfer_spec,
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
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if schedule is not None:
            self._values["schedule"] = schedule
        if status is not None:
            self._values["status"] = status

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
    def description(self) -> builtins.str:
        '''Unique description to identify the Transfer Job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#description StorageTransferJob#description}
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transfer_spec(self) -> "StorageTransferJobTransferSpec":
        '''transfer_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_spec StorageTransferJob#transfer_spec}
        '''
        result = self._values.get("transfer_spec")
        assert result is not None, "Required property 'transfer_spec' is missing"
        return typing.cast("StorageTransferJobTransferSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#id StorageTransferJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project in which the resource belongs. If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#project StorageTransferJob#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["StorageTransferJobSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule StorageTransferJob#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["StorageTransferJobSchedule"], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Status of the job.

        Default: ENABLED. NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#status StorageTransferJob#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "schedule_start_date": "scheduleStartDate",
        "repeat_interval": "repeatInterval",
        "schedule_end_date": "scheduleEndDate",
        "start_time_of_day": "startTimeOfDay",
    },
)
class StorageTransferJobSchedule:
    def __init__(
        self,
        *,
        schedule_start_date: typing.Union["StorageTransferJobScheduleScheduleStartDate", typing.Dict[str, typing.Any]],
        repeat_interval: typing.Optional[builtins.str] = None,
        schedule_end_date: typing.Optional[typing.Union["StorageTransferJobScheduleScheduleEndDate", typing.Dict[str, typing.Any]]] = None,
        start_time_of_day: typing.Optional[typing.Union["StorageTransferJobScheduleStartTimeOfDay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param schedule_start_date: schedule_start_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_start_date StorageTransferJob#schedule_start_date}
        :param repeat_interval: Interval between the start of each scheduled transfer. If unspecified, the default value is 24 hours. This value may not be less than 1 hour. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#repeat_interval StorageTransferJob#repeat_interval}
        :param schedule_end_date: schedule_end_date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_end_date StorageTransferJob#schedule_end_date}
        :param start_time_of_day: start_time_of_day block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#start_time_of_day StorageTransferJob#start_time_of_day}
        '''
        if isinstance(schedule_start_date, dict):
            schedule_start_date = StorageTransferJobScheduleScheduleStartDate(**schedule_start_date)
        if isinstance(schedule_end_date, dict):
            schedule_end_date = StorageTransferJobScheduleScheduleEndDate(**schedule_end_date)
        if isinstance(start_time_of_day, dict):
            start_time_of_day = StorageTransferJobScheduleStartTimeOfDay(**start_time_of_day)
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobSchedule.__init__)
            check_type(argname="argument schedule_start_date", value=schedule_start_date, expected_type=type_hints["schedule_start_date"])
            check_type(argname="argument repeat_interval", value=repeat_interval, expected_type=type_hints["repeat_interval"])
            check_type(argname="argument schedule_end_date", value=schedule_end_date, expected_type=type_hints["schedule_end_date"])
            check_type(argname="argument start_time_of_day", value=start_time_of_day, expected_type=type_hints["start_time_of_day"])
        self._values: typing.Dict[str, typing.Any] = {
            "schedule_start_date": schedule_start_date,
        }
        if repeat_interval is not None:
            self._values["repeat_interval"] = repeat_interval
        if schedule_end_date is not None:
            self._values["schedule_end_date"] = schedule_end_date
        if start_time_of_day is not None:
            self._values["start_time_of_day"] = start_time_of_day

    @builtins.property
    def schedule_start_date(self) -> "StorageTransferJobScheduleScheduleStartDate":
        '''schedule_start_date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_start_date StorageTransferJob#schedule_start_date}
        '''
        result = self._values.get("schedule_start_date")
        assert result is not None, "Required property 'schedule_start_date' is missing"
        return typing.cast("StorageTransferJobScheduleScheduleStartDate", result)

    @builtins.property
    def repeat_interval(self) -> typing.Optional[builtins.str]:
        '''Interval between the start of each scheduled transfer.

        If unspecified, the default value is 24 hours. This value may not be less than 1 hour. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#repeat_interval StorageTransferJob#repeat_interval}
        '''
        result = self._values.get("repeat_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_end_date(
        self,
    ) -> typing.Optional["StorageTransferJobScheduleScheduleEndDate"]:
        '''schedule_end_date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#schedule_end_date StorageTransferJob#schedule_end_date}
        '''
        result = self._values.get("schedule_end_date")
        return typing.cast(typing.Optional["StorageTransferJobScheduleScheduleEndDate"], result)

    @builtins.property
    def start_time_of_day(
        self,
    ) -> typing.Optional["StorageTransferJobScheduleStartTimeOfDay"]:
        '''start_time_of_day block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#start_time_of_day StorageTransferJob#start_time_of_day}
        '''
        result = self._values.get("start_time_of_day")
        return typing.cast(typing.Optional["StorageTransferJobScheduleStartTimeOfDay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScheduleEndDate")
    def put_schedule_end_date(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        :param month: Month of year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        :param year: Year of date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        value = StorageTransferJobScheduleScheduleEndDate(
            day=day, month=month, year=year
        )

        return typing.cast(None, jsii.invoke(self, "putScheduleEndDate", [value]))

    @jsii.member(jsii_name="putScheduleStartDate")
    def put_schedule_start_date(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        :param month: Month of year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        :param year: Year of date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        value = StorageTransferJobScheduleScheduleStartDate(
            day=day, month=month, year=year
        )

        return typing.cast(None, jsii.invoke(self, "putScheduleStartDate", [value]))

    @jsii.member(jsii_name="putStartTimeOfDay")
    def put_start_time_of_day(
        self,
        *,
        hours: jsii.Number,
        minutes: jsii.Number,
        nanos: jsii.Number,
        seconds: jsii.Number,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#hours StorageTransferJob#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#minutes StorageTransferJob#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#nanos StorageTransferJob#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#seconds StorageTransferJob#seconds}
        '''
        value = StorageTransferJobScheduleStartTimeOfDay(
            hours=hours, minutes=minutes, nanos=nanos, seconds=seconds
        )

        return typing.cast(None, jsii.invoke(self, "putStartTimeOfDay", [value]))

    @jsii.member(jsii_name="resetRepeatInterval")
    def reset_repeat_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepeatInterval", []))

    @jsii.member(jsii_name="resetScheduleEndDate")
    def reset_schedule_end_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleEndDate", []))

    @jsii.member(jsii_name="resetStartTimeOfDay")
    def reset_start_time_of_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimeOfDay", []))

    @builtins.property
    @jsii.member(jsii_name="scheduleEndDate")
    def schedule_end_date(
        self,
    ) -> "StorageTransferJobScheduleScheduleEndDateOutputReference":
        return typing.cast("StorageTransferJobScheduleScheduleEndDateOutputReference", jsii.get(self, "scheduleEndDate"))

    @builtins.property
    @jsii.member(jsii_name="scheduleStartDate")
    def schedule_start_date(
        self,
    ) -> "StorageTransferJobScheduleScheduleStartDateOutputReference":
        return typing.cast("StorageTransferJobScheduleScheduleStartDateOutputReference", jsii.get(self, "scheduleStartDate"))

    @builtins.property
    @jsii.member(jsii_name="startTimeOfDay")
    def start_time_of_day(
        self,
    ) -> "StorageTransferJobScheduleStartTimeOfDayOutputReference":
        return typing.cast("StorageTransferJobScheduleStartTimeOfDayOutputReference", jsii.get(self, "startTimeOfDay"))

    @builtins.property
    @jsii.member(jsii_name="repeatIntervalInput")
    def repeat_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repeatIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleEndDateInput")
    def schedule_end_date_input(
        self,
    ) -> typing.Optional["StorageTransferJobScheduleScheduleEndDate"]:
        return typing.cast(typing.Optional["StorageTransferJobScheduleScheduleEndDate"], jsii.get(self, "scheduleEndDateInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleStartDateInput")
    def schedule_start_date_input(
        self,
    ) -> typing.Optional["StorageTransferJobScheduleScheduleStartDate"]:
        return typing.cast(typing.Optional["StorageTransferJobScheduleScheduleStartDate"], jsii.get(self, "scheduleStartDateInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeOfDayInput")
    def start_time_of_day_input(
        self,
    ) -> typing.Optional["StorageTransferJobScheduleStartTimeOfDay"]:
        return typing.cast(typing.Optional["StorageTransferJobScheduleStartTimeOfDay"], jsii.get(self, "startTimeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="repeatInterval")
    def repeat_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repeatInterval"))

    @repeat_interval.setter
    def repeat_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleOutputReference, "repeat_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repeatInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageTransferJobSchedule]:
        return typing.cast(typing.Optional[StorageTransferJobSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleScheduleEndDate",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "month": "month", "year": "year"},
)
class StorageTransferJobScheduleScheduleEndDate:
    def __init__(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        :param month: Month of year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        :param year: Year of date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobScheduleScheduleEndDate.__init__)
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
        '''Day of month. Must be from 1 to 31 and valid for the year and month.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        '''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def month(self) -> jsii.Number:
        '''Month of year. Must be from 1 to 12.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        '''
        result = self._values.get("month")
        assert result is not None, "Required property 'month' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def year(self) -> jsii.Number:
        '''Year of date. Must be from 1 to 9999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        result = self._values.get("year")
        assert result is not None, "Required property 'year' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobScheduleScheduleEndDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobScheduleScheduleEndDateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleScheduleEndDateOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobScheduleScheduleEndDateOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleEndDateOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "month"))

    @month.setter
    def month(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleEndDateOutputReference, "month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "year"))

    @year.setter
    def year(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleEndDateOutputReference, "year").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "year", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobScheduleScheduleEndDate]:
        return typing.cast(typing.Optional[StorageTransferJobScheduleScheduleEndDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobScheduleScheduleEndDate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleEndDateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleScheduleStartDate",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "month": "month", "year": "year"},
)
class StorageTransferJobScheduleScheduleStartDate:
    def __init__(
        self,
        *,
        day: jsii.Number,
        month: jsii.Number,
        year: jsii.Number,
    ) -> None:
        '''
        :param day: Day of month. Must be from 1 to 31 and valid for the year and month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        :param month: Month of year. Must be from 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        :param year: Year of date. Must be from 1 to 9999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobScheduleScheduleStartDate.__init__)
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
        '''Day of month. Must be from 1 to 31 and valid for the year and month.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#day StorageTransferJob#day}
        '''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def month(self) -> jsii.Number:
        '''Month of year. Must be from 1 to 12.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#month StorageTransferJob#month}
        '''
        result = self._values.get("month")
        assert result is not None, "Required property 'month' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def year(self) -> jsii.Number:
        '''Year of date. Must be from 1 to 9999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#year StorageTransferJob#year}
        '''
        result = self._values.get("year")
        assert result is not None, "Required property 'year' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobScheduleScheduleStartDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobScheduleScheduleStartDateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleScheduleStartDateOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobScheduleScheduleStartDateOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleStartDateOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "month"))

    @month.setter
    def month(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleStartDateOutputReference, "month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "year"))

    @year.setter
    def year(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleStartDateOutputReference, "year").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "year", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobScheduleScheduleStartDate]:
        return typing.cast(typing.Optional[StorageTransferJobScheduleScheduleStartDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobScheduleScheduleStartDate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleScheduleStartDateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleStartTimeOfDay",
    jsii_struct_bases=[],
    name_mapping={
        "hours": "hours",
        "minutes": "minutes",
        "nanos": "nanos",
        "seconds": "seconds",
    },
)
class StorageTransferJobScheduleStartTimeOfDay:
    def __init__(
        self,
        *,
        hours: jsii.Number,
        minutes: jsii.Number,
        nanos: jsii.Number,
        seconds: jsii.Number,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#hours StorageTransferJob#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#minutes StorageTransferJob#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#nanos StorageTransferJob#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#seconds StorageTransferJob#seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobScheduleStartTimeOfDay.__init__)
            check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "hours": hours,
            "minutes": minutes,
            "nanos": nanos,
            "seconds": seconds,
        }

    @builtins.property
    def hours(self) -> jsii.Number:
        '''Hours of day in 24 hour format. Should be from 0 to 23.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#hours StorageTransferJob#hours}
        '''
        result = self._values.get("hours")
        assert result is not None, "Required property 'hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''Minutes of hour of day. Must be from 0 to 59.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#minutes StorageTransferJob#minutes}
        '''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nanos(self) -> jsii.Number:
        '''Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#nanos StorageTransferJob#nanos}
        '''
        result = self._values.get("nanos")
        assert result is not None, "Required property 'nanos' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def seconds(self) -> jsii.Number:
        '''Seconds of minutes of the time. Must normally be from 0 to 59.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#seconds StorageTransferJob#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobScheduleStartTimeOfDay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobScheduleStartTimeOfDayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobScheduleStartTimeOfDayOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobScheduleStartTimeOfDayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="hoursInput")
    def hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hoursInput"))

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @hours.setter
    def hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleStartTimeOfDayOutputReference, "hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hours", value)

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleStartTimeOfDayOutputReference, "minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleStartTimeOfDayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleStartTimeOfDayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobScheduleStartTimeOfDay]:
        return typing.cast(typing.Optional[StorageTransferJobScheduleStartTimeOfDay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobScheduleStartTimeOfDay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobScheduleStartTimeOfDayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpec",
    jsii_struct_bases=[],
    name_mapping={
        "aws_s3_data_source": "awsS3DataSource",
        "azure_blob_storage_data_source": "azureBlobStorageDataSource",
        "gcs_data_sink": "gcsDataSink",
        "gcs_data_source": "gcsDataSource",
        "http_data_source": "httpDataSource",
        "object_conditions": "objectConditions",
        "posix_data_sink": "posixDataSink",
        "posix_data_source": "posixDataSource",
        "transfer_options": "transferOptions",
    },
)
class StorageTransferJobTransferSpec:
    def __init__(
        self,
        *,
        aws_s3_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecAwsS3DataSource", typing.Dict[str, typing.Any]]] = None,
        azure_blob_storage_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecAzureBlobStorageDataSource", typing.Dict[str, typing.Any]]] = None,
        gcs_data_sink: typing.Optional[typing.Union["StorageTransferJobTransferSpecGcsDataSink", typing.Dict[str, typing.Any]]] = None,
        gcs_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecGcsDataSource", typing.Dict[str, typing.Any]]] = None,
        http_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecHttpDataSource", typing.Dict[str, typing.Any]]] = None,
        object_conditions: typing.Optional[typing.Union["StorageTransferJobTransferSpecObjectConditions", typing.Dict[str, typing.Any]]] = None,
        posix_data_sink: typing.Optional[typing.Union["StorageTransferJobTransferSpecPosixDataSink", typing.Dict[str, typing.Any]]] = None,
        posix_data_source: typing.Optional[typing.Union["StorageTransferJobTransferSpecPosixDataSource", typing.Dict[str, typing.Any]]] = None,
        transfer_options: typing.Optional[typing.Union["StorageTransferJobTransferSpecTransferOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_s3_data_source: aws_s3_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_s3_data_source StorageTransferJob#aws_s3_data_source}
        :param azure_blob_storage_data_source: azure_blob_storage_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_blob_storage_data_source StorageTransferJob#azure_blob_storage_data_source}
        :param gcs_data_sink: gcs_data_sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_sink StorageTransferJob#gcs_data_sink}
        :param gcs_data_source: gcs_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_source StorageTransferJob#gcs_data_source}
        :param http_data_source: http_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#http_data_source StorageTransferJob#http_data_source}
        :param object_conditions: object_conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#object_conditions StorageTransferJob#object_conditions}
        :param posix_data_sink: posix_data_sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_sink StorageTransferJob#posix_data_sink}
        :param posix_data_source: posix_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_source StorageTransferJob#posix_data_source}
        :param transfer_options: transfer_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_options StorageTransferJob#transfer_options}
        '''
        if isinstance(aws_s3_data_source, dict):
            aws_s3_data_source = StorageTransferJobTransferSpecAwsS3DataSource(**aws_s3_data_source)
        if isinstance(azure_blob_storage_data_source, dict):
            azure_blob_storage_data_source = StorageTransferJobTransferSpecAzureBlobStorageDataSource(**azure_blob_storage_data_source)
        if isinstance(gcs_data_sink, dict):
            gcs_data_sink = StorageTransferJobTransferSpecGcsDataSink(**gcs_data_sink)
        if isinstance(gcs_data_source, dict):
            gcs_data_source = StorageTransferJobTransferSpecGcsDataSource(**gcs_data_source)
        if isinstance(http_data_source, dict):
            http_data_source = StorageTransferJobTransferSpecHttpDataSource(**http_data_source)
        if isinstance(object_conditions, dict):
            object_conditions = StorageTransferJobTransferSpecObjectConditions(**object_conditions)
        if isinstance(posix_data_sink, dict):
            posix_data_sink = StorageTransferJobTransferSpecPosixDataSink(**posix_data_sink)
        if isinstance(posix_data_source, dict):
            posix_data_source = StorageTransferJobTransferSpecPosixDataSource(**posix_data_source)
        if isinstance(transfer_options, dict):
            transfer_options = StorageTransferJobTransferSpecTransferOptions(**transfer_options)
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpec.__init__)
            check_type(argname="argument aws_s3_data_source", value=aws_s3_data_source, expected_type=type_hints["aws_s3_data_source"])
            check_type(argname="argument azure_blob_storage_data_source", value=azure_blob_storage_data_source, expected_type=type_hints["azure_blob_storage_data_source"])
            check_type(argname="argument gcs_data_sink", value=gcs_data_sink, expected_type=type_hints["gcs_data_sink"])
            check_type(argname="argument gcs_data_source", value=gcs_data_source, expected_type=type_hints["gcs_data_source"])
            check_type(argname="argument http_data_source", value=http_data_source, expected_type=type_hints["http_data_source"])
            check_type(argname="argument object_conditions", value=object_conditions, expected_type=type_hints["object_conditions"])
            check_type(argname="argument posix_data_sink", value=posix_data_sink, expected_type=type_hints["posix_data_sink"])
            check_type(argname="argument posix_data_source", value=posix_data_source, expected_type=type_hints["posix_data_source"])
            check_type(argname="argument transfer_options", value=transfer_options, expected_type=type_hints["transfer_options"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_s3_data_source is not None:
            self._values["aws_s3_data_source"] = aws_s3_data_source
        if azure_blob_storage_data_source is not None:
            self._values["azure_blob_storage_data_source"] = azure_blob_storage_data_source
        if gcs_data_sink is not None:
            self._values["gcs_data_sink"] = gcs_data_sink
        if gcs_data_source is not None:
            self._values["gcs_data_source"] = gcs_data_source
        if http_data_source is not None:
            self._values["http_data_source"] = http_data_source
        if object_conditions is not None:
            self._values["object_conditions"] = object_conditions
        if posix_data_sink is not None:
            self._values["posix_data_sink"] = posix_data_sink
        if posix_data_source is not None:
            self._values["posix_data_source"] = posix_data_source
        if transfer_options is not None:
            self._values["transfer_options"] = transfer_options

    @builtins.property
    def aws_s3_data_source(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecAwsS3DataSource"]:
        '''aws_s3_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_s3_data_source StorageTransferJob#aws_s3_data_source}
        '''
        result = self._values.get("aws_s3_data_source")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecAwsS3DataSource"], result)

    @builtins.property
    def azure_blob_storage_data_source(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecAzureBlobStorageDataSource"]:
        '''azure_blob_storage_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_blob_storage_data_source StorageTransferJob#azure_blob_storage_data_source}
        '''
        result = self._values.get("azure_blob_storage_data_source")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecAzureBlobStorageDataSource"], result)

    @builtins.property
    def gcs_data_sink(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecGcsDataSink"]:
        '''gcs_data_sink block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_sink StorageTransferJob#gcs_data_sink}
        '''
        result = self._values.get("gcs_data_sink")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecGcsDataSink"], result)

    @builtins.property
    def gcs_data_source(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecGcsDataSource"]:
        '''gcs_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#gcs_data_source StorageTransferJob#gcs_data_source}
        '''
        result = self._values.get("gcs_data_source")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecGcsDataSource"], result)

    @builtins.property
    def http_data_source(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecHttpDataSource"]:
        '''http_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#http_data_source StorageTransferJob#http_data_source}
        '''
        result = self._values.get("http_data_source")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecHttpDataSource"], result)

    @builtins.property
    def object_conditions(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecObjectConditions"]:
        '''object_conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#object_conditions StorageTransferJob#object_conditions}
        '''
        result = self._values.get("object_conditions")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecObjectConditions"], result)

    @builtins.property
    def posix_data_sink(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecPosixDataSink"]:
        '''posix_data_sink block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_sink StorageTransferJob#posix_data_sink}
        '''
        result = self._values.get("posix_data_sink")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecPosixDataSink"], result)

    @builtins.property
    def posix_data_source(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecPosixDataSource"]:
        '''posix_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#posix_data_source StorageTransferJob#posix_data_source}
        '''
        result = self._values.get("posix_data_source")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecPosixDataSource"], result)

    @builtins.property
    def transfer_options(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecTransferOptions"]:
        '''transfer_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#transfer_options StorageTransferJob#transfer_options}
        '''
        result = self._values.get("transfer_options")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecTransferOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAwsS3DataSource",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "aws_access_key": "awsAccessKey",
        "role_arn": "roleArn",
    },
)
class StorageTransferJobTransferSpecAwsS3DataSource:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        aws_access_key: typing.Optional[typing.Union["StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey", typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: S3 Bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param aws_access_key: aws_access_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_access_key StorageTransferJob#aws_access_key}
        :param role_arn: The Amazon Resource Name (ARN) of the role to support temporary credentials via 'AssumeRoleWithWebIdentity'. For more information about ARNs, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns>`_. When a role ARN is provided, Transfer Service fetches temporary credentials for the session using a 'AssumeRoleWithWebIdentity' call for the provided role using the [GoogleServiceAccount][] for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#role_arn StorageTransferJob#role_arn}
        '''
        if isinstance(aws_access_key, dict):
            aws_access_key = StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey(**aws_access_key)
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAwsS3DataSource.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument aws_access_key", value=aws_access_key, expected_type=type_hints["aws_access_key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if aws_access_key is not None:
            self._values["aws_access_key"] = aws_access_key
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''S3 Bucket name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_access_key(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey"]:
        '''aws_access_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_access_key StorageTransferJob#aws_access_key}
        '''
        result = self._values.get("aws_access_key")
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey"], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to support temporary credentials via 'AssumeRoleWithWebIdentity'.

        For more information about ARNs, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns>`_. When a role ARN is provided, Transfer Service fetches temporary credentials for the session using a 'AssumeRoleWithWebIdentity' call for the provided role using the [GoogleServiceAccount][] for this project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#role_arn StorageTransferJob#role_arn}
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecAwsS3DataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "secret_access_key": "secretAccessKey",
    },
)
class StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey:
    def __init__(
        self,
        *,
        access_key_id: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key_id: AWS Key ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#access_key_id StorageTransferJob#access_key_id}
        :param secret_access_key: AWS Secret Access Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#secret_access_key StorageTransferJob#secret_access_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey.__init__)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_key_id": access_key_id,
            "secret_access_key": secret_access_key,
        }

    @builtins.property
    def access_key_id(self) -> builtins.str:
        '''AWS Key ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#access_key_id StorageTransferJob#access_key_id}
        '''
        result = self._values.get("access_key_id")
        assert result is not None, "Required property 'access_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key(self) -> builtins.str:
        '''AWS Secret Access Key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#secret_access_key StorageTransferJob#secret_access_key}
        '''
        result = self._values.get("secret_access_key")
        assert result is not None, "Required property 'secret_access_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accessKeyIdInput")
    def access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyInput")
    def secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @access_key_id.setter
    def access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference, "access_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKey"))

    @secret_access_key.setter
    def secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference, "secret_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageTransferJobTransferSpecAwsS3DataSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAwsS3DataSourceOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAwsS3DataSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsAccessKey")
    def put_aws_access_key(
        self,
        *,
        access_key_id: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key_id: AWS Key ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#access_key_id StorageTransferJob#access_key_id}
        :param secret_access_key: AWS Secret Access Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#secret_access_key StorageTransferJob#secret_access_key}
        '''
        value = StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey(
            access_key_id=access_key_id, secret_access_key=secret_access_key
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAccessKey", [value]))

    @jsii.member(jsii_name="resetAwsAccessKey")
    def reset_aws_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAccessKey", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKey")
    def aws_access_key(
        self,
    ) -> StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference:
        return typing.cast(StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference, jsii.get(self, "awsAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKeyInput")
    def aws_access_key_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey], jsii.get(self, "awsAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceOutputReference, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAwsS3DataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAwsS3DataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecAwsS3DataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAwsS3DataSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAzureBlobStorageDataSource",
    jsii_struct_bases=[],
    name_mapping={
        "azure_credentials": "azureCredentials",
        "container": "container",
        "storage_account": "storageAccount",
        "path": "path",
    },
)
class StorageTransferJobTransferSpecAzureBlobStorageDataSource:
    def __init__(
        self,
        *,
        azure_credentials: typing.Union["StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials", typing.Dict[str, typing.Any]],
        container: builtins.str,
        storage_account: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_credentials: azure_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_credentials StorageTransferJob#azure_credentials}
        :param container: The container to transfer from the Azure Storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#container StorageTransferJob#container}
        :param storage_account: The name of the Azure Storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#storage_account StorageTransferJob#storage_account}
        :param path: Root path to transfer objects. Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        if isinstance(azure_credentials, dict):
            azure_credentials = StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials(**azure_credentials)
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAzureBlobStorageDataSource.__init__)
            check_type(argname="argument azure_credentials", value=azure_credentials, expected_type=type_hints["azure_credentials"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "azure_credentials": azure_credentials,
            "container": container,
            "storage_account": storage_account,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def azure_credentials(
        self,
    ) -> "StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials":
        '''azure_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_credentials StorageTransferJob#azure_credentials}
        '''
        result = self._values.get("azure_credentials")
        assert result is not None, "Required property 'azure_credentials' is missing"
        return typing.cast("StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials", result)

    @builtins.property
    def container(self) -> builtins.str:
        '''The container to transfer from the Azure Storage account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#container StorageTransferJob#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account(self) -> builtins.str:
        '''The name of the Azure Storage account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#storage_account StorageTransferJob#storage_account}
        '''
        result = self._values.get("storage_account")
        assert result is not None, "Required property 'storage_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Root path to transfer objects.

        Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecAzureBlobStorageDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials",
    jsii_struct_bases=[],
    name_mapping={"sas_token": "sasToken"},
)
class StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials:
    def __init__(self, *, sas_token: builtins.str) -> None:
        '''
        :param sas_token: Azure shared access signature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#sas_token StorageTransferJob#sas_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials.__init__)
            check_type(argname="argument sas_token", value=sas_token, expected_type=type_hints["sas_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "sas_token": sas_token,
        }

    @builtins.property
    def sas_token(self) -> builtins.str:
        '''Azure shared access signature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#sas_token StorageTransferJob#sas_token}
        '''
        result = self._values.get("sas_token")
        assert result is not None, "Required property 'sas_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sasTokenInput")
    def sas_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="sasToken")
    def sas_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasToken"))

    @sas_token.setter
    def sas_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference, "sas_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureCredentials")
    def put_azure_credentials(self, *, sas_token: builtins.str) -> None:
        '''
        :param sas_token: Azure shared access signature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#sas_token StorageTransferJob#sas_token}
        '''
        value = StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials(
            sas_token=sas_token
        )

        return typing.cast(None, jsii.invoke(self, "putAzureCredentials", [value]))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="azureCredentials")
    def azure_credentials(
        self,
    ) -> StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference:
        return typing.cast(StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference, jsii.get(self, "azureCredentials"))

    @builtins.property
    @jsii.member(jsii_name="azureCredentialsInput")
    def azure_credentials_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials], jsii.get(self, "azureCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccount"))

    @storage_account.setter
    def storage_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference, "storage_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecGcsDataSink",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "path": "path"},
)
class StorageTransferJobTransferSpecGcsDataSink:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Google Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param path: Google Cloud Storage path in bucket to transfer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecGcsDataSink.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Google Cloud Storage bucket name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Google Cloud Storage path in bucket to transfer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecGcsDataSink(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecGcsDataSinkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecGcsDataSinkOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecGcsDataSinkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSinkOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSinkOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecGcsDataSink]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecGcsDataSink], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecGcsDataSink],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSinkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecGcsDataSource",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "path": "path"},
)
class StorageTransferJobTransferSpecGcsDataSource:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Google Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param path: Google Cloud Storage path in bucket to transfer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecGcsDataSource.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Google Cloud Storage bucket name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Google Cloud Storage path in bucket to transfer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecGcsDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecGcsDataSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecGcsDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecGcsDataSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSourceOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSourceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecGcsDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecGcsDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecGcsDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecGcsDataSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecHttpDataSource",
    jsii_struct_bases=[],
    name_mapping={"list_url": "listUrl"},
)
class StorageTransferJobTransferSpecHttpDataSource:
    def __init__(self, *, list_url: builtins.str) -> None:
        '''
        :param list_url: The URL that points to the file that stores the object list entries. This file must allow public access. Currently, only URLs with HTTP and HTTPS schemes are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#list_url StorageTransferJob#list_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecHttpDataSource.__init__)
            check_type(argname="argument list_url", value=list_url, expected_type=type_hints["list_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "list_url": list_url,
        }

    @builtins.property
    def list_url(self) -> builtins.str:
        '''The URL that points to the file that stores the object list entries.

        This file must allow public access. Currently, only URLs with HTTP and HTTPS schemes are supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#list_url StorageTransferJob#list_url}
        '''
        result = self._values.get("list_url")
        assert result is not None, "Required property 'list_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecHttpDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecHttpDataSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecHttpDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecHttpDataSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="listUrlInput")
    def list_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="listUrl")
    def list_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listUrl"))

    @list_url.setter
    def list_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecHttpDataSourceOutputReference, "list_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecHttpDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecHttpDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecHttpDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecHttpDataSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecObjectConditions",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_prefixes": "excludePrefixes",
        "include_prefixes": "includePrefixes",
        "max_time_elapsed_since_last_modification": "maxTimeElapsedSinceLastModification",
        "min_time_elapsed_since_last_modification": "minTimeElapsedSinceLastModification",
    },
)
class StorageTransferJobTransferSpecObjectConditions:
    def __init__(
        self,
        *,
        exclude_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_time_elapsed_since_last_modification: typing.Optional[builtins.str] = None,
        min_time_elapsed_since_last_modification: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exclude_prefixes: exclude_prefixes must follow the requirements described for include_prefixes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#exclude_prefixes StorageTransferJob#exclude_prefixes}
        :param include_prefixes: If include_refixes is specified, objects that satisfy the object conditions must have names that start with one of the include_prefixes and that do not start with any of the exclude_prefixes. If include_prefixes is not specified, all objects except those that have names starting with one of the exclude_prefixes must satisfy the object conditions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#include_prefixes StorageTransferJob#include_prefixes}
        :param max_time_elapsed_since_last_modification: A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#max_time_elapsed_since_last_modification StorageTransferJob#max_time_elapsed_since_last_modification}
        :param min_time_elapsed_since_last_modification: A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#min_time_elapsed_since_last_modification StorageTransferJob#min_time_elapsed_since_last_modification}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecObjectConditions.__init__)
            check_type(argname="argument exclude_prefixes", value=exclude_prefixes, expected_type=type_hints["exclude_prefixes"])
            check_type(argname="argument include_prefixes", value=include_prefixes, expected_type=type_hints["include_prefixes"])
            check_type(argname="argument max_time_elapsed_since_last_modification", value=max_time_elapsed_since_last_modification, expected_type=type_hints["max_time_elapsed_since_last_modification"])
            check_type(argname="argument min_time_elapsed_since_last_modification", value=min_time_elapsed_since_last_modification, expected_type=type_hints["min_time_elapsed_since_last_modification"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude_prefixes is not None:
            self._values["exclude_prefixes"] = exclude_prefixes
        if include_prefixes is not None:
            self._values["include_prefixes"] = include_prefixes
        if max_time_elapsed_since_last_modification is not None:
            self._values["max_time_elapsed_since_last_modification"] = max_time_elapsed_since_last_modification
        if min_time_elapsed_since_last_modification is not None:
            self._values["min_time_elapsed_since_last_modification"] = min_time_elapsed_since_last_modification

    @builtins.property
    def exclude_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''exclude_prefixes must follow the requirements described for include_prefixes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#exclude_prefixes StorageTransferJob#exclude_prefixes}
        '''
        result = self._values.get("exclude_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If include_refixes is specified, objects that satisfy the object conditions must have names that start with one of the include_prefixes and that do not start with any of the exclude_prefixes.

        If include_prefixes is not specified, all objects except those that have names starting with one of the exclude_prefixes must satisfy the object conditions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#include_prefixes StorageTransferJob#include_prefixes}
        '''
        result = self._values.get("include_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_time_elapsed_since_last_modification(self) -> typing.Optional[builtins.str]:
        '''A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#max_time_elapsed_since_last_modification StorageTransferJob#max_time_elapsed_since_last_modification}
        '''
        result = self._values.get("max_time_elapsed_since_last_modification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_time_elapsed_since_last_modification(self) -> typing.Optional[builtins.str]:
        '''A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#min_time_elapsed_since_last_modification StorageTransferJob#min_time_elapsed_since_last_modification}
        '''
        result = self._values.get("min_time_elapsed_since_last_modification")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecObjectConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecObjectConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecObjectConditionsOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecObjectConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludePrefixes")
    def reset_exclude_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludePrefixes", []))

    @jsii.member(jsii_name="resetIncludePrefixes")
    def reset_include_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePrefixes", []))

    @jsii.member(jsii_name="resetMaxTimeElapsedSinceLastModification")
    def reset_max_time_elapsed_since_last_modification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTimeElapsedSinceLastModification", []))

    @jsii.member(jsii_name="resetMinTimeElapsedSinceLastModification")
    def reset_min_time_elapsed_since_last_modification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTimeElapsedSinceLastModification", []))

    @builtins.property
    @jsii.member(jsii_name="excludePrefixesInput")
    def exclude_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="includePrefixesInput")
    def include_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTimeElapsedSinceLastModificationInput")
    def max_time_elapsed_since_last_modification_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTimeElapsedSinceLastModificationInput"))

    @builtins.property
    @jsii.member(jsii_name="minTimeElapsedSinceLastModificationInput")
    def min_time_elapsed_since_last_modification_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTimeElapsedSinceLastModificationInput"))

    @builtins.property
    @jsii.member(jsii_name="excludePrefixes")
    def exclude_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludePrefixes"))

    @exclude_prefixes.setter
    def exclude_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecObjectConditionsOutputReference, "exclude_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="includePrefixes")
    def include_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includePrefixes"))

    @include_prefixes.setter
    def include_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecObjectConditionsOutputReference, "include_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="maxTimeElapsedSinceLastModification")
    def max_time_elapsed_since_last_modification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTimeElapsedSinceLastModification"))

    @max_time_elapsed_since_last_modification.setter
    def max_time_elapsed_since_last_modification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecObjectConditionsOutputReference, "max_time_elapsed_since_last_modification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTimeElapsedSinceLastModification", value)

    @builtins.property
    @jsii.member(jsii_name="minTimeElapsedSinceLastModification")
    def min_time_elapsed_since_last_modification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTimeElapsedSinceLastModification"))

    @min_time_elapsed_since_last_modification.setter
    def min_time_elapsed_since_last_modification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecObjectConditionsOutputReference, "min_time_elapsed_since_last_modification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTimeElapsedSinceLastModification", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecObjectConditions]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecObjectConditions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecObjectConditions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecObjectConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageTransferJobTransferSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsS3DataSource")
    def put_aws_s3_data_source(
        self,
        *,
        bucket_name: builtins.str,
        aws_access_key: typing.Optional[typing.Union[StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey, typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: S3 Bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param aws_access_key: aws_access_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#aws_access_key StorageTransferJob#aws_access_key}
        :param role_arn: The Amazon Resource Name (ARN) of the role to support temporary credentials via 'AssumeRoleWithWebIdentity'. For more information about ARNs, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns>`_. When a role ARN is provided, Transfer Service fetches temporary credentials for the session using a 'AssumeRoleWithWebIdentity' call for the provided role using the [GoogleServiceAccount][] for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#role_arn StorageTransferJob#role_arn}
        '''
        value = StorageTransferJobTransferSpecAwsS3DataSource(
            bucket_name=bucket_name, aws_access_key=aws_access_key, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putAwsS3DataSource", [value]))

    @jsii.member(jsii_name="putAzureBlobStorageDataSource")
    def put_azure_blob_storage_data_source(
        self,
        *,
        azure_credentials: typing.Union[StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials, typing.Dict[str, typing.Any]],
        container: builtins.str,
        storage_account: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_credentials: azure_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#azure_credentials StorageTransferJob#azure_credentials}
        :param container: The container to transfer from the Azure Storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#container StorageTransferJob#container}
        :param storage_account: The name of the Azure Storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#storage_account StorageTransferJob#storage_account}
        :param path: Root path to transfer objects. Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        value = StorageTransferJobTransferSpecAzureBlobStorageDataSource(
            azure_credentials=azure_credentials,
            container=container,
            storage_account=storage_account,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorageDataSource", [value]))

    @jsii.member(jsii_name="putGcsDataSink")
    def put_gcs_data_sink(
        self,
        *,
        bucket_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Google Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param path: Google Cloud Storage path in bucket to transfer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        value = StorageTransferJobTransferSpecGcsDataSink(
            bucket_name=bucket_name, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putGcsDataSink", [value]))

    @jsii.member(jsii_name="putGcsDataSource")
    def put_gcs_data_source(
        self,
        *,
        bucket_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Google Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#bucket_name StorageTransferJob#bucket_name}
        :param path: Google Cloud Storage path in bucket to transfer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#path StorageTransferJob#path}
        '''
        value = StorageTransferJobTransferSpecGcsDataSource(
            bucket_name=bucket_name, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putGcsDataSource", [value]))

    @jsii.member(jsii_name="putHttpDataSource")
    def put_http_data_source(self, *, list_url: builtins.str) -> None:
        '''
        :param list_url: The URL that points to the file that stores the object list entries. This file must allow public access. Currently, only URLs with HTTP and HTTPS schemes are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#list_url StorageTransferJob#list_url}
        '''
        value = StorageTransferJobTransferSpecHttpDataSource(list_url=list_url)

        return typing.cast(None, jsii.invoke(self, "putHttpDataSource", [value]))

    @jsii.member(jsii_name="putObjectConditions")
    def put_object_conditions(
        self,
        *,
        exclude_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_time_elapsed_since_last_modification: typing.Optional[builtins.str] = None,
        min_time_elapsed_since_last_modification: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exclude_prefixes: exclude_prefixes must follow the requirements described for include_prefixes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#exclude_prefixes StorageTransferJob#exclude_prefixes}
        :param include_prefixes: If include_refixes is specified, objects that satisfy the object conditions must have names that start with one of the include_prefixes and that do not start with any of the exclude_prefixes. If include_prefixes is not specified, all objects except those that have names starting with one of the exclude_prefixes must satisfy the object conditions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#include_prefixes StorageTransferJob#include_prefixes}
        :param max_time_elapsed_since_last_modification: A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#max_time_elapsed_since_last_modification StorageTransferJob#max_time_elapsed_since_last_modification}
        :param min_time_elapsed_since_last_modification: A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#min_time_elapsed_since_last_modification StorageTransferJob#min_time_elapsed_since_last_modification}
        '''
        value = StorageTransferJobTransferSpecObjectConditions(
            exclude_prefixes=exclude_prefixes,
            include_prefixes=include_prefixes,
            max_time_elapsed_since_last_modification=max_time_elapsed_since_last_modification,
            min_time_elapsed_since_last_modification=min_time_elapsed_since_last_modification,
        )

        return typing.cast(None, jsii.invoke(self, "putObjectConditions", [value]))

    @jsii.member(jsii_name="putPosixDataSink")
    def put_posix_data_sink(self, *, root_directory: builtins.str) -> None:
        '''
        :param root_directory: Root directory path to the filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        value = StorageTransferJobTransferSpecPosixDataSink(
            root_directory=root_directory
        )

        return typing.cast(None, jsii.invoke(self, "putPosixDataSink", [value]))

    @jsii.member(jsii_name="putPosixDataSource")
    def put_posix_data_source(self, *, root_directory: builtins.str) -> None:
        '''
        :param root_directory: Root directory path to the filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        value = StorageTransferJobTransferSpecPosixDataSource(
            root_directory=root_directory
        )

        return typing.cast(None, jsii.invoke(self, "putPosixDataSource", [value]))

    @jsii.member(jsii_name="putTransferOptions")
    def put_transfer_options(
        self,
        *,
        delete_objects_from_source_after_transfer: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        delete_objects_unique_in_sink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        overwrite_objects_already_existing_in_sink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param delete_objects_from_source_after_transfer: Whether objects should be deleted from the source after they are transferred to the sink. Note that this option and delete_objects_unique_in_sink are mutually exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_from_source_after_transfer StorageTransferJob#delete_objects_from_source_after_transfer}
        :param delete_objects_unique_in_sink: Whether objects that exist only in the sink should be deleted. Note that this option and delete_objects_from_source_after_transfer are mutually exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_unique_in_sink StorageTransferJob#delete_objects_unique_in_sink}
        :param overwrite_objects_already_existing_in_sink: Whether overwriting objects that already exist in the sink is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#overwrite_objects_already_existing_in_sink StorageTransferJob#overwrite_objects_already_existing_in_sink}
        '''
        value = StorageTransferJobTransferSpecTransferOptions(
            delete_objects_from_source_after_transfer=delete_objects_from_source_after_transfer,
            delete_objects_unique_in_sink=delete_objects_unique_in_sink,
            overwrite_objects_already_existing_in_sink=overwrite_objects_already_existing_in_sink,
        )

        return typing.cast(None, jsii.invoke(self, "putTransferOptions", [value]))

    @jsii.member(jsii_name="resetAwsS3DataSource")
    def reset_aws_s3_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3DataSource", []))

    @jsii.member(jsii_name="resetAzureBlobStorageDataSource")
    def reset_azure_blob_storage_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorageDataSource", []))

    @jsii.member(jsii_name="resetGcsDataSink")
    def reset_gcs_data_sink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsDataSink", []))

    @jsii.member(jsii_name="resetGcsDataSource")
    def reset_gcs_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsDataSource", []))

    @jsii.member(jsii_name="resetHttpDataSource")
    def reset_http_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpDataSource", []))

    @jsii.member(jsii_name="resetObjectConditions")
    def reset_object_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectConditions", []))

    @jsii.member(jsii_name="resetPosixDataSink")
    def reset_posix_data_sink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosixDataSink", []))

    @jsii.member(jsii_name="resetPosixDataSource")
    def reset_posix_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosixDataSource", []))

    @jsii.member(jsii_name="resetTransferOptions")
    def reset_transfer_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransferOptions", []))

    @builtins.property
    @jsii.member(jsii_name="awsS3DataSource")
    def aws_s3_data_source(
        self,
    ) -> StorageTransferJobTransferSpecAwsS3DataSourceOutputReference:
        return typing.cast(StorageTransferJobTransferSpecAwsS3DataSourceOutputReference, jsii.get(self, "awsS3DataSource"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageDataSource")
    def azure_blob_storage_data_source(
        self,
    ) -> StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference:
        return typing.cast(StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference, jsii.get(self, "azureBlobStorageDataSource"))

    @builtins.property
    @jsii.member(jsii_name="gcsDataSink")
    def gcs_data_sink(self) -> StorageTransferJobTransferSpecGcsDataSinkOutputReference:
        return typing.cast(StorageTransferJobTransferSpecGcsDataSinkOutputReference, jsii.get(self, "gcsDataSink"))

    @builtins.property
    @jsii.member(jsii_name="gcsDataSource")
    def gcs_data_source(
        self,
    ) -> StorageTransferJobTransferSpecGcsDataSourceOutputReference:
        return typing.cast(StorageTransferJobTransferSpecGcsDataSourceOutputReference, jsii.get(self, "gcsDataSource"))

    @builtins.property
    @jsii.member(jsii_name="httpDataSource")
    def http_data_source(
        self,
    ) -> StorageTransferJobTransferSpecHttpDataSourceOutputReference:
        return typing.cast(StorageTransferJobTransferSpecHttpDataSourceOutputReference, jsii.get(self, "httpDataSource"))

    @builtins.property
    @jsii.member(jsii_name="objectConditions")
    def object_conditions(
        self,
    ) -> StorageTransferJobTransferSpecObjectConditionsOutputReference:
        return typing.cast(StorageTransferJobTransferSpecObjectConditionsOutputReference, jsii.get(self, "objectConditions"))

    @builtins.property
    @jsii.member(jsii_name="posixDataSink")
    def posix_data_sink(
        self,
    ) -> "StorageTransferJobTransferSpecPosixDataSinkOutputReference":
        return typing.cast("StorageTransferJobTransferSpecPosixDataSinkOutputReference", jsii.get(self, "posixDataSink"))

    @builtins.property
    @jsii.member(jsii_name="posixDataSource")
    def posix_data_source(
        self,
    ) -> "StorageTransferJobTransferSpecPosixDataSourceOutputReference":
        return typing.cast("StorageTransferJobTransferSpecPosixDataSourceOutputReference", jsii.get(self, "posixDataSource"))

    @builtins.property
    @jsii.member(jsii_name="transferOptions")
    def transfer_options(
        self,
    ) -> "StorageTransferJobTransferSpecTransferOptionsOutputReference":
        return typing.cast("StorageTransferJobTransferSpecTransferOptionsOutputReference", jsii.get(self, "transferOptions"))

    @builtins.property
    @jsii.member(jsii_name="awsS3DataSourceInput")
    def aws_s3_data_source_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAwsS3DataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAwsS3DataSource], jsii.get(self, "awsS3DataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageDataSourceInput")
    def azure_blob_storage_data_source_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecAzureBlobStorageDataSource], jsii.get(self, "azureBlobStorageDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsDataSinkInput")
    def gcs_data_sink_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecGcsDataSink]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecGcsDataSink], jsii.get(self, "gcsDataSinkInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsDataSourceInput")
    def gcs_data_source_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecGcsDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecGcsDataSource], jsii.get(self, "gcsDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="httpDataSourceInput")
    def http_data_source_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecHttpDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecHttpDataSource], jsii.get(self, "httpDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="objectConditionsInput")
    def object_conditions_input(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecObjectConditions]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecObjectConditions], jsii.get(self, "objectConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="posixDataSinkInput")
    def posix_data_sink_input(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecPosixDataSink"]:
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecPosixDataSink"], jsii.get(self, "posixDataSinkInput"))

    @builtins.property
    @jsii.member(jsii_name="posixDataSourceInput")
    def posix_data_source_input(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecPosixDataSource"]:
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecPosixDataSource"], jsii.get(self, "posixDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="transferOptionsInput")
    def transfer_options_input(
        self,
    ) -> typing.Optional["StorageTransferJobTransferSpecTransferOptions"]:
        return typing.cast(typing.Optional["StorageTransferJobTransferSpecTransferOptions"], jsii.get(self, "transferOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageTransferJobTransferSpec]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecPosixDataSink",
    jsii_struct_bases=[],
    name_mapping={"root_directory": "rootDirectory"},
)
class StorageTransferJobTransferSpecPosixDataSink:
    def __init__(self, *, root_directory: builtins.str) -> None:
        '''
        :param root_directory: Root directory path to the filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecPosixDataSink.__init__)
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "root_directory": root_directory,
        }

    @builtins.property
    def root_directory(self) -> builtins.str:
        '''Root directory path to the filesystem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        result = self._values.get("root_directory")
        assert result is not None, "Required property 'root_directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecPosixDataSink(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecPosixDataSinkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecPosixDataSinkOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecPosixDataSinkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecPosixDataSinkOutputReference, "root_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecPosixDataSink]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecPosixDataSink], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecPosixDataSink],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecPosixDataSinkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecPosixDataSource",
    jsii_struct_bases=[],
    name_mapping={"root_directory": "rootDirectory"},
)
class StorageTransferJobTransferSpecPosixDataSource:
    def __init__(self, *, root_directory: builtins.str) -> None:
        '''
        :param root_directory: Root directory path to the filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecPosixDataSource.__init__)
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "root_directory": root_directory,
        }

    @builtins.property
    def root_directory(self) -> builtins.str:
        '''Root directory path to the filesystem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#root_directory StorageTransferJob#root_directory}
        '''
        result = self._values.get("root_directory")
        assert result is not None, "Required property 'root_directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecPosixDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecPosixDataSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecPosixDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecPosixDataSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecPosixDataSourceOutputReference, "root_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecPosixDataSource]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecPosixDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecPosixDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecPosixDataSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecTransferOptions",
    jsii_struct_bases=[],
    name_mapping={
        "delete_objects_from_source_after_transfer": "deleteObjectsFromSourceAfterTransfer",
        "delete_objects_unique_in_sink": "deleteObjectsUniqueInSink",
        "overwrite_objects_already_existing_in_sink": "overwriteObjectsAlreadyExistingInSink",
    },
)
class StorageTransferJobTransferSpecTransferOptions:
    def __init__(
        self,
        *,
        delete_objects_from_source_after_transfer: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        delete_objects_unique_in_sink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        overwrite_objects_already_existing_in_sink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param delete_objects_from_source_after_transfer: Whether objects should be deleted from the source after they are transferred to the sink. Note that this option and delete_objects_unique_in_sink are mutually exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_from_source_after_transfer StorageTransferJob#delete_objects_from_source_after_transfer}
        :param delete_objects_unique_in_sink: Whether objects that exist only in the sink should be deleted. Note that this option and delete_objects_from_source_after_transfer are mutually exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_unique_in_sink StorageTransferJob#delete_objects_unique_in_sink}
        :param overwrite_objects_already_existing_in_sink: Whether overwriting objects that already exist in the sink is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#overwrite_objects_already_existing_in_sink StorageTransferJob#overwrite_objects_already_existing_in_sink}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecTransferOptions.__init__)
            check_type(argname="argument delete_objects_from_source_after_transfer", value=delete_objects_from_source_after_transfer, expected_type=type_hints["delete_objects_from_source_after_transfer"])
            check_type(argname="argument delete_objects_unique_in_sink", value=delete_objects_unique_in_sink, expected_type=type_hints["delete_objects_unique_in_sink"])
            check_type(argname="argument overwrite_objects_already_existing_in_sink", value=overwrite_objects_already_existing_in_sink, expected_type=type_hints["overwrite_objects_already_existing_in_sink"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_objects_from_source_after_transfer is not None:
            self._values["delete_objects_from_source_after_transfer"] = delete_objects_from_source_after_transfer
        if delete_objects_unique_in_sink is not None:
            self._values["delete_objects_unique_in_sink"] = delete_objects_unique_in_sink
        if overwrite_objects_already_existing_in_sink is not None:
            self._values["overwrite_objects_already_existing_in_sink"] = overwrite_objects_already_existing_in_sink

    @builtins.property
    def delete_objects_from_source_after_transfer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether objects should be deleted from the source after they are transferred to the sink.

        Note that this option and delete_objects_unique_in_sink are mutually exclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_from_source_after_transfer StorageTransferJob#delete_objects_from_source_after_transfer}
        '''
        result = self._values.get("delete_objects_from_source_after_transfer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def delete_objects_unique_in_sink(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether objects that exist only in the sink should be deleted.

        Note that this option and delete_objects_from_source_after_transfer are mutually exclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#delete_objects_unique_in_sink StorageTransferJob#delete_objects_unique_in_sink}
        '''
        result = self._values.get("delete_objects_unique_in_sink")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def overwrite_objects_already_existing_in_sink(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether overwriting objects that already exist in the sink is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/storage_transfer_job#overwrite_objects_already_existing_in_sink StorageTransferJob#overwrite_objects_already_existing_in_sink}
        '''
        result = self._values.get("overwrite_objects_already_existing_in_sink")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageTransferJobTransferSpecTransferOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageTransferJobTransferSpecTransferOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.storageTransferJob.StorageTransferJobTransferSpecTransferOptionsOutputReference",
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
            type_hints = typing.get_type_hints(StorageTransferJobTransferSpecTransferOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteObjectsFromSourceAfterTransfer")
    def reset_delete_objects_from_source_after_transfer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteObjectsFromSourceAfterTransfer", []))

    @jsii.member(jsii_name="resetDeleteObjectsUniqueInSink")
    def reset_delete_objects_unique_in_sink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteObjectsUniqueInSink", []))

    @jsii.member(jsii_name="resetOverwriteObjectsAlreadyExistingInSink")
    def reset_overwrite_objects_already_existing_in_sink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteObjectsAlreadyExistingInSink", []))

    @builtins.property
    @jsii.member(jsii_name="deleteObjectsFromSourceAfterTransferInput")
    def delete_objects_from_source_after_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteObjectsFromSourceAfterTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteObjectsUniqueInSinkInput")
    def delete_objects_unique_in_sink_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteObjectsUniqueInSinkInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteObjectsAlreadyExistingInSinkInput")
    def overwrite_objects_already_existing_in_sink_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteObjectsAlreadyExistingInSinkInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteObjectsFromSourceAfterTransfer")
    def delete_objects_from_source_after_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteObjectsFromSourceAfterTransfer"))

    @delete_objects_from_source_after_transfer.setter
    def delete_objects_from_source_after_transfer(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecTransferOptionsOutputReference, "delete_objects_from_source_after_transfer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteObjectsFromSourceAfterTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="deleteObjectsUniqueInSink")
    def delete_objects_unique_in_sink(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteObjectsUniqueInSink"))

    @delete_objects_unique_in_sink.setter
    def delete_objects_unique_in_sink(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecTransferOptionsOutputReference, "delete_objects_unique_in_sink").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteObjectsUniqueInSink", value)

    @builtins.property
    @jsii.member(jsii_name="overwriteObjectsAlreadyExistingInSink")
    def overwrite_objects_already_existing_in_sink(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwriteObjectsAlreadyExistingInSink"))

    @overwrite_objects_already_existing_in_sink.setter
    def overwrite_objects_already_existing_in_sink(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecTransferOptionsOutputReference, "overwrite_objects_already_existing_in_sink").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteObjectsAlreadyExistingInSink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageTransferJobTransferSpecTransferOptions]:
        return typing.cast(typing.Optional[StorageTransferJobTransferSpecTransferOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageTransferJobTransferSpecTransferOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageTransferJobTransferSpecTransferOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageTransferJob",
    "StorageTransferJobConfig",
    "StorageTransferJobSchedule",
    "StorageTransferJobScheduleOutputReference",
    "StorageTransferJobScheduleScheduleEndDate",
    "StorageTransferJobScheduleScheduleEndDateOutputReference",
    "StorageTransferJobScheduleScheduleStartDate",
    "StorageTransferJobScheduleScheduleStartDateOutputReference",
    "StorageTransferJobScheduleStartTimeOfDay",
    "StorageTransferJobScheduleStartTimeOfDayOutputReference",
    "StorageTransferJobTransferSpec",
    "StorageTransferJobTransferSpecAwsS3DataSource",
    "StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKey",
    "StorageTransferJobTransferSpecAwsS3DataSourceAwsAccessKeyOutputReference",
    "StorageTransferJobTransferSpecAwsS3DataSourceOutputReference",
    "StorageTransferJobTransferSpecAzureBlobStorageDataSource",
    "StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials",
    "StorageTransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsOutputReference",
    "StorageTransferJobTransferSpecAzureBlobStorageDataSourceOutputReference",
    "StorageTransferJobTransferSpecGcsDataSink",
    "StorageTransferJobTransferSpecGcsDataSinkOutputReference",
    "StorageTransferJobTransferSpecGcsDataSource",
    "StorageTransferJobTransferSpecGcsDataSourceOutputReference",
    "StorageTransferJobTransferSpecHttpDataSource",
    "StorageTransferJobTransferSpecHttpDataSourceOutputReference",
    "StorageTransferJobTransferSpecObjectConditions",
    "StorageTransferJobTransferSpecObjectConditionsOutputReference",
    "StorageTransferJobTransferSpecOutputReference",
    "StorageTransferJobTransferSpecPosixDataSink",
    "StorageTransferJobTransferSpecPosixDataSinkOutputReference",
    "StorageTransferJobTransferSpecPosixDataSource",
    "StorageTransferJobTransferSpecPosixDataSourceOutputReference",
    "StorageTransferJobTransferSpecTransferOptions",
    "StorageTransferJobTransferSpecTransferOptionsOutputReference",
]

publication.publish()
