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


class ContainerCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/container_cluster google_container_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        addons_config: typing.Optional[typing.Union["ContainerClusterAddonsConfig", typing.Dict[str, typing.Any]]] = None,
        authenticator_groups_config: typing.Optional[typing.Union["ContainerClusterAuthenticatorGroupsConfig", typing.Dict[str, typing.Any]]] = None,
        binary_authorization: typing.Optional[typing.Union["ContainerClusterBinaryAuthorization", typing.Dict[str, typing.Any]]] = None,
        cluster_autoscaling: typing.Optional[typing.Union["ContainerClusterClusterAutoscaling", typing.Dict[str, typing.Any]]] = None,
        cluster_ipv4_cidr: typing.Optional[builtins.str] = None,
        confidential_nodes: typing.Optional[typing.Union["ContainerClusterConfidentialNodes", typing.Dict[str, typing.Any]]] = None,
        database_encryption: typing.Optional[typing.Union["ContainerClusterDatabaseEncryption", typing.Dict[str, typing.Any]]] = None,
        datapath_provider: typing.Optional[builtins.str] = None,
        default_max_pods_per_node: typing.Optional[jsii.Number] = None,
        default_snat_status: typing.Optional[typing.Union["ContainerClusterDefaultSnatStatus", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union["ContainerClusterDnsConfig", typing.Dict[str, typing.Any]]] = None,
        enable_autopilot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_binary_authorization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_intranode_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_kubernetes_alpha: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_legacy_abac: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_shielded_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_tpu: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_node_count: typing.Optional[jsii.Number] = None,
        ip_allocation_policy: typing.Optional[typing.Union["ContainerClusterIpAllocationPolicy", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["ContainerClusterLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        logging_service: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["ContainerClusterMaintenancePolicy", typing.Dict[str, typing.Any]]] = None,
        master_auth: typing.Optional[typing.Union["ContainerClusterMasterAuth", typing.Dict[str, typing.Any]]] = None,
        master_authorized_networks_config: typing.Optional[typing.Union["ContainerClusterMasterAuthorizedNetworksConfig", typing.Dict[str, typing.Any]]] = None,
        mesh_certificates: typing.Optional[typing.Union["ContainerClusterMeshCertificates", typing.Dict[str, typing.Any]]] = None,
        min_master_version: typing.Optional[builtins.str] = None,
        monitoring_config: typing.Optional[typing.Union["ContainerClusterMonitoringConfig", typing.Dict[str, typing.Any]]] = None,
        monitoring_service: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        networking_mode: typing.Optional[builtins.str] = None,
        network_policy: typing.Optional[typing.Union["ContainerClusterNetworkPolicy", typing.Dict[str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["ContainerClusterNodeConfig", typing.Dict[str, typing.Any]]] = None,
        node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_pool: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePool", typing.Dict[str, typing.Any]]]]] = None,
        node_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["ContainerClusterNotificationConfig", typing.Dict[str, typing.Any]]] = None,
        private_cluster_config: typing.Optional[typing.Union["ContainerClusterPrivateClusterConfig", typing.Dict[str, typing.Any]]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        release_channel: typing.Optional[typing.Union["ContainerClusterReleaseChannel", typing.Dict[str, typing.Any]]] = None,
        remove_default_node_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        resource_usage_export_config: typing.Optional[typing.Union["ContainerClusterResourceUsageExportConfig", typing.Dict[str, typing.Any]]] = None,
        service_external_ips_config: typing.Optional[typing.Union["ContainerClusterServiceExternalIpsConfig", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ContainerClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        vertical_pod_autoscaling: typing.Optional[typing.Union["ContainerClusterVerticalPodAutoscaling", typing.Dict[str, typing.Any]]] = None,
        workload_identity_config: typing.Optional[typing.Union["ContainerClusterWorkloadIdentityConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/container_cluster google_container_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the cluster, unique within the project and location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name ContainerCluster#name}
        :param addons_config: addons_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#addons_config ContainerCluster#addons_config}
        :param authenticator_groups_config: authenticator_groups_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#authenticator_groups_config ContainerCluster#authenticator_groups_config}
        :param binary_authorization: binary_authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#binary_authorization ContainerCluster#binary_authorization}
        :param cluster_autoscaling: cluster_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_autoscaling ContainerCluster#cluster_autoscaling}
        :param cluster_ipv4_cidr: The IP address range of the Kubernetes pods in this cluster in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8. This field will only work for routes-based clusters, where ip_allocation_policy is not defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr ContainerCluster#cluster_ipv4_cidr}
        :param confidential_nodes: confidential_nodes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#confidential_nodes ContainerCluster#confidential_nodes}
        :param database_encryption: database_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#database_encryption ContainerCluster#database_encryption}
        :param datapath_provider: The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#datapath_provider ContainerCluster#datapath_provider}
        :param default_max_pods_per_node: The default maximum number of pods per node in this cluster. This doesn't work on "routes-based" clusters, clusters that don't have IP Aliasing enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_max_pods_per_node ContainerCluster#default_max_pods_per_node}
        :param default_snat_status: default_snat_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_snat_status ContainerCluster#default_snat_status}
        :param description: Description of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#description ContainerCluster#description}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_config ContainerCluster#dns_config}
        :param enable_autopilot: Enable Autopilot for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_autopilot ContainerCluster#enable_autopilot}
        :param enable_binary_authorization: Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Google Binary Authorization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_binary_authorization ContainerCluster#enable_binary_authorization}
        :param enable_intranode_visibility: Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_intranode_visibility ContainerCluster#enable_intranode_visibility}
        :param enable_kubernetes_alpha: Whether to enable Kubernetes Alpha features for this cluster. Note that when this option is enabled, the cluster cannot be upgraded and will be automatically deleted after 30 days. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_kubernetes_alpha ContainerCluster#enable_kubernetes_alpha}
        :param enable_legacy_abac: Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_legacy_abac ContainerCluster#enable_legacy_abac}
        :param enable_shielded_nodes: Enable Shielded Nodes features on all nodes in this cluster. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_shielded_nodes ContainerCluster#enable_shielded_nodes}
        :param enable_tpu: Whether to enable Cloud TPU resources in this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_tpu ContainerCluster#enable_tpu}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#id ContainerCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_node_count: The number of nodes to create in this cluster's default node pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Must be set if node_pool is not set. If you're using google_container_node_pool objects with no default node pool, you'll need to set this to a value of at least 1, alongside setting remove_default_node_pool to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#initial_node_count ContainerCluster#initial_node_count}
        :param ip_allocation_policy: ip_allocation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#ip_allocation_policy ContainerCluster#ip_allocation_policy}
        :param location: The location (region or zone) in which the cluster master will be created, as well as the default node location. If you specify a zone (such as us-central1-a), the cluster will be a zonal cluster with a single cluster master. If you specify a region (such as us-west1), the cluster will be a regional cluster with multiple masters spread across zones in the region, and with default node locations in those zones as well. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#location ContainerCluster#location}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_config ContainerCluster#logging_config}
        :param logging_service: The logging service that the cluster should write logs to. Available options include logging.googleapis.com(Legacy Stackdriver), logging.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Logging), and none. Defaults to logging.googleapis.com/kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_service ContainerCluster#logging_service}
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_policy ContainerCluster#maintenance_policy}
        :param master_auth: master_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_auth ContainerCluster#master_auth}
        :param master_authorized_networks_config: master_authorized_networks_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_authorized_networks_config ContainerCluster#master_authorized_networks_config}
        :param mesh_certificates: mesh_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mesh_certificates ContainerCluster#mesh_certificates}
        :param min_master_version: The minimum version of the master. GKE will auto-update the master to new versions, so this does not guarantee the current master version--use the read-only master_version field to obtain that. If unset, the cluster's version will be set by GKE to the version of the most recent official release (which is not necessarily the latest version). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_master_version ContainerCluster#min_master_version}
        :param monitoring_config: monitoring_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_config ContainerCluster#monitoring_config}
        :param monitoring_service: The monitoring service that the cluster should write metrics to. Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API. VM metrics will be collected by Google Compute Engine regardless of this setting Available options include monitoring.googleapis.com(Legacy Stackdriver), monitoring.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Monitoring), and none. Defaults to monitoring.googleapis.com/kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_service ContainerCluster#monitoring_service}
        :param network: The name or self_link of the Google Compute Engine network to which the cluster is connected. For Shared VPC, set this to the self link of the shared network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network ContainerCluster#network}
        :param networking_mode: Determines whether alias IPs or routes will be used for pod IPs in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#networking_mode ContainerCluster#networking_mode}
        :param network_policy: network_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy ContainerCluster#network_policy}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_config ContainerCluster#node_config}
        :param node_locations: The list of zones in which the cluster's nodes are located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If this is specified for a zonal cluster, omit the cluster's zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_locations ContainerCluster#node_locations}
        :param node_pool: node_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_pool ContainerCluster#node_pool}
        :param node_version: The Kubernetes version on the nodes. Must either be unset or set to the same value as min_master_version on create. Defaults to the default version set by GKE which is not necessarily the latest version. This only affects nodes in the default node pool. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. To update nodes in other node pools, use the version attribute on the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_version ContainerCluster#node_version}
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#notification_config ContainerCluster#notification_config}
        :param private_cluster_config: private_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_cluster_config ContainerCluster#private_cluster_config}
        :param private_ipv6_google_access: The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_ipv6_google_access ContainerCluster#private_ipv6_google_access}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#project ContainerCluster#project}
        :param release_channel: release_channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#release_channel ContainerCluster#release_channel}
        :param remove_default_node_pool: If true, deletes the default node pool upon cluster creation. If you're using google_container_node_pool resources with no default node pool, this should be set to true, alongside setting initial_node_count to at least 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#remove_default_node_pool ContainerCluster#remove_default_node_pool}
        :param resource_labels: The GCE resource labels (a map of key/value pairs) to be applied to the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_labels ContainerCluster#resource_labels}
        :param resource_usage_export_config: resource_usage_export_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_usage_export_config ContainerCluster#resource_usage_export_config}
        :param service_external_ips_config: service_external_ips_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_external_ips_config ContainerCluster#service_external_ips_config}
        :param subnetwork: The name or self_link of the Google Compute Engine subnetwork in which the cluster's instances are launched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#subnetwork ContainerCluster#subnetwork}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#timeouts ContainerCluster#timeouts}
        :param vertical_pod_autoscaling: vertical_pod_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#vertical_pod_autoscaling ContainerCluster#vertical_pod_autoscaling}
        :param workload_identity_config: workload_identity_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_identity_config ContainerCluster#workload_identity_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerClusterConfig(
            name=name,
            addons_config=addons_config,
            authenticator_groups_config=authenticator_groups_config,
            binary_authorization=binary_authorization,
            cluster_autoscaling=cluster_autoscaling,
            cluster_ipv4_cidr=cluster_ipv4_cidr,
            confidential_nodes=confidential_nodes,
            database_encryption=database_encryption,
            datapath_provider=datapath_provider,
            default_max_pods_per_node=default_max_pods_per_node,
            default_snat_status=default_snat_status,
            description=description,
            dns_config=dns_config,
            enable_autopilot=enable_autopilot,
            enable_binary_authorization=enable_binary_authorization,
            enable_intranode_visibility=enable_intranode_visibility,
            enable_kubernetes_alpha=enable_kubernetes_alpha,
            enable_legacy_abac=enable_legacy_abac,
            enable_shielded_nodes=enable_shielded_nodes,
            enable_tpu=enable_tpu,
            id=id,
            initial_node_count=initial_node_count,
            ip_allocation_policy=ip_allocation_policy,
            location=location,
            logging_config=logging_config,
            logging_service=logging_service,
            maintenance_policy=maintenance_policy,
            master_auth=master_auth,
            master_authorized_networks_config=master_authorized_networks_config,
            mesh_certificates=mesh_certificates,
            min_master_version=min_master_version,
            monitoring_config=monitoring_config,
            monitoring_service=monitoring_service,
            network=network,
            networking_mode=networking_mode,
            network_policy=network_policy,
            node_config=node_config,
            node_locations=node_locations,
            node_pool=node_pool,
            node_version=node_version,
            notification_config=notification_config,
            private_cluster_config=private_cluster_config,
            private_ipv6_google_access=private_ipv6_google_access,
            project=project,
            release_channel=release_channel,
            remove_default_node_pool=remove_default_node_pool,
            resource_labels=resource_labels,
            resource_usage_export_config=resource_usage_export_config,
            service_external_ips_config=service_external_ips_config,
            subnetwork=subnetwork,
            timeouts=timeouts,
            vertical_pod_autoscaling=vertical_pod_autoscaling,
            workload_identity_config=workload_identity_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAddonsConfig")
    def put_addons_config(
        self,
        *,
        cloudrun_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigCloudrunConfig", typing.Dict[str, typing.Any]]] = None,
        dns_cache_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigDnsCacheConfig", typing.Dict[str, typing.Any]]] = None,
        gce_persistent_disk_csi_driver_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig", typing.Dict[str, typing.Any]]] = None,
        gcp_filestore_csi_driver_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig", typing.Dict[str, typing.Any]]] = None,
        horizontal_pod_autoscaling: typing.Optional[typing.Union["ContainerClusterAddonsConfigHorizontalPodAutoscaling", typing.Dict[str, typing.Any]]] = None,
        http_load_balancing: typing.Optional[typing.Union["ContainerClusterAddonsConfigHttpLoadBalancing", typing.Dict[str, typing.Any]]] = None,
        network_policy_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigNetworkPolicyConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudrun_config: cloudrun_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cloudrun_config ContainerCluster#cloudrun_config}
        :param dns_cache_config: dns_cache_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_cache_config ContainerCluster#dns_cache_config}
        :param gce_persistent_disk_csi_driver_config: gce_persistent_disk_csi_driver_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gce_persistent_disk_csi_driver_config ContainerCluster#gce_persistent_disk_csi_driver_config}
        :param gcp_filestore_csi_driver_config: gcp_filestore_csi_driver_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcp_filestore_csi_driver_config ContainerCluster#gcp_filestore_csi_driver_config}
        :param horizontal_pod_autoscaling: horizontal_pod_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#horizontal_pod_autoscaling ContainerCluster#horizontal_pod_autoscaling}
        :param http_load_balancing: http_load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#http_load_balancing ContainerCluster#http_load_balancing}
        :param network_policy_config: network_policy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy_config ContainerCluster#network_policy_config}
        '''
        value = ContainerClusterAddonsConfig(
            cloudrun_config=cloudrun_config,
            dns_cache_config=dns_cache_config,
            gce_persistent_disk_csi_driver_config=gce_persistent_disk_csi_driver_config,
            gcp_filestore_csi_driver_config=gcp_filestore_csi_driver_config,
            horizontal_pod_autoscaling=horizontal_pod_autoscaling,
            http_load_balancing=http_load_balancing,
            network_policy_config=network_policy_config,
        )

        return typing.cast(None, jsii.invoke(self, "putAddonsConfig", [value]))

    @jsii.member(jsii_name="putAuthenticatorGroupsConfig")
    def put_authenticator_groups_config(self, *, security_group: builtins.str) -> None:
        '''
        :param security_group: The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format gke-security-groups@yourdomain.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#security_group ContainerCluster#security_group}
        '''
        value = ContainerClusterAuthenticatorGroupsConfig(
            security_group=security_group
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticatorGroupsConfig", [value]))

    @jsii.member(jsii_name="putBinaryAuthorization")
    def put_binary_authorization(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        evaluation_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable Binary Authorization for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param evaluation_mode: Mode of operation for Binary Authorization policy evaluation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#evaluation_mode ContainerCluster#evaluation_mode}
        '''
        value = ContainerClusterBinaryAuthorization(
            enabled=enabled, evaluation_mode=evaluation_mode
        )

        return typing.cast(None, jsii.invoke(self, "putBinaryAuthorization", [value]))

    @jsii.member(jsii_name="putClusterAutoscaling")
    def put_cluster_autoscaling(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_provisioning_defaults: typing.Optional[typing.Union["ContainerClusterClusterAutoscalingAutoProvisioningDefaults", typing.Dict[str, typing.Any]]] = None,
        resource_limits: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterClusterAutoscalingResourceLimits", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether node auto-provisioning is enabled. Resource limits for cpu and memory must be defined to enable node auto-provisioning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param auto_provisioning_defaults: auto_provisioning_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_provisioning_defaults ContainerCluster#auto_provisioning_defaults}
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_limits ContainerCluster#resource_limits}
        '''
        value = ContainerClusterClusterAutoscaling(
            enabled=enabled,
            auto_provisioning_defaults=auto_provisioning_defaults,
            resource_limits=resource_limits,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterAutoscaling", [value]))

    @jsii.member(jsii_name="putConfidentialNodes")
    def put_confidential_nodes(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether Confidential Nodes feature is enabled for all nodes in this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterConfidentialNodes(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putConfidentialNodes", [value]))

    @jsii.member(jsii_name="putDatabaseEncryption")
    def put_database_encryption(
        self,
        *,
        state: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param state: ENCRYPTED or DECRYPTED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#state ContainerCluster#state}
        :param key_name: The key to use to encrypt/decrypt secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key_name ContainerCluster#key_name}
        '''
        value = ContainerClusterDatabaseEncryption(state=state, key_name=key_name)

        return typing.cast(None, jsii.invoke(self, "putDatabaseEncryption", [value]))

    @jsii.member(jsii_name="putDefaultSnatStatus")
    def put_default_snat_status(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: When disabled is set to false, default IP masquerade rules will be applied to the nodes to prevent sNAT on cluster internal traffic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}
        '''
        value = ContainerClusterDefaultSnatStatus(disabled=disabled)

        return typing.cast(None, jsii.invoke(self, "putDefaultSnatStatus", [value]))

    @jsii.member(jsii_name="putDnsConfig")
    def put_dns_config(
        self,
        *,
        cluster_dns: typing.Optional[builtins.str] = None,
        cluster_dns_domain: typing.Optional[builtins.str] = None,
        cluster_dns_scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_dns: Which in-cluster DNS provider should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns ContainerCluster#cluster_dns}
        :param cluster_dns_domain: The suffix used for all cluster service records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_domain ContainerCluster#cluster_dns_domain}
        :param cluster_dns_scope: The scope of access to cluster DNS records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_scope ContainerCluster#cluster_dns_scope}
        '''
        value = ContainerClusterDnsConfig(
            cluster_dns=cluster_dns,
            cluster_dns_domain=cluster_dns_domain,
            cluster_dns_scope=cluster_dns_scope,
        )

        return typing.cast(None, jsii.invoke(self, "putDnsConfig", [value]))

    @jsii.member(jsii_name="putIpAllocationPolicy")
    def put_ip_allocation_policy(
        self,
        *,
        cluster_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        cluster_secondary_range_name: typing.Optional[builtins.str] = None,
        services_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        services_secondary_range_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_ipv4_cidr_block: The IP address range for the cluster pod IPs. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr_block ContainerCluster#cluster_ipv4_cidr_block}
        :param cluster_secondary_range_name: The name of the existing secondary range in the cluster's subnetwork to use for pod IP addresses. Alternatively, cluster_ipv4_cidr_block can be used to automatically create a GKE-managed one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_secondary_range_name ContainerCluster#cluster_secondary_range_name}
        :param services_ipv4_cidr_block: The IP address range of the services IPs in this cluster. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_ipv4_cidr_block ContainerCluster#services_ipv4_cidr_block}
        :param services_secondary_range_name: The name of the existing secondary range in the cluster's subnetwork to use for service ClusterIPs. Alternatively, services_ipv4_cidr_block can be used to automatically create a GKE-managed one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_secondary_range_name ContainerCluster#services_secondary_range_name}
        '''
        value = ContainerClusterIpAllocationPolicy(
            cluster_ipv4_cidr_block=cluster_ipv4_cidr_block,
            cluster_secondary_range_name=cluster_secondary_range_name,
            services_ipv4_cidr_block=services_ipv4_cidr_block,
            services_secondary_range_name=services_secondary_range_name,
        )

        return typing.cast(None, jsii.invoke(self, "putIpAllocationPolicy", [value]))

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        enable_components: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param enable_components: GKE components exposing logs. Valid values include SYSTEM_COMPONENTS and WORKLOADS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        value = ContainerClusterLoggingConfig(enable_components=enable_components)

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="putMaintenancePolicy")
    def put_maintenance_policy(
        self,
        *,
        daily_maintenance_window: typing.Optional[typing.Union["ContainerClusterMaintenancePolicyDailyMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        maintenance_exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterMaintenancePolicyMaintenanceExclusion", typing.Dict[str, typing.Any]]]]] = None,
        recurring_window: typing.Optional[typing.Union["ContainerClusterMaintenancePolicyRecurringWindow", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param daily_maintenance_window: daily_maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#daily_maintenance_window ContainerCluster#daily_maintenance_window}
        :param maintenance_exclusion: maintenance_exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_exclusion ContainerCluster#maintenance_exclusion}
        :param recurring_window: recurring_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurring_window ContainerCluster#recurring_window}
        '''
        value = ContainerClusterMaintenancePolicy(
            daily_maintenance_window=daily_maintenance_window,
            maintenance_exclusion=maintenance_exclusion,
            recurring_window=recurring_window,
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenancePolicy", [value]))

    @jsii.member(jsii_name="putMasterAuth")
    def put_master_auth(
        self,
        *,
        client_certificate_config: typing.Union["ContainerClusterMasterAuthClientCertificateConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param client_certificate_config: client_certificate_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#client_certificate_config ContainerCluster#client_certificate_config}
        '''
        value = ContainerClusterMasterAuth(
            client_certificate_config=client_certificate_config
        )

        return typing.cast(None, jsii.invoke(self, "putMasterAuth", [value]))

    @jsii.member(jsii_name="putMasterAuthorizedNetworksConfig")
    def put_master_authorized_networks_config(
        self,
        *,
        cidr_blocks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cidr_blocks: cidr_blocks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cidr_blocks ContainerCluster#cidr_blocks}
        '''
        value = ContainerClusterMasterAuthorizedNetworksConfig(cidr_blocks=cidr_blocks)

        return typing.cast(None, jsii.invoke(self, "putMasterAuthorizedNetworksConfig", [value]))

    @jsii.member(jsii_name="putMeshCertificates")
    def put_mesh_certificates(
        self,
        *,
        enable_certificates: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_certificates: When enabled the GKE Workload Identity Certificates controller and node agent will be deployed in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_certificates ContainerCluster#enable_certificates}
        '''
        value = ContainerClusterMeshCertificates(
            enable_certificates=enable_certificates
        )

        return typing.cast(None, jsii.invoke(self, "putMeshCertificates", [value]))

    @jsii.member(jsii_name="putMonitoringConfig")
    def put_monitoring_config(
        self,
        *,
        enable_components: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param enable_components: GKE components exposing metrics. Valid values include SYSTEM_COMPONENTS, APISERVER, CONTROLLER_MANAGER, and SCHEDULER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        value = ContainerClusterMonitoringConfig(enable_components=enable_components)

        return typing.cast(None, jsii.invoke(self, "putMonitoringConfig", [value]))

    @jsii.member(jsii_name="putNetworkPolicy")
    def put_network_policy(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether network policy is enabled on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param provider: The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#provider ContainerCluster#provider}
        '''
        value = ContainerClusterNetworkPolicy(enabled=enabled, provider=provider)

        return typing.cast(None, jsii.invoke(self, "putNetworkPolicy", [value]))

    @jsii.member(jsii_name="putNodeConfig")
    def put_node_config(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        gcfs_config: typing.Optional[typing.Union["ContainerClusterNodeConfigGcfsConfig", typing.Dict[str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodeConfigGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union["ContainerClusterNodeConfigGvnic", typing.Dict[str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union["ContainerClusterNodeConfigReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["ContainerClusterNodeConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodeConfigTaint", typing.Dict[str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union["ContainerClusterNodeConfigWorkloadMetadataConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        value = ContainerClusterNodeConfig(
            boot_disk_kms_key=boot_disk_kms_key,
            disk_size_gb=disk_size_gb,
            disk_type=disk_type,
            gcfs_config=gcfs_config,
            guest_accelerator=guest_accelerator,
            gvnic=gvnic,
            image_type=image_type,
            labels=labels,
            local_ssd_count=local_ssd_count,
            machine_type=machine_type,
            metadata=metadata,
            min_cpu_platform=min_cpu_platform,
            node_group=node_group,
            oauth_scopes=oauth_scopes,
            preemptible=preemptible,
            reservation_affinity=reservation_affinity,
            service_account=service_account,
            shielded_instance_config=shielded_instance_config,
            spot=spot,
            tags=tags,
            taint=taint,
            workload_metadata_config=workload_metadata_config,
        )

        return typing.cast(None, jsii.invoke(self, "putNodeConfig", [value]))

    @jsii.member(jsii_name="putNodePool")
    def put_node_pool(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePool", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerCluster.put_node_pool)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodePool", [value]))

    @jsii.member(jsii_name="putNotificationConfig")
    def put_notification_config(
        self,
        *,
        pubsub: typing.Union["ContainerClusterNotificationConfigPubsub", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param pubsub: pubsub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#pubsub ContainerCluster#pubsub}
        '''
        value = ContainerClusterNotificationConfig(pubsub=pubsub)

        return typing.cast(None, jsii.invoke(self, "putNotificationConfig", [value]))

    @jsii.member(jsii_name="putPrivateClusterConfig")
    def put_private_cluster_config(
        self,
        *,
        enable_private_endpoint: typing.Union[builtins.bool, cdktf.IResolvable],
        enable_private_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_global_access_config: typing.Optional[typing.Union["ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig", typing.Dict[str, typing.Any]]] = None,
        master_ipv4_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_private_endpoint: When true, the cluster's private endpoint is used as the cluster endpoint and access through the public endpoint is disabled. When false, either endpoint can be used. This field only applies to private clusters, when enable_private_nodes is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_endpoint ContainerCluster#enable_private_endpoint}
        :param enable_private_nodes: Enables the private cluster feature, creating a private endpoint on the cluster. In a private cluster, nodes only have RFC 1918 private addresses and communicate with the master's private endpoint via private networking. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_nodes ContainerCluster#enable_private_nodes}
        :param master_global_access_config: master_global_access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_global_access_config ContainerCluster#master_global_access_config}
        :param master_ipv4_cidr_block: The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning private IP addresses to the cluster master(s) and the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network, and it must be a /28 subnet. See Private Cluster Limitations for more details. This field only applies to private clusters, when enable_private_nodes is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_ipv4_cidr_block ContainerCluster#master_ipv4_cidr_block}
        '''
        value = ContainerClusterPrivateClusterConfig(
            enable_private_endpoint=enable_private_endpoint,
            enable_private_nodes=enable_private_nodes,
            master_global_access_config=master_global_access_config,
            master_ipv4_cidr_block=master_ipv4_cidr_block,
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateClusterConfig", [value]))

    @jsii.member(jsii_name="putReleaseChannel")
    def put_release_channel(self, *, channel: builtins.str) -> None:
        '''
        :param channel: The selected release channel. Accepted values are: UNSPECIFIED: Not set. RAPID: Weekly upgrade cadence; Early testers and developers who requires new features. REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel. STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#channel ContainerCluster#channel}
        '''
        value = ContainerClusterReleaseChannel(channel=channel)

        return typing.cast(None, jsii.invoke(self, "putReleaseChannel", [value]))

    @jsii.member(jsii_name="putResourceUsageExportConfig")
    def put_resource_usage_export_config(
        self,
        *,
        bigquery_destination: typing.Union["ContainerClusterResourceUsageExportConfigBigqueryDestination", typing.Dict[str, typing.Any]],
        enable_network_egress_metering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_resource_consumption_metering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bigquery_destination: bigquery_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#bigquery_destination ContainerCluster#bigquery_destination}
        :param enable_network_egress_metering: Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created in the cluster to meter network egress traffic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_network_egress_metering ContainerCluster#enable_network_egress_metering}
        :param enable_resource_consumption_metering: Whether to enable resource consumption metering on this cluster. When enabled, a table will be created in the resource export BigQuery dataset to store resource consumption data. The resulting table can be joined with the resource usage table or with BigQuery billing export. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_resource_consumption_metering ContainerCluster#enable_resource_consumption_metering}
        '''
        value = ContainerClusterResourceUsageExportConfig(
            bigquery_destination=bigquery_destination,
            enable_network_egress_metering=enable_network_egress_metering,
            enable_resource_consumption_metering=enable_resource_consumption_metering,
        )

        return typing.cast(None, jsii.invoke(self, "putResourceUsageExportConfig", [value]))

    @jsii.member(jsii_name="putServiceExternalIpsConfig")
    def put_service_external_ips_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: When enabled, services with exterenal ips specified will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterServiceExternalIpsConfig(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putServiceExternalIpsConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#create ContainerCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#delete ContainerCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#read ContainerCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#update ContainerCluster#update}.
        '''
        value = ContainerClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVerticalPodAutoscaling")
    def put_vertical_pod_autoscaling(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Enables vertical pod autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterVerticalPodAutoscaling(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putVerticalPodAutoscaling", [value]))

    @jsii.member(jsii_name="putWorkloadIdentityConfig")
    def put_workload_identity_config(
        self,
        *,
        workload_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param workload_pool: The workload pool to attach all Kubernetes service accounts to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_pool ContainerCluster#workload_pool}
        '''
        value = ContainerClusterWorkloadIdentityConfig(workload_pool=workload_pool)

        return typing.cast(None, jsii.invoke(self, "putWorkloadIdentityConfig", [value]))

    @jsii.member(jsii_name="resetAddonsConfig")
    def reset_addons_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddonsConfig", []))

    @jsii.member(jsii_name="resetAuthenticatorGroupsConfig")
    def reset_authenticator_groups_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticatorGroupsConfig", []))

    @jsii.member(jsii_name="resetBinaryAuthorization")
    def reset_binary_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinaryAuthorization", []))

    @jsii.member(jsii_name="resetClusterAutoscaling")
    def reset_cluster_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterAutoscaling", []))

    @jsii.member(jsii_name="resetClusterIpv4Cidr")
    def reset_cluster_ipv4_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIpv4Cidr", []))

    @jsii.member(jsii_name="resetConfidentialNodes")
    def reset_confidential_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialNodes", []))

    @jsii.member(jsii_name="resetDatabaseEncryption")
    def reset_database_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseEncryption", []))

    @jsii.member(jsii_name="resetDatapathProvider")
    def reset_datapath_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatapathProvider", []))

    @jsii.member(jsii_name="resetDefaultMaxPodsPerNode")
    def reset_default_max_pods_per_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultMaxPodsPerNode", []))

    @jsii.member(jsii_name="resetDefaultSnatStatus")
    def reset_default_snat_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSnatStatus", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDnsConfig")
    def reset_dns_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsConfig", []))

    @jsii.member(jsii_name="resetEnableAutopilot")
    def reset_enable_autopilot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutopilot", []))

    @jsii.member(jsii_name="resetEnableBinaryAuthorization")
    def reset_enable_binary_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBinaryAuthorization", []))

    @jsii.member(jsii_name="resetEnableIntranodeVisibility")
    def reset_enable_intranode_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntranodeVisibility", []))

    @jsii.member(jsii_name="resetEnableKubernetesAlpha")
    def reset_enable_kubernetes_alpha(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableKubernetesAlpha", []))

    @jsii.member(jsii_name="resetEnableLegacyAbac")
    def reset_enable_legacy_abac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLegacyAbac", []))

    @jsii.member(jsii_name="resetEnableShieldedNodes")
    def reset_enable_shielded_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableShieldedNodes", []))

    @jsii.member(jsii_name="resetEnableTpu")
    def reset_enable_tpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableTpu", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialNodeCount")
    def reset_initial_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialNodeCount", []))

    @jsii.member(jsii_name="resetIpAllocationPolicy")
    def reset_ip_allocation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAllocationPolicy", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetLoggingService")
    def reset_logging_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingService", []))

    @jsii.member(jsii_name="resetMaintenancePolicy")
    def reset_maintenance_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenancePolicy", []))

    @jsii.member(jsii_name="resetMasterAuth")
    def reset_master_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterAuth", []))

    @jsii.member(jsii_name="resetMasterAuthorizedNetworksConfig")
    def reset_master_authorized_networks_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterAuthorizedNetworksConfig", []))

    @jsii.member(jsii_name="resetMeshCertificates")
    def reset_mesh_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeshCertificates", []))

    @jsii.member(jsii_name="resetMinMasterVersion")
    def reset_min_master_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinMasterVersion", []))

    @jsii.member(jsii_name="resetMonitoringConfig")
    def reset_monitoring_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringConfig", []))

    @jsii.member(jsii_name="resetMonitoringService")
    def reset_monitoring_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringService", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNetworkingMode")
    def reset_networking_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkingMode", []))

    @jsii.member(jsii_name="resetNetworkPolicy")
    def reset_network_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkPolicy", []))

    @jsii.member(jsii_name="resetNodeConfig")
    def reset_node_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeConfig", []))

    @jsii.member(jsii_name="resetNodeLocations")
    def reset_node_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeLocations", []))

    @jsii.member(jsii_name="resetNodePool")
    def reset_node_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePool", []))

    @jsii.member(jsii_name="resetNodeVersion")
    def reset_node_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeVersion", []))

    @jsii.member(jsii_name="resetNotificationConfig")
    def reset_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfig", []))

    @jsii.member(jsii_name="resetPrivateClusterConfig")
    def reset_private_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateClusterConfig", []))

    @jsii.member(jsii_name="resetPrivateIpv6GoogleAccess")
    def reset_private_ipv6_google_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpv6GoogleAccess", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetReleaseChannel")
    def reset_release_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReleaseChannel", []))

    @jsii.member(jsii_name="resetRemoveDefaultNodePool")
    def reset_remove_default_node_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveDefaultNodePool", []))

    @jsii.member(jsii_name="resetResourceLabels")
    def reset_resource_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabels", []))

    @jsii.member(jsii_name="resetResourceUsageExportConfig")
    def reset_resource_usage_export_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceUsageExportConfig", []))

    @jsii.member(jsii_name="resetServiceExternalIpsConfig")
    def reset_service_external_ips_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceExternalIpsConfig", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVerticalPodAutoscaling")
    def reset_vertical_pod_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalPodAutoscaling", []))

    @jsii.member(jsii_name="resetWorkloadIdentityConfig")
    def reset_workload_identity_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadIdentityConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="addonsConfig")
    def addons_config(self) -> "ContainerClusterAddonsConfigOutputReference":
        return typing.cast("ContainerClusterAddonsConfigOutputReference", jsii.get(self, "addonsConfig"))

    @builtins.property
    @jsii.member(jsii_name="authenticatorGroupsConfig")
    def authenticator_groups_config(
        self,
    ) -> "ContainerClusterAuthenticatorGroupsConfigOutputReference":
        return typing.cast("ContainerClusterAuthenticatorGroupsConfigOutputReference", jsii.get(self, "authenticatorGroupsConfig"))

    @builtins.property
    @jsii.member(jsii_name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> "ContainerClusterBinaryAuthorizationOutputReference":
        return typing.cast("ContainerClusterBinaryAuthorizationOutputReference", jsii.get(self, "binaryAuthorization"))

    @builtins.property
    @jsii.member(jsii_name="clusterAutoscaling")
    def cluster_autoscaling(
        self,
    ) -> "ContainerClusterClusterAutoscalingOutputReference":
        return typing.cast("ContainerClusterClusterAutoscalingOutputReference", jsii.get(self, "clusterAutoscaling"))

    @builtins.property
    @jsii.member(jsii_name="confidentialNodes")
    def confidential_nodes(self) -> "ContainerClusterConfidentialNodesOutputReference":
        return typing.cast("ContainerClusterConfidentialNodesOutputReference", jsii.get(self, "confidentialNodes"))

    @builtins.property
    @jsii.member(jsii_name="databaseEncryption")
    def database_encryption(
        self,
    ) -> "ContainerClusterDatabaseEncryptionOutputReference":
        return typing.cast("ContainerClusterDatabaseEncryptionOutputReference", jsii.get(self, "databaseEncryption"))

    @builtins.property
    @jsii.member(jsii_name="defaultSnatStatus")
    def default_snat_status(self) -> "ContainerClusterDefaultSnatStatusOutputReference":
        return typing.cast("ContainerClusterDefaultSnatStatusOutputReference", jsii.get(self, "defaultSnatStatus"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfig")
    def dns_config(self) -> "ContainerClusterDnsConfigOutputReference":
        return typing.cast("ContainerClusterDnsConfigOutputReference", jsii.get(self, "dnsConfig"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="ipAllocationPolicy")
    def ip_allocation_policy(
        self,
    ) -> "ContainerClusterIpAllocationPolicyOutputReference":
        return typing.cast("ContainerClusterIpAllocationPolicyOutputReference", jsii.get(self, "ipAllocationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(self) -> "ContainerClusterLoggingConfigOutputReference":
        return typing.cast("ContainerClusterLoggingConfigOutputReference", jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicy")
    def maintenance_policy(self) -> "ContainerClusterMaintenancePolicyOutputReference":
        return typing.cast("ContainerClusterMaintenancePolicyOutputReference", jsii.get(self, "maintenancePolicy"))

    @builtins.property
    @jsii.member(jsii_name="masterAuth")
    def master_auth(self) -> "ContainerClusterMasterAuthOutputReference":
        return typing.cast("ContainerClusterMasterAuthOutputReference", jsii.get(self, "masterAuth"))

    @builtins.property
    @jsii.member(jsii_name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(
        self,
    ) -> "ContainerClusterMasterAuthorizedNetworksConfigOutputReference":
        return typing.cast("ContainerClusterMasterAuthorizedNetworksConfigOutputReference", jsii.get(self, "masterAuthorizedNetworksConfig"))

    @builtins.property
    @jsii.member(jsii_name="masterVersion")
    def master_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterVersion"))

    @builtins.property
    @jsii.member(jsii_name="meshCertificates")
    def mesh_certificates(self) -> "ContainerClusterMeshCertificatesOutputReference":
        return typing.cast("ContainerClusterMeshCertificatesOutputReference", jsii.get(self, "meshCertificates"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfig")
    def monitoring_config(self) -> "ContainerClusterMonitoringConfigOutputReference":
        return typing.cast("ContainerClusterMonitoringConfigOutputReference", jsii.get(self, "monitoringConfig"))

    @builtins.property
    @jsii.member(jsii_name="networkPolicy")
    def network_policy(self) -> "ContainerClusterNetworkPolicyOutputReference":
        return typing.cast("ContainerClusterNetworkPolicyOutputReference", jsii.get(self, "networkPolicy"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfig")
    def node_config(self) -> "ContainerClusterNodeConfigOutputReference":
        return typing.cast("ContainerClusterNodeConfigOutputReference", jsii.get(self, "nodeConfig"))

    @builtins.property
    @jsii.member(jsii_name="nodePool")
    def node_pool(self) -> "ContainerClusterNodePoolList":
        return typing.cast("ContainerClusterNodePoolList", jsii.get(self, "nodePool"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfig")
    def notification_config(
        self,
    ) -> "ContainerClusterNotificationConfigOutputReference":
        return typing.cast("ContainerClusterNotificationConfigOutputReference", jsii.get(self, "notificationConfig"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="privateClusterConfig")
    def private_cluster_config(
        self,
    ) -> "ContainerClusterPrivateClusterConfigOutputReference":
        return typing.cast("ContainerClusterPrivateClusterConfigOutputReference", jsii.get(self, "privateClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="releaseChannel")
    def release_channel(self) -> "ContainerClusterReleaseChannelOutputReference":
        return typing.cast("ContainerClusterReleaseChannelOutputReference", jsii.get(self, "releaseChannel"))

    @builtins.property
    @jsii.member(jsii_name="resourceUsageExportConfig")
    def resource_usage_export_config(
        self,
    ) -> "ContainerClusterResourceUsageExportConfigOutputReference":
        return typing.cast("ContainerClusterResourceUsageExportConfigOutputReference", jsii.get(self, "resourceUsageExportConfig"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="serviceExternalIpsConfig")
    def service_external_ips_config(
        self,
    ) -> "ContainerClusterServiceExternalIpsConfigOutputReference":
        return typing.cast("ContainerClusterServiceExternalIpsConfigOutputReference", jsii.get(self, "serviceExternalIpsConfig"))

    @builtins.property
    @jsii.member(jsii_name="servicesIpv4Cidr")
    def services_ipv4_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicesIpv4Cidr"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ContainerClusterTimeoutsOutputReference":
        return typing.cast("ContainerClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tpuIpv4CidrBlock")
    def tpu_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tpuIpv4CidrBlock"))

    @builtins.property
    @jsii.member(jsii_name="verticalPodAutoscaling")
    def vertical_pod_autoscaling(
        self,
    ) -> "ContainerClusterVerticalPodAutoscalingOutputReference":
        return typing.cast("ContainerClusterVerticalPodAutoscalingOutputReference", jsii.get(self, "verticalPodAutoscaling"))

    @builtins.property
    @jsii.member(jsii_name="workloadIdentityConfig")
    def workload_identity_config(
        self,
    ) -> "ContainerClusterWorkloadIdentityConfigOutputReference":
        return typing.cast("ContainerClusterWorkloadIdentityConfigOutputReference", jsii.get(self, "workloadIdentityConfig"))

    @builtins.property
    @jsii.member(jsii_name="addonsConfigInput")
    def addons_config_input(self) -> typing.Optional["ContainerClusterAddonsConfig"]:
        return typing.cast(typing.Optional["ContainerClusterAddonsConfig"], jsii.get(self, "addonsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticatorGroupsConfigInput")
    def authenticator_groups_config_input(
        self,
    ) -> typing.Optional["ContainerClusterAuthenticatorGroupsConfig"]:
        return typing.cast(typing.Optional["ContainerClusterAuthenticatorGroupsConfig"], jsii.get(self, "authenticatorGroupsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="binaryAuthorizationInput")
    def binary_authorization_input(
        self,
    ) -> typing.Optional["ContainerClusterBinaryAuthorization"]:
        return typing.cast(typing.Optional["ContainerClusterBinaryAuthorization"], jsii.get(self, "binaryAuthorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterAutoscalingInput")
    def cluster_autoscaling_input(
        self,
    ) -> typing.Optional["ContainerClusterClusterAutoscaling"]:
        return typing.cast(typing.Optional["ContainerClusterClusterAutoscaling"], jsii.get(self, "clusterAutoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIpv4CidrInput")
    def cluster_ipv4_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIpv4CidrInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialNodesInput")
    def confidential_nodes_input(
        self,
    ) -> typing.Optional["ContainerClusterConfidentialNodes"]:
        return typing.cast(typing.Optional["ContainerClusterConfidentialNodes"], jsii.get(self, "confidentialNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseEncryptionInput")
    def database_encryption_input(
        self,
    ) -> typing.Optional["ContainerClusterDatabaseEncryption"]:
        return typing.cast(typing.Optional["ContainerClusterDatabaseEncryption"], jsii.get(self, "databaseEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="datapathProviderInput")
    def datapath_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datapathProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultMaxPodsPerNodeInput")
    def default_max_pods_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultMaxPodsPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSnatStatusInput")
    def default_snat_status_input(
        self,
    ) -> typing.Optional["ContainerClusterDefaultSnatStatus"]:
        return typing.cast(typing.Optional["ContainerClusterDefaultSnatStatus"], jsii.get(self, "defaultSnatStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfigInput")
    def dns_config_input(self) -> typing.Optional["ContainerClusterDnsConfig"]:
        return typing.cast(typing.Optional["ContainerClusterDnsConfig"], jsii.get(self, "dnsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutopilotInput")
    def enable_autopilot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutopilotInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBinaryAuthorizationInput")
    def enable_binary_authorization_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBinaryAuthorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntranodeVisibilityInput")
    def enable_intranode_visibility_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntranodeVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="enableKubernetesAlphaInput")
    def enable_kubernetes_alpha_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableKubernetesAlphaInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLegacyAbacInput")
    def enable_legacy_abac_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLegacyAbacInput"))

    @builtins.property
    @jsii.member(jsii_name="enableShieldedNodesInput")
    def enable_shielded_nodes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableShieldedNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableTpuInput")
    def enable_tpu_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableTpuInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialNodeCountInput")
    def initial_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAllocationPolicyInput")
    def ip_allocation_policy_input(
        self,
    ) -> typing.Optional["ContainerClusterIpAllocationPolicy"]:
        return typing.cast(typing.Optional["ContainerClusterIpAllocationPolicy"], jsii.get(self, "ipAllocationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(self) -> typing.Optional["ContainerClusterLoggingConfig"]:
        return typing.cast(typing.Optional["ContainerClusterLoggingConfig"], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingServiceInput")
    def logging_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicyInput")
    def maintenance_policy_input(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicy"]:
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicy"], jsii.get(self, "maintenancePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="masterAuthInput")
    def master_auth_input(self) -> typing.Optional["ContainerClusterMasterAuth"]:
        return typing.cast(typing.Optional["ContainerClusterMasterAuth"], jsii.get(self, "masterAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="masterAuthorizedNetworksConfigInput")
    def master_authorized_networks_config_input(
        self,
    ) -> typing.Optional["ContainerClusterMasterAuthorizedNetworksConfig"]:
        return typing.cast(typing.Optional["ContainerClusterMasterAuthorizedNetworksConfig"], jsii.get(self, "masterAuthorizedNetworksConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="meshCertificatesInput")
    def mesh_certificates_input(
        self,
    ) -> typing.Optional["ContainerClusterMeshCertificates"]:
        return typing.cast(typing.Optional["ContainerClusterMeshCertificates"], jsii.get(self, "meshCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="minMasterVersionInput")
    def min_master_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minMasterVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfigInput")
    def monitoring_config_input(
        self,
    ) -> typing.Optional["ContainerClusterMonitoringConfig"]:
        return typing.cast(typing.Optional["ContainerClusterMonitoringConfig"], jsii.get(self, "monitoringConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringServiceInput")
    def monitoring_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkingModeInput")
    def networking_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPolicyInput")
    def network_policy_input(self) -> typing.Optional["ContainerClusterNetworkPolicy"]:
        return typing.cast(typing.Optional["ContainerClusterNetworkPolicy"], jsii.get(self, "networkPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfigInput")
    def node_config_input(self) -> typing.Optional["ContainerClusterNodeConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNodeConfig"], jsii.get(self, "nodeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeLocationsInput")
    def node_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodeLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolInput")
    def node_pool_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePool"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePool"]]], jsii.get(self, "nodePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeVersionInput")
    def node_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigInput")
    def notification_config_input(
        self,
    ) -> typing.Optional["ContainerClusterNotificationConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNotificationConfig"], jsii.get(self, "notificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="privateClusterConfigInput")
    def private_cluster_config_input(
        self,
    ) -> typing.Optional["ContainerClusterPrivateClusterConfig"]:
        return typing.cast(typing.Optional["ContainerClusterPrivateClusterConfig"], jsii.get(self, "privateClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccessInput")
    def private_ipv6_google_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpv6GoogleAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseChannelInput")
    def release_channel_input(
        self,
    ) -> typing.Optional["ContainerClusterReleaseChannel"]:
        return typing.cast(typing.Optional["ContainerClusterReleaseChannel"], jsii.get(self, "releaseChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="removeDefaultNodePoolInput")
    def remove_default_node_pool_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "removeDefaultNodePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelsInput")
    def resource_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "resourceLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceUsageExportConfigInput")
    def resource_usage_export_config_input(
        self,
    ) -> typing.Optional["ContainerClusterResourceUsageExportConfig"]:
        return typing.cast(typing.Optional["ContainerClusterResourceUsageExportConfig"], jsii.get(self, "resourceUsageExportConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceExternalIpsConfigInput")
    def service_external_ips_config_input(
        self,
    ) -> typing.Optional["ContainerClusterServiceExternalIpsConfig"]:
        return typing.cast(typing.Optional["ContainerClusterServiceExternalIpsConfig"], jsii.get(self, "serviceExternalIpsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ContainerClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ContainerClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalPodAutoscalingInput")
    def vertical_pod_autoscaling_input(
        self,
    ) -> typing.Optional["ContainerClusterVerticalPodAutoscaling"]:
        return typing.cast(typing.Optional["ContainerClusterVerticalPodAutoscaling"], jsii.get(self, "verticalPodAutoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadIdentityConfigInput")
    def workload_identity_config_input(
        self,
    ) -> typing.Optional["ContainerClusterWorkloadIdentityConfig"]:
        return typing.cast(typing.Optional["ContainerClusterWorkloadIdentityConfig"], jsii.get(self, "workloadIdentityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIpv4Cidr"))

    @cluster_ipv4_cidr.setter
    def cluster_ipv4_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "cluster_ipv4_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIpv4Cidr", value)

    @builtins.property
    @jsii.member(jsii_name="datapathProvider")
    def datapath_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datapathProvider"))

    @datapath_provider.setter
    def datapath_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "datapath_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datapathProvider", value)

    @builtins.property
    @jsii.member(jsii_name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultMaxPodsPerNode"))

    @default_max_pods_per_node.setter
    def default_max_pods_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "default_max_pods_per_node").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultMaxPodsPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutopilot")
    def enable_autopilot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutopilot"))

    @enable_autopilot.setter
    def enable_autopilot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_autopilot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutopilot", value)

    @builtins.property
    @jsii.member(jsii_name="enableBinaryAuthorization")
    def enable_binary_authorization(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBinaryAuthorization"))

    @enable_binary_authorization.setter
    def enable_binary_authorization(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_binary_authorization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBinaryAuthorization", value)

    @builtins.property
    @jsii.member(jsii_name="enableIntranodeVisibility")
    def enable_intranode_visibility(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntranodeVisibility"))

    @enable_intranode_visibility.setter
    def enable_intranode_visibility(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_intranode_visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntranodeVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableKubernetesAlpha"))

    @enable_kubernetes_alpha.setter
    def enable_kubernetes_alpha(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_kubernetes_alpha").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableKubernetesAlpha", value)

    @builtins.property
    @jsii.member(jsii_name="enableLegacyAbac")
    def enable_legacy_abac(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLegacyAbac"))

    @enable_legacy_abac.setter
    def enable_legacy_abac(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_legacy_abac").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLegacyAbac", value)

    @builtins.property
    @jsii.member(jsii_name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableShieldedNodes"))

    @enable_shielded_nodes.setter
    def enable_shielded_nodes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_shielded_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableShieldedNodes", value)

    @builtins.property
    @jsii.member(jsii_name="enableTpu")
    def enable_tpu(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableTpu"))

    @enable_tpu.setter
    def enable_tpu(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "enable_tpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableTpu", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialNodeCount")
    def initial_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialNodeCount"))

    @initial_node_count.setter
    def initial_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "initial_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="loggingService")
    def logging_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loggingService"))

    @logging_service.setter
    def logging_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "logging_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingService", value)

    @builtins.property
    @jsii.member(jsii_name="minMasterVersion")
    def min_master_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minMasterVersion"))

    @min_master_version.setter
    def min_master_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "min_master_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minMasterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringService")
    def monitoring_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitoringService"))

    @monitoring_service.setter
    def monitoring_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "monitoring_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringService", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="networkingMode")
    def networking_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkingMode"))

    @networking_mode.setter
    def networking_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "networking_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkingMode", value)

    @builtins.property
    @jsii.member(jsii_name="nodeLocations")
    def node_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeLocations"))

    @node_locations.setter
    def node_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "node_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeLocations", value)

    @builtins.property
    @jsii.member(jsii_name="nodeVersion")
    def node_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeVersion"))

    @node_version.setter
    def node_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "node_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpv6GoogleAccess"))

    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "private_ipv6_google_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpv6GoogleAccess", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="removeDefaultNodePool")
    def remove_default_node_pool(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "removeDefaultNodePool"))

    @remove_default_node_pool.setter
    def remove_default_node_pool(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "remove_default_node_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeDefaultNodePool", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabels")
    def resource_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "resourceLabels"))

    @resource_labels.setter
    def resource_labels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "resource_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabels", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCluster, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudrun_config": "cloudrunConfig",
        "dns_cache_config": "dnsCacheConfig",
        "gce_persistent_disk_csi_driver_config": "gcePersistentDiskCsiDriverConfig",
        "gcp_filestore_csi_driver_config": "gcpFilestoreCsiDriverConfig",
        "horizontal_pod_autoscaling": "horizontalPodAutoscaling",
        "http_load_balancing": "httpLoadBalancing",
        "network_policy_config": "networkPolicyConfig",
    },
)
class ContainerClusterAddonsConfig:
    def __init__(
        self,
        *,
        cloudrun_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigCloudrunConfig", typing.Dict[str, typing.Any]]] = None,
        dns_cache_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigDnsCacheConfig", typing.Dict[str, typing.Any]]] = None,
        gce_persistent_disk_csi_driver_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig", typing.Dict[str, typing.Any]]] = None,
        gcp_filestore_csi_driver_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig", typing.Dict[str, typing.Any]]] = None,
        horizontal_pod_autoscaling: typing.Optional[typing.Union["ContainerClusterAddonsConfigHorizontalPodAutoscaling", typing.Dict[str, typing.Any]]] = None,
        http_load_balancing: typing.Optional[typing.Union["ContainerClusterAddonsConfigHttpLoadBalancing", typing.Dict[str, typing.Any]]] = None,
        network_policy_config: typing.Optional[typing.Union["ContainerClusterAddonsConfigNetworkPolicyConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudrun_config: cloudrun_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cloudrun_config ContainerCluster#cloudrun_config}
        :param dns_cache_config: dns_cache_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_cache_config ContainerCluster#dns_cache_config}
        :param gce_persistent_disk_csi_driver_config: gce_persistent_disk_csi_driver_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gce_persistent_disk_csi_driver_config ContainerCluster#gce_persistent_disk_csi_driver_config}
        :param gcp_filestore_csi_driver_config: gcp_filestore_csi_driver_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcp_filestore_csi_driver_config ContainerCluster#gcp_filestore_csi_driver_config}
        :param horizontal_pod_autoscaling: horizontal_pod_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#horizontal_pod_autoscaling ContainerCluster#horizontal_pod_autoscaling}
        :param http_load_balancing: http_load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#http_load_balancing ContainerCluster#http_load_balancing}
        :param network_policy_config: network_policy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy_config ContainerCluster#network_policy_config}
        '''
        if isinstance(cloudrun_config, dict):
            cloudrun_config = ContainerClusterAddonsConfigCloudrunConfig(**cloudrun_config)
        if isinstance(dns_cache_config, dict):
            dns_cache_config = ContainerClusterAddonsConfigDnsCacheConfig(**dns_cache_config)
        if isinstance(gce_persistent_disk_csi_driver_config, dict):
            gce_persistent_disk_csi_driver_config = ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig(**gce_persistent_disk_csi_driver_config)
        if isinstance(gcp_filestore_csi_driver_config, dict):
            gcp_filestore_csi_driver_config = ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig(**gcp_filestore_csi_driver_config)
        if isinstance(horizontal_pod_autoscaling, dict):
            horizontal_pod_autoscaling = ContainerClusterAddonsConfigHorizontalPodAutoscaling(**horizontal_pod_autoscaling)
        if isinstance(http_load_balancing, dict):
            http_load_balancing = ContainerClusterAddonsConfigHttpLoadBalancing(**http_load_balancing)
        if isinstance(network_policy_config, dict):
            network_policy_config = ContainerClusterAddonsConfigNetworkPolicyConfig(**network_policy_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfig.__init__)
            check_type(argname="argument cloudrun_config", value=cloudrun_config, expected_type=type_hints["cloudrun_config"])
            check_type(argname="argument dns_cache_config", value=dns_cache_config, expected_type=type_hints["dns_cache_config"])
            check_type(argname="argument gce_persistent_disk_csi_driver_config", value=gce_persistent_disk_csi_driver_config, expected_type=type_hints["gce_persistent_disk_csi_driver_config"])
            check_type(argname="argument gcp_filestore_csi_driver_config", value=gcp_filestore_csi_driver_config, expected_type=type_hints["gcp_filestore_csi_driver_config"])
            check_type(argname="argument horizontal_pod_autoscaling", value=horizontal_pod_autoscaling, expected_type=type_hints["horizontal_pod_autoscaling"])
            check_type(argname="argument http_load_balancing", value=http_load_balancing, expected_type=type_hints["http_load_balancing"])
            check_type(argname="argument network_policy_config", value=network_policy_config, expected_type=type_hints["network_policy_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudrun_config is not None:
            self._values["cloudrun_config"] = cloudrun_config
        if dns_cache_config is not None:
            self._values["dns_cache_config"] = dns_cache_config
        if gce_persistent_disk_csi_driver_config is not None:
            self._values["gce_persistent_disk_csi_driver_config"] = gce_persistent_disk_csi_driver_config
        if gcp_filestore_csi_driver_config is not None:
            self._values["gcp_filestore_csi_driver_config"] = gcp_filestore_csi_driver_config
        if horizontal_pod_autoscaling is not None:
            self._values["horizontal_pod_autoscaling"] = horizontal_pod_autoscaling
        if http_load_balancing is not None:
            self._values["http_load_balancing"] = http_load_balancing
        if network_policy_config is not None:
            self._values["network_policy_config"] = network_policy_config

    @builtins.property
    def cloudrun_config(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigCloudrunConfig"]:
        '''cloudrun_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cloudrun_config ContainerCluster#cloudrun_config}
        '''
        result = self._values.get("cloudrun_config")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigCloudrunConfig"], result)

    @builtins.property
    def dns_cache_config(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigDnsCacheConfig"]:
        '''dns_cache_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_cache_config ContainerCluster#dns_cache_config}
        '''
        result = self._values.get("dns_cache_config")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigDnsCacheConfig"], result)

    @builtins.property
    def gce_persistent_disk_csi_driver_config(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig"]:
        '''gce_persistent_disk_csi_driver_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gce_persistent_disk_csi_driver_config ContainerCluster#gce_persistent_disk_csi_driver_config}
        '''
        result = self._values.get("gce_persistent_disk_csi_driver_config")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig"], result)

    @builtins.property
    def gcp_filestore_csi_driver_config(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig"]:
        '''gcp_filestore_csi_driver_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcp_filestore_csi_driver_config ContainerCluster#gcp_filestore_csi_driver_config}
        '''
        result = self._values.get("gcp_filestore_csi_driver_config")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig"], result)

    @builtins.property
    def horizontal_pod_autoscaling(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigHorizontalPodAutoscaling"]:
        '''horizontal_pod_autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#horizontal_pod_autoscaling ContainerCluster#horizontal_pod_autoscaling}
        '''
        result = self._values.get("horizontal_pod_autoscaling")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigHorizontalPodAutoscaling"], result)

    @builtins.property
    def http_load_balancing(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigHttpLoadBalancing"]:
        '''http_load_balancing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#http_load_balancing ContainerCluster#http_load_balancing}
        '''
        result = self._values.get("http_load_balancing")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigHttpLoadBalancing"], result)

    @builtins.property
    def network_policy_config(
        self,
    ) -> typing.Optional["ContainerClusterAddonsConfigNetworkPolicyConfig"]:
        '''network_policy_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy_config ContainerCluster#network_policy_config}
        '''
        result = self._values.get("network_policy_config")
        return typing.cast(typing.Optional["ContainerClusterAddonsConfigNetworkPolicyConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigCloudrunConfig",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled", "load_balancer_type": "loadBalancerType"},
)
class ContainerClusterAddonsConfigCloudrunConfig:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        load_balancer_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        :param load_balancer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#load_balancer_type ContainerCluster#load_balancer_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigCloudrunConfig.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument load_balancer_type", value=load_balancer_type, expected_type=type_hints["load_balancer_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }
        if load_balancer_type is not None:
            self._values["load_balancer_type"] = load_balancer_type

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.'''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def load_balancer_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#load_balancer_type ContainerCluster#load_balancer_type}.'''
        result = self._values.get("load_balancer_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigCloudrunConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigCloudrunConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigCloudrunConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigCloudrunConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLoadBalancerType")
    def reset_load_balancer_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerType", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTypeInput")
    def load_balancer_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigCloudrunConfigOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerType")
    def load_balancer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerType"))

    @load_balancer_type.setter
    def load_balancer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigCloudrunConfigOutputReference, "load_balancer_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigCloudrunConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigCloudrunConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigCloudrunConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigCloudrunConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigDnsCacheConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterAddonsConfigDnsCacheConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigDnsCacheConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigDnsCacheConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigDnsCacheConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigDnsCacheConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigDnsCacheConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigDnsCacheConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigDnsCacheConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigDnsCacheConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigDnsCacheConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigDnsCacheConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigHorizontalPodAutoscaling",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled"},
)
class ContainerClusterAddonsConfigHorizontalPodAutoscaling:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigHorizontalPodAutoscaling.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.'''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigHorizontalPodAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigHorizontalPodAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigHorizontalPodAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigHorizontalPodAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigHttpLoadBalancing",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled"},
)
class ContainerClusterAddonsConfigHttpLoadBalancing:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigHttpLoadBalancing.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.'''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigHttpLoadBalancing(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigHttpLoadBalancingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigHttpLoadBalancingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigHttpLoadBalancingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigHttpLoadBalancingOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigHttpLoadBalancing]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigHttpLoadBalancing], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigHttpLoadBalancing],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigHttpLoadBalancingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigNetworkPolicyConfig",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled"},
)
class ContainerClusterAddonsConfigNetworkPolicyConfig:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigNetworkPolicyConfig.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.'''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAddonsConfigNetworkPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigNetworkPolicyConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigNetworkPolicyConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfigNetworkPolicyConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterAddonsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAddonsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAddonsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudrunConfig")
    def put_cloudrun_config(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        load_balancer_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        :param load_balancer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#load_balancer_type ContainerCluster#load_balancer_type}.
        '''
        value = ContainerClusterAddonsConfigCloudrunConfig(
            disabled=disabled, load_balancer_type=load_balancer_type
        )

        return typing.cast(None, jsii.invoke(self, "putCloudrunConfig", [value]))

    @jsii.member(jsii_name="putDnsCacheConfig")
    def put_dns_cache_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        value = ContainerClusterAddonsConfigDnsCacheConfig(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putDnsCacheConfig", [value]))

    @jsii.member(jsii_name="putGcePersistentDiskCsiDriverConfig")
    def put_gce_persistent_disk_csi_driver_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        value = ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putGcePersistentDiskCsiDriverConfig", [value]))

    @jsii.member(jsii_name="putGcpFilestoreCsiDriverConfig")
    def put_gcp_filestore_csi_driver_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}.
        '''
        value = ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putGcpFilestoreCsiDriverConfig", [value]))

    @jsii.member(jsii_name="putHorizontalPodAutoscaling")
    def put_horizontal_pod_autoscaling(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        value = ContainerClusterAddonsConfigHorizontalPodAutoscaling(disabled=disabled)

        return typing.cast(None, jsii.invoke(self, "putHorizontalPodAutoscaling", [value]))

    @jsii.member(jsii_name="putHttpLoadBalancing")
    def put_http_load_balancing(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        value = ContainerClusterAddonsConfigHttpLoadBalancing(disabled=disabled)

        return typing.cast(None, jsii.invoke(self, "putHttpLoadBalancing", [value]))

    @jsii.member(jsii_name="putNetworkPolicyConfig")
    def put_network_policy_config(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}.
        '''
        value = ContainerClusterAddonsConfigNetworkPolicyConfig(disabled=disabled)

        return typing.cast(None, jsii.invoke(self, "putNetworkPolicyConfig", [value]))

    @jsii.member(jsii_name="resetCloudrunConfig")
    def reset_cloudrun_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudrunConfig", []))

    @jsii.member(jsii_name="resetDnsCacheConfig")
    def reset_dns_cache_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsCacheConfig", []))

    @jsii.member(jsii_name="resetGcePersistentDiskCsiDriverConfig")
    def reset_gce_persistent_disk_csi_driver_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePersistentDiskCsiDriverConfig", []))

    @jsii.member(jsii_name="resetGcpFilestoreCsiDriverConfig")
    def reset_gcp_filestore_csi_driver_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpFilestoreCsiDriverConfig", []))

    @jsii.member(jsii_name="resetHorizontalPodAutoscaling")
    def reset_horizontal_pod_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalPodAutoscaling", []))

    @jsii.member(jsii_name="resetHttpLoadBalancing")
    def reset_http_load_balancing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpLoadBalancing", []))

    @jsii.member(jsii_name="resetNetworkPolicyConfig")
    def reset_network_policy_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkPolicyConfig", []))

    @builtins.property
    @jsii.member(jsii_name="cloudrunConfig")
    def cloudrun_config(
        self,
    ) -> ContainerClusterAddonsConfigCloudrunConfigOutputReference:
        return typing.cast(ContainerClusterAddonsConfigCloudrunConfigOutputReference, jsii.get(self, "cloudrunConfig"))

    @builtins.property
    @jsii.member(jsii_name="dnsCacheConfig")
    def dns_cache_config(
        self,
    ) -> ContainerClusterAddonsConfigDnsCacheConfigOutputReference:
        return typing.cast(ContainerClusterAddonsConfigDnsCacheConfigOutputReference, jsii.get(self, "dnsCacheConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskCsiDriverConfig")
    def gce_persistent_disk_csi_driver_config(
        self,
    ) -> ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference:
        return typing.cast(ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference, jsii.get(self, "gcePersistentDiskCsiDriverConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcpFilestoreCsiDriverConfig")
    def gcp_filestore_csi_driver_config(
        self,
    ) -> ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference:
        return typing.cast(ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference, jsii.get(self, "gcpFilestoreCsiDriverConfig"))

    @builtins.property
    @jsii.member(jsii_name="horizontalPodAutoscaling")
    def horizontal_pod_autoscaling(
        self,
    ) -> ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference:
        return typing.cast(ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference, jsii.get(self, "horizontalPodAutoscaling"))

    @builtins.property
    @jsii.member(jsii_name="httpLoadBalancing")
    def http_load_balancing(
        self,
    ) -> ContainerClusterAddonsConfigHttpLoadBalancingOutputReference:
        return typing.cast(ContainerClusterAddonsConfigHttpLoadBalancingOutputReference, jsii.get(self, "httpLoadBalancing"))

    @builtins.property
    @jsii.member(jsii_name="networkPolicyConfig")
    def network_policy_config(
        self,
    ) -> ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference:
        return typing.cast(ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference, jsii.get(self, "networkPolicyConfig"))

    @builtins.property
    @jsii.member(jsii_name="cloudrunConfigInput")
    def cloudrun_config_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigCloudrunConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigCloudrunConfig], jsii.get(self, "cloudrunConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsCacheConfigInput")
    def dns_cache_config_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigDnsCacheConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigDnsCacheConfig], jsii.get(self, "dnsCacheConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskCsiDriverConfigInput")
    def gce_persistent_disk_csi_driver_config_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig], jsii.get(self, "gcePersistentDiskCsiDriverConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpFilestoreCsiDriverConfigInput")
    def gcp_filestore_csi_driver_config_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig], jsii.get(self, "gcpFilestoreCsiDriverConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalPodAutoscalingInput")
    def horizontal_pod_autoscaling_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigHorizontalPodAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigHorizontalPodAutoscaling], jsii.get(self, "horizontalPodAutoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="httpLoadBalancingInput")
    def http_load_balancing_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigHttpLoadBalancing]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigHttpLoadBalancing], jsii.get(self, "httpLoadBalancingInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPolicyConfigInput")
    def network_policy_config_input(
        self,
    ) -> typing.Optional[ContainerClusterAddonsConfigNetworkPolicyConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfigNetworkPolicyConfig], jsii.get(self, "networkPolicyConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterAddonsConfig]:
        return typing.cast(typing.Optional[ContainerClusterAddonsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAddonsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAddonsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAuthenticatorGroupsConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group": "securityGroup"},
)
class ContainerClusterAuthenticatorGroupsConfig:
    def __init__(self, *, security_group: builtins.str) -> None:
        '''
        :param security_group: The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format gke-security-groups@yourdomain.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#security_group ContainerCluster#security_group}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterAuthenticatorGroupsConfig.__init__)
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "security_group": security_group,
        }

    @builtins.property
    def security_group(self) -> builtins.str:
        '''The name of the RBAC security group for use with Google security groups in Kubernetes RBAC.

        Group name must be in format gke-security-groups@yourdomain.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#security_group ContainerCluster#security_group}
        '''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterAuthenticatorGroupsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterAuthenticatorGroupsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterAuthenticatorGroupsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterAuthenticatorGroupsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="securityGroupInput")
    def security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroup"))

    @security_group.setter
    def security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAuthenticatorGroupsConfigOutputReference, "security_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterAuthenticatorGroupsConfig]:
        return typing.cast(typing.Optional[ContainerClusterAuthenticatorGroupsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterAuthenticatorGroupsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterAuthenticatorGroupsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterBinaryAuthorization",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "evaluation_mode": "evaluationMode"},
)
class ContainerClusterBinaryAuthorization:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        evaluation_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable Binary Authorization for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param evaluation_mode: Mode of operation for Binary Authorization policy evaluation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#evaluation_mode ContainerCluster#evaluation_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterBinaryAuthorization.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument evaluation_mode", value=evaluation_mode, expected_type=type_hints["evaluation_mode"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if evaluation_mode is not None:
            self._values["evaluation_mode"] = evaluation_mode

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Binary Authorization for this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def evaluation_mode(self) -> typing.Optional[builtins.str]:
        '''Mode of operation for Binary Authorization policy evaluation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#evaluation_mode ContainerCluster#evaluation_mode}
        '''
        result = self._values.get("evaluation_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterBinaryAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterBinaryAuthorizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterBinaryAuthorizationOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterBinaryAuthorizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEvaluationMode")
    def reset_evaluation_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationMode", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationModeInput")
    def evaluation_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterBinaryAuthorizationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMode")
    def evaluation_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationMode"))

    @evaluation_mode.setter
    def evaluation_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterBinaryAuthorizationOutputReference, "evaluation_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterBinaryAuthorization]:
        return typing.cast(typing.Optional[ContainerClusterBinaryAuthorization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterBinaryAuthorization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterBinaryAuthorizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscaling",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "auto_provisioning_defaults": "autoProvisioningDefaults",
        "resource_limits": "resourceLimits",
    },
)
class ContainerClusterClusterAutoscaling:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_provisioning_defaults: typing.Optional[typing.Union["ContainerClusterClusterAutoscalingAutoProvisioningDefaults", typing.Dict[str, typing.Any]]] = None,
        resource_limits: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterClusterAutoscalingResourceLimits", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether node auto-provisioning is enabled. Resource limits for cpu and memory must be defined to enable node auto-provisioning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param auto_provisioning_defaults: auto_provisioning_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_provisioning_defaults ContainerCluster#auto_provisioning_defaults}
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_limits ContainerCluster#resource_limits}
        '''
        if isinstance(auto_provisioning_defaults, dict):
            auto_provisioning_defaults = ContainerClusterClusterAutoscalingAutoProvisioningDefaults(**auto_provisioning_defaults)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscaling.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument auto_provisioning_defaults", value=auto_provisioning_defaults, expected_type=type_hints["auto_provisioning_defaults"])
            check_type(argname="argument resource_limits", value=resource_limits, expected_type=type_hints["resource_limits"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if auto_provisioning_defaults is not None:
            self._values["auto_provisioning_defaults"] = auto_provisioning_defaults
        if resource_limits is not None:
            self._values["resource_limits"] = resource_limits

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether node auto-provisioning is enabled. Resource limits for cpu and memory must be defined to enable node auto-provisioning.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def auto_provisioning_defaults(
        self,
    ) -> typing.Optional["ContainerClusterClusterAutoscalingAutoProvisioningDefaults"]:
        '''auto_provisioning_defaults block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_provisioning_defaults ContainerCluster#auto_provisioning_defaults}
        '''
        result = self._values.get("auto_provisioning_defaults")
        return typing.cast(typing.Optional["ContainerClusterClusterAutoscalingAutoProvisioningDefaults"], result)

    @builtins.property
    def resource_limits(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterClusterAutoscalingResourceLimits"]]]:
        '''resource_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_limits ContainerCluster#resource_limits}
        '''
        result = self._values.get("resource_limits")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterClusterAutoscalingResourceLimits"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterClusterAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingAutoProvisioningDefaults",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_kms_key": "bootDiskKmsKey",
        "image_type": "imageType",
        "oauth_scopes": "oauthScopes",
        "service_account": "serviceAccount",
    },
)
class ContainerClusterClusterAutoscalingAutoProvisioningDefaults:
    def __init__(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        image_type: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param image_type: The default image type used by NAP once a new node pool is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param oauth_scopes: Scopes that are used by NAP when creating node pools. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingAutoProvisioningDefaults.__init__)
            check_type(argname="argument boot_disk_kms_key", value=boot_disk_kms_key, expected_type=type_hints["boot_disk_kms_key"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_kms_key is not None:
            self._values["boot_disk_kms_key"] = boot_disk_kms_key
        if image_type is not None:
            self._values["image_type"] = image_type
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if service_account is not None:
            self._values["service_account"] = service_account

    @builtins.property
    def boot_disk_kms_key(self) -> typing.Optional[builtins.str]:
        '''The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        '''
        result = self._values.get("boot_disk_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The default image type used by NAP once a new node pool is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Scopes that are used by NAP when creating node pools.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Platform Service Account to be used by the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterClusterAutoscalingAutoProvisioningDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskKmsKey")
    def reset_boot_disk_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskKmsKey", []))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKeyInput")
    def boot_disk_kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskKmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskKmsKey"))

    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, "boot_disk_kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, "image_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterClusterAutoscalingAutoProvisioningDefaults]:
        return typing.cast(typing.Optional[ContainerClusterClusterAutoscalingAutoProvisioningDefaults], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterClusterAutoscalingAutoProvisioningDefaults],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterClusterAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoProvisioningDefaults")
    def put_auto_provisioning_defaults(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        image_type: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param image_type: The default image type used by NAP once a new node pool is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param oauth_scopes: Scopes that are used by NAP when creating node pools. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        '''
        value = ContainerClusterClusterAutoscalingAutoProvisioningDefaults(
            boot_disk_kms_key=boot_disk_kms_key,
            image_type=image_type,
            oauth_scopes=oauth_scopes,
            service_account=service_account,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoProvisioningDefaults", [value]))

    @jsii.member(jsii_name="putResourceLimits")
    def put_resource_limits(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterClusterAutoscalingResourceLimits", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingOutputReference.put_resource_limits)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceLimits", [value]))

    @jsii.member(jsii_name="resetAutoProvisioningDefaults")
    def reset_auto_provisioning_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoProvisioningDefaults", []))

    @jsii.member(jsii_name="resetResourceLimits")
    def reset_resource_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLimits", []))

    @builtins.property
    @jsii.member(jsii_name="autoProvisioningDefaults")
    def auto_provisioning_defaults(
        self,
    ) -> ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference:
        return typing.cast(ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference, jsii.get(self, "autoProvisioningDefaults"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimits")
    def resource_limits(self) -> "ContainerClusterClusterAutoscalingResourceLimitsList":
        return typing.cast("ContainerClusterClusterAutoscalingResourceLimitsList", jsii.get(self, "resourceLimits"))

    @builtins.property
    @jsii.member(jsii_name="autoProvisioningDefaultsInput")
    def auto_provisioning_defaults_input(
        self,
    ) -> typing.Optional[ContainerClusterClusterAutoscalingAutoProvisioningDefaults]:
        return typing.cast(typing.Optional[ContainerClusterClusterAutoscalingAutoProvisioningDefaults], jsii.get(self, "autoProvisioningDefaultsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimitsInput")
    def resource_limits_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterClusterAutoscalingResourceLimits"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterClusterAutoscalingResourceLimits"]]], jsii.get(self, "resourceLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterClusterAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterClusterAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterClusterAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingResourceLimits",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "maximum": "maximum",
        "minimum": "minimum",
    },
)
class ContainerClusterClusterAutoscalingResourceLimits:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        maximum: typing.Optional[jsii.Number] = None,
        minimum: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param resource_type: The type of the resource. For example, cpu and memory. See the guide to using Node Auto-Provisioning for a list of types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_type ContainerCluster#resource_type}
        :param maximum: Maximum amount of the resource in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maximum ContainerCluster#maximum}
        :param minimum: Minimum amount of the resource in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#minimum ContainerCluster#minimum}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingResourceLimits.__init__)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_type": resource_type,
        }
        if maximum is not None:
            self._values["maximum"] = maximum
        if minimum is not None:
            self._values["minimum"] = minimum

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The type of the resource.

        For example, cpu and memory. See the guide to using Node Auto-Provisioning for a list of types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_type ContainerCluster#resource_type}
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maximum(self) -> typing.Optional[jsii.Number]:
        '''Maximum amount of the resource in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maximum ContainerCluster#maximum}
        '''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum(self) -> typing.Optional[jsii.Number]:
        '''Minimum amount of the resource in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#minimum ContainerCluster#minimum}
        '''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterClusterAutoscalingResourceLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterClusterAutoscalingResourceLimitsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingResourceLimitsList",
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
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingResourceLimitsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterClusterAutoscalingResourceLimitsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingResourceLimitsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterClusterAutoscalingResourceLimitsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterClusterAutoscalingResourceLimits]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterClusterAutoscalingResourceLimits]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterClusterAutoscalingResourceLimits]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterClusterAutoscalingResourceLimitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterClusterAutoscalingResourceLimitsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterClusterAutoscalingResourceLimitsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsOutputReference, "resource_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterClusterAutoscalingResourceLimits, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterClusterAutoscalingResourceLimits, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterClusterAutoscalingResourceLimits, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterClusterAutoscalingResourceLimitsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterConfidentialNodes",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterConfidentialNodes:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether Confidential Nodes feature is enabled for all nodes in this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterConfidentialNodes.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether Confidential Nodes feature is enabled for all nodes in this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterConfidentialNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterConfidentialNodesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterConfidentialNodesOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterConfidentialNodesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterConfidentialNodesOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterConfidentialNodes]:
        return typing.cast(typing.Optional[ContainerClusterConfidentialNodes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterConfidentialNodes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterConfidentialNodesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterConfig",
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
        "addons_config": "addonsConfig",
        "authenticator_groups_config": "authenticatorGroupsConfig",
        "binary_authorization": "binaryAuthorization",
        "cluster_autoscaling": "clusterAutoscaling",
        "cluster_ipv4_cidr": "clusterIpv4Cidr",
        "confidential_nodes": "confidentialNodes",
        "database_encryption": "databaseEncryption",
        "datapath_provider": "datapathProvider",
        "default_max_pods_per_node": "defaultMaxPodsPerNode",
        "default_snat_status": "defaultSnatStatus",
        "description": "description",
        "dns_config": "dnsConfig",
        "enable_autopilot": "enableAutopilot",
        "enable_binary_authorization": "enableBinaryAuthorization",
        "enable_intranode_visibility": "enableIntranodeVisibility",
        "enable_kubernetes_alpha": "enableKubernetesAlpha",
        "enable_legacy_abac": "enableLegacyAbac",
        "enable_shielded_nodes": "enableShieldedNodes",
        "enable_tpu": "enableTpu",
        "id": "id",
        "initial_node_count": "initialNodeCount",
        "ip_allocation_policy": "ipAllocationPolicy",
        "location": "location",
        "logging_config": "loggingConfig",
        "logging_service": "loggingService",
        "maintenance_policy": "maintenancePolicy",
        "master_auth": "masterAuth",
        "master_authorized_networks_config": "masterAuthorizedNetworksConfig",
        "mesh_certificates": "meshCertificates",
        "min_master_version": "minMasterVersion",
        "monitoring_config": "monitoringConfig",
        "monitoring_service": "monitoringService",
        "network": "network",
        "networking_mode": "networkingMode",
        "network_policy": "networkPolicy",
        "node_config": "nodeConfig",
        "node_locations": "nodeLocations",
        "node_pool": "nodePool",
        "node_version": "nodeVersion",
        "notification_config": "notificationConfig",
        "private_cluster_config": "privateClusterConfig",
        "private_ipv6_google_access": "privateIpv6GoogleAccess",
        "project": "project",
        "release_channel": "releaseChannel",
        "remove_default_node_pool": "removeDefaultNodePool",
        "resource_labels": "resourceLabels",
        "resource_usage_export_config": "resourceUsageExportConfig",
        "service_external_ips_config": "serviceExternalIpsConfig",
        "subnetwork": "subnetwork",
        "timeouts": "timeouts",
        "vertical_pod_autoscaling": "verticalPodAutoscaling",
        "workload_identity_config": "workloadIdentityConfig",
    },
)
class ContainerClusterConfig(cdktf.TerraformMetaArguments):
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
        addons_config: typing.Optional[typing.Union[ContainerClusterAddonsConfig, typing.Dict[str, typing.Any]]] = None,
        authenticator_groups_config: typing.Optional[typing.Union[ContainerClusterAuthenticatorGroupsConfig, typing.Dict[str, typing.Any]]] = None,
        binary_authorization: typing.Optional[typing.Union[ContainerClusterBinaryAuthorization, typing.Dict[str, typing.Any]]] = None,
        cluster_autoscaling: typing.Optional[typing.Union[ContainerClusterClusterAutoscaling, typing.Dict[str, typing.Any]]] = None,
        cluster_ipv4_cidr: typing.Optional[builtins.str] = None,
        confidential_nodes: typing.Optional[typing.Union[ContainerClusterConfidentialNodes, typing.Dict[str, typing.Any]]] = None,
        database_encryption: typing.Optional[typing.Union["ContainerClusterDatabaseEncryption", typing.Dict[str, typing.Any]]] = None,
        datapath_provider: typing.Optional[builtins.str] = None,
        default_max_pods_per_node: typing.Optional[jsii.Number] = None,
        default_snat_status: typing.Optional[typing.Union["ContainerClusterDefaultSnatStatus", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union["ContainerClusterDnsConfig", typing.Dict[str, typing.Any]]] = None,
        enable_autopilot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_binary_authorization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_intranode_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_kubernetes_alpha: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_legacy_abac: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_shielded_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_tpu: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_node_count: typing.Optional[jsii.Number] = None,
        ip_allocation_policy: typing.Optional[typing.Union["ContainerClusterIpAllocationPolicy", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["ContainerClusterLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        logging_service: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["ContainerClusterMaintenancePolicy", typing.Dict[str, typing.Any]]] = None,
        master_auth: typing.Optional[typing.Union["ContainerClusterMasterAuth", typing.Dict[str, typing.Any]]] = None,
        master_authorized_networks_config: typing.Optional[typing.Union["ContainerClusterMasterAuthorizedNetworksConfig", typing.Dict[str, typing.Any]]] = None,
        mesh_certificates: typing.Optional[typing.Union["ContainerClusterMeshCertificates", typing.Dict[str, typing.Any]]] = None,
        min_master_version: typing.Optional[builtins.str] = None,
        monitoring_config: typing.Optional[typing.Union["ContainerClusterMonitoringConfig", typing.Dict[str, typing.Any]]] = None,
        monitoring_service: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        networking_mode: typing.Optional[builtins.str] = None,
        network_policy: typing.Optional[typing.Union["ContainerClusterNetworkPolicy", typing.Dict[str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["ContainerClusterNodeConfig", typing.Dict[str, typing.Any]]] = None,
        node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_pool: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePool", typing.Dict[str, typing.Any]]]]] = None,
        node_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["ContainerClusterNotificationConfig", typing.Dict[str, typing.Any]]] = None,
        private_cluster_config: typing.Optional[typing.Union["ContainerClusterPrivateClusterConfig", typing.Dict[str, typing.Any]]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        release_channel: typing.Optional[typing.Union["ContainerClusterReleaseChannel", typing.Dict[str, typing.Any]]] = None,
        remove_default_node_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        resource_usage_export_config: typing.Optional[typing.Union["ContainerClusterResourceUsageExportConfig", typing.Dict[str, typing.Any]]] = None,
        service_external_ips_config: typing.Optional[typing.Union["ContainerClusterServiceExternalIpsConfig", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ContainerClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        vertical_pod_autoscaling: typing.Optional[typing.Union["ContainerClusterVerticalPodAutoscaling", typing.Dict[str, typing.Any]]] = None,
        workload_identity_config: typing.Optional[typing.Union["ContainerClusterWorkloadIdentityConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the cluster, unique within the project and location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name ContainerCluster#name}
        :param addons_config: addons_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#addons_config ContainerCluster#addons_config}
        :param authenticator_groups_config: authenticator_groups_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#authenticator_groups_config ContainerCluster#authenticator_groups_config}
        :param binary_authorization: binary_authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#binary_authorization ContainerCluster#binary_authorization}
        :param cluster_autoscaling: cluster_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_autoscaling ContainerCluster#cluster_autoscaling}
        :param cluster_ipv4_cidr: The IP address range of the Kubernetes pods in this cluster in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8. This field will only work for routes-based clusters, where ip_allocation_policy is not defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr ContainerCluster#cluster_ipv4_cidr}
        :param confidential_nodes: confidential_nodes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#confidential_nodes ContainerCluster#confidential_nodes}
        :param database_encryption: database_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#database_encryption ContainerCluster#database_encryption}
        :param datapath_provider: The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#datapath_provider ContainerCluster#datapath_provider}
        :param default_max_pods_per_node: The default maximum number of pods per node in this cluster. This doesn't work on "routes-based" clusters, clusters that don't have IP Aliasing enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_max_pods_per_node ContainerCluster#default_max_pods_per_node}
        :param default_snat_status: default_snat_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_snat_status ContainerCluster#default_snat_status}
        :param description: Description of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#description ContainerCluster#description}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_config ContainerCluster#dns_config}
        :param enable_autopilot: Enable Autopilot for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_autopilot ContainerCluster#enable_autopilot}
        :param enable_binary_authorization: Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Google Binary Authorization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_binary_authorization ContainerCluster#enable_binary_authorization}
        :param enable_intranode_visibility: Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_intranode_visibility ContainerCluster#enable_intranode_visibility}
        :param enable_kubernetes_alpha: Whether to enable Kubernetes Alpha features for this cluster. Note that when this option is enabled, the cluster cannot be upgraded and will be automatically deleted after 30 days. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_kubernetes_alpha ContainerCluster#enable_kubernetes_alpha}
        :param enable_legacy_abac: Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_legacy_abac ContainerCluster#enable_legacy_abac}
        :param enable_shielded_nodes: Enable Shielded Nodes features on all nodes in this cluster. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_shielded_nodes ContainerCluster#enable_shielded_nodes}
        :param enable_tpu: Whether to enable Cloud TPU resources in this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_tpu ContainerCluster#enable_tpu}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#id ContainerCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_node_count: The number of nodes to create in this cluster's default node pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Must be set if node_pool is not set. If you're using google_container_node_pool objects with no default node pool, you'll need to set this to a value of at least 1, alongside setting remove_default_node_pool to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#initial_node_count ContainerCluster#initial_node_count}
        :param ip_allocation_policy: ip_allocation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#ip_allocation_policy ContainerCluster#ip_allocation_policy}
        :param location: The location (region or zone) in which the cluster master will be created, as well as the default node location. If you specify a zone (such as us-central1-a), the cluster will be a zonal cluster with a single cluster master. If you specify a region (such as us-west1), the cluster will be a regional cluster with multiple masters spread across zones in the region, and with default node locations in those zones as well. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#location ContainerCluster#location}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_config ContainerCluster#logging_config}
        :param logging_service: The logging service that the cluster should write logs to. Available options include logging.googleapis.com(Legacy Stackdriver), logging.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Logging), and none. Defaults to logging.googleapis.com/kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_service ContainerCluster#logging_service}
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_policy ContainerCluster#maintenance_policy}
        :param master_auth: master_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_auth ContainerCluster#master_auth}
        :param master_authorized_networks_config: master_authorized_networks_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_authorized_networks_config ContainerCluster#master_authorized_networks_config}
        :param mesh_certificates: mesh_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mesh_certificates ContainerCluster#mesh_certificates}
        :param min_master_version: The minimum version of the master. GKE will auto-update the master to new versions, so this does not guarantee the current master version--use the read-only master_version field to obtain that. If unset, the cluster's version will be set by GKE to the version of the most recent official release (which is not necessarily the latest version). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_master_version ContainerCluster#min_master_version}
        :param monitoring_config: monitoring_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_config ContainerCluster#monitoring_config}
        :param monitoring_service: The monitoring service that the cluster should write metrics to. Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API. VM metrics will be collected by Google Compute Engine regardless of this setting Available options include monitoring.googleapis.com(Legacy Stackdriver), monitoring.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Monitoring), and none. Defaults to monitoring.googleapis.com/kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_service ContainerCluster#monitoring_service}
        :param network: The name or self_link of the Google Compute Engine network to which the cluster is connected. For Shared VPC, set this to the self link of the shared network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network ContainerCluster#network}
        :param networking_mode: Determines whether alias IPs or routes will be used for pod IPs in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#networking_mode ContainerCluster#networking_mode}
        :param network_policy: network_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy ContainerCluster#network_policy}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_config ContainerCluster#node_config}
        :param node_locations: The list of zones in which the cluster's nodes are located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If this is specified for a zonal cluster, omit the cluster's zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_locations ContainerCluster#node_locations}
        :param node_pool: node_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_pool ContainerCluster#node_pool}
        :param node_version: The Kubernetes version on the nodes. Must either be unset or set to the same value as min_master_version on create. Defaults to the default version set by GKE which is not necessarily the latest version. This only affects nodes in the default node pool. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. To update nodes in other node pools, use the version attribute on the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_version ContainerCluster#node_version}
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#notification_config ContainerCluster#notification_config}
        :param private_cluster_config: private_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_cluster_config ContainerCluster#private_cluster_config}
        :param private_ipv6_google_access: The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_ipv6_google_access ContainerCluster#private_ipv6_google_access}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#project ContainerCluster#project}
        :param release_channel: release_channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#release_channel ContainerCluster#release_channel}
        :param remove_default_node_pool: If true, deletes the default node pool upon cluster creation. If you're using google_container_node_pool resources with no default node pool, this should be set to true, alongside setting initial_node_count to at least 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#remove_default_node_pool ContainerCluster#remove_default_node_pool}
        :param resource_labels: The GCE resource labels (a map of key/value pairs) to be applied to the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_labels ContainerCluster#resource_labels}
        :param resource_usage_export_config: resource_usage_export_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_usage_export_config ContainerCluster#resource_usage_export_config}
        :param service_external_ips_config: service_external_ips_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_external_ips_config ContainerCluster#service_external_ips_config}
        :param subnetwork: The name or self_link of the Google Compute Engine subnetwork in which the cluster's instances are launched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#subnetwork ContainerCluster#subnetwork}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#timeouts ContainerCluster#timeouts}
        :param vertical_pod_autoscaling: vertical_pod_autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#vertical_pod_autoscaling ContainerCluster#vertical_pod_autoscaling}
        :param workload_identity_config: workload_identity_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_identity_config ContainerCluster#workload_identity_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(addons_config, dict):
            addons_config = ContainerClusterAddonsConfig(**addons_config)
        if isinstance(authenticator_groups_config, dict):
            authenticator_groups_config = ContainerClusterAuthenticatorGroupsConfig(**authenticator_groups_config)
        if isinstance(binary_authorization, dict):
            binary_authorization = ContainerClusterBinaryAuthorization(**binary_authorization)
        if isinstance(cluster_autoscaling, dict):
            cluster_autoscaling = ContainerClusterClusterAutoscaling(**cluster_autoscaling)
        if isinstance(confidential_nodes, dict):
            confidential_nodes = ContainerClusterConfidentialNodes(**confidential_nodes)
        if isinstance(database_encryption, dict):
            database_encryption = ContainerClusterDatabaseEncryption(**database_encryption)
        if isinstance(default_snat_status, dict):
            default_snat_status = ContainerClusterDefaultSnatStatus(**default_snat_status)
        if isinstance(dns_config, dict):
            dns_config = ContainerClusterDnsConfig(**dns_config)
        if isinstance(ip_allocation_policy, dict):
            ip_allocation_policy = ContainerClusterIpAllocationPolicy(**ip_allocation_policy)
        if isinstance(logging_config, dict):
            logging_config = ContainerClusterLoggingConfig(**logging_config)
        if isinstance(maintenance_policy, dict):
            maintenance_policy = ContainerClusterMaintenancePolicy(**maintenance_policy)
        if isinstance(master_auth, dict):
            master_auth = ContainerClusterMasterAuth(**master_auth)
        if isinstance(master_authorized_networks_config, dict):
            master_authorized_networks_config = ContainerClusterMasterAuthorizedNetworksConfig(**master_authorized_networks_config)
        if isinstance(mesh_certificates, dict):
            mesh_certificates = ContainerClusterMeshCertificates(**mesh_certificates)
        if isinstance(monitoring_config, dict):
            monitoring_config = ContainerClusterMonitoringConfig(**monitoring_config)
        if isinstance(network_policy, dict):
            network_policy = ContainerClusterNetworkPolicy(**network_policy)
        if isinstance(node_config, dict):
            node_config = ContainerClusterNodeConfig(**node_config)
        if isinstance(notification_config, dict):
            notification_config = ContainerClusterNotificationConfig(**notification_config)
        if isinstance(private_cluster_config, dict):
            private_cluster_config = ContainerClusterPrivateClusterConfig(**private_cluster_config)
        if isinstance(release_channel, dict):
            release_channel = ContainerClusterReleaseChannel(**release_channel)
        if isinstance(resource_usage_export_config, dict):
            resource_usage_export_config = ContainerClusterResourceUsageExportConfig(**resource_usage_export_config)
        if isinstance(service_external_ips_config, dict):
            service_external_ips_config = ContainerClusterServiceExternalIpsConfig(**service_external_ips_config)
        if isinstance(timeouts, dict):
            timeouts = ContainerClusterTimeouts(**timeouts)
        if isinstance(vertical_pod_autoscaling, dict):
            vertical_pod_autoscaling = ContainerClusterVerticalPodAutoscaling(**vertical_pod_autoscaling)
        if isinstance(workload_identity_config, dict):
            workload_identity_config = ContainerClusterWorkloadIdentityConfig(**workload_identity_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument addons_config", value=addons_config, expected_type=type_hints["addons_config"])
            check_type(argname="argument authenticator_groups_config", value=authenticator_groups_config, expected_type=type_hints["authenticator_groups_config"])
            check_type(argname="argument binary_authorization", value=binary_authorization, expected_type=type_hints["binary_authorization"])
            check_type(argname="argument cluster_autoscaling", value=cluster_autoscaling, expected_type=type_hints["cluster_autoscaling"])
            check_type(argname="argument cluster_ipv4_cidr", value=cluster_ipv4_cidr, expected_type=type_hints["cluster_ipv4_cidr"])
            check_type(argname="argument confidential_nodes", value=confidential_nodes, expected_type=type_hints["confidential_nodes"])
            check_type(argname="argument database_encryption", value=database_encryption, expected_type=type_hints["database_encryption"])
            check_type(argname="argument datapath_provider", value=datapath_provider, expected_type=type_hints["datapath_provider"])
            check_type(argname="argument default_max_pods_per_node", value=default_max_pods_per_node, expected_type=type_hints["default_max_pods_per_node"])
            check_type(argname="argument default_snat_status", value=default_snat_status, expected_type=type_hints["default_snat_status"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dns_config", value=dns_config, expected_type=type_hints["dns_config"])
            check_type(argname="argument enable_autopilot", value=enable_autopilot, expected_type=type_hints["enable_autopilot"])
            check_type(argname="argument enable_binary_authorization", value=enable_binary_authorization, expected_type=type_hints["enable_binary_authorization"])
            check_type(argname="argument enable_intranode_visibility", value=enable_intranode_visibility, expected_type=type_hints["enable_intranode_visibility"])
            check_type(argname="argument enable_kubernetes_alpha", value=enable_kubernetes_alpha, expected_type=type_hints["enable_kubernetes_alpha"])
            check_type(argname="argument enable_legacy_abac", value=enable_legacy_abac, expected_type=type_hints["enable_legacy_abac"])
            check_type(argname="argument enable_shielded_nodes", value=enable_shielded_nodes, expected_type=type_hints["enable_shielded_nodes"])
            check_type(argname="argument enable_tpu", value=enable_tpu, expected_type=type_hints["enable_tpu"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_node_count", value=initial_node_count, expected_type=type_hints["initial_node_count"])
            check_type(argname="argument ip_allocation_policy", value=ip_allocation_policy, expected_type=type_hints["ip_allocation_policy"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument logging_service", value=logging_service, expected_type=type_hints["logging_service"])
            check_type(argname="argument maintenance_policy", value=maintenance_policy, expected_type=type_hints["maintenance_policy"])
            check_type(argname="argument master_auth", value=master_auth, expected_type=type_hints["master_auth"])
            check_type(argname="argument master_authorized_networks_config", value=master_authorized_networks_config, expected_type=type_hints["master_authorized_networks_config"])
            check_type(argname="argument mesh_certificates", value=mesh_certificates, expected_type=type_hints["mesh_certificates"])
            check_type(argname="argument min_master_version", value=min_master_version, expected_type=type_hints["min_master_version"])
            check_type(argname="argument monitoring_config", value=monitoring_config, expected_type=type_hints["monitoring_config"])
            check_type(argname="argument monitoring_service", value=monitoring_service, expected_type=type_hints["monitoring_service"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument networking_mode", value=networking_mode, expected_type=type_hints["networking_mode"])
            check_type(argname="argument network_policy", value=network_policy, expected_type=type_hints["network_policy"])
            check_type(argname="argument node_config", value=node_config, expected_type=type_hints["node_config"])
            check_type(argname="argument node_locations", value=node_locations, expected_type=type_hints["node_locations"])
            check_type(argname="argument node_pool", value=node_pool, expected_type=type_hints["node_pool"])
            check_type(argname="argument node_version", value=node_version, expected_type=type_hints["node_version"])
            check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
            check_type(argname="argument private_cluster_config", value=private_cluster_config, expected_type=type_hints["private_cluster_config"])
            check_type(argname="argument private_ipv6_google_access", value=private_ipv6_google_access, expected_type=type_hints["private_ipv6_google_access"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument release_channel", value=release_channel, expected_type=type_hints["release_channel"])
            check_type(argname="argument remove_default_node_pool", value=remove_default_node_pool, expected_type=type_hints["remove_default_node_pool"])
            check_type(argname="argument resource_labels", value=resource_labels, expected_type=type_hints["resource_labels"])
            check_type(argname="argument resource_usage_export_config", value=resource_usage_export_config, expected_type=type_hints["resource_usage_export_config"])
            check_type(argname="argument service_external_ips_config", value=service_external_ips_config, expected_type=type_hints["service_external_ips_config"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vertical_pod_autoscaling", value=vertical_pod_autoscaling, expected_type=type_hints["vertical_pod_autoscaling"])
            check_type(argname="argument workload_identity_config", value=workload_identity_config, expected_type=type_hints["workload_identity_config"])
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
        if addons_config is not None:
            self._values["addons_config"] = addons_config
        if authenticator_groups_config is not None:
            self._values["authenticator_groups_config"] = authenticator_groups_config
        if binary_authorization is not None:
            self._values["binary_authorization"] = binary_authorization
        if cluster_autoscaling is not None:
            self._values["cluster_autoscaling"] = cluster_autoscaling
        if cluster_ipv4_cidr is not None:
            self._values["cluster_ipv4_cidr"] = cluster_ipv4_cidr
        if confidential_nodes is not None:
            self._values["confidential_nodes"] = confidential_nodes
        if database_encryption is not None:
            self._values["database_encryption"] = database_encryption
        if datapath_provider is not None:
            self._values["datapath_provider"] = datapath_provider
        if default_max_pods_per_node is not None:
            self._values["default_max_pods_per_node"] = default_max_pods_per_node
        if default_snat_status is not None:
            self._values["default_snat_status"] = default_snat_status
        if description is not None:
            self._values["description"] = description
        if dns_config is not None:
            self._values["dns_config"] = dns_config
        if enable_autopilot is not None:
            self._values["enable_autopilot"] = enable_autopilot
        if enable_binary_authorization is not None:
            self._values["enable_binary_authorization"] = enable_binary_authorization
        if enable_intranode_visibility is not None:
            self._values["enable_intranode_visibility"] = enable_intranode_visibility
        if enable_kubernetes_alpha is not None:
            self._values["enable_kubernetes_alpha"] = enable_kubernetes_alpha
        if enable_legacy_abac is not None:
            self._values["enable_legacy_abac"] = enable_legacy_abac
        if enable_shielded_nodes is not None:
            self._values["enable_shielded_nodes"] = enable_shielded_nodes
        if enable_tpu is not None:
            self._values["enable_tpu"] = enable_tpu
        if id is not None:
            self._values["id"] = id
        if initial_node_count is not None:
            self._values["initial_node_count"] = initial_node_count
        if ip_allocation_policy is not None:
            self._values["ip_allocation_policy"] = ip_allocation_policy
        if location is not None:
            self._values["location"] = location
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if logging_service is not None:
            self._values["logging_service"] = logging_service
        if maintenance_policy is not None:
            self._values["maintenance_policy"] = maintenance_policy
        if master_auth is not None:
            self._values["master_auth"] = master_auth
        if master_authorized_networks_config is not None:
            self._values["master_authorized_networks_config"] = master_authorized_networks_config
        if mesh_certificates is not None:
            self._values["mesh_certificates"] = mesh_certificates
        if min_master_version is not None:
            self._values["min_master_version"] = min_master_version
        if monitoring_config is not None:
            self._values["monitoring_config"] = monitoring_config
        if monitoring_service is not None:
            self._values["monitoring_service"] = monitoring_service
        if network is not None:
            self._values["network"] = network
        if networking_mode is not None:
            self._values["networking_mode"] = networking_mode
        if network_policy is not None:
            self._values["network_policy"] = network_policy
        if node_config is not None:
            self._values["node_config"] = node_config
        if node_locations is not None:
            self._values["node_locations"] = node_locations
        if node_pool is not None:
            self._values["node_pool"] = node_pool
        if node_version is not None:
            self._values["node_version"] = node_version
        if notification_config is not None:
            self._values["notification_config"] = notification_config
        if private_cluster_config is not None:
            self._values["private_cluster_config"] = private_cluster_config
        if private_ipv6_google_access is not None:
            self._values["private_ipv6_google_access"] = private_ipv6_google_access
        if project is not None:
            self._values["project"] = project
        if release_channel is not None:
            self._values["release_channel"] = release_channel
        if remove_default_node_pool is not None:
            self._values["remove_default_node_pool"] = remove_default_node_pool
        if resource_labels is not None:
            self._values["resource_labels"] = resource_labels
        if resource_usage_export_config is not None:
            self._values["resource_usage_export_config"] = resource_usage_export_config
        if service_external_ips_config is not None:
            self._values["service_external_ips_config"] = service_external_ips_config
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vertical_pod_autoscaling is not None:
            self._values["vertical_pod_autoscaling"] = vertical_pod_autoscaling
        if workload_identity_config is not None:
            self._values["workload_identity_config"] = workload_identity_config

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
        '''The name of the cluster, unique within the project and location.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name ContainerCluster#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addons_config(self) -> typing.Optional[ContainerClusterAddonsConfig]:
        '''addons_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#addons_config ContainerCluster#addons_config}
        '''
        result = self._values.get("addons_config")
        return typing.cast(typing.Optional[ContainerClusterAddonsConfig], result)

    @builtins.property
    def authenticator_groups_config(
        self,
    ) -> typing.Optional[ContainerClusterAuthenticatorGroupsConfig]:
        '''authenticator_groups_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#authenticator_groups_config ContainerCluster#authenticator_groups_config}
        '''
        result = self._values.get("authenticator_groups_config")
        return typing.cast(typing.Optional[ContainerClusterAuthenticatorGroupsConfig], result)

    @builtins.property
    def binary_authorization(
        self,
    ) -> typing.Optional[ContainerClusterBinaryAuthorization]:
        '''binary_authorization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#binary_authorization ContainerCluster#binary_authorization}
        '''
        result = self._values.get("binary_authorization")
        return typing.cast(typing.Optional[ContainerClusterBinaryAuthorization], result)

    @builtins.property
    def cluster_autoscaling(
        self,
    ) -> typing.Optional[ContainerClusterClusterAutoscaling]:
        '''cluster_autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_autoscaling ContainerCluster#cluster_autoscaling}
        '''
        result = self._values.get("cluster_autoscaling")
        return typing.cast(typing.Optional[ContainerClusterClusterAutoscaling], result)

    @builtins.property
    def cluster_ipv4_cidr(self) -> typing.Optional[builtins.str]:
        '''The IP address range of the Kubernetes pods in this cluster in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8. This field will only work for routes-based clusters, where ip_allocation_policy is not defined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr ContainerCluster#cluster_ipv4_cidr}
        '''
        result = self._values.get("cluster_ipv4_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def confidential_nodes(self) -> typing.Optional[ContainerClusterConfidentialNodes]:
        '''confidential_nodes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#confidential_nodes ContainerCluster#confidential_nodes}
        '''
        result = self._values.get("confidential_nodes")
        return typing.cast(typing.Optional[ContainerClusterConfidentialNodes], result)

    @builtins.property
    def database_encryption(
        self,
    ) -> typing.Optional["ContainerClusterDatabaseEncryption"]:
        '''database_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#database_encryption ContainerCluster#database_encryption}
        '''
        result = self._values.get("database_encryption")
        return typing.cast(typing.Optional["ContainerClusterDatabaseEncryption"], result)

    @builtins.property
    def datapath_provider(self) -> typing.Optional[builtins.str]:
        '''The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#datapath_provider ContainerCluster#datapath_provider}
        '''
        result = self._values.get("datapath_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_max_pods_per_node(self) -> typing.Optional[jsii.Number]:
        '''The default maximum number of pods per node in this cluster.

        This doesn't work on "routes-based" clusters, clusters that don't have IP Aliasing enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_max_pods_per_node ContainerCluster#default_max_pods_per_node}
        '''
        result = self._values.get("default_max_pods_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_snat_status(
        self,
    ) -> typing.Optional["ContainerClusterDefaultSnatStatus"]:
        '''default_snat_status block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#default_snat_status ContainerCluster#default_snat_status}
        '''
        result = self._values.get("default_snat_status")
        return typing.cast(typing.Optional["ContainerClusterDefaultSnatStatus"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#description ContainerCluster#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_config(self) -> typing.Optional["ContainerClusterDnsConfig"]:
        '''dns_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dns_config ContainerCluster#dns_config}
        '''
        result = self._values.get("dns_config")
        return typing.cast(typing.Optional["ContainerClusterDnsConfig"], result)

    @builtins.property
    def enable_autopilot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Autopilot for this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_autopilot ContainerCluster#enable_autopilot}
        '''
        result = self._values.get("enable_autopilot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_binary_authorization(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Google Binary Authorization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_binary_authorization ContainerCluster#enable_binary_authorization}
        '''
        result = self._values.get("enable_binary_authorization")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_intranode_visibility(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether Intra-node visibility is enabled for this cluster.

        This makes same node pod to pod traffic visible for VPC network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_intranode_visibility ContainerCluster#enable_intranode_visibility}
        '''
        result = self._values.get("enable_intranode_visibility")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_kubernetes_alpha(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable Kubernetes Alpha features for this cluster.

        Note that when this option is enabled, the cluster cannot be upgraded and will be automatically deleted after 30 days.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_kubernetes_alpha ContainerCluster#enable_kubernetes_alpha}
        '''
        result = self._values.get("enable_kubernetes_alpha")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_legacy_abac(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the ABAC authorizer is enabled for this cluster.

        When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_legacy_abac ContainerCluster#enable_legacy_abac}
        '''
        result = self._values.get("enable_legacy_abac")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_shielded_nodes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Shielded Nodes features on all nodes in this cluster. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_shielded_nodes ContainerCluster#enable_shielded_nodes}
        '''
        result = self._values.get("enable_shielded_nodes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_tpu(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable Cloud TPU resources in this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_tpu ContainerCluster#enable_tpu}
        '''
        result = self._values.get("enable_tpu")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#id ContainerCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_node_count(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes to create in this cluster's default node pool.

        In regional or multi-zonal clusters, this is the number of nodes per zone. Must be set if node_pool is not set. If you're using google_container_node_pool objects with no default node pool, you'll need to set this to a value of at least 1, alongside setting remove_default_node_pool to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#initial_node_count ContainerCluster#initial_node_count}
        '''
        result = self._values.get("initial_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip_allocation_policy(
        self,
    ) -> typing.Optional["ContainerClusterIpAllocationPolicy"]:
        '''ip_allocation_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#ip_allocation_policy ContainerCluster#ip_allocation_policy}
        '''
        result = self._values.get("ip_allocation_policy")
        return typing.cast(typing.Optional["ContainerClusterIpAllocationPolicy"], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The location (region or zone) in which the cluster master will be created, as well as the default node location.

        If you specify a zone (such as us-central1-a), the cluster will be a zonal cluster with a single cluster master. If you specify a region (such as us-west1), the cluster will be a regional cluster with multiple masters spread across zones in the region, and with default node locations in those zones as well.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#location ContainerCluster#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(self) -> typing.Optional["ContainerClusterLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_config ContainerCluster#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["ContainerClusterLoggingConfig"], result)

    @builtins.property
    def logging_service(self) -> typing.Optional[builtins.str]:
        '''The logging service that the cluster should write logs to.

        Available options include logging.googleapis.com(Legacy Stackdriver), logging.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Logging), and none. Defaults to logging.googleapis.com/kubernetes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#logging_service ContainerCluster#logging_service}
        '''
        result = self._values.get("logging_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_policy(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicy"]:
        '''maintenance_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_policy ContainerCluster#maintenance_policy}
        '''
        result = self._values.get("maintenance_policy")
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicy"], result)

    @builtins.property
    def master_auth(self) -> typing.Optional["ContainerClusterMasterAuth"]:
        '''master_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_auth ContainerCluster#master_auth}
        '''
        result = self._values.get("master_auth")
        return typing.cast(typing.Optional["ContainerClusterMasterAuth"], result)

    @builtins.property
    def master_authorized_networks_config(
        self,
    ) -> typing.Optional["ContainerClusterMasterAuthorizedNetworksConfig"]:
        '''master_authorized_networks_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_authorized_networks_config ContainerCluster#master_authorized_networks_config}
        '''
        result = self._values.get("master_authorized_networks_config")
        return typing.cast(typing.Optional["ContainerClusterMasterAuthorizedNetworksConfig"], result)

    @builtins.property
    def mesh_certificates(self) -> typing.Optional["ContainerClusterMeshCertificates"]:
        '''mesh_certificates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mesh_certificates ContainerCluster#mesh_certificates}
        '''
        result = self._values.get("mesh_certificates")
        return typing.cast(typing.Optional["ContainerClusterMeshCertificates"], result)

    @builtins.property
    def min_master_version(self) -> typing.Optional[builtins.str]:
        '''The minimum version of the master.

        GKE will auto-update the master to new versions, so this does not guarantee the current master version--use the read-only master_version field to obtain that. If unset, the cluster's version will be set by GKE to the version of the most recent official release (which is not necessarily the latest version).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_master_version ContainerCluster#min_master_version}
        '''
        result = self._values.get("min_master_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitoring_config(self) -> typing.Optional["ContainerClusterMonitoringConfig"]:
        '''monitoring_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_config ContainerCluster#monitoring_config}
        '''
        result = self._values.get("monitoring_config")
        return typing.cast(typing.Optional["ContainerClusterMonitoringConfig"], result)

    @builtins.property
    def monitoring_service(self) -> typing.Optional[builtins.str]:
        '''The monitoring service that the cluster should write metrics to.

        Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API. VM metrics will be collected by Google Compute Engine regardless of this setting Available options include monitoring.googleapis.com(Legacy Stackdriver), monitoring.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Monitoring), and none. Defaults to monitoring.googleapis.com/kubernetes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#monitoring_service ContainerCluster#monitoring_service}
        '''
        result = self._values.get("monitoring_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the Google Compute Engine network to which the cluster is connected.

        For Shared VPC, set this to the self link of the shared network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network ContainerCluster#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networking_mode(self) -> typing.Optional[builtins.str]:
        '''Determines whether alias IPs or routes will be used for pod IPs in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#networking_mode ContainerCluster#networking_mode}
        '''
        result = self._values.get("networking_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_policy(self) -> typing.Optional["ContainerClusterNetworkPolicy"]:
        '''network_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#network_policy ContainerCluster#network_policy}
        '''
        result = self._values.get("network_policy")
        return typing.cast(typing.Optional["ContainerClusterNetworkPolicy"], result)

    @builtins.property
    def node_config(self) -> typing.Optional["ContainerClusterNodeConfig"]:
        '''node_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_config ContainerCluster#node_config}
        '''
        result = self._values.get("node_config")
        return typing.cast(typing.Optional["ContainerClusterNodeConfig"], result)

    @builtins.property
    def node_locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of zones in which the cluster's nodes are located.

        Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If this is specified for a zonal cluster, omit the cluster's zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_locations ContainerCluster#node_locations}
        '''
        result = self._values.get("node_locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_pool(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePool"]]]:
        '''node_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_pool ContainerCluster#node_pool}
        '''
        result = self._values.get("node_pool")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePool"]]], result)

    @builtins.property
    def node_version(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes version on the nodes.

        Must either be unset or set to the same value as min_master_version on create. Defaults to the default version set by GKE which is not necessarily the latest version. This only affects nodes in the default node pool. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. To update nodes in other node pools, use the version attribute on the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_version ContainerCluster#node_version}
        '''
        result = self._values.get("node_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_config(
        self,
    ) -> typing.Optional["ContainerClusterNotificationConfig"]:
        '''notification_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#notification_config ContainerCluster#notification_config}
        '''
        result = self._values.get("notification_config")
        return typing.cast(typing.Optional["ContainerClusterNotificationConfig"], result)

    @builtins.property
    def private_cluster_config(
        self,
    ) -> typing.Optional["ContainerClusterPrivateClusterConfig"]:
        '''private_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_cluster_config ContainerCluster#private_cluster_config}
        '''
        result = self._values.get("private_cluster_config")
        return typing.cast(typing.Optional["ContainerClusterPrivateClusterConfig"], result)

    @builtins.property
    def private_ipv6_google_access(self) -> typing.Optional[builtins.str]:
        '''The desired state of IPv6 connectivity to Google Services.

        By default, no private IPv6 access to or from Google Services (all access will be via IPv4).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#private_ipv6_google_access ContainerCluster#private_ipv6_google_access}
        '''
        result = self._values.get("private_ipv6_google_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#project ContainerCluster#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_channel(self) -> typing.Optional["ContainerClusterReleaseChannel"]:
        '''release_channel block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#release_channel ContainerCluster#release_channel}
        '''
        result = self._values.get("release_channel")
        return typing.cast(typing.Optional["ContainerClusterReleaseChannel"], result)

    @builtins.property
    def remove_default_node_pool(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, deletes the default node pool upon cluster creation.

        If you're using google_container_node_pool resources with no default node pool, this should be set to true, alongside setting initial_node_count to at least 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#remove_default_node_pool ContainerCluster#remove_default_node_pool}
        '''
        result = self._values.get("remove_default_node_pool")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def resource_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_labels ContainerCluster#resource_labels}
        '''
        result = self._values.get("resource_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def resource_usage_export_config(
        self,
    ) -> typing.Optional["ContainerClusterResourceUsageExportConfig"]:
        '''resource_usage_export_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#resource_usage_export_config ContainerCluster#resource_usage_export_config}
        '''
        result = self._values.get("resource_usage_export_config")
        return typing.cast(typing.Optional["ContainerClusterResourceUsageExportConfig"], result)

    @builtins.property
    def service_external_ips_config(
        self,
    ) -> typing.Optional["ContainerClusterServiceExternalIpsConfig"]:
        '''service_external_ips_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_external_ips_config ContainerCluster#service_external_ips_config}
        '''
        result = self._values.get("service_external_ips_config")
        return typing.cast(typing.Optional["ContainerClusterServiceExternalIpsConfig"], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the Google Compute Engine subnetwork in which the cluster's instances are launched.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#subnetwork ContainerCluster#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ContainerClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#timeouts ContainerCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ContainerClusterTimeouts"], result)

    @builtins.property
    def vertical_pod_autoscaling(
        self,
    ) -> typing.Optional["ContainerClusterVerticalPodAutoscaling"]:
        '''vertical_pod_autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#vertical_pod_autoscaling ContainerCluster#vertical_pod_autoscaling}
        '''
        result = self._values.get("vertical_pod_autoscaling")
        return typing.cast(typing.Optional["ContainerClusterVerticalPodAutoscaling"], result)

    @builtins.property
    def workload_identity_config(
        self,
    ) -> typing.Optional["ContainerClusterWorkloadIdentityConfig"]:
        '''workload_identity_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_identity_config ContainerCluster#workload_identity_config}
        '''
        result = self._values.get("workload_identity_config")
        return typing.cast(typing.Optional["ContainerClusterWorkloadIdentityConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDatabaseEncryption",
    jsii_struct_bases=[],
    name_mapping={"state": "state", "key_name": "keyName"},
)
class ContainerClusterDatabaseEncryption:
    def __init__(
        self,
        *,
        state: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param state: ENCRYPTED or DECRYPTED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#state ContainerCluster#state}
        :param key_name: The key to use to encrypt/decrypt secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key_name ContainerCluster#key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterDatabaseEncryption.__init__)
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "state": state,
        }
        if key_name is not None:
            self._values["key_name"] = key_name

    @builtins.property
    def state(self) -> builtins.str:
        '''ENCRYPTED or DECRYPTED.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#state ContainerCluster#state}
        '''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''The key to use to encrypt/decrypt secrets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key_name ContainerCluster#key_name}
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterDatabaseEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterDatabaseEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDatabaseEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterDatabaseEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDatabaseEncryptionOutputReference, "key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDatabaseEncryptionOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterDatabaseEncryption]:
        return typing.cast(typing.Optional[ContainerClusterDatabaseEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterDatabaseEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDatabaseEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDefaultSnatStatus",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled"},
)
class ContainerClusterDefaultSnatStatus:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disabled: When disabled is set to false, default IP masquerade rules will be applied to the nodes to prevent sNAT on cluster internal traffic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterDefaultSnatStatus.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When disabled is set to false, default IP masquerade rules will be applied to the nodes to prevent sNAT on cluster internal traffic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disabled ContainerCluster#disabled}
        '''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterDefaultSnatStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterDefaultSnatStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDefaultSnatStatusOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterDefaultSnatStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDefaultSnatStatusOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterDefaultSnatStatus]:
        return typing.cast(typing.Optional[ContainerClusterDefaultSnatStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterDefaultSnatStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDefaultSnatStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDnsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_dns": "clusterDns",
        "cluster_dns_domain": "clusterDnsDomain",
        "cluster_dns_scope": "clusterDnsScope",
    },
)
class ContainerClusterDnsConfig:
    def __init__(
        self,
        *,
        cluster_dns: typing.Optional[builtins.str] = None,
        cluster_dns_domain: typing.Optional[builtins.str] = None,
        cluster_dns_scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_dns: Which in-cluster DNS provider should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns ContainerCluster#cluster_dns}
        :param cluster_dns_domain: The suffix used for all cluster service records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_domain ContainerCluster#cluster_dns_domain}
        :param cluster_dns_scope: The scope of access to cluster DNS records. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_scope ContainerCluster#cluster_dns_scope}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterDnsConfig.__init__)
            check_type(argname="argument cluster_dns", value=cluster_dns, expected_type=type_hints["cluster_dns"])
            check_type(argname="argument cluster_dns_domain", value=cluster_dns_domain, expected_type=type_hints["cluster_dns_domain"])
            check_type(argname="argument cluster_dns_scope", value=cluster_dns_scope, expected_type=type_hints["cluster_dns_scope"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_dns is not None:
            self._values["cluster_dns"] = cluster_dns
        if cluster_dns_domain is not None:
            self._values["cluster_dns_domain"] = cluster_dns_domain
        if cluster_dns_scope is not None:
            self._values["cluster_dns_scope"] = cluster_dns_scope

    @builtins.property
    def cluster_dns(self) -> typing.Optional[builtins.str]:
        '''Which in-cluster DNS provider should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns ContainerCluster#cluster_dns}
        '''
        result = self._values.get("cluster_dns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_dns_domain(self) -> typing.Optional[builtins.str]:
        '''The suffix used for all cluster service records.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_domain ContainerCluster#cluster_dns_domain}
        '''
        result = self._values.get("cluster_dns_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_dns_scope(self) -> typing.Optional[builtins.str]:
        '''The scope of access to cluster DNS records.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_dns_scope ContainerCluster#cluster_dns_scope}
        '''
        result = self._values.get("cluster_dns_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterDnsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterDnsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterDnsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterDnsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClusterDns")
    def reset_cluster_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterDns", []))

    @jsii.member(jsii_name="resetClusterDnsDomain")
    def reset_cluster_dns_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterDnsDomain", []))

    @jsii.member(jsii_name="resetClusterDnsScope")
    def reset_cluster_dns_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterDnsScope", []))

    @builtins.property
    @jsii.member(jsii_name="clusterDnsDomainInput")
    def cluster_dns_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterDnsDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterDnsInput")
    def cluster_dns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterDnsScopeInput")
    def cluster_dns_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterDnsScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterDns")
    def cluster_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterDns"))

    @cluster_dns.setter
    def cluster_dns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDnsConfigOutputReference, "cluster_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterDns", value)

    @builtins.property
    @jsii.member(jsii_name="clusterDnsDomain")
    def cluster_dns_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterDnsDomain"))

    @cluster_dns_domain.setter
    def cluster_dns_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDnsConfigOutputReference, "cluster_dns_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterDnsDomain", value)

    @builtins.property
    @jsii.member(jsii_name="clusterDnsScope")
    def cluster_dns_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterDnsScope"))

    @cluster_dns_scope.setter
    def cluster_dns_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDnsConfigOutputReference, "cluster_dns_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterDnsScope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterDnsConfig]:
        return typing.cast(typing.Optional[ContainerClusterDnsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerClusterDnsConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterDnsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterIpAllocationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_ipv4_cidr_block": "clusterIpv4CidrBlock",
        "cluster_secondary_range_name": "clusterSecondaryRangeName",
        "services_ipv4_cidr_block": "servicesIpv4CidrBlock",
        "services_secondary_range_name": "servicesSecondaryRangeName",
    },
)
class ContainerClusterIpAllocationPolicy:
    def __init__(
        self,
        *,
        cluster_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        cluster_secondary_range_name: typing.Optional[builtins.str] = None,
        services_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        services_secondary_range_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_ipv4_cidr_block: The IP address range for the cluster pod IPs. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr_block ContainerCluster#cluster_ipv4_cidr_block}
        :param cluster_secondary_range_name: The name of the existing secondary range in the cluster's subnetwork to use for pod IP addresses. Alternatively, cluster_ipv4_cidr_block can be used to automatically create a GKE-managed one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_secondary_range_name ContainerCluster#cluster_secondary_range_name}
        :param services_ipv4_cidr_block: The IP address range of the services IPs in this cluster. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_ipv4_cidr_block ContainerCluster#services_ipv4_cidr_block}
        :param services_secondary_range_name: The name of the existing secondary range in the cluster's subnetwork to use for service ClusterIPs. Alternatively, services_ipv4_cidr_block can be used to automatically create a GKE-managed one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_secondary_range_name ContainerCluster#services_secondary_range_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterIpAllocationPolicy.__init__)
            check_type(argname="argument cluster_ipv4_cidr_block", value=cluster_ipv4_cidr_block, expected_type=type_hints["cluster_ipv4_cidr_block"])
            check_type(argname="argument cluster_secondary_range_name", value=cluster_secondary_range_name, expected_type=type_hints["cluster_secondary_range_name"])
            check_type(argname="argument services_ipv4_cidr_block", value=services_ipv4_cidr_block, expected_type=type_hints["services_ipv4_cidr_block"])
            check_type(argname="argument services_secondary_range_name", value=services_secondary_range_name, expected_type=type_hints["services_secondary_range_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_ipv4_cidr_block is not None:
            self._values["cluster_ipv4_cidr_block"] = cluster_ipv4_cidr_block
        if cluster_secondary_range_name is not None:
            self._values["cluster_secondary_range_name"] = cluster_secondary_range_name
        if services_ipv4_cidr_block is not None:
            self._values["services_ipv4_cidr_block"] = services_ipv4_cidr_block
        if services_secondary_range_name is not None:
            self._values["services_secondary_range_name"] = services_secondary_range_name

    @builtins.property
    def cluster_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The IP address range for the cluster pod IPs.

        Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_ipv4_cidr_block ContainerCluster#cluster_ipv4_cidr_block}
        '''
        result = self._values.get("cluster_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_secondary_range_name(self) -> typing.Optional[builtins.str]:
        '''The name of the existing secondary range in the cluster's subnetwork to use for pod IP addresses.

        Alternatively, cluster_ipv4_cidr_block can be used to automatically create a GKE-managed one.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cluster_secondary_range_name ContainerCluster#cluster_secondary_range_name}
        '''
        result = self._values.get("cluster_secondary_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def services_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The IP address range of the services IPs in this cluster.

        Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_ipv4_cidr_block ContainerCluster#services_ipv4_cidr_block}
        '''
        result = self._values.get("services_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def services_secondary_range_name(self) -> typing.Optional[builtins.str]:
        '''The name of the existing secondary range in the cluster's subnetwork to use for service ClusterIPs.

        Alternatively, services_ipv4_cidr_block can be used to automatically create a GKE-managed one.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#services_secondary_range_name ContainerCluster#services_secondary_range_name}
        '''
        result = self._values.get("services_secondary_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterIpAllocationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterIpAllocationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterIpAllocationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterIpAllocationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIpv4CidrBlock"))

    @cluster_ipv4_cidr_block.setter
    def cluster_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterIpAllocationPolicyOutputReference, "cluster_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSecondaryRangeName"))

    @cluster_secondary_range_name.setter
    def cluster_secondary_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterIpAllocationPolicyOutputReference, "cluster_secondary_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecondaryRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicesIpv4CidrBlock"))

    @services_ipv4_cidr_block.setter
    def services_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterIpAllocationPolicyOutputReference, "services_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicesIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicesSecondaryRangeName"))

    @services_secondary_range_name.setter
    def services_secondary_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterIpAllocationPolicyOutputReference, "services_secondary_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicesSecondaryRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterIpAllocationPolicy]:
        return typing.cast(typing.Optional[ContainerClusterIpAllocationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterIpAllocationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterIpAllocationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_components": "enableComponents"},
)
class ContainerClusterLoggingConfig:
    def __init__(self, *, enable_components: typing.Sequence[builtins.str]) -> None:
        '''
        :param enable_components: GKE components exposing logs. Valid values include SYSTEM_COMPONENTS and WORKLOADS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterLoggingConfig.__init__)
            check_type(argname="argument enable_components", value=enable_components, expected_type=type_hints["enable_components"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_components": enable_components,
        }

    @builtins.property
    def enable_components(self) -> typing.List[builtins.str]:
        '''GKE components exposing logs. Valid values include SYSTEM_COMPONENTS and WORKLOADS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        result = self._values.get("enable_components")
        assert result is not None, "Required property 'enable_components' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableComponentsInput")
    def enable_components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enableComponentsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableComponents")
    def enable_components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enableComponents"))

    @enable_components.setter
    def enable_components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterLoggingConfigOutputReference, "enable_components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableComponents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterLoggingConfig]:
        return typing.cast(typing.Optional[ContainerClusterLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "daily_maintenance_window": "dailyMaintenanceWindow",
        "maintenance_exclusion": "maintenanceExclusion",
        "recurring_window": "recurringWindow",
    },
)
class ContainerClusterMaintenancePolicy:
    def __init__(
        self,
        *,
        daily_maintenance_window: typing.Optional[typing.Union["ContainerClusterMaintenancePolicyDailyMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        maintenance_exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterMaintenancePolicyMaintenanceExclusion", typing.Dict[str, typing.Any]]]]] = None,
        recurring_window: typing.Optional[typing.Union["ContainerClusterMaintenancePolicyRecurringWindow", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param daily_maintenance_window: daily_maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#daily_maintenance_window ContainerCluster#daily_maintenance_window}
        :param maintenance_exclusion: maintenance_exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_exclusion ContainerCluster#maintenance_exclusion}
        :param recurring_window: recurring_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurring_window ContainerCluster#recurring_window}
        '''
        if isinstance(daily_maintenance_window, dict):
            daily_maintenance_window = ContainerClusterMaintenancePolicyDailyMaintenanceWindow(**daily_maintenance_window)
        if isinstance(recurring_window, dict):
            recurring_window = ContainerClusterMaintenancePolicyRecurringWindow(**recurring_window)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicy.__init__)
            check_type(argname="argument daily_maintenance_window", value=daily_maintenance_window, expected_type=type_hints["daily_maintenance_window"])
            check_type(argname="argument maintenance_exclusion", value=maintenance_exclusion, expected_type=type_hints["maintenance_exclusion"])
            check_type(argname="argument recurring_window", value=recurring_window, expected_type=type_hints["recurring_window"])
        self._values: typing.Dict[str, typing.Any] = {}
        if daily_maintenance_window is not None:
            self._values["daily_maintenance_window"] = daily_maintenance_window
        if maintenance_exclusion is not None:
            self._values["maintenance_exclusion"] = maintenance_exclusion
        if recurring_window is not None:
            self._values["recurring_window"] = recurring_window

    @builtins.property
    def daily_maintenance_window(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicyDailyMaintenanceWindow"]:
        '''daily_maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#daily_maintenance_window ContainerCluster#daily_maintenance_window}
        '''
        result = self._values.get("daily_maintenance_window")
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicyDailyMaintenanceWindow"], result)

    @builtins.property
    def maintenance_exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterMaintenancePolicyMaintenanceExclusion"]]]:
        '''maintenance_exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#maintenance_exclusion ContainerCluster#maintenance_exclusion}
        '''
        result = self._values.get("maintenance_exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterMaintenancePolicyMaintenanceExclusion"]]], result)

    @builtins.property
    def recurring_window(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicyRecurringWindow"]:
        '''recurring_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurring_window ContainerCluster#recurring_window}
        '''
        result = self._values.get("recurring_window")
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicyRecurringWindow"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMaintenancePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyDailyMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"start_time": "startTime"},
)
class ContainerClusterMaintenancePolicyDailyMaintenanceWindow:
    def __init__(self, *, start_time: builtins.str) -> None:
        '''
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyDailyMaintenanceWindow.__init__)
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "start_time": start_time,
        }

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMaintenancePolicyDailyMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterMaintenancePolicyDailyMaintenanceWindow]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicyDailyMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMaintenancePolicyDailyMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyMaintenanceExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "end_time": "endTime",
        "exclusion_name": "exclusionName",
        "start_time": "startTime",
        "exclusion_options": "exclusionOptions",
    },
)
class ContainerClusterMaintenancePolicyMaintenanceExclusion:
    def __init__(
        self,
        *,
        end_time: builtins.str,
        exclusion_name: builtins.str,
        start_time: builtins.str,
        exclusion_options: typing.Optional[typing.Union["ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#end_time ContainerCluster#end_time}.
        :param exclusion_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#exclusion_name ContainerCluster#exclusion_name}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.
        :param exclusion_options: exclusion_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#exclusion_options ContainerCluster#exclusion_options}
        '''
        if isinstance(exclusion_options, dict):
            exclusion_options = ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions(**exclusion_options)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusion.__init__)
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument exclusion_name", value=exclusion_name, expected_type=type_hints["exclusion_name"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument exclusion_options", value=exclusion_options, expected_type=type_hints["exclusion_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "end_time": end_time,
            "exclusion_name": exclusion_name,
            "start_time": start_time,
        }
        if exclusion_options is not None:
            self._values["exclusion_options"] = exclusion_options

    @builtins.property
    def end_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#end_time ContainerCluster#end_time}.'''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusion_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#exclusion_name ContainerCluster#exclusion_name}.'''
        result = self._values.get("exclusion_name")
        assert result is not None, "Required property 'exclusion_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusion_options(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions"]:
        '''exclusion_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#exclusion_options ContainerCluster#exclusion_options}
        '''
        result = self._values.get("exclusion_options")
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMaintenancePolicyMaintenanceExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions",
    jsii_struct_bases=[],
    name_mapping={"scope": "scope"},
)
class ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions:
    def __init__(self, *, scope: builtins.str) -> None:
        '''
        :param scope: The scope of automatic upgrades to restrict in the exclusion window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#scope ContainerCluster#scope}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "scope": scope,
        }

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of automatic upgrades to restrict in the exclusion window.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#scope ContainerCluster#scope}
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMaintenancePolicyMaintenanceExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyMaintenanceExclusionList",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMaintenancePolicyMaintenanceExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMaintenancePolicyMaintenanceExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMaintenancePolicyMaintenanceExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExclusionOptions")
    def put_exclusion_options(self, *, scope: builtins.str) -> None:
        '''
        :param scope: The scope of automatic upgrades to restrict in the exclusion window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#scope ContainerCluster#scope}
        '''
        value = ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions(
            scope=scope
        )

        return typing.cast(None, jsii.invoke(self, "putExclusionOptions", [value]))

    @jsii.member(jsii_name="resetExclusionOptions")
    def reset_exclusion_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionOptions", []))

    @builtins.property
    @jsii.member(jsii_name="exclusionOptions")
    def exclusion_options(
        self,
    ) -> ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference:
        return typing.cast(ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference, jsii.get(self, "exclusionOptions"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionNameInput")
    def exclusion_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exclusionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionOptionsInput")
    def exclusion_options_input(
        self,
    ) -> typing.Optional[ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions], jsii.get(self, "exclusionOptionsInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="exclusionName")
    def exclusion_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclusionName"))

    @exclusion_name.setter
    def exclusion_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference, "exclusion_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusionName", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterMaintenancePolicyMaintenanceExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterMaintenancePolicyMaintenanceExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterMaintenancePolicyMaintenanceExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMaintenancePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDailyMaintenanceWindow")
    def put_daily_maintenance_window(self, *, start_time: builtins.str) -> None:
        '''
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.
        '''
        value = ContainerClusterMaintenancePolicyDailyMaintenanceWindow(
            start_time=start_time
        )

        return typing.cast(None, jsii.invoke(self, "putDailyMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putMaintenanceExclusion")
    def put_maintenance_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterMaintenancePolicyMaintenanceExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyOutputReference.put_maintenance_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMaintenanceExclusion", [value]))

    @jsii.member(jsii_name="putRecurringWindow")
    def put_recurring_window(
        self,
        *,
        end_time: builtins.str,
        recurrence: builtins.str,
        start_time: builtins.str,
    ) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#end_time ContainerCluster#end_time}.
        :param recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurrence ContainerCluster#recurrence}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.
        '''
        value = ContainerClusterMaintenancePolicyRecurringWindow(
            end_time=end_time, recurrence=recurrence, start_time=start_time
        )

        return typing.cast(None, jsii.invoke(self, "putRecurringWindow", [value]))

    @jsii.member(jsii_name="resetDailyMaintenanceWindow")
    def reset_daily_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyMaintenanceWindow", []))

    @jsii.member(jsii_name="resetMaintenanceExclusion")
    def reset_maintenance_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceExclusion", []))

    @jsii.member(jsii_name="resetRecurringWindow")
    def reset_recurring_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurringWindow", []))

    @builtins.property
    @jsii.member(jsii_name="dailyMaintenanceWindow")
    def daily_maintenance_window(
        self,
    ) -> ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference:
        return typing.cast(ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference, jsii.get(self, "dailyMaintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceExclusion")
    def maintenance_exclusion(
        self,
    ) -> ContainerClusterMaintenancePolicyMaintenanceExclusionList:
        return typing.cast(ContainerClusterMaintenancePolicyMaintenanceExclusionList, jsii.get(self, "maintenanceExclusion"))

    @builtins.property
    @jsii.member(jsii_name="recurringWindow")
    def recurring_window(
        self,
    ) -> "ContainerClusterMaintenancePolicyRecurringWindowOutputReference":
        return typing.cast("ContainerClusterMaintenancePolicyRecurringWindowOutputReference", jsii.get(self, "recurringWindow"))

    @builtins.property
    @jsii.member(jsii_name="dailyMaintenanceWindowInput")
    def daily_maintenance_window_input(
        self,
    ) -> typing.Optional[ContainerClusterMaintenancePolicyDailyMaintenanceWindow]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicyDailyMaintenanceWindow], jsii.get(self, "dailyMaintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceExclusionInput")
    def maintenance_exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMaintenancePolicyMaintenanceExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMaintenancePolicyMaintenanceExclusion]]], jsii.get(self, "maintenanceExclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="recurringWindowInput")
    def recurring_window_input(
        self,
    ) -> typing.Optional["ContainerClusterMaintenancePolicyRecurringWindow"]:
        return typing.cast(typing.Optional["ContainerClusterMaintenancePolicyRecurringWindow"], jsii.get(self, "recurringWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterMaintenancePolicy]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMaintenancePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyRecurringWindow",
    jsii_struct_bases=[],
    name_mapping={
        "end_time": "endTime",
        "recurrence": "recurrence",
        "start_time": "startTime",
    },
)
class ContainerClusterMaintenancePolicyRecurringWindow:
    def __init__(
        self,
        *,
        end_time: builtins.str,
        recurrence: builtins.str,
        start_time: builtins.str,
    ) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#end_time ContainerCluster#end_time}.
        :param recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurrence ContainerCluster#recurrence}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyRecurringWindow.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#end_time ContainerCluster#end_time}.'''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#recurrence ContainerCluster#recurrence}.'''
        result = self._values.get("recurrence")
        assert result is not None, "Required property 'recurrence' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#start_time ContainerCluster#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMaintenancePolicyRecurringWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMaintenancePolicyRecurringWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMaintenancePolicyRecurringWindowOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMaintenancePolicyRecurringWindowOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyRecurringWindowOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrence"))

    @recurrence.setter
    def recurrence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyRecurringWindowOutputReference, "recurrence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyRecurringWindowOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterMaintenancePolicyRecurringWindow]:
        return typing.cast(typing.Optional[ContainerClusterMaintenancePolicyRecurringWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMaintenancePolicyRecurringWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMaintenancePolicyRecurringWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuth",
    jsii_struct_bases=[],
    name_mapping={"client_certificate_config": "clientCertificateConfig"},
)
class ContainerClusterMasterAuth:
    def __init__(
        self,
        *,
        client_certificate_config: typing.Union["ContainerClusterMasterAuthClientCertificateConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param client_certificate_config: client_certificate_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#client_certificate_config ContainerCluster#client_certificate_config}
        '''
        if isinstance(client_certificate_config, dict):
            client_certificate_config = ContainerClusterMasterAuthClientCertificateConfig(**client_certificate_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuth.__init__)
            check_type(argname="argument client_certificate_config", value=client_certificate_config, expected_type=type_hints["client_certificate_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_certificate_config": client_certificate_config,
        }

    @builtins.property
    def client_certificate_config(
        self,
    ) -> "ContainerClusterMasterAuthClientCertificateConfig":
        '''client_certificate_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#client_certificate_config ContainerCluster#client_certificate_config}
        '''
        result = self._values.get("client_certificate_config")
        assert result is not None, "Required property 'client_certificate_config' is missing"
        return typing.cast("ContainerClusterMasterAuthClientCertificateConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMasterAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthClientCertificateConfig",
    jsii_struct_bases=[],
    name_mapping={"issue_client_certificate": "issueClientCertificate"},
)
class ContainerClusterMasterAuthClientCertificateConfig:
    def __init__(
        self,
        *,
        issue_client_certificate: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param issue_client_certificate: Whether client certificate authorization is enabled for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#issue_client_certificate ContainerCluster#issue_client_certificate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthClientCertificateConfig.__init__)
            check_type(argname="argument issue_client_certificate", value=issue_client_certificate, expected_type=type_hints["issue_client_certificate"])
        self._values: typing.Dict[str, typing.Any] = {
            "issue_client_certificate": issue_client_certificate,
        }

    @builtins.property
    def issue_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether client certificate authorization is enabled for this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#issue_client_certificate ContainerCluster#issue_client_certificate}
        '''
        result = self._values.get("issue_client_certificate")
        assert result is not None, "Required property 'issue_client_certificate' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMasterAuthClientCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMasterAuthClientCertificateConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthClientCertificateConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthClientCertificateConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="issueClientCertificateInput")
    def issue_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "issueClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="issueClientCertificate")
    def issue_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "issueClientCertificate"))

    @issue_client_certificate.setter
    def issue_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthClientCertificateConfigOutputReference, "issue_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issueClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterMasterAuthClientCertificateConfig]:
        return typing.cast(typing.Optional[ContainerClusterMasterAuthClientCertificateConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMasterAuthClientCertificateConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthClientCertificateConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMasterAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientCertificateConfig")
    def put_client_certificate_config(
        self,
        *,
        issue_client_certificate: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param issue_client_certificate: Whether client certificate authorization is enabled for this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#issue_client_certificate ContainerCluster#issue_client_certificate}
        '''
        value = ContainerClusterMasterAuthClientCertificateConfig(
            issue_client_certificate=issue_client_certificate
        )

        return typing.cast(None, jsii.invoke(self, "putClientCertificateConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateConfig")
    def client_certificate_config(
        self,
    ) -> ContainerClusterMasterAuthClientCertificateConfigOutputReference:
        return typing.cast(ContainerClusterMasterAuthClientCertificateConfigOutputReference, jsii.get(self, "clientCertificateConfig"))

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterCaCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateConfigInput")
    def client_certificate_config_input(
        self,
    ) -> typing.Optional[ContainerClusterMasterAuthClientCertificateConfig]:
        return typing.cast(typing.Optional[ContainerClusterMasterAuthClientCertificateConfig], jsii.get(self, "clientCertificateConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterMasterAuth]:
        return typing.cast(typing.Optional[ContainerClusterMasterAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMasterAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthorizedNetworksConfig",
    jsii_struct_bases=[],
    name_mapping={"cidr_blocks": "cidrBlocks"},
)
class ContainerClusterMasterAuthorizedNetworksConfig:
    def __init__(
        self,
        *,
        cidr_blocks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cidr_blocks: cidr_blocks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cidr_blocks ContainerCluster#cidr_blocks}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfig.__init__)
            check_type(argname="argument cidr_blocks", value=cidr_blocks, expected_type=type_hints["cidr_blocks"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cidr_blocks is not None:
            self._values["cidr_blocks"] = cidr_blocks

    @builtins.property
    def cidr_blocks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks"]]]:
        '''cidr_blocks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cidr_blocks ContainerCluster#cidr_blocks}
        '''
        result = self._values.get("cidr_blocks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMasterAuthorizedNetworksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks",
    jsii_struct_bases=[],
    name_mapping={"cidr_block": "cidrBlock", "display_name": "displayName"},
)
class ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks:
    def __init__(
        self,
        *,
        cidr_block: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cidr_block: External network that can access Kubernetes master through HTTPS. Must be specified in CIDR notation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cidr_block ContainerCluster#cidr_block}
        :param display_name: Field for users to identify CIDR blocks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#display_name ContainerCluster#display_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks.__init__)
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "cidr_block": cidr_block,
        }
        if display_name is not None:
            self._values["display_name"] = display_name

    @builtins.property
    def cidr_block(self) -> builtins.str:
        '''External network that can access Kubernetes master through HTTPS. Must be specified in CIDR notation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#cidr_block ContainerCluster#cidr_block}
        '''
        result = self._values.get("cidr_block")
        assert result is not None, "Required property 'cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Field for users to identify CIDR blocks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#display_name ContainerCluster#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList",
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
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterMasterAuthorizedNetworksConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMasterAuthorizedNetworksConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCidrBlocks")
    def put_cidr_blocks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMasterAuthorizedNetworksConfigOutputReference.put_cidr_blocks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCidrBlocks", [value]))

    @jsii.member(jsii_name="resetCidrBlocks")
    def reset_cidr_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlocks", []))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList:
        return typing.cast(ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList, jsii.get(self, "cidrBlocks"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocksInput")
    def cidr_blocks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks]]], jsii.get(self, "cidrBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterMasterAuthorizedNetworksConfig]:
        return typing.cast(typing.Optional[ContainerClusterMasterAuthorizedNetworksConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMasterAuthorizedNetworksConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMasterAuthorizedNetworksConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMeshCertificates",
    jsii_struct_bases=[],
    name_mapping={"enable_certificates": "enableCertificates"},
)
class ContainerClusterMeshCertificates:
    def __init__(
        self,
        *,
        enable_certificates: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_certificates: When enabled the GKE Workload Identity Certificates controller and node agent will be deployed in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_certificates ContainerCluster#enable_certificates}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMeshCertificates.__init__)
            check_type(argname="argument enable_certificates", value=enable_certificates, expected_type=type_hints["enable_certificates"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_certificates": enable_certificates,
        }

    @builtins.property
    def enable_certificates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When enabled the GKE Workload Identity Certificates controller and node agent will be deployed in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_certificates ContainerCluster#enable_certificates}
        '''
        result = self._values.get("enable_certificates")
        assert result is not None, "Required property 'enable_certificates' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMeshCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMeshCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMeshCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMeshCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableCertificatesInput")
    def enable_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCertificates")
    def enable_certificates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableCertificates"))

    @enable_certificates.setter
    def enable_certificates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMeshCertificatesOutputReference, "enable_certificates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCertificates", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterMeshCertificates]:
        return typing.cast(typing.Optional[ContainerClusterMeshCertificates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMeshCertificates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMeshCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMonitoringConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_components": "enableComponents"},
)
class ContainerClusterMonitoringConfig:
    def __init__(self, *, enable_components: typing.Sequence[builtins.str]) -> None:
        '''
        :param enable_components: GKE components exposing metrics. Valid values include SYSTEM_COMPONENTS, APISERVER, CONTROLLER_MANAGER, and SCHEDULER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterMonitoringConfig.__init__)
            check_type(argname="argument enable_components", value=enable_components, expected_type=type_hints["enable_components"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_components": enable_components,
        }

    @builtins.property
    def enable_components(self) -> typing.List[builtins.str]:
        '''GKE components exposing metrics. Valid values include SYSTEM_COMPONENTS, APISERVER, CONTROLLER_MANAGER, and SCHEDULER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_components ContainerCluster#enable_components}
        '''
        result = self._values.get("enable_components")
        assert result is not None, "Required property 'enable_components' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterMonitoringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterMonitoringConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterMonitoringConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterMonitoringConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableComponentsInput")
    def enable_components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enableComponentsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableComponents")
    def enable_components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enableComponents"))

    @enable_components.setter
    def enable_components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMonitoringConfigOutputReference, "enable_components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableComponents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterMonitoringConfig]:
        return typing.cast(typing.Optional[ContainerClusterMonitoringConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterMonitoringConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterMonitoringConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNetworkPolicy",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "provider": "provider"},
)
class ContainerClusterNetworkPolicy:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether network policy is enabled on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param provider: The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#provider ContainerCluster#provider}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNetworkPolicy.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether network policy is enabled on the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#provider ContainerCluster#provider}
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNetworkPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNetworkPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNetworkPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNetworkPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProvider")
    def reset_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvider", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="providerInput")
    def provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNetworkPolicyOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNetworkPolicyOutputReference, "provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provider", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNetworkPolicy]:
        return typing.cast(typing.Optional[ContainerClusterNetworkPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNetworkPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNetworkPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_kms_key": "bootDiskKmsKey",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
        "gcfs_config": "gcfsConfig",
        "guest_accelerator": "guestAccelerator",
        "gvnic": "gvnic",
        "image_type": "imageType",
        "labels": "labels",
        "local_ssd_count": "localSsdCount",
        "machine_type": "machineType",
        "metadata": "metadata",
        "min_cpu_platform": "minCpuPlatform",
        "node_group": "nodeGroup",
        "oauth_scopes": "oauthScopes",
        "preemptible": "preemptible",
        "reservation_affinity": "reservationAffinity",
        "service_account": "serviceAccount",
        "shielded_instance_config": "shieldedInstanceConfig",
        "spot": "spot",
        "tags": "tags",
        "taint": "taint",
        "workload_metadata_config": "workloadMetadataConfig",
    },
)
class ContainerClusterNodeConfig:
    def __init__(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        gcfs_config: typing.Optional[typing.Union["ContainerClusterNodeConfigGcfsConfig", typing.Dict[str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodeConfigGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union["ContainerClusterNodeConfigGvnic", typing.Dict[str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union["ContainerClusterNodeConfigReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["ContainerClusterNodeConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodeConfigTaint", typing.Dict[str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union["ContainerClusterNodeConfigWorkloadMetadataConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        if isinstance(gcfs_config, dict):
            gcfs_config = ContainerClusterNodeConfigGcfsConfig(**gcfs_config)
        if isinstance(gvnic, dict):
            gvnic = ContainerClusterNodeConfigGvnic(**gvnic)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = ContainerClusterNodeConfigReservationAffinity(**reservation_affinity)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = ContainerClusterNodeConfigShieldedInstanceConfig(**shielded_instance_config)
        if isinstance(workload_metadata_config, dict):
            workload_metadata_config = ContainerClusterNodeConfigWorkloadMetadataConfig(**workload_metadata_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfig.__init__)
            check_type(argname="argument boot_disk_kms_key", value=boot_disk_kms_key, expected_type=type_hints["boot_disk_kms_key"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument gcfs_config", value=gcfs_config, expected_type=type_hints["gcfs_config"])
            check_type(argname="argument guest_accelerator", value=guest_accelerator, expected_type=type_hints["guest_accelerator"])
            check_type(argname="argument gvnic", value=gvnic, expected_type=type_hints["gvnic"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument local_ssd_count", value=local_ssd_count, expected_type=type_hints["local_ssd_count"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument node_group", value=node_group, expected_type=type_hints["node_group"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument preemptible", value=preemptible, expected_type=type_hints["preemptible"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taint", value=taint, expected_type=type_hints["taint"])
            check_type(argname="argument workload_metadata_config", value=workload_metadata_config, expected_type=type_hints["workload_metadata_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_kms_key is not None:
            self._values["boot_disk_kms_key"] = boot_disk_kms_key
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if gcfs_config is not None:
            self._values["gcfs_config"] = gcfs_config
        if guest_accelerator is not None:
            self._values["guest_accelerator"] = guest_accelerator
        if gvnic is not None:
            self._values["gvnic"] = gvnic
        if image_type is not None:
            self._values["image_type"] = image_type
        if labels is not None:
            self._values["labels"] = labels
        if local_ssd_count is not None:
            self._values["local_ssd_count"] = local_ssd_count
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if metadata is not None:
            self._values["metadata"] = metadata
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if node_group is not None:
            self._values["node_group"] = node_group
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if preemptible is not None:
            self._values["preemptible"] = preemptible
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if service_account is not None:
            self._values["service_account"] = service_account
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if spot is not None:
            self._values["spot"] = spot
        if tags is not None:
            self._values["tags"] = tags
        if taint is not None:
            self._values["taint"] = taint
        if workload_metadata_config is not None:
            self._values["workload_metadata_config"] = workload_metadata_config

    @builtins.property
    def boot_disk_kms_key(self) -> typing.Optional[builtins.str]:
        '''The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        '''
        result = self._values.get("boot_disk_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcfs_config(self) -> typing.Optional["ContainerClusterNodeConfigGcfsConfig"]:
        '''gcfs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        '''
        result = self._values.get("gcfs_config")
        return typing.cast(typing.Optional["ContainerClusterNodeConfigGcfsConfig"], result)

    @builtins.property
    def guest_accelerator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigGuestAccelerator"]]]:
        '''List of the type and count of accelerator cards attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        '''
        result = self._values.get("guest_accelerator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigGuestAccelerator"]]], result)

    @builtins.property
    def gvnic(self) -> typing.Optional["ContainerClusterNodeConfigGvnic"]:
        '''gvnic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        '''
        result = self._values.get("gvnic")
        return typing.cast(typing.Optional["ContainerClusterNodeConfigGvnic"], result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The image type to use for this node.

        Note that for a given image type, the latest version of it will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The map of Kubernetes labels (key/value pairs) to be applied to each node.

        These will added in addition to any default label(s) that Kubernetes may apply to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def local_ssd_count(self) -> typing.Optional[jsii.Number]:
        '''The number of local SSD disks to be attached to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        '''
        result = self._values.get("local_ssd_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Google Compute Engine machine type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The metadata key/value pairs assigned to instances in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Minimum CPU platform to be used by this instance.

        The instance may be scheduled on the specified or newer CPU platform.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_group(self) -> typing.Optional[builtins.str]:
        '''Setting this field will assign instances of this pool to run on the specified node group.

        This is useful for running workloads on sole tenant nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        '''
        result = self._values.get("node_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of Google API scopes to be made available on all of the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes are created as preemptible VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["ContainerClusterNodeConfigReservationAffinity"], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Platform Service Account to be used by the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["ContainerClusterNodeConfigShieldedInstanceConfig"], result)

    @builtins.property
    def spot(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes are created as spot VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of instance tags applied to all nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigTaint"]]]:
        '''List of Kubernetes taints to be applied to each node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        '''
        result = self._values.get("taint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigTaint"]]], result)

    @builtins.property
    def workload_metadata_config(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigWorkloadMetadataConfig"]:
        '''workload_metadata_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        result = self._values.get("workload_metadata_config")
        return typing.cast(typing.Optional["ContainerClusterNodeConfigWorkloadMetadataConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGcfsConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterNodeConfigGcfsConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGcfsConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not GCFS is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigGcfsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigGcfsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGcfsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGcfsConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGcfsConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigGcfsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfigGcfsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGcfsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGuestAccelerator",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "gpu_partition_size": "gpuPartitionSize",
        "type": "type",
    },
)
class ContainerClusterNodeConfigGuestAccelerator:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        gpu_partition_size: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#count ContainerCluster#count}.
        :param gpu_partition_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gpu_partition_size ContainerCluster#gpu_partition_size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#type ContainerCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGuestAccelerator.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument gpu_partition_size", value=gpu_partition_size, expected_type=type_hints["gpu_partition_size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if gpu_partition_size is not None:
            self._values["gpu_partition_size"] = gpu_partition_size
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#count ContainerCluster#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gpu_partition_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gpu_partition_size ContainerCluster#gpu_partition_size}.'''
        result = self._values.get("gpu_partition_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#type ContainerCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigGuestAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigGuestAcceleratorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGuestAcceleratorList",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGuestAcceleratorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterNodeConfigGuestAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGuestAcceleratorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterNodeConfigGuestAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigGuestAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigGuestAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodeConfigGuestAcceleratorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGuestAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGuestAcceleratorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetGpuPartitionSize")
    def reset_gpu_partition_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuPartitionSize", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSizeInput")
    def gpu_partition_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpuPartitionSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSize")
    def gpu_partition_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpuPartitionSize"))

    @gpu_partition_size.setter
    def gpu_partition_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorOutputReference, "gpu_partition_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuPartitionSize", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterNodeConfigGuestAccelerator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterNodeConfigGuestAccelerator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterNodeConfigGuestAccelerator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGuestAcceleratorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGvnic",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterNodeConfigGvnic:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGvnic.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not gvnic is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigGvnic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigGvnicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigGvnicOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigGvnicOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGvnicOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodeConfigGvnic]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigGvnic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfigGvnic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigGvnicOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodeConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcfsConfig")
    def put_gcfs_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterNodeConfigGcfsConfig(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGcfsConfig", [value]))

    @jsii.member(jsii_name="putGuestAccelerator")
    def put_guest_accelerator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterNodeConfigGuestAccelerator, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigOutputReference.put_guest_accelerator)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestAccelerator", [value]))

    @jsii.member(jsii_name="putGvnic")
    def put_gvnic(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterNodeConfigGvnic(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGvnic", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        value = ContainerClusterNodeConfigReservationAffinity(
            consume_reservation_type=consume_reservation_type, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putReservationAffinity", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        value = ContainerClusterNodeConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodeConfigTaint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigOutputReference.put_taint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="putWorkloadMetadataConfig")
    def put_workload_metadata_config(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        value = ContainerClusterNodeConfigWorkloadMetadataConfig(mode=mode)

        return typing.cast(None, jsii.invoke(self, "putWorkloadMetadataConfig", [value]))

    @jsii.member(jsii_name="resetBootDiskKmsKey")
    def reset_boot_disk_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskKmsKey", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetGcfsConfig")
    def reset_gcfs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcfsConfig", []))

    @jsii.member(jsii_name="resetGuestAccelerator")
    def reset_guest_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestAccelerator", []))

    @jsii.member(jsii_name="resetGvnic")
    def reset_gvnic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGvnic", []))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLocalSsdCount")
    def reset_local_ssd_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSsdCount", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNodeGroup")
    def reset_node_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeGroup", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetPreemptible")
    def reset_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptible", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetSpot")
    def reset_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpot", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaint")
    def reset_taint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaint", []))

    @jsii.member(jsii_name="resetWorkloadMetadataConfig")
    def reset_workload_metadata_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadMetadataConfig", []))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfig")
    def gcfs_config(self) -> ContainerClusterNodeConfigGcfsConfigOutputReference:
        return typing.cast(ContainerClusterNodeConfigGcfsConfigOutputReference, jsii.get(self, "gcfsConfig"))

    @builtins.property
    @jsii.member(jsii_name="guestAccelerator")
    def guest_accelerator(self) -> ContainerClusterNodeConfigGuestAcceleratorList:
        return typing.cast(ContainerClusterNodeConfigGuestAcceleratorList, jsii.get(self, "guestAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="gvnic")
    def gvnic(self) -> ContainerClusterNodeConfigGvnicOutputReference:
        return typing.cast(ContainerClusterNodeConfigGvnicOutputReference, jsii.get(self, "gvnic"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "ContainerClusterNodeConfigReservationAffinityOutputReference":
        return typing.cast("ContainerClusterNodeConfigReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "ContainerClusterNodeConfigShieldedInstanceConfigOutputReference":
        return typing.cast("ContainerClusterNodeConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "ContainerClusterNodeConfigTaintList":
        return typing.cast("ContainerClusterNodeConfigTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> "ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference":
        return typing.cast("ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference", jsii.get(self, "workloadMetadataConfig"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKeyInput")
    def boot_disk_kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskKmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfigInput")
    def gcfs_config_input(
        self,
    ) -> typing.Optional[ContainerClusterNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigGcfsConfig], jsii.get(self, "gcfsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="guestAcceleratorInput")
    def guest_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigGuestAccelerator]]], jsii.get(self, "guestAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="gvnicInput")
    def gvnic_input(self) -> typing.Optional[ContainerClusterNodeConfigGvnic]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigGvnic], jsii.get(self, "gvnicInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="localSsdCountInput")
    def local_ssd_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localSsdCountInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeGroupInput")
    def node_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleInput")
    def preemptible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigReservationAffinity"]:
        return typing.cast(typing.Optional["ContainerClusterNodeConfigReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNodeConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInput")
    def spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "spotInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigTaint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodeConfigTaint"]]], jsii.get(self, "taintInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfigInput")
    def workload_metadata_config_input(
        self,
    ) -> typing.Optional["ContainerClusterNodeConfigWorkloadMetadataConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNodeConfigWorkloadMetadataConfig"], jsii.get(self, "workloadMetadataConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskKmsKey"))

    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "boot_disk_kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "image_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="localSsdCount")
    def local_ssd_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localSsdCount"))

    @local_ssd_count.setter
    def local_ssd_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "local_ssd_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localSsdCount", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="nodeGroup")
    def node_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeGroup"))

    @node_group.setter
    def node_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "node_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="preemptible")
    def preemptible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preemptible"))

    @preemptible.setter
    def preemptible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "spot"))

    @spot.setter
    def spot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spot", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodeConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "consume_reservation_type": "consumeReservationType",
        "key": "key",
        "values": "values",
    },
)
class ContainerClusterNodeConfigReservationAffinity:
    def __init__(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigReservationAffinity.__init__)
            check_type(argname="argument consume_reservation_type", value=consume_reservation_type, expected_type=type_hints["consume_reservation_type"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "consume_reservation_type": consume_reservation_type,
        }
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def consume_reservation_type(self) -> builtins.str:
        '''Corresponds to the type of reservation consumption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        '''
        result = self._values.get("consume_reservation_type")
        assert result is not None, "Required property 'consume_reservation_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key of a reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The label values of the reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigReservationAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigReservationAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationTypeInput")
    def consume_reservation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumeReservationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationType")
    def consume_reservation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumeReservationType"))

    @consume_reservation_type.setter
    def consume_reservation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigReservationAffinityOutputReference, "consume_reservation_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumeReservationType", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigReservationAffinityOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigReservationAffinityOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodeConfigReservationAffinity]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfigReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigReservationAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
    },
)
class ContainerClusterNodeConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has integrity monitoring enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has Secure Boot enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodeConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class ContainerClusterNodeConfigTaint:
    def __init__(
        self,
        *,
        effect: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param effect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#effect ContainerCluster#effect}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#value ContainerCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigTaint.__init__)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#effect ContainerCluster#effect}.'''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#value ContainerCluster#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigTaintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigTaintList",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigTaintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterNodeConfigTaintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigTaintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterNodeConfigTaintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigTaint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigTaint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodeConfigTaint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodeConfigTaintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigTaintOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigTaintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEffect")
    def reset_effect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffect", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintOutputReference, "effect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterNodeConfigTaint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterNodeConfigTaint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterNodeConfigTaint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigTaintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigWorkloadMetadataConfig",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class ContainerClusterNodeConfigWorkloadMetadataConfig:
    def __init__(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigWorkloadMetadataConfig.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode is the configuration for how to expose metadata to workloads running on the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodeConfigWorkloadMetadataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodeConfigWorkloadMetadataConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodeConfigWorkloadMetadataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodeConfigWorkloadMetadataConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePool",
    jsii_struct_bases=[],
    name_mapping={
        "autoscaling": "autoscaling",
        "initial_node_count": "initialNodeCount",
        "management": "management",
        "max_pods_per_node": "maxPodsPerNode",
        "name": "name",
        "name_prefix": "namePrefix",
        "node_config": "nodeConfig",
        "node_count": "nodeCount",
        "node_locations": "nodeLocations",
        "upgrade_settings": "upgradeSettings",
        "version": "version",
    },
)
class ContainerClusterNodePool:
    def __init__(
        self,
        *,
        autoscaling: typing.Optional[typing.Union["ContainerClusterNodePoolAutoscaling", typing.Dict[str, typing.Any]]] = None,
        initial_node_count: typing.Optional[jsii.Number] = None,
        management: typing.Optional[typing.Union["ContainerClusterNodePoolManagement", typing.Dict[str, typing.Any]]] = None,
        max_pods_per_node: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        node_config: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfig", typing.Dict[str, typing.Any]]] = None,
        node_count: typing.Optional[jsii.Number] = None,
        node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        upgrade_settings: typing.Optional[typing.Union["ContainerClusterNodePoolUpgradeSettings", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#autoscaling ContainerCluster#autoscaling}
        :param initial_node_count: The initial number of nodes for the pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Changing this will force recreation of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#initial_node_count ContainerCluster#initial_node_count}
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#management ContainerCluster#management}
        :param max_pods_per_node: The maximum number of pods per node in this node pool. Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_pods_per_node ContainerCluster#max_pods_per_node}
        :param name: The name of the node pool. If left blank, Terraform will auto-generate a unique name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name ContainerCluster#name}
        :param name_prefix: Creates a unique name for the node pool beginning with the specified prefix. Conflicts with name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name_prefix ContainerCluster#name_prefix}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_config ContainerCluster#node_config}
        :param node_count: The number of nodes per instance group. This field can be used to update the number of nodes per instance group but should not be used alongside autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_count ContainerCluster#node_count}
        :param node_locations: The list of zones in which the node pool's nodes should be located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If unspecified, the cluster-level node_locations will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_locations ContainerCluster#node_locations}
        :param upgrade_settings: upgrade_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#upgrade_settings ContainerCluster#upgrade_settings}
        :param version: The Kubernetes version for the nodes in this pool. Note that if this field and auto_upgrade are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#version ContainerCluster#version}
        '''
        if isinstance(autoscaling, dict):
            autoscaling = ContainerClusterNodePoolAutoscaling(**autoscaling)
        if isinstance(management, dict):
            management = ContainerClusterNodePoolManagement(**management)
        if isinstance(node_config, dict):
            node_config = ContainerClusterNodePoolNodeConfig(**node_config)
        if isinstance(upgrade_settings, dict):
            upgrade_settings = ContainerClusterNodePoolUpgradeSettings(**upgrade_settings)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePool.__init__)
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument initial_node_count", value=initial_node_count, expected_type=type_hints["initial_node_count"])
            check_type(argname="argument management", value=management, expected_type=type_hints["management"])
            check_type(argname="argument max_pods_per_node", value=max_pods_per_node, expected_type=type_hints["max_pods_per_node"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument node_config", value=node_config, expected_type=type_hints["node_config"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument node_locations", value=node_locations, expected_type=type_hints["node_locations"])
            check_type(argname="argument upgrade_settings", value=upgrade_settings, expected_type=type_hints["upgrade_settings"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if initial_node_count is not None:
            self._values["initial_node_count"] = initial_node_count
        if management is not None:
            self._values["management"] = management
        if max_pods_per_node is not None:
            self._values["max_pods_per_node"] = max_pods_per_node
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if node_config is not None:
            self._values["node_config"] = node_config
        if node_count is not None:
            self._values["node_count"] = node_count
        if node_locations is not None:
            self._values["node_locations"] = node_locations
        if upgrade_settings is not None:
            self._values["upgrade_settings"] = upgrade_settings
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def autoscaling(self) -> typing.Optional["ContainerClusterNodePoolAutoscaling"]:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#autoscaling ContainerCluster#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional["ContainerClusterNodePoolAutoscaling"], result)

    @builtins.property
    def initial_node_count(self) -> typing.Optional[jsii.Number]:
        '''The initial number of nodes for the pool.

        In regional or multi-zonal clusters, this is the number of nodes per zone. Changing this will force recreation of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#initial_node_count ContainerCluster#initial_node_count}
        '''
        result = self._values.get("initial_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def management(self) -> typing.Optional["ContainerClusterNodePoolManagement"]:
        '''management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#management ContainerCluster#management}
        '''
        result = self._values.get("management")
        return typing.cast(typing.Optional["ContainerClusterNodePoolManagement"], result)

    @builtins.property
    def max_pods_per_node(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of pods per node in this node pool.

        Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_pods_per_node ContainerCluster#max_pods_per_node}
        '''
        result = self._values.get("max_pods_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the node pool. If left blank, Terraform will auto-generate a unique name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name ContainerCluster#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name for the node pool beginning with the specified prefix. Conflicts with name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#name_prefix ContainerCluster#name_prefix}
        '''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_config(self) -> typing.Optional["ContainerClusterNodePoolNodeConfig"]:
        '''node_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_config ContainerCluster#node_config}
        '''
        result = self._values.get("node_config")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfig"], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes per instance group.

        This field can be used to update the number of nodes per instance group but should not be used alongside autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_count ContainerCluster#node_count}
        '''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of zones in which the node pool's nodes should be located.

        Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If unspecified, the cluster-level node_locations will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_locations ContainerCluster#node_locations}
        '''
        result = self._values.get("node_locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def upgrade_settings(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolUpgradeSettings"]:
        '''upgrade_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#upgrade_settings ContainerCluster#upgrade_settings}
        '''
        result = self._values.get("upgrade_settings")
        return typing.cast(typing.Optional["ContainerClusterNodePoolUpgradeSettings"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes version for the nodes in this pool.

        Note that if this field and auto_upgrade are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#version ContainerCluster#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolAutoscaling",
    jsii_struct_bases=[],
    name_mapping={"max_node_count": "maxNodeCount", "min_node_count": "minNodeCount"},
)
class ContainerClusterNodePoolAutoscaling:
    def __init__(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: Maximum number of nodes in the NodePool. Must be >= min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_node_count ContainerCluster#max_node_count}
        :param min_node_count: Minimum number of nodes in the NodePool. Must be >=0 and <= max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_node_count ContainerCluster#min_node_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolAutoscaling.__init__)
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_node_count": max_node_count,
            "min_node_count": min_node_count,
        }

    @builtins.property
    def max_node_count(self) -> jsii.Number:
        '''Maximum number of nodes in the NodePool. Must be >= min_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_node_count ContainerCluster#max_node_count}
        '''
        result = self._values.get("max_node_count")
        assert result is not None, "Required property 'max_node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_node_count(self) -> jsii.Number:
        '''Minimum number of nodes in the NodePool. Must be >=0 and <= max_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_node_count ContainerCluster#min_node_count}
        '''
        result = self._values.get("min_node_count")
        assert result is not None, "Required property 'min_node_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolAutoscalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxNodeCountInput")
    def max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCountInput")
    def min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeCount")
    def max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodeCount"))

    @max_node_count.setter
    def max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolAutoscalingOutputReference, "max_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolAutoscalingOutputReference, "min_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodePoolAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodePoolList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolList",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerClusterNodePoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterNodePoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePool]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolManagement",
    jsii_struct_bases=[],
    name_mapping={"auto_repair": "autoRepair", "auto_upgrade": "autoUpgrade"},
)
class ContainerClusterNodePoolManagement:
    def __init__(
        self,
        *,
        auto_repair: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param auto_repair: Whether the nodes will be automatically repaired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_repair ContainerCluster#auto_repair}
        :param auto_upgrade: Whether the nodes will be automatically upgraded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_upgrade ContainerCluster#auto_upgrade}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolManagement.__init__)
            check_type(argname="argument auto_repair", value=auto_repair, expected_type=type_hints["auto_repair"])
            check_type(argname="argument auto_upgrade", value=auto_upgrade, expected_type=type_hints["auto_upgrade"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_repair is not None:
            self._values["auto_repair"] = auto_repair
        if auto_upgrade is not None:
            self._values["auto_upgrade"] = auto_upgrade

    @builtins.property
    def auto_repair(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes will be automatically repaired.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_repair ContainerCluster#auto_repair}
        '''
        result = self._values.get("auto_repair")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes will be automatically upgraded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_upgrade ContainerCluster#auto_upgrade}
        '''
        result = self._values.get("auto_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolManagementOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoRepair")
    def reset_auto_repair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRepair", []))

    @jsii.member(jsii_name="resetAutoUpgrade")
    def reset_auto_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgrade", []))

    @builtins.property
    @jsii.member(jsii_name="autoRepairInput")
    def auto_repair_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoRepairInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeInput")
    def auto_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRepair")
    def auto_repair(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoRepair"))

    @auto_repair.setter
    def auto_repair(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolManagementOutputReference, "auto_repair").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRepair", value)

    @builtins.property
    @jsii.member(jsii_name="autoUpgrade")
    def auto_upgrade(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoUpgrade"))

    @auto_upgrade.setter
    def auto_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolManagementOutputReference, "auto_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodePoolManagement]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_kms_key": "bootDiskKmsKey",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
        "gcfs_config": "gcfsConfig",
        "guest_accelerator": "guestAccelerator",
        "gvnic": "gvnic",
        "image_type": "imageType",
        "labels": "labels",
        "local_ssd_count": "localSsdCount",
        "machine_type": "machineType",
        "metadata": "metadata",
        "min_cpu_platform": "minCpuPlatform",
        "node_group": "nodeGroup",
        "oauth_scopes": "oauthScopes",
        "preemptible": "preemptible",
        "reservation_affinity": "reservationAffinity",
        "service_account": "serviceAccount",
        "shielded_instance_config": "shieldedInstanceConfig",
        "spot": "spot",
        "tags": "tags",
        "taint": "taint",
        "workload_metadata_config": "workloadMetadataConfig",
    },
)
class ContainerClusterNodePoolNodeConfig:
    def __init__(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        gcfs_config: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfigGcfsConfig", typing.Dict[str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePoolNodeConfigGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfigGvnic", typing.Dict[str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfigReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePoolNodeConfigTaint", typing.Dict[str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union["ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        if isinstance(gcfs_config, dict):
            gcfs_config = ContainerClusterNodePoolNodeConfigGcfsConfig(**gcfs_config)
        if isinstance(gvnic, dict):
            gvnic = ContainerClusterNodePoolNodeConfigGvnic(**gvnic)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = ContainerClusterNodePoolNodeConfigReservationAffinity(**reservation_affinity)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = ContainerClusterNodePoolNodeConfigShieldedInstanceConfig(**shielded_instance_config)
        if isinstance(workload_metadata_config, dict):
            workload_metadata_config = ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig(**workload_metadata_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfig.__init__)
            check_type(argname="argument boot_disk_kms_key", value=boot_disk_kms_key, expected_type=type_hints["boot_disk_kms_key"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument gcfs_config", value=gcfs_config, expected_type=type_hints["gcfs_config"])
            check_type(argname="argument guest_accelerator", value=guest_accelerator, expected_type=type_hints["guest_accelerator"])
            check_type(argname="argument gvnic", value=gvnic, expected_type=type_hints["gvnic"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument local_ssd_count", value=local_ssd_count, expected_type=type_hints["local_ssd_count"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument node_group", value=node_group, expected_type=type_hints["node_group"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument preemptible", value=preemptible, expected_type=type_hints["preemptible"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taint", value=taint, expected_type=type_hints["taint"])
            check_type(argname="argument workload_metadata_config", value=workload_metadata_config, expected_type=type_hints["workload_metadata_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_kms_key is not None:
            self._values["boot_disk_kms_key"] = boot_disk_kms_key
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if gcfs_config is not None:
            self._values["gcfs_config"] = gcfs_config
        if guest_accelerator is not None:
            self._values["guest_accelerator"] = guest_accelerator
        if gvnic is not None:
            self._values["gvnic"] = gvnic
        if image_type is not None:
            self._values["image_type"] = image_type
        if labels is not None:
            self._values["labels"] = labels
        if local_ssd_count is not None:
            self._values["local_ssd_count"] = local_ssd_count
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if metadata is not None:
            self._values["metadata"] = metadata
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if node_group is not None:
            self._values["node_group"] = node_group
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if preemptible is not None:
            self._values["preemptible"] = preemptible
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if service_account is not None:
            self._values["service_account"] = service_account
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if spot is not None:
            self._values["spot"] = spot
        if tags is not None:
            self._values["tags"] = tags
        if taint is not None:
            self._values["taint"] = taint
        if workload_metadata_config is not None:
            self._values["workload_metadata_config"] = workload_metadata_config

    @builtins.property
    def boot_disk_kms_key(self) -> typing.Optional[builtins.str]:
        '''The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        '''
        result = self._values.get("boot_disk_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcfs_config(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigGcfsConfig"]:
        '''gcfs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        '''
        result = self._values.get("gcfs_config")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigGcfsConfig"], result)

    @builtins.property
    def guest_accelerator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigGuestAccelerator"]]]:
        '''List of the type and count of accelerator cards attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        '''
        result = self._values.get("guest_accelerator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigGuestAccelerator"]]], result)

    @builtins.property
    def gvnic(self) -> typing.Optional["ContainerClusterNodePoolNodeConfigGvnic"]:
        '''gvnic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        '''
        result = self._values.get("gvnic")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigGvnic"], result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The image type to use for this node.

        Note that for a given image type, the latest version of it will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The map of Kubernetes labels (key/value pairs) to be applied to each node.

        These will added in addition to any default label(s) that Kubernetes may apply to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def local_ssd_count(self) -> typing.Optional[jsii.Number]:
        '''The number of local SSD disks to be attached to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        '''
        result = self._values.get("local_ssd_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Google Compute Engine machine type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The metadata key/value pairs assigned to instances in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Minimum CPU platform to be used by this instance.

        The instance may be scheduled on the specified or newer CPU platform.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_group(self) -> typing.Optional[builtins.str]:
        '''Setting this field will assign instances of this pool to run on the specified node group.

        This is useful for running workloads on sole tenant nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        '''
        result = self._values.get("node_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of Google API scopes to be made available on all of the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes are created as preemptible VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigReservationAffinity"], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Platform Service Account to be used by the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigShieldedInstanceConfig"], result)

    @builtins.property
    def spot(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes are created as spot VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of instance tags applied to all nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigTaint"]]]:
        '''List of Kubernetes taints to be applied to each node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        '''
        result = self._values.get("taint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigTaint"]]], result)

    @builtins.property
    def workload_metadata_config(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig"]:
        '''workload_metadata_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        result = self._values.get("workload_metadata_config")
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGcfsConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterNodePoolNodeConfigGcfsConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGcfsConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not GCFS is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigGcfsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigGcfsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfigGcfsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGuestAccelerator",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "gpu_partition_size": "gpuPartitionSize",
        "type": "type",
    },
)
class ContainerClusterNodePoolNodeConfigGuestAccelerator:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        gpu_partition_size: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#count ContainerCluster#count}.
        :param gpu_partition_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gpu_partition_size ContainerCluster#gpu_partition_size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#type ContainerCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGuestAccelerator.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument gpu_partition_size", value=gpu_partition_size, expected_type=type_hints["gpu_partition_size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if gpu_partition_size is not None:
            self._values["gpu_partition_size"] = gpu_partition_size
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#count ContainerCluster#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gpu_partition_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gpu_partition_size ContainerCluster#gpu_partition_size}.'''
        result = self._values.get("gpu_partition_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#type ContainerCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigGuestAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigGuestAcceleratorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGuestAcceleratorList",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGuestAcceleratorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGuestAcceleratorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigGuestAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigGuestAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetGpuPartitionSize")
    def reset_gpu_partition_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuPartitionSize", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSizeInput")
    def gpu_partition_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpuPartitionSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSize")
    def gpu_partition_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpuPartitionSize"))

    @gpu_partition_size.setter
    def gpu_partition_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference, "gpu_partition_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuPartitionSize", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigGuestAccelerator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigGuestAccelerator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigGuestAccelerator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGvnic",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterNodePoolNodeConfigGvnic:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGvnic.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not gvnic is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigGvnic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigGvnicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigGvnicOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigGvnicOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGvnicOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigGvnic]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigGvnic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfigGvnic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigGvnicOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodePoolNodeConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcfsConfig")
    def put_gcfs_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterNodePoolNodeConfigGcfsConfig(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGcfsConfig", [value]))

    @jsii.member(jsii_name="putGuestAccelerator")
    def put_guest_accelerator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterNodePoolNodeConfigGuestAccelerator, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigOutputReference.put_guest_accelerator)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestAccelerator", [value]))

    @jsii.member(jsii_name="putGvnic")
    def put_gvnic(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterNodePoolNodeConfigGvnic(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGvnic", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        value = ContainerClusterNodePoolNodeConfigReservationAffinity(
            consume_reservation_type=consume_reservation_type, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putReservationAffinity", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        value = ContainerClusterNodePoolNodeConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerClusterNodePoolNodeConfigTaint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigOutputReference.put_taint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="putWorkloadMetadataConfig")
    def put_workload_metadata_config(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        value = ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig(mode=mode)

        return typing.cast(None, jsii.invoke(self, "putWorkloadMetadataConfig", [value]))

    @jsii.member(jsii_name="resetBootDiskKmsKey")
    def reset_boot_disk_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskKmsKey", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetGcfsConfig")
    def reset_gcfs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcfsConfig", []))

    @jsii.member(jsii_name="resetGuestAccelerator")
    def reset_guest_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestAccelerator", []))

    @jsii.member(jsii_name="resetGvnic")
    def reset_gvnic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGvnic", []))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLocalSsdCount")
    def reset_local_ssd_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSsdCount", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNodeGroup")
    def reset_node_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeGroup", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetPreemptible")
    def reset_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptible", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetSpot")
    def reset_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpot", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaint")
    def reset_taint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaint", []))

    @jsii.member(jsii_name="resetWorkloadMetadataConfig")
    def reset_workload_metadata_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadMetadataConfig", []))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference:
        return typing.cast(ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference, jsii.get(self, "gcfsConfig"))

    @builtins.property
    @jsii.member(jsii_name="guestAccelerator")
    def guest_accelerator(
        self,
    ) -> ContainerClusterNodePoolNodeConfigGuestAcceleratorList:
        return typing.cast(ContainerClusterNodePoolNodeConfigGuestAcceleratorList, jsii.get(self, "guestAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="gvnic")
    def gvnic(self) -> ContainerClusterNodePoolNodeConfigGvnicOutputReference:
        return typing.cast(ContainerClusterNodePoolNodeConfigGvnicOutputReference, jsii.get(self, "gvnic"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference":
        return typing.cast("ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference":
        return typing.cast("ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "ContainerClusterNodePoolNodeConfigTaintList":
        return typing.cast("ContainerClusterNodePoolNodeConfigTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> "ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference":
        return typing.cast("ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference", jsii.get(self, "workloadMetadataConfig"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKeyInput")
    def boot_disk_kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskKmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfigInput")
    def gcfs_config_input(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigGcfsConfig], jsii.get(self, "gcfsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="guestAcceleratorInput")
    def guest_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigGuestAccelerator]]], jsii.get(self, "guestAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="gvnicInput")
    def gvnic_input(self) -> typing.Optional[ContainerClusterNodePoolNodeConfigGvnic]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigGvnic], jsii.get(self, "gvnicInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="localSsdCountInput")
    def local_ssd_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localSsdCountInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeGroupInput")
    def node_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleInput")
    def preemptible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigReservationAffinity"]:
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInput")
    def spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "spotInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigTaint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerClusterNodePoolNodeConfigTaint"]]], jsii.get(self, "taintInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfigInput")
    def workload_metadata_config_input(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig"]:
        return typing.cast(typing.Optional["ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig"], jsii.get(self, "workloadMetadataConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskKmsKey"))

    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "boot_disk_kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "image_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="localSsdCount")
    def local_ssd_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localSsdCount"))

    @local_ssd_count.setter
    def local_ssd_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "local_ssd_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localSsdCount", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="nodeGroup")
    def node_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeGroup"))

    @node_group.setter
    def node_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "node_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="preemptible")
    def preemptible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preemptible"))

    @preemptible.setter
    def preemptible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "spot"))

    @spot.setter
    def spot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spot", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNodePoolNodeConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "consume_reservation_type": "consumeReservationType",
        "key": "key",
        "values": "values",
    },
)
class ContainerClusterNodePoolNodeConfigReservationAffinity:
    def __init__(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigReservationAffinity.__init__)
            check_type(argname="argument consume_reservation_type", value=consume_reservation_type, expected_type=type_hints["consume_reservation_type"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "consume_reservation_type": consume_reservation_type,
        }
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def consume_reservation_type(self) -> builtins.str:
        '''Corresponds to the type of reservation consumption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#consume_reservation_type ContainerCluster#consume_reservation_type}
        '''
        result = self._values.get("consume_reservation_type")
        assert result is not None, "Required property 'consume_reservation_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key of a reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The label values of the reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#values ContainerCluster#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationTypeInput")
    def consume_reservation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumeReservationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationType")
    def consume_reservation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumeReservationType"))

    @consume_reservation_type.setter
    def consume_reservation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference, "consume_reservation_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumeReservationType", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigReservationAffinity]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfigReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
    },
)
class ContainerClusterNodePoolNodeConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has integrity monitoring enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_integrity_monitoring ContainerCluster#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has Secure Boot enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_secure_boot ContainerCluster#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class ContainerClusterNodePoolNodeConfigTaint:
    def __init__(
        self,
        *,
        effect: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param effect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#effect ContainerCluster#effect}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#value ContainerCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigTaint.__init__)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#effect ContainerCluster#effect}.'''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#key ContainerCluster#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#value ContainerCluster#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigTaintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigTaintList",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigTaintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerClusterNodePoolNodeConfigTaintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigTaintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerClusterNodePoolNodeConfigTaintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigTaint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigTaint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerClusterNodePoolNodeConfigTaint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodePoolNodeConfigTaintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigTaintOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigTaintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEffect")
    def reset_effect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffect", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintOutputReference, "effect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigTaint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigTaint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigTaint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigTaintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig:
    def __init__(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode is the configuration for how to expose metadata to workloads running on the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#mode ContainerCluster#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterNodePoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: Maximum number of nodes in the NodePool. Must be >= min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_node_count ContainerCluster#max_node_count}
        :param min_node_count: Minimum number of nodes in the NodePool. Must be >=0 and <= max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_node_count ContainerCluster#min_node_count}
        '''
        value = ContainerClusterNodePoolAutoscaling(
            max_node_count=max_node_count, min_node_count=min_node_count
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putManagement")
    def put_management(
        self,
        *,
        auto_repair: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param auto_repair: Whether the nodes will be automatically repaired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_repair ContainerCluster#auto_repair}
        :param auto_upgrade: Whether the nodes will be automatically upgraded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#auto_upgrade ContainerCluster#auto_upgrade}
        '''
        value = ContainerClusterNodePoolManagement(
            auto_repair=auto_repair, auto_upgrade=auto_upgrade
        )

        return typing.cast(None, jsii.invoke(self, "putManagement", [value]))

    @jsii.member(jsii_name="putNodeConfig")
    def put_node_config(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        gcfs_config: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigGcfsConfig, typing.Dict[str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterNodePoolNodeConfigGuestAccelerator, typing.Dict[str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigGvnic, typing.Dict[str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigReservationAffinity, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigShieldedInstanceConfig, typing.Dict[str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerClusterNodePoolNodeConfigTaint, typing.Dict[str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union[ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#boot_disk_kms_key ContainerCluster#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_size_gb ContainerCluster#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#disk_type ContainerCluster#disk_type}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gcfs_config ContainerCluster#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#guest_accelerator ContainerCluster#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#gvnic ContainerCluster#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#image_type ContainerCluster#image_type}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#labels ContainerCluster#labels}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#local_ssd_count ContainerCluster#local_ssd_count}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#machine_type ContainerCluster#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#metadata ContainerCluster#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#min_cpu_platform ContainerCluster#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#node_group ContainerCluster#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#oauth_scopes ContainerCluster#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#preemptible ContainerCluster#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#reservation_affinity ContainerCluster#reservation_affinity}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#service_account ContainerCluster#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#shielded_instance_config ContainerCluster#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#spot ContainerCluster#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#tags ContainerCluster#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#taint ContainerCluster#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_metadata_config ContainerCluster#workload_metadata_config}
        '''
        value = ContainerClusterNodePoolNodeConfig(
            boot_disk_kms_key=boot_disk_kms_key,
            disk_size_gb=disk_size_gb,
            disk_type=disk_type,
            gcfs_config=gcfs_config,
            guest_accelerator=guest_accelerator,
            gvnic=gvnic,
            image_type=image_type,
            labels=labels,
            local_ssd_count=local_ssd_count,
            machine_type=machine_type,
            metadata=metadata,
            min_cpu_platform=min_cpu_platform,
            node_group=node_group,
            oauth_scopes=oauth_scopes,
            preemptible=preemptible,
            reservation_affinity=reservation_affinity,
            service_account=service_account,
            shielded_instance_config=shielded_instance_config,
            spot=spot,
            tags=tags,
            taint=taint,
            workload_metadata_config=workload_metadata_config,
        )

        return typing.cast(None, jsii.invoke(self, "putNodeConfig", [value]))

    @jsii.member(jsii_name="putUpgradeSettings")
    def put_upgrade_settings(
        self,
        *,
        max_surge: jsii.Number,
        max_unavailable: jsii.Number,
    ) -> None:
        '''
        :param max_surge: The number of additional nodes that can be added to the node pool during an upgrade. Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_surge ContainerCluster#max_surge}
        :param max_unavailable: The number of nodes that can be simultaneously unavailable during an upgrade. Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_unavailable ContainerCluster#max_unavailable}
        '''
        value = ContainerClusterNodePoolUpgradeSettings(
            max_surge=max_surge, max_unavailable=max_unavailable
        )

        return typing.cast(None, jsii.invoke(self, "putUpgradeSettings", [value]))

    @jsii.member(jsii_name="resetAutoscaling")
    def reset_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaling", []))

    @jsii.member(jsii_name="resetInitialNodeCount")
    def reset_initial_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialNodeCount", []))

    @jsii.member(jsii_name="resetManagement")
    def reset_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagement", []))

    @jsii.member(jsii_name="resetMaxPodsPerNode")
    def reset_max_pods_per_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPodsPerNode", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNodeConfig")
    def reset_node_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeConfig", []))

    @jsii.member(jsii_name="resetNodeCount")
    def reset_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeCount", []))

    @jsii.member(jsii_name="resetNodeLocations")
    def reset_node_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeLocations", []))

    @jsii.member(jsii_name="resetUpgradeSettings")
    def reset_upgrade_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeSettings", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(self) -> ContainerClusterNodePoolAutoscalingOutputReference:
        return typing.cast(ContainerClusterNodePoolAutoscalingOutputReference, jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="instanceGroupUrls")
    def instance_group_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceGroupUrls"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceGroupUrls")
    def managed_instance_group_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "managedInstanceGroupUrls"))

    @builtins.property
    @jsii.member(jsii_name="management")
    def management(self) -> ContainerClusterNodePoolManagementOutputReference:
        return typing.cast(ContainerClusterNodePoolManagementOutputReference, jsii.get(self, "management"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfig")
    def node_config(self) -> ContainerClusterNodePoolNodeConfigOutputReference:
        return typing.cast(ContainerClusterNodePoolNodeConfigOutputReference, jsii.get(self, "nodeConfig"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> "ContainerClusterNodePoolUpgradeSettingsOutputReference":
        return typing.cast("ContainerClusterNodePoolUpgradeSettingsOutputReference", jsii.get(self, "upgradeSettings"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(self) -> typing.Optional[ContainerClusterNodePoolAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolAutoscaling], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="initialNodeCountInput")
    def initial_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="managementInput")
    def management_input(self) -> typing.Optional[ContainerClusterNodePoolManagement]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolManagement], jsii.get(self, "managementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNodeInput")
    def max_pods_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfigInput")
    def node_config_input(self) -> typing.Optional[ContainerClusterNodePoolNodeConfig]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolNodeConfig], jsii.get(self, "nodeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeLocationsInput")
    def node_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodeLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettingsInput")
    def upgrade_settings_input(
        self,
    ) -> typing.Optional["ContainerClusterNodePoolUpgradeSettings"]:
        return typing.cast(typing.Optional["ContainerClusterNodePoolUpgradeSettings"], jsii.get(self, "upgradeSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="initialNodeCount")
    def initial_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialNodeCount"))

    @initial_node_count.setter
    def initial_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "initial_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNode")
    def max_pods_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPodsPerNode"))

    @max_pods_per_node.setter
    def max_pods_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "max_pods_per_node").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPodsPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="nodeLocations")
    def node_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeLocations"))

    @node_locations.setter
    def node_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "node_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeLocations", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterNodePool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterNodePool, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterNodePool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolUpgradeSettings",
    jsii_struct_bases=[],
    name_mapping={"max_surge": "maxSurge", "max_unavailable": "maxUnavailable"},
)
class ContainerClusterNodePoolUpgradeSettings:
    def __init__(self, *, max_surge: jsii.Number, max_unavailable: jsii.Number) -> None:
        '''
        :param max_surge: The number of additional nodes that can be added to the node pool during an upgrade. Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_surge ContainerCluster#max_surge}
        :param max_unavailable: The number of nodes that can be simultaneously unavailable during an upgrade. Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_unavailable ContainerCluster#max_unavailable}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNodePoolUpgradeSettings.__init__)
            check_type(argname="argument max_surge", value=max_surge, expected_type=type_hints["max_surge"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_surge": max_surge,
            "max_unavailable": max_unavailable,
        }

    @builtins.property
    def max_surge(self) -> jsii.Number:
        '''The number of additional nodes that can be added to the node pool during an upgrade.

        Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_surge ContainerCluster#max_surge}
        '''
        result = self._values.get("max_surge")
        assert result is not None, "Required property 'max_surge' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_unavailable(self) -> jsii.Number:
        '''The number of nodes that can be simultaneously unavailable during an upgrade.

        Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#max_unavailable ContainerCluster#max_unavailable}
        '''
        result = self._values.get("max_unavailable")
        assert result is not None, "Required property 'max_unavailable' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNodePoolUpgradeSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNodePoolUpgradeSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNodePoolUpgradeSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNodePoolUpgradeSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxSurgeInput")
    def max_surge_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSurgeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnavailableInput")
    def max_unavailable_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnavailableInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSurge")
    def max_surge(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSurge"))

    @max_surge.setter
    def max_surge(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolUpgradeSettingsOutputReference, "max_surge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSurge", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnavailable")
    def max_unavailable(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnavailable"))

    @max_unavailable.setter
    def max_unavailable(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolUpgradeSettingsOutputReference, "max_unavailable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnavailable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNodePoolUpgradeSettings]:
        return typing.cast(typing.Optional[ContainerClusterNodePoolUpgradeSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNodePoolUpgradeSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNodePoolUpgradeSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNotificationConfig",
    jsii_struct_bases=[],
    name_mapping={"pubsub": "pubsub"},
)
class ContainerClusterNotificationConfig:
    def __init__(
        self,
        *,
        pubsub: typing.Union["ContainerClusterNotificationConfigPubsub", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param pubsub: pubsub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#pubsub ContainerCluster#pubsub}
        '''
        if isinstance(pubsub, dict):
            pubsub = ContainerClusterNotificationConfigPubsub(**pubsub)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNotificationConfig.__init__)
            check_type(argname="argument pubsub", value=pubsub, expected_type=type_hints["pubsub"])
        self._values: typing.Dict[str, typing.Any] = {
            "pubsub": pubsub,
        }

    @builtins.property
    def pubsub(self) -> "ContainerClusterNotificationConfigPubsub":
        '''pubsub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#pubsub ContainerCluster#pubsub}
        '''
        result = self._values.get("pubsub")
        assert result is not None, "Required property 'pubsub' is missing"
        return typing.cast("ContainerClusterNotificationConfigPubsub", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNotificationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNotificationConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNotificationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPubsub")
    def put_pubsub(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether or not the notification config is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param topic: The pubsub topic to push upgrade notifications to. Must be in the same project as the cluster. Must be in the format: projects/{project}/topics/{topic}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#topic ContainerCluster#topic}
        '''
        value = ContainerClusterNotificationConfigPubsub(enabled=enabled, topic=topic)

        return typing.cast(None, jsii.invoke(self, "putPubsub", [value]))

    @builtins.property
    @jsii.member(jsii_name="pubsub")
    def pubsub(self) -> "ContainerClusterNotificationConfigPubsubOutputReference":
        return typing.cast("ContainerClusterNotificationConfigPubsubOutputReference", jsii.get(self, "pubsub"))

    @builtins.property
    @jsii.member(jsii_name="pubsubInput")
    def pubsub_input(
        self,
    ) -> typing.Optional["ContainerClusterNotificationConfigPubsub"]:
        return typing.cast(typing.Optional["ContainerClusterNotificationConfigPubsub"], jsii.get(self, "pubsubInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterNotificationConfig]:
        return typing.cast(typing.Optional[ContainerClusterNotificationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNotificationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNotificationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNotificationConfigPubsub",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "topic": "topic"},
)
class ContainerClusterNotificationConfigPubsub:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether or not the notification config is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        :param topic: The pubsub topic to push upgrade notifications to. Must be in the same project as the cluster. Must be in the format: projects/{project}/topics/{topic}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#topic ContainerCluster#topic}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterNotificationConfigPubsub.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether or not the notification config is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''The pubsub topic to push upgrade notifications to.

        Must be in the same project as the cluster. Must be in the format: projects/{project}/topics/{topic}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#topic ContainerCluster#topic}
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterNotificationConfigPubsub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterNotificationConfigPubsubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterNotificationConfigPubsubOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterNotificationConfigPubsubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTopic")
    def reset_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopic", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNotificationConfigPubsubOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNotificationConfigPubsubOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterNotificationConfigPubsub]:
        return typing.cast(typing.Optional[ContainerClusterNotificationConfigPubsub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterNotificationConfigPubsub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterNotificationConfigPubsubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterPrivateClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_private_endpoint": "enablePrivateEndpoint",
        "enable_private_nodes": "enablePrivateNodes",
        "master_global_access_config": "masterGlobalAccessConfig",
        "master_ipv4_cidr_block": "masterIpv4CidrBlock",
    },
)
class ContainerClusterPrivateClusterConfig:
    def __init__(
        self,
        *,
        enable_private_endpoint: typing.Union[builtins.bool, cdktf.IResolvable],
        enable_private_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_global_access_config: typing.Optional[typing.Union["ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig", typing.Dict[str, typing.Any]]] = None,
        master_ipv4_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_private_endpoint: When true, the cluster's private endpoint is used as the cluster endpoint and access through the public endpoint is disabled. When false, either endpoint can be used. This field only applies to private clusters, when enable_private_nodes is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_endpoint ContainerCluster#enable_private_endpoint}
        :param enable_private_nodes: Enables the private cluster feature, creating a private endpoint on the cluster. In a private cluster, nodes only have RFC 1918 private addresses and communicate with the master's private endpoint via private networking. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_nodes ContainerCluster#enable_private_nodes}
        :param master_global_access_config: master_global_access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_global_access_config ContainerCluster#master_global_access_config}
        :param master_ipv4_cidr_block: The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning private IP addresses to the cluster master(s) and the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network, and it must be a /28 subnet. See Private Cluster Limitations for more details. This field only applies to private clusters, when enable_private_nodes is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_ipv4_cidr_block ContainerCluster#master_ipv4_cidr_block}
        '''
        if isinstance(master_global_access_config, dict):
            master_global_access_config = ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig(**master_global_access_config)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterPrivateClusterConfig.__init__)
            check_type(argname="argument enable_private_endpoint", value=enable_private_endpoint, expected_type=type_hints["enable_private_endpoint"])
            check_type(argname="argument enable_private_nodes", value=enable_private_nodes, expected_type=type_hints["enable_private_nodes"])
            check_type(argname="argument master_global_access_config", value=master_global_access_config, expected_type=type_hints["master_global_access_config"])
            check_type(argname="argument master_ipv4_cidr_block", value=master_ipv4_cidr_block, expected_type=type_hints["master_ipv4_cidr_block"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_private_endpoint": enable_private_endpoint,
        }
        if enable_private_nodes is not None:
            self._values["enable_private_nodes"] = enable_private_nodes
        if master_global_access_config is not None:
            self._values["master_global_access_config"] = master_global_access_config
        if master_ipv4_cidr_block is not None:
            self._values["master_ipv4_cidr_block"] = master_ipv4_cidr_block

    @builtins.property
    def enable_private_endpoint(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, the cluster's private endpoint is used as the cluster endpoint and access through the public endpoint is disabled.

        When false, either endpoint can be used. This field only applies to private clusters, when enable_private_nodes is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_endpoint ContainerCluster#enable_private_endpoint}
        '''
        result = self._values.get("enable_private_endpoint")
        assert result is not None, "Required property 'enable_private_endpoint' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def enable_private_nodes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables the private cluster feature, creating a private endpoint on the cluster.

        In a private cluster, nodes only have RFC 1918 private addresses and communicate with the master's private endpoint via private networking.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_private_nodes ContainerCluster#enable_private_nodes}
        '''
        result = self._values.get("enable_private_nodes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def master_global_access_config(
        self,
    ) -> typing.Optional["ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig"]:
        '''master_global_access_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_global_access_config ContainerCluster#master_global_access_config}
        '''
        result = self._values.get("master_global_access_config")
        return typing.cast(typing.Optional["ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig"], result)

    @builtins.property
    def master_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The IP range in CIDR notation to use for the hosted master network.

        This range will be used for assigning private IP addresses to the cluster master(s) and the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network, and it must be a /28 subnet. See Private Cluster Limitations for more details. This field only applies to private clusters, when enable_private_nodes is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#master_ipv4_cidr_block ContainerCluster#master_ipv4_cidr_block}
        '''
        result = self._values.get("master_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterPrivateClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether the cluster master is accessible globally or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether the cluster master is accessible globally or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig]:
        return typing.cast(typing.Optional[ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterPrivateClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterPrivateClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterPrivateClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMasterGlobalAccessConfig")
    def put_master_global_access_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether the cluster master is accessible globally or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        value = ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putMasterGlobalAccessConfig", [value]))

    @jsii.member(jsii_name="resetEnablePrivateNodes")
    def reset_enable_private_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePrivateNodes", []))

    @jsii.member(jsii_name="resetMasterGlobalAccessConfig")
    def reset_master_global_access_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterGlobalAccessConfig", []))

    @jsii.member(jsii_name="resetMasterIpv4CidrBlock")
    def reset_master_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterIpv4CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="masterGlobalAccessConfig")
    def master_global_access_config(
        self,
    ) -> ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference:
        return typing.cast(ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference, jsii.get(self, "masterGlobalAccessConfig"))

    @builtins.property
    @jsii.member(jsii_name="peeringName")
    def peering_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peeringName"))

    @builtins.property
    @jsii.member(jsii_name="privateEndpoint")
    def private_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="enablePrivateEndpointInput")
    def enable_private_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePrivateEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePrivateNodesInput")
    def enable_private_nodes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePrivateNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="masterGlobalAccessConfigInput")
    def master_global_access_config_input(
        self,
    ) -> typing.Optional[ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig]:
        return typing.cast(typing.Optional[ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig], jsii.get(self, "masterGlobalAccessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="masterIpv4CidrBlockInput")
    def master_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterIpv4CidrBlockInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigOutputReference, "enable_private_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePrivateEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="enablePrivateNodes")
    def enable_private_nodes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePrivateNodes"))

    @enable_private_nodes.setter
    def enable_private_nodes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigOutputReference, "enable_private_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePrivateNodes", value)

    @builtins.property
    @jsii.member(jsii_name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterIpv4CidrBlock"))

    @master_ipv4_cidr_block.setter
    def master_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigOutputReference, "master_ipv4_cidr_block").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterPrivateClusterConfig]:
        return typing.cast(typing.Optional[ContainerClusterPrivateClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterPrivateClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterPrivateClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterReleaseChannel",
    jsii_struct_bases=[],
    name_mapping={"channel": "channel"},
)
class ContainerClusterReleaseChannel:
    def __init__(self, *, channel: builtins.str) -> None:
        '''
        :param channel: The selected release channel. Accepted values are: UNSPECIFIED: Not set. RAPID: Weekly upgrade cadence; Early testers and developers who requires new features. REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel. STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#channel ContainerCluster#channel}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterReleaseChannel.__init__)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
        self._values: typing.Dict[str, typing.Any] = {
            "channel": channel,
        }

    @builtins.property
    def channel(self) -> builtins.str:
        '''The selected release channel.

        Accepted values are:
        UNSPECIFIED: Not set.
        RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
        REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
        STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#channel ContainerCluster#channel}
        '''
        result = self._values.get("channel")
        assert result is not None, "Required property 'channel' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterReleaseChannel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterReleaseChannelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterReleaseChannelOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterReleaseChannelOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterReleaseChannelOutputReference, "channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterReleaseChannel]:
        return typing.cast(typing.Optional[ContainerClusterReleaseChannel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterReleaseChannel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterReleaseChannelOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterResourceUsageExportConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bigquery_destination": "bigqueryDestination",
        "enable_network_egress_metering": "enableNetworkEgressMetering",
        "enable_resource_consumption_metering": "enableResourceConsumptionMetering",
    },
)
class ContainerClusterResourceUsageExportConfig:
    def __init__(
        self,
        *,
        bigquery_destination: typing.Union["ContainerClusterResourceUsageExportConfigBigqueryDestination", typing.Dict[str, typing.Any]],
        enable_network_egress_metering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_resource_consumption_metering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bigquery_destination: bigquery_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#bigquery_destination ContainerCluster#bigquery_destination}
        :param enable_network_egress_metering: Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created in the cluster to meter network egress traffic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_network_egress_metering ContainerCluster#enable_network_egress_metering}
        :param enable_resource_consumption_metering: Whether to enable resource consumption metering on this cluster. When enabled, a table will be created in the resource export BigQuery dataset to store resource consumption data. The resulting table can be joined with the resource usage table or with BigQuery billing export. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_resource_consumption_metering ContainerCluster#enable_resource_consumption_metering}
        '''
        if isinstance(bigquery_destination, dict):
            bigquery_destination = ContainerClusterResourceUsageExportConfigBigqueryDestination(**bigquery_destination)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterResourceUsageExportConfig.__init__)
            check_type(argname="argument bigquery_destination", value=bigquery_destination, expected_type=type_hints["bigquery_destination"])
            check_type(argname="argument enable_network_egress_metering", value=enable_network_egress_metering, expected_type=type_hints["enable_network_egress_metering"])
            check_type(argname="argument enable_resource_consumption_metering", value=enable_resource_consumption_metering, expected_type=type_hints["enable_resource_consumption_metering"])
        self._values: typing.Dict[str, typing.Any] = {
            "bigquery_destination": bigquery_destination,
        }
        if enable_network_egress_metering is not None:
            self._values["enable_network_egress_metering"] = enable_network_egress_metering
        if enable_resource_consumption_metering is not None:
            self._values["enable_resource_consumption_metering"] = enable_resource_consumption_metering

    @builtins.property
    def bigquery_destination(
        self,
    ) -> "ContainerClusterResourceUsageExportConfigBigqueryDestination":
        '''bigquery_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#bigquery_destination ContainerCluster#bigquery_destination}
        '''
        result = self._values.get("bigquery_destination")
        assert result is not None, "Required property 'bigquery_destination' is missing"
        return typing.cast("ContainerClusterResourceUsageExportConfigBigqueryDestination", result)

    @builtins.property
    def enable_network_egress_metering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable network egress metering for this cluster.

        If enabled, a daemonset will be created in the cluster to meter network egress traffic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_network_egress_metering ContainerCluster#enable_network_egress_metering}
        '''
        result = self._values.get("enable_network_egress_metering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_resource_consumption_metering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable resource consumption metering on this cluster.

        When enabled, a table will be created in the resource export BigQuery dataset to store resource consumption data. The resulting table can be joined with the resource usage table or with BigQuery billing export. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enable_resource_consumption_metering ContainerCluster#enable_resource_consumption_metering}
        '''
        result = self._values.get("enable_resource_consumption_metering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterResourceUsageExportConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterResourceUsageExportConfigBigqueryDestination",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId"},
)
class ContainerClusterResourceUsageExportConfigBigqueryDestination:
    def __init__(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: The ID of a BigQuery Dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dataset_id ContainerCluster#dataset_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterResourceUsageExportConfigBigqueryDestination.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of a BigQuery Dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dataset_id ContainerCluster#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterResourceUsageExportConfigBigqueryDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterResourceUsageExportConfigBigqueryDestination]:
        return typing.cast(typing.Optional[ContainerClusterResourceUsageExportConfigBigqueryDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterResourceUsageExportConfigBigqueryDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerClusterResourceUsageExportConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterResourceUsageExportConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterResourceUsageExportConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigqueryDestination")
    def put_bigquery_destination(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: The ID of a BigQuery Dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#dataset_id ContainerCluster#dataset_id}
        '''
        value = ContainerClusterResourceUsageExportConfigBigqueryDestination(
            dataset_id=dataset_id
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryDestination", [value]))

    @jsii.member(jsii_name="resetEnableNetworkEgressMetering")
    def reset_enable_network_egress_metering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNetworkEgressMetering", []))

    @jsii.member(jsii_name="resetEnableResourceConsumptionMetering")
    def reset_enable_resource_consumption_metering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableResourceConsumptionMetering", []))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference:
        return typing.cast(ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference, jsii.get(self, "bigqueryDestination"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationInput")
    def bigquery_destination_input(
        self,
    ) -> typing.Optional[ContainerClusterResourceUsageExportConfigBigqueryDestination]:
        return typing.cast(typing.Optional[ContainerClusterResourceUsageExportConfigBigqueryDestination], jsii.get(self, "bigqueryDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNetworkEgressMeteringInput")
    def enable_network_egress_metering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableNetworkEgressMeteringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableResourceConsumptionMeteringInput")
    def enable_resource_consumption_metering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableResourceConsumptionMeteringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNetworkEgressMetering")
    def enable_network_egress_metering(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableNetworkEgressMetering"))

    @enable_network_egress_metering.setter
    def enable_network_egress_metering(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterResourceUsageExportConfigOutputReference, "enable_network_egress_metering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNetworkEgressMetering", value)

    @builtins.property
    @jsii.member(jsii_name="enableResourceConsumptionMetering")
    def enable_resource_consumption_metering(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableResourceConsumptionMetering"))

    @enable_resource_consumption_metering.setter
    def enable_resource_consumption_metering(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterResourceUsageExportConfigOutputReference, "enable_resource_consumption_metering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableResourceConsumptionMetering", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterResourceUsageExportConfig]:
        return typing.cast(typing.Optional[ContainerClusterResourceUsageExportConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterResourceUsageExportConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterResourceUsageExportConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterServiceExternalIpsConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterServiceExternalIpsConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: When enabled, services with exterenal ips specified will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterServiceExternalIpsConfig.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When enabled, services with exterenal ips specified will be allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterServiceExternalIpsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterServiceExternalIpsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterServiceExternalIpsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterServiceExternalIpsConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterServiceExternalIpsConfigOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerClusterServiceExternalIpsConfig]:
        return typing.cast(typing.Optional[ContainerClusterServiceExternalIpsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterServiceExternalIpsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterServiceExternalIpsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ContainerClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#create ContainerCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#delete ContainerCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#read ContainerCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#update ContainerCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#create ContainerCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#delete ContainerCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#read ContainerCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#update ContainerCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterVerticalPodAutoscaling",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ContainerClusterVerticalPodAutoscaling:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Enables vertical pod autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterVerticalPodAutoscaling.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Enables vertical pod autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#enabled ContainerCluster#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterVerticalPodAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterVerticalPodAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterVerticalPodAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterVerticalPodAutoscalingOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerClusterVerticalPodAutoscalingOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterVerticalPodAutoscaling]:
        return typing.cast(typing.Optional[ContainerClusterVerticalPodAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterVerticalPodAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterVerticalPodAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterWorkloadIdentityConfig",
    jsii_struct_bases=[],
    name_mapping={"workload_pool": "workloadPool"},
)
class ContainerClusterWorkloadIdentityConfig:
    def __init__(self, *, workload_pool: typing.Optional[builtins.str] = None) -> None:
        '''
        :param workload_pool: The workload pool to attach all Kubernetes service accounts to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_pool ContainerCluster#workload_pool}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerClusterWorkloadIdentityConfig.__init__)
            check_type(argname="argument workload_pool", value=workload_pool, expected_type=type_hints["workload_pool"])
        self._values: typing.Dict[str, typing.Any] = {}
        if workload_pool is not None:
            self._values["workload_pool"] = workload_pool

    @builtins.property
    def workload_pool(self) -> typing.Optional[builtins.str]:
        '''The workload pool to attach all Kubernetes service accounts to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/container_cluster#workload_pool ContainerCluster#workload_pool}
        '''
        result = self._values.get("workload_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerClusterWorkloadIdentityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerClusterWorkloadIdentityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.containerCluster.ContainerClusterWorkloadIdentityConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerClusterWorkloadIdentityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWorkloadPool")
    def reset_workload_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadPool", []))

    @builtins.property
    @jsii.member(jsii_name="workloadPoolInput")
    def workload_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workloadPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadPool")
    def workload_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workloadPool"))

    @workload_pool.setter
    def workload_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterWorkloadIdentityConfigOutputReference, "workload_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadPool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerClusterWorkloadIdentityConfig]:
        return typing.cast(typing.Optional[ContainerClusterWorkloadIdentityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerClusterWorkloadIdentityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerClusterWorkloadIdentityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContainerCluster",
    "ContainerClusterAddonsConfig",
    "ContainerClusterAddonsConfigCloudrunConfig",
    "ContainerClusterAddonsConfigCloudrunConfigOutputReference",
    "ContainerClusterAddonsConfigDnsCacheConfig",
    "ContainerClusterAddonsConfigDnsCacheConfigOutputReference",
    "ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfig",
    "ContainerClusterAddonsConfigGcePersistentDiskCsiDriverConfigOutputReference",
    "ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfig",
    "ContainerClusterAddonsConfigGcpFilestoreCsiDriverConfigOutputReference",
    "ContainerClusterAddonsConfigHorizontalPodAutoscaling",
    "ContainerClusterAddonsConfigHorizontalPodAutoscalingOutputReference",
    "ContainerClusterAddonsConfigHttpLoadBalancing",
    "ContainerClusterAddonsConfigHttpLoadBalancingOutputReference",
    "ContainerClusterAddonsConfigNetworkPolicyConfig",
    "ContainerClusterAddonsConfigNetworkPolicyConfigOutputReference",
    "ContainerClusterAddonsConfigOutputReference",
    "ContainerClusterAuthenticatorGroupsConfig",
    "ContainerClusterAuthenticatorGroupsConfigOutputReference",
    "ContainerClusterBinaryAuthorization",
    "ContainerClusterBinaryAuthorizationOutputReference",
    "ContainerClusterClusterAutoscaling",
    "ContainerClusterClusterAutoscalingAutoProvisioningDefaults",
    "ContainerClusterClusterAutoscalingAutoProvisioningDefaultsOutputReference",
    "ContainerClusterClusterAutoscalingOutputReference",
    "ContainerClusterClusterAutoscalingResourceLimits",
    "ContainerClusterClusterAutoscalingResourceLimitsList",
    "ContainerClusterClusterAutoscalingResourceLimitsOutputReference",
    "ContainerClusterConfidentialNodes",
    "ContainerClusterConfidentialNodesOutputReference",
    "ContainerClusterConfig",
    "ContainerClusterDatabaseEncryption",
    "ContainerClusterDatabaseEncryptionOutputReference",
    "ContainerClusterDefaultSnatStatus",
    "ContainerClusterDefaultSnatStatusOutputReference",
    "ContainerClusterDnsConfig",
    "ContainerClusterDnsConfigOutputReference",
    "ContainerClusterIpAllocationPolicy",
    "ContainerClusterIpAllocationPolicyOutputReference",
    "ContainerClusterLoggingConfig",
    "ContainerClusterLoggingConfigOutputReference",
    "ContainerClusterMaintenancePolicy",
    "ContainerClusterMaintenancePolicyDailyMaintenanceWindow",
    "ContainerClusterMaintenancePolicyDailyMaintenanceWindowOutputReference",
    "ContainerClusterMaintenancePolicyMaintenanceExclusion",
    "ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptions",
    "ContainerClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsOutputReference",
    "ContainerClusterMaintenancePolicyMaintenanceExclusionList",
    "ContainerClusterMaintenancePolicyMaintenanceExclusionOutputReference",
    "ContainerClusterMaintenancePolicyOutputReference",
    "ContainerClusterMaintenancePolicyRecurringWindow",
    "ContainerClusterMaintenancePolicyRecurringWindowOutputReference",
    "ContainerClusterMasterAuth",
    "ContainerClusterMasterAuthClientCertificateConfig",
    "ContainerClusterMasterAuthClientCertificateConfigOutputReference",
    "ContainerClusterMasterAuthOutputReference",
    "ContainerClusterMasterAuthorizedNetworksConfig",
    "ContainerClusterMasterAuthorizedNetworksConfigCidrBlocks",
    "ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksList",
    "ContainerClusterMasterAuthorizedNetworksConfigCidrBlocksOutputReference",
    "ContainerClusterMasterAuthorizedNetworksConfigOutputReference",
    "ContainerClusterMeshCertificates",
    "ContainerClusterMeshCertificatesOutputReference",
    "ContainerClusterMonitoringConfig",
    "ContainerClusterMonitoringConfigOutputReference",
    "ContainerClusterNetworkPolicy",
    "ContainerClusterNetworkPolicyOutputReference",
    "ContainerClusterNodeConfig",
    "ContainerClusterNodeConfigGcfsConfig",
    "ContainerClusterNodeConfigGcfsConfigOutputReference",
    "ContainerClusterNodeConfigGuestAccelerator",
    "ContainerClusterNodeConfigGuestAcceleratorList",
    "ContainerClusterNodeConfigGuestAcceleratorOutputReference",
    "ContainerClusterNodeConfigGvnic",
    "ContainerClusterNodeConfigGvnicOutputReference",
    "ContainerClusterNodeConfigOutputReference",
    "ContainerClusterNodeConfigReservationAffinity",
    "ContainerClusterNodeConfigReservationAffinityOutputReference",
    "ContainerClusterNodeConfigShieldedInstanceConfig",
    "ContainerClusterNodeConfigShieldedInstanceConfigOutputReference",
    "ContainerClusterNodeConfigTaint",
    "ContainerClusterNodeConfigTaintList",
    "ContainerClusterNodeConfigTaintOutputReference",
    "ContainerClusterNodeConfigWorkloadMetadataConfig",
    "ContainerClusterNodeConfigWorkloadMetadataConfigOutputReference",
    "ContainerClusterNodePool",
    "ContainerClusterNodePoolAutoscaling",
    "ContainerClusterNodePoolAutoscalingOutputReference",
    "ContainerClusterNodePoolList",
    "ContainerClusterNodePoolManagement",
    "ContainerClusterNodePoolManagementOutputReference",
    "ContainerClusterNodePoolNodeConfig",
    "ContainerClusterNodePoolNodeConfigGcfsConfig",
    "ContainerClusterNodePoolNodeConfigGcfsConfigOutputReference",
    "ContainerClusterNodePoolNodeConfigGuestAccelerator",
    "ContainerClusterNodePoolNodeConfigGuestAcceleratorList",
    "ContainerClusterNodePoolNodeConfigGuestAcceleratorOutputReference",
    "ContainerClusterNodePoolNodeConfigGvnic",
    "ContainerClusterNodePoolNodeConfigGvnicOutputReference",
    "ContainerClusterNodePoolNodeConfigOutputReference",
    "ContainerClusterNodePoolNodeConfigReservationAffinity",
    "ContainerClusterNodePoolNodeConfigReservationAffinityOutputReference",
    "ContainerClusterNodePoolNodeConfigShieldedInstanceConfig",
    "ContainerClusterNodePoolNodeConfigShieldedInstanceConfigOutputReference",
    "ContainerClusterNodePoolNodeConfigTaint",
    "ContainerClusterNodePoolNodeConfigTaintList",
    "ContainerClusterNodePoolNodeConfigTaintOutputReference",
    "ContainerClusterNodePoolNodeConfigWorkloadMetadataConfig",
    "ContainerClusterNodePoolNodeConfigWorkloadMetadataConfigOutputReference",
    "ContainerClusterNodePoolOutputReference",
    "ContainerClusterNodePoolUpgradeSettings",
    "ContainerClusterNodePoolUpgradeSettingsOutputReference",
    "ContainerClusterNotificationConfig",
    "ContainerClusterNotificationConfigOutputReference",
    "ContainerClusterNotificationConfigPubsub",
    "ContainerClusterNotificationConfigPubsubOutputReference",
    "ContainerClusterPrivateClusterConfig",
    "ContainerClusterPrivateClusterConfigMasterGlobalAccessConfig",
    "ContainerClusterPrivateClusterConfigMasterGlobalAccessConfigOutputReference",
    "ContainerClusterPrivateClusterConfigOutputReference",
    "ContainerClusterReleaseChannel",
    "ContainerClusterReleaseChannelOutputReference",
    "ContainerClusterResourceUsageExportConfig",
    "ContainerClusterResourceUsageExportConfigBigqueryDestination",
    "ContainerClusterResourceUsageExportConfigBigqueryDestinationOutputReference",
    "ContainerClusterResourceUsageExportConfigOutputReference",
    "ContainerClusterServiceExternalIpsConfig",
    "ContainerClusterServiceExternalIpsConfigOutputReference",
    "ContainerClusterTimeouts",
    "ContainerClusterTimeoutsOutputReference",
    "ContainerClusterVerticalPodAutoscaling",
    "ContainerClusterVerticalPodAutoscalingOutputReference",
    "ContainerClusterWorkloadIdentityConfig",
    "ContainerClusterWorkloadIdentityConfigOutputReference",
]

publication.publish()
