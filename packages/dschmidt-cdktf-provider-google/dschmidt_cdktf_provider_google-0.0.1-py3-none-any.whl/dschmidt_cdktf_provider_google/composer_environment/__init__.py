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


class ComposerEnvironment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/composer_environment google_composer_environment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        config: typing.Optional[typing.Union["ComposerEnvironmentConfigA", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ComposerEnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/composer_environment google_composer_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#name ComposerEnvironment#name}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#config ComposerEnvironment#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#id ComposerEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Label values must be between 0 and 63 characters long and must conform to the regular expression (`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?)?. No more than 64 labels can be associated with a given environment. Both keys and values must be <= 128 bytes in size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#labels ComposerEnvironment#labels}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#project ComposerEnvironment#project}
        :param region: The location or Compute Engine region for the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#region ComposerEnvironment#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#timeouts ComposerEnvironment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = ComposerEnvironmentConfig(
            name=name,
            config=config,
            id=id,
            labels=labels,
            project=project,
            region=region,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        database_config: typing.Optional[typing.Union["ComposerEnvironmentConfigDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union["ComposerEnvironmentConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        environment_size: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["ComposerEnvironmentConfigMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        master_authorized_networks_config: typing.Optional[typing.Union["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig", typing.Dict[str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["ComposerEnvironmentConfigNodeConfig", typing.Dict[str, typing.Any]]] = None,
        node_count: typing.Optional[jsii.Number] = None,
        private_environment_config: typing.Optional[typing.Union["ComposerEnvironmentConfigPrivateEnvironmentConfig", typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union["ComposerEnvironmentConfigSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        web_server_config: typing.Optional[typing.Union["ComposerEnvironmentConfigWebServerConfig", typing.Dict[str, typing.Any]]] = None,
        web_server_network_access_control: typing.Optional[typing.Union["ComposerEnvironmentConfigWebServerNetworkAccessControl", typing.Dict[str, typing.Any]]] = None,
        workloads_config: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database_config: database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#database_config ComposerEnvironment#database_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#encryption_config ComposerEnvironment#encryption_config}
        :param environment_size: The size of the Cloud Composer environment. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#environment_size ComposerEnvironment#environment_size}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#maintenance_window ComposerEnvironment#maintenance_window}
        :param master_authorized_networks_config: master_authorized_networks_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_authorized_networks_config ComposerEnvironment#master_authorized_networks_config}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_config ComposerEnvironment#node_config}
        :param node_count: The number of nodes in the Kubernetes Engine cluster that will be used to run this environment. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_count ComposerEnvironment#node_count}
        :param private_environment_config: private_environment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#private_environment_config ComposerEnvironment#private_environment_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#software_config ComposerEnvironment#software_config}
        :param web_server_config: web_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_config ComposerEnvironment#web_server_config}
        :param web_server_network_access_control: web_server_network_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_network_access_control ComposerEnvironment#web_server_network_access_control}
        :param workloads_config: workloads_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#workloads_config ComposerEnvironment#workloads_config}
        '''
        value = ComposerEnvironmentConfigA(
            database_config=database_config,
            encryption_config=encryption_config,
            environment_size=environment_size,
            maintenance_window=maintenance_window,
            master_authorized_networks_config=master_authorized_networks_config,
            node_config=node_config,
            node_count=node_count,
            private_environment_config=private_environment_config,
            software_config=software_config,
            web_server_config=web_server_config,
            web_server_network_access_control=web_server_network_access_control,
            workloads_config=workloads_config,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#create ComposerEnvironment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#delete ComposerEnvironment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#update ComposerEnvironment#update}.
        '''
        value = ComposerEnvironmentTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

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
    @jsii.member(jsii_name="config")
    def config(self) -> "ComposerEnvironmentConfigAOutputReference":
        return typing.cast("ComposerEnvironmentConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComposerEnvironmentTimeoutsOutputReference":
        return typing.cast("ComposerEnvironmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["ComposerEnvironmentConfigA"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComposerEnvironmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComposerEnvironmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironment, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironment, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironment, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfig",
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
        "config": "config",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
    },
)
class ComposerEnvironmentConfig(cdktf.TerraformMetaArguments):
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
        config: typing.Optional[typing.Union["ComposerEnvironmentConfigA", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ComposerEnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#name ComposerEnvironment#name}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#config ComposerEnvironment#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#id ComposerEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Label values must be between 0 and 63 characters long and must conform to the regular expression (`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?)?. No more than 64 labels can be associated with a given environment. Both keys and values must be <= 128 bytes in size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#labels ComposerEnvironment#labels}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#project ComposerEnvironment#project}
        :param region: The location or Compute Engine region for the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#region ComposerEnvironment#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#timeouts ComposerEnvironment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = ComposerEnvironmentConfigA(**config)
        if isinstance(timeouts, dict):
            timeouts = ComposerEnvironmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if config is not None:
            self._values["config"] = config
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
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
    def name(self) -> builtins.str:
        '''Name of the environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#name ComposerEnvironment#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> typing.Optional["ComposerEnvironmentConfigA"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#config ComposerEnvironment#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigA"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#id ComposerEnvironment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-defined labels for this environment.

        The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Label values must be between 0 and 63 characters long and must conform to the regular expression (`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?)?. No more than 64 labels can be associated with a given environment. Both keys and values must be <= 128 bytes in size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#labels ComposerEnvironment#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#project ComposerEnvironment#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The location or Compute Engine region for the environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#region ComposerEnvironment#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComposerEnvironmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#timeouts ComposerEnvironment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComposerEnvironmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "database_config": "databaseConfig",
        "encryption_config": "encryptionConfig",
        "environment_size": "environmentSize",
        "maintenance_window": "maintenanceWindow",
        "master_authorized_networks_config": "masterAuthorizedNetworksConfig",
        "node_config": "nodeConfig",
        "node_count": "nodeCount",
        "private_environment_config": "privateEnvironmentConfig",
        "software_config": "softwareConfig",
        "web_server_config": "webServerConfig",
        "web_server_network_access_control": "webServerNetworkAccessControl",
        "workloads_config": "workloadsConfig",
    },
)
class ComposerEnvironmentConfigA:
    def __init__(
        self,
        *,
        database_config: typing.Optional[typing.Union["ComposerEnvironmentConfigDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union["ComposerEnvironmentConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        environment_size: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["ComposerEnvironmentConfigMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        master_authorized_networks_config: typing.Optional[typing.Union["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig", typing.Dict[str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["ComposerEnvironmentConfigNodeConfig", typing.Dict[str, typing.Any]]] = None,
        node_count: typing.Optional[jsii.Number] = None,
        private_environment_config: typing.Optional[typing.Union["ComposerEnvironmentConfigPrivateEnvironmentConfig", typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union["ComposerEnvironmentConfigSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        web_server_config: typing.Optional[typing.Union["ComposerEnvironmentConfigWebServerConfig", typing.Dict[str, typing.Any]]] = None,
        web_server_network_access_control: typing.Optional[typing.Union["ComposerEnvironmentConfigWebServerNetworkAccessControl", typing.Dict[str, typing.Any]]] = None,
        workloads_config: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database_config: database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#database_config ComposerEnvironment#database_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#encryption_config ComposerEnvironment#encryption_config}
        :param environment_size: The size of the Cloud Composer environment. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#environment_size ComposerEnvironment#environment_size}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#maintenance_window ComposerEnvironment#maintenance_window}
        :param master_authorized_networks_config: master_authorized_networks_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_authorized_networks_config ComposerEnvironment#master_authorized_networks_config}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_config ComposerEnvironment#node_config}
        :param node_count: The number of nodes in the Kubernetes Engine cluster that will be used to run this environment. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_count ComposerEnvironment#node_count}
        :param private_environment_config: private_environment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#private_environment_config ComposerEnvironment#private_environment_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#software_config ComposerEnvironment#software_config}
        :param web_server_config: web_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_config ComposerEnvironment#web_server_config}
        :param web_server_network_access_control: web_server_network_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_network_access_control ComposerEnvironment#web_server_network_access_control}
        :param workloads_config: workloads_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#workloads_config ComposerEnvironment#workloads_config}
        '''
        if isinstance(database_config, dict):
            database_config = ComposerEnvironmentConfigDatabaseConfig(**database_config)
        if isinstance(encryption_config, dict):
            encryption_config = ComposerEnvironmentConfigEncryptionConfig(**encryption_config)
        if isinstance(maintenance_window, dict):
            maintenance_window = ComposerEnvironmentConfigMaintenanceWindow(**maintenance_window)
        if isinstance(master_authorized_networks_config, dict):
            master_authorized_networks_config = ComposerEnvironmentConfigMasterAuthorizedNetworksConfig(**master_authorized_networks_config)
        if isinstance(node_config, dict):
            node_config = ComposerEnvironmentConfigNodeConfig(**node_config)
        if isinstance(private_environment_config, dict):
            private_environment_config = ComposerEnvironmentConfigPrivateEnvironmentConfig(**private_environment_config)
        if isinstance(software_config, dict):
            software_config = ComposerEnvironmentConfigSoftwareConfig(**software_config)
        if isinstance(web_server_config, dict):
            web_server_config = ComposerEnvironmentConfigWebServerConfig(**web_server_config)
        if isinstance(web_server_network_access_control, dict):
            web_server_network_access_control = ComposerEnvironmentConfigWebServerNetworkAccessControl(**web_server_network_access_control)
        if isinstance(workloads_config, dict):
            workloads_config = ComposerEnvironmentConfigWorkloadsConfig(**workloads_config)
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigA.__init__)
            check_type(argname="argument database_config", value=database_config, expected_type=type_hints["database_config"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument environment_size", value=environment_size, expected_type=type_hints["environment_size"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument master_authorized_networks_config", value=master_authorized_networks_config, expected_type=type_hints["master_authorized_networks_config"])
            check_type(argname="argument node_config", value=node_config, expected_type=type_hints["node_config"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument private_environment_config", value=private_environment_config, expected_type=type_hints["private_environment_config"])
            check_type(argname="argument software_config", value=software_config, expected_type=type_hints["software_config"])
            check_type(argname="argument web_server_config", value=web_server_config, expected_type=type_hints["web_server_config"])
            check_type(argname="argument web_server_network_access_control", value=web_server_network_access_control, expected_type=type_hints["web_server_network_access_control"])
            check_type(argname="argument workloads_config", value=workloads_config, expected_type=type_hints["workloads_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if database_config is not None:
            self._values["database_config"] = database_config
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if environment_size is not None:
            self._values["environment_size"] = environment_size
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if master_authorized_networks_config is not None:
            self._values["master_authorized_networks_config"] = master_authorized_networks_config
        if node_config is not None:
            self._values["node_config"] = node_config
        if node_count is not None:
            self._values["node_count"] = node_count
        if private_environment_config is not None:
            self._values["private_environment_config"] = private_environment_config
        if software_config is not None:
            self._values["software_config"] = software_config
        if web_server_config is not None:
            self._values["web_server_config"] = web_server_config
        if web_server_network_access_control is not None:
            self._values["web_server_network_access_control"] = web_server_network_access_control
        if workloads_config is not None:
            self._values["workloads_config"] = workloads_config

    @builtins.property
    def database_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigDatabaseConfig"]:
        '''database_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#database_config ComposerEnvironment#database_config}
        '''
        result = self._values.get("database_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigDatabaseConfig"], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigEncryptionConfig"]:
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#encryption_config ComposerEnvironment#encryption_config}
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigEncryptionConfig"], result)

    @builtins.property
    def environment_size(self) -> typing.Optional[builtins.str]:
        '''The size of the Cloud Composer environment.

        This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#environment_size ComposerEnvironment#environment_size}
        '''
        result = self._values.get("environment_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#maintenance_window ComposerEnvironment#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigMaintenanceWindow"], result)

    @builtins.property
    def master_authorized_networks_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig"]:
        '''master_authorized_networks_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_authorized_networks_config ComposerEnvironment#master_authorized_networks_config}
        '''
        result = self._values.get("master_authorized_networks_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig"], result)

    @builtins.property
    def node_config(self) -> typing.Optional["ComposerEnvironmentConfigNodeConfig"]:
        '''node_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_config ComposerEnvironment#node_config}
        '''
        result = self._values.get("node_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigNodeConfig"], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes in the Kubernetes Engine cluster that will be used to run this environment.

        This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#node_count ComposerEnvironment#node_count}
        '''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def private_environment_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigPrivateEnvironmentConfig"]:
        '''private_environment_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#private_environment_config ComposerEnvironment#private_environment_config}
        '''
        result = self._values.get("private_environment_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigPrivateEnvironmentConfig"], result)

    @builtins.property
    def software_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigSoftwareConfig"]:
        '''software_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#software_config ComposerEnvironment#software_config}
        '''
        result = self._values.get("software_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigSoftwareConfig"], result)

    @builtins.property
    def web_server_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWebServerConfig"]:
        '''web_server_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_config ComposerEnvironment#web_server_config}
        '''
        result = self._values.get("web_server_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWebServerConfig"], result)

    @builtins.property
    def web_server_network_access_control(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWebServerNetworkAccessControl"]:
        '''web_server_network_access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_network_access_control ComposerEnvironment#web_server_network_access_control}
        '''
        result = self._values.get("web_server_network_access_control")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWebServerNetworkAccessControl"], result)

    @builtins.property
    def workloads_config(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfig"]:
        '''workloads_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#workloads_config ComposerEnvironment#workloads_config}
        '''
        result = self._values.get("workloads_config")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigAOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDatabaseConfig")
    def put_database_config(self, *, machine_type: builtins.str) -> None:
        '''
        :param machine_type: Optional. Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. If not specified, db-n1-standard-2 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        value = ComposerEnvironmentConfigDatabaseConfig(machine_type=machine_type)

        return typing.cast(None, jsii.invoke(self, "putDatabaseConfig", [value]))

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Optional. Customer-managed Encryption Key available through Google's Key Management Service. Cannot be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#kms_key_name ComposerEnvironment#kms_key_name}
        '''
        value = ComposerEnvironmentConfigEncryptionConfig(kms_key_name=kms_key_name)

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        end_time: builtins.str,
        recurrence: builtins.str,
        start_time: builtins.str,
    ) -> None:
        '''
        :param end_time: Maintenance window end time. It is used only to calculate the duration of the maintenance window. The value for end-time must be in the future, relative to 'start_time'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#end_time ComposerEnvironment#end_time}
        :param recurrence: Maintenance window recurrence. Format is a subset of RFC-5545 (https://tools.ietf.org/html/rfc5545) 'RRULE'. The only allowed values for 'FREQ' field are 'FREQ=DAILY' and 'FREQ=WEEKLY;BYDAY=...'. Example values: 'FREQ=WEEKLY;BYDAY=TU,WE', 'FREQ=DAILY'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#recurrence ComposerEnvironment#recurrence}
        :param start_time: Start time of the first recurrence of the maintenance window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#start_time ComposerEnvironment#start_time}
        '''
        value = ComposerEnvironmentConfigMaintenanceWindow(
            end_time=end_time, recurrence=recurrence, start_time=start_time
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putMasterAuthorizedNetworksConfig")
    def put_master_authorized_networks_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        cidr_blocks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether or not master authorized networks is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enabled ComposerEnvironment#enabled}
        :param cidr_blocks: cidr_blocks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cidr_blocks ComposerEnvironment#cidr_blocks}
        '''
        value = ComposerEnvironmentConfigMasterAuthorizedNetworksConfig(
            enabled=enabled, cidr_blocks=cidr_blocks
        )

        return typing.cast(None, jsii.invoke(self, "putMasterAuthorizedNetworksConfig", [value]))

    @jsii.member(jsii_name="putNodeConfig")
    def put_node_config(
        self,
        *,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        enable_ip_masq_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_allocation_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigNodeConfigIpAllocationPolicy", typing.Dict[str, typing.Any]]]]] = None,
        machine_type: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_size_gb: The disk size in GB used for node VMs. Minimum size is 20GB. If unspecified, defaults to 100GB. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#disk_size_gb ComposerEnvironment#disk_size_gb}
        :param enable_ip_masq_agent: Deploys 'ip-masq-agent' daemon set in the GKE cluster and defines nonMasqueradeCIDRs equals to pod IP range so IP masquerading is used for all destination addresses, except between pods traffic. See: https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_ip_masq_agent ComposerEnvironment#enable_ip_masq_agent}
        :param ip_allocation_policy: Configuration for controlling how IPs are allocated in the GKE cluster. Cannot be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#ip_allocation_policy ComposerEnvironment#ip_allocation_policy}
        :param machine_type: The Compute Engine machine type used for cluster instances, specified as a name or relative resource name. For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        :param network: The Compute Engine machine type used for cluster instances, specified as a name or relative resource name. For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. The network must belong to the environment's project. If unspecified, the "default" network ID in the environment's project is used. If a Custom Subnet Network is provided, subnetwork must also be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#network ComposerEnvironment#network}
        :param oauth_scopes: The set of Google API scopes to be made available on all node VMs. Cannot be updated. If empty, defaults to ["https://www.googleapis.com/auth/cloud-platform"]. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#oauth_scopes ComposerEnvironment#oauth_scopes}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. If a service account is not specified, the "default" Compute Engine service account is used. Cannot be updated. If given, note that the service account must have roles/composer.worker for any GCP resources created under the Cloud Composer Environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#service_account ComposerEnvironment#service_account}
        :param subnetwork: The Compute Engine subnetwork to be used for machine communications, , specified as a self-link, relative resource name (e.g. "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided, network must also be provided and the subnetwork must belong to the enclosing environment's project and region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#subnetwork ComposerEnvironment#subnetwork}
        :param tags: The list of instance tags applied to all node VMs. Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with RFC1035. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#tags ComposerEnvironment#tags}
        :param zone: The Compute Engine zone in which to deploy the VMs running the Apache Airflow software, specified as the zone name or relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project and region. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#zone ComposerEnvironment#zone}
        '''
        value = ComposerEnvironmentConfigNodeConfig(
            disk_size_gb=disk_size_gb,
            enable_ip_masq_agent=enable_ip_masq_agent,
            ip_allocation_policy=ip_allocation_policy,
            machine_type=machine_type,
            network=network,
            oauth_scopes=oauth_scopes,
            service_account=service_account,
            subnetwork=subnetwork,
            tags=tags,
            zone=zone,
        )

        return typing.cast(None, jsii.invoke(self, "putNodeConfig", [value]))

    @jsii.member(jsii_name="putPrivateEnvironmentConfig")
    def put_private_environment_config(
        self,
        *,
        cloud_composer_connection_subnetwork: typing.Optional[builtins.str] = None,
        cloud_composer_network_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        cloud_sql_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        enable_private_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_privately_used_public_ips: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        web_server_ipv4_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_composer_connection_subnetwork: When specified, the environment will use Private Service Connect instead of VPC peerings to connect to Cloud SQL in the Tenant Project, and the PSC endpoint in the Customer Project will use an IP address from this subnetwork. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_connection_subnetwork ComposerEnvironment#cloud_composer_connection_subnetwork}
        :param cloud_composer_network_ipv4_cidr_block: The CIDR block from which IP range for Cloud Composer Network in tenant project will be reserved. Needs to be disjoint from private_cluster_config.master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_network_ipv4_cidr_block ComposerEnvironment#cloud_composer_network_ipv4_cidr_block}
        :param cloud_sql_ipv4_cidr_block: The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from web_server_ipv4_cidr_block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_sql_ipv4_cidr_block ComposerEnvironment#cloud_sql_ipv4_cidr_block}
        :param enable_private_endpoint: If true, access to the public endpoint of the GKE cluster is denied. If this field is set to true, ip_allocation_policy.use_ip_aliases must be set to true for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_private_endpoint ComposerEnvironment#enable_private_endpoint}
        :param enable_privately_used_public_ips: When enabled, IPs from public (non-RFC1918) ranges can be used for ip_allocation_policy.cluster_ipv4_cidr_block and ip_allocation_policy.service_ipv4_cidr_block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_privately_used_public_ips ComposerEnvironment#enable_privately_used_public_ips}
        :param master_ipv4_cidr_block: The IP range in CIDR notation to use for the hosted master network. This range is used for assigning internal IP addresses to the cluster master or set of masters and to the internal load balancer virtual IP. This range must not overlap with any other ranges in use within the cluster's network. If left blank, the default value of '172.16.0.0/28' is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_ipv4_cidr_block ComposerEnvironment#master_ipv4_cidr_block}
        :param web_server_ipv4_cidr_block: The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_ipv4_cidr_block ComposerEnvironment#web_server_ipv4_cidr_block}
        '''
        value = ComposerEnvironmentConfigPrivateEnvironmentConfig(
            cloud_composer_connection_subnetwork=cloud_composer_connection_subnetwork,
            cloud_composer_network_ipv4_cidr_block=cloud_composer_network_ipv4_cidr_block,
            cloud_sql_ipv4_cidr_block=cloud_sql_ipv4_cidr_block,
            enable_private_endpoint=enable_private_endpoint,
            enable_privately_used_public_ips=enable_privately_used_public_ips,
            master_ipv4_cidr_block=master_ipv4_cidr_block,
            web_server_ipv4_cidr_block=web_server_ipv4_cidr_block,
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateEnvironmentConfig", [value]))

    @jsii.member(jsii_name="putSoftwareConfig")
    def put_software_config(
        self,
        *,
        airflow_config_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image_version: typing.Optional[builtins.str] = None,
        pypi_packages: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_version: typing.Optional[builtins.str] = None,
        scheduler_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param airflow_config_overrides: Apache Airflow configuration properties to override. Property keys contain the section and property names, separated by a hyphen, for example "core-dags_are_paused_at_creation". Section names must not contain hyphens ("-"), opening square brackets ("["), or closing square brackets ("]"). The property name must not be empty and cannot contain "=" or ";". Section and property names cannot contain characters: "." Apache Airflow configuration property names must be written in snake_case. Property values can contain any character, and can be written in any lower/upper case format. Certain Apache Airflow configuration property values are blacklisted, and cannot be overridden. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#airflow_config_overrides ComposerEnvironment#airflow_config_overrides}
        :param env_variables: Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes. Environment variable names must match the regular expression [a-zA-Z_][a-zA-Z0-9_]*. They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+), and they cannot match any of the following reserved names: AIRFLOW_HOME C_FORCE_ROOT CONTAINER_NAME DAGS_FOLDER GCP_PROJECT GCS_BUCKET GKE_CLUSTER_NAME SQL_DATABASE SQL_INSTANCE SQL_PASSWORD SQL_PROJECT SQL_REGION SQL_USER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#env_variables ComposerEnvironment#env_variables}
        :param image_version: The version of the software running in the environment. This encapsulates both the version of Cloud Composer functionality and the version of Apache Airflow. It must match the regular expression composer-([0-9]+(.[0-9]+.[0-9]+(-preview.[0-9]+)?)?|latest)-airflow-([0-9]+(.[0-9]+(.[0-9]+)?)?). The Cloud Composer portion of the image version is a full semantic version, or an alias in the form of major version number or 'latest'. The Apache Airflow portion of the image version is a full semantic version that points to one of the supported Apache Airflow versions, or an alias in the form of only major or major.minor versions specified. See documentation for more details and version list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#image_version ComposerEnvironment#image_version}
        :param pypi_packages: Custom Python Package Index (PyPI) packages to be installed in the environment. Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without pinning it to a version specifier, use the empty string as the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#pypi_packages ComposerEnvironment#pypi_packages}
        :param python_version: The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes. Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use Python major version 3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#python_version ComposerEnvironment#python_version}
        :param scheduler_count: The number of schedulers for Airflow. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler_count ComposerEnvironment#scheduler_count}
        '''
        value = ComposerEnvironmentConfigSoftwareConfig(
            airflow_config_overrides=airflow_config_overrides,
            env_variables=env_variables,
            image_version=image_version,
            pypi_packages=pypi_packages,
            python_version=python_version,
            scheduler_count=scheduler_count,
        )

        return typing.cast(None, jsii.invoke(self, "putSoftwareConfig", [value]))

    @jsii.member(jsii_name="putWebServerConfig")
    def put_web_server_config(self, *, machine_type: builtins.str) -> None:
        '''
        :param machine_type: Optional. Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. If not specified, composer-n1-webserver-2 will be used. Value custom is returned only in response, if Airflow web server parameters were manually changed to a non-standard values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        value = ComposerEnvironmentConfigWebServerConfig(machine_type=machine_type)

        return typing.cast(None, jsii.invoke(self, "putWebServerConfig", [value]))

    @jsii.member(jsii_name="putWebServerNetworkAccessControl")
    def put_web_server_network_access_control(
        self,
        *,
        allowed_ip_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed_ip_range: allowed_ip_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#allowed_ip_range ComposerEnvironment#allowed_ip_range}
        '''
        value = ComposerEnvironmentConfigWebServerNetworkAccessControl(
            allowed_ip_range=allowed_ip_range
        )

        return typing.cast(None, jsii.invoke(self, "putWebServerNetworkAccessControl", [value]))

    @jsii.member(jsii_name="putWorkloadsConfig")
    def put_workloads_config(
        self,
        *,
        scheduler: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigScheduler", typing.Dict[str, typing.Any]]] = None,
        web_server: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigWebServer", typing.Dict[str, typing.Any]]] = None,
        worker: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigWorker", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduler: scheduler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler ComposerEnvironment#scheduler}
        :param web_server: web_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server ComposerEnvironment#web_server}
        :param worker: worker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#worker ComposerEnvironment#worker}
        '''
        value = ComposerEnvironmentConfigWorkloadsConfig(
            scheduler=scheduler, web_server=web_server, worker=worker
        )

        return typing.cast(None, jsii.invoke(self, "putWorkloadsConfig", [value]))

    @jsii.member(jsii_name="resetDatabaseConfig")
    def reset_database_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseConfig", []))

    @jsii.member(jsii_name="resetEncryptionConfig")
    def reset_encryption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfig", []))

    @jsii.member(jsii_name="resetEnvironmentSize")
    def reset_environment_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentSize", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetMasterAuthorizedNetworksConfig")
    def reset_master_authorized_networks_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterAuthorizedNetworksConfig", []))

    @jsii.member(jsii_name="resetNodeConfig")
    def reset_node_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeConfig", []))

    @jsii.member(jsii_name="resetNodeCount")
    def reset_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeCount", []))

    @jsii.member(jsii_name="resetPrivateEnvironmentConfig")
    def reset_private_environment_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateEnvironmentConfig", []))

    @jsii.member(jsii_name="resetSoftwareConfig")
    def reset_software_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareConfig", []))

    @jsii.member(jsii_name="resetWebServerConfig")
    def reset_web_server_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebServerConfig", []))

    @jsii.member(jsii_name="resetWebServerNetworkAccessControl")
    def reset_web_server_network_access_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebServerNetworkAccessControl", []))

    @jsii.member(jsii_name="resetWorkloadsConfig")
    def reset_workloads_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadsConfig", []))

    @builtins.property
    @jsii.member(jsii_name="airflowUri")
    def airflow_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "airflowUri"))

    @builtins.property
    @jsii.member(jsii_name="dagGcsPrefix")
    def dag_gcs_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dagGcsPrefix"))

    @builtins.property
    @jsii.member(jsii_name="databaseConfig")
    def database_config(
        self,
    ) -> "ComposerEnvironmentConfigDatabaseConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigDatabaseConfigOutputReference", jsii.get(self, "databaseConfig"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> "ComposerEnvironmentConfigEncryptionConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigEncryptionConfigOutputReference", jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="gkeCluster")
    def gke_cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeCluster"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> "ComposerEnvironmentConfigMaintenanceWindowOutputReference":
        return typing.cast("ComposerEnvironmentConfigMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(
        self,
    ) -> "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference", jsii.get(self, "masterAuthorizedNetworksConfig"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfig")
    def node_config(self) -> "ComposerEnvironmentConfigNodeConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigNodeConfigOutputReference", jsii.get(self, "nodeConfig"))

    @builtins.property
    @jsii.member(jsii_name="privateEnvironmentConfig")
    def private_environment_config(
        self,
    ) -> "ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference", jsii.get(self, "privateEnvironmentConfig"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfig")
    def software_config(
        self,
    ) -> "ComposerEnvironmentConfigSoftwareConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigSoftwareConfigOutputReference", jsii.get(self, "softwareConfig"))

    @builtins.property
    @jsii.member(jsii_name="webServerConfig")
    def web_server_config(
        self,
    ) -> "ComposerEnvironmentConfigWebServerConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigWebServerConfigOutputReference", jsii.get(self, "webServerConfig"))

    @builtins.property
    @jsii.member(jsii_name="webServerNetworkAccessControl")
    def web_server_network_access_control(
        self,
    ) -> "ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference":
        return typing.cast("ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference", jsii.get(self, "webServerNetworkAccessControl"))

    @builtins.property
    @jsii.member(jsii_name="workloadsConfig")
    def workloads_config(
        self,
    ) -> "ComposerEnvironmentConfigWorkloadsConfigOutputReference":
        return typing.cast("ComposerEnvironmentConfigWorkloadsConfigOutputReference", jsii.get(self, "workloadsConfig"))

    @builtins.property
    @jsii.member(jsii_name="databaseConfigInput")
    def database_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigDatabaseConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigDatabaseConfig"], jsii.get(self, "databaseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigEncryptionConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigEncryptionConfig"], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSizeInput")
    def environment_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigMaintenanceWindow"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="masterAuthorizedNetworksConfigInput")
    def master_authorized_networks_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigMasterAuthorizedNetworksConfig"], jsii.get(self, "masterAuthorizedNetworksConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfigInput")
    def node_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigNodeConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigNodeConfig"], jsii.get(self, "nodeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="privateEnvironmentConfigInput")
    def private_environment_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigPrivateEnvironmentConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigPrivateEnvironmentConfig"], jsii.get(self, "privateEnvironmentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfigInput")
    def software_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigSoftwareConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigSoftwareConfig"], jsii.get(self, "softwareConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="webServerConfigInput")
    def web_server_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWebServerConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWebServerConfig"], jsii.get(self, "webServerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="webServerNetworkAccessControlInput")
    def web_server_network_access_control_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWebServerNetworkAccessControl"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWebServerNetworkAccessControl"], jsii.get(self, "webServerNetworkAccessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadsConfigInput")
    def workloads_config_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfig"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfig"], jsii.get(self, "workloadsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSize")
    def environment_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentSize"))

    @environment_size.setter
    def environment_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigAOutputReference, "environment_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentSize", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigAOutputReference, "node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComposerEnvironmentConfigA]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigDatabaseConfig",
    jsii_struct_bases=[],
    name_mapping={"machine_type": "machineType"},
)
class ComposerEnvironmentConfigDatabaseConfig:
    def __init__(self, *, machine_type: builtins.str) -> None:
        '''
        :param machine_type: Optional. Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. If not specified, db-n1-standard-2 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigDatabaseConfig.__init__)
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "machine_type": machine_type,
        }

    @builtins.property
    def machine_type(self) -> builtins.str:
        '''Optional.

        Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. If not specified, db-n1-standard-2 will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        result = self._values.get("machine_type")
        assert result is not None, "Required property 'machine_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigDatabaseConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigDatabaseConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigDatabaseConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigDatabaseConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigDatabaseConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigDatabaseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigDatabaseConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigDatabaseConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class ComposerEnvironmentConfigEncryptionConfig:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Optional. Customer-managed Encryption Key available through Google's Key Management Service. Cannot be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#kms_key_name ComposerEnvironment#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigEncryptionConfig.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Optional. Customer-managed Encryption Key available through Google's Key Management Service. Cannot be updated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#kms_key_name ComposerEnvironment#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigEncryptionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigEncryptionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigEncryptionConfigOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigEncryptionConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigEncryptionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={
        "end_time": "endTime",
        "recurrence": "recurrence",
        "start_time": "startTime",
    },
)
class ComposerEnvironmentConfigMaintenanceWindow:
    def __init__(
        self,
        *,
        end_time: builtins.str,
        recurrence: builtins.str,
        start_time: builtins.str,
    ) -> None:
        '''
        :param end_time: Maintenance window end time. It is used only to calculate the duration of the maintenance window. The value for end-time must be in the future, relative to 'start_time'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#end_time ComposerEnvironment#end_time}
        :param recurrence: Maintenance window recurrence. Format is a subset of RFC-5545 (https://tools.ietf.org/html/rfc5545) 'RRULE'. The only allowed values for 'FREQ' field are 'FREQ=DAILY' and 'FREQ=WEEKLY;BYDAY=...'. Example values: 'FREQ=WEEKLY;BYDAY=TU,WE', 'FREQ=DAILY'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#recurrence ComposerEnvironment#recurrence}
        :param start_time: Start time of the first recurrence of the maintenance window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#start_time ComposerEnvironment#start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMaintenanceWindow.__init__)
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument recurrence", value=recurrence, expected_type=type_hints["recurrence"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "end_time": end_time,
            "recurrence": recurrence,
            "start_time": start_time,
        }

    @builtins.property
    def end_time(self) -> builtins.str:
        '''Maintenance window end time.

        It is used only to calculate the duration of the maintenance window. The value for end-time must be in the future, relative to 'start_time'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#end_time ComposerEnvironment#end_time}
        '''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence(self) -> builtins.str:
        '''Maintenance window recurrence.

        Format is a subset of RFC-5545 (https://tools.ietf.org/html/rfc5545) 'RRULE'. The only allowed values for 'FREQ' field are 'FREQ=DAILY' and 'FREQ=WEEKLY;BYDAY=...'. Example values: 'FREQ=WEEKLY;BYDAY=TU,WE', 'FREQ=DAILY'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#recurrence ComposerEnvironment#recurrence}
        '''
        result = self._values.get("recurrence")
        assert result is not None, "Required property 'recurrence' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Start time of the first recurrence of the maintenance window.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#start_time ComposerEnvironment#start_time}
        '''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrenceInput")
    def recurrence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMaintenanceWindowOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrence"))

    @recurrence.setter
    def recurrence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMaintenanceWindowOutputReference, "recurrence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMaintenanceWindowOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigMaintenanceWindow]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMasterAuthorizedNetworksConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "cidr_blocks": "cidrBlocks"},
)
class ComposerEnvironmentConfigMasterAuthorizedNetworksConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        cidr_blocks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether or not master authorized networks is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enabled ComposerEnvironment#enabled}
        :param cidr_blocks: cidr_blocks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cidr_blocks ComposerEnvironment#cidr_blocks}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument cidr_blocks", value=cidr_blocks, expected_type=type_hints["cidr_blocks"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if cidr_blocks is not None:
            self._values["cidr_blocks"] = cidr_blocks

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not master authorized networks is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enabled ComposerEnvironment#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def cidr_blocks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks"]]]:
        '''cidr_blocks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cidr_blocks ComposerEnvironment#cidr_blocks}
        '''
        result = self._values.get("cidr_blocks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigMasterAuthorizedNetworksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks",
    jsii_struct_bases=[],
    name_mapping={"cidr_block": "cidrBlock", "display_name": "displayName"},
)
class ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks:
    def __init__(
        self,
        *,
        cidr_block: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cidr_block: cidr_block must be specified in CIDR notation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cidr_block ComposerEnvironment#cidr_block}
        :param display_name: display_name is a field for users to identify CIDR blocks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#display_name ComposerEnvironment#display_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks.__init__)
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "cidr_block": cidr_block,
        }
        if display_name is not None:
            self._values["display_name"] = display_name

    @builtins.property
    def cidr_block(self) -> builtins.str:
        '''cidr_block must be specified in CIDR notation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cidr_block ComposerEnvironment#cidr_block}
        '''
        result = self._values.get("cidr_block")
        assert result is not None, "Required property 'cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''display_name is a field for users to identify CIDR blocks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#display_name ComposerEnvironment#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCidrBlocks")
    def put_cidr_blocks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference.put_cidr_blocks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCidrBlocks", [value]))

    @jsii.member(jsii_name="resetCidrBlocks")
    def reset_cidr_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlocks", []))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList:
        return typing.cast(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList, jsii.get(self, "cidrBlocks"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocksInput")
    def cidr_blocks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks]]], jsii.get(self, "cidrBlocksInput"))

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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigMasterAuthorizedNetworksConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigMasterAuthorizedNetworksConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigMasterAuthorizedNetworksConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigNodeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "disk_size_gb": "diskSizeGb",
        "enable_ip_masq_agent": "enableIpMasqAgent",
        "ip_allocation_policy": "ipAllocationPolicy",
        "machine_type": "machineType",
        "network": "network",
        "oauth_scopes": "oauthScopes",
        "service_account": "serviceAccount",
        "subnetwork": "subnetwork",
        "tags": "tags",
        "zone": "zone",
    },
)
class ComposerEnvironmentConfigNodeConfig:
    def __init__(
        self,
        *,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        enable_ip_masq_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_allocation_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigNodeConfigIpAllocationPolicy", typing.Dict[str, typing.Any]]]]] = None,
        machine_type: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_size_gb: The disk size in GB used for node VMs. Minimum size is 20GB. If unspecified, defaults to 100GB. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#disk_size_gb ComposerEnvironment#disk_size_gb}
        :param enable_ip_masq_agent: Deploys 'ip-masq-agent' daemon set in the GKE cluster and defines nonMasqueradeCIDRs equals to pod IP range so IP masquerading is used for all destination addresses, except between pods traffic. See: https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_ip_masq_agent ComposerEnvironment#enable_ip_masq_agent}
        :param ip_allocation_policy: Configuration for controlling how IPs are allocated in the GKE cluster. Cannot be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#ip_allocation_policy ComposerEnvironment#ip_allocation_policy}
        :param machine_type: The Compute Engine machine type used for cluster instances, specified as a name or relative resource name. For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        :param network: The Compute Engine machine type used for cluster instances, specified as a name or relative resource name. For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. The network must belong to the environment's project. If unspecified, the "default" network ID in the environment's project is used. If a Custom Subnet Network is provided, subnetwork must also be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#network ComposerEnvironment#network}
        :param oauth_scopes: The set of Google API scopes to be made available on all node VMs. Cannot be updated. If empty, defaults to ["https://www.googleapis.com/auth/cloud-platform"]. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#oauth_scopes ComposerEnvironment#oauth_scopes}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. If a service account is not specified, the "default" Compute Engine service account is used. Cannot be updated. If given, note that the service account must have roles/composer.worker for any GCP resources created under the Cloud Composer Environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#service_account ComposerEnvironment#service_account}
        :param subnetwork: The Compute Engine subnetwork to be used for machine communications, , specified as a self-link, relative resource name (e.g. "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided, network must also be provided and the subnetwork must belong to the enclosing environment's project and region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#subnetwork ComposerEnvironment#subnetwork}
        :param tags: The list of instance tags applied to all node VMs. Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with RFC1035. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#tags ComposerEnvironment#tags}
        :param zone: The Compute Engine zone in which to deploy the VMs running the Apache Airflow software, specified as the zone name or relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project and region. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#zone ComposerEnvironment#zone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfig.__init__)
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument enable_ip_masq_agent", value=enable_ip_masq_agent, expected_type=type_hints["enable_ip_masq_agent"])
            check_type(argname="argument ip_allocation_policy", value=ip_allocation_policy, expected_type=type_hints["ip_allocation_policy"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if enable_ip_masq_agent is not None:
            self._values["enable_ip_masq_agent"] = enable_ip_masq_agent
        if ip_allocation_policy is not None:
            self._values["ip_allocation_policy"] = ip_allocation_policy
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if network is not None:
            self._values["network"] = network
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if service_account is not None:
            self._values["service_account"] = service_account
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
        if tags is not None:
            self._values["tags"] = tags
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''The disk size in GB used for node VMs.

        Minimum size is 20GB. If unspecified, defaults to 100GB. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#disk_size_gb ComposerEnvironment#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_ip_masq_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Deploys 'ip-masq-agent' daemon set in the GKE cluster and defines nonMasqueradeCIDRs equals to pod IP range so IP masquerading is used for all destination addresses, except between pods traffic.

        See: https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_ip_masq_agent ComposerEnvironment#enable_ip_masq_agent}
        '''
        result = self._values.get("enable_ip_masq_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_allocation_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigNodeConfigIpAllocationPolicy"]]]:
        '''Configuration for controlling how IPs are allocated in the GKE cluster. Cannot be updated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#ip_allocation_policy ComposerEnvironment#ip_allocation_policy}
        '''
        result = self._values.get("ip_allocation_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigNodeConfigIpAllocationPolicy"]]], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine machine type used for cluster instances, specified as a name or relative resource name.

        For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine machine type used for cluster instances, specified as a name or relative resource name.

        For example: "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and region/zone. The network must belong to the environment's project. If unspecified, the "default" network ID in the environment's project is used. If a Custom Subnet Network is provided, subnetwork must also be provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#network ComposerEnvironment#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of Google API scopes to be made available on all node VMs.

        Cannot be updated. If empty, defaults to ["https://www.googleapis.com/auth/cloud-platform"]. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#oauth_scopes ComposerEnvironment#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Platform Service Account to be used by the node VMs.

        If a service account is not specified, the "default" Compute Engine service account is used. Cannot be updated. If given, note that the service account must have roles/composer.worker for any GCP resources created under the Cloud Composer Environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#service_account ComposerEnvironment#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine subnetwork to be used for machine communications, , specified as a self-link, relative resource name (e.g. "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided, network must also be provided and the subnetwork must belong to the enclosing environment's project and region.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#subnetwork ComposerEnvironment#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of instance tags applied to all node VMs.

        Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with RFC1035. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#tags ComposerEnvironment#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine zone in which to deploy the VMs running the Apache Airflow software, specified as the zone name or relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project and region. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#zone ComposerEnvironment#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigNodeConfigIpAllocationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_ipv4_cidr_block": "clusterIpv4CidrBlock",
        "cluster_secondary_range_name": "clusterSecondaryRangeName",
        "services_ipv4_cidr_block": "servicesIpv4CidrBlock",
        "services_secondary_range_name": "servicesSecondaryRangeName",
        "use_ip_aliases": "useIpAliases",
    },
)
class ComposerEnvironmentConfigNodeConfigIpAllocationPolicy:
    def __init__(
        self,
        *,
        cluster_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        cluster_secondary_range_name: typing.Optional[builtins.str] = None,
        services_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        services_secondary_range_name: typing.Optional[builtins.str] = None,
        use_ip_aliases: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cluster_ipv4_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cluster_ipv4_cidr_block ComposerEnvironment#cluster_ipv4_cidr_block}.
        :param cluster_secondary_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cluster_secondary_range_name ComposerEnvironment#cluster_secondary_range_name}.
        :param services_ipv4_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#services_ipv4_cidr_block ComposerEnvironment#services_ipv4_cidr_block}.
        :param services_secondary_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#services_secondary_range_name ComposerEnvironment#services_secondary_range_name}.
        :param use_ip_aliases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#use_ip_aliases ComposerEnvironment#use_ip_aliases}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigIpAllocationPolicy.__init__)
            check_type(argname="argument cluster_ipv4_cidr_block", value=cluster_ipv4_cidr_block, expected_type=type_hints["cluster_ipv4_cidr_block"])
            check_type(argname="argument cluster_secondary_range_name", value=cluster_secondary_range_name, expected_type=type_hints["cluster_secondary_range_name"])
            check_type(argname="argument services_ipv4_cidr_block", value=services_ipv4_cidr_block, expected_type=type_hints["services_ipv4_cidr_block"])
            check_type(argname="argument services_secondary_range_name", value=services_secondary_range_name, expected_type=type_hints["services_secondary_range_name"])
            check_type(argname="argument use_ip_aliases", value=use_ip_aliases, expected_type=type_hints["use_ip_aliases"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_ipv4_cidr_block is not None:
            self._values["cluster_ipv4_cidr_block"] = cluster_ipv4_cidr_block
        if cluster_secondary_range_name is not None:
            self._values["cluster_secondary_range_name"] = cluster_secondary_range_name
        if services_ipv4_cidr_block is not None:
            self._values["services_ipv4_cidr_block"] = services_ipv4_cidr_block
        if services_secondary_range_name is not None:
            self._values["services_secondary_range_name"] = services_secondary_range_name
        if use_ip_aliases is not None:
            self._values["use_ip_aliases"] = use_ip_aliases

    @builtins.property
    def cluster_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cluster_ipv4_cidr_block ComposerEnvironment#cluster_ipv4_cidr_block}.'''
        result = self._values.get("cluster_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_secondary_range_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cluster_secondary_range_name ComposerEnvironment#cluster_secondary_range_name}.'''
        result = self._values.get("cluster_secondary_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def services_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#services_ipv4_cidr_block ComposerEnvironment#services_ipv4_cidr_block}.'''
        result = self._values.get("services_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def services_secondary_range_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#services_secondary_range_name ComposerEnvironment#services_secondary_range_name}.'''
        result = self._values.get("services_secondary_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_ip_aliases(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#use_ip_aliases ComposerEnvironment#use_ip_aliases}.'''
        result = self._values.get("use_ip_aliases")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigNodeConfigIpAllocationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetClusterIpv4CidrBlock")
    def reset_cluster_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetClusterSecondaryRangeName")
    def reset_cluster_secondary_range_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterSecondaryRangeName", []))

    @jsii.member(jsii_name="resetServicesIpv4CidrBlock")
    def reset_services_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicesIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetServicesSecondaryRangeName")
    def reset_services_secondary_range_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicesSecondaryRangeName", []))

    @jsii.member(jsii_name="resetUseIpAliases")
    def reset_use_ip_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseIpAliases", []))

    @builtins.property
    @jsii.member(jsii_name="clusterIpv4CidrBlockInput")
    def cluster_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecondaryRangeNameInput")
    def cluster_secondary_range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSecondaryRangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesIpv4CidrBlockInput")
    def services_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicesIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesSecondaryRangeNameInput")
    def services_secondary_range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicesSecondaryRangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useIpAliasesInput")
    def use_ip_aliases_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useIpAliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIpv4CidrBlock"))

    @cluster_ipv4_cidr_block.setter
    def cluster_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "cluster_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSecondaryRangeName"))

    @cluster_secondary_range_name.setter
    def cluster_secondary_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "cluster_secondary_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecondaryRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicesIpv4CidrBlock"))

    @services_ipv4_cidr_block.setter
    def services_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "services_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicesIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicesSecondaryRangeName"))

    @services_secondary_range_name.setter
    def services_secondary_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "services_secondary_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicesSecondaryRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="useIpAliases")
    def use_ip_aliases(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useIpAliases"))

    @use_ip_aliases.setter
    def use_ip_aliases(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "use_ip_aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useIpAliases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigNodeConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigNodeConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIpAllocationPolicy")
    def put_ip_allocation_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigNodeConfigOutputReference.put_ip_allocation_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpAllocationPolicy", [value]))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetEnableIpMasqAgent")
    def reset_enable_ip_masq_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIpMasqAgent", []))

    @jsii.member(jsii_name="resetIpAllocationPolicy")
    def reset_ip_allocation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAllocationPolicy", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="ipAllocationPolicy")
    def ip_allocation_policy(
        self,
    ) -> ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList:
        return typing.cast(ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList, jsii.get(self, "ipAllocationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIpMasqAgentInput")
    def enable_ip_masq_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIpMasqAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAllocationPolicyInput")
    def ip_allocation_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigNodeConfigIpAllocationPolicy]]], jsii.get(self, "ipAllocationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="enableIpMasqAgent")
    def enable_ip_masq_agent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIpMasqAgent"))

    @enable_ip_masq_agent.setter
    def enable_ip_masq_agent(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "enable_ip_masq_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpMasqAgent", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComposerEnvironmentConfigNodeConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigNodeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigNodeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigNodeConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigPrivateEnvironmentConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_composer_connection_subnetwork": "cloudComposerConnectionSubnetwork",
        "cloud_composer_network_ipv4_cidr_block": "cloudComposerNetworkIpv4CidrBlock",
        "cloud_sql_ipv4_cidr_block": "cloudSqlIpv4CidrBlock",
        "enable_private_endpoint": "enablePrivateEndpoint",
        "enable_privately_used_public_ips": "enablePrivatelyUsedPublicIps",
        "master_ipv4_cidr_block": "masterIpv4CidrBlock",
        "web_server_ipv4_cidr_block": "webServerIpv4CidrBlock",
    },
)
class ComposerEnvironmentConfigPrivateEnvironmentConfig:
    def __init__(
        self,
        *,
        cloud_composer_connection_subnetwork: typing.Optional[builtins.str] = None,
        cloud_composer_network_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        cloud_sql_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        enable_private_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_privately_used_public_ips: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        web_server_ipv4_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_composer_connection_subnetwork: When specified, the environment will use Private Service Connect instead of VPC peerings to connect to Cloud SQL in the Tenant Project, and the PSC endpoint in the Customer Project will use an IP address from this subnetwork. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_connection_subnetwork ComposerEnvironment#cloud_composer_connection_subnetwork}
        :param cloud_composer_network_ipv4_cidr_block: The CIDR block from which IP range for Cloud Composer Network in tenant project will be reserved. Needs to be disjoint from private_cluster_config.master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_network_ipv4_cidr_block ComposerEnvironment#cloud_composer_network_ipv4_cidr_block}
        :param cloud_sql_ipv4_cidr_block: The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from web_server_ipv4_cidr_block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_sql_ipv4_cidr_block ComposerEnvironment#cloud_sql_ipv4_cidr_block}
        :param enable_private_endpoint: If true, access to the public endpoint of the GKE cluster is denied. If this field is set to true, ip_allocation_policy.use_ip_aliases must be set to true for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_private_endpoint ComposerEnvironment#enable_private_endpoint}
        :param enable_privately_used_public_ips: When enabled, IPs from public (non-RFC1918) ranges can be used for ip_allocation_policy.cluster_ipv4_cidr_block and ip_allocation_policy.service_ipv4_cidr_block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_privately_used_public_ips ComposerEnvironment#enable_privately_used_public_ips}
        :param master_ipv4_cidr_block: The IP range in CIDR notation to use for the hosted master network. This range is used for assigning internal IP addresses to the cluster master or set of masters and to the internal load balancer virtual IP. This range must not overlap with any other ranges in use within the cluster's network. If left blank, the default value of '172.16.0.0/28' is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_ipv4_cidr_block ComposerEnvironment#master_ipv4_cidr_block}
        :param web_server_ipv4_cidr_block: The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_ipv4_cidr_block ComposerEnvironment#web_server_ipv4_cidr_block}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigPrivateEnvironmentConfig.__init__)
            check_type(argname="argument cloud_composer_connection_subnetwork", value=cloud_composer_connection_subnetwork, expected_type=type_hints["cloud_composer_connection_subnetwork"])
            check_type(argname="argument cloud_composer_network_ipv4_cidr_block", value=cloud_composer_network_ipv4_cidr_block, expected_type=type_hints["cloud_composer_network_ipv4_cidr_block"])
            check_type(argname="argument cloud_sql_ipv4_cidr_block", value=cloud_sql_ipv4_cidr_block, expected_type=type_hints["cloud_sql_ipv4_cidr_block"])
            check_type(argname="argument enable_private_endpoint", value=enable_private_endpoint, expected_type=type_hints["enable_private_endpoint"])
            check_type(argname="argument enable_privately_used_public_ips", value=enable_privately_used_public_ips, expected_type=type_hints["enable_privately_used_public_ips"])
            check_type(argname="argument master_ipv4_cidr_block", value=master_ipv4_cidr_block, expected_type=type_hints["master_ipv4_cidr_block"])
            check_type(argname="argument web_server_ipv4_cidr_block", value=web_server_ipv4_cidr_block, expected_type=type_hints["web_server_ipv4_cidr_block"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_composer_connection_subnetwork is not None:
            self._values["cloud_composer_connection_subnetwork"] = cloud_composer_connection_subnetwork
        if cloud_composer_network_ipv4_cidr_block is not None:
            self._values["cloud_composer_network_ipv4_cidr_block"] = cloud_composer_network_ipv4_cidr_block
        if cloud_sql_ipv4_cidr_block is not None:
            self._values["cloud_sql_ipv4_cidr_block"] = cloud_sql_ipv4_cidr_block
        if enable_private_endpoint is not None:
            self._values["enable_private_endpoint"] = enable_private_endpoint
        if enable_privately_used_public_ips is not None:
            self._values["enable_privately_used_public_ips"] = enable_privately_used_public_ips
        if master_ipv4_cidr_block is not None:
            self._values["master_ipv4_cidr_block"] = master_ipv4_cidr_block
        if web_server_ipv4_cidr_block is not None:
            self._values["web_server_ipv4_cidr_block"] = web_server_ipv4_cidr_block

    @builtins.property
    def cloud_composer_connection_subnetwork(self) -> typing.Optional[builtins.str]:
        '''When specified, the environment will use Private Service Connect instead of VPC peerings to connect to Cloud SQL in the Tenant Project, and the PSC endpoint in the Customer Project will use an IP address from this subnetwork.

        This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_connection_subnetwork ComposerEnvironment#cloud_composer_connection_subnetwork}
        '''
        result = self._values.get("cloud_composer_connection_subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_composer_network_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The CIDR block from which IP range for Cloud Composer Network in tenant project will be reserved.

        Needs to be disjoint from private_cluster_config.master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_composer_network_ipv4_cidr_block ComposerEnvironment#cloud_composer_network_ipv4_cidr_block}
        '''
        result = self._values.get("cloud_composer_network_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_sql_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The CIDR block from which IP range in tenant project will be reserved for Cloud SQL.

        Needs to be disjoint from web_server_ipv4_cidr_block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cloud_sql_ipv4_cidr_block ComposerEnvironment#cloud_sql_ipv4_cidr_block}
        '''
        result = self._values.get("cloud_sql_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_private_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, access to the public endpoint of the GKE cluster is denied.

        If this field is set to true, ip_allocation_policy.use_ip_aliases must be set to true for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_private_endpoint ComposerEnvironment#enable_private_endpoint}
        '''
        result = self._values.get("enable_private_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_privately_used_public_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When enabled, IPs from public (non-RFC1918) ranges can be used for ip_allocation_policy.cluster_ipv4_cidr_block and ip_allocation_policy.service_ipv4_cidr_block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#enable_privately_used_public_ips ComposerEnvironment#enable_privately_used_public_ips}
        '''
        result = self._values.get("enable_privately_used_public_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def master_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The IP range in CIDR notation to use for the hosted master network.

        This range is used for assigning internal IP addresses to the cluster master or set of masters and to the internal load balancer virtual IP. This range must not overlap with any other ranges in use within the cluster's network. If left blank, the default value of '172.16.0.0/28' is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#master_ipv4_cidr_block ComposerEnvironment#master_ipv4_cidr_block}
        '''
        result = self._values.get("master_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_server_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The CIDR block from which IP range for web server will be reserved.

        Needs to be disjoint from master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server_ipv4_cidr_block ComposerEnvironment#web_server_ipv4_cidr_block}
        '''
        result = self._values.get("web_server_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigPrivateEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudComposerConnectionSubnetwork")
    def reset_cloud_composer_connection_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudComposerConnectionSubnetwork", []))

    @jsii.member(jsii_name="resetCloudComposerNetworkIpv4CidrBlock")
    def reset_cloud_composer_network_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudComposerNetworkIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetCloudSqlIpv4CidrBlock")
    def reset_cloud_sql_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudSqlIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetEnablePrivateEndpoint")
    def reset_enable_private_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePrivateEndpoint", []))

    @jsii.member(jsii_name="resetEnablePrivatelyUsedPublicIps")
    def reset_enable_privately_used_public_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePrivatelyUsedPublicIps", []))

    @jsii.member(jsii_name="resetMasterIpv4CidrBlock")
    def reset_master_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetWebServerIpv4CidrBlock")
    def reset_web_server_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebServerIpv4CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="cloudComposerConnectionSubnetworkInput")
    def cloud_composer_connection_subnetwork_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudComposerConnectionSubnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudComposerNetworkIpv4CidrBlockInput")
    def cloud_composer_network_ipv4_cidr_block_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudComposerNetworkIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudSqlIpv4CidrBlockInput")
    def cloud_sql_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudSqlIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePrivateEndpointInput")
    def enable_private_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePrivateEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePrivatelyUsedPublicIpsInput")
    def enable_privately_used_public_ips_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePrivatelyUsedPublicIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="masterIpv4CidrBlockInput")
    def master_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="webServerIpv4CidrBlockInput")
    def web_server_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webServerIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudComposerConnectionSubnetwork")
    def cloud_composer_connection_subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudComposerConnectionSubnetwork"))

    @cloud_composer_connection_subnetwork.setter
    def cloud_composer_connection_subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "cloud_composer_connection_subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudComposerConnectionSubnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="cloudComposerNetworkIpv4CidrBlock")
    def cloud_composer_network_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudComposerNetworkIpv4CidrBlock"))

    @cloud_composer_network_ipv4_cidr_block.setter
    def cloud_composer_network_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "cloud_composer_network_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudComposerNetworkIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="cloudSqlIpv4CidrBlock")
    def cloud_sql_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudSqlIpv4CidrBlock"))

    @cloud_sql_ipv4_cidr_block.setter
    def cloud_sql_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "cloud_sql_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudSqlIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePrivateEndpoint"))

    @enable_private_endpoint.setter
    def enable_private_endpoint(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "enable_private_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePrivateEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="enablePrivatelyUsedPublicIps")
    def enable_privately_used_public_ips(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePrivatelyUsedPublicIps"))

    @enable_privately_used_public_ips.setter
    def enable_privately_used_public_ips(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "enable_privately_used_public_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePrivatelyUsedPublicIps", value)

    @builtins.property
    @jsii.member(jsii_name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterIpv4CidrBlock"))

    @master_ipv4_cidr_block.setter
    def master_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "master_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="webServerIpv4CidrBlock")
    def web_server_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webServerIpv4CidrBlock"))

    @web_server_ipv4_cidr_block.setter
    def web_server_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "web_server_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webServerIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigPrivateEnvironmentConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigPrivateEnvironmentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigPrivateEnvironmentConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigSoftwareConfig",
    jsii_struct_bases=[],
    name_mapping={
        "airflow_config_overrides": "airflowConfigOverrides",
        "env_variables": "envVariables",
        "image_version": "imageVersion",
        "pypi_packages": "pypiPackages",
        "python_version": "pythonVersion",
        "scheduler_count": "schedulerCount",
    },
)
class ComposerEnvironmentConfigSoftwareConfig:
    def __init__(
        self,
        *,
        airflow_config_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image_version: typing.Optional[builtins.str] = None,
        pypi_packages: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_version: typing.Optional[builtins.str] = None,
        scheduler_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param airflow_config_overrides: Apache Airflow configuration properties to override. Property keys contain the section and property names, separated by a hyphen, for example "core-dags_are_paused_at_creation". Section names must not contain hyphens ("-"), opening square brackets ("["), or closing square brackets ("]"). The property name must not be empty and cannot contain "=" or ";". Section and property names cannot contain characters: "." Apache Airflow configuration property names must be written in snake_case. Property values can contain any character, and can be written in any lower/upper case format. Certain Apache Airflow configuration property values are blacklisted, and cannot be overridden. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#airflow_config_overrides ComposerEnvironment#airflow_config_overrides}
        :param env_variables: Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes. Environment variable names must match the regular expression [a-zA-Z_][a-zA-Z0-9_]*. They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+), and they cannot match any of the following reserved names: AIRFLOW_HOME C_FORCE_ROOT CONTAINER_NAME DAGS_FOLDER GCP_PROJECT GCS_BUCKET GKE_CLUSTER_NAME SQL_DATABASE SQL_INSTANCE SQL_PASSWORD SQL_PROJECT SQL_REGION SQL_USER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#env_variables ComposerEnvironment#env_variables}
        :param image_version: The version of the software running in the environment. This encapsulates both the version of Cloud Composer functionality and the version of Apache Airflow. It must match the regular expression composer-([0-9]+(.[0-9]+.[0-9]+(-preview.[0-9]+)?)?|latest)-airflow-([0-9]+(.[0-9]+(.[0-9]+)?)?). The Cloud Composer portion of the image version is a full semantic version, or an alias in the form of major version number or 'latest'. The Apache Airflow portion of the image version is a full semantic version that points to one of the supported Apache Airflow versions, or an alias in the form of only major or major.minor versions specified. See documentation for more details and version list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#image_version ComposerEnvironment#image_version}
        :param pypi_packages: Custom Python Package Index (PyPI) packages to be installed in the environment. Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without pinning it to a version specifier, use the empty string as the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#pypi_packages ComposerEnvironment#pypi_packages}
        :param python_version: The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes. Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use Python major version 3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#python_version ComposerEnvironment#python_version}
        :param scheduler_count: The number of schedulers for Airflow. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler_count ComposerEnvironment#scheduler_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigSoftwareConfig.__init__)
            check_type(argname="argument airflow_config_overrides", value=airflow_config_overrides, expected_type=type_hints["airflow_config_overrides"])
            check_type(argname="argument env_variables", value=env_variables, expected_type=type_hints["env_variables"])
            check_type(argname="argument image_version", value=image_version, expected_type=type_hints["image_version"])
            check_type(argname="argument pypi_packages", value=pypi_packages, expected_type=type_hints["pypi_packages"])
            check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
            check_type(argname="argument scheduler_count", value=scheduler_count, expected_type=type_hints["scheduler_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if airflow_config_overrides is not None:
            self._values["airflow_config_overrides"] = airflow_config_overrides
        if env_variables is not None:
            self._values["env_variables"] = env_variables
        if image_version is not None:
            self._values["image_version"] = image_version
        if pypi_packages is not None:
            self._values["pypi_packages"] = pypi_packages
        if python_version is not None:
            self._values["python_version"] = python_version
        if scheduler_count is not None:
            self._values["scheduler_count"] = scheduler_count

    @builtins.property
    def airflow_config_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Apache Airflow configuration properties to override.

        Property keys contain the section and property names, separated by a hyphen, for example "core-dags_are_paused_at_creation". Section names must not contain hyphens ("-"), opening square brackets ("["), or closing square brackets ("]"). The property name must not be empty and cannot contain "=" or ";". Section and property names cannot contain characters: "." Apache Airflow configuration property names must be written in snake_case. Property values can contain any character, and can be written in any lower/upper case format. Certain Apache Airflow configuration property values are blacklisted, and cannot be overridden.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#airflow_config_overrides ComposerEnvironment#airflow_config_overrides}
        '''
        result = self._values.get("airflow_config_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def env_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.

        Environment variable names must match the regular expression [a-zA-Z_][a-zA-Z0-9_]*. They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+), and they cannot match any of the following reserved names: AIRFLOW_HOME C_FORCE_ROOT CONTAINER_NAME DAGS_FOLDER GCP_PROJECT GCS_BUCKET GKE_CLUSTER_NAME SQL_DATABASE SQL_INSTANCE SQL_PASSWORD SQL_PROJECT SQL_REGION SQL_USER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#env_variables ComposerEnvironment#env_variables}
        '''
        result = self._values.get("env_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def image_version(self) -> typing.Optional[builtins.str]:
        '''The version of the software running in the environment.

        This encapsulates both the version of Cloud Composer functionality and the version of Apache Airflow. It must match the regular expression composer-([0-9]+(.[0-9]+.[0-9]+(-preview.[0-9]+)?)?|latest)-airflow-([0-9]+(.[0-9]+(.[0-9]+)?)?). The Cloud Composer portion of the image version is a full semantic version, or an alias in the form of major version number or 'latest'. The Apache Airflow portion of the image version is a full semantic version that points to one of the supported Apache Airflow versions, or an alias in the form of only major or major.minor versions specified. See documentation for more details and version list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#image_version ComposerEnvironment#image_version}
        '''
        result = self._values.get("image_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pypi_packages(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom Python Package Index (PyPI) packages to be installed in the environment.

        Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without pinning it to a version specifier, use the empty string as the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#pypi_packages ComposerEnvironment#pypi_packages}
        '''
        result = self._values.get("pypi_packages")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def python_version(self) -> typing.Optional[builtins.str]:
        '''The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.

        Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use Python major version 3.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#python_version ComposerEnvironment#python_version}
        '''
        result = self._values.get("python_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduler_count(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers for Airflow. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler_count ComposerEnvironment#scheduler_count}
        '''
        result = self._values.get("scheduler_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigSoftwareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigSoftwareConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigSoftwareConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigSoftwareConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAirflowConfigOverrides")
    def reset_airflow_config_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAirflowConfigOverrides", []))

    @jsii.member(jsii_name="resetEnvVariables")
    def reset_env_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvVariables", []))

    @jsii.member(jsii_name="resetImageVersion")
    def reset_image_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersion", []))

    @jsii.member(jsii_name="resetPypiPackages")
    def reset_pypi_packages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPypiPackages", []))

    @jsii.member(jsii_name="resetPythonVersion")
    def reset_python_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonVersion", []))

    @jsii.member(jsii_name="resetSchedulerCount")
    def reset_scheduler_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulerCount", []))

    @builtins.property
    @jsii.member(jsii_name="airflowConfigOverridesInput")
    def airflow_config_overrides_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "airflowConfigOverridesInput"))

    @builtins.property
    @jsii.member(jsii_name="envVariablesInput")
    def env_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "envVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionInput")
    def image_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pypiPackagesInput")
    def pypi_packages_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "pypiPackagesInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonVersionInput")
    def python_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pythonVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulerCountInput")
    def scheduler_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="airflowConfigOverrides")
    def airflow_config_overrides(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "airflowConfigOverrides"))

    @airflow_config_overrides.setter
    def airflow_config_overrides(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "airflow_config_overrides").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowConfigOverrides", value)

    @builtins.property
    @jsii.member(jsii_name="envVariables")
    def env_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "envVariables"))

    @env_variables.setter
    def env_variables(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "env_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "envVariables", value)

    @builtins.property
    @jsii.member(jsii_name="imageVersion")
    def image_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageVersion"))

    @image_version.setter
    def image_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "image_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pypiPackages")
    def pypi_packages(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "pypiPackages"))

    @pypi_packages.setter
    def pypi_packages(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "pypi_packages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pypiPackages", value)

    @builtins.property
    @jsii.member(jsii_name="pythonVersion")
    def python_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pythonVersion"))

    @python_version.setter
    def python_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "python_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonVersion", value)

    @builtins.property
    @jsii.member(jsii_name="schedulerCount")
    def scheduler_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "schedulerCount"))

    @scheduler_count.setter
    def scheduler_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "scheduler_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigSoftwareConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigSoftwareConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigSoftwareConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigSoftwareConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerConfig",
    jsii_struct_bases=[],
    name_mapping={"machine_type": "machineType"},
)
class ComposerEnvironmentConfigWebServerConfig:
    def __init__(self, *, machine_type: builtins.str) -> None:
        '''
        :param machine_type: Optional. Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. If not specified, composer-n1-webserver-2 will be used. Value custom is returned only in response, if Airflow web server parameters were manually changed to a non-standard values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerConfig.__init__)
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "machine_type": machine_type,
        }

    @builtins.property
    def machine_type(self) -> builtins.str:
        '''Optional.

        Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. If not specified, composer-n1-webserver-2 will be used. Value custom is returned only in response, if Airflow web server parameters were manually changed to a non-standard values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#machine_type ComposerEnvironment#machine_type}
        '''
        result = self._values.get("machine_type")
        assert result is not None, "Required property 'machine_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWebServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWebServerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWebServerConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWebServerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWebServerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerNetworkAccessControl",
    jsii_struct_bases=[],
    name_mapping={"allowed_ip_range": "allowedIpRange"},
)
class ComposerEnvironmentConfigWebServerNetworkAccessControl:
    def __init__(
        self,
        *,
        allowed_ip_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed_ip_range: allowed_ip_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#allowed_ip_range ComposerEnvironment#allowed_ip_range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControl.__init__)
            check_type(argname="argument allowed_ip_range", value=allowed_ip_range, expected_type=type_hints["allowed_ip_range"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_ip_range is not None:
            self._values["allowed_ip_range"] = allowed_ip_range

    @builtins.property
    def allowed_ip_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange"]]]:
        '''allowed_ip_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#allowed_ip_range ComposerEnvironment#allowed_ip_range}
        '''
        result = self._values.get("allowed_ip_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWebServerNetworkAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "description": "description"},
)
class ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange:
    def __init__(
        self,
        *,
        value: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: IP address or range, defined using CIDR notation, of requests that this rule applies to. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. IP range prefixes should be properly truncated. For example, 1.2.3.4/24 should be truncated to 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 should be truncated to 2001:db8::/32. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#value ComposerEnvironment#value}
        :param description: A description of this ip range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#description ComposerEnvironment#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def value(self) -> builtins.str:
        '''IP address or range, defined using CIDR notation, of requests that this rule applies to.

        Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. IP range prefixes should be properly truncated. For example, 1.2.3.4/24 should be truncated to 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 should be truncated to 2001:db8::/32.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#value ComposerEnvironment#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this ip range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#description ComposerEnvironment#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedIpRange")
    def put_allowed_ip_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference.put_allowed_ip_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedIpRange", [value]))

    @jsii.member(jsii_name="resetAllowedIpRange")
    def reset_allowed_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedIpRange", []))

    @builtins.property
    @jsii.member(jsii_name="allowedIpRange")
    def allowed_ip_range(
        self,
    ) -> ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList:
        return typing.cast(ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList, jsii.get(self, "allowedIpRange"))

    @builtins.property
    @jsii.member(jsii_name="allowedIpRangeInput")
    def allowed_ip_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]], jsii.get(self, "allowedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWebServerNetworkAccessControl]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWebServerNetworkAccessControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWebServerNetworkAccessControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "scheduler": "scheduler",
        "web_server": "webServer",
        "worker": "worker",
    },
)
class ComposerEnvironmentConfigWorkloadsConfig:
    def __init__(
        self,
        *,
        scheduler: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigScheduler", typing.Dict[str, typing.Any]]] = None,
        web_server: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigWebServer", typing.Dict[str, typing.Any]]] = None,
        worker: typing.Optional[typing.Union["ComposerEnvironmentConfigWorkloadsConfigWorker", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduler: scheduler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler ComposerEnvironment#scheduler}
        :param web_server: web_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server ComposerEnvironment#web_server}
        :param worker: worker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#worker ComposerEnvironment#worker}
        '''
        if isinstance(scheduler, dict):
            scheduler = ComposerEnvironmentConfigWorkloadsConfigScheduler(**scheduler)
        if isinstance(web_server, dict):
            web_server = ComposerEnvironmentConfigWorkloadsConfigWebServer(**web_server)
        if isinstance(worker, dict):
            worker = ComposerEnvironmentConfigWorkloadsConfigWorker(**worker)
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfig.__init__)
            check_type(argname="argument scheduler", value=scheduler, expected_type=type_hints["scheduler"])
            check_type(argname="argument web_server", value=web_server, expected_type=type_hints["web_server"])
            check_type(argname="argument worker", value=worker, expected_type=type_hints["worker"])
        self._values: typing.Dict[str, typing.Any] = {}
        if scheduler is not None:
            self._values["scheduler"] = scheduler
        if web_server is not None:
            self._values["web_server"] = web_server
        if worker is not None:
            self._values["worker"] = worker

    @builtins.property
    def scheduler(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigScheduler"]:
        '''scheduler block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#scheduler ComposerEnvironment#scheduler}
        '''
        result = self._values.get("scheduler")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigScheduler"], result)

    @builtins.property
    def web_server(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWebServer"]:
        '''web_server block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#web_server ComposerEnvironment#web_server}
        '''
        result = self._values.get("web_server")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWebServer"], result)

    @builtins.property
    def worker(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWorker"]:
        '''worker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#worker ComposerEnvironment#worker}
        '''
        result = self._values.get("worker")
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWorker"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWorkloadsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWorkloadsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScheduler")
    def put_scheduler(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        cpu: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The number of schedulers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#count ComposerEnvironment#count}
        :param cpu: CPU request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param memory_gb: Memory (GB) request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param storage_gb: Storage (GB) request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        value = ComposerEnvironmentConfigWorkloadsConfigScheduler(
            count=count, cpu=cpu, memory_gb=memory_gb, storage_gb=storage_gb
        )

        return typing.cast(None, jsii.invoke(self, "putScheduler", [value]))

    @jsii.member(jsii_name="putWebServer")
    def put_web_server(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: CPU request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param memory_gb: Memory (GB) request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param storage_gb: Storage (GB) request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        value = ComposerEnvironmentConfigWorkloadsConfigWebServer(
            cpu=cpu, memory_gb=memory_gb, storage_gb=storage_gb
        )

        return typing.cast(None, jsii.invoke(self, "putWebServer", [value]))

    @jsii.member(jsii_name="putWorker")
    def put_worker(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        max_count: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        min_count: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: CPU request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param max_count: Maximum number of workers for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#max_count ComposerEnvironment#max_count}
        :param memory_gb: Memory (GB) request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param min_count: Minimum number of workers for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#min_count ComposerEnvironment#min_count}
        :param storage_gb: Storage (GB) request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        value = ComposerEnvironmentConfigWorkloadsConfigWorker(
            cpu=cpu,
            max_count=max_count,
            memory_gb=memory_gb,
            min_count=min_count,
            storage_gb=storage_gb,
        )

        return typing.cast(None, jsii.invoke(self, "putWorker", [value]))

    @jsii.member(jsii_name="resetScheduler")
    def reset_scheduler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduler", []))

    @jsii.member(jsii_name="resetWebServer")
    def reset_web_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebServer", []))

    @jsii.member(jsii_name="resetWorker")
    def reset_worker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorker", []))

    @builtins.property
    @jsii.member(jsii_name="scheduler")
    def scheduler(
        self,
    ) -> "ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference":
        return typing.cast("ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference", jsii.get(self, "scheduler"))

    @builtins.property
    @jsii.member(jsii_name="webServer")
    def web_server(
        self,
    ) -> "ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference":
        return typing.cast("ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference", jsii.get(self, "webServer"))

    @builtins.property
    @jsii.member(jsii_name="worker")
    def worker(self) -> "ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference":
        return typing.cast("ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference", jsii.get(self, "worker"))

    @builtins.property
    @jsii.member(jsii_name="schedulerInput")
    def scheduler_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigScheduler"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigScheduler"], jsii.get(self, "schedulerInput"))

    @builtins.property
    @jsii.member(jsii_name="webServerInput")
    def web_server_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWebServer"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWebServer"], jsii.get(self, "webServerInput"))

    @builtins.property
    @jsii.member(jsii_name="workerInput")
    def worker_input(
        self,
    ) -> typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWorker"]:
        return typing.cast(typing.Optional["ComposerEnvironmentConfigWorkloadsConfigWorker"], jsii.get(self, "workerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWorkloadsConfig]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWorkloadsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWorkloadsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigScheduler",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "cpu": "cpu",
        "memory_gb": "memoryGb",
        "storage_gb": "storageGb",
    },
)
class ComposerEnvironmentConfigWorkloadsConfigScheduler:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        cpu: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The number of schedulers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#count ComposerEnvironment#count}
        :param cpu: CPU request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param memory_gb: Memory (GB) request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param storage_gb: Storage (GB) request and limit for a single Airflow scheduler replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigScheduler.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory_gb", value=memory_gb, expected_type=type_hints["memory_gb"])
            check_type(argname="argument storage_gb", value=storage_gb, expected_type=type_hints["storage_gb"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory_gb is not None:
            self._values["memory_gb"] = memory_gb
        if storage_gb is not None:
            self._values["storage_gb"] = storage_gb

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#count ComposerEnvironment#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''CPU request and limit for a single Airflow scheduler replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Memory (GB) request and limit for a single Airflow scheduler replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        '''
        result = self._values.get("memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_gb(self) -> typing.Optional[jsii.Number]:
        '''Storage (GB) request and limit for a single Airflow scheduler replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        result = self._values.get("storage_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWorkloadsConfigScheduler(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMemoryGb")
    def reset_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGb", []))

    @jsii.member(jsii_name="resetStorageGb")
    def reset_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageGb", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGbInput")
    def memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="storageGbInput")
    def storage_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="memoryGb")
    def memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryGb"))

    @memory_gb.setter
    def memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference, "memory_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="storageGb")
    def storage_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageGb"))

    @storage_gb.setter
    def storage_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference, "storage_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWorkloadsConfigScheduler]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWorkloadsConfigScheduler], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWorkloadsConfigScheduler],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigWebServer",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory_gb": "memoryGb", "storage_gb": "storageGb"},
)
class ComposerEnvironmentConfigWorkloadsConfigWebServer:
    def __init__(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: CPU request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param memory_gb: Memory (GB) request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param storage_gb: Storage (GB) request and limit for Airflow web server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigWebServer.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory_gb", value=memory_gb, expected_type=type_hints["memory_gb"])
            check_type(argname="argument storage_gb", value=storage_gb, expected_type=type_hints["storage_gb"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory_gb is not None:
            self._values["memory_gb"] = memory_gb
        if storage_gb is not None:
            self._values["storage_gb"] = storage_gb

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''CPU request and limit for Airflow web server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Memory (GB) request and limit for Airflow web server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        '''
        result = self._values.get("memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_gb(self) -> typing.Optional[jsii.Number]:
        '''Storage (GB) request and limit for Airflow web server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        result = self._values.get("storage_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWorkloadsConfigWebServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMemoryGb")
    def reset_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGb", []))

    @jsii.member(jsii_name="resetStorageGb")
    def reset_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageGb", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGbInput")
    def memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="storageGbInput")
    def storage_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="memoryGb")
    def memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryGb"))

    @memory_gb.setter
    def memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference, "memory_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="storageGb")
    def storage_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageGb"))

    @storage_gb.setter
    def storage_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference, "storage_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWebServer]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWebServer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWebServer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigWorker",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "max_count": "maxCount",
        "memory_gb": "memoryGb",
        "min_count": "minCount",
        "storage_gb": "storageGb",
    },
)
class ComposerEnvironmentConfigWorkloadsConfigWorker:
    def __init__(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        max_count: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        min_count: typing.Optional[jsii.Number] = None,
        storage_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: CPU request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        :param max_count: Maximum number of workers for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#max_count ComposerEnvironment#max_count}
        :param memory_gb: Memory (GB) request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        :param min_count: Minimum number of workers for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#min_count ComposerEnvironment#min_count}
        :param storage_gb: Storage (GB) request and limit for a single Airflow worker replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigWorker.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument max_count", value=max_count, expected_type=type_hints["max_count"])
            check_type(argname="argument memory_gb", value=memory_gb, expected_type=type_hints["memory_gb"])
            check_type(argname="argument min_count", value=min_count, expected_type=type_hints["min_count"])
            check_type(argname="argument storage_gb", value=storage_gb, expected_type=type_hints["storage_gb"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if max_count is not None:
            self._values["max_count"] = max_count
        if memory_gb is not None:
            self._values["memory_gb"] = memory_gb
        if min_count is not None:
            self._values["min_count"] = min_count
        if storage_gb is not None:
            self._values["storage_gb"] = storage_gb

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''CPU request and limit for a single Airflow worker replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#cpu ComposerEnvironment#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_count(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of workers for autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#max_count ComposerEnvironment#max_count}
        '''
        result = self._values.get("max_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Memory (GB) request and limit for a single Airflow worker replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#memory_gb ComposerEnvironment#memory_gb}
        '''
        result = self._values.get("memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_count(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of workers for autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#min_count ComposerEnvironment#min_count}
        '''
        result = self._values.get("min_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_gb(self) -> typing.Optional[jsii.Number]:
        '''Storage (GB) request and limit for a single Airflow worker replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#storage_gb ComposerEnvironment#storage_gb}
        '''
        result = self._values.get("storage_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentConfigWorkloadsConfigWorker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMaxCount")
    def reset_max_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCount", []))

    @jsii.member(jsii_name="resetMemoryGb")
    def reset_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGb", []))

    @jsii.member(jsii_name="resetMinCount")
    def reset_min_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCount", []))

    @jsii.member(jsii_name="resetStorageGb")
    def reset_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageGb", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCountInput")
    def max_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCountInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGbInput")
    def memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="minCountInput")
    def min_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCountInput"))

    @builtins.property
    @jsii.member(jsii_name="storageGbInput")
    def storage_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="maxCount")
    def max_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCount"))

    @max_count.setter
    def max_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "max_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCount", value)

    @builtins.property
    @jsii.member(jsii_name="memoryGb")
    def memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryGb"))

    @memory_gb.setter
    def memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "memory_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="minCount")
    def min_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCount"))

    @min_count.setter
    def min_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "min_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCount", value)

    @builtins.property
    @jsii.member(jsii_name="storageGb")
    def storage_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageGb"))

    @storage_gb.setter
    def storage_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "storage_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWorker]:
        return typing.cast(typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWorker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComposerEnvironmentConfigWorkloadsConfigWorker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComposerEnvironmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#create ComposerEnvironment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#delete ComposerEnvironment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#update ComposerEnvironment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComposerEnvironmentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#create ComposerEnvironment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#delete ComposerEnvironment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/composer_environment#update ComposerEnvironment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComposerEnvironmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComposerEnvironmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.composerEnvironment.ComposerEnvironmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComposerEnvironmentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComposerEnvironmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComposerEnvironmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComposerEnvironmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComposerEnvironmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComposerEnvironment",
    "ComposerEnvironmentConfig",
    "ComposerEnvironmentConfigA",
    "ComposerEnvironmentConfigAOutputReference",
    "ComposerEnvironmentConfigDatabaseConfig",
    "ComposerEnvironmentConfigDatabaseConfigOutputReference",
    "ComposerEnvironmentConfigEncryptionConfig",
    "ComposerEnvironmentConfigEncryptionConfigOutputReference",
    "ComposerEnvironmentConfigMaintenanceWindow",
    "ComposerEnvironmentConfigMaintenanceWindowOutputReference",
    "ComposerEnvironmentConfigMasterAuthorizedNetworksConfig",
    "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocks",
    "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksList",
    "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlocksOutputReference",
    "ComposerEnvironmentConfigMasterAuthorizedNetworksConfigOutputReference",
    "ComposerEnvironmentConfigNodeConfig",
    "ComposerEnvironmentConfigNodeConfigIpAllocationPolicy",
    "ComposerEnvironmentConfigNodeConfigIpAllocationPolicyList",
    "ComposerEnvironmentConfigNodeConfigIpAllocationPolicyOutputReference",
    "ComposerEnvironmentConfigNodeConfigOutputReference",
    "ComposerEnvironmentConfigPrivateEnvironmentConfig",
    "ComposerEnvironmentConfigPrivateEnvironmentConfigOutputReference",
    "ComposerEnvironmentConfigSoftwareConfig",
    "ComposerEnvironmentConfigSoftwareConfigOutputReference",
    "ComposerEnvironmentConfigWebServerConfig",
    "ComposerEnvironmentConfigWebServerConfigOutputReference",
    "ComposerEnvironmentConfigWebServerNetworkAccessControl",
    "ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRange",
    "ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeList",
    "ComposerEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeOutputReference",
    "ComposerEnvironmentConfigWebServerNetworkAccessControlOutputReference",
    "ComposerEnvironmentConfigWorkloadsConfig",
    "ComposerEnvironmentConfigWorkloadsConfigOutputReference",
    "ComposerEnvironmentConfigWorkloadsConfigScheduler",
    "ComposerEnvironmentConfigWorkloadsConfigSchedulerOutputReference",
    "ComposerEnvironmentConfigWorkloadsConfigWebServer",
    "ComposerEnvironmentConfigWorkloadsConfigWebServerOutputReference",
    "ComposerEnvironmentConfigWorkloadsConfigWorker",
    "ComposerEnvironmentConfigWorkloadsConfigWorkerOutputReference",
    "ComposerEnvironmentTimeouts",
    "ComposerEnvironmentTimeoutsOutputReference",
]

publication.publish()
