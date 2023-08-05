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


class OsConfigPatchDeployment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeployment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment google_os_config_patch_deployment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        instance_filter: typing.Union["OsConfigPatchDeploymentInstanceFilter", typing.Dict[str, typing.Any]],
        patch_deployment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        one_time_schedule: typing.Optional[typing.Union["OsConfigPatchDeploymentOneTimeSchedule", typing.Dict[str, typing.Any]]] = None,
        patch_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        recurring_schedule: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringSchedule", typing.Dict[str, typing.Any]]] = None,
        rollout: typing.Optional[typing.Union["OsConfigPatchDeploymentRollout", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["OsConfigPatchDeploymentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment google_os_config_patch_deployment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_filter: instance_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_filter OsConfigPatchDeployment#instance_filter}
        :param patch_deployment_id: A name for the patch deployment in the project. When creating a name the following rules apply: Must contain only lowercase letters, numbers, and hyphens. Must start with a letter. Must be between 1-63 characters. Must end with a number or a letter. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_deployment_id OsConfigPatchDeployment#patch_deployment_id}
        :param description: Description of the patch deployment. Length of the description is limited to 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#description OsConfigPatchDeployment#description}
        :param duration: Duration of the patch. After the duration ends, the patch times out. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#duration OsConfigPatchDeployment#duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param one_time_schedule: one_time_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#one_time_schedule OsConfigPatchDeployment#one_time_schedule}
        :param patch_config: patch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_config OsConfigPatchDeployment#patch_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#project OsConfigPatchDeployment#project}.
        :param recurring_schedule: recurring_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#recurring_schedule OsConfigPatchDeployment#recurring_schedule}
        :param rollout: rollout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#rollout OsConfigPatchDeployment#rollout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#timeouts OsConfigPatchDeployment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeployment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OsConfigPatchDeploymentConfig(
            instance_filter=instance_filter,
            patch_deployment_id=patch_deployment_id,
            description=description,
            duration=duration,
            id=id,
            one_time_schedule=one_time_schedule,
            patch_config=patch_config,
            project=project,
            recurring_schedule=recurring_schedule,
            rollout=rollout,
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

    @jsii.member(jsii_name="putInstanceFilter")
    def put_instance_filter(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OsConfigPatchDeploymentInstanceFilterGroupLabels", typing.Dict[str, typing.Any]]]]] = None,
        instance_name_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: Target all VM instances in the project. If true, no other criteria is permitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#all OsConfigPatchDeployment#all}
        :param group_labels: group_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#group_labels OsConfigPatchDeployment#group_labels}
        :param instance_name_prefixes: Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_name_prefixes OsConfigPatchDeployment#instance_name_prefixes}
        :param instances: Targets any of the VM instances specified. Instances are specified by their URI in the 'form zones/{{zone}}/instances/{{instance_name}}', 'projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}', or 'https://www.googleapis.com/compute/v1/projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instances OsConfigPatchDeployment#instances}
        :param zones: Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zones OsConfigPatchDeployment#zones}
        '''
        value = OsConfigPatchDeploymentInstanceFilter(
            all=all,
            group_labels=group_labels,
            instance_name_prefixes=instance_name_prefixes,
            instances=instances,
            zones=zones,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceFilter", [value]))

    @jsii.member(jsii_name="putOneTimeSchedule")
    def put_one_time_schedule(self, *, execute_time: builtins.str) -> None:
        '''
        :param execute_time: The desired patch job execution time. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#execute_time OsConfigPatchDeployment#execute_time}
        '''
        value = OsConfigPatchDeploymentOneTimeSchedule(execute_time=execute_time)

        return typing.cast(None, jsii.invoke(self, "putOneTimeSchedule", [value]))

    @jsii.member(jsii_name="putPatchConfig")
    def put_patch_config(
        self,
        *,
        apt: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigApt", typing.Dict[str, typing.Any]]] = None,
        goo: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigGoo", typing.Dict[str, typing.Any]]] = None,
        mig_instances_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        post_step: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStep", typing.Dict[str, typing.Any]]] = None,
        pre_step: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStep", typing.Dict[str, typing.Any]]] = None,
        reboot_config: typing.Optional[builtins.str] = None,
        windows_update: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigWindowsUpdate", typing.Dict[str, typing.Any]]] = None,
        yum: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigYum", typing.Dict[str, typing.Any]]] = None,
        zypper: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigZypper", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param apt: apt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#apt OsConfigPatchDeployment#apt}
        :param goo: goo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#goo OsConfigPatchDeployment#goo}
        :param mig_instances_allowed: Allows the patch job to run on Managed instance groups (MIGs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mig_instances_allowed OsConfigPatchDeployment#mig_instances_allowed}
        :param post_step: post_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#post_step OsConfigPatchDeployment#post_step}
        :param pre_step: pre_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#pre_step OsConfigPatchDeployment#pre_step}
        :param reboot_config: Post-patch reboot settings. Possible values: ["DEFAULT", "ALWAYS", "NEVER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#reboot_config OsConfigPatchDeployment#reboot_config}
        :param windows_update: windows_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_update OsConfigPatchDeployment#windows_update}
        :param yum: yum block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#yum OsConfigPatchDeployment#yum}
        :param zypper: zypper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zypper OsConfigPatchDeployment#zypper}
        '''
        value = OsConfigPatchDeploymentPatchConfig(
            apt=apt,
            goo=goo,
            mig_instances_allowed=mig_instances_allowed,
            post_step=post_step,
            pre_step=pre_step,
            reboot_config=reboot_config,
            windows_update=windows_update,
            yum=yum,
            zypper=zypper,
        )

        return typing.cast(None, jsii.invoke(self, "putPatchConfig", [value]))

    @jsii.member(jsii_name="putRecurringSchedule")
    def put_recurring_schedule(
        self,
        *,
        time_of_day: typing.Union["OsConfigPatchDeploymentRecurringScheduleTimeOfDay", typing.Dict[str, typing.Any]],
        time_zone: typing.Union["OsConfigPatchDeploymentRecurringScheduleTimeZone", typing.Dict[str, typing.Any]],
        end_time: typing.Optional[builtins.str] = None,
        monthly: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringScheduleMonthly", typing.Dict[str, typing.Any]]] = None,
        start_time: typing.Optional[builtins.str] = None,
        weekly: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringScheduleWeekly", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param time_of_day: time_of_day block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_of_day OsConfigPatchDeployment#time_of_day}
        :param time_zone: time_zone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_zone OsConfigPatchDeployment#time_zone}
        :param end_time: The end time at which a recurring patch deployment schedule is no longer active. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#end_time OsConfigPatchDeployment#end_time}
        :param monthly: monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#monthly OsConfigPatchDeployment#monthly}
        :param start_time: The time that the recurring schedule becomes effective. Defaults to createTime of the patch deployment. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#start_time OsConfigPatchDeployment#start_time}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#weekly OsConfigPatchDeployment#weekly}
        '''
        value = OsConfigPatchDeploymentRecurringSchedule(
            time_of_day=time_of_day,
            time_zone=time_zone,
            end_time=end_time,
            monthly=monthly,
            start_time=start_time,
            weekly=weekly,
        )

        return typing.cast(None, jsii.invoke(self, "putRecurringSchedule", [value]))

    @jsii.member(jsii_name="putRollout")
    def put_rollout(
        self,
        *,
        disruption_budget: typing.Union["OsConfigPatchDeploymentRolloutDisruptionBudget", typing.Dict[str, typing.Any]],
        mode: builtins.str,
    ) -> None:
        '''
        :param disruption_budget: disruption_budget block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#disruption_budget OsConfigPatchDeployment#disruption_budget}
        :param mode: Mode of the patch rollout. Possible values: ["ZONE_BY_ZONE", "CONCURRENT_ZONES"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mode OsConfigPatchDeployment#mode}
        '''
        value = OsConfigPatchDeploymentRollout(
            disruption_budget=disruption_budget, mode=mode
        )

        return typing.cast(None, jsii.invoke(self, "putRollout", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#create OsConfigPatchDeployment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#delete OsConfigPatchDeployment#delete}.
        '''
        value = OsConfigPatchDeploymentTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOneTimeSchedule")
    def reset_one_time_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOneTimeSchedule", []))

    @jsii.member(jsii_name="resetPatchConfig")
    def reset_patch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatchConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRecurringSchedule")
    def reset_recurring_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurringSchedule", []))

    @jsii.member(jsii_name="resetRollout")
    def reset_rollout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollout", []))

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
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="instanceFilter")
    def instance_filter(self) -> "OsConfigPatchDeploymentInstanceFilterOutputReference":
        return typing.cast("OsConfigPatchDeploymentInstanceFilterOutputReference", jsii.get(self, "instanceFilter"))

    @builtins.property
    @jsii.member(jsii_name="lastExecuteTime")
    def last_execute_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastExecuteTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="oneTimeSchedule")
    def one_time_schedule(
        self,
    ) -> "OsConfigPatchDeploymentOneTimeScheduleOutputReference":
        return typing.cast("OsConfigPatchDeploymentOneTimeScheduleOutputReference", jsii.get(self, "oneTimeSchedule"))

    @builtins.property
    @jsii.member(jsii_name="patchConfig")
    def patch_config(self) -> "OsConfigPatchDeploymentPatchConfigOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigOutputReference", jsii.get(self, "patchConfig"))

    @builtins.property
    @jsii.member(jsii_name="recurringSchedule")
    def recurring_schedule(
        self,
    ) -> "OsConfigPatchDeploymentRecurringScheduleOutputReference":
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleOutputReference", jsii.get(self, "recurringSchedule"))

    @builtins.property
    @jsii.member(jsii_name="rollout")
    def rollout(self) -> "OsConfigPatchDeploymentRolloutOutputReference":
        return typing.cast("OsConfigPatchDeploymentRolloutOutputReference", jsii.get(self, "rollout"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "OsConfigPatchDeploymentTimeoutsOutputReference":
        return typing.cast("OsConfigPatchDeploymentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceFilterInput")
    def instance_filter_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentInstanceFilter"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentInstanceFilter"], jsii.get(self, "instanceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="oneTimeScheduleInput")
    def one_time_schedule_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentOneTimeSchedule"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentOneTimeSchedule"], jsii.get(self, "oneTimeScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="patchConfigInput")
    def patch_config_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfig"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfig"], jsii.get(self, "patchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="patchDeploymentIdInput")
    def patch_deployment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patchDeploymentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="recurringScheduleInput")
    def recurring_schedule_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringSchedule"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringSchedule"], jsii.get(self, "recurringScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="rolloutInput")
    def rollout_input(self) -> typing.Optional["OsConfigPatchDeploymentRollout"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRollout"], jsii.get(self, "rolloutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["OsConfigPatchDeploymentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["OsConfigPatchDeploymentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeployment, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeployment, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeployment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="patchDeploymentId")
    def patch_deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchDeploymentId"))

    @patch_deployment_id.setter
    def patch_deployment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeployment, "patch_deployment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchDeploymentId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeployment, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_filter": "instanceFilter",
        "patch_deployment_id": "patchDeploymentId",
        "description": "description",
        "duration": "duration",
        "id": "id",
        "one_time_schedule": "oneTimeSchedule",
        "patch_config": "patchConfig",
        "project": "project",
        "recurring_schedule": "recurringSchedule",
        "rollout": "rollout",
        "timeouts": "timeouts",
    },
)
class OsConfigPatchDeploymentConfig(cdktf.TerraformMetaArguments):
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
        instance_filter: typing.Union["OsConfigPatchDeploymentInstanceFilter", typing.Dict[str, typing.Any]],
        patch_deployment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        one_time_schedule: typing.Optional[typing.Union["OsConfigPatchDeploymentOneTimeSchedule", typing.Dict[str, typing.Any]]] = None,
        patch_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        recurring_schedule: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringSchedule", typing.Dict[str, typing.Any]]] = None,
        rollout: typing.Optional[typing.Union["OsConfigPatchDeploymentRollout", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["OsConfigPatchDeploymentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance_filter: instance_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_filter OsConfigPatchDeployment#instance_filter}
        :param patch_deployment_id: A name for the patch deployment in the project. When creating a name the following rules apply: Must contain only lowercase letters, numbers, and hyphens. Must start with a letter. Must be between 1-63 characters. Must end with a number or a letter. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_deployment_id OsConfigPatchDeployment#patch_deployment_id}
        :param description: Description of the patch deployment. Length of the description is limited to 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#description OsConfigPatchDeployment#description}
        :param duration: Duration of the patch. After the duration ends, the patch times out. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#duration OsConfigPatchDeployment#duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param one_time_schedule: one_time_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#one_time_schedule OsConfigPatchDeployment#one_time_schedule}
        :param patch_config: patch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_config OsConfigPatchDeployment#patch_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#project OsConfigPatchDeployment#project}.
        :param recurring_schedule: recurring_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#recurring_schedule OsConfigPatchDeployment#recurring_schedule}
        :param rollout: rollout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#rollout OsConfigPatchDeployment#rollout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#timeouts OsConfigPatchDeployment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(instance_filter, dict):
            instance_filter = OsConfigPatchDeploymentInstanceFilter(**instance_filter)
        if isinstance(one_time_schedule, dict):
            one_time_schedule = OsConfigPatchDeploymentOneTimeSchedule(**one_time_schedule)
        if isinstance(patch_config, dict):
            patch_config = OsConfigPatchDeploymentPatchConfig(**patch_config)
        if isinstance(recurring_schedule, dict):
            recurring_schedule = OsConfigPatchDeploymentRecurringSchedule(**recurring_schedule)
        if isinstance(rollout, dict):
            rollout = OsConfigPatchDeploymentRollout(**rollout)
        if isinstance(timeouts, dict):
            timeouts = OsConfigPatchDeploymentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_filter", value=instance_filter, expected_type=type_hints["instance_filter"])
            check_type(argname="argument patch_deployment_id", value=patch_deployment_id, expected_type=type_hints["patch_deployment_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument one_time_schedule", value=one_time_schedule, expected_type=type_hints["one_time_schedule"])
            check_type(argname="argument patch_config", value=patch_config, expected_type=type_hints["patch_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument recurring_schedule", value=recurring_schedule, expected_type=type_hints["recurring_schedule"])
            check_type(argname="argument rollout", value=rollout, expected_type=type_hints["rollout"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_filter": instance_filter,
            "patch_deployment_id": patch_deployment_id,
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
        if description is not None:
            self._values["description"] = description
        if duration is not None:
            self._values["duration"] = duration
        if id is not None:
            self._values["id"] = id
        if one_time_schedule is not None:
            self._values["one_time_schedule"] = one_time_schedule
        if patch_config is not None:
            self._values["patch_config"] = patch_config
        if project is not None:
            self._values["project"] = project
        if recurring_schedule is not None:
            self._values["recurring_schedule"] = recurring_schedule
        if rollout is not None:
            self._values["rollout"] = rollout
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
    def instance_filter(self) -> "OsConfigPatchDeploymentInstanceFilter":
        '''instance_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_filter OsConfigPatchDeployment#instance_filter}
        '''
        result = self._values.get("instance_filter")
        assert result is not None, "Required property 'instance_filter' is missing"
        return typing.cast("OsConfigPatchDeploymentInstanceFilter", result)

    @builtins.property
    def patch_deployment_id(self) -> builtins.str:
        '''A name for the patch deployment in the project.

        When creating a name the following rules apply:
        Must contain only lowercase letters, numbers, and hyphens.
        Must start with a letter.
        Must be between 1-63 characters.
        Must end with a number or a letter.
        Must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_deployment_id OsConfigPatchDeployment#patch_deployment_id}
        '''
        result = self._values.get("patch_deployment_id")
        assert result is not None, "Required property 'patch_deployment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the patch deployment. Length of the description is limited to 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#description OsConfigPatchDeployment#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Duration of the patch.

        After the duration ends, the patch times out.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#duration OsConfigPatchDeployment#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def one_time_schedule(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentOneTimeSchedule"]:
        '''one_time_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#one_time_schedule OsConfigPatchDeployment#one_time_schedule}
        '''
        result = self._values.get("one_time_schedule")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentOneTimeSchedule"], result)

    @builtins.property
    def patch_config(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfig"]:
        '''patch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#patch_config OsConfigPatchDeployment#patch_config}
        '''
        result = self._values.get("patch_config")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#project OsConfigPatchDeployment#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recurring_schedule(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringSchedule"]:
        '''recurring_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#recurring_schedule OsConfigPatchDeployment#recurring_schedule}
        '''
        result = self._values.get("recurring_schedule")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringSchedule"], result)

    @builtins.property
    def rollout(self) -> typing.Optional["OsConfigPatchDeploymentRollout"]:
        '''rollout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#rollout OsConfigPatchDeployment#rollout}
        '''
        result = self._values.get("rollout")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRollout"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["OsConfigPatchDeploymentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#timeouts OsConfigPatchDeployment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentInstanceFilter",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "group_labels": "groupLabels",
        "instance_name_prefixes": "instanceNamePrefixes",
        "instances": "instances",
        "zones": "zones",
    },
)
class OsConfigPatchDeploymentInstanceFilter:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OsConfigPatchDeploymentInstanceFilterGroupLabels", typing.Dict[str, typing.Any]]]]] = None,
        instance_name_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: Target all VM instances in the project. If true, no other criteria is permitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#all OsConfigPatchDeployment#all}
        :param group_labels: group_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#group_labels OsConfigPatchDeployment#group_labels}
        :param instance_name_prefixes: Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_name_prefixes OsConfigPatchDeployment#instance_name_prefixes}
        :param instances: Targets any of the VM instances specified. Instances are specified by their URI in the 'form zones/{{zone}}/instances/{{instance_name}}', 'projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}', or 'https://www.googleapis.com/compute/v1/projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instances OsConfigPatchDeployment#instances}
        :param zones: Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zones OsConfigPatchDeployment#zones}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilter.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument group_labels", value=group_labels, expected_type=type_hints["group_labels"])
            check_type(argname="argument instance_name_prefixes", value=instance_name_prefixes, expected_type=type_hints["instance_name_prefixes"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if group_labels is not None:
            self._values["group_labels"] = group_labels
        if instance_name_prefixes is not None:
            self._values["instance_name_prefixes"] = instance_name_prefixes
        if instances is not None:
            self._values["instances"] = instances
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def all(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Target all VM instances in the project. If true, no other criteria is permitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#all OsConfigPatchDeployment#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def group_labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OsConfigPatchDeploymentInstanceFilterGroupLabels"]]]:
        '''group_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#group_labels OsConfigPatchDeployment#group_labels}
        '''
        result = self._values.get("group_labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OsConfigPatchDeploymentInstanceFilterGroupLabels"]]], result)

    @builtins.property
    def instance_name_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets VMs whose name starts with one of these prefixes.

        Similar to labels, this is another way to group
        VMs when targeting configs, for example prefix="prod-".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instance_name_prefixes OsConfigPatchDeployment#instance_name_prefixes}
        '''
        result = self._values.get("instance_name_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets any of the VM instances specified. Instances are specified by their URI in the 'form zones/{{zone}}/instances/{{instance_name}}', 'projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}', or 'https://www.googleapis.com/compute/v1/projects/{{project_id}}/zones/{{zone}}/instances/{{instance_name}}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#instances OsConfigPatchDeployment#instances}
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zones OsConfigPatchDeployment#zones}
        '''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentInstanceFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentInstanceFilterGroupLabels",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class OsConfigPatchDeploymentInstanceFilterGroupLabels:
    def __init__(self, *, labels: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param labels: Compute Engine instance labels that must be present for a VM instance to be targeted by this filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#labels OsConfigPatchDeployment#labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterGroupLabels.__init__)
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "labels": labels,
        }

    @builtins.property
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Compute Engine instance labels that must be present for a VM instance to be targeted by this filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#labels OsConfigPatchDeployment#labels}
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentInstanceFilterGroupLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentInstanceFilterGroupLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentInstanceFilterGroupLabelsList",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterGroupLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterGroupLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OsConfigPatchDeploymentInstanceFilterGroupLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OsConfigPatchDeploymentInstanceFilterGroupLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OsConfigPatchDeploymentInstanceFilterGroupLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OsConfigPatchDeploymentInstanceFilterGroupLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OsConfigPatchDeploymentInstanceFilterGroupLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OsConfigPatchDeploymentInstanceFilterGroupLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentInstanceFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentInstanceFilterOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGroupLabels")
    def put_group_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OsConfigPatchDeploymentInstanceFilterGroupLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentInstanceFilterOutputReference.put_group_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGroupLabels", [value]))

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetGroupLabels")
    def reset_group_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupLabels", []))

    @jsii.member(jsii_name="resetInstanceNamePrefixes")
    def reset_instance_name_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceNamePrefixes", []))

    @jsii.member(jsii_name="resetInstances")
    def reset_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstances", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="groupLabels")
    def group_labels(self) -> OsConfigPatchDeploymentInstanceFilterGroupLabelsList:
        return typing.cast(OsConfigPatchDeploymentInstanceFilterGroupLabelsList, jsii.get(self, "groupLabels"))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="groupLabelsInput")
    def group_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OsConfigPatchDeploymentInstanceFilterGroupLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OsConfigPatchDeploymentInstanceFilterGroupLabels]]], jsii.get(self, "groupLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceNamePrefixesInput")
    def instance_name_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceNamePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "all"))

    @all.setter
    def all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterOutputReference, "all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="instanceNamePrefixes")
    def instance_name_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNamePrefixes"))

    @instance_name_prefixes.setter
    def instance_name_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterOutputReference, "instance_name_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceNamePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterOutputReference, "instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterOutputReference, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentInstanceFilter]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentInstanceFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentInstanceFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentInstanceFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentOneTimeSchedule",
    jsii_struct_bases=[],
    name_mapping={"execute_time": "executeTime"},
)
class OsConfigPatchDeploymentOneTimeSchedule:
    def __init__(self, *, execute_time: builtins.str) -> None:
        '''
        :param execute_time: The desired patch job execution time. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#execute_time OsConfigPatchDeployment#execute_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentOneTimeSchedule.__init__)
            check_type(argname="argument execute_time", value=execute_time, expected_type=type_hints["execute_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "execute_time": execute_time,
        }

    @builtins.property
    def execute_time(self) -> builtins.str:
        '''The desired patch job execution time. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#execute_time OsConfigPatchDeployment#execute_time}
        '''
        result = self._values.get("execute_time")
        assert result is not None, "Required property 'execute_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentOneTimeSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentOneTimeScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentOneTimeScheduleOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentOneTimeScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="executeTimeInput")
    def execute_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executeTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="executeTime")
    def execute_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executeTime"))

    @execute_time.setter
    def execute_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentOneTimeScheduleOutputReference, "execute_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executeTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentOneTimeSchedule]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentOneTimeSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentOneTimeSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentOneTimeScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "apt": "apt",
        "goo": "goo",
        "mig_instances_allowed": "migInstancesAllowed",
        "post_step": "postStep",
        "pre_step": "preStep",
        "reboot_config": "rebootConfig",
        "windows_update": "windowsUpdate",
        "yum": "yum",
        "zypper": "zypper",
    },
)
class OsConfigPatchDeploymentPatchConfig:
    def __init__(
        self,
        *,
        apt: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigApt", typing.Dict[str, typing.Any]]] = None,
        goo: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigGoo", typing.Dict[str, typing.Any]]] = None,
        mig_instances_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        post_step: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStep", typing.Dict[str, typing.Any]]] = None,
        pre_step: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStep", typing.Dict[str, typing.Any]]] = None,
        reboot_config: typing.Optional[builtins.str] = None,
        windows_update: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigWindowsUpdate", typing.Dict[str, typing.Any]]] = None,
        yum: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigYum", typing.Dict[str, typing.Any]]] = None,
        zypper: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigZypper", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param apt: apt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#apt OsConfigPatchDeployment#apt}
        :param goo: goo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#goo OsConfigPatchDeployment#goo}
        :param mig_instances_allowed: Allows the patch job to run on Managed instance groups (MIGs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mig_instances_allowed OsConfigPatchDeployment#mig_instances_allowed}
        :param post_step: post_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#post_step OsConfigPatchDeployment#post_step}
        :param pre_step: pre_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#pre_step OsConfigPatchDeployment#pre_step}
        :param reboot_config: Post-patch reboot settings. Possible values: ["DEFAULT", "ALWAYS", "NEVER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#reboot_config OsConfigPatchDeployment#reboot_config}
        :param windows_update: windows_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_update OsConfigPatchDeployment#windows_update}
        :param yum: yum block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#yum OsConfigPatchDeployment#yum}
        :param zypper: zypper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zypper OsConfigPatchDeployment#zypper}
        '''
        if isinstance(apt, dict):
            apt = OsConfigPatchDeploymentPatchConfigApt(**apt)
        if isinstance(goo, dict):
            goo = OsConfigPatchDeploymentPatchConfigGoo(**goo)
        if isinstance(post_step, dict):
            post_step = OsConfigPatchDeploymentPatchConfigPostStep(**post_step)
        if isinstance(pre_step, dict):
            pre_step = OsConfigPatchDeploymentPatchConfigPreStep(**pre_step)
        if isinstance(windows_update, dict):
            windows_update = OsConfigPatchDeploymentPatchConfigWindowsUpdate(**windows_update)
        if isinstance(yum, dict):
            yum = OsConfigPatchDeploymentPatchConfigYum(**yum)
        if isinstance(zypper, dict):
            zypper = OsConfigPatchDeploymentPatchConfigZypper(**zypper)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfig.__init__)
            check_type(argname="argument apt", value=apt, expected_type=type_hints["apt"])
            check_type(argname="argument goo", value=goo, expected_type=type_hints["goo"])
            check_type(argname="argument mig_instances_allowed", value=mig_instances_allowed, expected_type=type_hints["mig_instances_allowed"])
            check_type(argname="argument post_step", value=post_step, expected_type=type_hints["post_step"])
            check_type(argname="argument pre_step", value=pre_step, expected_type=type_hints["pre_step"])
            check_type(argname="argument reboot_config", value=reboot_config, expected_type=type_hints["reboot_config"])
            check_type(argname="argument windows_update", value=windows_update, expected_type=type_hints["windows_update"])
            check_type(argname="argument yum", value=yum, expected_type=type_hints["yum"])
            check_type(argname="argument zypper", value=zypper, expected_type=type_hints["zypper"])
        self._values: typing.Dict[str, typing.Any] = {}
        if apt is not None:
            self._values["apt"] = apt
        if goo is not None:
            self._values["goo"] = goo
        if mig_instances_allowed is not None:
            self._values["mig_instances_allowed"] = mig_instances_allowed
        if post_step is not None:
            self._values["post_step"] = post_step
        if pre_step is not None:
            self._values["pre_step"] = pre_step
        if reboot_config is not None:
            self._values["reboot_config"] = reboot_config
        if windows_update is not None:
            self._values["windows_update"] = windows_update
        if yum is not None:
            self._values["yum"] = yum
        if zypper is not None:
            self._values["zypper"] = zypper

    @builtins.property
    def apt(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigApt"]:
        '''apt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#apt OsConfigPatchDeployment#apt}
        '''
        result = self._values.get("apt")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigApt"], result)

    @builtins.property
    def goo(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigGoo"]:
        '''goo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#goo OsConfigPatchDeployment#goo}
        '''
        result = self._values.get("goo")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigGoo"], result)

    @builtins.property
    def mig_instances_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows the patch job to run on Managed instance groups (MIGs).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mig_instances_allowed OsConfigPatchDeployment#mig_instances_allowed}
        '''
        result = self._values.get("mig_instances_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def post_step(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStep"]:
        '''post_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#post_step OsConfigPatchDeployment#post_step}
        '''
        result = self._values.get("post_step")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStep"], result)

    @builtins.property
    def pre_step(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStep"]:
        '''pre_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#pre_step OsConfigPatchDeployment#pre_step}
        '''
        result = self._values.get("pre_step")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStep"], result)

    @builtins.property
    def reboot_config(self) -> typing.Optional[builtins.str]:
        '''Post-patch reboot settings. Possible values: ["DEFAULT", "ALWAYS", "NEVER"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#reboot_config OsConfigPatchDeployment#reboot_config}
        '''
        result = self._values.get("reboot_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def windows_update(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigWindowsUpdate"]:
        '''windows_update block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_update OsConfigPatchDeployment#windows_update}
        '''
        result = self._values.get("windows_update")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigWindowsUpdate"], result)

    @builtins.property
    def yum(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigYum"]:
        '''yum block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#yum OsConfigPatchDeployment#yum}
        '''
        result = self._values.get("yum")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigYum"], result)

    @builtins.property
    def zypper(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigZypper"]:
        '''zypper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#zypper OsConfigPatchDeployment#zypper}
        '''
        result = self._values.get("zypper")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigZypper"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigApt",
    jsii_struct_bases=[],
    name_mapping={
        "excludes": "excludes",
        "exclusive_packages": "exclusivePackages",
        "type": "type",
    },
)
class OsConfigPatchDeploymentPatchConfigApt:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param excludes: List of packages to exclude from update. These packages will be excluded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_packages: An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        :param type: By changing the type to DIST, the patching is performed using apt-get dist-upgrade instead. Possible values: ["DIST", "UPGRADE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#type OsConfigPatchDeployment#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigApt.__init__)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument exclusive_packages", value=exclusive_packages, expected_type=type_hints["exclusive_packages"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if exclusive_packages is not None:
            self._values["exclusive_packages"] = exclusive_packages
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of packages to exclude from update. These packages will be excluded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclusive_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An exclusive list of packages to be updated.

        These are the only packages that will be updated.
        If these packages are not installed, they will be ignored. This field cannot be specified with
        any other patch configuration fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        '''
        result = self._values.get("exclusive_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''By changing the type to DIST, the patching is performed using apt-get dist-upgrade instead. Possible values: ["DIST", "UPGRADE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#type OsConfigPatchDeployment#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigApt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigAptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigAptOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigAptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetExclusivePackages")
    def reset_exclusive_packages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusivePackages", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusivePackagesInput")
    def exclusive_packages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusivePackagesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigAptOutputReference, "excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="exclusivePackages")
    def exclusive_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusivePackages"))

    @exclusive_packages.setter
    def exclusive_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigAptOutputReference, "exclusive_packages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusivePackages", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigAptOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfigApt]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigApt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigApt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigAptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigGoo",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class OsConfigPatchDeploymentPatchConfigGoo:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: goo update settings. Use this setting to override the default goo patch rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#enabled OsConfigPatchDeployment#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigGoo.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''goo update settings. Use this setting to override the default goo patch rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#enabled OsConfigPatchDeployment#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigGoo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigGooOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigGooOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigGooOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigGooOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfigGoo]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigGoo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigGoo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigGooOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApt")
    def put_apt(
        self,
        *,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param excludes: List of packages to exclude from update. These packages will be excluded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_packages: An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        :param type: By changing the type to DIST, the patching is performed using apt-get dist-upgrade instead. Possible values: ["DIST", "UPGRADE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#type OsConfigPatchDeployment#type}
        '''
        value = OsConfigPatchDeploymentPatchConfigApt(
            excludes=excludes, exclusive_packages=exclusive_packages, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putApt", [value]))

    @jsii.member(jsii_name="putGoo")
    def put_goo(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: goo update settings. Use this setting to override the default goo patch rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#enabled OsConfigPatchDeployment#enabled}
        '''
        value = OsConfigPatchDeploymentPatchConfigGoo(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGoo", [value]))

    @jsii.member(jsii_name="putPostStep")
    def put_post_step(
        self,
        *,
        linux_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig", typing.Dict[str, typing.Any]]] = None,
        windows_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param linux_exec_step_config: linux_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        :param windows_exec_step_config: windows_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        value = OsConfigPatchDeploymentPatchConfigPostStep(
            linux_exec_step_config=linux_exec_step_config,
            windows_exec_step_config=windows_exec_step_config,
        )

        return typing.cast(None, jsii.invoke(self, "putPostStep", [value]))

    @jsii.member(jsii_name="putPreStep")
    def put_pre_step(
        self,
        *,
        linux_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig", typing.Dict[str, typing.Any]]] = None,
        windows_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param linux_exec_step_config: linux_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        :param windows_exec_step_config: windows_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        value = OsConfigPatchDeploymentPatchConfigPreStep(
            linux_exec_step_config=linux_exec_step_config,
            windows_exec_step_config=windows_exec_step_config,
        )

        return typing.cast(None, jsii.invoke(self, "putPreStep", [value]))

    @jsii.member(jsii_name="putWindowsUpdate")
    def put_windows_update(
        self,
        *,
        classifications: typing.Optional[typing.Sequence[builtins.str]] = None,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param classifications: Only apply updates of these windows update classifications. If empty, all updates are applied. Possible values: ["CRITICAL", "SECURITY", "DEFINITION", "DRIVER", "FEATURE_PACK", "SERVICE_PACK", "TOOL", "UPDATE_ROLLUP", "UPDATE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#classifications OsConfigPatchDeployment#classifications}
        :param excludes: List of KBs to exclude from update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_patches: An exclusive list of kbs to be updated. These are the only patches that will be updated. This field must not be used with other patch configurations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        '''
        value = OsConfigPatchDeploymentPatchConfigWindowsUpdate(
            classifications=classifications,
            excludes=excludes,
            exclusive_patches=exclusive_patches,
        )

        return typing.cast(None, jsii.invoke(self, "putWindowsUpdate", [value]))

    @jsii.member(jsii_name="putYum")
    def put_yum(
        self,
        *,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        minimal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param excludes: List of packages to exclude from update. These packages will be excluded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_packages: An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        :param minimal: Will cause patch to run yum update-minimal instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minimal OsConfigPatchDeployment#minimal}
        :param security: Adds the --security flag to yum update. Not supported on all platforms. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#security OsConfigPatchDeployment#security}
        '''
        value = OsConfigPatchDeploymentPatchConfigYum(
            excludes=excludes,
            exclusive_packages=exclusive_packages,
            minimal=minimal,
            security=security,
        )

        return typing.cast(None, jsii.invoke(self, "putYum", [value]))

    @jsii.member(jsii_name="putZypper")
    def put_zypper(
        self,
        *,
        categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        severities: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_optional: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        with_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param categories: Install only patches with these categories. Common categories include security, recommended, and feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#categories OsConfigPatchDeployment#categories}
        :param excludes: List of packages to exclude from update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_patches: An exclusive list of patches to be updated. These are the only patches that will be installed using 'zypper patch patch:' command. This field must not be used with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        :param severities: Install only patches with these severities. Common severities include critical, important, moderate, and low. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#severities OsConfigPatchDeployment#severities}
        :param with_optional: Adds the --with-optional flag to zypper patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_optional OsConfigPatchDeployment#with_optional}
        :param with_update: Adds the --with-update flag, to zypper patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_update OsConfigPatchDeployment#with_update}
        '''
        value = OsConfigPatchDeploymentPatchConfigZypper(
            categories=categories,
            excludes=excludes,
            exclusive_patches=exclusive_patches,
            severities=severities,
            with_optional=with_optional,
            with_update=with_update,
        )

        return typing.cast(None, jsii.invoke(self, "putZypper", [value]))

    @jsii.member(jsii_name="resetApt")
    def reset_apt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApt", []))

    @jsii.member(jsii_name="resetGoo")
    def reset_goo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoo", []))

    @jsii.member(jsii_name="resetMigInstancesAllowed")
    def reset_mig_instances_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMigInstancesAllowed", []))

    @jsii.member(jsii_name="resetPostStep")
    def reset_post_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostStep", []))

    @jsii.member(jsii_name="resetPreStep")
    def reset_pre_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreStep", []))

    @jsii.member(jsii_name="resetRebootConfig")
    def reset_reboot_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRebootConfig", []))

    @jsii.member(jsii_name="resetWindowsUpdate")
    def reset_windows_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsUpdate", []))

    @jsii.member(jsii_name="resetYum")
    def reset_yum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYum", []))

    @jsii.member(jsii_name="resetZypper")
    def reset_zypper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZypper", []))

    @builtins.property
    @jsii.member(jsii_name="apt")
    def apt(self) -> OsConfigPatchDeploymentPatchConfigAptOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigAptOutputReference, jsii.get(self, "apt"))

    @builtins.property
    @jsii.member(jsii_name="goo")
    def goo(self) -> OsConfigPatchDeploymentPatchConfigGooOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigGooOutputReference, jsii.get(self, "goo"))

    @builtins.property
    @jsii.member(jsii_name="postStep")
    def post_step(self) -> "OsConfigPatchDeploymentPatchConfigPostStepOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigPostStepOutputReference", jsii.get(self, "postStep"))

    @builtins.property
    @jsii.member(jsii_name="preStep")
    def pre_step(self) -> "OsConfigPatchDeploymentPatchConfigPreStepOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigPreStepOutputReference", jsii.get(self, "preStep"))

    @builtins.property
    @jsii.member(jsii_name="windowsUpdate")
    def windows_update(
        self,
    ) -> "OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference", jsii.get(self, "windowsUpdate"))

    @builtins.property
    @jsii.member(jsii_name="yum")
    def yum(self) -> "OsConfigPatchDeploymentPatchConfigYumOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigYumOutputReference", jsii.get(self, "yum"))

    @builtins.property
    @jsii.member(jsii_name="zypper")
    def zypper(self) -> "OsConfigPatchDeploymentPatchConfigZypperOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigZypperOutputReference", jsii.get(self, "zypper"))

    @builtins.property
    @jsii.member(jsii_name="aptInput")
    def apt_input(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfigApt]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigApt], jsii.get(self, "aptInput"))

    @builtins.property
    @jsii.member(jsii_name="gooInput")
    def goo_input(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfigGoo]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigGoo], jsii.get(self, "gooInput"))

    @builtins.property
    @jsii.member(jsii_name="migInstancesAllowedInput")
    def mig_instances_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "migInstancesAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="postStepInput")
    def post_step_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStep"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStep"], jsii.get(self, "postStepInput"))

    @builtins.property
    @jsii.member(jsii_name="preStepInput")
    def pre_step_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStep"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStep"], jsii.get(self, "preStepInput"))

    @builtins.property
    @jsii.member(jsii_name="rebootConfigInput")
    def reboot_config_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rebootConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsUpdateInput")
    def windows_update_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigWindowsUpdate"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigWindowsUpdate"], jsii.get(self, "windowsUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="yumInput")
    def yum_input(self) -> typing.Optional["OsConfigPatchDeploymentPatchConfigYum"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigYum"], jsii.get(self, "yumInput"))

    @builtins.property
    @jsii.member(jsii_name="zypperInput")
    def zypper_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigZypper"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigZypper"], jsii.get(self, "zypperInput"))

    @builtins.property
    @jsii.member(jsii_name="migInstancesAllowed")
    def mig_instances_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "migInstancesAllowed"))

    @mig_instances_allowed.setter
    def mig_instances_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigOutputReference, "mig_instances_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migInstancesAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="rebootConfig")
    def reboot_config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rebootConfig"))

    @reboot_config.setter
    def reboot_config(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigOutputReference, "reboot_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rebootConfig", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStep",
    jsii_struct_bases=[],
    name_mapping={
        "linux_exec_step_config": "linuxExecStepConfig",
        "windows_exec_step_config": "windowsExecStepConfig",
    },
)
class OsConfigPatchDeploymentPatchConfigPostStep:
    def __init__(
        self,
        *,
        linux_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig", typing.Dict[str, typing.Any]]] = None,
        windows_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param linux_exec_step_config: linux_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        :param windows_exec_step_config: windows_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        if isinstance(linux_exec_step_config, dict):
            linux_exec_step_config = OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig(**linux_exec_step_config)
        if isinstance(windows_exec_step_config, dict):
            windows_exec_step_config = OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig(**windows_exec_step_config)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStep.__init__)
            check_type(argname="argument linux_exec_step_config", value=linux_exec_step_config, expected_type=type_hints["linux_exec_step_config"])
            check_type(argname="argument windows_exec_step_config", value=windows_exec_step_config, expected_type=type_hints["windows_exec_step_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if linux_exec_step_config is not None:
            self._values["linux_exec_step_config"] = linux_exec_step_config
        if windows_exec_step_config is not None:
            self._values["windows_exec_step_config"] = windows_exec_step_config

    @builtins.property
    def linux_exec_step_config(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig"]:
        '''linux_exec_step_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        '''
        result = self._values.get("linux_exec_step_config")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig"], result)

    @builtins.property
    def windows_exec_step_config(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig"]:
        '''windows_exec_step_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        result = self._values.get("windows_exec_step_config")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPostStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_success_codes": "allowedSuccessCodes",
        "gcs_object": "gcsObject",
        "interpreter": "interpreter",
        "local_path": "localPath",
    },
)
class OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig:
    def __init__(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        if isinstance(gcs_object, dict):
            gcs_object = OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject(**gcs_object)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig.__init__)
            check_type(argname="argument allowed_success_codes", value=allowed_success_codes, expected_type=type_hints["allowed_success_codes"])
            check_type(argname="argument gcs_object", value=gcs_object, expected_type=type_hints["gcs_object"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_success_codes is not None:
            self._values["allowed_success_codes"] = allowed_success_codes
        if gcs_object is not None:
            self._values["gcs_object"] = gcs_object
        if interpreter is not None:
            self._values["interpreter"] = interpreter
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_success_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Defaults to [0]. A list of possible return values that the execution can return to indicate a success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        '''
        result = self._values.get("allowed_success_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def gcs_object(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject"]:
        '''gcs_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        '''
        result = self._values.get("gcs_object")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject"], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script will
        be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''An absolute path to the executable on the VM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "generation_number": "generationNumber",
        "object": "object",
    },
)
class OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument generation_number", value=generation_number, expected_type=type_hints["generation_number"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "generation_number": generation_number,
            "object": object,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Bucket of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def generation_number(self) -> builtins.str:
        '''Generation number of the Cloud Storage object.

        This is used to ensure that the ExecStep specified by this PatchJob does not change.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        '''
        result = self._values.get("generation_number")
        assert result is not None, "Required property 'generation_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Name of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationNumberInput")
    def generation_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generationNumber")
    def generation_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generationNumber"))

    @generation_number.setter
    def generation_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference, "generation_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generationNumber", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcsObject")
    def put_gcs_object(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        value = OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject(
            bucket=bucket, generation_number=generation_number, object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGcsObject", [value]))

    @jsii.member(jsii_name="resetAllowedSuccessCodes")
    def reset_allowed_success_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedSuccessCodes", []))

    @jsii.member(jsii_name="resetGcsObject")
    def reset_gcs_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsObject", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="gcsObject")
    def gcs_object(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference, jsii.get(self, "gcsObject"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodesInput")
    def allowed_success_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedSuccessCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsObjectInput")
    def gcs_object_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject], jsii.get(self, "gcsObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodes")
    def allowed_success_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedSuccessCodes"))

    @allowed_success_codes.setter
    def allowed_success_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference, "allowed_success_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedSuccessCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPostStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLinuxExecStepConfig")
    def put_linux_exec_step_config(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject, typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        value = OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig(
            allowed_success_codes=allowed_success_codes,
            gcs_object=gcs_object,
            interpreter=interpreter,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putLinuxExecStepConfig", [value]))

    @jsii.member(jsii_name="putWindowsExecStepConfig")
    def put_windows_exec_step_config(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        value = OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig(
            allowed_success_codes=allowed_success_codes,
            gcs_object=gcs_object,
            interpreter=interpreter,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putWindowsExecStepConfig", [value]))

    @jsii.member(jsii_name="resetLinuxExecStepConfig")
    def reset_linux_exec_step_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxExecStepConfig", []))

    @jsii.member(jsii_name="resetWindowsExecStepConfig")
    def reset_windows_exec_step_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsExecStepConfig", []))

    @builtins.property
    @jsii.member(jsii_name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference, jsii.get(self, "linuxExecStepConfig"))

    @builtins.property
    @jsii.member(jsii_name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference", jsii.get(self, "windowsExecStepConfig"))

    @builtins.property
    @jsii.member(jsii_name="linuxExecStepConfigInput")
    def linux_exec_step_config_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig], jsii.get(self, "linuxExecStepConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsExecStepConfigInput")
    def windows_exec_step_config_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig"], jsii.get(self, "windowsExecStepConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStep]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStep], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPostStep],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_success_codes": "allowedSuccessCodes",
        "gcs_object": "gcsObject",
        "interpreter": "interpreter",
        "local_path": "localPath",
    },
)
class OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig:
    def __init__(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        if isinstance(gcs_object, dict):
            gcs_object = OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject(**gcs_object)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig.__init__)
            check_type(argname="argument allowed_success_codes", value=allowed_success_codes, expected_type=type_hints["allowed_success_codes"])
            check_type(argname="argument gcs_object", value=gcs_object, expected_type=type_hints["gcs_object"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_success_codes is not None:
            self._values["allowed_success_codes"] = allowed_success_codes
        if gcs_object is not None:
            self._values["gcs_object"] = gcs_object
        if interpreter is not None:
            self._values["interpreter"] = interpreter
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_success_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Defaults to [0]. A list of possible return values that the execution can return to indicate a success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        '''
        result = self._values.get("allowed_success_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def gcs_object(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject"]:
        '''gcs_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        '''
        result = self._values.get("gcs_object")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject"], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script will
        be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''An absolute path to the executable on the VM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "generation_number": "generationNumber",
        "object": "object",
    },
)
class OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument generation_number", value=generation_number, expected_type=type_hints["generation_number"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "generation_number": generation_number,
            "object": object,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Bucket of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def generation_number(self) -> builtins.str:
        '''Generation number of the Cloud Storage object.

        This is used to ensure that the ExecStep specified by this PatchJob does not change.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        '''
        result = self._values.get("generation_number")
        assert result is not None, "Required property 'generation_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Name of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationNumberInput")
    def generation_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generationNumber")
    def generation_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generationNumber"))

    @generation_number.setter
    def generation_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference, "generation_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generationNumber", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcsObject")
    def put_gcs_object(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        value = OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject(
            bucket=bucket, generation_number=generation_number, object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGcsObject", [value]))

    @jsii.member(jsii_name="resetAllowedSuccessCodes")
    def reset_allowed_success_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedSuccessCodes", []))

    @jsii.member(jsii_name="resetGcsObject")
    def reset_gcs_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsObject", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="gcsObject")
    def gcs_object(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference, jsii.get(self, "gcsObject"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodesInput")
    def allowed_success_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedSuccessCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsObjectInput")
    def gcs_object_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject], jsii.get(self, "gcsObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodes")
    def allowed_success_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedSuccessCodes"))

    @allowed_success_codes.setter
    def allowed_success_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference, "allowed_success_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedSuccessCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStep",
    jsii_struct_bases=[],
    name_mapping={
        "linux_exec_step_config": "linuxExecStepConfig",
        "windows_exec_step_config": "windowsExecStepConfig",
    },
)
class OsConfigPatchDeploymentPatchConfigPreStep:
    def __init__(
        self,
        *,
        linux_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig", typing.Dict[str, typing.Any]]] = None,
        windows_exec_step_config: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param linux_exec_step_config: linux_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        :param windows_exec_step_config: windows_exec_step_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        if isinstance(linux_exec_step_config, dict):
            linux_exec_step_config = OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig(**linux_exec_step_config)
        if isinstance(windows_exec_step_config, dict):
            windows_exec_step_config = OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig(**windows_exec_step_config)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStep.__init__)
            check_type(argname="argument linux_exec_step_config", value=linux_exec_step_config, expected_type=type_hints["linux_exec_step_config"])
            check_type(argname="argument windows_exec_step_config", value=windows_exec_step_config, expected_type=type_hints["windows_exec_step_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if linux_exec_step_config is not None:
            self._values["linux_exec_step_config"] = linux_exec_step_config
        if windows_exec_step_config is not None:
            self._values["windows_exec_step_config"] = windows_exec_step_config

    @builtins.property
    def linux_exec_step_config(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig"]:
        '''linux_exec_step_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#linux_exec_step_config OsConfigPatchDeployment#linux_exec_step_config}
        '''
        result = self._values.get("linux_exec_step_config")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig"], result)

    @builtins.property
    def windows_exec_step_config(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig"]:
        '''windows_exec_step_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#windows_exec_step_config OsConfigPatchDeployment#windows_exec_step_config}
        '''
        result = self._values.get("windows_exec_step_config")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPreStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_success_codes": "allowedSuccessCodes",
        "gcs_object": "gcsObject",
        "interpreter": "interpreter",
        "local_path": "localPath",
    },
)
class OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig:
    def __init__(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        if isinstance(gcs_object, dict):
            gcs_object = OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject(**gcs_object)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig.__init__)
            check_type(argname="argument allowed_success_codes", value=allowed_success_codes, expected_type=type_hints["allowed_success_codes"])
            check_type(argname="argument gcs_object", value=gcs_object, expected_type=type_hints["gcs_object"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_success_codes is not None:
            self._values["allowed_success_codes"] = allowed_success_codes
        if gcs_object is not None:
            self._values["gcs_object"] = gcs_object
        if interpreter is not None:
            self._values["interpreter"] = interpreter
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_success_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Defaults to [0]. A list of possible return values that the execution can return to indicate a success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        '''
        result = self._values.get("allowed_success_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def gcs_object(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject"]:
        '''gcs_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        '''
        result = self._values.get("gcs_object")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject"], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script will
        be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''An absolute path to the executable on the VM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "generation_number": "generationNumber",
        "object": "object",
    },
)
class OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument generation_number", value=generation_number, expected_type=type_hints["generation_number"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "generation_number": generation_number,
            "object": object,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Bucket of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def generation_number(self) -> builtins.str:
        '''Generation number of the Cloud Storage object.

        This is used to ensure that the ExecStep specified by this PatchJob does not change.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        '''
        result = self._values.get("generation_number")
        assert result is not None, "Required property 'generation_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Name of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationNumberInput")
    def generation_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generationNumber")
    def generation_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generationNumber"))

    @generation_number.setter
    def generation_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference, "generation_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generationNumber", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcsObject")
    def put_gcs_object(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        value = OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject(
            bucket=bucket, generation_number=generation_number, object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGcsObject", [value]))

    @jsii.member(jsii_name="resetAllowedSuccessCodes")
    def reset_allowed_success_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedSuccessCodes", []))

    @jsii.member(jsii_name="resetGcsObject")
    def reset_gcs_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsObject", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="gcsObject")
    def gcs_object(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference, jsii.get(self, "gcsObject"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodesInput")
    def allowed_success_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedSuccessCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsObjectInput")
    def gcs_object_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject], jsii.get(self, "gcsObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodes")
    def allowed_success_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedSuccessCodes"))

    @allowed_success_codes.setter
    def allowed_success_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference, "allowed_success_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedSuccessCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPreStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLinuxExecStepConfig")
    def put_linux_exec_step_config(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject, typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        value = OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig(
            allowed_success_codes=allowed_success_codes,
            gcs_object=gcs_object,
            interpreter=interpreter,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putLinuxExecStepConfig", [value]))

    @jsii.member(jsii_name="putWindowsExecStepConfig")
    def put_windows_exec_step_config(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        value = OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig(
            allowed_success_codes=allowed_success_codes,
            gcs_object=gcs_object,
            interpreter=interpreter,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putWindowsExecStepConfig", [value]))

    @jsii.member(jsii_name="resetLinuxExecStepConfig")
    def reset_linux_exec_step_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxExecStepConfig", []))

    @jsii.member(jsii_name="resetWindowsExecStepConfig")
    def reset_windows_exec_step_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsExecStepConfig", []))

    @builtins.property
    @jsii.member(jsii_name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference, jsii.get(self, "linuxExecStepConfig"))

    @builtins.property
    @jsii.member(jsii_name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference":
        return typing.cast("OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference", jsii.get(self, "windowsExecStepConfig"))

    @builtins.property
    @jsii.member(jsii_name="linuxExecStepConfigInput")
    def linux_exec_step_config_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig], jsii.get(self, "linuxExecStepConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsExecStepConfigInput")
    def windows_exec_step_config_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig"], jsii.get(self, "windowsExecStepConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStep]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStep], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPreStep],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_success_codes": "allowedSuccessCodes",
        "gcs_object": "gcsObject",
        "interpreter": "interpreter",
        "local_path": "localPath",
    },
)
class OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig:
    def __init__(
        self,
        *,
        allowed_success_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        gcs_object: typing.Optional[typing.Union["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject", typing.Dict[str, typing.Any]]] = None,
        interpreter: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_success_codes: Defaults to [0]. A list of possible return values that the execution can return to indicate a success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        :param gcs_object: gcs_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        :param local_path: An absolute path to the executable on the VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        if isinstance(gcs_object, dict):
            gcs_object = OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject(**gcs_object)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig.__init__)
            check_type(argname="argument allowed_success_codes", value=allowed_success_codes, expected_type=type_hints["allowed_success_codes"])
            check_type(argname="argument gcs_object", value=gcs_object, expected_type=type_hints["gcs_object"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_success_codes is not None:
            self._values["allowed_success_codes"] = allowed_success_codes
        if gcs_object is not None:
            self._values["gcs_object"] = gcs_object
        if interpreter is not None:
            self._values["interpreter"] = interpreter
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_success_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Defaults to [0]. A list of possible return values that the execution can return to indicate a success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#allowed_success_codes OsConfigPatchDeployment#allowed_success_codes}
        '''
        result = self._values.get("allowed_success_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def gcs_object(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject"]:
        '''gcs_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#gcs_object OsConfigPatchDeployment#gcs_object}
        '''
        result = self._values.get("gcs_object")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject"], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script will
        be executed directly, which will likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#interpreter OsConfigPatchDeployment#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''An absolute path to the executable on the VM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#local_path OsConfigPatchDeployment#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "generation_number": "generationNumber",
        "object": "object",
    },
)
class OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument generation_number", value=generation_number, expected_type=type_hints["generation_number"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "generation_number": generation_number,
            "object": object,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Bucket of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def generation_number(self) -> builtins.str:
        '''Generation number of the Cloud Storage object.

        This is used to ensure that the ExecStep specified by this PatchJob does not change.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        '''
        result = self._values.get("generation_number")
        assert result is not None, "Required property 'generation_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Name of the Cloud Storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationNumberInput")
    def generation_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generationNumber")
    def generation_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generationNumber"))

    @generation_number.setter
    def generation_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference, "generation_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generationNumber", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcsObject")
    def put_gcs_object(
        self,
        *,
        bucket: builtins.str,
        generation_number: builtins.str,
        object: builtins.str,
    ) -> None:
        '''
        :param bucket: Bucket of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#bucket OsConfigPatchDeployment#bucket}
        :param generation_number: Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#generation_number OsConfigPatchDeployment#generation_number}
        :param object: Name of the Cloud Storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#object OsConfigPatchDeployment#object}
        '''
        value = OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject(
            bucket=bucket, generation_number=generation_number, object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGcsObject", [value]))

    @jsii.member(jsii_name="resetAllowedSuccessCodes")
    def reset_allowed_success_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedSuccessCodes", []))

    @jsii.member(jsii_name="resetGcsObject")
    def reset_gcs_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsObject", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="gcsObject")
    def gcs_object(
        self,
    ) -> OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference:
        return typing.cast(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference, jsii.get(self, "gcsObject"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodesInput")
    def allowed_success_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedSuccessCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsObjectInput")
    def gcs_object_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject], jsii.get(self, "gcsObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedSuccessCodes")
    def allowed_success_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedSuccessCodes"))

    @allowed_success_codes.setter
    def allowed_success_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference, "allowed_success_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedSuccessCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigWindowsUpdate",
    jsii_struct_bases=[],
    name_mapping={
        "classifications": "classifications",
        "excludes": "excludes",
        "exclusive_patches": "exclusivePatches",
    },
)
class OsConfigPatchDeploymentPatchConfigWindowsUpdate:
    def __init__(
        self,
        *,
        classifications: typing.Optional[typing.Sequence[builtins.str]] = None,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param classifications: Only apply updates of these windows update classifications. If empty, all updates are applied. Possible values: ["CRITICAL", "SECURITY", "DEFINITION", "DRIVER", "FEATURE_PACK", "SERVICE_PACK", "TOOL", "UPDATE_ROLLUP", "UPDATE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#classifications OsConfigPatchDeployment#classifications}
        :param excludes: List of KBs to exclude from update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_patches: An exclusive list of kbs to be updated. These are the only patches that will be updated. This field must not be used with other patch configurations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigWindowsUpdate.__init__)
            check_type(argname="argument classifications", value=classifications, expected_type=type_hints["classifications"])
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument exclusive_patches", value=exclusive_patches, expected_type=type_hints["exclusive_patches"])
        self._values: typing.Dict[str, typing.Any] = {}
        if classifications is not None:
            self._values["classifications"] = classifications
        if excludes is not None:
            self._values["excludes"] = excludes
        if exclusive_patches is not None:
            self._values["exclusive_patches"] = exclusive_patches

    @builtins.property
    def classifications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only apply updates of these windows update classifications.

        If empty, all updates are applied. Possible values: ["CRITICAL", "SECURITY", "DEFINITION", "DRIVER", "FEATURE_PACK", "SERVICE_PACK", "TOOL", "UPDATE_ROLLUP", "UPDATE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#classifications OsConfigPatchDeployment#classifications}
        '''
        result = self._values.get("classifications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of KBs to exclude from update.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclusive_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An exclusive list of kbs to be updated.

        These are the only patches that will be updated.
        This field must not be used with other patch configurations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        '''
        result = self._values.get("exclusive_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigWindowsUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClassifications")
    def reset_classifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassifications", []))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetExclusivePatches")
    def reset_exclusive_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusivePatches", []))

    @builtins.property
    @jsii.member(jsii_name="classificationsInput")
    def classifications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "classificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusivePatchesInput")
    def exclusive_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusivePatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="classifications")
    def classifications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "classifications"))

    @classifications.setter
    def classifications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference, "classifications").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classifications", value)

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference, "excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="exclusivePatches")
    def exclusive_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusivePatches"))

    @exclusive_patches.setter
    def exclusive_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference, "exclusive_patches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusivePatches", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigWindowsUpdate]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigWindowsUpdate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigWindowsUpdate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigYum",
    jsii_struct_bases=[],
    name_mapping={
        "excludes": "excludes",
        "exclusive_packages": "exclusivePackages",
        "minimal": "minimal",
        "security": "security",
    },
)
class OsConfigPatchDeploymentPatchConfigYum:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        minimal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param excludes: List of packages to exclude from update. These packages will be excluded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_packages: An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        :param minimal: Will cause patch to run yum update-minimal instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minimal OsConfigPatchDeployment#minimal}
        :param security: Adds the --security flag to yum update. Not supported on all platforms. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#security OsConfigPatchDeployment#security}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigYum.__init__)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument exclusive_packages", value=exclusive_packages, expected_type=type_hints["exclusive_packages"])
            check_type(argname="argument minimal", value=minimal, expected_type=type_hints["minimal"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
        self._values: typing.Dict[str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if exclusive_packages is not None:
            self._values["exclusive_packages"] = exclusive_packages
        if minimal is not None:
            self._values["minimal"] = minimal
        if security is not None:
            self._values["security"] = security

    @builtins.property
    def excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of packages to exclude from update. These packages will be excluded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclusive_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An exclusive list of packages to be updated.

        These are the only packages that will be updated.
        If these packages are not installed, they will be ignored. This field cannot be specified with
        any other patch configuration fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_packages OsConfigPatchDeployment#exclusive_packages}
        '''
        result = self._values.get("exclusive_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def minimal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Will cause patch to run yum update-minimal instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minimal OsConfigPatchDeployment#minimal}
        '''
        result = self._values.get("minimal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Adds the --security flag to yum update. Not supported on all platforms.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#security OsConfigPatchDeployment#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigYum(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigYumOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigYumOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigYumOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetExclusivePackages")
    def reset_exclusive_packages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusivePackages", []))

    @jsii.member(jsii_name="resetMinimal")
    def reset_minimal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimal", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusivePackagesInput")
    def exclusive_packages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusivePackagesInput"))

    @builtins.property
    @jsii.member(jsii_name="minimalInput")
    def minimal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "minimalInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigYumOutputReference, "excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="exclusivePackages")
    def exclusive_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusivePackages"))

    @exclusive_packages.setter
    def exclusive_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigYumOutputReference, "exclusive_packages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusivePackages", value)

    @builtins.property
    @jsii.member(jsii_name="minimal")
    def minimal(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "minimal"))

    @minimal.setter
    def minimal(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigYumOutputReference, "minimal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimal", value)

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "security"))

    @security.setter
    def security(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigYumOutputReference, "security").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "security", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentPatchConfigYum]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigYum], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigYum],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigYumOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigZypper",
    jsii_struct_bases=[],
    name_mapping={
        "categories": "categories",
        "excludes": "excludes",
        "exclusive_patches": "exclusivePatches",
        "severities": "severities",
        "with_optional": "withOptional",
        "with_update": "withUpdate",
    },
)
class OsConfigPatchDeploymentPatchConfigZypper:
    def __init__(
        self,
        *,
        categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusive_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        severities: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_optional: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        with_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param categories: Install only patches with these categories. Common categories include security, recommended, and feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#categories OsConfigPatchDeployment#categories}
        :param excludes: List of packages to exclude from update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        :param exclusive_patches: An exclusive list of patches to be updated. These are the only patches that will be installed using 'zypper patch patch:' command. This field must not be used with any other patch configuration fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        :param severities: Install only patches with these severities. Common severities include critical, important, moderate, and low. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#severities OsConfigPatchDeployment#severities}
        :param with_optional: Adds the --with-optional flag to zypper patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_optional OsConfigPatchDeployment#with_optional}
        :param with_update: Adds the --with-update flag, to zypper patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_update OsConfigPatchDeployment#with_update}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigZypper.__init__)
            check_type(argname="argument categories", value=categories, expected_type=type_hints["categories"])
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument exclusive_patches", value=exclusive_patches, expected_type=type_hints["exclusive_patches"])
            check_type(argname="argument severities", value=severities, expected_type=type_hints["severities"])
            check_type(argname="argument with_optional", value=with_optional, expected_type=type_hints["with_optional"])
            check_type(argname="argument with_update", value=with_update, expected_type=type_hints["with_update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if categories is not None:
            self._values["categories"] = categories
        if excludes is not None:
            self._values["excludes"] = excludes
        if exclusive_patches is not None:
            self._values["exclusive_patches"] = exclusive_patches
        if severities is not None:
            self._values["severities"] = severities
        if with_optional is not None:
            self._values["with_optional"] = with_optional
        if with_update is not None:
            self._values["with_update"] = with_update

    @builtins.property
    def categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Install only patches with these categories. Common categories include security, recommended, and feature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#categories OsConfigPatchDeployment#categories}
        '''
        result = self._values.get("categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of packages to exclude from update.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#excludes OsConfigPatchDeployment#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclusive_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An exclusive list of patches to be updated.

        These are the only patches that will be installed using 'zypper patch patch:' command.
        This field must not be used with any other patch configuration fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#exclusive_patches OsConfigPatchDeployment#exclusive_patches}
        '''
        result = self._values.get("exclusive_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def severities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Install only patches with these severities. Common severities include critical, important, moderate, and low.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#severities OsConfigPatchDeployment#severities}
        '''
        result = self._values.get("severities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def with_optional(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Adds the --with-optional flag to zypper patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_optional OsConfigPatchDeployment#with_optional}
        '''
        result = self._values.get("with_optional")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def with_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Adds the --with-update flag, to zypper patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#with_update OsConfigPatchDeployment#with_update}
        '''
        result = self._values.get("with_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentPatchConfigZypper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentPatchConfigZypperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentPatchConfigZypperOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentPatchConfigZypperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCategories")
    def reset_categories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategories", []))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetExclusivePatches")
    def reset_exclusive_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusivePatches", []))

    @jsii.member(jsii_name="resetSeverities")
    def reset_severities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverities", []))

    @jsii.member(jsii_name="resetWithOptional")
    def reset_with_optional(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithOptional", []))

    @jsii.member(jsii_name="resetWithUpdate")
    def reset_with_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="categoriesInput")
    def categories_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "categoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusivePatchesInput")
    def exclusive_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusivePatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="severitiesInput")
    def severities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "severitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="withOptionalInput")
    def with_optional_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withOptionalInput"))

    @builtins.property
    @jsii.member(jsii_name="withUpdateInput")
    def with_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="categories")
    def categories(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "categories"))

    @categories.setter
    def categories(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "categories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categories", value)

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="exclusivePatches")
    def exclusive_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusivePatches"))

    @exclusive_patches.setter
    def exclusive_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "exclusive_patches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusivePatches", value)

    @builtins.property
    @jsii.member(jsii_name="severities")
    def severities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "severities"))

    @severities.setter
    def severities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "severities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severities", value)

    @builtins.property
    @jsii.member(jsii_name="withOptional")
    def with_optional(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withOptional"))

    @with_optional.setter
    def with_optional(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "with_optional").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withOptional", value)

    @builtins.property
    @jsii.member(jsii_name="withUpdate")
    def with_update(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withUpdate"))

    @with_update.setter
    def with_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "with_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentPatchConfigZypper]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentPatchConfigZypper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentPatchConfigZypper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentPatchConfigZypperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "time_of_day": "timeOfDay",
        "time_zone": "timeZone",
        "end_time": "endTime",
        "monthly": "monthly",
        "start_time": "startTime",
        "weekly": "weekly",
    },
)
class OsConfigPatchDeploymentRecurringSchedule:
    def __init__(
        self,
        *,
        time_of_day: typing.Union["OsConfigPatchDeploymentRecurringScheduleTimeOfDay", typing.Dict[str, typing.Any]],
        time_zone: typing.Union["OsConfigPatchDeploymentRecurringScheduleTimeZone", typing.Dict[str, typing.Any]],
        end_time: typing.Optional[builtins.str] = None,
        monthly: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringScheduleMonthly", typing.Dict[str, typing.Any]]] = None,
        start_time: typing.Optional[builtins.str] = None,
        weekly: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringScheduleWeekly", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param time_of_day: time_of_day block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_of_day OsConfigPatchDeployment#time_of_day}
        :param time_zone: time_zone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_zone OsConfigPatchDeployment#time_zone}
        :param end_time: The end time at which a recurring patch deployment schedule is no longer active. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#end_time OsConfigPatchDeployment#end_time}
        :param monthly: monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#monthly OsConfigPatchDeployment#monthly}
        :param start_time: The time that the recurring schedule becomes effective. Defaults to createTime of the patch deployment. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#start_time OsConfigPatchDeployment#start_time}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#weekly OsConfigPatchDeployment#weekly}
        '''
        if isinstance(time_of_day, dict):
            time_of_day = OsConfigPatchDeploymentRecurringScheduleTimeOfDay(**time_of_day)
        if isinstance(time_zone, dict):
            time_zone = OsConfigPatchDeploymentRecurringScheduleTimeZone(**time_zone)
        if isinstance(monthly, dict):
            monthly = OsConfigPatchDeploymentRecurringScheduleMonthly(**monthly)
        if isinstance(weekly, dict):
            weekly = OsConfigPatchDeploymentRecurringScheduleWeekly(**weekly)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringSchedule.__init__)
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument monthly", value=monthly, expected_type=type_hints["monthly"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_of_day": time_of_day,
            "time_zone": time_zone,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if monthly is not None:
            self._values["monthly"] = monthly
        if start_time is not None:
            self._values["start_time"] = start_time
        if weekly is not None:
            self._values["weekly"] = weekly

    @builtins.property
    def time_of_day(self) -> "OsConfigPatchDeploymentRecurringScheduleTimeOfDay":
        '''time_of_day block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_of_day OsConfigPatchDeployment#time_of_day}
        '''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleTimeOfDay", result)

    @builtins.property
    def time_zone(self) -> "OsConfigPatchDeploymentRecurringScheduleTimeZone":
        '''time_zone block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#time_zone OsConfigPatchDeployment#time_zone}
        '''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleTimeZone", result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''The end time at which a recurring patch deployment schedule is no longer active.

        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#end_time OsConfigPatchDeployment#end_time}
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monthly(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthly"]:
        '''monthly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#monthly OsConfigPatchDeployment#monthly}
        '''
        result = self._values.get("monthly")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthly"], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''The time that the recurring schedule becomes effective.

        Defaults to createTime of the patch deployment.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#start_time OsConfigPatchDeployment#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleWeekly"]:
        '''weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#weekly OsConfigPatchDeployment#weekly}
        '''
        result = self._values.get("weekly")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleWeekly"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleMonthly",
    jsii_struct_bases=[],
    name_mapping={"month_day": "monthDay", "week_day_of_month": "weekDayOfMonth"},
)
class OsConfigPatchDeploymentRecurringScheduleMonthly:
    def __init__(
        self,
        *,
        month_day: typing.Optional[jsii.Number] = None,
        week_day_of_month: typing.Optional[typing.Union["OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param month_day: One day of the month. 1-31 indicates the 1st to the 31st day. -1 indicates the last day of the month. Months without the target day will be skipped. For example, a schedule to run "every month on the 31st" will not run in February, April, June, etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#month_day OsConfigPatchDeployment#month_day}
        :param week_day_of_month: week_day_of_month block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_day_of_month OsConfigPatchDeployment#week_day_of_month}
        '''
        if isinstance(week_day_of_month, dict):
            week_day_of_month = OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth(**week_day_of_month)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleMonthly.__init__)
            check_type(argname="argument month_day", value=month_day, expected_type=type_hints["month_day"])
            check_type(argname="argument week_day_of_month", value=week_day_of_month, expected_type=type_hints["week_day_of_month"])
        self._values: typing.Dict[str, typing.Any] = {}
        if month_day is not None:
            self._values["month_day"] = month_day
        if week_day_of_month is not None:
            self._values["week_day_of_month"] = week_day_of_month

    @builtins.property
    def month_day(self) -> typing.Optional[jsii.Number]:
        '''One day of the month.

        1-31 indicates the 1st to the 31st day. -1 indicates the last day of the month.
        Months without the target day will be skipped. For example, a schedule to run "every month on the 31st"
        will not run in February, April, June, etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#month_day OsConfigPatchDeployment#month_day}
        '''
        result = self._values.get("month_day")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def week_day_of_month(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth"]:
        '''week_day_of_month block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_day_of_month OsConfigPatchDeployment#week_day_of_month}
        '''
        result = self._values.get("week_day_of_month")
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringScheduleMonthly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeekDayOfMonth")
    def put_week_day_of_month(
        self,
        *,
        day_of_week: builtins.str,
        week_ordinal: jsii.Number,
    ) -> None:
        '''
        :param day_of_week: A day of the week. Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        :param week_ordinal: Week number in a month. 1-4 indicates the 1st to 4th week of the month. -1 indicates the last week of the month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_ordinal OsConfigPatchDeployment#week_ordinal}
        '''
        value = OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth(
            day_of_week=day_of_week, week_ordinal=week_ordinal
        )

        return typing.cast(None, jsii.invoke(self, "putWeekDayOfMonth", [value]))

    @jsii.member(jsii_name="resetMonthDay")
    def reset_month_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthDay", []))

    @jsii.member(jsii_name="resetWeekDayOfMonth")
    def reset_week_day_of_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekDayOfMonth", []))

    @builtins.property
    @jsii.member(jsii_name="weekDayOfMonth")
    def week_day_of_month(
        self,
    ) -> "OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference":
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference", jsii.get(self, "weekDayOfMonth"))

    @builtins.property
    @jsii.member(jsii_name="monthDayInput")
    def month_day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthDayInput"))

    @builtins.property
    @jsii.member(jsii_name="weekDayOfMonthInput")
    def week_day_of_month_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth"], jsii.get(self, "weekDayOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="monthDay")
    def month_day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthDay"))

    @month_day.setter
    def month_day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference, "month_day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthDay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthly]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth",
    jsii_struct_bases=[],
    name_mapping={"day_of_week": "dayOfWeek", "week_ordinal": "weekOrdinal"},
)
class OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth:
    def __init__(self, *, day_of_week: builtins.str, week_ordinal: jsii.Number) -> None:
        '''
        :param day_of_week: A day of the week. Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        :param week_ordinal: Week number in a month. 1-4 indicates the 1st to 4th week of the month. -1 indicates the last week of the month. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_ordinal OsConfigPatchDeployment#week_ordinal}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth.__init__)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument week_ordinal", value=week_ordinal, expected_type=type_hints["week_ordinal"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
            "week_ordinal": week_ordinal,
        }

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''A day of the week. Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        '''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def week_ordinal(self) -> jsii.Number:
        '''Week number in a month.

        1-4 indicates the 1st to 4th week of the month. -1 indicates the last week of the month.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_ordinal OsConfigPatchDeployment#week_ordinal}
        '''
        result = self._values.get("week_ordinal")
        assert result is not None, "Required property 'week_ordinal' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="weekOrdinalInput")
    def week_ordinal_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weekOrdinalInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="weekOrdinal")
    def week_ordinal(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weekOrdinal"))

    @week_ordinal.setter
    def week_ordinal(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference, "week_ordinal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekOrdinal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentRecurringScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMonthly")
    def put_monthly(
        self,
        *,
        month_day: typing.Optional[jsii.Number] = None,
        week_day_of_month: typing.Optional[typing.Union[OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param month_day: One day of the month. 1-31 indicates the 1st to the 31st day. -1 indicates the last day of the month. Months without the target day will be skipped. For example, a schedule to run "every month on the 31st" will not run in February, April, June, etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#month_day OsConfigPatchDeployment#month_day}
        :param week_day_of_month: week_day_of_month block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#week_day_of_month OsConfigPatchDeployment#week_day_of_month}
        '''
        value = OsConfigPatchDeploymentRecurringScheduleMonthly(
            month_day=month_day, week_day_of_month=week_day_of_month
        )

        return typing.cast(None, jsii.invoke(self, "putMonthly", [value]))

    @jsii.member(jsii_name="putTimeOfDay")
    def put_time_of_day(
        self,
        *,
        hours: typing.Optional[jsii.Number] = None,
        minutes: typing.Optional[jsii.Number] = None,
        nanos: typing.Optional[jsii.Number] = None,
        seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#hours OsConfigPatchDeployment#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minutes OsConfigPatchDeployment#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#nanos OsConfigPatchDeployment#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#seconds OsConfigPatchDeployment#seconds}
        '''
        value = OsConfigPatchDeploymentRecurringScheduleTimeOfDay(
            hours=hours, minutes=minutes, nanos=nanos, seconds=seconds
        )

        return typing.cast(None, jsii.invoke(self, "putTimeOfDay", [value]))

    @jsii.member(jsii_name="putTimeZone")
    def put_time_zone(
        self,
        *,
        id: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: IANA Time Zone Database time zone, e.g. "America/New_York". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: IANA Time Zone Database version number, e.g. "2019a". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#version OsConfigPatchDeployment#version}
        '''
        value = OsConfigPatchDeploymentRecurringScheduleTimeZone(
            id=id, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putTimeZone", [value]))

    @jsii.member(jsii_name="putWeekly")
    def put_weekly(self, *, day_of_week: builtins.str) -> None:
        '''
        :param day_of_week: IANA Time Zone Database time zone, e.g. "America/New_York". Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        '''
        value = OsConfigPatchDeploymentRecurringScheduleWeekly(day_of_week=day_of_week)

        return typing.cast(None, jsii.invoke(self, "putWeekly", [value]))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetMonthly")
    def reset_monthly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthly", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetWeekly")
    def reset_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekly", []))

    @builtins.property
    @jsii.member(jsii_name="lastExecuteTime")
    def last_execute_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastExecuteTime"))

    @builtins.property
    @jsii.member(jsii_name="monthly")
    def monthly(self) -> OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference:
        return typing.cast(OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference, jsii.get(self, "monthly"))

    @builtins.property
    @jsii.member(jsii_name="nextExecuteTime")
    def next_execute_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextExecuteTime"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(
        self,
    ) -> "OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference":
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference", jsii.get(self, "timeOfDay"))

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(
        self,
    ) -> "OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference":
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference", jsii.get(self, "timeZone"))

    @builtins.property
    @jsii.member(jsii_name="weekly")
    def weekly(self) -> "OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference":
        return typing.cast("OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference", jsii.get(self, "weekly"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyInput")
    def monthly_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthly]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleMonthly], jsii.get(self, "monthlyInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleTimeOfDay"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleTimeOfDay"], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleTimeZone"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleTimeZone"], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyInput")
    def weekly_input(
        self,
    ) -> typing.Optional["OsConfigPatchDeploymentRecurringScheduleWeekly"]:
        return typing.cast(typing.Optional["OsConfigPatchDeploymentRecurringScheduleWeekly"], jsii.get(self, "weeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringSchedule]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleTimeOfDay",
    jsii_struct_bases=[],
    name_mapping={
        "hours": "hours",
        "minutes": "minutes",
        "nanos": "nanos",
        "seconds": "seconds",
    },
)
class OsConfigPatchDeploymentRecurringScheduleTimeOfDay:
    def __init__(
        self,
        *,
        hours: typing.Optional[jsii.Number] = None,
        minutes: typing.Optional[jsii.Number] = None,
        nanos: typing.Optional[jsii.Number] = None,
        seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#hours OsConfigPatchDeployment#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minutes OsConfigPatchDeployment#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#nanos OsConfigPatchDeployment#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#seconds OsConfigPatchDeployment#seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleTimeOfDay.__init__)
            check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hours is not None:
            self._values["hours"] = hours
        if minutes is not None:
            self._values["minutes"] = minutes
        if nanos is not None:
            self._values["nanos"] = nanos
        if seconds is not None:
            self._values["seconds"] = seconds

    @builtins.property
    def hours(self) -> typing.Optional[jsii.Number]:
        '''Hours of day in 24 hour format.

        Should be from 0 to 23.
        An API may choose to allow the value "24:00:00" for scenarios like business closing time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#hours OsConfigPatchDeployment#hours}
        '''
        result = self._values.get("hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minutes(self) -> typing.Optional[jsii.Number]:
        '''Minutes of hour of day. Must be from 0 to 59.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#minutes OsConfigPatchDeployment#minutes}
        '''
        result = self._values.get("minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#nanos OsConfigPatchDeployment#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seconds(self) -> typing.Optional[jsii.Number]:
        '''Seconds of minutes of the time.

        Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#seconds OsConfigPatchDeployment#seconds}
        '''
        result = self._values.get("seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringScheduleTimeOfDay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHours")
    def reset_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHours", []))

    @jsii.member(jsii_name="resetMinutes")
    def reset_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinutes", []))

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @jsii.member(jsii_name="resetSeconds")
    def reset_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeconds", []))

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
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference, "hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hours", value)

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference, "minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeOfDay]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeOfDay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeOfDay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleTimeZone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "version": "version"},
)
class OsConfigPatchDeploymentRecurringScheduleTimeZone:
    def __init__(
        self,
        *,
        id: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: IANA Time Zone Database time zone, e.g. "America/New_York". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: IANA Time Zone Database version number, e.g. "2019a". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#version OsConfigPatchDeployment#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleTimeZone.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> builtins.str:
        '''IANA Time Zone Database time zone, e.g. "America/New_York".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#id OsConfigPatchDeployment#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''IANA Time Zone Database version number, e.g. "2019a".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#version OsConfigPatchDeployment#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringScheduleTimeZone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeZone]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeZone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringScheduleTimeZone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleWeekly",
    jsii_struct_bases=[],
    name_mapping={"day_of_week": "dayOfWeek"},
)
class OsConfigPatchDeploymentRecurringScheduleWeekly:
    def __init__(self, *, day_of_week: builtins.str) -> None:
        '''
        :param day_of_week: IANA Time Zone Database time zone, e.g. "America/New_York". Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleWeekly.__init__)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
        }

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''IANA Time Zone Database time zone, e.g. "America/New_York". Possible values: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#day_of_week OsConfigPatchDeployment#day_of_week}
        '''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRecurringScheduleWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRecurringScheduleWeekly]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRecurringScheduleWeekly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRecurringScheduleWeekly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRollout",
    jsii_struct_bases=[],
    name_mapping={"disruption_budget": "disruptionBudget", "mode": "mode"},
)
class OsConfigPatchDeploymentRollout:
    def __init__(
        self,
        *,
        disruption_budget: typing.Union["OsConfigPatchDeploymentRolloutDisruptionBudget", typing.Dict[str, typing.Any]],
        mode: builtins.str,
    ) -> None:
        '''
        :param disruption_budget: disruption_budget block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#disruption_budget OsConfigPatchDeployment#disruption_budget}
        :param mode: Mode of the patch rollout. Possible values: ["ZONE_BY_ZONE", "CONCURRENT_ZONES"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mode OsConfigPatchDeployment#mode}
        '''
        if isinstance(disruption_budget, dict):
            disruption_budget = OsConfigPatchDeploymentRolloutDisruptionBudget(**disruption_budget)
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRollout.__init__)
            check_type(argname="argument disruption_budget", value=disruption_budget, expected_type=type_hints["disruption_budget"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "disruption_budget": disruption_budget,
            "mode": mode,
        }

    @builtins.property
    def disruption_budget(self) -> "OsConfigPatchDeploymentRolloutDisruptionBudget":
        '''disruption_budget block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#disruption_budget OsConfigPatchDeployment#disruption_budget}
        '''
        result = self._values.get("disruption_budget")
        assert result is not None, "Required property 'disruption_budget' is missing"
        return typing.cast("OsConfigPatchDeploymentRolloutDisruptionBudget", result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode of the patch rollout. Possible values: ["ZONE_BY_ZONE", "CONCURRENT_ZONES"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#mode OsConfigPatchDeployment#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRollout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRolloutDisruptionBudget",
    jsii_struct_bases=[],
    name_mapping={"fixed": "fixed", "percentage": "percentage"},
)
class OsConfigPatchDeploymentRolloutDisruptionBudget:
    def __init__(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#fixed OsConfigPatchDeployment#fixed}
        :param percentage: Specifies the relative value defined as a percentage, which will be multiplied by a reference value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#percentage OsConfigPatchDeployment#percentage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRolloutDisruptionBudget.__init__)
            check_type(argname="argument fixed", value=fixed, expected_type=type_hints["fixed"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fixed is not None:
            self._values["fixed"] = fixed
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def fixed(self) -> typing.Optional[jsii.Number]:
        '''Specifies a fixed value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#fixed OsConfigPatchDeployment#fixed}
        '''
        result = self._values.get("fixed")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''Specifies the relative value defined as a percentage, which will be multiplied by a reference value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#percentage OsConfigPatchDeployment#percentage}
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentRolloutDisruptionBudget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFixed")
    def reset_fixed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixed", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="fixedInput")
    def fixed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fixedInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="fixed")
    def fixed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fixed"))

    @fixed.setter
    def fixed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference, "fixed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixed", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRolloutDisruptionBudget]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRolloutDisruptionBudget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRolloutDisruptionBudget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OsConfigPatchDeploymentRolloutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentRolloutOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentRolloutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDisruptionBudget")
    def put_disruption_budget(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#fixed OsConfigPatchDeployment#fixed}
        :param percentage: Specifies the relative value defined as a percentage, which will be multiplied by a reference value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#percentage OsConfigPatchDeployment#percentage}
        '''
        value = OsConfigPatchDeploymentRolloutDisruptionBudget(
            fixed=fixed, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDisruptionBudget", [value]))

    @builtins.property
    @jsii.member(jsii_name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference:
        return typing.cast(OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference, jsii.get(self, "disruptionBudget"))

    @builtins.property
    @jsii.member(jsii_name="disruptionBudgetInput")
    def disruption_budget_input(
        self,
    ) -> typing.Optional[OsConfigPatchDeploymentRolloutDisruptionBudget]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRolloutDisruptionBudget], jsii.get(self, "disruptionBudgetInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRolloutOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OsConfigPatchDeploymentRollout]:
        return typing.cast(typing.Optional[OsConfigPatchDeploymentRollout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OsConfigPatchDeploymentRollout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentRolloutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class OsConfigPatchDeploymentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#create OsConfigPatchDeployment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#delete OsConfigPatchDeployment#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#create OsConfigPatchDeployment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/os_config_patch_deployment#delete OsConfigPatchDeployment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OsConfigPatchDeploymentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OsConfigPatchDeploymentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.osConfigPatchDeployment.OsConfigPatchDeploymentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(OsConfigPatchDeploymentTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OsConfigPatchDeploymentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OsConfigPatchDeploymentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OsConfigPatchDeploymentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OsConfigPatchDeploymentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OsConfigPatchDeployment",
    "OsConfigPatchDeploymentConfig",
    "OsConfigPatchDeploymentInstanceFilter",
    "OsConfigPatchDeploymentInstanceFilterGroupLabels",
    "OsConfigPatchDeploymentInstanceFilterGroupLabelsList",
    "OsConfigPatchDeploymentInstanceFilterGroupLabelsOutputReference",
    "OsConfigPatchDeploymentInstanceFilterOutputReference",
    "OsConfigPatchDeploymentOneTimeSchedule",
    "OsConfigPatchDeploymentOneTimeScheduleOutputReference",
    "OsConfigPatchDeploymentPatchConfig",
    "OsConfigPatchDeploymentPatchConfigApt",
    "OsConfigPatchDeploymentPatchConfigAptOutputReference",
    "OsConfigPatchDeploymentPatchConfigGoo",
    "OsConfigPatchDeploymentPatchConfigGooOutputReference",
    "OsConfigPatchDeploymentPatchConfigOutputReference",
    "OsConfigPatchDeploymentPatchConfigPostStep",
    "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfig",
    "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject",
    "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectOutputReference",
    "OsConfigPatchDeploymentPatchConfigPostStepLinuxExecStepConfigOutputReference",
    "OsConfigPatchDeploymentPatchConfigPostStepOutputReference",
    "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfig",
    "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject",
    "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectOutputReference",
    "OsConfigPatchDeploymentPatchConfigPostStepWindowsExecStepConfigOutputReference",
    "OsConfigPatchDeploymentPatchConfigPreStep",
    "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfig",
    "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject",
    "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectOutputReference",
    "OsConfigPatchDeploymentPatchConfigPreStepLinuxExecStepConfigOutputReference",
    "OsConfigPatchDeploymentPatchConfigPreStepOutputReference",
    "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfig",
    "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject",
    "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectOutputReference",
    "OsConfigPatchDeploymentPatchConfigPreStepWindowsExecStepConfigOutputReference",
    "OsConfigPatchDeploymentPatchConfigWindowsUpdate",
    "OsConfigPatchDeploymentPatchConfigWindowsUpdateOutputReference",
    "OsConfigPatchDeploymentPatchConfigYum",
    "OsConfigPatchDeploymentPatchConfigYumOutputReference",
    "OsConfigPatchDeploymentPatchConfigZypper",
    "OsConfigPatchDeploymentPatchConfigZypperOutputReference",
    "OsConfigPatchDeploymentRecurringSchedule",
    "OsConfigPatchDeploymentRecurringScheduleMonthly",
    "OsConfigPatchDeploymentRecurringScheduleMonthlyOutputReference",
    "OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth",
    "OsConfigPatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthOutputReference",
    "OsConfigPatchDeploymentRecurringScheduleOutputReference",
    "OsConfigPatchDeploymentRecurringScheduleTimeOfDay",
    "OsConfigPatchDeploymentRecurringScheduleTimeOfDayOutputReference",
    "OsConfigPatchDeploymentRecurringScheduleTimeZone",
    "OsConfigPatchDeploymentRecurringScheduleTimeZoneOutputReference",
    "OsConfigPatchDeploymentRecurringScheduleWeekly",
    "OsConfigPatchDeploymentRecurringScheduleWeeklyOutputReference",
    "OsConfigPatchDeploymentRollout",
    "OsConfigPatchDeploymentRolloutDisruptionBudget",
    "OsConfigPatchDeploymentRolloutDisruptionBudgetOutputReference",
    "OsConfigPatchDeploymentRolloutOutputReference",
    "OsConfigPatchDeploymentTimeouts",
    "OsConfigPatchDeploymentTimeoutsOutputReference",
]

publication.publish()
