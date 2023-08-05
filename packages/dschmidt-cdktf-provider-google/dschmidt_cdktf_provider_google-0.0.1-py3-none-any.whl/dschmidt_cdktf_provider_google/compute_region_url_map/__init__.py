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


class ComputeRegionUrlMap(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMap",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map google_compute_region_url_map}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["ComputeRegionUrlMapDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        host_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        path_matcher: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        test: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ComputeRegionUrlMapTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map google_compute_region_url_map} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        :param default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_service ComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_url_redirect ComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        :param host_rule: host_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rule ComputeRegionUrlMap#host_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#id ComputeRegionUrlMap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_matcher: path_matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_matcher ComputeRegionUrlMap#path_matcher}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#project ComputeRegionUrlMap#project}.
        :param region: The Region in which the url map should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#region ComputeRegionUrlMap#region}
        :param test: test block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#test ComputeRegionUrlMap#test}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeouts ComputeRegionUrlMap#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMap.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeRegionUrlMapConfig(
            name=name,
            default_service=default_service,
            default_url_redirect=default_url_redirect,
            description=description,
            host_rule=host_rule,
            id=id,
            path_matcher=path_matcher,
            project=project,
            region=region,
            test=test,
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

    @jsii.member(jsii_name="putDefaultUrlRedirect")
    def put_default_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        value = ComputeRegionUrlMapDefaultUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUrlRedirect", [value]))

    @jsii.member(jsii_name="putHostRule")
    def put_host_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMap.put_host_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostRule", [value]))

    @jsii.member(jsii_name="putPathMatcher")
    def put_path_matcher(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMap.put_path_matcher)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPathMatcher", [value]))

    @jsii.member(jsii_name="putTest")
    def put_test(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMap.put_test)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTest", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#create ComputeRegionUrlMap#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delete ComputeRegionUrlMap#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#update ComputeRegionUrlMap#update}.
        '''
        value = ComputeRegionUrlMapTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDefaultService")
    def reset_default_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultService", []))

    @jsii.member(jsii_name="resetDefaultUrlRedirect")
    def reset_default_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultUrlRedirect", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHostRule")
    def reset_host_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRule", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPathMatcher")
    def reset_path_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathMatcher", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetTest")
    def reset_test(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTest", []))

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
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirect")
    def default_url_redirect(
        self,
    ) -> "ComputeRegionUrlMapDefaultUrlRedirectOutputReference":
        return typing.cast("ComputeRegionUrlMapDefaultUrlRedirectOutputReference", jsii.get(self, "defaultUrlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="hostRule")
    def host_rule(self) -> "ComputeRegionUrlMapHostRuleList":
        return typing.cast("ComputeRegionUrlMapHostRuleList", jsii.get(self, "hostRule"))

    @builtins.property
    @jsii.member(jsii_name="mapId")
    def map_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mapId"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcher")
    def path_matcher(self) -> "ComputeRegionUrlMapPathMatcherList":
        return typing.cast("ComputeRegionUrlMapPathMatcherList", jsii.get(self, "pathMatcher"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="test")
    def test(self) -> "ComputeRegionUrlMapTestList":
        return typing.cast("ComputeRegionUrlMapTestList", jsii.get(self, "test"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeRegionUrlMapTimeoutsOutputReference":
        return typing.cast("ComputeRegionUrlMapTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="defaultServiceInput")
    def default_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirectInput")
    def default_url_redirect_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapDefaultUrlRedirect"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapDefaultUrlRedirect"], jsii.get(self, "defaultUrlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRuleInput")
    def host_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapHostRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapHostRule"]]], jsii.get(self, "hostRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcherInput")
    def path_matcher_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcher"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcher"]]], jsii.get(self, "pathMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="testInput")
    def test_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapTest"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapTest"]]], jsii.get(self, "testInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeRegionUrlMapTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeRegionUrlMapTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultService")
    def default_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultService"))

    @default_service.setter
    def default_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "default_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultService", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMap, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapConfig",
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
        "default_service": "defaultService",
        "default_url_redirect": "defaultUrlRedirect",
        "description": "description",
        "host_rule": "hostRule",
        "id": "id",
        "path_matcher": "pathMatcher",
        "project": "project",
        "region": "region",
        "test": "test",
        "timeouts": "timeouts",
    },
)
class ComputeRegionUrlMapConfig(cdktf.TerraformMetaArguments):
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
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["ComputeRegionUrlMapDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        host_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        path_matcher: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        test: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ComputeRegionUrlMapTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        :param default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_service ComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_url_redirect ComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        :param host_rule: host_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rule ComputeRegionUrlMap#host_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#id ComputeRegionUrlMap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_matcher: path_matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_matcher ComputeRegionUrlMap#path_matcher}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#project ComputeRegionUrlMap#project}.
        :param region: The Region in which the url map should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#region ComputeRegionUrlMap#region}
        :param test: test block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#test ComputeRegionUrlMap#test}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeouts ComputeRegionUrlMap#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_url_redirect, dict):
            default_url_redirect = ComputeRegionUrlMapDefaultUrlRedirect(**default_url_redirect)
        if isinstance(timeouts, dict):
            timeouts = ComputeRegionUrlMapTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_service", value=default_service, expected_type=type_hints["default_service"])
            check_type(argname="argument default_url_redirect", value=default_url_redirect, expected_type=type_hints["default_url_redirect"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument host_rule", value=host_rule, expected_type=type_hints["host_rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path_matcher", value=path_matcher, expected_type=type_hints["path_matcher"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
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
        if default_service is not None:
            self._values["default_service"] = default_service
        if default_url_redirect is not None:
            self._values["default_url_redirect"] = default_url_redirect
        if description is not None:
            self._values["description"] = description
        if host_rule is not None:
            self._values["host_rule"] = host_rule
        if id is not None:
            self._values["id"] = id
        if path_matcher is not None:
            self._values["path_matcher"] = path_matcher
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if test is not None:
            self._values["test"] = test
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
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_service(self) -> typing.Optional[builtins.str]:
        '''The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match.

        If defaultRouteAction is additionally specified, advanced
        routing actions like URL Rewrites, etc. take effect prior to sending the request to the
        backend. However, if defaultService is specified, defaultRouteAction cannot contain any
        weightedBackendServices. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified.  Only one of defaultService,
        defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_service ComputeRegionUrlMap#default_service}
        '''
        result = self._values.get("default_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_url_redirect(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapDefaultUrlRedirect"]:
        '''default_url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_url_redirect ComputeRegionUrlMap#default_url_redirect}
        '''
        result = self._values.get("default_url_redirect")
        return typing.cast(typing.Optional["ComputeRegionUrlMapDefaultUrlRedirect"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapHostRule"]]]:
        '''host_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rule ComputeRegionUrlMap#host_rule}
        '''
        result = self._values.get("host_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapHostRule"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#id ComputeRegionUrlMap#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_matcher(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcher"]]]:
        '''path_matcher block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_matcher ComputeRegionUrlMap#path_matcher}
        '''
        result = self._values.get("path_matcher")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcher"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#project ComputeRegionUrlMap#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Region in which the url map should reside. If it is not provided, the provider region is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#region ComputeRegionUrlMap#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapTest"]]]:
        '''test block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#test ComputeRegionUrlMap#test}
        '''
        result = self._values.get("test")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapTest"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeRegionUrlMapTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeouts ComputeRegionUrlMap#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeRegionUrlMapTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapDefaultUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class ComputeRegionUrlMapDefaultUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapDefaultUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the original URL is
        retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to
        false, the URL scheme of the redirected request will remain the same as that of the
        request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this
        true for TargetHttpsProxy is not permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied together with
        prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the
        original request will be used for the redirect. The value must be between 1 and 1024
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or
        neither. If neither is supplied, the path of the original request will be used for
        the redirect. The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapDefaultUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapDefaultUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapDefaultUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapDefaultUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeRegionUrlMapDefaultUrlRedirect]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapDefaultUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapDefaultUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapDefaultUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapHostRule",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "path_matcher": "pathMatcher",
        "description": "description",
    },
)
class ComputeRegionUrlMapHostRule:
    def __init__(
        self,
        *,
        hosts: typing.Sequence[builtins.str],
        path_matcher: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: The list of host patterns to match. They must be valid hostnames, except * will match any string of ([a-z0-9-.]*). In that case, * must be the first character and must be followed in the pattern by either - or .. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#hosts ComputeRegionUrlMap#hosts}
        :param path_matcher: The name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_matcher ComputeRegionUrlMap#path_matcher}
        :param description: An optional description of this HostRule. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapHostRule.__init__)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument path_matcher", value=path_matcher, expected_type=type_hints["path_matcher"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "hosts": hosts,
            "path_matcher": path_matcher,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def hosts(self) -> typing.List[builtins.str]:
        '''The list of host patterns to match.

        They must be valid
        hostnames, except * will match any string of ([a-z0-9-.]*). In
        that case, * must be the first character and must be followed in
        the pattern by either - or ..

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#hosts ComputeRegionUrlMap#hosts}
        '''
        result = self._values.get("hosts")
        assert result is not None, "Required property 'hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path_matcher(self) -> builtins.str:
        '''The name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_matcher ComputeRegionUrlMap#path_matcher}
        '''
        result = self._values.get("path_matcher")
        assert result is not None, "Required property 'path_matcher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this HostRule. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapHostRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapHostRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapHostRuleList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapHostRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ComputeRegionUrlMapHostRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapHostRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapHostRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapHostRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapHostRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapHostRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapHostRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapHostRuleOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapHostRuleOutputReference.__init__)
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
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcherInput")
    def path_matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleOutputReference, "hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="pathMatcher")
    def path_matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathMatcher"))

    @path_matcher.setter
    def path_matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleOutputReference, "path_matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathMatcher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapHostRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapHostRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapHostRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapHostRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcher",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "default_service": "defaultService",
        "default_url_redirect": "defaultUrlRedirect",
        "description": "description",
        "path_rule": "pathRule",
        "route_rules": "routeRules",
    },
)
class ComputeRegionUrlMapPathMatcher:
    def __init__(
        self,
        *,
        name: builtins.str,
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        path_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRule", typing.Dict[str, typing.Any]]]]] = None,
        route_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRules", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: The name to which this PathMatcher is referred by the HostRule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        :param default_service: A reference to a RegionBackendService resource. This will be used if none of the pathRules defined by this PathMatcher is matched by the URL's path portion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_service ComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_url_redirect ComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        :param path_rule: path_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_rule ComputeRegionUrlMap#path_rule}
        :param route_rules: route_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_rules ComputeRegionUrlMap#route_rules}
        '''
        if isinstance(default_url_redirect, dict):
            default_url_redirect = ComputeRegionUrlMapPathMatcherDefaultUrlRedirect(**default_url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcher.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_service", value=default_service, expected_type=type_hints["default_service"])
            check_type(argname="argument default_url_redirect", value=default_url_redirect, expected_type=type_hints["default_url_redirect"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument path_rule", value=path_rule, expected_type=type_hints["path_rule"])
            check_type(argname="argument route_rules", value=route_rules, expected_type=type_hints["route_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if default_service is not None:
            self._values["default_service"] = default_service
        if default_url_redirect is not None:
            self._values["default_url_redirect"] = default_url_redirect
        if description is not None:
            self._values["description"] = description
        if path_rule is not None:
            self._values["path_rule"] = path_rule
        if route_rules is not None:
            self._values["route_rules"] = route_rules

    @builtins.property
    def name(self) -> builtins.str:
        '''The name to which this PathMatcher is referred by the HostRule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_service(self) -> typing.Optional[builtins.str]:
        '''A reference to a RegionBackendService resource.

        This will be used if
        none of the pathRules defined by this PathMatcher is matched by
        the URL's path portion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_service ComputeRegionUrlMap#default_service}
        '''
        result = self._values.get("default_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_url_redirect(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherDefaultUrlRedirect"]:
        '''default_url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#default_url_redirect ComputeRegionUrlMap#default_url_redirect}
        '''
        result = self._values.get("default_url_redirect")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherDefaultUrlRedirect"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRule"]]]:
        '''path_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_rule ComputeRegionUrlMap#path_rule}
        '''
        result = self._values.get("path_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRule"]]], result)

    @builtins.property
    def route_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRules"]]]:
        '''route_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_rules ComputeRegionUrlMap#route_rules}
        '''
        result = self._values.get("route_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcher(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherDefaultUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class ComputeRegionUrlMapPathMatcherDefaultUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherDefaultUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the original URL is
        retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to
        false, the URL scheme of the redirected request will remain the same as that of the
        request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this
        true for TargetHttpsProxy is not permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied together with
        prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the
        original request will be used for the redirect. The value must be between 1 and 1024
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or
        neither. If neither is supplied, the path of the original request will be used for
        the redirect. The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherDefaultUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherDefaultUrlRedirect]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherDefaultUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherDefaultUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcher]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcher]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcher]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDefaultUrlRedirect")
    def put_default_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        value = ComputeRegionUrlMapPathMatcherDefaultUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUrlRedirect", [value]))

    @jsii.member(jsii_name="putPathRule")
    def put_path_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherOutputReference.put_path_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPathRule", [value]))

    @jsii.member(jsii_name="putRouteRules")
    def put_route_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherOutputReference.put_route_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRouteRules", [value]))

    @jsii.member(jsii_name="resetDefaultService")
    def reset_default_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultService", []))

    @jsii.member(jsii_name="resetDefaultUrlRedirect")
    def reset_default_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultUrlRedirect", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPathRule")
    def reset_path_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRule", []))

    @jsii.member(jsii_name="resetRouteRules")
    def reset_route_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteRules", []))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirect")
    def default_url_redirect(
        self,
    ) -> ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, jsii.get(self, "defaultUrlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="pathRule")
    def path_rule(self) -> "ComputeRegionUrlMapPathMatcherPathRuleList":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleList", jsii.get(self, "pathRule"))

    @builtins.property
    @jsii.member(jsii_name="routeRules")
    def route_rules(self) -> "ComputeRegionUrlMapPathMatcherRouteRulesList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesList", jsii.get(self, "routeRules"))

    @builtins.property
    @jsii.member(jsii_name="defaultServiceInput")
    def default_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirectInput")
    def default_url_redirect_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherDefaultUrlRedirect]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherDefaultUrlRedirect], jsii.get(self, "defaultUrlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRuleInput")
    def path_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRule"]]], jsii.get(self, "pathRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="routeRulesInput")
    def route_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRules"]]], jsii.get(self, "routeRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultService")
    def default_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultService"))

    @default_service.setter
    def default_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherOutputReference, "default_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultService", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcher, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcher, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcher, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRule",
    jsii_struct_bases=[],
    name_mapping={
        "paths": "paths",
        "route_action": "routeAction",
        "service": "service",
        "url_redirect": "urlRedirect",
    },
)
class ComputeRegionUrlMapPathMatcherPathRule:
    def __init__(
        self,
        *,
        paths: typing.Sequence[builtins.str],
        route_action: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteAction", typing.Dict[str, typing.Any]]] = None,
        service: typing.Optional[builtins.str] = None,
        url_redirect: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param paths: The list of path patterns to match. Each must start with / and the only place a * is allowed is at the end following a /. The string fed to the path matcher does not include any text after the first ? or #, and those chars are not allowed here. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#paths ComputeRegionUrlMap#paths}
        :param route_action: route_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_action ComputeRegionUrlMap#route_action}
        :param service: The region backend service resource to which traffic is directed if this rule is matched. If routeAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if service is specified, routeAction cannot contain any weightedBackendService s. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of urlRedirect, service or routeAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        :param url_redirect: url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_redirect ComputeRegionUrlMap#url_redirect}
        '''
        if isinstance(route_action, dict):
            route_action = ComputeRegionUrlMapPathMatcherPathRuleRouteAction(**route_action)
        if isinstance(url_redirect, dict):
            url_redirect = ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(**url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRule.__init__)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument route_action", value=route_action, expected_type=type_hints["route_action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url_redirect", value=url_redirect, expected_type=type_hints["url_redirect"])
        self._values: typing.Dict[str, typing.Any] = {
            "paths": paths,
        }
        if route_action is not None:
            self._values["route_action"] = route_action
        if service is not None:
            self._values["service"] = service
        if url_redirect is not None:
            self._values["url_redirect"] = url_redirect

    @builtins.property
    def paths(self) -> typing.List[builtins.str]:
        '''The list of path patterns to match.

        Each must start with / and the only place a

        - is allowed is at the end following a /. The string fed to the path matcher
          does not include any text after the first ? or #, and those chars are not
          allowed here.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#paths ComputeRegionUrlMap#paths}
        '''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def route_action(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteAction"]:
        '''route_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_action ComputeRegionUrlMap#route_action}
        '''
        result = self._values.get("route_action")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteAction"], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The region backend service resource to which traffic is directed if this rule is matched.

        If routeAction is additionally specified,
        advanced routing actions like URL Rewrites, etc. take effect prior to sending
        the request to the backend. However, if service is specified, routeAction cannot
        contain any weightedBackendService s. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified. Only one of urlRedirect,
        service or routeAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_redirect(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"]:
        '''url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_redirect ComputeRegionUrlMap#url_redirect}
        '''
        result = self._values.get("url_redirect")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRouteAction")
    def put_route_action(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteAction(
            cors_policy=cors_policy,
            fault_injection_policy=fault_injection_policy,
            request_mirror_policy=request_mirror_policy,
            retry_policy=retry_policy,
            timeout=timeout,
            url_rewrite=url_rewrite,
            weighted_backend_services=weighted_backend_services,
        )

        return typing.cast(None, jsii.invoke(self, "putRouteAction", [value]))

    @jsii.member(jsii_name="putUrlRedirect")
    def put_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirect", [value]))

    @jsii.member(jsii_name="resetRouteAction")
    def reset_route_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteAction", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrlRedirect")
    def reset_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirect", []))

    @builtins.property
    @jsii.member(jsii_name="routeAction")
    def route_action(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference", jsii.get(self, "routeAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirect")
    def url_redirect(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference", jsii.get(self, "urlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="routeActionInput")
    def route_action_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteAction"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteAction"], jsii.get(self, "routeActionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectInput")
    def url_redirect_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"], jsii.get(self, "urlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleOutputReference, "paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteAction",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "fault_injection_policy": "faultInjectionPolicy",
        "request_mirror_policy": "requestMirrorPolicy",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
        "url_rewrite": "urlRewrite",
        "weighted_backend_services": "weightedBackendServices",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteAction:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        if isinstance(cors_policy, dict):
            cors_policy = ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(**cors_policy)
        if isinstance(fault_injection_policy, dict):
            fault_injection_policy = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(**fault_injection_policy)
        if isinstance(request_mirror_policy, dict):
            request_mirror_policy = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(**request_mirror_policy)
        if isinstance(retry_policy, dict):
            retry_policy = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(**timeout)
        if isinstance(url_rewrite, dict):
            url_rewrite = ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(**url_rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteAction.__init__)
            check_type(argname="argument cors_policy", value=cors_policy, expected_type=type_hints["cors_policy"])
            check_type(argname="argument fault_injection_policy", value=fault_injection_policy, expected_type=type_hints["fault_injection_policy"])
            check_type(argname="argument request_mirror_policy", value=request_mirror_policy, expected_type=type_hints["request_mirror_policy"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url_rewrite", value=url_rewrite, expected_type=type_hints["url_rewrite"])
            check_type(argname="argument weighted_backend_services", value=weighted_backend_services, expected_type=type_hints["weighted_backend_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if fault_injection_policy is not None:
            self._values["fault_injection_policy"] = fault_injection_policy
        if request_mirror_policy is not None:
            self._values["request_mirror_policy"] = request_mirror_policy
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if url_rewrite is not None:
            self._values["url_rewrite"] = url_rewrite
        if weighted_backend_services is not None:
            self._values["weighted_backend_services"] = weighted_backend_services

    @builtins.property
    def cors_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy"]:
        '''cors_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy"], result)

    @builtins.property
    def fault_injection_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy"]:
        '''fault_injection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        '''
        result = self._values.get("fault_injection_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy"], result)

    @builtins.property
    def request_mirror_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"]:
        '''request_mirror_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        '''
        result = self._values.get("request_mirror_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"], result)

    @builtins.property
    def url_rewrite(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"]:
        '''url_rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        '''
        result = self._values.get("url_rewrite")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"], result)

    @builtins.property
    def weighted_backend_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]]:
        '''weighted_backend_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        result = self._values.get("weighted_backend_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disabled": "disabled",
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin_regexes": "allowOriginRegexes",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disabled: If true, specifies the CORS policy is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origin_regexes", value=allow_origin_regexes, expected_type=type_hints["allow_origin_regexes"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin_regexes is not None:
            self._values["allow_origin_regexes"] = allow_origin_regexes
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If true, specifies the CORS policy is disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        '''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''In response to a preflight request, setting this to true indicates that the actual request can include user credentials.

        This translates to the Access-
        Control-Allow-Credentials header. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origin_regexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the regular expression patterns that match allowed origins.

        For
        regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript
        An origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        '''
        result = self._values.get("allow_origin_regexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of origins that will be allowed to do CORS requests.

        An
        origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long the results of a preflight request can be cached.

        This
        translates to the content for the Access-Control-Max-Age header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOriginRegexes")
    def reset_allow_origin_regexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOriginRegexes", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexesInput")
    def allow_origin_regexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginRegexesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexes")
    def allow_origin_regexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOriginRegexes"))

    @allow_origin_regexes.setter
    def allow_origin_regexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_origin_regexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOriginRegexes", value)

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOrigins"))

    @allow_origins.setter
    def allow_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy:
    def __init__(
        self,
        *,
        abort: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort", typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        if isinstance(abort, dict):
            abort = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(**abort)
        if isinstance(delay, dict):
            delay = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(**delay)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy.__init__)
            check_type(argname="argument abort", value=abort, expected_type=type_hints["abort"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort"]:
        '''abort block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        '''
        result = self._values.get("abort")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort"], result)

    @builtins.property
    def delay(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay"]:
        '''delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort",
    jsii_struct_bases=[],
    name_mapping={"http_status": "httpStatus", "percentage": "percentage"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort:
    def __init__(self, *, http_status: jsii.Number, percentage: jsii.Number) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort.__init__)
            check_type(argname="argument http_status", value=http_status, expected_type=type_hints["http_status"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_status": http_status,
            "percentage": percentage,
        }

    @builtins.property
    def http_status(self) -> jsii.Number:
        '''The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        '''
        result = self._values.get("http_status")
        assert result is not None, "Required property 'http_status' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection.

        The value must be between 0.0 and 100.0
        inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="httpStatusInput")
    def http_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="httpStatus")
    def http_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpStatus"))

    @http_status.setter
    def http_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "http_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpStatus", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay",
    jsii_struct_bases=[],
    name_mapping={"fixed_delay": "fixedDelay", "percentage": "percentage"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay:
    def __init__(
        self,
        *,
        fixed_delay: typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay", typing.Dict[str, typing.Any]],
        percentage: jsii.Number,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        if isinstance(fixed_delay, dict):
            fixed_delay = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(**fixed_delay)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay.__init__)
            check_type(argname="argument fixed_delay", value=fixed_delay, expected_type=type_hints["fixed_delay"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "fixed_delay": fixed_delay,
            "percentage": percentage,
        }

    @builtins.property
    def fixed_delay(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay":
        '''fixed_delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        '''
        result = self._values.get("fixed_delay")
        assert result is not None, "Required property 'fixed_delay' is missing"
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay", result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection.

        The value must be between 0.0 and
        100.0 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFixedDelay")
    def put_fixed_delay(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putFixedDelay", [value]))

    @builtins.property
    @jsii.member(jsii_name="fixedDelay")
    def fixed_delay(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, jsii.get(self, "fixedDelay"))

    @builtins.property
    @jsii.member(jsii_name="fixedDelayInput")
    def fixed_delay_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "fixedDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAbort")
    def put_abort(self, *, http_status: jsii.Number, percentage: jsii.Number) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(
            http_status=http_status, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAbort", [value]))

    @jsii.member(jsii_name="putDelay")
    def put_delay(
        self,
        *,
        fixed_delay: typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay, typing.Dict[str, typing.Any]],
        percentage: jsii.Number,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(
            fixed_delay=fixed_delay, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDelay", [value]))

    @jsii.member(jsii_name="resetAbort")
    def reset_abort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbort", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @builtins.property
    @jsii.member(jsii_name="abort")
    def abort(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, jsii.get(self, "abort"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, jsii.get(self, "delay"))

    @builtins.property
    @jsii.member(jsii_name="abortInput")
    def abort_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort], jsii.get(self, "abortInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsPolicy")
    def put_cors_policy(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disabled: If true, specifies the CORS policy is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(
            disabled=disabled,
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origin_regexes=allow_origin_regexes,
            allow_origins=allow_origins,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsPolicy", [value]))

    @jsii.member(jsii_name="putFaultInjectionPolicy")
    def put_fault_injection_policy(
        self,
        *,
        abort: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort, typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(
            abort=abort, delay=delay
        )

        return typing.cast(None, jsii.invoke(self, "putFaultInjectionPolicy", [value]))

    @jsii.member(jsii_name="putRequestMirrorPolicy")
    def put_request_mirror_policy(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(
            backend_service=backend_service
        )

        return typing.cast(None, jsii.invoke(self, "putRequestMirrorPolicy", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        num_retries: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. - 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. - connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. - refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. - cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled - deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted - unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(
            num_retries=num_retries,
            per_try_timeout=per_try_timeout,
            retry_conditions=retry_conditions,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putUrlRewrite")
    def put_url_rewrite(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(
            host_rewrite=host_rewrite, path_prefix_rewrite=path_prefix_rewrite
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewrite", [value]))

    @jsii.member(jsii_name="putWeightedBackendServices")
    def put_weighted_backend_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference.put_weighted_backend_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedBackendServices", [value]))

    @jsii.member(jsii_name="resetCorsPolicy")
    def reset_cors_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsPolicy", []))

    @jsii.member(jsii_name="resetFaultInjectionPolicy")
    def reset_fault_injection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaultInjectionPolicy", []))

    @jsii.member(jsii_name="resetRequestMirrorPolicy")
    def reset_request_mirror_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMirrorPolicy", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrlRewrite")
    def reset_url_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewrite", []))

    @jsii.member(jsii_name="resetWeightedBackendServices")
    def reset_weighted_backend_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedBackendServices", []))

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, jsii.get(self, "corsPolicy"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference, jsii.get(self, "faultInjectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference", jsii.get(self, "requestMirrorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="urlRewrite")
    def url_rewrite(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference", jsii.get(self, "urlRewrite"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServices")
    def weighted_backend_services(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList", jsii.get(self, "weightedBackendServices"))

    @builtins.property
    @jsii.member(jsii_name="corsPolicyInput")
    def cors_policy_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy], jsii.get(self, "corsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicyInput")
    def fault_injection_policy_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy], jsii.get(self, "faultInjectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicyInput")
    def request_mirror_policy_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"], jsii.get(self, "requestMirrorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteInput")
    def url_rewrite_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"], jsii.get(self, "urlRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServicesInput")
    def weighted_backend_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]], jsii.get(self, "weightedBackendServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy",
    jsii_struct_bases=[],
    name_mapping={"backend_service": "backendService"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy:
    def __init__(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
        }

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The RegionBackendService resource being mirrored to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "num_retries": "numRetries",
        "per_try_timeout": "perTryTimeout",
        "retry_conditions": "retryConditions",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy:
    def __init__(
        self,
        *,
        num_retries: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. - 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. - connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. - refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. - cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled - deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted - unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        if isinstance(per_try_timeout, dict):
            per_try_timeout = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(**per_try_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy.__init__)
            check_type(argname="argument num_retries", value=num_retries, expected_type=type_hints["num_retries"])
            check_type(argname="argument per_try_timeout", value=per_try_timeout, expected_type=type_hints["per_try_timeout"])
            check_type(argname="argument retry_conditions", value=retry_conditions, expected_type=type_hints["retry_conditions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if num_retries is not None:
            self._values["num_retries"] = num_retries
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_conditions is not None:
            self._values["retry_conditions"] = retry_conditions

    @builtins.property
    def num_retries(self) -> typing.Optional[jsii.Number]:
        '''Specifies the allowed number retries. This number must be > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        '''
        result = self._values.get("num_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def per_try_timeout(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"]:
        '''per_try_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        '''
        result = self._values.get("per_try_timeout")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"], result)

    @builtins.property
    def retry_conditions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more conditions when this retry rule applies. Valid values are:.

        - 5xx: Loadbalancer will attempt a retry if the backend service responds with
          any 5xx response code, or if the backend service does not respond at all,
          example: disconnects, reset, read timeout, connection failure, and refused
          streams.
        - gateway-error: Similar to 5xx, but only applies to response codes
          502, 503 or 504.
        - connect-failure: Loadbalancer will retry on failures
          connecting to backend services, for example due to connection timeouts.
        - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes.
          Currently the only retriable error supported is 409.
        - refused-stream: Loadbalancer will retry if the backend service resets the stream with a
          REFUSED_STREAM error code. This reset type indicates that it is safe to retry.
        - cancelled: Loadbalancer will retry if the gRPC status code in the response
          header is set to cancelled
        - deadline-exceeded: Loadbalancer will retry if the
          gRPC status code in the response header is set to deadline-exceeded
        - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response
          header is set to resource-exhausted
        - unavailable: Loadbalancer will retry if
          the gRPC status code in the response header is set to unavailable

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        result = self._values.get("retry_conditions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerTryTimeout")
    def put_per_try_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putPerTryTimeout", [value]))

    @jsii.member(jsii_name="resetNumRetries")
    def reset_num_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumRetries", []))

    @jsii.member(jsii_name="resetPerTryTimeout")
    def reset_per_try_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerTryTimeout", []))

    @jsii.member(jsii_name="resetRetryConditions")
    def reset_retry_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConditions", []))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeout")
    def per_try_timeout(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference", jsii.get(self, "perTryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="numRetriesInput")
    def num_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeoutInput")
    def per_try_timeout_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"], jsii.get(self, "perTryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConditionsInput")
    def retry_conditions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "retryConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="numRetries")
    def num_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRetries"))

    @num_retries.setter
    def num_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "num_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numRetries", value)

    @builtins.property
    @jsii.member(jsii_name="retryConditions")
    def retry_conditions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryConditions"))

    @retry_conditions.setter
    def retry_conditions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "retry_conditions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryConditions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite",
    jsii_struct_bases=[],
    name_mapping={
        "host_rewrite": "hostRewrite",
        "path_prefix_rewrite": "pathPrefixRewrite",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite:
    def __init__(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite.__init__)
            check_type(argname="argument host_rewrite", value=host_rewrite, expected_type=type_hints["host_rewrite"])
            check_type(argname="argument path_prefix_rewrite", value=path_prefix_rewrite, expected_type=type_hints["path_prefix_rewrite"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_rewrite is not None:
            self._values["host_rewrite"] = host_rewrite
        if path_prefix_rewrite is not None:
            self._values["path_prefix_rewrite"] = path_prefix_rewrite

    @builtins.property
    def host_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite.

        The value must be between 1 and
        255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        '''
        result = self._values.get("host_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_prefix_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite.

        The value must
        be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        result = self._values.get("path_prefix_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRewrite")
    def reset_host_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRewrite", []))

    @jsii.member(jsii_name="resetPathPrefixRewrite")
    def reset_path_prefix_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="hostRewriteInput")
    def host_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewriteInput")
    def path_prefix_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRewrite")
    def host_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRewrite"))

    @host_rewrite.setter
    def host_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "host_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefixRewrite"))

    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "path_prefix_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices",
    jsii_struct_bases=[],
    name_mapping={
        "backend_service": "backendService",
        "weight": "weight",
        "header_action": "headerAction",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices:
    def __init__(
        self,
        *,
        backend_service: builtins.str,
        weight: jsii.Number,
        header_action: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend_service: The default RegionBackendService resource. Before forwarding the request to backendService, the loadbalancer applies any relevant headerActions specified as part of this backendServiceWeight. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        :param weight: Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) . The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backendService, subsequent requests will be sent to the same backendService as determined by the BackendService's session affinity policy. The value must be between 0 and 1000 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weight ComputeRegionUrlMap#weight}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        '''
        if isinstance(header_action, dict):
            header_action = ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(**header_action)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
            "weight": weight,
        }
        if header_action is not None:
            self._values["header_action"] = header_action

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The default RegionBackendService resource.

        Before
        forwarding the request to backendService, the loadbalancer applies any relevant
        headerActions specified as part of this backendServiceWeight.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) .

        The selection of a
        backend service is determined only for new traffic. Once a user's request has
        been directed to a backendService, subsequent requests will be sent to the same
        backendService as determined by the BackendService's session affinity policy.
        The value must be between 0 and 1000

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weight ComputeRegionUrlMap#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the
        original URL is retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to false, the URL scheme of the redirected request will remain the
        same as that of the request. This must only be set for UrlMaps used in
        TargetHttpProxys. Setting this true for TargetHttpsProxy is not
        permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied
        together with prefixRedirect. Supply one alone or neither. If neither is
        supplied, the path of the original request will be used for the redirect.
        The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with
        pathRedirect. Supply one alone or neither. If neither is supplied, the
        path of the original request will be used for the redirect. The value
        must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRules",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "header_action": "headerAction",
        "match_rules": "matchRules",
        "route_action": "routeAction",
        "service": "service",
        "url_redirect": "urlRedirect",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRules:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        header_action: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction", typing.Dict[str, typing.Any]]] = None,
        match_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRules", typing.Dict[str, typing.Any]]]]] = None,
        route_action: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteAction", typing.Dict[str, typing.Any]]] = None,
        service: typing.Optional[builtins.str] = None,
        url_redirect: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param priority: For routeRules within a given pathMatcher, priority determines the order in which load balancer will interpret routeRules. RouteRules are evaluated in order of priority, from the lowest to highest number. The priority of a rule decreases as its number increases (1, 2, 3, N+1). The first rule that matches the request is applied. You cannot configure two or more routeRules with the same priority. Priority for each rule must be set to a number between 0 and 2147483647 inclusive. Priority numbers can have gaps, which enable you to add or remove rules in the future without affecting the rest of the rules. For example, 1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the future without any impact on existing rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#priority ComputeRegionUrlMap#priority}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#match_rules ComputeRegionUrlMap#match_rules}
        :param route_action: route_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_action ComputeRegionUrlMap#route_action}
        :param service: The region backend service resource to which traffic is directed if this rule is matched. If routeAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if service is specified, routeAction cannot contain any weightedBackendService s. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of urlRedirect, service or routeAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        :param url_redirect: url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_redirect ComputeRegionUrlMap#url_redirect}
        '''
        if isinstance(header_action, dict):
            header_action = ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(**header_action)
        if isinstance(route_action, dict):
            route_action = ComputeRegionUrlMapPathMatcherRouteRulesRouteAction(**route_action)
        if isinstance(url_redirect, dict):
            url_redirect = ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(**url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRules.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
            check_type(argname="argument match_rules", value=match_rules, expected_type=type_hints["match_rules"])
            check_type(argname="argument route_action", value=route_action, expected_type=type_hints["route_action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url_redirect", value=url_redirect, expected_type=type_hints["url_redirect"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
        }
        if header_action is not None:
            self._values["header_action"] = header_action
        if match_rules is not None:
            self._values["match_rules"] = match_rules
        if route_action is not None:
            self._values["route_action"] = route_action
        if service is not None:
            self._values["service"] = service
        if url_redirect is not None:
            self._values["url_redirect"] = url_redirect

    @builtins.property
    def priority(self) -> jsii.Number:
        '''For routeRules within a given pathMatcher, priority determines the order in which load balancer will interpret routeRules.

        RouteRules are evaluated
        in order of priority, from the lowest to highest number. The priority of
        a rule decreases as its number increases (1, 2, 3, N+1). The first rule
        that matches the request is applied.

        You cannot configure two or more routeRules with the same priority.
        Priority for each rule must be set to a number between 0 and
        2147483647 inclusive.

        Priority numbers can have gaps, which enable you to add or remove rules
        in the future without affecting the rest of the rules. For example,
        1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which
        you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the
        future without any impact on existing rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#priority ComputeRegionUrlMap#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction"], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#match_rules ComputeRegionUrlMap#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRules"]]], result)

    @builtins.property
    def route_action(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteAction"]:
        '''route_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#route_action ComputeRegionUrlMap#route_action}
        '''
        result = self._values.get("route_action")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteAction"], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The region backend service resource to which traffic is directed if this rule is matched.

        If routeAction is additionally specified,
        advanced routing actions like URL Rewrites, etc. take effect prior to sending
        the request to the backend. However, if service is specified, routeAction cannot
        contain any weightedBackendService s. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified. Only one of urlRedirect,
        service or routeAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_redirect(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"]:
        '''url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_redirect ComputeRegionUrlMap#url_redirect}
        '''
        result = self._values.get("url_redirect")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "full_path_match": "fullPathMatch",
        "header_matches": "headerMatches",
        "ignore_case": "ignoreCase",
        "metadata_filters": "metadataFilters",
        "prefix_match": "prefixMatch",
        "query_parameter_matches": "queryParameterMatches",
        "regex_match": "regexMatch",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRules:
    def __init__(
        self,
        *,
        full_path_match: typing.Optional[builtins.str] = None,
        header_matches: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches", typing.Dict[str, typing.Any]]]]] = None,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata_filters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters", typing.Dict[str, typing.Any]]]]] = None,
        prefix_match: typing.Optional[builtins.str] = None,
        query_parameter_matches: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches", typing.Dict[str, typing.Any]]]]] = None,
        regex_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param full_path_match: For satisfying the matchRule condition, the path of the request must exactly match the value specified in fullPathMatch after removing any query parameters and anchor that may be part of the original URL. FullPathMatch must be between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#full_path_match ComputeRegionUrlMap#full_path_match}
        :param header_matches: header_matches block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_matches ComputeRegionUrlMap#header_matches}
        :param ignore_case: Specifies that prefixMatch and fullPathMatch matches are case sensitive. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#ignore_case ComputeRegionUrlMap#ignore_case}
        :param metadata_filters: metadata_filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#metadata_filters ComputeRegionUrlMap#metadata_filters}
        :param prefix_match: For satisfying the matchRule condition, the request's path must begin with the specified prefixMatch. prefixMatch must begin with a /. The value must be between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_match ComputeRegionUrlMap#prefix_match}
        :param query_parameter_matches: query_parameter_matches block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#query_parameter_matches ComputeRegionUrlMap#query_parameter_matches}
        :param regex_match: For satisfying the matchRule condition, the path of the request must satisfy the regular expression specified in regexMatch after removing any query parameters and anchor supplied with the original URL. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRules.__init__)
            check_type(argname="argument full_path_match", value=full_path_match, expected_type=type_hints["full_path_match"])
            check_type(argname="argument header_matches", value=header_matches, expected_type=type_hints["header_matches"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument metadata_filters", value=metadata_filters, expected_type=type_hints["metadata_filters"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
            check_type(argname="argument query_parameter_matches", value=query_parameter_matches, expected_type=type_hints["query_parameter_matches"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
        self._values: typing.Dict[str, typing.Any] = {}
        if full_path_match is not None:
            self._values["full_path_match"] = full_path_match
        if header_matches is not None:
            self._values["header_matches"] = header_matches
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if metadata_filters is not None:
            self._values["metadata_filters"] = metadata_filters
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match
        if query_parameter_matches is not None:
            self._values["query_parameter_matches"] = query_parameter_matches
        if regex_match is not None:
            self._values["regex_match"] = regex_match

    @builtins.property
    def full_path_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the path of the request must exactly match the value specified in fullPathMatch after removing any query parameters and anchor that may be part of the original URL.

        FullPathMatch must be between 1
        and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must
        be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#full_path_match ComputeRegionUrlMap#full_path_match}
        '''
        result = self._values.get("full_path_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header_matches(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches"]]]:
        '''header_matches block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_matches ComputeRegionUrlMap#header_matches}
        '''
        result = self._values.get("header_matches")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches"]]], result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies that prefixMatch and fullPathMatch matches are case sensitive. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#ignore_case ComputeRegionUrlMap#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metadata_filters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters"]]]:
        '''metadata_filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#metadata_filters ComputeRegionUrlMap#metadata_filters}
        '''
        result = self._values.get("metadata_filters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters"]]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the request's path must begin with the specified prefixMatch.

        prefixMatch must begin with a /. The value must be
        between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or
        regexMatch must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_match ComputeRegionUrlMap#prefix_match}
        '''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_parameter_matches(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]]:
        '''query_parameter_matches block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#query_parameter_matches ComputeRegionUrlMap#query_parameter_matches}
        '''
        result = self._values.get("query_parameter_matches")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the path of the request must satisfy the regular expression specified in regexMatch after removing any query parameters and anchor supplied with the original URL.

        For regular expression grammar please
        see en.cppreference.com/w/cpp/regex/ecmascript  Only one of prefixMatch,
        fullPathMatch or regexMatch must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "exact_match": "exactMatch",
        "invert_match": "invertMatch",
        "prefix_match": "prefixMatch",
        "present_match": "presentMatch",
        "range_match": "rangeMatch",
        "regex_match": "regexMatch",
        "suffix_match": "suffixMatch",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        exact_match: typing.Optional[builtins.str] = None,
        invert_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prefix_match: typing.Optional[builtins.str] = None,
        present_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        range_match: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch", typing.Dict[str, typing.Any]]] = None,
        regex_match: typing.Optional[builtins.str] = None,
        suffix_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_name: The name of the HTTP header to match. For matching against the HTTP request's authority, use a headerMatch with the header name ":authority". For matching a request's method, use the headerName ":method". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param exact_match: The value should exactly match contents of exactMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#exact_match ComputeRegionUrlMap#exact_match}
        :param invert_match: If set to false, the headerMatch is considered a match if the match criteria above are met. If set to true, the headerMatch is considered a match if the match criteria above are NOT met. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#invert_match ComputeRegionUrlMap#invert_match}
        :param prefix_match: The value of the header must start with the contents of prefixMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_match ComputeRegionUrlMap#prefix_match}
        :param present_match: A header with the contents of headerName must exist. The match takes place whether or not the request's header has a value or not. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#present_match ComputeRegionUrlMap#present_match}
        :param range_match: range_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_match ComputeRegionUrlMap#range_match}
        :param regex_match: The value of the header must match the regular expression specified in regexMatch. For regular expression grammar, please see: en.cppreference.com/w/cpp/regex/ecmascript For matching against a port specified in the HTTP request, use a headerMatch with headerName set to PORT and a regular expression that satisfies the RFC2616 Host header's port specifier. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        :param suffix_match: The value of the header must end with the contents of suffixMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#suffix_match ComputeRegionUrlMap#suffix_match}
        '''
        if isinstance(range_match, dict):
            range_match = ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(**range_match)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument exact_match", value=exact_match, expected_type=type_hints["exact_match"])
            check_type(argname="argument invert_match", value=invert_match, expected_type=type_hints["invert_match"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
            check_type(argname="argument present_match", value=present_match, expected_type=type_hints["present_match"])
            check_type(argname="argument range_match", value=range_match, expected_type=type_hints["range_match"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
            check_type(argname="argument suffix_match", value=suffix_match, expected_type=type_hints["suffix_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
        }
        if exact_match is not None:
            self._values["exact_match"] = exact_match
        if invert_match is not None:
            self._values["invert_match"] = invert_match
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match
        if present_match is not None:
            self._values["present_match"] = present_match
        if range_match is not None:
            self._values["range_match"] = range_match
        if regex_match is not None:
            self._values["regex_match"] = regex_match
        if suffix_match is not None:
            self._values["suffix_match"] = suffix_match

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the HTTP header to match.

        For matching against the HTTP request's
        authority, use a headerMatch with the header name ":authority". For matching a
        request's method, use the headerName ":method".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exact_match(self) -> typing.Optional[builtins.str]:
        '''The value should exactly match contents of exactMatch.

        Only one of exactMatch,
        prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#exact_match ComputeRegionUrlMap#exact_match}
        '''
        result = self._values.get("exact_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to false, the headerMatch is considered a match if the match criteria above are met.

        If set to true, the headerMatch is considered a match if the
        match criteria above are NOT met. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#invert_match ComputeRegionUrlMap#invert_match}
        '''
        result = self._values.get("invert_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must start with the contents of prefixMatch.

        Only one of
        exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_match ComputeRegionUrlMap#prefix_match}
        '''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def present_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A header with the contents of headerName must exist.

        The match takes place
        whether or not the request's header has a value or not. Only one of exactMatch,
        prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#present_match ComputeRegionUrlMap#present_match}
        '''
        result = self._values.get("present_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def range_match(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"]:
        '''range_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_match ComputeRegionUrlMap#range_match}
        '''
        result = self._values.get("range_match")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must match the regular expression specified in regexMatch.

        For regular expression grammar, please see:
        en.cppreference.com/w/cpp/regex/ecmascript  For matching against a port
        specified in the HTTP request, use a headerMatch with headerName set to PORT and
        a regular expression that satisfies the RFC2616 Host header's port specifier.
        Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or
        rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must end with the contents of suffixMatch.

        Only one of
        exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#suffix_match ComputeRegionUrlMap#suffix_match}
        '''
        result = self._values.get("suffix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRangeMatch")
    def put_range_match(
        self,
        *,
        range_end: jsii.Number,
        range_start: jsii.Number,
    ) -> None:
        '''
        :param range_end: The end of the range (exclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_end ComputeRegionUrlMap#range_end}
        :param range_start: The start of the range (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_start ComputeRegionUrlMap#range_start}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(
            range_end=range_end, range_start=range_start
        )

        return typing.cast(None, jsii.invoke(self, "putRangeMatch", [value]))

    @jsii.member(jsii_name="resetExactMatch")
    def reset_exact_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExactMatch", []))

    @jsii.member(jsii_name="resetInvertMatch")
    def reset_invert_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertMatch", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @jsii.member(jsii_name="resetPresentMatch")
    def reset_present_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentMatch", []))

    @jsii.member(jsii_name="resetRangeMatch")
    def reset_range_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeMatch", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @jsii.member(jsii_name="resetSuffixMatch")
    def reset_suffix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffixMatch", []))

    @builtins.property
    @jsii.member(jsii_name="rangeMatch")
    def range_match(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference", jsii.get(self, "rangeMatch"))

    @builtins.property
    @jsii.member(jsii_name="exactMatchInput")
    def exact_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="invertMatchInput")
    def invert_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixMatchInput")
    def prefix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="presentMatchInput")
    def present_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "presentMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeMatchInput")
    def range_match_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"], jsii.get(self, "rangeMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixMatchInput")
    def suffix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="exactMatch")
    def exact_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exactMatch"))

    @exact_match.setter
    def exact_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "exact_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exactMatch", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="invertMatch")
    def invert_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertMatch"))

    @invert_match.setter
    def invert_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "invert_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertMatch", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="presentMatch")
    def present_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "presentMatch"))

    @present_match.setter
    def present_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "present_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presentMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="suffixMatch")
    def suffix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffixMatch"))

    @suffix_match.setter
    def suffix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "suffix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch",
    jsii_struct_bases=[],
    name_mapping={"range_end": "rangeEnd", "range_start": "rangeStart"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch:
    def __init__(self, *, range_end: jsii.Number, range_start: jsii.Number) -> None:
        '''
        :param range_end: The end of the range (exclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_end ComputeRegionUrlMap#range_end}
        :param range_start: The start of the range (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_start ComputeRegionUrlMap#range_start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch.__init__)
            check_type(argname="argument range_end", value=range_end, expected_type=type_hints["range_end"])
            check_type(argname="argument range_start", value=range_start, expected_type=type_hints["range_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "range_end": range_end,
            "range_start": range_start,
        }

    @builtins.property
    def range_end(self) -> jsii.Number:
        '''The end of the range (exclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_end ComputeRegionUrlMap#range_end}
        '''
        result = self._values.get("range_end")
        assert result is not None, "Required property 'range_end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def range_start(self) -> jsii.Number:
        '''The start of the range (inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#range_start ComputeRegionUrlMap#range_start}
        '''
        result = self._values.get("range_start")
        assert result is not None, "Required property 'range_start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="rangeEndInput")
    def range_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeStartInput")
    def range_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeEnd")
    def range_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeEnd"))

    @range_end.setter
    def range_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "range_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="rangeStart")
    def range_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeStart"))

    @range_start.setter
    def range_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "range_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeStart", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters",
    jsii_struct_bases=[],
    name_mapping={
        "filter_labels": "filterLabels",
        "filter_match_criteria": "filterMatchCriteria",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters:
    def __init__(
        self,
        *,
        filter_labels: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels", typing.Dict[str, typing.Any]]]],
        filter_match_criteria: builtins.str,
    ) -> None:
        '''
        :param filter_labels: filter_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#filter_labels ComputeRegionUrlMap#filter_labels}
        :param filter_match_criteria: Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match. Supported values are:. MATCH_ANY: At least one of the filterLabels must have a matching label in the provided metadata. MATCH_ALL: All filterLabels must have matching labels in the provided metadata. Possible values: ["MATCH_ALL", "MATCH_ANY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#filter_match_criteria ComputeRegionUrlMap#filter_match_criteria}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters.__init__)
            check_type(argname="argument filter_labels", value=filter_labels, expected_type=type_hints["filter_labels"])
            check_type(argname="argument filter_match_criteria", value=filter_match_criteria, expected_type=type_hints["filter_match_criteria"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter_labels": filter_labels,
            "filter_match_criteria": filter_match_criteria,
        }

    @builtins.property
    def filter_labels(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels"]]:
        '''filter_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#filter_labels ComputeRegionUrlMap#filter_labels}
        '''
        result = self._values.get("filter_labels")
        assert result is not None, "Required property 'filter_labels' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels"]], result)

    @builtins.property
    def filter_match_criteria(self) -> builtins.str:
        '''Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match. Supported values are:.

        MATCH_ANY: At least one of the filterLabels must have a matching label in the
        provided metadata.
        MATCH_ALL: All filterLabels must have matching labels in
        the provided metadata. Possible values: ["MATCH_ALL", "MATCH_ANY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#filter_match_criteria ComputeRegionUrlMap#filter_match_criteria}
        '''
        result = self._values.get("filter_match_criteria")
        assert result is not None, "Required property 'filter_match_criteria' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Name of metadata label. The name can have a maximum length of 1024 characters and must be at least 1 character long. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        :param value: The value of the label must match the specified value. value can have a maximum length of 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#value ComputeRegionUrlMap#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of metadata label.

        The name can have a maximum length of 1024 characters
        and must be at least 1 character long.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the label must match the specified value. value can have a maximum length of 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#value ComputeRegionUrlMap#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilterLabels")
    def put_filter_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference.put_filter_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilterLabels", [value]))

    @builtins.property
    @jsii.member(jsii_name="filterLabels")
    def filter_labels(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, jsii.get(self, "filterLabels"))

    @builtins.property
    @jsii.member(jsii_name="filterLabelsInput")
    def filter_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]], jsii.get(self, "filterLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteriaInput")
    def filter_match_criteria_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterMatchCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteria")
    def filter_match_criteria(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterMatchCriteria"))

    @filter_match_criteria.setter
    def filter_match_criteria(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference, "filter_match_criteria").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterMatchCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderMatches")
    def put_header_matches(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_header_matches)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaderMatches", [value]))

    @jsii.member(jsii_name="putMetadataFilters")
    def put_metadata_filters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_metadata_filters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadataFilters", [value]))

    @jsii.member(jsii_name="putQueryParameterMatches")
    def put_query_parameter_matches(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_query_parameter_matches)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParameterMatches", [value]))

    @jsii.member(jsii_name="resetFullPathMatch")
    def reset_full_path_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullPathMatch", []))

    @jsii.member(jsii_name="resetHeaderMatches")
    def reset_header_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderMatches", []))

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetMetadataFilters")
    def reset_metadata_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataFilters", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @jsii.member(jsii_name="resetQueryParameterMatches")
    def reset_query_parameter_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParameterMatches", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @builtins.property
    @jsii.member(jsii_name="headerMatches")
    def header_matches(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, jsii.get(self, "headerMatches"))

    @builtins.property
    @jsii.member(jsii_name="metadataFilters")
    def metadata_filters(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, jsii.get(self, "metadataFilters"))

    @builtins.property
    @jsii.member(jsii_name="queryParameterMatches")
    def query_parameter_matches(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList", jsii.get(self, "queryParameterMatches"))

    @builtins.property
    @jsii.member(jsii_name="fullPathMatchInput")
    def full_path_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullPathMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="headerMatchesInput")
    def header_matches_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]], jsii.get(self, "headerMatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataFiltersInput")
    def metadata_filters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]], jsii.get(self, "metadataFiltersInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixMatchInput")
    def prefix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParameterMatchesInput")
    def query_parameter_matches_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]], jsii.get(self, "queryParameterMatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="fullPathMatch")
    def full_path_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullPathMatch"))

    @full_path_match.setter
    def full_path_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "full_path_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullPathMatch", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "exact_match": "exactMatch",
        "present_match": "presentMatch",
        "regex_match": "regexMatch",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches:
    def __init__(
        self,
        *,
        name: builtins.str,
        exact_match: typing.Optional[builtins.str] = None,
        present_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        regex_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the query parameter to match. The query parameter must exist in the request, in the absence of which the request match fails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        :param exact_match: The queryParameterMatch matches if the value of the parameter exactly matches the contents of exactMatch. Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#exact_match ComputeRegionUrlMap#exact_match}
        :param present_match: Specifies that the queryParameterMatch matches if the request contains the query parameter, irrespective of whether the parameter has a value or not. Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#present_match ComputeRegionUrlMap#present_match}
        :param regex_match: The queryParameterMatch matches if the value of the parameter matches the regular expression specified by regexMatch. For the regular expression grammar, please see en.cppreference.com/w/cpp/regex/ecmascript Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument exact_match", value=exact_match, expected_type=type_hints["exact_match"])
            check_type(argname="argument present_match", value=present_match, expected_type=type_hints["present_match"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if exact_match is not None:
            self._values["exact_match"] = exact_match
        if present_match is not None:
            self._values["present_match"] = present_match
        if regex_match is not None:
            self._values["regex_match"] = regex_match

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the query parameter to match.

        The query parameter must exist in the
        request, in the absence of which the request match fails.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#name ComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exact_match(self) -> typing.Optional[builtins.str]:
        '''The queryParameterMatch matches if the value of the parameter exactly matches the contents of exactMatch.

        Only one of presentMatch, exactMatch and regexMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#exact_match ComputeRegionUrlMap#exact_match}
        '''
        result = self._values.get("exact_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def present_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies that the queryParameterMatch matches if the request contains the query parameter, irrespective of whether the parameter has a value or not.

        Only one of
        presentMatch, exactMatch and regexMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#present_match ComputeRegionUrlMap#present_match}
        '''
        result = self._values.get("present_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''The queryParameterMatch matches if the value of the parameter matches the regular expression specified by regexMatch.

        For the regular expression grammar,
        please see en.cppreference.com/w/cpp/regex/ecmascript  Only one of presentMatch,
        exactMatch and regexMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#regex_match ComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExactMatch")
    def reset_exact_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExactMatch", []))

    @jsii.member(jsii_name="resetPresentMatch")
    def reset_present_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentMatch", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @builtins.property
    @jsii.member(jsii_name="exactMatchInput")
    def exact_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="presentMatchInput")
    def present_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "presentMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="exactMatch")
    def exact_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exactMatch"))

    @exact_match.setter
    def exact_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "exact_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exactMatch", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="presentMatch")
    def present_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "presentMatch"))

    @present_match.setter
    def present_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "present_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presentMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesOutputReference.put_match_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchRules", [value]))

    @jsii.member(jsii_name="putRouteAction")
    def put_route_action(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteAction(
            cors_policy=cors_policy,
            fault_injection_policy=fault_injection_policy,
            request_mirror_policy=request_mirror_policy,
            retry_policy=retry_policy,
            timeout=timeout,
            url_rewrite=url_rewrite,
            weighted_backend_services=weighted_backend_services,
        )

        return typing.cast(None, jsii.invoke(self, "putRouteAction", [value]))

    @jsii.member(jsii_name="putUrlRedirect")
    def put_url_redirect(
        self,
        *,
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
        strip_query: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
            strip_query=strip_query,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirect", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @jsii.member(jsii_name="resetMatchRules")
    def reset_match_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchRules", []))

    @jsii.member(jsii_name="resetRouteAction")
    def reset_route_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteAction", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrlRedirect")
    def reset_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirect", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="routeAction")
    def route_action(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference", jsii.get(self, "routeAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirect")
    def url_redirect(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference", jsii.get(self, "urlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="routeActionInput")
    def route_action_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteAction"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteAction"], jsii.get(self, "routeActionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectInput")
    def url_redirect_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"], jsii.get(self, "urlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteAction",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "fault_injection_policy": "faultInjectionPolicy",
        "request_mirror_policy": "requestMirrorPolicy",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
        "url_rewrite": "urlRewrite",
        "weighted_backend_services": "weightedBackendServices",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteAction:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        if isinstance(cors_policy, dict):
            cors_policy = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(**cors_policy)
        if isinstance(fault_injection_policy, dict):
            fault_injection_policy = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(**fault_injection_policy)
        if isinstance(request_mirror_policy, dict):
            request_mirror_policy = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(**request_mirror_policy)
        if isinstance(retry_policy, dict):
            retry_policy = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(**timeout)
        if isinstance(url_rewrite, dict):
            url_rewrite = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(**url_rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteAction.__init__)
            check_type(argname="argument cors_policy", value=cors_policy, expected_type=type_hints["cors_policy"])
            check_type(argname="argument fault_injection_policy", value=fault_injection_policy, expected_type=type_hints["fault_injection_policy"])
            check_type(argname="argument request_mirror_policy", value=request_mirror_policy, expected_type=type_hints["request_mirror_policy"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url_rewrite", value=url_rewrite, expected_type=type_hints["url_rewrite"])
            check_type(argname="argument weighted_backend_services", value=weighted_backend_services, expected_type=type_hints["weighted_backend_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if fault_injection_policy is not None:
            self._values["fault_injection_policy"] = fault_injection_policy
        if request_mirror_policy is not None:
            self._values["request_mirror_policy"] = request_mirror_policy
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if url_rewrite is not None:
            self._values["url_rewrite"] = url_rewrite
        if weighted_backend_services is not None:
            self._values["weighted_backend_services"] = weighted_backend_services

    @builtins.property
    def cors_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy"]:
        '''cors_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#cors_policy ComputeRegionUrlMap#cors_policy}
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy"], result)

    @builtins.property
    def fault_injection_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy"]:
        '''fault_injection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fault_injection_policy ComputeRegionUrlMap#fault_injection_policy}
        '''
        result = self._values.get("fault_injection_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy"], result)

    @builtins.property
    def request_mirror_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"]:
        '''request_mirror_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_mirror_policy ComputeRegionUrlMap#request_mirror_policy}
        '''
        result = self._values.get("request_mirror_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_policy ComputeRegionUrlMap#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#timeout ComputeRegionUrlMap#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"], result)

    @builtins.property
    def url_rewrite(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"]:
        '''url_rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#url_rewrite ComputeRegionUrlMap#url_rewrite}
        '''
        result = self._values.get("url_rewrite")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"], result)

    @builtins.property
    def weighted_backend_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]]:
        '''weighted_backend_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weighted_backend_services ComputeRegionUrlMap#weighted_backend_services}
        '''
        result = self._values.get("weighted_backend_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin_regexes": "allowOriginRegexes",
        "allow_origins": "allowOrigins",
        "disabled": "disabled",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        :param disabled: If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy.__init__)
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origin_regexes", value=allow_origin_regexes, expected_type=type_hints["allow_origin_regexes"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin_regexes is not None:
            self._values["allow_origin_regexes"] = allow_origin_regexes
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if disabled is not None:
            self._values["disabled"] = disabled
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''In response to a preflight request, setting this to true indicates that the actual request can include user credentials.

        This translates to the Access-
        Control-Allow-Credentials header. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origin_regexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the regular expression patterns that match allowed origins.

        For
        regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript
        An origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        '''
        result = self._values.get("allow_origin_regexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of origins that will be allowed to do CORS requests.

        An
        origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long the results of a preflight request can be cached.

        This
        translates to the content for the Access-Control-Max-Age header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOriginRegexes")
    def reset_allow_origin_regexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOriginRegexes", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexesInput")
    def allow_origin_regexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginRegexesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexes")
    def allow_origin_regexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOriginRegexes"))

    @allow_origin_regexes.setter
    def allow_origin_regexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_origin_regexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOriginRegexes", value)

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOrigins"))

    @allow_origins.setter
    def allow_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy:
    def __init__(
        self,
        *,
        abort: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort", typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        if isinstance(abort, dict):
            abort = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(**abort)
        if isinstance(delay, dict):
            delay = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(**delay)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy.__init__)
            check_type(argname="argument abort", value=abort, expected_type=type_hints["abort"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort"]:
        '''abort block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        '''
        result = self._values.get("abort")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort"], result)

    @builtins.property
    def delay(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay"]:
        '''delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort",
    jsii_struct_bases=[],
    name_mapping={"http_status": "httpStatus", "percentage": "percentage"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort:
    def __init__(
        self,
        *,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort.__init__)
            check_type(argname="argument http_status", value=http_status, expected_type=type_hints["http_status"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_status is not None:
            self._values["http_status"] = http_status
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def http_status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        '''
        result = self._values.get("http_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection.

        The value must be between 0.0 and 100.0
        inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpStatus")
    def reset_http_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpStatus", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="httpStatusInput")
    def http_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="httpStatus")
    def http_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpStatus"))

    @http_status.setter
    def http_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "http_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpStatus", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay",
    jsii_struct_bases=[],
    name_mapping={"fixed_delay": "fixedDelay", "percentage": "percentage"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay:
    def __init__(
        self,
        *,
        fixed_delay: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay", typing.Dict[str, typing.Any]]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        if isinstance(fixed_delay, dict):
            fixed_delay = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(**fixed_delay)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay.__init__)
            check_type(argname="argument fixed_delay", value=fixed_delay, expected_type=type_hints["fixed_delay"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fixed_delay is not None:
            self._values["fixed_delay"] = fixed_delay
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def fixed_delay(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay"]:
        '''fixed_delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        '''
        result = self._values.get("fixed_delay")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay"], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection.

        The value must be between 0.0 and
        100.0 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFixedDelay")
    def put_fixed_delay(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putFixedDelay", [value]))

    @jsii.member(jsii_name="resetFixedDelay")
    def reset_fixed_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedDelay", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="fixedDelay")
    def fixed_delay(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, jsii.get(self, "fixedDelay"))

    @builtins.property
    @jsii.member(jsii_name="fixedDelayInput")
    def fixed_delay_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "fixedDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAbort")
    def put_abort(
        self,
        *,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#http_status ComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(
            http_status=http_status, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAbort", [value]))

    @jsii.member(jsii_name="putDelay")
    def put_delay(
        self,
        *,
        fixed_delay: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay, typing.Dict[str, typing.Any]]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#fixed_delay ComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#percentage ComputeRegionUrlMap#percentage}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(
            fixed_delay=fixed_delay, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDelay", [value]))

    @jsii.member(jsii_name="resetAbort")
    def reset_abort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbort", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @builtins.property
    @jsii.member(jsii_name="abort")
    def abort(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, jsii.get(self, "abort"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, jsii.get(self, "delay"))

    @builtins.property
    @jsii.member(jsii_name="abortInput")
    def abort_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort], jsii.get(self, "abortInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsPolicy")
    def put_cors_policy(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_credentials ComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_headers ComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_methods ComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origin_regexes ComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#allow_origins ComputeRegionUrlMap#allow_origins}
        :param disabled: If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#disabled ComputeRegionUrlMap#disabled}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#expose_headers ComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#max_age ComputeRegionUrlMap#max_age}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origin_regexes=allow_origin_regexes,
            allow_origins=allow_origins,
            disabled=disabled,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsPolicy", [value]))

    @jsii.member(jsii_name="putFaultInjectionPolicy")
    def put_fault_injection_policy(
        self,
        *,
        abort: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort, typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#abort ComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delay ComputeRegionUrlMap#delay}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(
            abort=abort, delay=delay
        )

        return typing.cast(None, jsii.invoke(self, "putFaultInjectionPolicy", [value]))

    @jsii.member(jsii_name="putRequestMirrorPolicy")
    def put_request_mirror_policy(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(
            backend_service=backend_service
        )

        return typing.cast(None, jsii.invoke(self, "putRequestMirrorPolicy", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        num_retries: jsii.Number,
        per_try_timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(
            num_retries=num_retries,
            per_try_timeout=per_try_timeout,
            retry_conditions=retry_conditions,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putUrlRewrite")
    def put_url_rewrite(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(
            host_rewrite=host_rewrite, path_prefix_rewrite=path_prefix_rewrite
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewrite", [value]))

    @jsii.member(jsii_name="putWeightedBackendServices")
    def put_weighted_backend_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference.put_weighted_backend_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedBackendServices", [value]))

    @jsii.member(jsii_name="resetCorsPolicy")
    def reset_cors_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsPolicy", []))

    @jsii.member(jsii_name="resetFaultInjectionPolicy")
    def reset_fault_injection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaultInjectionPolicy", []))

    @jsii.member(jsii_name="resetRequestMirrorPolicy")
    def reset_request_mirror_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMirrorPolicy", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrlRewrite")
    def reset_url_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewrite", []))

    @jsii.member(jsii_name="resetWeightedBackendServices")
    def reset_weighted_backend_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedBackendServices", []))

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, jsii.get(self, "corsPolicy"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference, jsii.get(self, "faultInjectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference", jsii.get(self, "requestMirrorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="urlRewrite")
    def url_rewrite(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference", jsii.get(self, "urlRewrite"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServices")
    def weighted_backend_services(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList", jsii.get(self, "weightedBackendServices"))

    @builtins.property
    @jsii.member(jsii_name="corsPolicyInput")
    def cors_policy_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy], jsii.get(self, "corsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicyInput")
    def fault_injection_policy_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy], jsii.get(self, "faultInjectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicyInput")
    def request_mirror_policy_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"], jsii.get(self, "requestMirrorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteInput")
    def url_rewrite_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"], jsii.get(self, "urlRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServicesInput")
    def weighted_backend_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]], jsii.get(self, "weightedBackendServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy",
    jsii_struct_bases=[],
    name_mapping={"backend_service": "backendService"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy:
    def __init__(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
        }

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The RegionBackendService resource being mirrored to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "num_retries": "numRetries",
        "per_try_timeout": "perTryTimeout",
        "retry_conditions": "retryConditions",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy:
    def __init__(
        self,
        *,
        num_retries: jsii.Number,
        per_try_timeout: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        if isinstance(per_try_timeout, dict):
            per_try_timeout = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(**per_try_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy.__init__)
            check_type(argname="argument num_retries", value=num_retries, expected_type=type_hints["num_retries"])
            check_type(argname="argument per_try_timeout", value=per_try_timeout, expected_type=type_hints["per_try_timeout"])
            check_type(argname="argument retry_conditions", value=retry_conditions, expected_type=type_hints["retry_conditions"])
        self._values: typing.Dict[str, typing.Any] = {
            "num_retries": num_retries,
        }
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_conditions is not None:
            self._values["retry_conditions"] = retry_conditions

    @builtins.property
    def num_retries(self) -> jsii.Number:
        '''Specifies the allowed number retries. This number must be > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#num_retries ComputeRegionUrlMap#num_retries}
        '''
        result = self._values.get("num_retries")
        assert result is not None, "Required property 'num_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def per_try_timeout(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"]:
        '''per_try_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#per_try_timeout ComputeRegionUrlMap#per_try_timeout}
        '''
        result = self._values.get("per_try_timeout")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"], result)

    @builtins.property
    def retry_conditions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more conditions when this retry rule applies. Valid values are:.

        5xx: Loadbalancer will attempt a retry if the backend service responds with
        any 5xx response code, or if the backend service does not respond at all,
        example: disconnects, reset, read timeout, connection failure, and refused
        streams.
        gateway-error: Similar to 5xx, but only applies to response codes
        502, 503 or 504.
        connect-failure: Loadbalancer will retry on failures
        connecting to backend services, for example due to connection timeouts.
        retriable-4xx: Loadbalancer will retry for retriable 4xx response codes.
        Currently the only retriable error supported is 409.
        refused-stream: Loadbalancer will retry if the backend service resets the stream with a
        REFUSED_STREAM error code. This reset type indicates that it is safe to retry.
        cancelled: Loadbalancer will retry if the gRPC status code in the response
        header is set to cancelled
        deadline-exceeded: Loadbalancer will retry if the
        gRPC status code in the response header is set to deadline-exceeded
        resource-exhausted: Loadbalancer will retry if the gRPC status code in the response
        header is set to resource-exhausted
        unavailable: Loadbalancer will retry if the gRPC status code in
        the response header is set to unavailable

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#retry_conditions ComputeRegionUrlMap#retry_conditions}
        '''
        result = self._values.get("retry_conditions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerTryTimeout")
    def put_per_try_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putPerTryTimeout", [value]))

    @jsii.member(jsii_name="resetPerTryTimeout")
    def reset_per_try_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerTryTimeout", []))

    @jsii.member(jsii_name="resetRetryConditions")
    def reset_retry_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConditions", []))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeout")
    def per_try_timeout(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference", jsii.get(self, "perTryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="numRetriesInput")
    def num_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeoutInput")
    def per_try_timeout_input(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"]:
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"], jsii.get(self, "perTryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConditionsInput")
    def retry_conditions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "retryConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="numRetries")
    def num_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRetries"))

    @num_retries.setter
    def num_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "num_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numRetries", value)

    @builtins.property
    @jsii.member(jsii_name="retryConditions")
    def retry_conditions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryConditions"))

    @retry_conditions.setter
    def retry_conditions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "retry_conditions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryConditions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#seconds ComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#nanos ComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite",
    jsii_struct_bases=[],
    name_mapping={
        "host_rewrite": "hostRewrite",
        "path_prefix_rewrite": "pathPrefixRewrite",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite:
    def __init__(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite.__init__)
            check_type(argname="argument host_rewrite", value=host_rewrite, expected_type=type_hints["host_rewrite"])
            check_type(argname="argument path_prefix_rewrite", value=path_prefix_rewrite, expected_type=type_hints["path_prefix_rewrite"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_rewrite is not None:
            self._values["host_rewrite"] = host_rewrite
        if path_prefix_rewrite is not None:
            self._values["path_prefix_rewrite"] = path_prefix_rewrite

    @builtins.property
    def host_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite.

        The value must be between 1 and
        255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_rewrite ComputeRegionUrlMap#host_rewrite}
        '''
        result = self._values.get("host_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_prefix_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite.

        The value must
        be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_prefix_rewrite ComputeRegionUrlMap#path_prefix_rewrite}
        '''
        result = self._values.get("path_prefix_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRewrite")
    def reset_host_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRewrite", []))

    @jsii.member(jsii_name="resetPathPrefixRewrite")
    def reset_path_prefix_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="hostRewriteInput")
    def host_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewriteInput")
    def path_prefix_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRewrite")
    def host_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRewrite"))

    @host_rewrite.setter
    def host_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "host_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefixRewrite"))

    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "path_prefix_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices",
    jsii_struct_bases=[],
    name_mapping={
        "backend_service": "backendService",
        "weight": "weight",
        "header_action": "headerAction",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices:
    def __init__(
        self,
        *,
        backend_service: builtins.str,
        weight: jsii.Number,
        header_action: typing.Optional[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend_service: The default RegionBackendService resource. Before forwarding the request to backendService, the loadbalancer applies any relevant headerActions specified as part of this backendServiceWeight. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        :param weight: Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) . The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backendService, subsequent requests will be sent to the same backendService as determined by the BackendService's session affinity policy. The value must be between 0 and 1000 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weight ComputeRegionUrlMap#weight}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        '''
        if isinstance(header_action, dict):
            header_action = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(**header_action)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
            "weight": weight,
        }
        if header_action is not None:
            self._values["header_action"] = header_action

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The default RegionBackendService resource.

        Before
        forwarding the request to backendService, the loadbalancer applies any relevant
        headerActions specified as part of this backendServiceWeight.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#backend_service ComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) .

        The selection of a
        backend service is determined only for new traffic. Once a user's request has
        been directed to a backendService, subsequent requests will be sent to the same
        backendService as determined by the BackendService's session affinity policy.
        The value must be between 0 and 1000

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#weight ComputeRegionUrlMap#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_action ComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList":
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_name ComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#header_value ComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#replace ComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_add ComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#request_headers_to_remove ComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_add ComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#response_headers_to_remove ComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference:
        return typing.cast(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
        "strip_query": "stripQuery",
    },
)
class ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect:
    def __init__(
        self,
        *,
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
        strip_query: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect.__init__)
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code
        if strip_query is not None:
            self._values["strip_query"] = strip_query

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host_redirect ComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to false, the URL scheme of the redirected request will remain the
        same as that of the request. This must only be set for UrlMaps used in
        TargetHttpProxys. Setting this true for TargetHttpsProxy is not
        permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#https_redirect ComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied
        together with prefixRedirect. Supply one alone or neither. If neither is
        supplied, the path of the original request will be used for the redirect.
        The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path_redirect ComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with
        pathRedirect. Supply one alone or neither. If neither is supplied, the
        path of the original request will be used for the redirect. The value
        must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#prefix_redirect ComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#redirect_response_code ComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strip_query(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query
        portion of the original URL is retained. The default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#strip_query ComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @jsii.member(jsii_name="resetStripQuery")
    def reset_strip_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStripQuery", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect]:
        return typing.cast(typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapTest",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "path": "path",
        "service": "service",
        "description": "description",
    },
)
class ComputeRegionUrlMapTest:
    def __init__(
        self,
        *,
        host: builtins.str,
        path: builtins.str,
        service: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Host portion of the URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host ComputeRegionUrlMap#host}
        :param path: Path portion of the URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path ComputeRegionUrlMap#path}
        :param service: A reference to expected RegionBackendService resource the given URL should be mapped to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        :param description: Description of this test case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTest.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "path": path,
            "service": service,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def host(self) -> builtins.str:
        '''Host portion of the URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#host ComputeRegionUrlMap#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path portion of the URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#path ComputeRegionUrlMap#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''A reference to expected RegionBackendService resource the given URL should be mapped to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#service ComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of this test case.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#description ComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapTest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapTestList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapTestList",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTestList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ComputeRegionUrlMapTestOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTestList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeRegionUrlMapTestOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapTest]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapTest]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeRegionUrlMapTest]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeRegionUrlMapTestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapTestOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTestOutputReference.__init__)
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
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapTest, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapTest, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapTest, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeRegionUrlMapTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#create ComputeRegionUrlMap#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delete ComputeRegionUrlMap#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#update ComputeRegionUrlMap#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#create ComputeRegionUrlMap#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#delete ComputeRegionUrlMap#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_region_url_map#update ComputeRegionUrlMap#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRegionUrlMapTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeRegionUrlMapTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeRegionUrlMap.ComputeRegionUrlMapTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeRegionUrlMapTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeRegionUrlMapTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeRegionUrlMapTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeRegionUrlMapTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeRegionUrlMapTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeRegionUrlMap",
    "ComputeRegionUrlMapConfig",
    "ComputeRegionUrlMapDefaultUrlRedirect",
    "ComputeRegionUrlMapDefaultUrlRedirectOutputReference",
    "ComputeRegionUrlMapHostRule",
    "ComputeRegionUrlMapHostRuleList",
    "ComputeRegionUrlMapHostRuleOutputReference",
    "ComputeRegionUrlMapPathMatcher",
    "ComputeRegionUrlMapPathMatcherDefaultUrlRedirect",
    "ComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference",
    "ComputeRegionUrlMapPathMatcherList",
    "ComputeRegionUrlMapPathMatcherOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRule",
    "ComputeRegionUrlMapPathMatcherPathRuleList",
    "ComputeRegionUrlMapPathMatcherPathRuleOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteAction",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList",
    "ComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference",
    "ComputeRegionUrlMapPathMatcherPathRuleUrlRedirect",
    "ComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRules",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderAction",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRules",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList",
    "ComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteAction",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList",
    "ComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference",
    "ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect",
    "ComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference",
    "ComputeRegionUrlMapTest",
    "ComputeRegionUrlMapTestList",
    "ComputeRegionUrlMapTestOutputReference",
    "ComputeRegionUrlMapTimeouts",
    "ComputeRegionUrlMapTimeoutsOutputReference",
]

publication.publish()
