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


class NetworkConnectivitySpoke(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpoke",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke google_network_connectivity_spoke}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        hub: builtins.str,
        location: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linked_interconnect_attachments: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedInterconnectAttachments", typing.Dict[str, typing.Any]]] = None,
        linked_router_appliance_instances: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedRouterApplianceInstances", typing.Dict[str, typing.Any]]] = None,
        linked_vpn_tunnels: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedVpnTunnels", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["NetworkConnectivitySpokeTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke google_network_connectivity_spoke} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hub: Immutable. The URI of the hub that this spoke is attached to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#hub NetworkConnectivitySpoke#hub}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#location NetworkConnectivitySpoke#location}
        :param name: Immutable. The name of the spoke. Spoke names must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#name NetworkConnectivitySpoke#name}
        :param description: An optional description of the spoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#description NetworkConnectivitySpoke#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#id NetworkConnectivitySpoke#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#labels NetworkConnectivitySpoke#labels}
        :param linked_interconnect_attachments: linked_interconnect_attachments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_interconnect_attachments NetworkConnectivitySpoke#linked_interconnect_attachments}
        :param linked_router_appliance_instances: linked_router_appliance_instances block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_router_appliance_instances NetworkConnectivitySpoke#linked_router_appliance_instances}
        :param linked_vpn_tunnels: linked_vpn_tunnels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_vpn_tunnels NetworkConnectivitySpoke#linked_vpn_tunnels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#project NetworkConnectivitySpoke#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#timeouts NetworkConnectivitySpoke#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpoke.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConnectivitySpokeConfig(
            hub=hub,
            location=location,
            name=name,
            description=description,
            id=id,
            labels=labels,
            linked_interconnect_attachments=linked_interconnect_attachments,
            linked_router_appliance_instances=linked_router_appliance_instances,
            linked_vpn_tunnels=linked_vpn_tunnels,
            project=project,
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

    @jsii.member(jsii_name="putLinkedInterconnectAttachments")
    def put_linked_interconnect_attachments(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked interconnect attachment resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        value = NetworkConnectivitySpokeLinkedInterconnectAttachments(
            site_to_site_data_transfer=site_to_site_data_transfer, uris=uris
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedInterconnectAttachments", [value]))

    @jsii.member(jsii_name="putLinkedRouterApplianceInstances")
    def put_linked_router_appliance_instances(
        self,
        *,
        instances: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances", typing.Dict[str, typing.Any]]]],
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param instances: instances block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#instances NetworkConnectivitySpoke#instances}
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        value = NetworkConnectivitySpokeLinkedRouterApplianceInstances(
            instances=instances, site_to_site_data_transfer=site_to_site_data_transfer
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedRouterApplianceInstances", [value]))

    @jsii.member(jsii_name="putLinkedVpnTunnels")
    def put_linked_vpn_tunnels(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked VPN tunnel resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        value = NetworkConnectivitySpokeLinkedVpnTunnels(
            site_to_site_data_transfer=site_to_site_data_transfer, uris=uris
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedVpnTunnels", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#create NetworkConnectivitySpoke#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#delete NetworkConnectivitySpoke#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#update NetworkConnectivitySpoke#update}.
        '''
        value = NetworkConnectivitySpokeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLinkedInterconnectAttachments")
    def reset_linked_interconnect_attachments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedInterconnectAttachments", []))

    @jsii.member(jsii_name="resetLinkedRouterApplianceInstances")
    def reset_linked_router_appliance_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedRouterApplianceInstances", []))

    @jsii.member(jsii_name="resetLinkedVpnTunnels")
    def reset_linked_vpn_tunnels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedVpnTunnels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(
        self,
    ) -> "NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference":
        return typing.cast("NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference", jsii.get(self, "linkedInterconnectAttachments"))

    @builtins.property
    @jsii.member(jsii_name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(
        self,
    ) -> "NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference":
        return typing.cast("NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference", jsii.get(self, "linkedRouterApplianceInstances"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpnTunnels")
    def linked_vpn_tunnels(
        self,
    ) -> "NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference":
        return typing.cast("NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference", jsii.get(self, "linkedVpnTunnels"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkConnectivitySpokeTimeoutsOutputReference":
        return typing.cast("NetworkConnectivitySpokeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hubInput")
    def hub_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hubInput"))

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
    @jsii.member(jsii_name="linkedInterconnectAttachmentsInput")
    def linked_interconnect_attachments_input(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedInterconnectAttachments"]:
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedInterconnectAttachments"], jsii.get(self, "linkedInterconnectAttachmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedRouterApplianceInstancesInput")
    def linked_router_appliance_instances_input(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedRouterApplianceInstances"]:
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedRouterApplianceInstances"], jsii.get(self, "linkedRouterApplianceInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpnTunnelsInput")
    def linked_vpn_tunnels_input(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedVpnTunnels"]:
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedVpnTunnels"], jsii.get(self, "linkedVpnTunnelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkConnectivitySpokeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkConnectivitySpokeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hub")
    def hub(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hub"))

    @hub.setter
    def hub(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "hub").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hub", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpoke, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hub": "hub",
        "location": "location",
        "name": "name",
        "description": "description",
        "id": "id",
        "labels": "labels",
        "linked_interconnect_attachments": "linkedInterconnectAttachments",
        "linked_router_appliance_instances": "linkedRouterApplianceInstances",
        "linked_vpn_tunnels": "linkedVpnTunnels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class NetworkConnectivitySpokeConfig(cdktf.TerraformMetaArguments):
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
        hub: builtins.str,
        location: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linked_interconnect_attachments: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedInterconnectAttachments", typing.Dict[str, typing.Any]]] = None,
        linked_router_appliance_instances: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedRouterApplianceInstances", typing.Dict[str, typing.Any]]] = None,
        linked_vpn_tunnels: typing.Optional[typing.Union["NetworkConnectivitySpokeLinkedVpnTunnels", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["NetworkConnectivitySpokeTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param hub: Immutable. The URI of the hub that this spoke is attached to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#hub NetworkConnectivitySpoke#hub}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#location NetworkConnectivitySpoke#location}
        :param name: Immutable. The name of the spoke. Spoke names must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#name NetworkConnectivitySpoke#name}
        :param description: An optional description of the spoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#description NetworkConnectivitySpoke#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#id NetworkConnectivitySpoke#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#labels NetworkConnectivitySpoke#labels}
        :param linked_interconnect_attachments: linked_interconnect_attachments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_interconnect_attachments NetworkConnectivitySpoke#linked_interconnect_attachments}
        :param linked_router_appliance_instances: linked_router_appliance_instances block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_router_appliance_instances NetworkConnectivitySpoke#linked_router_appliance_instances}
        :param linked_vpn_tunnels: linked_vpn_tunnels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_vpn_tunnels NetworkConnectivitySpoke#linked_vpn_tunnels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#project NetworkConnectivitySpoke#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#timeouts NetworkConnectivitySpoke#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(linked_interconnect_attachments, dict):
            linked_interconnect_attachments = NetworkConnectivitySpokeLinkedInterconnectAttachments(**linked_interconnect_attachments)
        if isinstance(linked_router_appliance_instances, dict):
            linked_router_appliance_instances = NetworkConnectivitySpokeLinkedRouterApplianceInstances(**linked_router_appliance_instances)
        if isinstance(linked_vpn_tunnels, dict):
            linked_vpn_tunnels = NetworkConnectivitySpokeLinkedVpnTunnels(**linked_vpn_tunnels)
        if isinstance(timeouts, dict):
            timeouts = NetworkConnectivitySpokeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hub", value=hub, expected_type=type_hints["hub"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument linked_interconnect_attachments", value=linked_interconnect_attachments, expected_type=type_hints["linked_interconnect_attachments"])
            check_type(argname="argument linked_router_appliance_instances", value=linked_router_appliance_instances, expected_type=type_hints["linked_router_appliance_instances"])
            check_type(argname="argument linked_vpn_tunnels", value=linked_vpn_tunnels, expected_type=type_hints["linked_vpn_tunnels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "hub": hub,
            "location": location,
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
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if linked_interconnect_attachments is not None:
            self._values["linked_interconnect_attachments"] = linked_interconnect_attachments
        if linked_router_appliance_instances is not None:
            self._values["linked_router_appliance_instances"] = linked_router_appliance_instances
        if linked_vpn_tunnels is not None:
            self._values["linked_vpn_tunnels"] = linked_vpn_tunnels
        if project is not None:
            self._values["project"] = project
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
    def hub(self) -> builtins.str:
        '''Immutable. The URI of the hub that this spoke is attached to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#hub NetworkConnectivitySpoke#hub}
        '''
        result = self._values.get("hub")
        assert result is not None, "Required property 'hub' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#location NetworkConnectivitySpoke#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Immutable. The name of the spoke. Spoke names must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#name NetworkConnectivitySpoke#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the spoke.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#description NetworkConnectivitySpoke#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#id NetworkConnectivitySpoke#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#labels NetworkConnectivitySpoke#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def linked_interconnect_attachments(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedInterconnectAttachments"]:
        '''linked_interconnect_attachments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_interconnect_attachments NetworkConnectivitySpoke#linked_interconnect_attachments}
        '''
        result = self._values.get("linked_interconnect_attachments")
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedInterconnectAttachments"], result)

    @builtins.property
    def linked_router_appliance_instances(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedRouterApplianceInstances"]:
        '''linked_router_appliance_instances block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_router_appliance_instances NetworkConnectivitySpoke#linked_router_appliance_instances}
        '''
        result = self._values.get("linked_router_appliance_instances")
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedRouterApplianceInstances"], result)

    @builtins.property
    def linked_vpn_tunnels(
        self,
    ) -> typing.Optional["NetworkConnectivitySpokeLinkedVpnTunnels"]:
        '''linked_vpn_tunnels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#linked_vpn_tunnels NetworkConnectivitySpoke#linked_vpn_tunnels}
        '''
        result = self._values.get("linked_vpn_tunnels")
        return typing.cast(typing.Optional["NetworkConnectivitySpokeLinkedVpnTunnels"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#project NetworkConnectivitySpoke#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkConnectivitySpokeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#timeouts NetworkConnectivitySpoke#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkConnectivitySpokeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedInterconnectAttachments",
    jsii_struct_bases=[],
    name_mapping={
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
        "uris": "uris",
    },
)
class NetworkConnectivitySpokeLinkedInterconnectAttachments:
    def __init__(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked interconnect attachment resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedInterconnectAttachments.__init__)
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[str, typing.Any] = {
            "site_to_site_data_transfer": site_to_site_data_transfer,
            "uris": uris,
        }

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def uris(self) -> typing.List[builtins.str]:
        '''The URIs of linked interconnect attachment resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        result = self._values.get("uris")
        assert result is not None, "Required property 'uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeLinkedInterconnectAttachments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference, "site_to_site_data_transfer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference, "uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectivitySpokeLinkedInterconnectAttachments]:
        return typing.cast(typing.Optional[NetworkConnectivitySpokeLinkedInterconnectAttachments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectivitySpokeLinkedInterconnectAttachments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedRouterApplianceInstances",
    jsii_struct_bases=[],
    name_mapping={
        "instances": "instances",
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
    },
)
class NetworkConnectivitySpokeLinkedRouterApplianceInstances:
    def __init__(
        self,
        *,
        instances: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances", typing.Dict[str, typing.Any]]]],
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param instances: instances block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#instances NetworkConnectivitySpoke#instances}
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstances.__init__)
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
        self._values: typing.Dict[str, typing.Any] = {
            "instances": instances,
            "site_to_site_data_transfer": site_to_site_data_transfer,
        }

    @builtins.property
    def instances(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances"]]:
        '''instances block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#instances NetworkConnectivitySpoke#instances}
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances"]], result)

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeLinkedRouterApplianceInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances",
    jsii_struct_bases=[],
    name_mapping={"ip_address": "ipAddress", "virtual_machine": "virtualMachine"},
)
class NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances:
    def __init__(
        self,
        *,
        ip_address: typing.Optional[builtins.str] = None,
        virtual_machine: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_address: The IP address on the VM to use for peering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#ip_address NetworkConnectivitySpoke#ip_address}
        :param virtual_machine: The URI of the virtual machine resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#virtual_machine NetworkConnectivitySpoke#virtual_machine}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances.__init__)
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address on the VM to use for peering.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#ip_address NetworkConnectivitySpoke#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_machine(self) -> typing.Optional[builtins.str]:
        '''The URI of the virtual machine resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#virtual_machine NetworkConnectivitySpoke#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetVirtualMachine")
    def reset_virtual_machine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachine", []))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineInput")
    def virtual_machine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachine")
    def virtual_machine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachine"))

    @virtual_machine.setter
    def virtual_machine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference, "virtual_machine").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachine", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstances")
    def put_instances(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference.put_instances)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstances", [value]))

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(
        self,
    ) -> NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList:
        return typing.cast(NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, jsii.get(self, "instances"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference, "site_to_site_data_transfer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectivitySpokeLinkedRouterApplianceInstances]:
        return typing.cast(typing.Optional[NetworkConnectivitySpokeLinkedRouterApplianceInstances], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectivitySpokeLinkedRouterApplianceInstances],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedVpnTunnels",
    jsii_struct_bases=[],
    name_mapping={
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
        "uris": "uris",
    },
)
class NetworkConnectivitySpokeLinkedVpnTunnels:
    def __init__(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, cdktf.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked VPN tunnel resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedVpnTunnels.__init__)
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[str, typing.Any] = {
            "site_to_site_data_transfer": site_to_site_data_transfer,
            "uris": uris,
        }

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#site_to_site_data_transfer NetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def uris(self) -> typing.List[builtins.str]:
        '''The URIs of linked VPN tunnel resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#uris NetworkConnectivitySpoke#uris}
        '''
        result = self._values.get("uris")
        assert result is not None, "Required property 'uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeLinkedVpnTunnels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference, "site_to_site_data_transfer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference, "uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectivitySpokeLinkedVpnTunnels]:
        return typing.cast(typing.Optional[NetworkConnectivitySpokeLinkedVpnTunnels], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectivitySpokeLinkedVpnTunnels],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class NetworkConnectivitySpokeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#create NetworkConnectivitySpoke#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#delete NetworkConnectivitySpoke#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#update NetworkConnectivitySpoke#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#create NetworkConnectivitySpoke#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#delete NetworkConnectivitySpoke#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_connectivity_spoke#update NetworkConnectivitySpoke#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectivitySpokeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectivitySpokeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.networkConnectivitySpoke.NetworkConnectivitySpokeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectivitySpokeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectivitySpokeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectivitySpokeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectivitySpokeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectivitySpokeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkConnectivitySpoke",
    "NetworkConnectivitySpokeConfig",
    "NetworkConnectivitySpokeLinkedInterconnectAttachments",
    "NetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference",
    "NetworkConnectivitySpokeLinkedRouterApplianceInstances",
    "NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances",
    "NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList",
    "NetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference",
    "NetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference",
    "NetworkConnectivitySpokeLinkedVpnTunnels",
    "NetworkConnectivitySpokeLinkedVpnTunnelsOutputReference",
    "NetworkConnectivitySpokeTimeouts",
    "NetworkConnectivitySpokeTimeoutsOutputReference",
]

publication.publish()
