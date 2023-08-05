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


class DnsManagedZone(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZone",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone google_dns_managed_zone}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dns_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dnssec_config: typing.Optional[typing.Union["DnsManagedZoneDnssecConfig", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_config: typing.Optional[typing.Union["DnsManagedZoneForwardingConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        peering_config: typing.Optional[typing.Union["DnsManagedZonePeeringConfig", typing.Dict[str, typing.Any]]] = None,
        private_visibility_config: typing.Optional[typing.Union["DnsManagedZonePrivateVisibilityConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DnsManagedZoneTimeouts", typing.Dict[str, typing.Any]]] = None,
        visibility: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone google_dns_managed_zone} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dns_name: The DNS name of this managed zone, for instance "example.com.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dns_name DnsManagedZone#dns_name}
        :param name: User assigned name for this resource. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#name DnsManagedZone#name}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#description DnsManagedZone#description}
        :param dnssec_config: dnssec_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dnssec_config DnsManagedZone#dnssec_config}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#force_destroy DnsManagedZone#force_destroy}.
        :param forwarding_config: forwarding_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#forwarding_config DnsManagedZone#forwarding_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#id DnsManagedZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this ManagedZone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#labels DnsManagedZone#labels}
        :param peering_config: peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#peering_config DnsManagedZone#peering_config}
        :param private_visibility_config: private_visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#private_visibility_config DnsManagedZone#private_visibility_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#project DnsManagedZone#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#timeouts DnsManagedZone#timeouts}
        :param visibility: The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. Default value: "public" Possible values: ["private", "public"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#visibility DnsManagedZone#visibility}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZone.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DnsManagedZoneConfig(
            dns_name=dns_name,
            name=name,
            description=description,
            dnssec_config=dnssec_config,
            force_destroy=force_destroy,
            forwarding_config=forwarding_config,
            id=id,
            labels=labels,
            peering_config=peering_config,
            private_visibility_config=private_visibility_config,
            project=project,
            timeouts=timeouts,
            visibility=visibility,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDnssecConfig")
    def put_dnssec_config(
        self,
        *,
        default_key_specs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZoneDnssecConfigDefaultKeySpecs", typing.Dict[str, typing.Any]]]]] = None,
        kind: typing.Optional[builtins.str] = None,
        non_existence: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_key_specs: default_key_specs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#default_key_specs DnsManagedZone#default_key_specs}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#kind DnsManagedZone#kind}
        :param non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses. non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#non_existence DnsManagedZone#non_existence}
        :param state: Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#state DnsManagedZone#state}
        '''
        value = DnsManagedZoneDnssecConfig(
            default_key_specs=default_key_specs,
            kind=kind,
            non_existence=non_existence,
            state=state,
        )

        return typing.cast(None, jsii.invoke(self, "putDnssecConfig", [value]))

    @jsii.member(jsii_name="putForwardingConfig")
    def put_forwarding_config(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_name_servers DnsManagedZone#target_name_servers}
        '''
        value = DnsManagedZoneForwardingConfig(target_name_servers=target_name_servers)

        return typing.cast(None, jsii.invoke(self, "putForwardingConfig", [value]))

    @jsii.member(jsii_name="putPeeringConfig")
    def put_peering_config(
        self,
        *,
        target_network: typing.Union["DnsManagedZonePeeringConfigTargetNetwork", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target_network: target_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_network DnsManagedZone#target_network}
        '''
        value = DnsManagedZonePeeringConfig(target_network=target_network)

        return typing.cast(None, jsii.invoke(self, "putPeeringConfig", [value]))

    @jsii.member(jsii_name="putPrivateVisibilityConfig")
    def put_private_visibility_config(
        self,
        *,
        networks: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZonePrivateVisibilityConfigNetworks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#networks DnsManagedZone#networks}
        '''
        value = DnsManagedZonePrivateVisibilityConfig(networks=networks)

        return typing.cast(None, jsii.invoke(self, "putPrivateVisibilityConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#create DnsManagedZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#delete DnsManagedZone#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#update DnsManagedZone#update}.
        '''
        value = DnsManagedZoneTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDnssecConfig")
    def reset_dnssec_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnssecConfig", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetForwardingConfig")
    def reset_forwarding_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPeeringConfig")
    def reset_peering_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeeringConfig", []))

    @jsii.member(jsii_name="resetPrivateVisibilityConfig")
    def reset_private_visibility_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateVisibilityConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

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
    @jsii.member(jsii_name="dnssecConfig")
    def dnssec_config(self) -> "DnsManagedZoneDnssecConfigOutputReference":
        return typing.cast("DnsManagedZoneDnssecConfigOutputReference", jsii.get(self, "dnssecConfig"))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfig")
    def forwarding_config(self) -> "DnsManagedZoneForwardingConfigOutputReference":
        return typing.cast("DnsManagedZoneForwardingConfigOutputReference", jsii.get(self, "forwardingConfig"))

    @builtins.property
    @jsii.member(jsii_name="managedZoneId")
    def managed_zone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="nameServers")
    def name_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameServers"))

    @builtins.property
    @jsii.member(jsii_name="peeringConfig")
    def peering_config(self) -> "DnsManagedZonePeeringConfigOutputReference":
        return typing.cast("DnsManagedZonePeeringConfigOutputReference", jsii.get(self, "peeringConfig"))

    @builtins.property
    @jsii.member(jsii_name="privateVisibilityConfig")
    def private_visibility_config(
        self,
    ) -> "DnsManagedZonePrivateVisibilityConfigOutputReference":
        return typing.cast("DnsManagedZonePrivateVisibilityConfigOutputReference", jsii.get(self, "privateVisibilityConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DnsManagedZoneTimeoutsOutputReference":
        return typing.cast("DnsManagedZoneTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dnssecConfigInput")
    def dnssec_config_input(self) -> typing.Optional["DnsManagedZoneDnssecConfig"]:
        return typing.cast(typing.Optional["DnsManagedZoneDnssecConfig"], jsii.get(self, "dnssecConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfigInput")
    def forwarding_config_input(
        self,
    ) -> typing.Optional["DnsManagedZoneForwardingConfig"]:
        return typing.cast(typing.Optional["DnsManagedZoneForwardingConfig"], jsii.get(self, "forwardingConfigInput"))

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
    @jsii.member(jsii_name="peeringConfigInput")
    def peering_config_input(self) -> typing.Optional["DnsManagedZonePeeringConfig"]:
        return typing.cast(typing.Optional["DnsManagedZonePeeringConfig"], jsii.get(self, "peeringConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="privateVisibilityConfigInput")
    def private_visibility_config_input(
        self,
    ) -> typing.Optional["DnsManagedZonePrivateVisibilityConfig"]:
        return typing.cast(typing.Optional["DnsManagedZonePrivateVisibilityConfig"], jsii.get(self, "privateVisibilityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DnsManagedZoneTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DnsManagedZoneTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "dns_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value)

    @builtins.property
    @jsii.member(jsii_name="forceDestroy")
    def force_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDestroy"))

    @force_destroy.setter
    def force_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "force_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZone, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dns_name": "dnsName",
        "name": "name",
        "description": "description",
        "dnssec_config": "dnssecConfig",
        "force_destroy": "forceDestroy",
        "forwarding_config": "forwardingConfig",
        "id": "id",
        "labels": "labels",
        "peering_config": "peeringConfig",
        "private_visibility_config": "privateVisibilityConfig",
        "project": "project",
        "timeouts": "timeouts",
        "visibility": "visibility",
    },
)
class DnsManagedZoneConfig(cdktf.TerraformMetaArguments):
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
        dns_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dnssec_config: typing.Optional[typing.Union["DnsManagedZoneDnssecConfig", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_config: typing.Optional[typing.Union["DnsManagedZoneForwardingConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        peering_config: typing.Optional[typing.Union["DnsManagedZonePeeringConfig", typing.Dict[str, typing.Any]]] = None,
        private_visibility_config: typing.Optional[typing.Union["DnsManagedZonePrivateVisibilityConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DnsManagedZoneTimeouts", typing.Dict[str, typing.Any]]] = None,
        visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dns_name: The DNS name of this managed zone, for instance "example.com.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dns_name DnsManagedZone#dns_name}
        :param name: User assigned name for this resource. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#name DnsManagedZone#name}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#description DnsManagedZone#description}
        :param dnssec_config: dnssec_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dnssec_config DnsManagedZone#dnssec_config}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#force_destroy DnsManagedZone#force_destroy}.
        :param forwarding_config: forwarding_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#forwarding_config DnsManagedZone#forwarding_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#id DnsManagedZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this ManagedZone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#labels DnsManagedZone#labels}
        :param peering_config: peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#peering_config DnsManagedZone#peering_config}
        :param private_visibility_config: private_visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#private_visibility_config DnsManagedZone#private_visibility_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#project DnsManagedZone#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#timeouts DnsManagedZone#timeouts}
        :param visibility: The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. Default value: "public" Possible values: ["private", "public"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#visibility DnsManagedZone#visibility}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dnssec_config, dict):
            dnssec_config = DnsManagedZoneDnssecConfig(**dnssec_config)
        if isinstance(forwarding_config, dict):
            forwarding_config = DnsManagedZoneForwardingConfig(**forwarding_config)
        if isinstance(peering_config, dict):
            peering_config = DnsManagedZonePeeringConfig(**peering_config)
        if isinstance(private_visibility_config, dict):
            private_visibility_config = DnsManagedZonePrivateVisibilityConfig(**private_visibility_config)
        if isinstance(timeouts, dict):
            timeouts = DnsManagedZoneTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dnssec_config", value=dnssec_config, expected_type=type_hints["dnssec_config"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument forwarding_config", value=forwarding_config, expected_type=type_hints["forwarding_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument peering_config", value=peering_config, expected_type=type_hints["peering_config"])
            check_type(argname="argument private_visibility_config", value=private_visibility_config, expected_type=type_hints["private_visibility_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
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
        if description is not None:
            self._values["description"] = description
        if dnssec_config is not None:
            self._values["dnssec_config"] = dnssec_config
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if forwarding_config is not None:
            self._values["forwarding_config"] = forwarding_config
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if peering_config is not None:
            self._values["peering_config"] = peering_config
        if private_visibility_config is not None:
            self._values["private_visibility_config"] = private_visibility_config
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if visibility is not None:
            self._values["visibility"] = visibility

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
    def dns_name(self) -> builtins.str:
        '''The DNS name of this managed zone, for instance "example.com.".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dns_name DnsManagedZone#dns_name}
        '''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''User assigned name for this resource. Must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#name DnsManagedZone#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A textual description field. Defaults to 'Managed by Terraform'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#description DnsManagedZone#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dnssec_config(self) -> typing.Optional["DnsManagedZoneDnssecConfig"]:
        '''dnssec_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#dnssec_config DnsManagedZone#dnssec_config}
        '''
        result = self._values.get("dnssec_config")
        return typing.cast(typing.Optional["DnsManagedZoneDnssecConfig"], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#force_destroy DnsManagedZone#force_destroy}.'''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarding_config(self) -> typing.Optional["DnsManagedZoneForwardingConfig"]:
        '''forwarding_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#forwarding_config DnsManagedZone#forwarding_config}
        '''
        result = self._values.get("forwarding_config")
        return typing.cast(typing.Optional["DnsManagedZoneForwardingConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#id DnsManagedZone#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to this ManagedZone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#labels DnsManagedZone#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def peering_config(self) -> typing.Optional["DnsManagedZonePeeringConfig"]:
        '''peering_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#peering_config DnsManagedZone#peering_config}
        '''
        result = self._values.get("peering_config")
        return typing.cast(typing.Optional["DnsManagedZonePeeringConfig"], result)

    @builtins.property
    def private_visibility_config(
        self,
    ) -> typing.Optional["DnsManagedZonePrivateVisibilityConfig"]:
        '''private_visibility_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#private_visibility_config DnsManagedZone#private_visibility_config}
        '''
        result = self._values.get("private_visibility_config")
        return typing.cast(typing.Optional["DnsManagedZonePrivateVisibilityConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#project DnsManagedZone#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DnsManagedZoneTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#timeouts DnsManagedZone#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DnsManagedZoneTimeouts"], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.

        Default value: "public" Possible values: ["private", "public"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#visibility DnsManagedZone#visibility}
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneDnssecConfig",
    jsii_struct_bases=[],
    name_mapping={
        "default_key_specs": "defaultKeySpecs",
        "kind": "kind",
        "non_existence": "nonExistence",
        "state": "state",
    },
)
class DnsManagedZoneDnssecConfig:
    def __init__(
        self,
        *,
        default_key_specs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZoneDnssecConfigDefaultKeySpecs", typing.Dict[str, typing.Any]]]]] = None,
        kind: typing.Optional[builtins.str] = None,
        non_existence: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_key_specs: default_key_specs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#default_key_specs DnsManagedZone#default_key_specs}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#kind DnsManagedZone#kind}
        :param non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses. non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#non_existence DnsManagedZone#non_existence}
        :param state: Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#state DnsManagedZone#state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfig.__init__)
            check_type(argname="argument default_key_specs", value=default_key_specs, expected_type=type_hints["default_key_specs"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument non_existence", value=non_existence, expected_type=type_hints["non_existence"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_key_specs is not None:
            self._values["default_key_specs"] = default_key_specs
        if kind is not None:
            self._values["kind"] = kind
        if non_existence is not None:
            self._values["non_existence"] = non_existence
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def default_key_specs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneDnssecConfigDefaultKeySpecs"]]]:
        '''default_key_specs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#default_key_specs DnsManagedZone#default_key_specs}
        '''
        result = self._values.get("default_key_specs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneDnssecConfigDefaultKeySpecs"]]], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Identifies what kind of resource this is.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#kind DnsManagedZone#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def non_existence(self) -> typing.Optional[builtins.str]:
        '''Specifies the mechanism used to provide authenticated denial-of-existence responses.

        non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#non_existence DnsManagedZone#non_existence}
        '''
        result = self._values.get("non_existence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#state DnsManagedZone#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneDnssecConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneDnssecConfigDefaultKeySpecs",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "key_length": "keyLength",
        "key_type": "keyType",
        "kind": "kind",
    },
)
class DnsManagedZoneDnssecConfigDefaultKeySpecs:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        key_length: typing.Optional[jsii.Number] = None,
        key_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: String mnemonic specifying the DNSSEC algorithm of this key Possible values: ["ecdsap256sha256", "ecdsap384sha384", "rsasha1", "rsasha256", "rsasha512"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#algorithm DnsManagedZone#algorithm}
        :param key_length: Length of the keys in bits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#key_length DnsManagedZone#key_length}
        :param key_type: Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, will only be used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and will be used to sign all other types of resource record sets. Possible values: ["keySigning", "zoneSigning"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#key_type DnsManagedZone#key_type}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#kind DnsManagedZone#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigDefaultKeySpecs.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument key_length", value=key_length, expected_type=type_hints["key_length"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if key_length is not None:
            self._values["key_length"] = key_length
        if key_type is not None:
            self._values["key_type"] = key_type
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        '''String mnemonic specifying the DNSSEC algorithm of this key Possible values: ["ecdsap256sha256", "ecdsap384sha384", "rsasha1", "rsasha256", "rsasha512"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#algorithm DnsManagedZone#algorithm}
        '''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_length(self) -> typing.Optional[jsii.Number]:
        '''Length of the keys in bits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#key_length DnsManagedZone#key_length}
        '''
        result = self._values.get("key_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def key_type(self) -> typing.Optional[builtins.str]:
        '''Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK).

        Key signing keys have the Secure Entry
        Point flag set and, when active, will only be used to sign
        resource record sets of type DNSKEY. Zone signing keys do
        not have the Secure Entry Point flag set and will be used
        to sign all other types of resource record sets. Possible values: ["keySigning", "zoneSigning"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#key_type DnsManagedZone#key_type}
        '''
        result = self._values.get("key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Identifies what kind of resource this is.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#kind DnsManagedZone#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneDnssecConfigDefaultKeySpecs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZoneDnssecConfigDefaultKeySpecsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneDnssecConfigDefaultKeySpecsList",
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
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigDefaultKeySpecsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigDefaultKeySpecsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneDnssecConfigDefaultKeySpecs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneDnssecConfigDefaultKeySpecs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneDnssecConfigDefaultKeySpecs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetKeyLength")
    def reset_key_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyLength", []))

    @jsii.member(jsii_name="resetKeyType")
    def reset_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="keyLengthInput")
    def key_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keyLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="keyLength")
    def key_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keyLength"))

    @key_length.setter
    def key_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "key_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyLength", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DnsManagedZoneDnssecConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneDnssecConfigOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultKeySpecs")
    def put_default_key_specs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DnsManagedZoneDnssecConfigDefaultKeySpecs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneDnssecConfigOutputReference.put_default_key_specs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultKeySpecs", [value]))

    @jsii.member(jsii_name="resetDefaultKeySpecs")
    def reset_default_key_specs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultKeySpecs", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetNonExistence")
    def reset_non_existence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonExistence", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @builtins.property
    @jsii.member(jsii_name="defaultKeySpecs")
    def default_key_specs(self) -> DnsManagedZoneDnssecConfigDefaultKeySpecsList:
        return typing.cast(DnsManagedZoneDnssecConfigDefaultKeySpecsList, jsii.get(self, "defaultKeySpecs"))

    @builtins.property
    @jsii.member(jsii_name="defaultKeySpecsInput")
    def default_key_specs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneDnssecConfigDefaultKeySpecs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneDnssecConfigDefaultKeySpecs]]], jsii.get(self, "defaultKeySpecsInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nonExistenceInput")
    def non_existence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nonExistenceInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="nonExistence")
    def non_existence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nonExistence"))

    @non_existence.setter
    def non_existence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigOutputReference, "non_existence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonExistence", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsManagedZoneDnssecConfig]:
        return typing.cast(typing.Optional[DnsManagedZoneDnssecConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DnsManagedZoneDnssecConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneDnssecConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneForwardingConfig",
    jsii_struct_bases=[],
    name_mapping={"target_name_servers": "targetNameServers"},
)
class DnsManagedZoneForwardingConfig:
    def __init__(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_name_servers DnsManagedZone#target_name_servers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfig.__init__)
            check_type(argname="argument target_name_servers", value=target_name_servers, expected_type=type_hints["target_name_servers"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_name_servers": target_name_servers,
        }

    @builtins.property
    def target_name_servers(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneForwardingConfigTargetNameServers"]]:
        '''target_name_servers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_name_servers DnsManagedZone#target_name_servers}
        '''
        result = self._values.get("target_name_servers")
        assert result is not None, "Required property 'target_name_servers' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneForwardingConfigTargetNameServers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneForwardingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZoneForwardingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneForwardingConfigOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetNameServers")
    def put_target_name_servers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigOutputReference.put_target_name_servers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetNameServers", [value]))

    @builtins.property
    @jsii.member(jsii_name="targetNameServers")
    def target_name_servers(
        self,
    ) -> "DnsManagedZoneForwardingConfigTargetNameServersList":
        return typing.cast("DnsManagedZoneForwardingConfigTargetNameServersList", jsii.get(self, "targetNameServers"))

    @builtins.property
    @jsii.member(jsii_name="targetNameServersInput")
    def target_name_servers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneForwardingConfigTargetNameServers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DnsManagedZoneForwardingConfigTargetNameServers"]]], jsii.get(self, "targetNameServersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsManagedZoneForwardingConfig]:
        return typing.cast(typing.Optional[DnsManagedZoneForwardingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DnsManagedZoneForwardingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneForwardingConfigTargetNameServers",
    jsii_struct_bases=[],
    name_mapping={"ipv4_address": "ipv4Address", "forwarding_path": "forwardingPath"},
)
class DnsManagedZoneForwardingConfigTargetNameServers:
    def __init__(
        self,
        *,
        ipv4_address: builtins.str,
        forwarding_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ipv4_address: IPv4 address of a target name server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#ipv4_address DnsManagedZone#ipv4_address}
        :param forwarding_path: Forwarding path for this TargetNameServer. If unset or 'default' Cloud DNS will make forwarding decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#forwarding_path DnsManagedZone#forwarding_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigTargetNameServers.__init__)
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument forwarding_path", value=forwarding_path, expected_type=type_hints["forwarding_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "ipv4_address": ipv4_address,
        }
        if forwarding_path is not None:
            self._values["forwarding_path"] = forwarding_path

    @builtins.property
    def ipv4_address(self) -> builtins.str:
        '''IPv4 address of a target name server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#ipv4_address DnsManagedZone#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        assert result is not None, "Required property 'ipv4_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def forwarding_path(self) -> typing.Optional[builtins.str]:
        '''Forwarding path for this TargetNameServer.

        If unset or 'default' Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#forwarding_path DnsManagedZone#forwarding_path}
        '''
        result = self._values.get("forwarding_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneForwardingConfigTargetNameServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZoneForwardingConfigTargetNameServersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneForwardingConfigTargetNameServersList",
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
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigTargetNameServersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DnsManagedZoneForwardingConfigTargetNameServersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigTargetNameServersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DnsManagedZoneForwardingConfigTargetNameServersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneForwardingConfigTargetNameServers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneForwardingConfigTargetNameServers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZoneForwardingConfigTargetNameServers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DnsManagedZoneForwardingConfigTargetNameServersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneForwardingConfigTargetNameServersOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZoneForwardingConfigTargetNameServersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetForwardingPath")
    def reset_forwarding_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingPath", []))

    @builtins.property
    @jsii.member(jsii_name="forwardingPathInput")
    def forwarding_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingPathInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingPath")
    def forwarding_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingPath"))

    @forwarding_path.setter
    def forwarding_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersOutputReference, "forwarding_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingPath", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersOutputReference, "ipv4_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneForwardingConfigTargetNameServersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePeeringConfig",
    jsii_struct_bases=[],
    name_mapping={"target_network": "targetNetwork"},
)
class DnsManagedZonePeeringConfig:
    def __init__(
        self,
        *,
        target_network: typing.Union["DnsManagedZonePeeringConfigTargetNetwork", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target_network: target_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_network DnsManagedZone#target_network}
        '''
        if isinstance(target_network, dict):
            target_network = DnsManagedZonePeeringConfigTargetNetwork(**target_network)
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePeeringConfig.__init__)
            check_type(argname="argument target_network", value=target_network, expected_type=type_hints["target_network"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_network": target_network,
        }

    @builtins.property
    def target_network(self) -> "DnsManagedZonePeeringConfigTargetNetwork":
        '''target_network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#target_network DnsManagedZone#target_network}
        '''
        result = self._values.get("target_network")
        assert result is not None, "Required property 'target_network' is missing"
        return typing.cast("DnsManagedZonePeeringConfigTargetNetwork", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZonePeeringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZonePeeringConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePeeringConfigOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZonePeeringConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetNetwork")
    def put_target_network(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to forward queries to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#network_url DnsManagedZone#network_url}
        '''
        value = DnsManagedZonePeeringConfigTargetNetwork(network_url=network_url)

        return typing.cast(None, jsii.invoke(self, "putTargetNetwork", [value]))

    @builtins.property
    @jsii.member(jsii_name="targetNetwork")
    def target_network(
        self,
    ) -> "DnsManagedZonePeeringConfigTargetNetworkOutputReference":
        return typing.cast("DnsManagedZonePeeringConfigTargetNetworkOutputReference", jsii.get(self, "targetNetwork"))

    @builtins.property
    @jsii.member(jsii_name="targetNetworkInput")
    def target_network_input(
        self,
    ) -> typing.Optional["DnsManagedZonePeeringConfigTargetNetwork"]:
        return typing.cast(typing.Optional["DnsManagedZonePeeringConfigTargetNetwork"], jsii.get(self, "targetNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsManagedZonePeeringConfig]:
        return typing.cast(typing.Optional[DnsManagedZonePeeringConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DnsManagedZonePeeringConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePeeringConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePeeringConfigTargetNetwork",
    jsii_struct_bases=[],
    name_mapping={"network_url": "networkUrl"},
)
class DnsManagedZonePeeringConfigTargetNetwork:
    def __init__(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to forward queries to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#network_url DnsManagedZone#network_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePeeringConfigTargetNetwork.__init__)
            check_type(argname="argument network_url", value=network_url, expected_type=type_hints["network_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_url": network_url,
        }

    @builtins.property
    def network_url(self) -> builtins.str:
        '''The id or fully qualified URL of the VPC network to forward queries to.

        This should be formatted like 'projects/{project}/global/networks/{network}' or
        'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#network_url DnsManagedZone#network_url}
        '''
        result = self._values.get("network_url")
        assert result is not None, "Required property 'network_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZonePeeringConfigTargetNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZonePeeringConfigTargetNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePeeringConfigTargetNetworkOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZonePeeringConfigTargetNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="networkUrlInput")
    def network_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUrl")
    def network_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkUrl"))

    @network_url.setter
    def network_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePeeringConfigTargetNetworkOutputReference, "network_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DnsManagedZonePeeringConfigTargetNetwork]:
        return typing.cast(typing.Optional[DnsManagedZonePeeringConfigTargetNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DnsManagedZonePeeringConfigTargetNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePeeringConfigTargetNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePrivateVisibilityConfig",
    jsii_struct_bases=[],
    name_mapping={"networks": "networks"},
)
class DnsManagedZonePrivateVisibilityConfig:
    def __init__(
        self,
        *,
        networks: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DnsManagedZonePrivateVisibilityConfigNetworks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#networks DnsManagedZone#networks}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfig.__init__)
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
        self._values: typing.Dict[str, typing.Any] = {
            "networks": networks,
        }

    @builtins.property
    def networks(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DnsManagedZonePrivateVisibilityConfigNetworks"]]:
        '''networks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#networks DnsManagedZone#networks}
        '''
        result = self._values.get("networks")
        assert result is not None, "Required property 'networks' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DnsManagedZonePrivateVisibilityConfigNetworks"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZonePrivateVisibilityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePrivateVisibilityConfigNetworks",
    jsii_struct_bases=[],
    name_mapping={"network_url": "networkUrl"},
)
class DnsManagedZonePrivateVisibilityConfigNetworks:
    def __init__(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to bind to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#network_url DnsManagedZone#network_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigNetworks.__init__)
            check_type(argname="argument network_url", value=network_url, expected_type=type_hints["network_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_url": network_url,
        }

    @builtins.property
    def network_url(self) -> builtins.str:
        '''The id or fully qualified URL of the VPC network to bind to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#network_url DnsManagedZone#network_url}
        '''
        result = self._values.get("network_url")
        assert result is not None, "Required property 'network_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZonePrivateVisibilityConfigNetworks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZonePrivateVisibilityConfigNetworksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePrivateVisibilityConfigNetworksList",
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
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigNetworksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DnsManagedZonePrivateVisibilityConfigNetworksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigNetworksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DnsManagedZonePrivateVisibilityConfigNetworksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZonePrivateVisibilityConfigNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZonePrivateVisibilityConfigNetworks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZonePrivateVisibilityConfigNetworks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DnsManagedZonePrivateVisibilityConfigNetworksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePrivateVisibilityConfigNetworksOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigNetworksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="networkUrlInput")
    def network_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUrl")
    def network_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkUrl"))

    @network_url.setter
    def network_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksOutputReference, "network_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigNetworksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DnsManagedZonePrivateVisibilityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZonePrivateVisibilityConfigOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNetworks")
    def put_networks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DnsManagedZonePrivateVisibilityConfigNetworks, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZonePrivateVisibilityConfigOutputReference.put_networks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworks", [value]))

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> DnsManagedZonePrivateVisibilityConfigNetworksList:
        return typing.cast(DnsManagedZonePrivateVisibilityConfigNetworksList, jsii.get(self, "networks"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZonePrivateVisibilityConfigNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DnsManagedZonePrivateVisibilityConfigNetworks]]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsManagedZonePrivateVisibilityConfig]:
        return typing.cast(typing.Optional[DnsManagedZonePrivateVisibilityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DnsManagedZonePrivateVisibilityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZonePrivateVisibilityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DnsManagedZoneTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#create DnsManagedZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#delete DnsManagedZone#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#update DnsManagedZone#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsManagedZoneTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#create DnsManagedZone#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#delete DnsManagedZone#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dns_managed_zone#update DnsManagedZone#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsManagedZoneTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsManagedZoneTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dnsManagedZone.DnsManagedZoneTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DnsManagedZoneTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DnsManagedZoneTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DnsManagedZoneTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DnsManagedZoneTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DnsManagedZoneTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DnsManagedZone",
    "DnsManagedZoneConfig",
    "DnsManagedZoneDnssecConfig",
    "DnsManagedZoneDnssecConfigDefaultKeySpecs",
    "DnsManagedZoneDnssecConfigDefaultKeySpecsList",
    "DnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference",
    "DnsManagedZoneDnssecConfigOutputReference",
    "DnsManagedZoneForwardingConfig",
    "DnsManagedZoneForwardingConfigOutputReference",
    "DnsManagedZoneForwardingConfigTargetNameServers",
    "DnsManagedZoneForwardingConfigTargetNameServersList",
    "DnsManagedZoneForwardingConfigTargetNameServersOutputReference",
    "DnsManagedZonePeeringConfig",
    "DnsManagedZonePeeringConfigOutputReference",
    "DnsManagedZonePeeringConfigTargetNetwork",
    "DnsManagedZonePeeringConfigTargetNetworkOutputReference",
    "DnsManagedZonePrivateVisibilityConfig",
    "DnsManagedZonePrivateVisibilityConfigNetworks",
    "DnsManagedZonePrivateVisibilityConfigNetworksList",
    "DnsManagedZonePrivateVisibilityConfigNetworksOutputReference",
    "DnsManagedZonePrivateVisibilityConfigOutputReference",
    "DnsManagedZoneTimeouts",
    "DnsManagedZoneTimeoutsOutputReference",
]

publication.publish()
