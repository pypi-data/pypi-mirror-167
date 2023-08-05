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


class ComputeSecurityPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy google_compute_security_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        adaptive_protection_config: typing.Optional[typing.Union["ComputeSecurityPolicyAdaptiveProtectionConfig", typing.Dict[str, typing.Any]]] = None,
        advanced_options_config: typing.Optional[typing.Union["ComputeSecurityPolicyAdvancedOptionsConfig", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeSecurityPolicyRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ComputeSecurityPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy google_compute_security_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the security policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#name ComputeSecurityPolicy#name}
        :param adaptive_protection_config: adaptive_protection_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#adaptive_protection_config ComputeSecurityPolicy#adaptive_protection_config}
        :param advanced_options_config: advanced_options_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#advanced_options_config ComputeSecurityPolicy#advanced_options_config}
        :param description: An optional description of this security policy. Max size is 2048. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#description ComputeSecurityPolicy#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#id ComputeSecurityPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#project ComputeSecurityPolicy#project}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule ComputeSecurityPolicy#rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#timeouts ComputeSecurityPolicy#timeouts}
        :param type: The type indicates the intended use of the security policy. CLOUD_ARMOR - Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers. CLOUD_ARMOR_EDGE - Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeSecurityPolicyConfig(
            name=name,
            adaptive_protection_config=adaptive_protection_config,
            advanced_options_config=advanced_options_config,
            description=description,
            id=id,
            project=project,
            rule=rule,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdaptiveProtectionConfig")
    def put_adaptive_protection_config(
        self,
        *,
        layer7_ddos_defense_config: typing.Optional[typing.Union["ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param layer7_ddos_defense_config: layer_7_ddos_defense_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#layer_7_ddos_defense_config ComputeSecurityPolicy#layer_7_ddos_defense_config}
        '''
        value = ComputeSecurityPolicyAdaptiveProtectionConfig(
            layer7_ddos_defense_config=layer7_ddos_defense_config
        )

        return typing.cast(None, jsii.invoke(self, "putAdaptiveProtectionConfig", [value]))

    @jsii.member(jsii_name="putAdvancedOptionsConfig")
    def put_advanced_options_config(
        self,
        *,
        json_parsing: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param json_parsing: JSON body parsing. Supported values include: "DISABLED", "STANDARD". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#json_parsing ComputeSecurityPolicy#json_parsing}
        :param log_level: Logging level. Supported values include: "NORMAL", "VERBOSE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#log_level ComputeSecurityPolicy#log_level}
        '''
        value = ComputeSecurityPolicyAdvancedOptionsConfig(
            json_parsing=json_parsing, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedOptionsConfig", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeSecurityPolicyRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicy.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#create ComputeSecurityPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#delete ComputeSecurityPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#update ComputeSecurityPolicy#update}.
        '''
        value = ComputeSecurityPolicyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdaptiveProtectionConfig")
    def reset_adaptive_protection_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdaptiveProtectionConfig", []))

    @jsii.member(jsii_name="resetAdvancedOptionsConfig")
    def reset_advanced_options_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedOptionsConfig", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="adaptiveProtectionConfig")
    def adaptive_protection_config(
        self,
    ) -> "ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference":
        return typing.cast("ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference", jsii.get(self, "adaptiveProtectionConfig"))

    @builtins.property
    @jsii.member(jsii_name="advancedOptionsConfig")
    def advanced_options_config(
        self,
    ) -> "ComputeSecurityPolicyAdvancedOptionsConfigOutputReference":
        return typing.cast("ComputeSecurityPolicyAdvancedOptionsConfigOutputReference", jsii.get(self, "advancedOptionsConfig"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ComputeSecurityPolicyRuleList":
        return typing.cast("ComputeSecurityPolicyRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeSecurityPolicyTimeoutsOutputReference":
        return typing.cast("ComputeSecurityPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="adaptiveProtectionConfigInput")
    def adaptive_protection_config_input(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyAdaptiveProtectionConfig"]:
        return typing.cast(typing.Optional["ComputeSecurityPolicyAdaptiveProtectionConfig"], jsii.get(self, "adaptiveProtectionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedOptionsConfigInput")
    def advanced_options_config_input(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyAdvancedOptionsConfig"]:
        return typing.cast(typing.Optional["ComputeSecurityPolicyAdvancedOptionsConfig"], jsii.get(self, "advancedOptionsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeSecurityPolicyRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeSecurityPolicyRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeSecurityPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeSecurityPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicy, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicy, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicy, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdaptiveProtectionConfig",
    jsii_struct_bases=[],
    name_mapping={"layer7_ddos_defense_config": "layer7DdosDefenseConfig"},
)
class ComputeSecurityPolicyAdaptiveProtectionConfig:
    def __init__(
        self,
        *,
        layer7_ddos_defense_config: typing.Optional[typing.Union["ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param layer7_ddos_defense_config: layer_7_ddos_defense_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#layer_7_ddos_defense_config ComputeSecurityPolicy#layer_7_ddos_defense_config}
        '''
        if isinstance(layer7_ddos_defense_config, dict):
            layer7_ddos_defense_config = ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(**layer7_ddos_defense_config)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdaptiveProtectionConfig.__init__)
            check_type(argname="argument layer7_ddos_defense_config", value=layer7_ddos_defense_config, expected_type=type_hints["layer7_ddos_defense_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if layer7_ddos_defense_config is not None:
            self._values["layer7_ddos_defense_config"] = layer7_ddos_defense_config

    @builtins.property
    def layer7_ddos_defense_config(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig"]:
        '''layer_7_ddos_defense_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#layer_7_ddos_defense_config ComputeSecurityPolicy#layer_7_ddos_defense_config}
        '''
        result = self._values.get("layer7_ddos_defense_config")
        return typing.cast(typing.Optional["ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyAdaptiveProtectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable", "rule_visibility": "ruleVisibility"},
)
class ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig:
    def __init__(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rule_visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable: If set to true, enables CAAP for L7 DDoS detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enable ComputeSecurityPolicy#enable}
        :param rule_visibility: Rule visibility. Supported values include: "STANDARD", "PREMIUM". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule_visibility ComputeSecurityPolicy#rule_visibility}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig.__init__)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument rule_visibility", value=rule_visibility, expected_type=type_hints["rule_visibility"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable is not None:
            self._values["enable"] = enable
        if rule_visibility is not None:
            self._values["rule_visibility"] = rule_visibility

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, enables CAAP for L7 DDoS detection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enable ComputeSecurityPolicy#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rule_visibility(self) -> typing.Optional[builtins.str]:
        '''Rule visibility. Supported values include: "STANDARD", "PREMIUM".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule_visibility ComputeSecurityPolicy#rule_visibility}
        '''
        result = self._values.get("rule_visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetRuleVisibility")
    def reset_rule_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleVisibility", []))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleVisibilityInput")
    def rule_visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="ruleVisibility")
    def rule_visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleVisibility"))

    @rule_visibility.setter
    def rule_visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference, "rule_visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLayer7DdosDefenseConfig")
    def put_layer7_ddos_defense_config(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rule_visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable: If set to true, enables CAAP for L7 DDoS detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enable ComputeSecurityPolicy#enable}
        :param rule_visibility: Rule visibility. Supported values include: "STANDARD", "PREMIUM". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule_visibility ComputeSecurityPolicy#rule_visibility}
        '''
        value = ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(
            enable=enable, rule_visibility=rule_visibility
        )

        return typing.cast(None, jsii.invoke(self, "putLayer7DdosDefenseConfig", [value]))

    @jsii.member(jsii_name="resetLayer7DdosDefenseConfig")
    def reset_layer7_ddos_defense_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLayer7DdosDefenseConfig", []))

    @builtins.property
    @jsii.member(jsii_name="layer7DdosDefenseConfig")
    def layer7_ddos_defense_config(
        self,
    ) -> ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference:
        return typing.cast(ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference, jsii.get(self, "layer7DdosDefenseConfig"))

    @builtins.property
    @jsii.member(jsii_name="layer7DdosDefenseConfigInput")
    def layer7_ddos_defense_config_input(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig], jsii.get(self, "layer7DdosDefenseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdvancedOptionsConfig",
    jsii_struct_bases=[],
    name_mapping={"json_parsing": "jsonParsing", "log_level": "logLevel"},
)
class ComputeSecurityPolicyAdvancedOptionsConfig:
    def __init__(
        self,
        *,
        json_parsing: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param json_parsing: JSON body parsing. Supported values include: "DISABLED", "STANDARD". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#json_parsing ComputeSecurityPolicy#json_parsing}
        :param log_level: Logging level. Supported values include: "NORMAL", "VERBOSE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#log_level ComputeSecurityPolicy#log_level}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdvancedOptionsConfig.__init__)
            check_type(argname="argument json_parsing", value=json_parsing, expected_type=type_hints["json_parsing"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if json_parsing is not None:
            self._values["json_parsing"] = json_parsing
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def json_parsing(self) -> typing.Optional[builtins.str]:
        '''JSON body parsing. Supported values include: "DISABLED", "STANDARD".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#json_parsing ComputeSecurityPolicy#json_parsing}
        '''
        result = self._values.get("json_parsing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Logging level. Supported values include: "NORMAL", "VERBOSE".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#log_level ComputeSecurityPolicy#log_level}
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyAdvancedOptionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyAdvancedOptionsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyAdvancedOptionsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyAdvancedOptionsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetJsonParsing")
    def reset_json_parsing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonParsing", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="jsonParsingInput")
    def json_parsing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonParsingInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonParsing")
    def json_parsing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonParsing"))

    @json_parsing.setter
    def json_parsing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdvancedOptionsConfigOutputReference, "json_parsing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonParsing", value)

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdvancedOptionsConfigOutputReference, "log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdvancedOptionsConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdvancedOptionsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyAdvancedOptionsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyAdvancedOptionsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyConfig",
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
        "adaptive_protection_config": "adaptiveProtectionConfig",
        "advanced_options_config": "advancedOptionsConfig",
        "description": "description",
        "id": "id",
        "project": "project",
        "rule": "rule",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class ComputeSecurityPolicyConfig(cdktf.TerraformMetaArguments):
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
        adaptive_protection_config: typing.Optional[typing.Union[ComputeSecurityPolicyAdaptiveProtectionConfig, typing.Dict[str, typing.Any]]] = None,
        advanced_options_config: typing.Optional[typing.Union[ComputeSecurityPolicyAdvancedOptionsConfig, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeSecurityPolicyRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ComputeSecurityPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the security policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#name ComputeSecurityPolicy#name}
        :param adaptive_protection_config: adaptive_protection_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#adaptive_protection_config ComputeSecurityPolicy#adaptive_protection_config}
        :param advanced_options_config: advanced_options_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#advanced_options_config ComputeSecurityPolicy#advanced_options_config}
        :param description: An optional description of this security policy. Max size is 2048. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#description ComputeSecurityPolicy#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#id ComputeSecurityPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#project ComputeSecurityPolicy#project}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule ComputeSecurityPolicy#rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#timeouts ComputeSecurityPolicy#timeouts}
        :param type: The type indicates the intended use of the security policy. CLOUD_ARMOR - Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers. CLOUD_ARMOR_EDGE - Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(adaptive_protection_config, dict):
            adaptive_protection_config = ComputeSecurityPolicyAdaptiveProtectionConfig(**adaptive_protection_config)
        if isinstance(advanced_options_config, dict):
            advanced_options_config = ComputeSecurityPolicyAdvancedOptionsConfig(**advanced_options_config)
        if isinstance(timeouts, dict):
            timeouts = ComputeSecurityPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument adaptive_protection_config", value=adaptive_protection_config, expected_type=type_hints["adaptive_protection_config"])
            check_type(argname="argument advanced_options_config", value=advanced_options_config, expected_type=type_hints["advanced_options_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
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
        if adaptive_protection_config is not None:
            self._values["adaptive_protection_config"] = adaptive_protection_config
        if advanced_options_config is not None:
            self._values["advanced_options_config"] = advanced_options_config
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if rule is not None:
            self._values["rule"] = rule
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
        '''The name of the security policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#name ComputeSecurityPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adaptive_protection_config(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfig]:
        '''adaptive_protection_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#adaptive_protection_config ComputeSecurityPolicy#adaptive_protection_config}
        '''
        result = self._values.get("adaptive_protection_config")
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdaptiveProtectionConfig], result)

    @builtins.property
    def advanced_options_config(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyAdvancedOptionsConfig]:
        '''advanced_options_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#advanced_options_config ComputeSecurityPolicy#advanced_options_config}
        '''
        result = self._values.get("advanced_options_config")
        return typing.cast(typing.Optional[ComputeSecurityPolicyAdvancedOptionsConfig], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this security policy. Max size is 2048.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#description ComputeSecurityPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#id ComputeSecurityPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project in which the resource belongs. If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#project ComputeSecurityPolicy#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeSecurityPolicyRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rule ComputeSecurityPolicy#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeSecurityPolicyRule"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeSecurityPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#timeouts ComputeSecurityPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeSecurityPolicyTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type indicates the intended use of the security policy.

        CLOUD_ARMOR - Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers. CLOUD_ARMOR_EDGE - Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match": "match",
        "priority": "priority",
        "description": "description",
        "preview": "preview",
        "rate_limit_options": "rateLimitOptions",
        "redirect_options": "redirectOptions",
    },
)
class ComputeSecurityPolicyRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        match: typing.Union["ComputeSecurityPolicyRuleMatch", typing.Dict[str, typing.Any]],
        priority: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        preview: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rate_limit_options: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRateLimitOptions", typing.Dict[str, typing.Any]]] = None,
        redirect_options: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRedirectOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: Action to take when match matches the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#action ComputeSecurityPolicy#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#match ComputeSecurityPolicy#match}
        :param priority: An unique positive integer indicating the priority of evaluation for a rule. Rules are evaluated from highest priority (lowest numerically) to lowest priority (highest numerically) in order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#priority ComputeSecurityPolicy#priority}
        :param description: An optional description of this rule. Max size is 64. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#description ComputeSecurityPolicy#description}
        :param preview: When set to true, the action specified above is not enforced. Stackdriver logs for requests that trigger a preview action are annotated as such. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#preview ComputeSecurityPolicy#preview}
        :param rate_limit_options: rate_limit_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rate_limit_options ComputeSecurityPolicy#rate_limit_options}
        :param redirect_options: redirect_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#redirect_options ComputeSecurityPolicy#redirect_options}
        '''
        if isinstance(match, dict):
            match = ComputeSecurityPolicyRuleMatch(**match)
        if isinstance(rate_limit_options, dict):
            rate_limit_options = ComputeSecurityPolicyRuleRateLimitOptions(**rate_limit_options)
        if isinstance(redirect_options, dict):
            redirect_options = ComputeSecurityPolicyRuleRedirectOptions(**redirect_options)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument preview", value=preview, expected_type=type_hints["preview"])
            check_type(argname="argument rate_limit_options", value=rate_limit_options, expected_type=type_hints["rate_limit_options"])
            check_type(argname="argument redirect_options", value=redirect_options, expected_type=type_hints["redirect_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match": match,
            "priority": priority,
        }
        if description is not None:
            self._values["description"] = description
        if preview is not None:
            self._values["preview"] = preview
        if rate_limit_options is not None:
            self._values["rate_limit_options"] = rate_limit_options
        if redirect_options is not None:
            self._values["redirect_options"] = redirect_options

    @builtins.property
    def action(self) -> builtins.str:
        '''Action to take when match matches the request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#action ComputeSecurityPolicy#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match(self) -> "ComputeSecurityPolicyRuleMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#match ComputeSecurityPolicy#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("ComputeSecurityPolicyRuleMatch", result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''An unique positive integer indicating the priority of evaluation for a rule.

        Rules are evaluated from highest priority (lowest numerically) to lowest priority (highest numerically) in order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#priority ComputeSecurityPolicy#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this rule. Max size is 64.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#description ComputeSecurityPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preview(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When set to true, the action specified above is not enforced.

        Stackdriver logs for requests that trigger a preview action are annotated as such.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#preview ComputeSecurityPolicy#preview}
        '''
        result = self._values.get("preview")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rate_limit_options(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRateLimitOptions"]:
        '''rate_limit_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rate_limit_options ComputeSecurityPolicy#rate_limit_options}
        '''
        result = self._values.get("rate_limit_options")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRateLimitOptions"], result)

    @builtins.property
    def redirect_options(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRedirectOptions"]:
        '''redirect_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#redirect_options ComputeSecurityPolicy#redirect_options}
        '''
        result = self._values.get("redirect_options")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRedirectOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleList",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ComputeSecurityPolicyRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeSecurityPolicyRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeSecurityPolicyRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeSecurityPolicyRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeSecurityPolicyRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatch",
    jsii_struct_bases=[],
    name_mapping={
        "config": "config",
        "expr": "expr",
        "versioned_expr": "versionedExpr",
    },
)
class ComputeSecurityPolicyRuleMatch:
    def __init__(
        self,
        *,
        config: typing.Optional[typing.Union["ComputeSecurityPolicyRuleMatchConfig", typing.Dict[str, typing.Any]]] = None,
        expr: typing.Optional[typing.Union["ComputeSecurityPolicyRuleMatchExpr", typing.Dict[str, typing.Any]]] = None,
        versioned_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#config ComputeSecurityPolicy#config}
        :param expr: expr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expr ComputeSecurityPolicy#expr}
        :param versioned_expr: Predefined rule expression. If this field is specified, config must also be specified. Available options: SRC_IPS_V1: Must specify the corresponding src_ip_ranges field in config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#versioned_expr ComputeSecurityPolicy#versioned_expr}
        '''
        if isinstance(config, dict):
            config = ComputeSecurityPolicyRuleMatchConfig(**config)
        if isinstance(expr, dict):
            expr = ComputeSecurityPolicyRuleMatchExpr(**expr)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatch.__init__)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument expr", value=expr, expected_type=type_hints["expr"])
            check_type(argname="argument versioned_expr", value=versioned_expr, expected_type=type_hints["versioned_expr"])
        self._values: typing.Dict[str, typing.Any] = {}
        if config is not None:
            self._values["config"] = config
        if expr is not None:
            self._values["expr"] = expr
        if versioned_expr is not None:
            self._values["versioned_expr"] = versioned_expr

    @builtins.property
    def config(self) -> typing.Optional["ComputeSecurityPolicyRuleMatchConfig"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#config ComputeSecurityPolicy#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleMatchConfig"], result)

    @builtins.property
    def expr(self) -> typing.Optional["ComputeSecurityPolicyRuleMatchExpr"]:
        '''expr block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expr ComputeSecurityPolicy#expr}
        '''
        result = self._values.get("expr")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleMatchExpr"], result)

    @builtins.property
    def versioned_expr(self) -> typing.Optional[builtins.str]:
        '''Predefined rule expression.

        If this field is specified, config must also be specified. Available options:   SRC_IPS_V1: Must specify the corresponding src_ip_ranges field in config.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#versioned_expr ComputeSecurityPolicy#versioned_expr}
        '''
        result = self._values.get("versioned_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatchConfig",
    jsii_struct_bases=[],
    name_mapping={"src_ip_ranges": "srcIpRanges"},
)
class ComputeSecurityPolicyRuleMatchConfig:
    def __init__(self, *, src_ip_ranges: typing.Sequence[builtins.str]) -> None:
        '''
        :param src_ip_ranges: Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation to match against inbound traffic. There is a limit of 10 IP ranges per rule. A value of '*' matches all IPs (can be used to override the default behavior). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#src_ip_ranges ComputeSecurityPolicy#src_ip_ranges}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatchConfig.__init__)
            check_type(argname="argument src_ip_ranges", value=src_ip_ranges, expected_type=type_hints["src_ip_ranges"])
        self._values: typing.Dict[str, typing.Any] = {
            "src_ip_ranges": src_ip_ranges,
        }

    @builtins.property
    def src_ip_ranges(self) -> typing.List[builtins.str]:
        '''Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation to match against inbound traffic.

        There is a limit of 10 IP ranges per rule. A value of '*' matches all IPs (can be used to override the default behavior).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#src_ip_ranges ComputeSecurityPolicy#src_ip_ranges}
        '''
        result = self._values.get("src_ip_ranges")
        assert result is not None, "Required property 'src_ip_ranges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleMatchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatchConfigOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatchConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="srcIpRangesInput")
    def src_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "srcIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="srcIpRanges")
    def src_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "srcIpRanges"))

    @src_ip_ranges.setter
    def src_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchConfigOutputReference, "src_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "srcIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeSecurityPolicyRuleMatchConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleMatchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatchExpr",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression"},
)
class ComputeSecurityPolicyRuleMatchExpr:
    def __init__(self, *, expression: builtins.str) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. The application context of the containing message determines which well-known feature set of CEL is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expression ComputeSecurityPolicy#expression}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatchExpr.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }

    @builtins.property
    def expression(self) -> builtins.str:
        '''Textual representation of an expression in Common Expression Language syntax.

        The application context of the containing message determines which well-known feature set of CEL is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expression ComputeSecurityPolicy#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleMatchExpr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleMatchExprOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatchExprOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatchExprOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchExprOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeSecurityPolicyRuleMatchExpr]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatchExpr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleMatchExpr],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchExprOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeSecurityPolicyRuleMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleMatchOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfig")
    def put_config(self, *, src_ip_ranges: typing.Sequence[builtins.str]) -> None:
        '''
        :param src_ip_ranges: Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation to match against inbound traffic. There is a limit of 10 IP ranges per rule. A value of '*' matches all IPs (can be used to override the default behavior). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#src_ip_ranges ComputeSecurityPolicy#src_ip_ranges}
        '''
        value = ComputeSecurityPolicyRuleMatchConfig(src_ip_ranges=src_ip_ranges)

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putExpr")
    def put_expr(self, *, expression: builtins.str) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. The application context of the containing message determines which well-known feature set of CEL is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expression ComputeSecurityPolicy#expression}
        '''
        value = ComputeSecurityPolicyRuleMatchExpr(expression=expression)

        return typing.cast(None, jsii.invoke(self, "putExpr", [value]))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetExpr")
    def reset_expr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpr", []))

    @jsii.member(jsii_name="resetVersionedExpr")
    def reset_versioned_expr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionedExpr", []))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> ComputeSecurityPolicyRuleMatchConfigOutputReference:
        return typing.cast(ComputeSecurityPolicyRuleMatchConfigOutputReference, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="expr")
    def expr(self) -> ComputeSecurityPolicyRuleMatchExprOutputReference:
        return typing.cast(ComputeSecurityPolicyRuleMatchExprOutputReference, jsii.get(self, "expr"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional[ComputeSecurityPolicyRuleMatchConfig]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatchConfig], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="exprInput")
    def expr_input(self) -> typing.Optional[ComputeSecurityPolicyRuleMatchExpr]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatchExpr], jsii.get(self, "exprInput"))

    @builtins.property
    @jsii.member(jsii_name="versionedExprInput")
    def versioned_expr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionedExprInput"))

    @builtins.property
    @jsii.member(jsii_name="versionedExpr")
    def versioned_expr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionedExpr"))

    @versioned_expr.setter
    def versioned_expr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchOutputReference, "versioned_expr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionedExpr", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeSecurityPolicyRuleMatch]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeSecurityPolicyRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        config: typing.Optional[typing.Union[ComputeSecurityPolicyRuleMatchConfig, typing.Dict[str, typing.Any]]] = None,
        expr: typing.Optional[typing.Union[ComputeSecurityPolicyRuleMatchExpr, typing.Dict[str, typing.Any]]] = None,
        versioned_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#config ComputeSecurityPolicy#config}
        :param expr: expr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#expr ComputeSecurityPolicy#expr}
        :param versioned_expr: Predefined rule expression. If this field is specified, config must also be specified. Available options: SRC_IPS_V1: Must specify the corresponding src_ip_ranges field in config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#versioned_expr ComputeSecurityPolicy#versioned_expr}
        '''
        value = ComputeSecurityPolicyRuleMatch(
            config=config, expr=expr, versioned_expr=versioned_expr
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putRateLimitOptions")
    def put_rate_limit_options(
        self,
        *,
        conform_action: builtins.str,
        exceed_action: builtins.str,
        rate_limit_threshold: typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold", typing.Dict[str, typing.Any]],
        ban_duration_sec: typing.Optional[jsii.Number] = None,
        ban_threshold: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold", typing.Dict[str, typing.Any]]] = None,
        enforce_on_key: typing.Optional[builtins.str] = None,
        enforce_on_key_name: typing.Optional[builtins.str] = None,
        exceed_redirect_options: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conform_action: Action to take for requests that are under the configured rate limit threshold. Valid option is "allow" only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#conform_action ComputeSecurityPolicy#conform_action}
        :param exceed_action: Action to take for requests that are above the configured rate limit threshold, to either deny with a specified HTTP response code, or redirect to a different endpoint. Valid options are "deny()" where valid values for status are 403, 404, 429, and 502, and "redirect" where the redirect parameters come from exceedRedirectOptions below. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_action ComputeSecurityPolicy#exceed_action}
        :param rate_limit_threshold: rate_limit_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rate_limit_threshold ComputeSecurityPolicy#rate_limit_threshold}
        :param ban_duration_sec: Can only be specified if the action for the rule is "rate_based_ban". If specified, determines the time (in seconds) the traffic will continue to be banned by the rate limit after the rate falls below the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_duration_sec ComputeSecurityPolicy#ban_duration_sec}
        :param ban_threshold: ban_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_threshold ComputeSecurityPolicy#ban_threshold}
        :param enforce_on_key: Determines the key to enforce the rateLimitThreshold on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key ComputeSecurityPolicy#enforce_on_key}
        :param enforce_on_key_name: Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key_name ComputeSecurityPolicy#enforce_on_key_name}
        :param exceed_redirect_options: exceed_redirect_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_redirect_options ComputeSecurityPolicy#exceed_redirect_options}
        '''
        value = ComputeSecurityPolicyRuleRateLimitOptions(
            conform_action=conform_action,
            exceed_action=exceed_action,
            rate_limit_threshold=rate_limit_threshold,
            ban_duration_sec=ban_duration_sec,
            ban_threshold=ban_threshold,
            enforce_on_key=enforce_on_key,
            enforce_on_key_name=enforce_on_key_name,
            exceed_redirect_options=exceed_redirect_options,
        )

        return typing.cast(None, jsii.invoke(self, "putRateLimitOptions", [value]))

    @jsii.member(jsii_name="putRedirectOptions")
    def put_redirect_options(
        self,
        *,
        type: builtins.str,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of the redirect action. Available options: EXTERNAL_302: Must specify the corresponding target field in config. GOOGLE_RECAPTCHA: Cannot specify target field in config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        :param target: Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        value = ComputeSecurityPolicyRuleRedirectOptions(type=type, target=target)

        return typing.cast(None, jsii.invoke(self, "putRedirectOptions", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPreview")
    def reset_preview(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreview", []))

    @jsii.member(jsii_name="resetRateLimitOptions")
    def reset_rate_limit_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimitOptions", []))

    @jsii.member(jsii_name="resetRedirectOptions")
    def reset_redirect_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectOptions", []))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> ComputeSecurityPolicyRuleMatchOutputReference:
        return typing.cast(ComputeSecurityPolicyRuleMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitOptions")
    def rate_limit_options(
        self,
    ) -> "ComputeSecurityPolicyRuleRateLimitOptionsOutputReference":
        return typing.cast("ComputeSecurityPolicyRuleRateLimitOptionsOutputReference", jsii.get(self, "rateLimitOptions"))

    @builtins.property
    @jsii.member(jsii_name="redirectOptions")
    def redirect_options(
        self,
    ) -> "ComputeSecurityPolicyRuleRedirectOptionsOutputReference":
        return typing.cast("ComputeSecurityPolicyRuleRedirectOptionsOutputReference", jsii.get(self, "redirectOptions"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[ComputeSecurityPolicyRuleMatch]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="previewInput")
    def preview_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "previewInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitOptionsInput")
    def rate_limit_options_input(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRateLimitOptions"]:
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRateLimitOptions"], jsii.get(self, "rateLimitOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectOptionsInput")
    def redirect_options_input(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRedirectOptions"]:
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRedirectOptions"], jsii.get(self, "redirectOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="preview")
    def preview(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preview"))

    @preview.setter
    def preview(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleOutputReference, "preview").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preview", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeSecurityPolicyRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeSecurityPolicyRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeSecurityPolicyRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptions",
    jsii_struct_bases=[],
    name_mapping={
        "conform_action": "conformAction",
        "exceed_action": "exceedAction",
        "rate_limit_threshold": "rateLimitThreshold",
        "ban_duration_sec": "banDurationSec",
        "ban_threshold": "banThreshold",
        "enforce_on_key": "enforceOnKey",
        "enforce_on_key_name": "enforceOnKeyName",
        "exceed_redirect_options": "exceedRedirectOptions",
    },
)
class ComputeSecurityPolicyRuleRateLimitOptions:
    def __init__(
        self,
        *,
        conform_action: builtins.str,
        exceed_action: builtins.str,
        rate_limit_threshold: typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold", typing.Dict[str, typing.Any]],
        ban_duration_sec: typing.Optional[jsii.Number] = None,
        ban_threshold: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold", typing.Dict[str, typing.Any]]] = None,
        enforce_on_key: typing.Optional[builtins.str] = None,
        enforce_on_key_name: typing.Optional[builtins.str] = None,
        exceed_redirect_options: typing.Optional[typing.Union["ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conform_action: Action to take for requests that are under the configured rate limit threshold. Valid option is "allow" only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#conform_action ComputeSecurityPolicy#conform_action}
        :param exceed_action: Action to take for requests that are above the configured rate limit threshold, to either deny with a specified HTTP response code, or redirect to a different endpoint. Valid options are "deny()" where valid values for status are 403, 404, 429, and 502, and "redirect" where the redirect parameters come from exceedRedirectOptions below. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_action ComputeSecurityPolicy#exceed_action}
        :param rate_limit_threshold: rate_limit_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rate_limit_threshold ComputeSecurityPolicy#rate_limit_threshold}
        :param ban_duration_sec: Can only be specified if the action for the rule is "rate_based_ban". If specified, determines the time (in seconds) the traffic will continue to be banned by the rate limit after the rate falls below the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_duration_sec ComputeSecurityPolicy#ban_duration_sec}
        :param ban_threshold: ban_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_threshold ComputeSecurityPolicy#ban_threshold}
        :param enforce_on_key: Determines the key to enforce the rateLimitThreshold on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key ComputeSecurityPolicy#enforce_on_key}
        :param enforce_on_key_name: Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key_name ComputeSecurityPolicy#enforce_on_key_name}
        :param exceed_redirect_options: exceed_redirect_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_redirect_options ComputeSecurityPolicy#exceed_redirect_options}
        '''
        if isinstance(rate_limit_threshold, dict):
            rate_limit_threshold = ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold(**rate_limit_threshold)
        if isinstance(ban_threshold, dict):
            ban_threshold = ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold(**ban_threshold)
        if isinstance(exceed_redirect_options, dict):
            exceed_redirect_options = ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions(**exceed_redirect_options)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptions.__init__)
            check_type(argname="argument conform_action", value=conform_action, expected_type=type_hints["conform_action"])
            check_type(argname="argument exceed_action", value=exceed_action, expected_type=type_hints["exceed_action"])
            check_type(argname="argument rate_limit_threshold", value=rate_limit_threshold, expected_type=type_hints["rate_limit_threshold"])
            check_type(argname="argument ban_duration_sec", value=ban_duration_sec, expected_type=type_hints["ban_duration_sec"])
            check_type(argname="argument ban_threshold", value=ban_threshold, expected_type=type_hints["ban_threshold"])
            check_type(argname="argument enforce_on_key", value=enforce_on_key, expected_type=type_hints["enforce_on_key"])
            check_type(argname="argument enforce_on_key_name", value=enforce_on_key_name, expected_type=type_hints["enforce_on_key_name"])
            check_type(argname="argument exceed_redirect_options", value=exceed_redirect_options, expected_type=type_hints["exceed_redirect_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "conform_action": conform_action,
            "exceed_action": exceed_action,
            "rate_limit_threshold": rate_limit_threshold,
        }
        if ban_duration_sec is not None:
            self._values["ban_duration_sec"] = ban_duration_sec
        if ban_threshold is not None:
            self._values["ban_threshold"] = ban_threshold
        if enforce_on_key is not None:
            self._values["enforce_on_key"] = enforce_on_key
        if enforce_on_key_name is not None:
            self._values["enforce_on_key_name"] = enforce_on_key_name
        if exceed_redirect_options is not None:
            self._values["exceed_redirect_options"] = exceed_redirect_options

    @builtins.property
    def conform_action(self) -> builtins.str:
        '''Action to take for requests that are under the configured rate limit threshold. Valid option is "allow" only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#conform_action ComputeSecurityPolicy#conform_action}
        '''
        result = self._values.get("conform_action")
        assert result is not None, "Required property 'conform_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exceed_action(self) -> builtins.str:
        '''Action to take for requests that are above the configured rate limit threshold, to either deny with a specified HTTP response code, or redirect to a different endpoint.

        Valid options are "deny()" where valid values for status are 403, 404, 429, and 502, and "redirect" where the redirect parameters come from exceedRedirectOptions below.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_action ComputeSecurityPolicy#exceed_action}
        '''
        result = self._values.get("exceed_action")
        assert result is not None, "Required property 'exceed_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rate_limit_threshold(
        self,
    ) -> "ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold":
        '''rate_limit_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#rate_limit_threshold ComputeSecurityPolicy#rate_limit_threshold}
        '''
        result = self._values.get("rate_limit_threshold")
        assert result is not None, "Required property 'rate_limit_threshold' is missing"
        return typing.cast("ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold", result)

    @builtins.property
    def ban_duration_sec(self) -> typing.Optional[jsii.Number]:
        '''Can only be specified if the action for the rule is "rate_based_ban".

        If specified, determines the time (in seconds) the traffic will continue to be banned by the rate limit after the rate falls below the threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_duration_sec ComputeSecurityPolicy#ban_duration_sec}
        '''
        result = self._values.get("ban_duration_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ban_threshold(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold"]:
        '''ban_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#ban_threshold ComputeSecurityPolicy#ban_threshold}
        '''
        result = self._values.get("ban_threshold")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold"], result)

    @builtins.property
    def enforce_on_key(self) -> typing.Optional[builtins.str]:
        '''Determines the key to enforce the rateLimitThreshold on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key ComputeSecurityPolicy#enforce_on_key}
        '''
        result = self._values.get("enforce_on_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enforce_on_key_name(self) -> typing.Optional[builtins.str]:
        '''Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value.

        HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#enforce_on_key_name ComputeSecurityPolicy#enforce_on_key_name}
        '''
        result = self._values.get("enforce_on_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exceed_redirect_options(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions"]:
        '''exceed_redirect_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#exceed_redirect_options ComputeSecurityPolicy#exceed_redirect_options}
        '''
        result = self._values.get("exceed_redirect_options")
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleRateLimitOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval_sec": "intervalSec"},
)
class ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold:
    def __init__(self, *, count: jsii.Number, interval_sec: jsii.Number) -> None:
        '''
        :param count: Number of HTTP(S) requests for calculating the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        :param interval_sec: Interval over which the threshold is computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval_sec", value=interval_sec, expected_type=type_hints["interval_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval_sec": interval_sec,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Number of HTTP(S) requests for calculating the threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        '''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_sec(self) -> jsii.Number:
        '''Interval over which the threshold is computed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        result = self._values.get("interval_sec")
        assert result is not None, "Required property 'interval_sec' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSecInput")
    def interval_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="intervalSec")
    def interval_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSec"))

    @interval_sec.setter
    def interval_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference, "interval_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "target": "target"},
)
class ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions:
    def __init__(
        self,
        *,
        type: builtins.str,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of the redirect action. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        :param target: Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the redirect action.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeSecurityPolicyRuleRateLimitOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBanThreshold")
    def put_ban_threshold(
        self,
        *,
        count: jsii.Number,
        interval_sec: jsii.Number,
    ) -> None:
        '''
        :param count: Number of HTTP(S) requests for calculating the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        :param interval_sec: Interval over which the threshold is computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        value = ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold(
            count=count, interval_sec=interval_sec
        )

        return typing.cast(None, jsii.invoke(self, "putBanThreshold", [value]))

    @jsii.member(jsii_name="putExceedRedirectOptions")
    def put_exceed_redirect_options(
        self,
        *,
        type: builtins.str,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of the redirect action. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        :param target: Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        value = ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions(
            type=type, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putExceedRedirectOptions", [value]))

    @jsii.member(jsii_name="putRateLimitThreshold")
    def put_rate_limit_threshold(
        self,
        *,
        count: jsii.Number,
        interval_sec: jsii.Number,
    ) -> None:
        '''
        :param count: Number of HTTP(S) requests for calculating the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        :param interval_sec: Interval over which the threshold is computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        value = ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold(
            count=count, interval_sec=interval_sec
        )

        return typing.cast(None, jsii.invoke(self, "putRateLimitThreshold", [value]))

    @jsii.member(jsii_name="resetBanDurationSec")
    def reset_ban_duration_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBanDurationSec", []))

    @jsii.member(jsii_name="resetBanThreshold")
    def reset_ban_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBanThreshold", []))

    @jsii.member(jsii_name="resetEnforceOnKey")
    def reset_enforce_on_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceOnKey", []))

    @jsii.member(jsii_name="resetEnforceOnKeyName")
    def reset_enforce_on_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceOnKeyName", []))

    @jsii.member(jsii_name="resetExceedRedirectOptions")
    def reset_exceed_redirect_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExceedRedirectOptions", []))

    @builtins.property
    @jsii.member(jsii_name="banThreshold")
    def ban_threshold(
        self,
    ) -> ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference:
        return typing.cast(ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference, jsii.get(self, "banThreshold"))

    @builtins.property
    @jsii.member(jsii_name="exceedRedirectOptions")
    def exceed_redirect_options(
        self,
    ) -> ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference:
        return typing.cast(ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference, jsii.get(self, "exceedRedirectOptions"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitThreshold")
    def rate_limit_threshold(
        self,
    ) -> "ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference":
        return typing.cast("ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference", jsii.get(self, "rateLimitThreshold"))

    @builtins.property
    @jsii.member(jsii_name="banDurationSecInput")
    def ban_duration_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "banDurationSecInput"))

    @builtins.property
    @jsii.member(jsii_name="banThresholdInput")
    def ban_threshold_input(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold], jsii.get(self, "banThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="conformActionInput")
    def conform_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conformActionInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceOnKeyInput")
    def enforce_on_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enforceOnKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceOnKeyNameInput")
    def enforce_on_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enforceOnKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="exceedActionInput")
    def exceed_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exceedActionInput"))

    @builtins.property
    @jsii.member(jsii_name="exceedRedirectOptionsInput")
    def exceed_redirect_options_input(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions], jsii.get(self, "exceedRedirectOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitThresholdInput")
    def rate_limit_threshold_input(
        self,
    ) -> typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold"]:
        return typing.cast(typing.Optional["ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold"], jsii.get(self, "rateLimitThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="banDurationSec")
    def ban_duration_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "banDurationSec"))

    @ban_duration_sec.setter
    def ban_duration_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "ban_duration_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "banDurationSec", value)

    @builtins.property
    @jsii.member(jsii_name="conformAction")
    def conform_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conformAction"))

    @conform_action.setter
    def conform_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "conform_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformAction", value)

    @builtins.property
    @jsii.member(jsii_name="enforceOnKey")
    def enforce_on_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enforceOnKey"))

    @enforce_on_key.setter
    def enforce_on_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "enforce_on_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceOnKey", value)

    @builtins.property
    @jsii.member(jsii_name="enforceOnKeyName")
    def enforce_on_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enforceOnKeyName"))

    @enforce_on_key_name.setter
    def enforce_on_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "enforce_on_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceOnKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="exceedAction")
    def exceed_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exceedAction"))

    @exceed_action.setter
    def exceed_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "exceed_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceedAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptions]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleRateLimitOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval_sec": "intervalSec"},
)
class ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold:
    def __init__(self, *, count: jsii.Number, interval_sec: jsii.Number) -> None:
        '''
        :param count: Number of HTTP(S) requests for calculating the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        :param interval_sec: Interval over which the threshold is computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval_sec", value=interval_sec, expected_type=type_hints["interval_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval_sec": interval_sec,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Number of HTTP(S) requests for calculating the threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#count ComputeSecurityPolicy#count}
        '''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_sec(self) -> jsii.Number:
        '''Interval over which the threshold is computed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#interval_sec ComputeSecurityPolicy#interval_sec}
        '''
        result = self._values.get("interval_sec")
        assert result is not None, "Required property 'interval_sec' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSecInput")
    def interval_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="intervalSec")
    def interval_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSec"))

    @interval_sec.setter
    def interval_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference, "interval_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRedirectOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "target": "target"},
)
class ComputeSecurityPolicyRuleRedirectOptions:
    def __init__(
        self,
        *,
        type: builtins.str,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of the redirect action. Available options: EXTERNAL_302: Must specify the corresponding target field in config. GOOGLE_RECAPTCHA: Cannot specify target field in config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        :param target: Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRedirectOptions.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the redirect action.

        Available options: EXTERNAL_302: Must specify the corresponding target field in config. GOOGLE_RECAPTCHA: Cannot specify target field in config.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#type ComputeSecurityPolicy#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#target ComputeSecurityPolicy#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyRuleRedirectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyRuleRedirectOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyRuleRedirectOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyRuleRedirectOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRedirectOptionsOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRedirectOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComputeSecurityPolicyRuleRedirectOptions]:
        return typing.cast(typing.Optional[ComputeSecurityPolicyRuleRedirectOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeSecurityPolicyRuleRedirectOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyRuleRedirectOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeSecurityPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#create ComputeSecurityPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#delete ComputeSecurityPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#update ComputeSecurityPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeSecurityPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#create ComputeSecurityPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#delete ComputeSecurityPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/compute_security_policy#update ComputeSecurityPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeSecurityPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.computeSecurityPolicy.ComputeSecurityPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeSecurityPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeSecurityPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeSecurityPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeSecurityPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeSecurityPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeSecurityPolicy",
    "ComputeSecurityPolicyAdaptiveProtectionConfig",
    "ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig",
    "ComputeSecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigOutputReference",
    "ComputeSecurityPolicyAdaptiveProtectionConfigOutputReference",
    "ComputeSecurityPolicyAdvancedOptionsConfig",
    "ComputeSecurityPolicyAdvancedOptionsConfigOutputReference",
    "ComputeSecurityPolicyConfig",
    "ComputeSecurityPolicyRule",
    "ComputeSecurityPolicyRuleList",
    "ComputeSecurityPolicyRuleMatch",
    "ComputeSecurityPolicyRuleMatchConfig",
    "ComputeSecurityPolicyRuleMatchConfigOutputReference",
    "ComputeSecurityPolicyRuleMatchExpr",
    "ComputeSecurityPolicyRuleMatchExprOutputReference",
    "ComputeSecurityPolicyRuleMatchOutputReference",
    "ComputeSecurityPolicyRuleOutputReference",
    "ComputeSecurityPolicyRuleRateLimitOptions",
    "ComputeSecurityPolicyRuleRateLimitOptionsBanThreshold",
    "ComputeSecurityPolicyRuleRateLimitOptionsBanThresholdOutputReference",
    "ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptions",
    "ComputeSecurityPolicyRuleRateLimitOptionsExceedRedirectOptionsOutputReference",
    "ComputeSecurityPolicyRuleRateLimitOptionsOutputReference",
    "ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThreshold",
    "ComputeSecurityPolicyRuleRateLimitOptionsRateLimitThresholdOutputReference",
    "ComputeSecurityPolicyRuleRedirectOptions",
    "ComputeSecurityPolicyRuleRedirectOptionsOutputReference",
    "ComputeSecurityPolicyTimeouts",
    "ComputeSecurityPolicyTimeoutsOutputReference",
]

publication.publish()
