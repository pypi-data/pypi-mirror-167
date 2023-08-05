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


class DataprocCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster google_dataproc_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        cluster_config: typing.Optional[typing.Union["DataprocClusterClusterConfig", typing.Dict[str, typing.Any]]] = None,
        graceful_decommission_timeout: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataprocClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_cluster_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster google_dataproc_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the cluster, unique within the project and zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#name DataprocCluster#name}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cluster_config DataprocCluster#cluster_config}
        :param graceful_decommission_timeout: The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a terraform apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#graceful_decommission_timeout DataprocCluster#graceful_decommission_timeout}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#id DataprocCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The list of labels (key/value pairs) to be applied to instances in the cluster. GCP generates some itself including goog-dataproc-cluster-name which is the name of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#labels DataprocCluster#labels}
        :param project: The ID of the project in which the cluster will exist. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#project DataprocCluster#project}
        :param region: The region in which the cluster and associated nodes will be created in. Defaults to global. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#region DataprocCluster#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#timeouts DataprocCluster#timeouts}
        :param virtual_cluster_config: virtual_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#virtual_cluster_config DataprocCluster#virtual_cluster_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataprocClusterConfig(
            name=name,
            cluster_config=cluster_config,
            graceful_decommission_timeout=graceful_decommission_timeout,
            id=id,
            labels=labels,
            project=project,
            region=region,
            timeouts=timeouts,
            virtual_cluster_config=virtual_cluster_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putClusterConfig")
    def put_cluster_config(
        self,
        *,
        autoscaling_config: typing.Optional[typing.Union["DataprocClusterClusterConfigAutoscalingConfig", typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union["DataprocClusterClusterConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        endpoint_config: typing.Optional[typing.Union["DataprocClusterClusterConfigEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        gce_cluster_config: typing.Optional[typing.Union["DataprocClusterClusterConfigGceClusterConfig", typing.Dict[str, typing.Any]]] = None,
        initialization_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterClusterConfigInitializationAction", typing.Dict[str, typing.Any]]]]] = None,
        lifecycle_config: typing.Optional[typing.Union["DataprocClusterClusterConfigLifecycleConfig", typing.Dict[str, typing.Any]]] = None,
        master_config: typing.Optional[typing.Union["DataprocClusterClusterConfigMasterConfig", typing.Dict[str, typing.Any]]] = None,
        metastore_config: typing.Optional[typing.Union["DataprocClusterClusterConfigMetastoreConfig", typing.Dict[str, typing.Any]]] = None,
        preemptible_worker_config: typing.Optional[typing.Union["DataprocClusterClusterConfigPreemptibleWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        security_config: typing.Optional[typing.Union["DataprocClusterClusterConfigSecurityConfig", typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union["DataprocClusterClusterConfigSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
        temp_bucket: typing.Optional[builtins.str] = None,
        worker_config: typing.Optional[typing.Union["DataprocClusterClusterConfigWorkerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling_config: autoscaling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling_config DataprocCluster#autoscaling_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#encryption_config DataprocCluster#encryption_config}
        :param endpoint_config: endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#endpoint_config DataprocCluster#endpoint_config}
        :param gce_cluster_config: gce_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gce_cluster_config DataprocCluster#gce_cluster_config}
        :param initialization_action: initialization_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#initialization_action DataprocCluster#initialization_action}
        :param lifecycle_config: lifecycle_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#lifecycle_config DataprocCluster#lifecycle_config}
        :param master_config: master_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#master_config DataprocCluster#master_config}
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        :param preemptible_worker_config: preemptible_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible_worker_config DataprocCluster#preemptible_worker_config}
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#security_config DataprocCluster#security_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#software_config DataprocCluster#software_config}
        :param staging_bucket: The Cloud Storage staging bucket used to stage files, such as Hadoop jars, between client machines and the cluster. Note: If you don't explicitly specify a staging_bucket then GCP will auto create / assign one for you. However, you are not guaranteed an auto generated bucket which is solely dedicated to your cluster; it may be shared with other clusters in the same region/zone also choosing to use the auto generation option. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        :param temp_bucket: The Cloud Storage temp bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. Note: If you don't explicitly specify a temp_bucket then GCP will auto create / assign one for you. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#temp_bucket DataprocCluster#temp_bucket}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#worker_config DataprocCluster#worker_config}
        '''
        value = DataprocClusterClusterConfig(
            autoscaling_config=autoscaling_config,
            encryption_config=encryption_config,
            endpoint_config=endpoint_config,
            gce_cluster_config=gce_cluster_config,
            initialization_action=initialization_action,
            lifecycle_config=lifecycle_config,
            master_config=master_config,
            metastore_config=metastore_config,
            preemptible_worker_config=preemptible_worker_config,
            security_config=security_config,
            software_config=software_config,
            staging_bucket=staging_bucket,
            temp_bucket=temp_bucket,
            worker_config=worker_config,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#create DataprocCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#delete DataprocCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#update DataprocCluster#update}.
        '''
        value = DataprocClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualClusterConfig")
    def put_virtual_cluster_config(
        self,
        *,
        auxiliary_services_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig", typing.Dict[str, typing.Any]]] = None,
        kubernetes_cluster_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfig", typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auxiliary_services_config: auxiliary_services_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auxiliary_services_config DataprocCluster#auxiliary_services_config}
        :param kubernetes_cluster_config: kubernetes_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_cluster_config DataprocCluster#kubernetes_cluster_config}
        :param staging_bucket: A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        '''
        value = DataprocClusterVirtualClusterConfig(
            auxiliary_services_config=auxiliary_services_config,
            kubernetes_cluster_config=kubernetes_cluster_config,
            staging_bucket=staging_bucket,
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualClusterConfig", [value]))

    @jsii.member(jsii_name="resetClusterConfig")
    def reset_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterConfig", []))

    @jsii.member(jsii_name="resetGracefulDecommissionTimeout")
    def reset_graceful_decommission_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracefulDecommissionTimeout", []))

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

    @jsii.member(jsii_name="resetVirtualClusterConfig")
    def reset_virtual_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualClusterConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(self) -> "DataprocClusterClusterConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigOutputReference", jsii.get(self, "clusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataprocClusterTimeoutsOutputReference":
        return typing.cast("DataprocClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualClusterConfig")
    def virtual_cluster_config(
        self,
    ) -> "DataprocClusterVirtualClusterConfigOutputReference":
        return typing.cast("DataprocClusterVirtualClusterConfigOutputReference", jsii.get(self, "virtualClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfigInput")
    def cluster_config_input(self) -> typing.Optional["DataprocClusterClusterConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfig"], jsii.get(self, "clusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gracefulDecommissionTimeoutInput")
    def graceful_decommission_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracefulDecommissionTimeoutInput"))

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
    ) -> typing.Optional[typing.Union["DataprocClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataprocClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualClusterConfigInput")
    def virtual_cluster_config_input(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfig"]:
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfig"], jsii.get(self, "virtualClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gracefulDecommissionTimeout")
    def graceful_decommission_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracefulDecommissionTimeout"))

    @graceful_decommission_timeout.setter
    def graceful_decommission_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "graceful_decommission_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracefulDecommissionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocCluster, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "autoscaling_config": "autoscalingConfig",
        "encryption_config": "encryptionConfig",
        "endpoint_config": "endpointConfig",
        "gce_cluster_config": "gceClusterConfig",
        "initialization_action": "initializationAction",
        "lifecycle_config": "lifecycleConfig",
        "master_config": "masterConfig",
        "metastore_config": "metastoreConfig",
        "preemptible_worker_config": "preemptibleWorkerConfig",
        "security_config": "securityConfig",
        "software_config": "softwareConfig",
        "staging_bucket": "stagingBucket",
        "temp_bucket": "tempBucket",
        "worker_config": "workerConfig",
    },
)
class DataprocClusterClusterConfig:
    def __init__(
        self,
        *,
        autoscaling_config: typing.Optional[typing.Union["DataprocClusterClusterConfigAutoscalingConfig", typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union["DataprocClusterClusterConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        endpoint_config: typing.Optional[typing.Union["DataprocClusterClusterConfigEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        gce_cluster_config: typing.Optional[typing.Union["DataprocClusterClusterConfigGceClusterConfig", typing.Dict[str, typing.Any]]] = None,
        initialization_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterClusterConfigInitializationAction", typing.Dict[str, typing.Any]]]]] = None,
        lifecycle_config: typing.Optional[typing.Union["DataprocClusterClusterConfigLifecycleConfig", typing.Dict[str, typing.Any]]] = None,
        master_config: typing.Optional[typing.Union["DataprocClusterClusterConfigMasterConfig", typing.Dict[str, typing.Any]]] = None,
        metastore_config: typing.Optional[typing.Union["DataprocClusterClusterConfigMetastoreConfig", typing.Dict[str, typing.Any]]] = None,
        preemptible_worker_config: typing.Optional[typing.Union["DataprocClusterClusterConfigPreemptibleWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        security_config: typing.Optional[typing.Union["DataprocClusterClusterConfigSecurityConfig", typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union["DataprocClusterClusterConfigSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
        temp_bucket: typing.Optional[builtins.str] = None,
        worker_config: typing.Optional[typing.Union["DataprocClusterClusterConfigWorkerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling_config: autoscaling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling_config DataprocCluster#autoscaling_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#encryption_config DataprocCluster#encryption_config}
        :param endpoint_config: endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#endpoint_config DataprocCluster#endpoint_config}
        :param gce_cluster_config: gce_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gce_cluster_config DataprocCluster#gce_cluster_config}
        :param initialization_action: initialization_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#initialization_action DataprocCluster#initialization_action}
        :param lifecycle_config: lifecycle_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#lifecycle_config DataprocCluster#lifecycle_config}
        :param master_config: master_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#master_config DataprocCluster#master_config}
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        :param preemptible_worker_config: preemptible_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible_worker_config DataprocCluster#preemptible_worker_config}
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#security_config DataprocCluster#security_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#software_config DataprocCluster#software_config}
        :param staging_bucket: The Cloud Storage staging bucket used to stage files, such as Hadoop jars, between client machines and the cluster. Note: If you don't explicitly specify a staging_bucket then GCP will auto create / assign one for you. However, you are not guaranteed an auto generated bucket which is solely dedicated to your cluster; it may be shared with other clusters in the same region/zone also choosing to use the auto generation option. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        :param temp_bucket: The Cloud Storage temp bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. Note: If you don't explicitly specify a temp_bucket then GCP will auto create / assign one for you. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#temp_bucket DataprocCluster#temp_bucket}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#worker_config DataprocCluster#worker_config}
        '''
        if isinstance(autoscaling_config, dict):
            autoscaling_config = DataprocClusterClusterConfigAutoscalingConfig(**autoscaling_config)
        if isinstance(encryption_config, dict):
            encryption_config = DataprocClusterClusterConfigEncryptionConfig(**encryption_config)
        if isinstance(endpoint_config, dict):
            endpoint_config = DataprocClusterClusterConfigEndpointConfig(**endpoint_config)
        if isinstance(gce_cluster_config, dict):
            gce_cluster_config = DataprocClusterClusterConfigGceClusterConfig(**gce_cluster_config)
        if isinstance(lifecycle_config, dict):
            lifecycle_config = DataprocClusterClusterConfigLifecycleConfig(**lifecycle_config)
        if isinstance(master_config, dict):
            master_config = DataprocClusterClusterConfigMasterConfig(**master_config)
        if isinstance(metastore_config, dict):
            metastore_config = DataprocClusterClusterConfigMetastoreConfig(**metastore_config)
        if isinstance(preemptible_worker_config, dict):
            preemptible_worker_config = DataprocClusterClusterConfigPreemptibleWorkerConfig(**preemptible_worker_config)
        if isinstance(security_config, dict):
            security_config = DataprocClusterClusterConfigSecurityConfig(**security_config)
        if isinstance(software_config, dict):
            software_config = DataprocClusterClusterConfigSoftwareConfig(**software_config)
        if isinstance(worker_config, dict):
            worker_config = DataprocClusterClusterConfigWorkerConfig(**worker_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfig.__init__)
            check_type(argname="argument autoscaling_config", value=autoscaling_config, expected_type=type_hints["autoscaling_config"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument endpoint_config", value=endpoint_config, expected_type=type_hints["endpoint_config"])
            check_type(argname="argument gce_cluster_config", value=gce_cluster_config, expected_type=type_hints["gce_cluster_config"])
            check_type(argname="argument initialization_action", value=initialization_action, expected_type=type_hints["initialization_action"])
            check_type(argname="argument lifecycle_config", value=lifecycle_config, expected_type=type_hints["lifecycle_config"])
            check_type(argname="argument master_config", value=master_config, expected_type=type_hints["master_config"])
            check_type(argname="argument metastore_config", value=metastore_config, expected_type=type_hints["metastore_config"])
            check_type(argname="argument preemptible_worker_config", value=preemptible_worker_config, expected_type=type_hints["preemptible_worker_config"])
            check_type(argname="argument security_config", value=security_config, expected_type=type_hints["security_config"])
            check_type(argname="argument software_config", value=software_config, expected_type=type_hints["software_config"])
            check_type(argname="argument staging_bucket", value=staging_bucket, expected_type=type_hints["staging_bucket"])
            check_type(argname="argument temp_bucket", value=temp_bucket, expected_type=type_hints["temp_bucket"])
            check_type(argname="argument worker_config", value=worker_config, expected_type=type_hints["worker_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscaling_config is not None:
            self._values["autoscaling_config"] = autoscaling_config
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if endpoint_config is not None:
            self._values["endpoint_config"] = endpoint_config
        if gce_cluster_config is not None:
            self._values["gce_cluster_config"] = gce_cluster_config
        if initialization_action is not None:
            self._values["initialization_action"] = initialization_action
        if lifecycle_config is not None:
            self._values["lifecycle_config"] = lifecycle_config
        if master_config is not None:
            self._values["master_config"] = master_config
        if metastore_config is not None:
            self._values["metastore_config"] = metastore_config
        if preemptible_worker_config is not None:
            self._values["preemptible_worker_config"] = preemptible_worker_config
        if security_config is not None:
            self._values["security_config"] = security_config
        if software_config is not None:
            self._values["software_config"] = software_config
        if staging_bucket is not None:
            self._values["staging_bucket"] = staging_bucket
        if temp_bucket is not None:
            self._values["temp_bucket"] = temp_bucket
        if worker_config is not None:
            self._values["worker_config"] = worker_config

    @builtins.property
    def autoscaling_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigAutoscalingConfig"]:
        '''autoscaling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling_config DataprocCluster#autoscaling_config}
        '''
        result = self._values.get("autoscaling_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigAutoscalingConfig"], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigEncryptionConfig"]:
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#encryption_config DataprocCluster#encryption_config}
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigEncryptionConfig"], result)

    @builtins.property
    def endpoint_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigEndpointConfig"]:
        '''endpoint_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#endpoint_config DataprocCluster#endpoint_config}
        '''
        result = self._values.get("endpoint_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigEndpointConfig"], result)

    @builtins.property
    def gce_cluster_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigGceClusterConfig"]:
        '''gce_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gce_cluster_config DataprocCluster#gce_cluster_config}
        '''
        result = self._values.get("gce_cluster_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigGceClusterConfig"], result)

    @builtins.property
    def initialization_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigInitializationAction"]]]:
        '''initialization_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#initialization_action DataprocCluster#initialization_action}
        '''
        result = self._values.get("initialization_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigInitializationAction"]]], result)

    @builtins.property
    def lifecycle_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigLifecycleConfig"]:
        '''lifecycle_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#lifecycle_config DataprocCluster#lifecycle_config}
        '''
        result = self._values.get("lifecycle_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigLifecycleConfig"], result)

    @builtins.property
    def master_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigMasterConfig"]:
        '''master_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#master_config DataprocCluster#master_config}
        '''
        result = self._values.get("master_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigMasterConfig"], result)

    @builtins.property
    def metastore_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigMetastoreConfig"]:
        '''metastore_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        '''
        result = self._values.get("metastore_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigMetastoreConfig"], result)

    @builtins.property
    def preemptible_worker_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfig"]:
        '''preemptible_worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible_worker_config DataprocCluster#preemptible_worker_config}
        '''
        result = self._values.get("preemptible_worker_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfig"], result)

    @builtins.property
    def security_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigSecurityConfig"]:
        '''security_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#security_config DataprocCluster#security_config}
        '''
        result = self._values.get("security_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigSecurityConfig"], result)

    @builtins.property
    def software_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigSoftwareConfig"]:
        '''software_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#software_config DataprocCluster#software_config}
        '''
        result = self._values.get("software_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigSoftwareConfig"], result)

    @builtins.property
    def staging_bucket(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage staging bucket used to stage files, such as Hadoop jars, between client machines and the cluster.

        Note: If you don't explicitly specify a staging_bucket then GCP will auto create / assign one for you. However, you are not guaranteed an auto generated bucket which is solely dedicated to your cluster; it may be shared with other clusters in the same region/zone also choosing to use the auto generation option.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        '''
        result = self._values.get("staging_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temp_bucket(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage temp bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files.

        Note: If you don't explicitly specify a temp_bucket then GCP will auto create / assign one for you.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#temp_bucket DataprocCluster#temp_bucket}
        '''
        result = self._values.get("temp_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def worker_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigWorkerConfig"]:
        '''worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#worker_config DataprocCluster#worker_config}
        '''
        result = self._values.get("worker_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigWorkerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigAutoscalingConfig",
    jsii_struct_bases=[],
    name_mapping={"policy_uri": "policyUri"},
)
class DataprocClusterClusterConfigAutoscalingConfig:
    def __init__(self, *, policy_uri: builtins.str) -> None:
        '''
        :param policy_uri: The autoscaling policy used by the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#policy_uri DataprocCluster#policy_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigAutoscalingConfig.__init__)
            check_type(argname="argument policy_uri", value=policy_uri, expected_type=type_hints["policy_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy_uri": policy_uri,
        }

    @builtins.property
    def policy_uri(self) -> builtins.str:
        '''The autoscaling policy used by the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#policy_uri DataprocCluster#policy_uri}
        '''
        result = self._values.get("policy_uri")
        assert result is not None, "Required property 'policy_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigAutoscalingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigAutoscalingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigAutoscalingConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigAutoscalingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="policyUriInput")
    def policy_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyUriInput"))

    @builtins.property
    @jsii.member(jsii_name="policyUri")
    def policy_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyUri"))

    @policy_uri.setter
    def policy_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigAutoscalingConfigOutputReference, "policy_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigAutoscalingConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigAutoscalingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigAutoscalingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigAutoscalingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class DataprocClusterClusterConfigEncryptionConfig:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The Cloud KMS key name to use for PD disk encryption for all instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_name DataprocCluster#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigEncryptionConfig.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''The Cloud KMS key name to use for PD disk encryption for all instances in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_name DataprocCluster#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigEncryptionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigEncryptionConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigEncryptionConfigOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigEncryptionConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigEncryptionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigEndpointConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_http_port_access": "enableHttpPortAccess"},
)
class DataprocClusterClusterConfigEndpointConfig:
    def __init__(
        self,
        *,
        enable_http_port_access: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_http_port_access: The flag to enable http access to specific ports on the cluster from external sources (aka Component Gateway). Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_http_port_access DataprocCluster#enable_http_port_access}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigEndpointConfig.__init__)
            check_type(argname="argument enable_http_port_access", value=enable_http_port_access, expected_type=type_hints["enable_http_port_access"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_http_port_access": enable_http_port_access,
        }

    @builtins.property
    def enable_http_port_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''The flag to enable http access to specific ports on the cluster from external sources (aka Component Gateway).

        Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_http_port_access DataprocCluster#enable_http_port_access}
        '''
        result = self._values.get("enable_http_port_access")
        assert result is not None, "Required property 'enable_http_port_access' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigEndpointConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigEndpointConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigEndpointConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="httpPorts")
    def http_ports(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "httpPorts"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpPortAccessInput")
    def enable_http_port_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttpPortAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpPortAccess")
    def enable_http_port_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttpPortAccess"))

    @enable_http_port_access.setter
    def enable_http_port_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigEndpointConfigOutputReference, "enable_http_port_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpPortAccess", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigEndpointConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigEndpointConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigEndpointConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigEndpointConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigGceClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "internal_ip_only": "internalIpOnly",
        "metadata": "metadata",
        "network": "network",
        "service_account": "serviceAccount",
        "service_account_scopes": "serviceAccountScopes",
        "shielded_instance_config": "shieldedInstanceConfig",
        "subnetwork": "subnetwork",
        "tags": "tags",
        "zone": "zone",
    },
)
class DataprocClusterClusterConfigGceClusterConfig:
    def __init__(
        self,
        *,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        service_account_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        shielded_instance_config: typing.Optional[typing.Union["DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal_ip_only: By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. If set to true, all instances in the cluster will only have internal IP addresses. Note: Private Google Access (also known as privateIpGoogleAccess) must be enabled on the subnetwork that the cluster will be launched in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#internal_ip_only DataprocCluster#internal_ip_only}
        :param metadata: A map of the Compute Engine metadata entries to add to all instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metadata DataprocCluster#metadata}
        :param network: The name or self_link of the Google Compute Engine network to the cluster will be part of. Conflicts with subnetwork. If neither is specified, this defaults to the "default" network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#network DataprocCluster#network}
        :param service_account: The service account to be used by the Node VMs. If not specified, the "default" service account is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account DataprocCluster#service_account}
        :param service_account_scopes: The set of Google API scopes to be made available on all of the node VMs under the service_account specified. These can be either FQDNs, or scope aliases. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account_scopes DataprocCluster#service_account_scopes}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#shielded_instance_config DataprocCluster#shielded_instance_config}
        :param subnetwork: The name or self_link of the Google Compute Engine subnetwork the cluster will be part of. Conflicts with network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#subnetwork DataprocCluster#subnetwork}
        :param tags: The list of instance tags applied to instances in the cluster. Tags are used to identify valid sources or targets for network firewalls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tags DataprocCluster#tags}
        :param zone: The GCP zone where your data is stored and used (i.e. where the master and the worker nodes will be created in). If region is set to 'global' (default) then zone is mandatory, otherwise GCP is able to make use of Auto Zone Placement to determine this automatically for you. Note: This setting additionally determines and restricts which computing resources are available for use with other configs such as cluster_config.master_config.machine_type and cluster_config.worker_config.machine_type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#zone DataprocCluster#zone}
        '''
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig(**shielded_instance_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigGceClusterConfig.__init__)
            check_type(argname="argument internal_ip_only", value=internal_ip_only, expected_type=type_hints["internal_ip_only"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument service_account_scopes", value=service_account_scopes, expected_type=type_hints["service_account_scopes"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {}
        if internal_ip_only is not None:
            self._values["internal_ip_only"] = internal_ip_only
        if metadata is not None:
            self._values["metadata"] = metadata
        if network is not None:
            self._values["network"] = network
        if service_account is not None:
            self._values["service_account"] = service_account
        if service_account_scopes is not None:
            self._values["service_account_scopes"] = service_account_scopes
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
        if tags is not None:
            self._values["tags"] = tags
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def internal_ip_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance.

        If set to true, all instances in the cluster will only have internal IP addresses. Note: Private Google Access (also known as privateIpGoogleAccess) must be enabled on the subnetwork that the cluster will be launched in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#internal_ip_only DataprocCluster#internal_ip_only}
        '''
        result = self._values.get("internal_ip_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of the Compute Engine metadata entries to add to all instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metadata DataprocCluster#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the Google Compute Engine network to the cluster will be part of.

        Conflicts with subnetwork. If neither is specified, this defaults to the "default" network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#network DataprocCluster#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The service account to be used by the Node VMs. If not specified, the "default" service account is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account DataprocCluster#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of Google API scopes to be made available on all of the node VMs under the service_account specified.

        These can be either FQDNs, or scope aliases.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account_scopes DataprocCluster#service_account_scopes}
        '''
        result = self._values.get("service_account_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#shielded_instance_config DataprocCluster#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig"], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the Google Compute Engine subnetwork the cluster will be part of. Conflicts with network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#subnetwork DataprocCluster#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of instance tags applied to instances in the cluster.

        Tags are used to identify valid sources or targets for network firewalls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tags DataprocCluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The GCP zone where your data is stored and used (i.e. where the master and the worker nodes will be created in). If region is set to 'global' (default) then zone is mandatory, otherwise GCP is able to make use of Auto Zone Placement to determine this automatically for you. Note: This setting additionally determines and restricts which computing resources are available for use with other configs such as cluster_config.master_config.machine_type and cluster_config.worker_config.machine_type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#zone DataprocCluster#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigGceClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigGceClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigGceClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigGceClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether instances have integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_integrity_monitoring DataprocCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether instances have Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_secure_boot DataprocCluster#enable_secure_boot}
        :param enable_vtpm: Defines whether instances have the vTPM enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_vtpm DataprocCluster#enable_vtpm}
        '''
        value = DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
            enable_vtpm=enable_vtpm,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="resetInternalIpOnly")
    def reset_internal_ip_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalIpOnly", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetServiceAccountScopes")
    def reset_service_account_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountScopes", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

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
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="internalIpOnlyInput")
    def internal_ip_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalIpOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountScopesInput")
    def service_account_scopes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceAccountScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

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
    @jsii.member(jsii_name="internalIpOnly")
    def internal_ip_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internalIpOnly"))

    @internal_ip_only.setter
    def internal_ip_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "internal_ip_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalIpOnly", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountScopes")
    def service_account_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceAccountScopes"))

    @service_account_scopes.setter
    def service_account_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "service_account_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountScopes", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigGceClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigGceClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigGceClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
        "enable_vtpm": "enableVtpm",
    },
)
class DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether instances have integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_integrity_monitoring DataprocCluster#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether instances have Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_secure_boot DataprocCluster#enable_secure_boot}
        :param enable_vtpm: Defines whether instances have the vTPM enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_vtpm DataprocCluster#enable_vtpm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
            check_type(argname="argument enable_vtpm", value=enable_vtpm, expected_type=type_hints["enable_vtpm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot
        if enable_vtpm is not None:
            self._values["enable_vtpm"] = enable_vtpm

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether instances have integrity monitoring enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_integrity_monitoring DataprocCluster#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether instances have Secure Boot enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_secure_boot DataprocCluster#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_vtpm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether instances have the vTPM enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_vtpm DataprocCluster#enable_vtpm}
        '''
        result = self._values.get("enable_vtpm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @jsii.member(jsii_name="resetEnableVtpm")
    def reset_enable_vtpm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableVtpm", []))

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
    @jsii.member(jsii_name="enableVtpmInput")
    def enable_vtpm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableVtpmInput"))

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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="enableVtpm")
    def enable_vtpm(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableVtpm"))

    @enable_vtpm.setter
    def enable_vtpm(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_vtpm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVtpm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigInitializationAction",
    jsii_struct_bases=[],
    name_mapping={"script": "script", "timeout_sec": "timeoutSec"},
)
class DataprocClusterClusterConfigInitializationAction:
    def __init__(
        self,
        *,
        script: builtins.str,
        timeout_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param script: The script to be executed during initialization of the cluster. The script must be a GCS file with a gs:// prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#script DataprocCluster#script}
        :param timeout_sec: The maximum duration (in seconds) which script is allowed to take to execute its action. GCP will default to a predetermined computed value if not set (currently 300). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#timeout_sec DataprocCluster#timeout_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigInitializationAction.__init__)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument timeout_sec", value=timeout_sec, expected_type=type_hints["timeout_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "script": script,
        }
        if timeout_sec is not None:
            self._values["timeout_sec"] = timeout_sec

    @builtins.property
    def script(self) -> builtins.str:
        '''The script to be executed during initialization of the cluster.

        The script must be a GCS file with a gs:// prefix.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#script DataprocCluster#script}
        '''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_sec(self) -> typing.Optional[jsii.Number]:
        '''The maximum duration (in seconds) which script is allowed to take to execute its action.

        GCP will default to a predetermined computed value if not set (currently 300).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#timeout_sec DataprocCluster#timeout_sec}
        '''
        result = self._values.get("timeout_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigInitializationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigInitializationActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigInitializationActionList",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigInitializationActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataprocClusterClusterConfigInitializationActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigInitializationActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataprocClusterClusterConfigInitializationActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigInitializationAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigInitializationAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigInitializationAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigInitializationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigInitializationActionOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigInitializationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetTimeoutSec")
    def reset_timeout_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSec", []))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecInput")
    def timeout_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecInput"))

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionOutputReference, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSec")
    def timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSec"))

    @timeout_sec.setter
    def timeout_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionOutputReference, "timeout_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataprocClusterClusterConfigInitializationAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataprocClusterClusterConfigInitializationAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataprocClusterClusterConfigInitializationAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigInitializationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigLifecycleConfig",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete_time": "autoDeleteTime",
        "idle_delete_ttl": "idleDeleteTtl",
    },
)
class DataprocClusterClusterConfigLifecycleConfig:
    def __init__(
        self,
        *,
        auto_delete_time: typing.Optional[builtins.str] = None,
        idle_delete_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete_time: The time when cluster will be auto-deleted. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auto_delete_time DataprocCluster#auto_delete_time}
        :param idle_delete_ttl: The duration to keep the cluster alive while idling (no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#idle_delete_ttl DataprocCluster#idle_delete_ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigLifecycleConfig.__init__)
            check_type(argname="argument auto_delete_time", value=auto_delete_time, expected_type=type_hints["auto_delete_time"])
            check_type(argname="argument idle_delete_ttl", value=idle_delete_ttl, expected_type=type_hints["idle_delete_ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_delete_time is not None:
            self._values["auto_delete_time"] = auto_delete_time
        if idle_delete_ttl is not None:
            self._values["idle_delete_ttl"] = idle_delete_ttl

    @builtins.property
    def auto_delete_time(self) -> typing.Optional[builtins.str]:
        '''The time when cluster will be auto-deleted. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auto_delete_time DataprocCluster#auto_delete_time}
        '''
        result = self._values.get("auto_delete_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_delete_ttl(self) -> typing.Optional[builtins.str]:
        '''The duration to keep the cluster alive while idling (no jobs running).

        After this TTL, the cluster will be deleted. Valid range: [10m, 14d].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#idle_delete_ttl DataprocCluster#idle_delete_ttl}
        '''
        result = self._values.get("idle_delete_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigLifecycleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigLifecycleConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigLifecycleConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigLifecycleConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoDeleteTime")
    def reset_auto_delete_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeleteTime", []))

    @jsii.member(jsii_name="resetIdleDeleteTtl")
    def reset_idle_delete_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleDeleteTtl", []))

    @builtins.property
    @jsii.member(jsii_name="idleStartTime")
    def idle_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idleStartTime"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTimeInput")
    def auto_delete_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoDeleteTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idleDeleteTtlInput")
    def idle_delete_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idleDeleteTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTime")
    def auto_delete_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDeleteTime"))

    @auto_delete_time.setter
    def auto_delete_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigLifecycleConfigOutputReference, "auto_delete_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeleteTime", value)

    @builtins.property
    @jsii.member(jsii_name="idleDeleteTtl")
    def idle_delete_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idleDeleteTtl"))

    @idle_delete_ttl.setter
    def idle_delete_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigLifecycleConfigOutputReference, "idle_delete_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleDeleteTtl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigLifecycleConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigLifecycleConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigLifecycleConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigLifecycleConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "disk_config": "diskConfig",
        "image_uri": "imageUri",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "num_instances": "numInstances",
    },
)
class DataprocClusterClusterConfigMasterConfig:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterClusterConfigMasterConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["DataprocClusterClusterConfigMasterConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param image_uri: The URI for the image to use for this master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        :param machine_type: The name of a Google Compute Engine machine type to create for the master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: The name of a minimum generation of CPU family for the master/worker. If not specified, GCP will default to a predetermined computed value for each zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param num_instances: Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        if isinstance(disk_config, dict):
            disk_config = DataprocClusterClusterConfigMasterConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfig.__init__)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if num_instances is not None:
            self._values["num_instances"] = num_instances

    @builtins.property
    def accelerators(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigMasterConfigAccelerators"]]]:
        '''accelerators block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigMasterConfigAccelerators"]]], result)

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigMasterConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigMasterConfigDiskConfig"], result)

    @builtins.property
    def image_uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the image to use for this master/worker.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        '''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Google Compute Engine machine type to create for the master/worker.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''The name of a minimum generation of CPU family for the master/worker.

        If not specified, GCP will default to a predetermined computed value for each zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigMasterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigAccelerators",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_type": "acceleratorType",
    },
)
class DataprocClusterClusterConfigMasterConfigAccelerators:
    def __init__(
        self,
        *,
        accelerator_count: jsii.Number,
        accelerator_type: builtins.str,
    ) -> None:
        '''
        :param accelerator_count: The number of the accelerator cards of this type exposed to this instance. Often restricted to one of 1, 2, 4, or 8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_count DataprocCluster#accelerator_count}
        :param accelerator_type: The short name of the accelerator type to expose to this instance. For example, nvidia-tesla-k80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_type DataprocCluster#accelerator_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigAccelerators.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_count": accelerator_count,
            "accelerator_type": accelerator_type,
        }

    @builtins.property
    def accelerator_count(self) -> jsii.Number:
        '''The number of the accelerator cards of this type exposed to this instance.

        Often restricted to one of 1, 2, 4, or 8.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_count DataprocCluster#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        assert result is not None, "Required property 'accelerator_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def accelerator_type(self) -> builtins.str:
        '''The short name of the accelerator type to expose to this instance. For example, nvidia-tesla-k80.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_type DataprocCluster#accelerator_type}
        '''
        result = self._values.get("accelerator_type")
        assert result is not None, "Required property 'accelerator_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigMasterConfigAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigMasterConfigAcceleratorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigAcceleratorsList",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigAcceleratorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigAcceleratorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigMasterConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigMasterConfigAccelerators]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigMasterConfigAccelerators]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceleratorCount"))

    @accelerator_count.setter
    def accelerator_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference, "accelerator_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorCount", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference, "accelerator_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataprocClusterClusterConfigMasterConfigAccelerators, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataprocClusterClusterConfigMasterConfigAccelerators, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataprocClusterClusterConfigMasterConfigAccelerators, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class DataprocClusterClusterConfigMasterConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each node, specified in GB. The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the primary disk attached to each node, specified in GB.

        The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigMasterConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMasterConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMasterConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigMasterConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigMasterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMasterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccelerators")
    def put_accelerators(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterClusterConfigMasterConfigAccelerators, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMasterConfigOutputReference.put_accelerators)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccelerators", [value]))

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each node, specified in GB. The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        value = DataprocClusterClusterConfigMasterConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetAccelerators")
    def reset_accelerators(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerators", []))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetImageUri")
    def reset_image_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageUri", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(self) -> DataprocClusterClusterConfigMasterConfigAcceleratorsList:
        return typing.cast(DataprocClusterClusterConfigMasterConfigAcceleratorsList, jsii.get(self, "accelerators"))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorsInput")
    def accelerators_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigMasterConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigMasterConfigAccelerators]]], jsii.get(self, "acceleratorsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMasterConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMasterConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUriInput")
    def image_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigOutputReference, "image_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMasterConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMasterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigMasterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMasterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMetastoreConfig",
    jsii_struct_bases=[],
    name_mapping={"dataproc_metastore_service": "dataprocMetastoreService"},
)
class DataprocClusterClusterConfigMetastoreConfig:
    def __init__(self, *, dataproc_metastore_service: builtins.str) -> None:
        '''
        :param dataproc_metastore_service: Resource name of an existing Dataproc Metastore service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMetastoreConfig.__init__)
            check_type(argname="argument dataproc_metastore_service", value=dataproc_metastore_service, expected_type=type_hints["dataproc_metastore_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataproc_metastore_service": dataproc_metastore_service,
        }

    @builtins.property
    def dataproc_metastore_service(self) -> builtins.str:
        '''Resource name of an existing Dataproc Metastore service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        result = self._values.get("dataproc_metastore_service")
        assert result is not None, "Required property 'dataproc_metastore_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigMetastoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigMetastoreConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigMetastoreConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigMetastoreConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreServiceInput")
    def dataproc_metastore_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataprocMetastoreServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataprocMetastoreService"))

    @dataproc_metastore_service.setter
    def dataproc_metastore_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMetastoreConfigOutputReference, "dataproc_metastore_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataprocMetastoreService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMetastoreConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMetastoreConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigMetastoreConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigMetastoreConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscalingConfig")
    def put_autoscaling_config(self, *, policy_uri: builtins.str) -> None:
        '''
        :param policy_uri: The autoscaling policy used by the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#policy_uri DataprocCluster#policy_uri}
        '''
        value = DataprocClusterClusterConfigAutoscalingConfig(policy_uri=policy_uri)

        return typing.cast(None, jsii.invoke(self, "putAutoscalingConfig", [value]))

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The Cloud KMS key name to use for PD disk encryption for all instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_name DataprocCluster#kms_key_name}
        '''
        value = DataprocClusterClusterConfigEncryptionConfig(kms_key_name=kms_key_name)

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @jsii.member(jsii_name="putEndpointConfig")
    def put_endpoint_config(
        self,
        *,
        enable_http_port_access: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_http_port_access: The flag to enable http access to specific ports on the cluster from external sources (aka Component Gateway). Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_http_port_access DataprocCluster#enable_http_port_access}
        '''
        value = DataprocClusterClusterConfigEndpointConfig(
            enable_http_port_access=enable_http_port_access
        )

        return typing.cast(None, jsii.invoke(self, "putEndpointConfig", [value]))

    @jsii.member(jsii_name="putGceClusterConfig")
    def put_gce_cluster_config(
        self,
        *,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        service_account_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        shielded_instance_config: typing.Optional[typing.Union[DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig, typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal_ip_only: By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. If set to true, all instances in the cluster will only have internal IP addresses. Note: Private Google Access (also known as privateIpGoogleAccess) must be enabled on the subnetwork that the cluster will be launched in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#internal_ip_only DataprocCluster#internal_ip_only}
        :param metadata: A map of the Compute Engine metadata entries to add to all instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metadata DataprocCluster#metadata}
        :param network: The name or self_link of the Google Compute Engine network to the cluster will be part of. Conflicts with subnetwork. If neither is specified, this defaults to the "default" network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#network DataprocCluster#network}
        :param service_account: The service account to be used by the Node VMs. If not specified, the "default" service account is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account DataprocCluster#service_account}
        :param service_account_scopes: The set of Google API scopes to be made available on all of the node VMs under the service_account specified. These can be either FQDNs, or scope aliases. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#service_account_scopes DataprocCluster#service_account_scopes}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#shielded_instance_config DataprocCluster#shielded_instance_config}
        :param subnetwork: The name or self_link of the Google Compute Engine subnetwork the cluster will be part of. Conflicts with network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#subnetwork DataprocCluster#subnetwork}
        :param tags: The list of instance tags applied to instances in the cluster. Tags are used to identify valid sources or targets for network firewalls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tags DataprocCluster#tags}
        :param zone: The GCP zone where your data is stored and used (i.e. where the master and the worker nodes will be created in). If region is set to 'global' (default) then zone is mandatory, otherwise GCP is able to make use of Auto Zone Placement to determine this automatically for you. Note: This setting additionally determines and restricts which computing resources are available for use with other configs such as cluster_config.master_config.machine_type and cluster_config.worker_config.machine_type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#zone DataprocCluster#zone}
        '''
        value = DataprocClusterClusterConfigGceClusterConfig(
            internal_ip_only=internal_ip_only,
            metadata=metadata,
            network=network,
            service_account=service_account,
            service_account_scopes=service_account_scopes,
            shielded_instance_config=shielded_instance_config,
            subnetwork=subnetwork,
            tags=tags,
            zone=zone,
        )

        return typing.cast(None, jsii.invoke(self, "putGceClusterConfig", [value]))

    @jsii.member(jsii_name="putInitializationAction")
    def put_initialization_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterClusterConfigInitializationAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigOutputReference.put_initialization_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitializationAction", [value]))

    @jsii.member(jsii_name="putLifecycleConfig")
    def put_lifecycle_config(
        self,
        *,
        auto_delete_time: typing.Optional[builtins.str] = None,
        idle_delete_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete_time: The time when cluster will be auto-deleted. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auto_delete_time DataprocCluster#auto_delete_time}
        :param idle_delete_ttl: The duration to keep the cluster alive while idling (no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#idle_delete_ttl DataprocCluster#idle_delete_ttl}
        '''
        value = DataprocClusterClusterConfigLifecycleConfig(
            auto_delete_time=auto_delete_time, idle_delete_ttl=idle_delete_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putLifecycleConfig", [value]))

    @jsii.member(jsii_name="putMasterConfig")
    def put_master_config(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterClusterConfigMasterConfigAccelerators, typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union[DataprocClusterClusterConfigMasterConfigDiskConfig, typing.Dict[str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param image_uri: The URI for the image to use for this master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        :param machine_type: The name of a Google Compute Engine machine type to create for the master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: The name of a minimum generation of CPU family for the master/worker. If not specified, GCP will default to a predetermined computed value for each zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param num_instances: Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        value = DataprocClusterClusterConfigMasterConfig(
            accelerators=accelerators,
            disk_config=disk_config,
            image_uri=image_uri,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            num_instances=num_instances,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterConfig", [value]))

    @jsii.member(jsii_name="putMetastoreConfig")
    def put_metastore_config(self, *, dataproc_metastore_service: builtins.str) -> None:
        '''
        :param dataproc_metastore_service: Resource name of an existing Dataproc Metastore service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        value = DataprocClusterClusterConfigMetastoreConfig(
            dataproc_metastore_service=dataproc_metastore_service
        )

        return typing.cast(None, jsii.invoke(self, "putMetastoreConfig", [value]))

    @jsii.member(jsii_name="putPreemptibleWorkerConfig")
    def put_preemptible_worker_config(
        self,
        *,
        disk_config: typing.Optional[typing.Union["DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param num_instances: Specifies the number of preemptible nodes to create. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        :param preemptibility: Specifies the preemptibility of the secondary nodes. Defaults to PREEMPTIBLE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptibility DataprocCluster#preemptibility}
        '''
        value = DataprocClusterClusterConfigPreemptibleWorkerConfig(
            disk_config=disk_config,
            num_instances=num_instances,
            preemptibility=preemptibility,
        )

        return typing.cast(None, jsii.invoke(self, "putPreemptibleWorkerConfig", [value]))

    @jsii.member(jsii_name="putSecurityConfig")
    def put_security_config(
        self,
        *,
        kerberos_config: typing.Union["DataprocClusterClusterConfigSecurityConfigKerberosConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param kerberos_config: kerberos_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kerberos_config DataprocCluster#kerberos_config}
        '''
        value = DataprocClusterClusterConfigSecurityConfig(
            kerberos_config=kerberos_config
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityConfig", [value]))

    @jsii.member(jsii_name="putSoftwareConfig")
    def put_software_config(
        self,
        *,
        image_version: typing.Optional[builtins.str] = None,
        optional_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        override_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param image_version: The Cloud Dataproc image version to use for the cluster - this controls the sets of software versions installed onto the nodes when you create clusters. If not specified, defaults to the latest version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_version DataprocCluster#image_version}
        :param optional_components: The set of optional components to activate on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#optional_components DataprocCluster#optional_components}
        :param override_properties: A list of override and additional properties (key/value pairs) used to modify various aspects of the common configuration files used when creating a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#override_properties DataprocCluster#override_properties}
        '''
        value = DataprocClusterClusterConfigSoftwareConfig(
            image_version=image_version,
            optional_components=optional_components,
            override_properties=override_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putSoftwareConfig", [value]))

    @jsii.member(jsii_name="putWorkerConfig")
    def put_worker_config(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterClusterConfigWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["DataprocClusterClusterConfigWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param image_uri: The URI for the image to use for this master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        :param machine_type: The name of a Google Compute Engine machine type to create for the master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: The name of a minimum generation of CPU family for the master/worker. If not specified, GCP will default to a predetermined computed value for each zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param num_instances: Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        value = DataprocClusterClusterConfigWorkerConfig(
            accelerators=accelerators,
            disk_config=disk_config,
            image_uri=image_uri,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            num_instances=num_instances,
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerConfig", [value]))

    @jsii.member(jsii_name="resetAutoscalingConfig")
    def reset_autoscaling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingConfig", []))

    @jsii.member(jsii_name="resetEncryptionConfig")
    def reset_encryption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfig", []))

    @jsii.member(jsii_name="resetEndpointConfig")
    def reset_endpoint_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointConfig", []))

    @jsii.member(jsii_name="resetGceClusterConfig")
    def reset_gce_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGceClusterConfig", []))

    @jsii.member(jsii_name="resetInitializationAction")
    def reset_initialization_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializationAction", []))

    @jsii.member(jsii_name="resetLifecycleConfig")
    def reset_lifecycle_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfig", []))

    @jsii.member(jsii_name="resetMasterConfig")
    def reset_master_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterConfig", []))

    @jsii.member(jsii_name="resetMetastoreConfig")
    def reset_metastore_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastoreConfig", []))

    @jsii.member(jsii_name="resetPreemptibleWorkerConfig")
    def reset_preemptible_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptibleWorkerConfig", []))

    @jsii.member(jsii_name="resetSecurityConfig")
    def reset_security_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfig", []))

    @jsii.member(jsii_name="resetSoftwareConfig")
    def reset_software_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareConfig", []))

    @jsii.member(jsii_name="resetStagingBucket")
    def reset_staging_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagingBucket", []))

    @jsii.member(jsii_name="resetTempBucket")
    def reset_temp_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTempBucket", []))

    @jsii.member(jsii_name="resetWorkerConfig")
    def reset_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> DataprocClusterClusterConfigAutoscalingConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigAutoscalingConfigOutputReference, jsii.get(self, "autoscalingConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> DataprocClusterClusterConfigEncryptionConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigEncryptionConfigOutputReference, jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfig")
    def endpoint_config(
        self,
    ) -> DataprocClusterClusterConfigEndpointConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigEndpointConfigOutputReference, jsii.get(self, "endpointConfig"))

    @builtins.property
    @jsii.member(jsii_name="gceClusterConfig")
    def gce_cluster_config(
        self,
    ) -> DataprocClusterClusterConfigGceClusterConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigGceClusterConfigOutputReference, jsii.get(self, "gceClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="initializationAction")
    def initialization_action(
        self,
    ) -> DataprocClusterClusterConfigInitializationActionList:
        return typing.cast(DataprocClusterClusterConfigInitializationActionList, jsii.get(self, "initializationAction"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfig")
    def lifecycle_config(
        self,
    ) -> DataprocClusterClusterConfigLifecycleConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigLifecycleConfigOutputReference, jsii.get(self, "lifecycleConfig"))

    @builtins.property
    @jsii.member(jsii_name="masterConfig")
    def master_config(self) -> DataprocClusterClusterConfigMasterConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigMasterConfigOutputReference, jsii.get(self, "masterConfig"))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfig")
    def metastore_config(
        self,
    ) -> DataprocClusterClusterConfigMetastoreConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigMetastoreConfigOutputReference, jsii.get(self, "metastoreConfig"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleWorkerConfig")
    def preemptible_worker_config(
        self,
    ) -> "DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference", jsii.get(self, "preemptibleWorkerConfig"))

    @builtins.property
    @jsii.member(jsii_name="securityConfig")
    def security_config(
        self,
    ) -> "DataprocClusterClusterConfigSecurityConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigSecurityConfigOutputReference", jsii.get(self, "securityConfig"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfig")
    def software_config(
        self,
    ) -> "DataprocClusterClusterConfigSoftwareConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigSoftwareConfigOutputReference", jsii.get(self, "softwareConfig"))

    @builtins.property
    @jsii.member(jsii_name="workerConfig")
    def worker_config(
        self,
    ) -> "DataprocClusterClusterConfigWorkerConfigOutputReference":
        return typing.cast("DataprocClusterClusterConfigWorkerConfigOutputReference", jsii.get(self, "workerConfig"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfigInput")
    def autoscaling_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigAutoscalingConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigAutoscalingConfig], jsii.get(self, "autoscalingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigEncryptionConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigEncryptionConfig], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigInput")
    def endpoint_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigEndpointConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigEndpointConfig], jsii.get(self, "endpointConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gceClusterConfigInput")
    def gce_cluster_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigGceClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigGceClusterConfig], jsii.get(self, "gceClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="initializationActionInput")
    def initialization_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigInitializationAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigInitializationAction]]], jsii.get(self, "initializationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigInput")
    def lifecycle_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigLifecycleConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigLifecycleConfig], jsii.get(self, "lifecycleConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="masterConfigInput")
    def master_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMasterConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMasterConfig], jsii.get(self, "masterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfigInput")
    def metastore_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigMetastoreConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigMetastoreConfig], jsii.get(self, "metastoreConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleWorkerConfigInput")
    def preemptible_worker_config_input(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfig"], jsii.get(self, "preemptibleWorkerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigInput")
    def security_config_input(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigSecurityConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfigSecurityConfig"], jsii.get(self, "securityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfigInput")
    def software_config_input(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigSoftwareConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfigSoftwareConfig"], jsii.get(self, "softwareConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucketInput")
    def staging_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stagingBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="tempBucketInput")
    def temp_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tempBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigInput")
    def worker_config_input(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigWorkerConfig"]:
        return typing.cast(typing.Optional["DataprocClusterClusterConfigWorkerConfig"], jsii.get(self, "workerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucket")
    def staging_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingBucket"))

    @staging_bucket.setter
    def staging_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigOutputReference, "staging_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingBucket", value)

    @builtins.property
    @jsii.member(jsii_name="tempBucket")
    def temp_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tempBucket"))

    @temp_bucket.setter
    def temp_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigOutputReference, "temp_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tempBucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataprocClusterClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigPreemptibleWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "disk_config": "diskConfig",
        "num_instances": "numInstances",
        "preemptibility": "preemptibility",
    },
)
class DataprocClusterClusterConfigPreemptibleWorkerConfig:
    def __init__(
        self,
        *,
        disk_config: typing.Optional[typing.Union["DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param num_instances: Specifies the number of preemptible nodes to create. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        :param preemptibility: Specifies the preemptibility of the secondary nodes. Defaults to PREEMPTIBLE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptibility DataprocCluster#preemptibility}
        '''
        if isinstance(disk_config, dict):
            disk_config = DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigPreemptibleWorkerConfig.__init__)
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
            check_type(argname="argument preemptibility", value=preemptibility, expected_type=type_hints["preemptibility"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if num_instances is not None:
            self._values["num_instances"] = num_instances
        if preemptibility is not None:
            self._values["preemptibility"] = preemptibility

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig"], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of preemptible nodes to create. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preemptibility(self) -> typing.Optional[builtins.str]:
        '''Specifies the preemptibility of the secondary nodes. Defaults to PREEMPTIBLE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptibility DataprocCluster#preemptibility}
        '''
        result = self._values.get("preemptibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigPreemptibleWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each preemptible worker node, specified in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each preemptible worker node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each preemptible worker node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the primary disk attached to each preemptible worker node, specified in GB.

        The smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''The disk type of the primary disk attached to each preemptible worker node.

        Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''The amount of local SSD disks that will be attached to each preemptible worker node. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each preemptible worker node, specified in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each preemptible worker node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each preemptible worker node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        value = DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @jsii.member(jsii_name="resetPreemptibility")
    def reset_preemptibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptibility", []))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibilityInput")
    def preemptibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preemptibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="preemptibility")
    def preemptibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preemptibility"))

    @preemptibility.setter
    def preemptibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference, "preemptibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigPreemptibleWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSecurityConfig",
    jsii_struct_bases=[],
    name_mapping={"kerberos_config": "kerberosConfig"},
)
class DataprocClusterClusterConfigSecurityConfig:
    def __init__(
        self,
        *,
        kerberos_config: typing.Union["DataprocClusterClusterConfigSecurityConfigKerberosConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param kerberos_config: kerberos_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kerberos_config DataprocCluster#kerberos_config}
        '''
        if isinstance(kerberos_config, dict):
            kerberos_config = DataprocClusterClusterConfigSecurityConfigKerberosConfig(**kerberos_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSecurityConfig.__init__)
            check_type(argname="argument kerberos_config", value=kerberos_config, expected_type=type_hints["kerberos_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "kerberos_config": kerberos_config,
        }

    @builtins.property
    def kerberos_config(
        self,
    ) -> "DataprocClusterClusterConfigSecurityConfigKerberosConfig":
        '''kerberos_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kerberos_config DataprocCluster#kerberos_config}
        '''
        result = self._values.get("kerberos_config")
        assert result is not None, "Required property 'kerberos_config' is missing"
        return typing.cast("DataprocClusterClusterConfigSecurityConfigKerberosConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigSecurityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSecurityConfigKerberosConfig",
    jsii_struct_bases=[],
    name_mapping={
        "kms_key_uri": "kmsKeyUri",
        "root_principal_password_uri": "rootPrincipalPasswordUri",
        "cross_realm_trust_admin_server": "crossRealmTrustAdminServer",
        "cross_realm_trust_kdc": "crossRealmTrustKdc",
        "cross_realm_trust_realm": "crossRealmTrustRealm",
        "cross_realm_trust_shared_password_uri": "crossRealmTrustSharedPasswordUri",
        "enable_kerberos": "enableKerberos",
        "kdc_db_key_uri": "kdcDbKeyUri",
        "key_password_uri": "keyPasswordUri",
        "keystore_password_uri": "keystorePasswordUri",
        "keystore_uri": "keystoreUri",
        "realm": "realm",
        "tgt_lifetime_hours": "tgtLifetimeHours",
        "truststore_password_uri": "truststorePasswordUri",
        "truststore_uri": "truststoreUri",
    },
)
class DataprocClusterClusterConfigSecurityConfigKerberosConfig:
    def __init__(
        self,
        *,
        kms_key_uri: builtins.str,
        root_principal_password_uri: builtins.str,
        cross_realm_trust_admin_server: typing.Optional[builtins.str] = None,
        cross_realm_trust_kdc: typing.Optional[builtins.str] = None,
        cross_realm_trust_realm: typing.Optional[builtins.str] = None,
        cross_realm_trust_shared_password_uri: typing.Optional[builtins.str] = None,
        enable_kerberos: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kdc_db_key_uri: typing.Optional[builtins.str] = None,
        key_password_uri: typing.Optional[builtins.str] = None,
        keystore_password_uri: typing.Optional[builtins.str] = None,
        keystore_uri: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        tgt_lifetime_hours: typing.Optional[jsii.Number] = None,
        truststore_password_uri: typing.Optional[builtins.str] = None,
        truststore_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_uri: The uri of the KMS key used to encrypt various sensitive files. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_uri DataprocCluster#kms_key_uri}
        :param root_principal_password_uri: The cloud Storage URI of a KMS encrypted file containing the root principal password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#root_principal_password_uri DataprocCluster#root_principal_password_uri}
        :param cross_realm_trust_admin_server: The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_admin_server DataprocCluster#cross_realm_trust_admin_server}
        :param cross_realm_trust_kdc: The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_kdc DataprocCluster#cross_realm_trust_kdc}
        :param cross_realm_trust_realm: The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_realm DataprocCluster#cross_realm_trust_realm}
        :param cross_realm_trust_shared_password_uri: The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_shared_password_uri DataprocCluster#cross_realm_trust_shared_password_uri}
        :param enable_kerberos: Flag to indicate whether to Kerberize the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_kerberos DataprocCluster#enable_kerberos}
        :param kdc_db_key_uri: The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kdc_db_key_uri DataprocCluster#kdc_db_key_uri}
        :param key_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#key_password_uri DataprocCluster#key_password_uri}
        :param keystore_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore. For the self-signed certificate, this password is generated by Dataproc Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_password_uri DataprocCluster#keystore_password_uri}
        :param keystore_uri: The Cloud Storage URI of the keystore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_uri DataprocCluster#keystore_uri}
        :param realm: The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#realm DataprocCluster#realm}
        :param tgt_lifetime_hours: The lifetime of the ticket granting ticket, in hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tgt_lifetime_hours DataprocCluster#tgt_lifetime_hours}
        :param truststore_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_password_uri DataprocCluster#truststore_password_uri}
        :param truststore_uri: The Cloud Storage URI of the truststore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_uri DataprocCluster#truststore_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSecurityConfigKerberosConfig.__init__)
            check_type(argname="argument kms_key_uri", value=kms_key_uri, expected_type=type_hints["kms_key_uri"])
            check_type(argname="argument root_principal_password_uri", value=root_principal_password_uri, expected_type=type_hints["root_principal_password_uri"])
            check_type(argname="argument cross_realm_trust_admin_server", value=cross_realm_trust_admin_server, expected_type=type_hints["cross_realm_trust_admin_server"])
            check_type(argname="argument cross_realm_trust_kdc", value=cross_realm_trust_kdc, expected_type=type_hints["cross_realm_trust_kdc"])
            check_type(argname="argument cross_realm_trust_realm", value=cross_realm_trust_realm, expected_type=type_hints["cross_realm_trust_realm"])
            check_type(argname="argument cross_realm_trust_shared_password_uri", value=cross_realm_trust_shared_password_uri, expected_type=type_hints["cross_realm_trust_shared_password_uri"])
            check_type(argname="argument enable_kerberos", value=enable_kerberos, expected_type=type_hints["enable_kerberos"])
            check_type(argname="argument kdc_db_key_uri", value=kdc_db_key_uri, expected_type=type_hints["kdc_db_key_uri"])
            check_type(argname="argument key_password_uri", value=key_password_uri, expected_type=type_hints["key_password_uri"])
            check_type(argname="argument keystore_password_uri", value=keystore_password_uri, expected_type=type_hints["keystore_password_uri"])
            check_type(argname="argument keystore_uri", value=keystore_uri, expected_type=type_hints["keystore_uri"])
            check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
            check_type(argname="argument tgt_lifetime_hours", value=tgt_lifetime_hours, expected_type=type_hints["tgt_lifetime_hours"])
            check_type(argname="argument truststore_password_uri", value=truststore_password_uri, expected_type=type_hints["truststore_password_uri"])
            check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_uri": kms_key_uri,
            "root_principal_password_uri": root_principal_password_uri,
        }
        if cross_realm_trust_admin_server is not None:
            self._values["cross_realm_trust_admin_server"] = cross_realm_trust_admin_server
        if cross_realm_trust_kdc is not None:
            self._values["cross_realm_trust_kdc"] = cross_realm_trust_kdc
        if cross_realm_trust_realm is not None:
            self._values["cross_realm_trust_realm"] = cross_realm_trust_realm
        if cross_realm_trust_shared_password_uri is not None:
            self._values["cross_realm_trust_shared_password_uri"] = cross_realm_trust_shared_password_uri
        if enable_kerberos is not None:
            self._values["enable_kerberos"] = enable_kerberos
        if kdc_db_key_uri is not None:
            self._values["kdc_db_key_uri"] = kdc_db_key_uri
        if key_password_uri is not None:
            self._values["key_password_uri"] = key_password_uri
        if keystore_password_uri is not None:
            self._values["keystore_password_uri"] = keystore_password_uri
        if keystore_uri is not None:
            self._values["keystore_uri"] = keystore_uri
        if realm is not None:
            self._values["realm"] = realm
        if tgt_lifetime_hours is not None:
            self._values["tgt_lifetime_hours"] = tgt_lifetime_hours
        if truststore_password_uri is not None:
            self._values["truststore_password_uri"] = truststore_password_uri
        if truststore_uri is not None:
            self._values["truststore_uri"] = truststore_uri

    @builtins.property
    def kms_key_uri(self) -> builtins.str:
        '''The uri of the KMS key used to encrypt various sensitive files.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_uri DataprocCluster#kms_key_uri}
        '''
        result = self._values.get("kms_key_uri")
        assert result is not None, "Required property 'kms_key_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_principal_password_uri(self) -> builtins.str:
        '''The cloud Storage URI of a KMS encrypted file containing the root principal password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#root_principal_password_uri DataprocCluster#root_principal_password_uri}
        '''
        result = self._values.get("root_principal_password_uri")
        assert result is not None, "Required property 'root_principal_password_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_realm_trust_admin_server(self) -> typing.Optional[builtins.str]:
        '''The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_admin_server DataprocCluster#cross_realm_trust_admin_server}
        '''
        result = self._values.get("cross_realm_trust_admin_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_kdc(self) -> typing.Optional[builtins.str]:
        '''The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_kdc DataprocCluster#cross_realm_trust_kdc}
        '''
        result = self._values.get("cross_realm_trust_kdc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_realm(self) -> typing.Optional[builtins.str]:
        '''The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_realm DataprocCluster#cross_realm_trust_realm}
        '''
        result = self._values.get("cross_realm_trust_realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_shared_password_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_shared_password_uri DataprocCluster#cross_realm_trust_shared_password_uri}
        '''
        result = self._values.get("cross_realm_trust_shared_password_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_kerberos(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to indicate whether to Kerberize the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_kerberos DataprocCluster#enable_kerberos}
        '''
        result = self._values.get("enable_kerberos")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kdc_db_key_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kdc_db_key_uri DataprocCluster#kdc_db_key_uri}
        '''
        result = self._values.get("kdc_db_key_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_password_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key.

        For the self-signed certificate, this password is generated by Dataproc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#key_password_uri DataprocCluster#key_password_uri}
        '''
        result = self._values.get("key_password_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keystore_password_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore.

        For the self-signed certificate, this password is generated
        by Dataproc

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_password_uri DataprocCluster#keystore_password_uri}
        '''
        result = self._values.get("keystore_password_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keystore_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of the keystore file used for SSL encryption.

        If not provided, Dataproc will provide a self-signed certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_uri DataprocCluster#keystore_uri}
        '''
        result = self._values.get("keystore_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def realm(self) -> typing.Optional[builtins.str]:
        '''The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#realm DataprocCluster#realm}
        '''
        result = self._values.get("realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tgt_lifetime_hours(self) -> typing.Optional[jsii.Number]:
        '''The lifetime of the ticket granting ticket, in hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tgt_lifetime_hours DataprocCluster#tgt_lifetime_hours}
        '''
        result = self._values.get("tgt_lifetime_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def truststore_password_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore.

        For the self-signed certificate, this password is generated by Dataproc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_password_uri DataprocCluster#truststore_password_uri}
        '''
        result = self._values.get("truststore_password_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def truststore_uri(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage URI of the truststore file used for SSL encryption.

        If not provided, Dataproc will provide a self-signed certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_uri DataprocCluster#truststore_uri}
        '''
        result = self._values.get("truststore_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigSecurityConfigKerberosConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCrossRealmTrustAdminServer")
    def reset_cross_realm_trust_admin_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustAdminServer", []))

    @jsii.member(jsii_name="resetCrossRealmTrustKdc")
    def reset_cross_realm_trust_kdc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustKdc", []))

    @jsii.member(jsii_name="resetCrossRealmTrustRealm")
    def reset_cross_realm_trust_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustRealm", []))

    @jsii.member(jsii_name="resetCrossRealmTrustSharedPasswordUri")
    def reset_cross_realm_trust_shared_password_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustSharedPasswordUri", []))

    @jsii.member(jsii_name="resetEnableKerberos")
    def reset_enable_kerberos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableKerberos", []))

    @jsii.member(jsii_name="resetKdcDbKeyUri")
    def reset_kdc_db_key_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKdcDbKeyUri", []))

    @jsii.member(jsii_name="resetKeyPasswordUri")
    def reset_key_password_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPasswordUri", []))

    @jsii.member(jsii_name="resetKeystorePasswordUri")
    def reset_keystore_password_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeystorePasswordUri", []))

    @jsii.member(jsii_name="resetKeystoreUri")
    def reset_keystore_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeystoreUri", []))

    @jsii.member(jsii_name="resetRealm")
    def reset_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealm", []))

    @jsii.member(jsii_name="resetTgtLifetimeHours")
    def reset_tgt_lifetime_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTgtLifetimeHours", []))

    @jsii.member(jsii_name="resetTruststorePasswordUri")
    def reset_truststore_password_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststorePasswordUri", []))

    @jsii.member(jsii_name="resetTruststoreUri")
    def reset_truststore_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststoreUri", []))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustAdminServerInput")
    def cross_realm_trust_admin_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustAdminServerInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustKdcInput")
    def cross_realm_trust_kdc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustKdcInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustRealmInput")
    def cross_realm_trust_realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustRealmInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustSharedPasswordUriInput")
    def cross_realm_trust_shared_password_uri_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustSharedPasswordUriInput"))

    @builtins.property
    @jsii.member(jsii_name="enableKerberosInput")
    def enable_kerberos_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableKerberosInput"))

    @builtins.property
    @jsii.member(jsii_name="kdcDbKeyUriInput")
    def kdc_db_key_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kdcDbKeyUriInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPasswordUriInput")
    def key_password_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPasswordUriInput"))

    @builtins.property
    @jsii.member(jsii_name="keystorePasswordUriInput")
    def keystore_password_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keystorePasswordUriInput"))

    @builtins.property
    @jsii.member(jsii_name="keystoreUriInput")
    def keystore_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keystoreUriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyUriInput")
    def kms_key_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyUriInput"))

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="rootPrincipalPasswordUriInput")
    def root_principal_password_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootPrincipalPasswordUriInput"))

    @builtins.property
    @jsii.member(jsii_name="tgtLifetimeHoursInput")
    def tgt_lifetime_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tgtLifetimeHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="truststorePasswordUriInput")
    def truststore_password_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststorePasswordUriInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreUriInput")
    def truststore_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreUriInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustAdminServer"))

    @cross_realm_trust_admin_server.setter
    def cross_realm_trust_admin_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_admin_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustAdminServer", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustKdc"))

    @cross_realm_trust_kdc.setter
    def cross_realm_trust_kdc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_kdc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustKdc", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustRealm"))

    @cross_realm_trust_realm.setter
    def cross_realm_trust_realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_realm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustRealm", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustSharedPasswordUri")
    def cross_realm_trust_shared_password_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustSharedPasswordUri"))

    @cross_realm_trust_shared_password_uri.setter
    def cross_realm_trust_shared_password_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_shared_password_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustSharedPasswordUri", value)

    @builtins.property
    @jsii.member(jsii_name="enableKerberos")
    def enable_kerberos(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableKerberos"))

    @enable_kerberos.setter
    def enable_kerberos(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "enable_kerberos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableKerberos", value)

    @builtins.property
    @jsii.member(jsii_name="kdcDbKeyUri")
    def kdc_db_key_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kdcDbKeyUri"))

    @kdc_db_key_uri.setter
    def kdc_db_key_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "kdc_db_key_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kdcDbKeyUri", value)

    @builtins.property
    @jsii.member(jsii_name="keyPasswordUri")
    def key_password_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPasswordUri"))

    @key_password_uri.setter
    def key_password_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "key_password_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPasswordUri", value)

    @builtins.property
    @jsii.member(jsii_name="keystorePasswordUri")
    def keystore_password_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keystorePasswordUri"))

    @keystore_password_uri.setter
    def keystore_password_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "keystore_password_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keystorePasswordUri", value)

    @builtins.property
    @jsii.member(jsii_name="keystoreUri")
    def keystore_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keystoreUri"))

    @keystore_uri.setter
    def keystore_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "keystore_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keystoreUri", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyUri")
    def kms_key_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyUri"))

    @kms_key_uri.setter
    def kms_key_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "kms_key_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyUri", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "realm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="rootPrincipalPasswordUri")
    def root_principal_password_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootPrincipalPasswordUri"))

    @root_principal_password_uri.setter
    def root_principal_password_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "root_principal_password_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootPrincipalPasswordUri", value)

    @builtins.property
    @jsii.member(jsii_name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tgtLifetimeHours"))

    @tgt_lifetime_hours.setter
    def tgt_lifetime_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "tgt_lifetime_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tgtLifetimeHours", value)

    @builtins.property
    @jsii.member(jsii_name="truststorePasswordUri")
    def truststore_password_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststorePasswordUri"))

    @truststore_password_uri.setter
    def truststore_password_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "truststore_password_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststorePasswordUri", value)

    @builtins.property
    @jsii.member(jsii_name="truststoreUri")
    def truststore_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreUri"))

    @truststore_uri.setter
    def truststore_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "truststore_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigSecurityConfigKerberosConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigSecurityConfigKerberosConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigSecurityConfigKerberosConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigSecurityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSecurityConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSecurityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKerberosConfig")
    def put_kerberos_config(
        self,
        *,
        kms_key_uri: builtins.str,
        root_principal_password_uri: builtins.str,
        cross_realm_trust_admin_server: typing.Optional[builtins.str] = None,
        cross_realm_trust_kdc: typing.Optional[builtins.str] = None,
        cross_realm_trust_realm: typing.Optional[builtins.str] = None,
        cross_realm_trust_shared_password_uri: typing.Optional[builtins.str] = None,
        enable_kerberos: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kdc_db_key_uri: typing.Optional[builtins.str] = None,
        key_password_uri: typing.Optional[builtins.str] = None,
        keystore_password_uri: typing.Optional[builtins.str] = None,
        keystore_uri: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        tgt_lifetime_hours: typing.Optional[jsii.Number] = None,
        truststore_password_uri: typing.Optional[builtins.str] = None,
        truststore_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_uri: The uri of the KMS key used to encrypt various sensitive files. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kms_key_uri DataprocCluster#kms_key_uri}
        :param root_principal_password_uri: The cloud Storage URI of a KMS encrypted file containing the root principal password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#root_principal_password_uri DataprocCluster#root_principal_password_uri}
        :param cross_realm_trust_admin_server: The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_admin_server DataprocCluster#cross_realm_trust_admin_server}
        :param cross_realm_trust_kdc: The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_kdc DataprocCluster#cross_realm_trust_kdc}
        :param cross_realm_trust_realm: The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_realm DataprocCluster#cross_realm_trust_realm}
        :param cross_realm_trust_shared_password_uri: The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cross_realm_trust_shared_password_uri DataprocCluster#cross_realm_trust_shared_password_uri}
        :param enable_kerberos: Flag to indicate whether to Kerberize the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#enable_kerberos DataprocCluster#enable_kerberos}
        :param kdc_db_key_uri: The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kdc_db_key_uri DataprocCluster#kdc_db_key_uri}
        :param key_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#key_password_uri DataprocCluster#key_password_uri}
        :param keystore_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore. For the self-signed certificate, this password is generated by Dataproc Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_password_uri DataprocCluster#keystore_password_uri}
        :param keystore_uri: The Cloud Storage URI of the keystore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#keystore_uri DataprocCluster#keystore_uri}
        :param realm: The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#realm DataprocCluster#realm}
        :param tgt_lifetime_hours: The lifetime of the ticket granting ticket, in hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#tgt_lifetime_hours DataprocCluster#tgt_lifetime_hours}
        :param truststore_password_uri: The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_password_uri DataprocCluster#truststore_password_uri}
        :param truststore_uri: The Cloud Storage URI of the truststore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#truststore_uri DataprocCluster#truststore_uri}
        '''
        value = DataprocClusterClusterConfigSecurityConfigKerberosConfig(
            kms_key_uri=kms_key_uri,
            root_principal_password_uri=root_principal_password_uri,
            cross_realm_trust_admin_server=cross_realm_trust_admin_server,
            cross_realm_trust_kdc=cross_realm_trust_kdc,
            cross_realm_trust_realm=cross_realm_trust_realm,
            cross_realm_trust_shared_password_uri=cross_realm_trust_shared_password_uri,
            enable_kerberos=enable_kerberos,
            kdc_db_key_uri=kdc_db_key_uri,
            key_password_uri=key_password_uri,
            keystore_password_uri=keystore_password_uri,
            keystore_uri=keystore_uri,
            realm=realm,
            tgt_lifetime_hours=tgt_lifetime_hours,
            truststore_password_uri=truststore_password_uri,
            truststore_uri=truststore_uri,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberosConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="kerberosConfig")
    def kerberos_config(
        self,
    ) -> DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference, jsii.get(self, "kerberosConfig"))

    @builtins.property
    @jsii.member(jsii_name="kerberosConfigInput")
    def kerberos_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigSecurityConfigKerberosConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigSecurityConfigKerberosConfig], jsii.get(self, "kerberosConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigSecurityConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigSecurityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigSecurityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSecurityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSoftwareConfig",
    jsii_struct_bases=[],
    name_mapping={
        "image_version": "imageVersion",
        "optional_components": "optionalComponents",
        "override_properties": "overrideProperties",
    },
)
class DataprocClusterClusterConfigSoftwareConfig:
    def __init__(
        self,
        *,
        image_version: typing.Optional[builtins.str] = None,
        optional_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        override_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param image_version: The Cloud Dataproc image version to use for the cluster - this controls the sets of software versions installed onto the nodes when you create clusters. If not specified, defaults to the latest version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_version DataprocCluster#image_version}
        :param optional_components: The set of optional components to activate on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#optional_components DataprocCluster#optional_components}
        :param override_properties: A list of override and additional properties (key/value pairs) used to modify various aspects of the common configuration files used when creating a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#override_properties DataprocCluster#override_properties}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSoftwareConfig.__init__)
            check_type(argname="argument image_version", value=image_version, expected_type=type_hints["image_version"])
            check_type(argname="argument optional_components", value=optional_components, expected_type=type_hints["optional_components"])
            check_type(argname="argument override_properties", value=override_properties, expected_type=type_hints["override_properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if image_version is not None:
            self._values["image_version"] = image_version
        if optional_components is not None:
            self._values["optional_components"] = optional_components
        if override_properties is not None:
            self._values["override_properties"] = override_properties

    @builtins.property
    def image_version(self) -> typing.Optional[builtins.str]:
        '''The Cloud Dataproc image version to use for the cluster - this controls the sets of software versions installed onto the nodes when you create clusters.

        If not specified, defaults to the latest version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_version DataprocCluster#image_version}
        '''
        result = self._values.get("image_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional_components(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of optional components to activate on the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#optional_components DataprocCluster#optional_components}
        '''
        result = self._values.get("optional_components")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def override_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of override and additional properties (key/value pairs) used to modify various aspects of the common configuration files used when creating a cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#override_properties DataprocCluster#override_properties}
        '''
        result = self._values.get("override_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigSoftwareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigSoftwareConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigSoftwareConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigSoftwareConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetImageVersion")
    def reset_image_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersion", []))

    @jsii.member(jsii_name="resetOptionalComponents")
    def reset_optional_components(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionalComponents", []))

    @jsii.member(jsii_name="resetOverrideProperties")
    def reset_override_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideProperties", []))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "properties"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionInput")
    def image_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalComponentsInput")
    def optional_components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionalComponentsInput"))

    @builtins.property
    @jsii.member(jsii_name="overridePropertiesInput")
    def override_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "overridePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersion")
    def image_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageVersion"))

    @image_version.setter
    def image_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSoftwareConfigOutputReference, "image_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="optionalComponents")
    def optional_components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "optionalComponents"))

    @optional_components.setter
    def optional_components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSoftwareConfigOutputReference, "optional_components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalComponents", value)

    @builtins.property
    @jsii.member(jsii_name="overrideProperties")
    def override_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "overrideProperties"))

    @override_properties.setter
    def override_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSoftwareConfigOutputReference, "override_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigSoftwareConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigSoftwareConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigSoftwareConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigSoftwareConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "disk_config": "diskConfig",
        "image_uri": "imageUri",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "num_instances": "numInstances",
    },
)
class DataprocClusterClusterConfigWorkerConfig:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterClusterConfigWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["DataprocClusterClusterConfigWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        :param image_uri: The URI for the image to use for this master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        :param machine_type: The name of a Google Compute Engine machine type to create for the master/worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: The name of a minimum generation of CPU family for the master/worker. If not specified, GCP will default to a predetermined computed value for each zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param num_instances: Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        if isinstance(disk_config, dict):
            disk_config = DataprocClusterClusterConfigWorkerConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfig.__init__)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if num_instances is not None:
            self._values["num_instances"] = num_instances

    @builtins.property
    def accelerators(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigWorkerConfigAccelerators"]]]:
        '''accelerators block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerators DataprocCluster#accelerators}
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterClusterConfigWorkerConfigAccelerators"]]], result)

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["DataprocClusterClusterConfigWorkerConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#disk_config DataprocCluster#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["DataprocClusterClusterConfigWorkerConfigDiskConfig"], result)

    @builtins.property
    def image_uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the image to use for this master/worker.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#image_uri DataprocCluster#image_uri}
        '''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Google Compute Engine machine type to create for the master/worker.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''The name of a minimum generation of CPU family for the master/worker.

        If not specified, GCP will default to a predetermined computed value for each zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of master/worker nodes to create. If not specified, GCP will default to a predetermined computed value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_instances DataprocCluster#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigAccelerators",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_type": "acceleratorType",
    },
)
class DataprocClusterClusterConfigWorkerConfigAccelerators:
    def __init__(
        self,
        *,
        accelerator_count: jsii.Number,
        accelerator_type: builtins.str,
    ) -> None:
        '''
        :param accelerator_count: The number of the accelerator cards of this type exposed to this instance. Often restricted to one of 1, 2, 4, or 8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_count DataprocCluster#accelerator_count}
        :param accelerator_type: The short name of the accelerator type to expose to this instance. For example, nvidia-tesla-k80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_type DataprocCluster#accelerator_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigAccelerators.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_count": accelerator_count,
            "accelerator_type": accelerator_type,
        }

    @builtins.property
    def accelerator_count(self) -> jsii.Number:
        '''The number of the accelerator cards of this type exposed to this instance.

        Often restricted to one of 1, 2, 4, or 8.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_count DataprocCluster#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        assert result is not None, "Required property 'accelerator_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def accelerator_type(self) -> builtins.str:
        '''The short name of the accelerator type to expose to this instance. For example, nvidia-tesla-k80.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#accelerator_type DataprocCluster#accelerator_type}
        '''
        result = self._values.get("accelerator_type")
        assert result is not None, "Required property 'accelerator_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigWorkerConfigAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigWorkerConfigAcceleratorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigAcceleratorsList",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigAcceleratorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigAcceleratorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigWorkerConfigAccelerators]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigWorkerConfigAccelerators]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceleratorCount"))

    @accelerator_count.setter
    def accelerator_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference, "accelerator_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorCount", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference, "accelerator_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataprocClusterClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataprocClusterClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataprocClusterClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class DataprocClusterClusterConfigWorkerConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each node, specified in GB. The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the primary disk attached to each node, specified in GB.

        The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterClusterConfigWorkerConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigWorkerConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigWorkerConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterClusterConfigWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterClusterConfigWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccelerators")
    def put_accelerators(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterClusterConfigWorkerConfigAccelerators, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterClusterConfigWorkerConfigOutputReference.put_accelerators)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccelerators", [value]))

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Size of the primary disk attached to each node, specified in GB. The primary disk contains the boot volume and system libraries, and the smallest allowed disk size is 10GB. GCP will default to a predetermined computed value if not set (currently 500GB). Note: If SSDs are not attached, it also contains the HDFS data blocks and Hadoop working directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_size_gb DataprocCluster#boot_disk_size_gb}
        :param boot_disk_type: The disk type of the primary disk attached to each node. Such as "pd-ssd" or "pd-standard". Defaults to "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#boot_disk_type DataprocCluster#boot_disk_type}
        :param num_local_ssds: The amount of local SSD disks that will be attached to each master cluster node. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#num_local_ssds DataprocCluster#num_local_ssds}
        '''
        value = DataprocClusterClusterConfigWorkerConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetAccelerators")
    def reset_accelerators(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerators", []))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetImageUri")
    def reset_image_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageUri", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(self) -> DataprocClusterClusterConfigWorkerConfigAcceleratorsList:
        return typing.cast(DataprocClusterClusterConfigWorkerConfigAcceleratorsList, jsii.get(self, "accelerators"))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference:
        return typing.cast(DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorsInput")
    def accelerators_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterClusterConfigWorkerConfigAccelerators]]], jsii.get(self, "acceleratorsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigWorkerConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUriInput")
    def image_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigOutputReference, "image_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterClusterConfigWorkerConfig]:
        return typing.cast(typing.Optional[DataprocClusterClusterConfigWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterClusterConfigWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterClusterConfigWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterConfig",
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
        "cluster_config": "clusterConfig",
        "graceful_decommission_timeout": "gracefulDecommissionTimeout",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
        "virtual_cluster_config": "virtualClusterConfig",
    },
)
class DataprocClusterConfig(cdktf.TerraformMetaArguments):
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
        cluster_config: typing.Optional[typing.Union[DataprocClusterClusterConfig, typing.Dict[str, typing.Any]]] = None,
        graceful_decommission_timeout: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataprocClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_cluster_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the cluster, unique within the project and zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#name DataprocCluster#name}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cluster_config DataprocCluster#cluster_config}
        :param graceful_decommission_timeout: The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a terraform apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#graceful_decommission_timeout DataprocCluster#graceful_decommission_timeout}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#id DataprocCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The list of labels (key/value pairs) to be applied to instances in the cluster. GCP generates some itself including goog-dataproc-cluster-name which is the name of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#labels DataprocCluster#labels}
        :param project: The ID of the project in which the cluster will exist. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#project DataprocCluster#project}
        :param region: The region in which the cluster and associated nodes will be created in. Defaults to global. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#region DataprocCluster#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#timeouts DataprocCluster#timeouts}
        :param virtual_cluster_config: virtual_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#virtual_cluster_config DataprocCluster#virtual_cluster_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cluster_config, dict):
            cluster_config = DataprocClusterClusterConfig(**cluster_config)
        if isinstance(timeouts, dict):
            timeouts = DataprocClusterTimeouts(**timeouts)
        if isinstance(virtual_cluster_config, dict):
            virtual_cluster_config = DataprocClusterVirtualClusterConfig(**virtual_cluster_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cluster_config", value=cluster_config, expected_type=type_hints["cluster_config"])
            check_type(argname="argument graceful_decommission_timeout", value=graceful_decommission_timeout, expected_type=type_hints["graceful_decommission_timeout"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_cluster_config", value=virtual_cluster_config, expected_type=type_hints["virtual_cluster_config"])
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
        if cluster_config is not None:
            self._values["cluster_config"] = cluster_config
        if graceful_decommission_timeout is not None:
            self._values["graceful_decommission_timeout"] = graceful_decommission_timeout
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
        if virtual_cluster_config is not None:
            self._values["virtual_cluster_config"] = virtual_cluster_config

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
        '''The name of the cluster, unique within the project and zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#name DataprocCluster#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_config(self) -> typing.Optional[DataprocClusterClusterConfig]:
        '''cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#cluster_config DataprocCluster#cluster_config}
        '''
        result = self._values.get("cluster_config")
        return typing.cast(typing.Optional[DataprocClusterClusterConfig], result)

    @builtins.property
    def graceful_decommission_timeout(self) -> typing.Optional[builtins.str]:
        '''The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a terraform apply.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#graceful_decommission_timeout DataprocCluster#graceful_decommission_timeout}
        '''
        result = self._values.get("graceful_decommission_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#id DataprocCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of labels (key/value pairs) to be applied to instances in the cluster.

        GCP generates some itself including goog-dataproc-cluster-name which is the name of the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#labels DataprocCluster#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the cluster will exist.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#project DataprocCluster#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region in which the cluster and associated nodes will be created in. Defaults to global.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#region DataprocCluster#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataprocClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#timeouts DataprocCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataprocClusterTimeouts"], result)

    @builtins.property
    def virtual_cluster_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfig"]:
        '''virtual_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#virtual_cluster_config DataprocCluster#virtual_cluster_config}
        '''
        result = self._values.get("virtual_cluster_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DataprocClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#create DataprocCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#delete DataprocCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#update DataprocCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#create DataprocCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#delete DataprocCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#update DataprocCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataprocClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataprocClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataprocClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "auxiliary_services_config": "auxiliaryServicesConfig",
        "kubernetes_cluster_config": "kubernetesClusterConfig",
        "staging_bucket": "stagingBucket",
    },
)
class DataprocClusterVirtualClusterConfig:
    def __init__(
        self,
        *,
        auxiliary_services_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig", typing.Dict[str, typing.Any]]] = None,
        kubernetes_cluster_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfig", typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auxiliary_services_config: auxiliary_services_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auxiliary_services_config DataprocCluster#auxiliary_services_config}
        :param kubernetes_cluster_config: kubernetes_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_cluster_config DataprocCluster#kubernetes_cluster_config}
        :param staging_bucket: A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        '''
        if isinstance(auxiliary_services_config, dict):
            auxiliary_services_config = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig(**auxiliary_services_config)
        if isinstance(kubernetes_cluster_config, dict):
            kubernetes_cluster_config = DataprocClusterVirtualClusterConfigKubernetesClusterConfig(**kubernetes_cluster_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfig.__init__)
            check_type(argname="argument auxiliary_services_config", value=auxiliary_services_config, expected_type=type_hints["auxiliary_services_config"])
            check_type(argname="argument kubernetes_cluster_config", value=kubernetes_cluster_config, expected_type=type_hints["kubernetes_cluster_config"])
            check_type(argname="argument staging_bucket", value=staging_bucket, expected_type=type_hints["staging_bucket"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auxiliary_services_config is not None:
            self._values["auxiliary_services_config"] = auxiliary_services_config
        if kubernetes_cluster_config is not None:
            self._values["kubernetes_cluster_config"] = kubernetes_cluster_config
        if staging_bucket is not None:
            self._values["staging_bucket"] = staging_bucket

    @builtins.property
    def auxiliary_services_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig"]:
        '''auxiliary_services_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#auxiliary_services_config DataprocCluster#auxiliary_services_config}
        '''
        result = self._values.get("auxiliary_services_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig"], result)

    @builtins.property
    def kubernetes_cluster_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfig"]:
        '''kubernetes_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_cluster_config DataprocCluster#kubernetes_cluster_config}
        '''
        result = self._values.get("kubernetes_cluster_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfig"], result)

    @builtins.property
    def staging_bucket(self) -> typing.Optional[builtins.str]:
        '''A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output.

        If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#staging_bucket DataprocCluster#staging_bucket}
        '''
        result = self._values.get("staging_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metastore_config": "metastoreConfig",
        "spark_history_server_config": "sparkHistoryServerConfig",
    },
)
class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig:
    def __init__(
        self,
        *,
        metastore_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig", typing.Dict[str, typing.Any]]] = None,
        spark_history_server_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        :param spark_history_server_config: spark_history_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spark_history_server_config DataprocCluster#spark_history_server_config}
        '''
        if isinstance(metastore_config, dict):
            metastore_config = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig(**metastore_config)
        if isinstance(spark_history_server_config, dict):
            spark_history_server_config = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig(**spark_history_server_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig.__init__)
            check_type(argname="argument metastore_config", value=metastore_config, expected_type=type_hints["metastore_config"])
            check_type(argname="argument spark_history_server_config", value=spark_history_server_config, expected_type=type_hints["spark_history_server_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metastore_config is not None:
            self._values["metastore_config"] = metastore_config
        if spark_history_server_config is not None:
            self._values["spark_history_server_config"] = spark_history_server_config

    @builtins.property
    def metastore_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig"]:
        '''metastore_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        '''
        result = self._values.get("metastore_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig"], result)

    @builtins.property
    def spark_history_server_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig"]:
        '''spark_history_server_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spark_history_server_config DataprocCluster#spark_history_server_config}
        '''
        result = self._values.get("spark_history_server_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig",
    jsii_struct_bases=[],
    name_mapping={"dataproc_metastore_service": "dataprocMetastoreService"},
)
class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig:
    def __init__(
        self,
        *,
        dataproc_metastore_service: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataproc_metastore_service: The Hive Metastore configuration for this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig.__init__)
            check_type(argname="argument dataproc_metastore_service", value=dataproc_metastore_service, expected_type=type_hints["dataproc_metastore_service"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dataproc_metastore_service is not None:
            self._values["dataproc_metastore_service"] = dataproc_metastore_service

    @builtins.property
    def dataproc_metastore_service(self) -> typing.Optional[builtins.str]:
        '''The Hive Metastore configuration for this workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        result = self._values.get("dataproc_metastore_service")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataprocMetastoreService")
    def reset_dataproc_metastore_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataprocMetastoreService", []))

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreServiceInput")
    def dataproc_metastore_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataprocMetastoreServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataprocMetastoreService"))

    @dataproc_metastore_service.setter
    def dataproc_metastore_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference, "dataproc_metastore_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataprocMetastoreService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetastoreConfig")
    def put_metastore_config(
        self,
        *,
        dataproc_metastore_service: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataproc_metastore_service: The Hive Metastore configuration for this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_metastore_service DataprocCluster#dataproc_metastore_service}
        '''
        value = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig(
            dataproc_metastore_service=dataproc_metastore_service
        )

        return typing.cast(None, jsii.invoke(self, "putMetastoreConfig", [value]))

    @jsii.member(jsii_name="putSparkHistoryServerConfig")
    def put_spark_history_server_config(
        self,
        *,
        dataproc_cluster: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataproc_cluster: Resource name of an existing Dataproc Cluster to act as a Spark History Server for the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_cluster DataprocCluster#dataproc_cluster}
        '''
        value = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig(
            dataproc_cluster=dataproc_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putSparkHistoryServerConfig", [value]))

    @jsii.member(jsii_name="resetMetastoreConfig")
    def reset_metastore_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastoreConfig", []))

    @jsii.member(jsii_name="resetSparkHistoryServerConfig")
    def reset_spark_history_server_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkHistoryServerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfig")
    def metastore_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference, jsii.get(self, "metastoreConfig"))

    @builtins.property
    @jsii.member(jsii_name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference":
        return typing.cast("DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference", jsii.get(self, "sparkHistoryServerConfig"))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfigInput")
    def metastore_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig], jsii.get(self, "metastoreConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkHistoryServerConfigInput")
    def spark_history_server_config_input(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig"]:
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig"], jsii.get(self, "sparkHistoryServerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig",
    jsii_struct_bases=[],
    name_mapping={"dataproc_cluster": "dataprocCluster"},
)
class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig:
    def __init__(
        self,
        *,
        dataproc_cluster: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataproc_cluster: Resource name of an existing Dataproc Cluster to act as a Spark History Server for the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_cluster DataprocCluster#dataproc_cluster}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig.__init__)
            check_type(argname="argument dataproc_cluster", value=dataproc_cluster, expected_type=type_hints["dataproc_cluster"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dataproc_cluster is not None:
            self._values["dataproc_cluster"] = dataproc_cluster

    @builtins.property
    def dataproc_cluster(self) -> typing.Optional[builtins.str]:
        '''Resource name of an existing Dataproc Cluster to act as a Spark History Server for the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#dataproc_cluster DataprocCluster#dataproc_cluster}
        '''
        result = self._values.get("dataproc_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataprocCluster")
    def reset_dataproc_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataprocCluster", []))

    @builtins.property
    @jsii.member(jsii_name="dataprocClusterInput")
    def dataproc_cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataprocClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="dataprocCluster")
    def dataproc_cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataprocCluster"))

    @dataproc_cluster.setter
    def dataproc_cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference, "dataproc_cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataprocCluster", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gke_cluster_config": "gkeClusterConfig",
        "kubernetes_software_config": "kubernetesSoftwareConfig",
        "kubernetes_namespace": "kubernetesNamespace",
    },
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfig:
    def __init__(
        self,
        *,
        gke_cluster_config: typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig", typing.Dict[str, typing.Any]],
        kubernetes_software_config: typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig", typing.Dict[str, typing.Any]],
        kubernetes_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gke_cluster_config: gke_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_config DataprocCluster#gke_cluster_config}
        :param kubernetes_software_config: kubernetes_software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_software_config DataprocCluster#kubernetes_software_config}
        :param kubernetes_namespace: A namespace within the Kubernetes cluster to deploy into. If this namespace does not exist, it is created. If it exists, Dataproc verifies that another Dataproc VirtualCluster is not installed into it. If not specified, the name of the Dataproc Cluster is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_namespace DataprocCluster#kubernetes_namespace}
        '''
        if isinstance(gke_cluster_config, dict):
            gke_cluster_config = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig(**gke_cluster_config)
        if isinstance(kubernetes_software_config, dict):
            kubernetes_software_config = DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig(**kubernetes_software_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfig.__init__)
            check_type(argname="argument gke_cluster_config", value=gke_cluster_config, expected_type=type_hints["gke_cluster_config"])
            check_type(argname="argument kubernetes_software_config", value=kubernetes_software_config, expected_type=type_hints["kubernetes_software_config"])
            check_type(argname="argument kubernetes_namespace", value=kubernetes_namespace, expected_type=type_hints["kubernetes_namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "gke_cluster_config": gke_cluster_config,
            "kubernetes_software_config": kubernetes_software_config,
        }
        if kubernetes_namespace is not None:
            self._values["kubernetes_namespace"] = kubernetes_namespace

    @builtins.property
    def gke_cluster_config(
        self,
    ) -> "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig":
        '''gke_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_config DataprocCluster#gke_cluster_config}
        '''
        result = self._values.get("gke_cluster_config")
        assert result is not None, "Required property 'gke_cluster_config' is missing"
        return typing.cast("DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig", result)

    @builtins.property
    def kubernetes_software_config(
        self,
    ) -> "DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig":
        '''kubernetes_software_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_software_config DataprocCluster#kubernetes_software_config}
        '''
        result = self._values.get("kubernetes_software_config")
        assert result is not None, "Required property 'kubernetes_software_config' is missing"
        return typing.cast("DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig", result)

    @builtins.property
    def kubernetes_namespace(self) -> typing.Optional[builtins.str]:
        '''A namespace within the Kubernetes cluster to deploy into.

        If this namespace does not exist, it is created. If it exists, Dataproc verifies that another Dataproc VirtualCluster is not installed into it. If not specified, the name of the Dataproc Cluster is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_namespace DataprocCluster#kubernetes_namespace}
        '''
        result = self._values.get("kubernetes_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gke_cluster_target": "gkeClusterTarget",
        "node_pool_target": "nodePoolTarget",
    },
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig:
    def __init__(
        self,
        *,
        gke_cluster_target: typing.Optional[builtins.str] = None,
        node_pool_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param gke_cluster_target: A target GKE cluster to deploy to. It must be in the same project and region as the Dataproc cluster (the GKE cluster can be zonal or regional). Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_target DataprocCluster#gke_cluster_target}
        :param node_pool_target: node_pool_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool_target DataprocCluster#node_pool_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig.__init__)
            check_type(argname="argument gke_cluster_target", value=gke_cluster_target, expected_type=type_hints["gke_cluster_target"])
            check_type(argname="argument node_pool_target", value=node_pool_target, expected_type=type_hints["node_pool_target"])
        self._values: typing.Dict[str, typing.Any] = {}
        if gke_cluster_target is not None:
            self._values["gke_cluster_target"] = gke_cluster_target
        if node_pool_target is not None:
            self._values["node_pool_target"] = node_pool_target

    @builtins.property
    def gke_cluster_target(self) -> typing.Optional[builtins.str]:
        '''A target GKE cluster to deploy to.

        It must be in the same project and region as the Dataproc cluster (the GKE cluster can be zonal or regional). Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_target DataprocCluster#gke_cluster_target}
        '''
        result = self._values.get("gke_cluster_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_pool_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget"]]]:
        '''node_pool_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool_target DataprocCluster#node_pool_target}
        '''
        result = self._values.get("node_pool_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget",
    jsii_struct_bases=[],
    name_mapping={
        "node_pool": "nodePool",
        "roles": "roles",
        "node_pool_config": "nodePoolConfig",
    },
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget:
    def __init__(
        self,
        *,
        node_pool: builtins.str,
        roles: typing.Sequence[builtins.str],
        node_pool_config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param node_pool: The target GKE node pool. Format: 'projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{nodePool}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool DataprocCluster#node_pool}
        :param roles: The roles associated with the GKE node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#roles DataprocCluster#roles}
        :param node_pool_config: node_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool_config DataprocCluster#node_pool_config}
        '''
        if isinstance(node_pool_config, dict):
            node_pool_config = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig(**node_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget.__init__)
            check_type(argname="argument node_pool", value=node_pool, expected_type=type_hints["node_pool"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument node_pool_config", value=node_pool_config, expected_type=type_hints["node_pool_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "node_pool": node_pool,
            "roles": roles,
        }
        if node_pool_config is not None:
            self._values["node_pool_config"] = node_pool_config

    @builtins.property
    def node_pool(self) -> builtins.str:
        '''The target GKE node pool. Format: 'projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{nodePool}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool DataprocCluster#node_pool}
        '''
        result = self._values.get("node_pool")
        assert result is not None, "Required property 'node_pool' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''The roles associated with the GKE node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#roles DataprocCluster#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def node_pool_config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig"]:
        '''node_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool_config DataprocCluster#node_pool_config}
        '''
        result = self._values.get("node_pool_config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "locations": "locations",
        "autoscaling": "autoscaling",
        "config": "config",
    },
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig:
    def __init__(
        self,
        *,
        locations: typing.Sequence[builtins.str],
        autoscaling: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling", typing.Dict[str, typing.Any]]] = None,
        config: typing.Optional[typing.Union["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param locations: The list of Compute Engine zones where node pool nodes associated with a Dataproc on GKE virtual cluster will be located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#locations DataprocCluster#locations}
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling DataprocCluster#autoscaling}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#config DataprocCluster#config}
        '''
        if isinstance(autoscaling, dict):
            autoscaling = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling(**autoscaling)
        if isinstance(config, dict):
            config = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig(**config)
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig.__init__)
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
        self._values: typing.Dict[str, typing.Any] = {
            "locations": locations,
        }
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if config is not None:
            self._values["config"] = config

    @builtins.property
    def locations(self) -> typing.List[builtins.str]:
        '''The list of Compute Engine zones where node pool nodes associated with a Dataproc on GKE virtual cluster will be located.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#locations DataprocCluster#locations}
        '''
        result = self._values.get("locations")
        assert result is not None, "Required property 'locations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def autoscaling(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling"]:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling DataprocCluster#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling"], result)

    @builtins.property
    def config(
        self,
    ) -> typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#config DataprocCluster#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling",
    jsii_struct_bases=[],
    name_mapping={"max_node_count": "maxNodeCount", "min_node_count": "minNodeCount"},
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling:
    def __init__(
        self,
        *,
        max_node_count: typing.Optional[jsii.Number] = None,
        min_node_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_node_count: The maximum number of nodes in the node pool. Must be >= minNodeCount, and must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#max_node_count DataprocCluster#max_node_count}
        :param min_node_count: The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_node_count DataprocCluster#min_node_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling.__init__)
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_node_count is not None:
            self._values["max_node_count"] = max_node_count
        if min_node_count is not None:
            self._values["min_node_count"] = min_node_count

    @builtins.property
    def max_node_count(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of nodes in the node pool. Must be >= minNodeCount, and must be > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#max_node_count DataprocCluster#max_node_count}
        '''
        result = self._values.get("max_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_node_count(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_node_count DataprocCluster#min_node_count}
        '''
        result = self._values.get("min_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxNodeCount")
    def reset_max_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNodeCount", []))

    @jsii.member(jsii_name="resetMinNodeCount")
    def reset_min_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNodeCount", []))

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
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference, "max_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference, "min_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig",
    jsii_struct_bases=[],
    name_mapping={
        "local_ssd_count": "localSsdCount",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "preemptible": "preemptible",
        "spot": "spot",
    },
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig:
    def __init__(
        self,
        *,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param local_ssd_count: The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#local_ssd_count DataprocCluster#local_ssd_count}
        :param machine_type: The name of a Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or a newer CPU platform. Specify the friendly names of CPU platforms, such as "Intel Haswell" or "Intel Sandy Bridge". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Preemptible nodes cannot be used in a node pool with the CONTROLLER role or in the DEFAULT node pool if the CONTROLLER role is not assigned (the DEFAULT node pool will assume the CONTROLLER role). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible DataprocCluster#preemptible}
        :param spot: Spot flag for enabling Spot VM, which is a rebrand of the existing preemptible flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spot DataprocCluster#spot}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig.__init__)
            check_type(argname="argument local_ssd_count", value=local_ssd_count, expected_type=type_hints["local_ssd_count"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument preemptible", value=preemptible, expected_type=type_hints["preemptible"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
        self._values: typing.Dict[str, typing.Any] = {}
        if local_ssd_count is not None:
            self._values["local_ssd_count"] = local_ssd_count
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if preemptible is not None:
            self._values["preemptible"] = preemptible
        if spot is not None:
            self._values["spot"] = spot

    @builtins.property
    def local_ssd_count(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#local_ssd_count DataprocCluster#local_ssd_count}
        '''
        result = self._values.get("local_ssd_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Compute Engine machine type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Minimum CPU platform to be used by this instance.

        The instance may be scheduled on the specified or a newer CPU platform. Specify the friendly names of CPU platforms, such as "Intel Haswell" or "Intel Sandy Bridge".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the nodes are created as preemptible VM instances.

        Preemptible nodes cannot be used in a node pool with the CONTROLLER role or in the DEFAULT node pool if the CONTROLLER role is not assigned (the DEFAULT node pool will assume the CONTROLLER role).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible DataprocCluster#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def spot(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Spot flag for enabling Spot VM, which is a rebrand of the existing preemptible flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spot DataprocCluster#spot}
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLocalSsdCount")
    def reset_local_ssd_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSsdCount", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetPreemptible")
    def reset_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptible", []))

    @jsii.member(jsii_name="resetSpot")
    def reset_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpot", []))

    @builtins.property
    @jsii.member(jsii_name="localSsdCountInput")
    def local_ssd_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localSsdCountInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleInput")
    def preemptible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInput")
    def spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "spotInput"))

    @builtins.property
    @jsii.member(jsii_name="localSsdCount")
    def local_ssd_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localSsdCount"))

    @local_ssd_count.setter
    def local_ssd_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "local_ssd_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localSsdCount", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

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
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "spot"))

    @spot.setter
    def spot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        max_node_count: typing.Optional[jsii.Number] = None,
        min_node_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_node_count: The maximum number of nodes in the node pool. Must be >= minNodeCount, and must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#max_node_count DataprocCluster#max_node_count}
        :param min_node_count: The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_node_count DataprocCluster#min_node_count}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling(
            max_node_count=max_node_count, min_node_count=min_node_count
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param local_ssd_count: The minimum number of nodes in the node pool. Must be >= 0 and <= maxNodeCount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#local_ssd_count DataprocCluster#local_ssd_count}
        :param machine_type: The name of a Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#machine_type DataprocCluster#machine_type}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or a newer CPU platform. Specify the friendly names of CPU platforms, such as "Intel Haswell" or "Intel Sandy Bridge". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#min_cpu_platform DataprocCluster#min_cpu_platform}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Preemptible nodes cannot be used in a node pool with the CONTROLLER role or in the DEFAULT node pool if the CONTROLLER role is not assigned (the DEFAULT node pool will assume the CONTROLLER role). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#preemptible DataprocCluster#preemptible}
        :param spot: Spot flag for enabling Spot VM, which is a rebrand of the existing preemptible flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spot DataprocCluster#spot}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig(
            local_ssd_count=local_ssd_count,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            preemptible=preemptible,
            spot=spot,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetAutoscaling")
    def reset_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaling", []))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference, jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locations"))

    @locations.setter
    def locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference, "locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNodePoolConfig")
    def put_node_pool_config(
        self,
        *,
        locations: typing.Sequence[builtins.str],
        autoscaling: typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling, typing.Dict[str, typing.Any]]] = None,
        config: typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param locations: The list of Compute Engine zones where node pool nodes associated with a Dataproc on GKE virtual cluster will be located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#locations DataprocCluster#locations}
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#autoscaling DataprocCluster#autoscaling}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#config DataprocCluster#config}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig(
            locations=locations, autoscaling=autoscaling, config=config
        )

        return typing.cast(None, jsii.invoke(self, "putNodePoolConfig", [value]))

    @jsii.member(jsii_name="resetNodePoolConfig")
    def reset_node_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePoolConfig", []))

    @builtins.property
    @jsii.member(jsii_name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference, jsii.get(self, "nodePoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolConfigInput")
    def node_pool_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig], jsii.get(self, "nodePoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolInput")
    def node_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePool")
    def node_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodePool"))

    @node_pool.setter
    def node_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference, "node_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodePool", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference, "roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodePoolTarget")
    def put_node_pool_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference.put_node_pool_target)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodePoolTarget", [value]))

    @jsii.member(jsii_name="resetGkeClusterTarget")
    def reset_gke_cluster_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGkeClusterTarget", []))

    @jsii.member(jsii_name="resetNodePoolTarget")
    def reset_node_pool_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePoolTarget", []))

    @builtins.property
    @jsii.member(jsii_name="nodePoolTarget")
    def node_pool_target(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList, jsii.get(self, "nodePoolTarget"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterTargetInput")
    def gke_cluster_target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolTargetInput")
    def node_pool_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]], jsii.get(self, "nodePoolTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterTarget")
    def gke_cluster_target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterTarget"))

    @gke_cluster_target.setter
    def gke_cluster_target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference, "gke_cluster_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterTarget", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig",
    jsii_struct_bases=[],
    name_mapping={"component_version": "componentVersion", "properties": "properties"},
)
class DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig:
    def __init__(
        self,
        *,
        component_version: typing.Mapping[builtins.str, builtins.str],
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param component_version: The components that should be installed in this Dataproc cluster. The key must be a string from the KubernetesComponent enumeration. The value is the version of the software to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#component_version DataprocCluster#component_version}
        :param properties: The properties to set on daemon config files. Property keys are specified in prefix:property format, for example spark:spark.kubernetes.container.image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#properties DataprocCluster#properties}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig.__init__)
            check_type(argname="argument component_version", value=component_version, expected_type=type_hints["component_version"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "component_version": component_version,
        }
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def component_version(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The components that should be installed in this Dataproc cluster.

        The key must be a string from the KubernetesComponent enumeration. The value is the version of the software to be installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#component_version DataprocCluster#component_version}
        '''
        result = self._values.get("component_version")
        assert result is not None, "Required property 'component_version' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The properties to set on daemon config files. Property keys are specified in prefix:property format, for example spark:spark.kubernetes.container.image.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#properties DataprocCluster#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="componentVersionInput")
    def component_version_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "componentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="componentVersion")
    def component_version(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "componentVersion"))

    @component_version.setter
    def component_version(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference, "component_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "componentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGkeClusterConfig")
    def put_gke_cluster_config(
        self,
        *,
        gke_cluster_target: typing.Optional[builtins.str] = None,
        node_pool_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param gke_cluster_target: A target GKE cluster to deploy to. It must be in the same project and region as the Dataproc cluster (the GKE cluster can be zonal or regional). Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_target DataprocCluster#gke_cluster_target}
        :param node_pool_target: node_pool_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#node_pool_target DataprocCluster#node_pool_target}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig(
            gke_cluster_target=gke_cluster_target, node_pool_target=node_pool_target
        )

        return typing.cast(None, jsii.invoke(self, "putGkeClusterConfig", [value]))

    @jsii.member(jsii_name="putKubernetesSoftwareConfig")
    def put_kubernetes_software_config(
        self,
        *,
        component_version: typing.Mapping[builtins.str, builtins.str],
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param component_version: The components that should be installed in this Dataproc cluster. The key must be a string from the KubernetesComponent enumeration. The value is the version of the software to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#component_version DataprocCluster#component_version}
        :param properties: The properties to set on daemon config files. Property keys are specified in prefix:property format, for example spark:spark.kubernetes.container.image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#properties DataprocCluster#properties}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig(
            component_version=component_version, properties=properties
        )

        return typing.cast(None, jsii.invoke(self, "putKubernetesSoftwareConfig", [value]))

    @jsii.member(jsii_name="resetKubernetesNamespace")
    def reset_kubernetes_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterConfig")
    def gke_cluster_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference, jsii.get(self, "gkeClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesSoftwareConfig")
    def kubernetes_software_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference, jsii.get(self, "kubernetesSoftwareConfig"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterConfigInput")
    def gke_cluster_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig], jsii.get(self, "gkeClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesNamespaceInput")
    def kubernetes_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesSoftwareConfigInput")
    def kubernetes_software_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig], jsii.get(self, "kubernetesSoftwareConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesNamespace")
    def kubernetes_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesNamespace"))

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference, "kubernetes_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataprocClusterVirtualClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.dataprocCluster.DataprocClusterVirtualClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataprocClusterVirtualClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuxiliaryServicesConfig")
    def put_auxiliary_services_config(
        self,
        *,
        metastore_config: typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig, typing.Dict[str, typing.Any]]] = None,
        spark_history_server_config: typing.Optional[typing.Union[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#metastore_config DataprocCluster#metastore_config}
        :param spark_history_server_config: spark_history_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#spark_history_server_config DataprocCluster#spark_history_server_config}
        '''
        value = DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig(
            metastore_config=metastore_config,
            spark_history_server_config=spark_history_server_config,
        )

        return typing.cast(None, jsii.invoke(self, "putAuxiliaryServicesConfig", [value]))

    @jsii.member(jsii_name="putKubernetesClusterConfig")
    def put_kubernetes_cluster_config(
        self,
        *,
        gke_cluster_config: typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig, typing.Dict[str, typing.Any]],
        kubernetes_software_config: typing.Union[DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig, typing.Dict[str, typing.Any]],
        kubernetes_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gke_cluster_config: gke_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#gke_cluster_config DataprocCluster#gke_cluster_config}
        :param kubernetes_software_config: kubernetes_software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_software_config DataprocCluster#kubernetes_software_config}
        :param kubernetes_namespace: A namespace within the Kubernetes cluster to deploy into. If this namespace does not exist, it is created. If it exists, Dataproc verifies that another Dataproc VirtualCluster is not installed into it. If not specified, the name of the Dataproc Cluster is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/dataproc_cluster#kubernetes_namespace DataprocCluster#kubernetes_namespace}
        '''
        value = DataprocClusterVirtualClusterConfigKubernetesClusterConfig(
            gke_cluster_config=gke_cluster_config,
            kubernetes_software_config=kubernetes_software_config,
            kubernetes_namespace=kubernetes_namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putKubernetesClusterConfig", [value]))

    @jsii.member(jsii_name="resetAuxiliaryServicesConfig")
    def reset_auxiliary_services_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuxiliaryServicesConfig", []))

    @jsii.member(jsii_name="resetKubernetesClusterConfig")
    def reset_kubernetes_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesClusterConfig", []))

    @jsii.member(jsii_name="resetStagingBucket")
    def reset_staging_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagingBucket", []))

    @builtins.property
    @jsii.member(jsii_name="auxiliaryServicesConfig")
    def auxiliary_services_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference, jsii.get(self, "auxiliaryServicesConfig"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesClusterConfig")
    def kubernetes_cluster_config(
        self,
    ) -> DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference:
        return typing.cast(DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference, jsii.get(self, "kubernetesClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="auxiliaryServicesConfigInput")
    def auxiliary_services_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig], jsii.get(self, "auxiliaryServicesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesClusterConfigInput")
    def kubernetes_cluster_config_input(
        self,
    ) -> typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfigKubernetesClusterConfig], jsii.get(self, "kubernetesClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucketInput")
    def staging_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stagingBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucket")
    def staging_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingBucket"))

    @staging_bucket.setter
    def staging_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigOutputReference, "staging_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingBucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataprocClusterVirtualClusterConfig]:
        return typing.cast(typing.Optional[DataprocClusterVirtualClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataprocClusterVirtualClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataprocClusterVirtualClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataprocCluster",
    "DataprocClusterClusterConfig",
    "DataprocClusterClusterConfigAutoscalingConfig",
    "DataprocClusterClusterConfigAutoscalingConfigOutputReference",
    "DataprocClusterClusterConfigEncryptionConfig",
    "DataprocClusterClusterConfigEncryptionConfigOutputReference",
    "DataprocClusterClusterConfigEndpointConfig",
    "DataprocClusterClusterConfigEndpointConfigOutputReference",
    "DataprocClusterClusterConfigGceClusterConfig",
    "DataprocClusterClusterConfigGceClusterConfigOutputReference",
    "DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfig",
    "DataprocClusterClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference",
    "DataprocClusterClusterConfigInitializationAction",
    "DataprocClusterClusterConfigInitializationActionList",
    "DataprocClusterClusterConfigInitializationActionOutputReference",
    "DataprocClusterClusterConfigLifecycleConfig",
    "DataprocClusterClusterConfigLifecycleConfigOutputReference",
    "DataprocClusterClusterConfigMasterConfig",
    "DataprocClusterClusterConfigMasterConfigAccelerators",
    "DataprocClusterClusterConfigMasterConfigAcceleratorsList",
    "DataprocClusterClusterConfigMasterConfigAcceleratorsOutputReference",
    "DataprocClusterClusterConfigMasterConfigDiskConfig",
    "DataprocClusterClusterConfigMasterConfigDiskConfigOutputReference",
    "DataprocClusterClusterConfigMasterConfigOutputReference",
    "DataprocClusterClusterConfigMetastoreConfig",
    "DataprocClusterClusterConfigMetastoreConfigOutputReference",
    "DataprocClusterClusterConfigOutputReference",
    "DataprocClusterClusterConfigPreemptibleWorkerConfig",
    "DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfig",
    "DataprocClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutputReference",
    "DataprocClusterClusterConfigPreemptibleWorkerConfigOutputReference",
    "DataprocClusterClusterConfigSecurityConfig",
    "DataprocClusterClusterConfigSecurityConfigKerberosConfig",
    "DataprocClusterClusterConfigSecurityConfigKerberosConfigOutputReference",
    "DataprocClusterClusterConfigSecurityConfigOutputReference",
    "DataprocClusterClusterConfigSoftwareConfig",
    "DataprocClusterClusterConfigSoftwareConfigOutputReference",
    "DataprocClusterClusterConfigWorkerConfig",
    "DataprocClusterClusterConfigWorkerConfigAccelerators",
    "DataprocClusterClusterConfigWorkerConfigAcceleratorsList",
    "DataprocClusterClusterConfigWorkerConfigAcceleratorsOutputReference",
    "DataprocClusterClusterConfigWorkerConfigDiskConfig",
    "DataprocClusterClusterConfigWorkerConfigDiskConfigOutputReference",
    "DataprocClusterClusterConfigWorkerConfigOutputReference",
    "DataprocClusterConfig",
    "DataprocClusterTimeouts",
    "DataprocClusterTimeoutsOutputReference",
    "DataprocClusterVirtualClusterConfig",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfig",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigOutputReference",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigOutputReference",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig",
    "DataprocClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfig",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetList",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigOutputReference",
    "DataprocClusterVirtualClusterConfigKubernetesClusterConfigOutputReference",
    "DataprocClusterVirtualClusterConfigOutputReference",
]

publication.publish()
