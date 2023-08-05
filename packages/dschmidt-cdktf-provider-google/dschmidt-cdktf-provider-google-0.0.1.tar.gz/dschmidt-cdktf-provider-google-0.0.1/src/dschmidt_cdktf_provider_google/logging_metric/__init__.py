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


class LoggingMetric(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetric",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/logging_metric google_logging_metric}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: builtins.str,
        metric_descriptor: typing.Union["LoggingMetricMetricDescriptor", typing.Dict[str, typing.Any]],
        name: builtins.str,
        bucket_options: typing.Optional[typing.Union["LoggingMetricBucketOptions", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LoggingMetricTimeouts", typing.Dict[str, typing.Any]]] = None,
        value_extractor: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/logging_metric google_logging_metric} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log entries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#filter LoggingMetric#filter}
        :param metric_descriptor: metric_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_descriptor LoggingMetric#metric_descriptor}
        :param name: The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100 characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#name LoggingMetric#name}
        :param bucket_options: bucket_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bucket_options LoggingMetric#bucket_options}
        :param description: A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#description LoggingMetric#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#id LoggingMetric#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param label_extractors: A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the valueExtractor field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#label_extractors LoggingMetric#label_extractors}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#project LoggingMetric#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#timeouts LoggingMetric#timeouts}
        :param value_extractor: A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_extractor LoggingMetric#value_extractor}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetric.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoggingMetricConfig(
            filter=filter,
            metric_descriptor=metric_descriptor,
            name=name,
            bucket_options=bucket_options,
            description=description,
            id=id,
            label_extractors=label_extractors,
            project=project,
            timeouts=timeouts,
            value_extractor=value_extractor,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBucketOptions")
    def put_bucket_options(
        self,
        *,
        explicit_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsExplicitBuckets", typing.Dict[str, typing.Any]]] = None,
        exponential_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsExponentialBuckets", typing.Dict[str, typing.Any]]] = None,
        linear_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsLinearBuckets", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param explicit_buckets: explicit_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#explicit_buckets LoggingMetric#explicit_buckets}
        :param exponential_buckets: exponential_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#exponential_buckets LoggingMetric#exponential_buckets}
        :param linear_buckets: linear_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#linear_buckets LoggingMetric#linear_buckets}
        '''
        value = LoggingMetricBucketOptions(
            explicit_buckets=explicit_buckets,
            exponential_buckets=exponential_buckets,
            linear_buckets=linear_buckets,
        )

        return typing.cast(None, jsii.invoke(self, "putBucketOptions", [value]))

    @jsii.member(jsii_name="putMetricDescriptor")
    def put_metric_descriptor(
        self,
        *,
        metric_kind: builtins.str,
        value_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoggingMetricMetricDescriptorLabels", typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_kind: Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metricKind and valueType might not be supported. For counter metrics, set this to DELTA. Possible values: ["DELTA", "GAUGE", "CUMULATIVE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_kind LoggingMetric#metric_kind}
        :param value_type: Whether the measurement is an integer, a floating-point number, etc. Some combinations of metricKind and valueType might not be supported. For counter metrics, set this to INT64. Possible values: ["BOOL", "INT64", "DOUBLE", "STRING", "DISTRIBUTION", "MONEY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_type LoggingMetric#value_type}
        :param display_name: A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#display_name LoggingMetric#display_name}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#labels LoggingMetric#labels}
        :param unit: The unit in which the metric value is reported. It is only applicable if the valueType is 'INT64', 'DOUBLE', or 'DISTRIBUTION'. The supported units are a subset of `The Unified Code for Units of Measure <http://unitsofmeasure.org/ucum.html>`_ standard Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#unit LoggingMetric#unit}
        '''
        value = LoggingMetricMetricDescriptor(
            metric_kind=metric_kind,
            value_type=value_type,
            display_name=display_name,
            labels=labels,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putMetricDescriptor", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#create LoggingMetric#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#delete LoggingMetric#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#update LoggingMetric#update}.
        '''
        value = LoggingMetricTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBucketOptions")
    def reset_bucket_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabelExtractors")
    def reset_label_extractors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelExtractors", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetValueExtractor")
    def reset_value_extractor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueExtractor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bucketOptions")
    def bucket_options(self) -> "LoggingMetricBucketOptionsOutputReference":
        return typing.cast("LoggingMetricBucketOptionsOutputReference", jsii.get(self, "bucketOptions"))

    @builtins.property
    @jsii.member(jsii_name="metricDescriptor")
    def metric_descriptor(self) -> "LoggingMetricMetricDescriptorOutputReference":
        return typing.cast("LoggingMetricMetricDescriptorOutputReference", jsii.get(self, "metricDescriptor"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LoggingMetricTimeoutsOutputReference":
        return typing.cast("LoggingMetricTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bucketOptionsInput")
    def bucket_options_input(self) -> typing.Optional["LoggingMetricBucketOptions"]:
        return typing.cast(typing.Optional["LoggingMetricBucketOptions"], jsii.get(self, "bucketOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelExtractorsInput")
    def label_extractors_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelExtractorsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricDescriptorInput")
    def metric_descriptor_input(
        self,
    ) -> typing.Optional["LoggingMetricMetricDescriptor"]:
        return typing.cast(typing.Optional["LoggingMetricMetricDescriptor"], jsii.get(self, "metricDescriptorInput"))

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
    ) -> typing.Optional[typing.Union["LoggingMetricTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LoggingMetricTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueExtractorInput")
    def value_extractor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueExtractorInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labelExtractors")
    def label_extractors(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelExtractors"))

    @label_extractors.setter
    def label_extractors(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "label_extractors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelExtractors", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="valueExtractor")
    def value_extractor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueExtractor"))

    @value_extractor.setter
    def value_extractor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetric, "value_extractor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueExtractor", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptions",
    jsii_struct_bases=[],
    name_mapping={
        "explicit_buckets": "explicitBuckets",
        "exponential_buckets": "exponentialBuckets",
        "linear_buckets": "linearBuckets",
    },
)
class LoggingMetricBucketOptions:
    def __init__(
        self,
        *,
        explicit_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsExplicitBuckets", typing.Dict[str, typing.Any]]] = None,
        exponential_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsExponentialBuckets", typing.Dict[str, typing.Any]]] = None,
        linear_buckets: typing.Optional[typing.Union["LoggingMetricBucketOptionsLinearBuckets", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param explicit_buckets: explicit_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#explicit_buckets LoggingMetric#explicit_buckets}
        :param exponential_buckets: exponential_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#exponential_buckets LoggingMetric#exponential_buckets}
        :param linear_buckets: linear_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#linear_buckets LoggingMetric#linear_buckets}
        '''
        if isinstance(explicit_buckets, dict):
            explicit_buckets = LoggingMetricBucketOptionsExplicitBuckets(**explicit_buckets)
        if isinstance(exponential_buckets, dict):
            exponential_buckets = LoggingMetricBucketOptionsExponentialBuckets(**exponential_buckets)
        if isinstance(linear_buckets, dict):
            linear_buckets = LoggingMetricBucketOptionsLinearBuckets(**linear_buckets)
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricBucketOptions.__init__)
            check_type(argname="argument explicit_buckets", value=explicit_buckets, expected_type=type_hints["explicit_buckets"])
            check_type(argname="argument exponential_buckets", value=exponential_buckets, expected_type=type_hints["exponential_buckets"])
            check_type(argname="argument linear_buckets", value=linear_buckets, expected_type=type_hints["linear_buckets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if explicit_buckets is not None:
            self._values["explicit_buckets"] = explicit_buckets
        if exponential_buckets is not None:
            self._values["exponential_buckets"] = exponential_buckets
        if linear_buckets is not None:
            self._values["linear_buckets"] = linear_buckets

    @builtins.property
    def explicit_buckets(
        self,
    ) -> typing.Optional["LoggingMetricBucketOptionsExplicitBuckets"]:
        '''explicit_buckets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#explicit_buckets LoggingMetric#explicit_buckets}
        '''
        result = self._values.get("explicit_buckets")
        return typing.cast(typing.Optional["LoggingMetricBucketOptionsExplicitBuckets"], result)

    @builtins.property
    def exponential_buckets(
        self,
    ) -> typing.Optional["LoggingMetricBucketOptionsExponentialBuckets"]:
        '''exponential_buckets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#exponential_buckets LoggingMetric#exponential_buckets}
        '''
        result = self._values.get("exponential_buckets")
        return typing.cast(typing.Optional["LoggingMetricBucketOptionsExponentialBuckets"], result)

    @builtins.property
    def linear_buckets(
        self,
    ) -> typing.Optional["LoggingMetricBucketOptionsLinearBuckets"]:
        '''linear_buckets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#linear_buckets LoggingMetric#linear_buckets}
        '''
        result = self._values.get("linear_buckets")
        return typing.cast(typing.Optional["LoggingMetricBucketOptionsLinearBuckets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricBucketOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsExplicitBuckets",
    jsii_struct_bases=[],
    name_mapping={"bounds": "bounds"},
)
class LoggingMetricBucketOptionsExplicitBuckets:
    def __init__(self, *, bounds: typing.Sequence[jsii.Number]) -> None:
        '''
        :param bounds: The values must be monotonically increasing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bounds LoggingMetric#bounds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsExplicitBuckets.__init__)
            check_type(argname="argument bounds", value=bounds, expected_type=type_hints["bounds"])
        self._values: typing.Dict[str, typing.Any] = {
            "bounds": bounds,
        }

    @builtins.property
    def bounds(self) -> typing.List[jsii.Number]:
        '''The values must be monotonically increasing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bounds LoggingMetric#bounds}
        '''
        result = self._values.get("bounds")
        assert result is not None, "Required property 'bounds' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricBucketOptionsExplicitBuckets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoggingMetricBucketOptionsExplicitBucketsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsExplicitBucketsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsExplicitBucketsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="boundsInput")
    def bounds_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "boundsInput"))

    @builtins.property
    @jsii.member(jsii_name="bounds")
    def bounds(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "bounds"))

    @bounds.setter
    def bounds(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExplicitBucketsOutputReference, "bounds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bounds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsExplicitBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsExplicitBuckets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoggingMetricBucketOptionsExplicitBuckets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExplicitBucketsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsExponentialBuckets",
    jsii_struct_bases=[],
    name_mapping={
        "growth_factor": "growthFactor",
        "num_finite_buckets": "numFiniteBuckets",
        "scale": "scale",
    },
)
class LoggingMetricBucketOptionsExponentialBuckets:
    def __init__(
        self,
        *,
        growth_factor: typing.Optional[jsii.Number] = None,
        num_finite_buckets: typing.Optional[jsii.Number] = None,
        scale: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param growth_factor: Must be greater than 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#growth_factor LoggingMetric#growth_factor}
        :param num_finite_buckets: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        :param scale: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#scale LoggingMetric#scale}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsExponentialBuckets.__init__)
            check_type(argname="argument growth_factor", value=growth_factor, expected_type=type_hints["growth_factor"])
            check_type(argname="argument num_finite_buckets", value=num_finite_buckets, expected_type=type_hints["num_finite_buckets"])
            check_type(argname="argument scale", value=scale, expected_type=type_hints["scale"])
        self._values: typing.Dict[str, typing.Any] = {}
        if growth_factor is not None:
            self._values["growth_factor"] = growth_factor
        if num_finite_buckets is not None:
            self._values["num_finite_buckets"] = num_finite_buckets
        if scale is not None:
            self._values["scale"] = scale

    @builtins.property
    def growth_factor(self) -> typing.Optional[jsii.Number]:
        '''Must be greater than 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#growth_factor LoggingMetric#growth_factor}
        '''
        result = self._values.get("growth_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_finite_buckets(self) -> typing.Optional[jsii.Number]:
        '''Must be greater than 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        '''
        result = self._values.get("num_finite_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale(self) -> typing.Optional[jsii.Number]:
        '''Must be greater than 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#scale LoggingMetric#scale}
        '''
        result = self._values.get("scale")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricBucketOptionsExponentialBuckets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoggingMetricBucketOptionsExponentialBucketsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsExponentialBucketsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsExponentialBucketsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGrowthFactor")
    def reset_growth_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrowthFactor", []))

    @jsii.member(jsii_name="resetNumFiniteBuckets")
    def reset_num_finite_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumFiniteBuckets", []))

    @jsii.member(jsii_name="resetScale")
    def reset_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScale", []))

    @builtins.property
    @jsii.member(jsii_name="growthFactorInput")
    def growth_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "growthFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="numFiniteBucketsInput")
    def num_finite_buckets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numFiniteBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInput")
    def scale_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleInput"))

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "growthFactor"))

    @growth_factor.setter
    def growth_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExponentialBucketsOutputReference, "growth_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "growthFactor", value)

    @builtins.property
    @jsii.member(jsii_name="numFiniteBuckets")
    def num_finite_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numFiniteBuckets"))

    @num_finite_buckets.setter
    def num_finite_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExponentialBucketsOutputReference, "num_finite_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numFiniteBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @scale.setter
    def scale(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExponentialBucketsOutputReference, "scale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scale", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsExponentialBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsExponentialBuckets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoggingMetricBucketOptionsExponentialBuckets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsExponentialBucketsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsLinearBuckets",
    jsii_struct_bases=[],
    name_mapping={
        "num_finite_buckets": "numFiniteBuckets",
        "offset": "offset",
        "width": "width",
    },
)
class LoggingMetricBucketOptionsLinearBuckets:
    def __init__(
        self,
        *,
        num_finite_buckets: typing.Optional[jsii.Number] = None,
        offset: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_finite_buckets: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        :param offset: Lower bound of the first bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#offset LoggingMetric#offset}
        :param width: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#width LoggingMetric#width}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsLinearBuckets.__init__)
            check_type(argname="argument num_finite_buckets", value=num_finite_buckets, expected_type=type_hints["num_finite_buckets"])
            check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {}
        if num_finite_buckets is not None:
            self._values["num_finite_buckets"] = num_finite_buckets
        if offset is not None:
            self._values["offset"] = offset
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def num_finite_buckets(self) -> typing.Optional[jsii.Number]:
        '''Must be greater than 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        '''
        result = self._values.get("num_finite_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset(self) -> typing.Optional[jsii.Number]:
        '''Lower bound of the first bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#offset LoggingMetric#offset}
        '''
        result = self._values.get("offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Must be greater than 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#width LoggingMetric#width}
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricBucketOptionsLinearBuckets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoggingMetricBucketOptionsLinearBucketsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsLinearBucketsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsLinearBucketsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNumFiniteBuckets")
    def reset_num_finite_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumFiniteBuckets", []))

    @jsii.member(jsii_name="resetOffset")
    def reset_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffset", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="numFiniteBucketsInput")
    def num_finite_buckets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numFiniteBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetInput")
    def offset_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="numFiniteBuckets")
    def num_finite_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numFiniteBuckets"))

    @num_finite_buckets.setter
    def num_finite_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsLinearBucketsOutputReference, "num_finite_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numFiniteBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="offset")
    def offset(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offset"))

    @offset.setter
    def offset(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsLinearBucketsOutputReference, "offset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offset", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsLinearBucketsOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsLinearBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsLinearBuckets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoggingMetricBucketOptionsLinearBuckets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsLinearBucketsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoggingMetricBucketOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricBucketOptionsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricBucketOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExplicitBuckets")
    def put_explicit_buckets(self, *, bounds: typing.Sequence[jsii.Number]) -> None:
        '''
        :param bounds: The values must be monotonically increasing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bounds LoggingMetric#bounds}
        '''
        value = LoggingMetricBucketOptionsExplicitBuckets(bounds=bounds)

        return typing.cast(None, jsii.invoke(self, "putExplicitBuckets", [value]))

    @jsii.member(jsii_name="putExponentialBuckets")
    def put_exponential_buckets(
        self,
        *,
        growth_factor: typing.Optional[jsii.Number] = None,
        num_finite_buckets: typing.Optional[jsii.Number] = None,
        scale: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param growth_factor: Must be greater than 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#growth_factor LoggingMetric#growth_factor}
        :param num_finite_buckets: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        :param scale: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#scale LoggingMetric#scale}
        '''
        value = LoggingMetricBucketOptionsExponentialBuckets(
            growth_factor=growth_factor,
            num_finite_buckets=num_finite_buckets,
            scale=scale,
        )

        return typing.cast(None, jsii.invoke(self, "putExponentialBuckets", [value]))

    @jsii.member(jsii_name="putLinearBuckets")
    def put_linear_buckets(
        self,
        *,
        num_finite_buckets: typing.Optional[jsii.Number] = None,
        offset: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_finite_buckets: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#num_finite_buckets LoggingMetric#num_finite_buckets}
        :param offset: Lower bound of the first bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#offset LoggingMetric#offset}
        :param width: Must be greater than 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#width LoggingMetric#width}
        '''
        value = LoggingMetricBucketOptionsLinearBuckets(
            num_finite_buckets=num_finite_buckets, offset=offset, width=width
        )

        return typing.cast(None, jsii.invoke(self, "putLinearBuckets", [value]))

    @jsii.member(jsii_name="resetExplicitBuckets")
    def reset_explicit_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExplicitBuckets", []))

    @jsii.member(jsii_name="resetExponentialBuckets")
    def reset_exponential_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExponentialBuckets", []))

    @jsii.member(jsii_name="resetLinearBuckets")
    def reset_linear_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinearBuckets", []))

    @builtins.property
    @jsii.member(jsii_name="explicitBuckets")
    def explicit_buckets(
        self,
    ) -> LoggingMetricBucketOptionsExplicitBucketsOutputReference:
        return typing.cast(LoggingMetricBucketOptionsExplicitBucketsOutputReference, jsii.get(self, "explicitBuckets"))

    @builtins.property
    @jsii.member(jsii_name="exponentialBuckets")
    def exponential_buckets(
        self,
    ) -> LoggingMetricBucketOptionsExponentialBucketsOutputReference:
        return typing.cast(LoggingMetricBucketOptionsExponentialBucketsOutputReference, jsii.get(self, "exponentialBuckets"))

    @builtins.property
    @jsii.member(jsii_name="linearBuckets")
    def linear_buckets(self) -> LoggingMetricBucketOptionsLinearBucketsOutputReference:
        return typing.cast(LoggingMetricBucketOptionsLinearBucketsOutputReference, jsii.get(self, "linearBuckets"))

    @builtins.property
    @jsii.member(jsii_name="explicitBucketsInput")
    def explicit_buckets_input(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsExplicitBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsExplicitBuckets], jsii.get(self, "explicitBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="exponentialBucketsInput")
    def exponential_buckets_input(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsExponentialBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsExponentialBuckets], jsii.get(self, "exponentialBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="linearBucketsInput")
    def linear_buckets_input(
        self,
    ) -> typing.Optional[LoggingMetricBucketOptionsLinearBuckets]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptionsLinearBuckets], jsii.get(self, "linearBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoggingMetricBucketOptions]:
        return typing.cast(typing.Optional[LoggingMetricBucketOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoggingMetricBucketOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricBucketOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "metric_descriptor": "metricDescriptor",
        "name": "name",
        "bucket_options": "bucketOptions",
        "description": "description",
        "id": "id",
        "label_extractors": "labelExtractors",
        "project": "project",
        "timeouts": "timeouts",
        "value_extractor": "valueExtractor",
    },
)
class LoggingMetricConfig(cdktf.TerraformMetaArguments):
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
        filter: builtins.str,
        metric_descriptor: typing.Union["LoggingMetricMetricDescriptor", typing.Dict[str, typing.Any]],
        name: builtins.str,
        bucket_options: typing.Optional[typing.Union[LoggingMetricBucketOptions, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LoggingMetricTimeouts", typing.Dict[str, typing.Any]]] = None,
        value_extractor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log entries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#filter LoggingMetric#filter}
        :param metric_descriptor: metric_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_descriptor LoggingMetric#metric_descriptor}
        :param name: The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100 characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#name LoggingMetric#name}
        :param bucket_options: bucket_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bucket_options LoggingMetric#bucket_options}
        :param description: A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#description LoggingMetric#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#id LoggingMetric#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param label_extractors: A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the valueExtractor field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#label_extractors LoggingMetric#label_extractors}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#project LoggingMetric#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#timeouts LoggingMetric#timeouts}
        :param value_extractor: A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_extractor LoggingMetric#value_extractor}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metric_descriptor, dict):
            metric_descriptor = LoggingMetricMetricDescriptor(**metric_descriptor)
        if isinstance(bucket_options, dict):
            bucket_options = LoggingMetricBucketOptions(**bucket_options)
        if isinstance(timeouts, dict):
            timeouts = LoggingMetricTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument metric_descriptor", value=metric_descriptor, expected_type=type_hints["metric_descriptor"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument bucket_options", value=bucket_options, expected_type=type_hints["bucket_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument label_extractors", value=label_extractors, expected_type=type_hints["label_extractors"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument value_extractor", value=value_extractor, expected_type=type_hints["value_extractor"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "metric_descriptor": metric_descriptor,
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
        if bucket_options is not None:
            self._values["bucket_options"] = bucket_options
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if label_extractors is not None:
            self._values["label_extractors"] = label_extractors
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if value_extractor is not None:
            self._values["value_extractor"] = value_extractor

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
    def filter(self) -> builtins.str:
        '''An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log entries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#filter LoggingMetric#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_descriptor(self) -> "LoggingMetricMetricDescriptor":
        '''metric_descriptor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_descriptor LoggingMetric#metric_descriptor}
        '''
        result = self._values.get("metric_descriptor")
        assert result is not None, "Required property 'metric_descriptor' is missing"
        return typing.cast("LoggingMetricMetricDescriptor", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The client-assigned metric identifier.

        Examples - "error_count", "nginx/requests".
        Metric identifiers are limited to 100 characters and can include only the following
        characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash
        character (/) denotes a hierarchy of name pieces, and it cannot be the first character
        of the name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#name LoggingMetric#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_options(self) -> typing.Optional[LoggingMetricBucketOptions]:
        '''bucket_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#bucket_options LoggingMetric#bucket_options}
        '''
        result = self._values.get("bucket_options")
        return typing.cast(typing.Optional[LoggingMetricBucketOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#description LoggingMetric#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#id LoggingMetric#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_extractors(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value.

        Each label key specified in the LabelDescriptor must
        have an associated extractor expression in this map. The syntax of the extractor expression is
        the same as for the valueExtractor field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#label_extractors LoggingMetric#label_extractors}
        '''
        result = self._values.get("label_extractors")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#project LoggingMetric#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LoggingMetricTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#timeouts LoggingMetric#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LoggingMetricTimeouts"], result)

    @builtins.property
    def value_extractor(self) -> typing.Optional[builtins.str]:
        '''A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log entry.

        Two functions are supported for value extraction - EXTRACT(field) or
        REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which
        the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax
        (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified
        log entry field. The value of the field is converted to a string before applying the regex. It is an
        error to specify a regex that does not include exactly one capture group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_extractor LoggingMetric#value_extractor}
        '''
        result = self._values.get("value_extractor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricMetricDescriptor",
    jsii_struct_bases=[],
    name_mapping={
        "metric_kind": "metricKind",
        "value_type": "valueType",
        "display_name": "displayName",
        "labels": "labels",
        "unit": "unit",
    },
)
class LoggingMetricMetricDescriptor:
    def __init__(
        self,
        *,
        metric_kind: builtins.str,
        value_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoggingMetricMetricDescriptorLabels", typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_kind: Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metricKind and valueType might not be supported. For counter metrics, set this to DELTA. Possible values: ["DELTA", "GAUGE", "CUMULATIVE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_kind LoggingMetric#metric_kind}
        :param value_type: Whether the measurement is an integer, a floating-point number, etc. Some combinations of metricKind and valueType might not be supported. For counter metrics, set this to INT64. Possible values: ["BOOL", "INT64", "DOUBLE", "STRING", "DISTRIBUTION", "MONEY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_type LoggingMetric#value_type}
        :param display_name: A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#display_name LoggingMetric#display_name}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#labels LoggingMetric#labels}
        :param unit: The unit in which the metric value is reported. It is only applicable if the valueType is 'INT64', 'DOUBLE', or 'DISTRIBUTION'. The supported units are a subset of `The Unified Code for Units of Measure <http://unitsofmeasure.org/ucum.html>`_ standard Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#unit LoggingMetric#unit}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptor.__init__)
            check_type(argname="argument metric_kind", value=metric_kind, expected_type=type_hints["metric_kind"])
            check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_kind": metric_kind,
            "value_type": value_type,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if labels is not None:
            self._values["labels"] = labels
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_kind(self) -> builtins.str:
        '''Whether the metric records instantaneous values, changes to a value, etc.

        Some combinations of metricKind and valueType might not be supported.
        For counter metrics, set this to DELTA. Possible values: ["DELTA", "GAUGE", "CUMULATIVE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#metric_kind LoggingMetric#metric_kind}
        '''
        result = self._values.get("metric_kind")
        assert result is not None, "Required property 'metric_kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_type(self) -> builtins.str:
        '''Whether the measurement is an integer, a floating-point number, etc.

        Some combinations of metricKind and valueType might not be supported.
        For counter metrics, set this to INT64. Possible values: ["BOOL", "INT64", "DOUBLE", "STRING", "DISTRIBUTION", "MONEY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_type LoggingMetric#value_type}
        '''
        result = self._values.get("value_type")
        assert result is not None, "Required property 'value_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A concise name for the metric, which can be displayed in user interfaces.

        Use sentence case
        without an ending period, for example "Request count". This field is optional but it is
        recommended to be set for any metrics associated with user-visible concepts, such as Quota.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#display_name LoggingMetric#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoggingMetricMetricDescriptorLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#labels LoggingMetric#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoggingMetricMetricDescriptorLabels"]]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''The unit in which the metric value is reported.

        It is only applicable if the valueType is
        'INT64', 'DOUBLE', or 'DISTRIBUTION'. The supported units are a subset of
        `The Unified Code for Units of Measure <http://unitsofmeasure.org/ucum.html>`_ standard

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#unit LoggingMetric#unit}
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricMetricDescriptor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricMetricDescriptorLabels",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "description": "description",
        "value_type": "valueType",
    },
)
class LoggingMetricMetricDescriptorLabels:
    def __init__(
        self,
        *,
        key: builtins.str,
        description: typing.Optional[builtins.str] = None,
        value_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The label key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#key LoggingMetric#key}
        :param description: A human-readable description for the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#description LoggingMetric#description}
        :param value_type: The type of data that can be assigned to the label. Default value: "STRING" Possible values: ["BOOL", "INT64", "STRING"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_type LoggingMetric#value_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorLabels.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }
        if description is not None:
            self._values["description"] = description
        if value_type is not None:
            self._values["value_type"] = value_type

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#key LoggingMetric#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#description LoggingMetric#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_type(self) -> typing.Optional[builtins.str]:
        '''The type of data that can be assigned to the label. Default value: "STRING" Possible values: ["BOOL", "INT64", "STRING"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#value_type LoggingMetric#value_type}
        '''
        result = self._values.get("value_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricMetricDescriptorLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoggingMetricMetricDescriptorLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricMetricDescriptorLabelsList",
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
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoggingMetricMetricDescriptorLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoggingMetricMetricDescriptorLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoggingMetricMetricDescriptorLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoggingMetricMetricDescriptorLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoggingMetricMetricDescriptorLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoggingMetricMetricDescriptorLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricMetricDescriptorLabelsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetValueType")
    def reset_value_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueType", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueTypeInput")
    def value_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="valueType")
    def value_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueType"))

    @value_type.setter
    def value_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsOutputReference, "value_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoggingMetricMetricDescriptorLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoggingMetricMetricDescriptorLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoggingMetricMetricDescriptorLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoggingMetricMetricDescriptorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricMetricDescriptorOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoggingMetricMetricDescriptorLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricMetricDescriptorOutputReference.put_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> LoggingMetricMetricDescriptorLabelsList:
        return typing.cast(LoggingMetricMetricDescriptorLabelsList, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoggingMetricMetricDescriptorLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoggingMetricMetricDescriptorLabels]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricKindInput")
    def metric_kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricKindInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueTypeInput")
    def value_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="metricKind")
    def metric_kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricKind"))

    @metric_kind.setter
    def metric_kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorOutputReference, "metric_kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricKind", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="valueType")
    def value_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueType"))

    @value_type.setter
    def value_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorOutputReference, "value_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoggingMetricMetricDescriptor]:
        return typing.cast(typing.Optional[LoggingMetricMetricDescriptor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoggingMetricMetricDescriptor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricMetricDescriptorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LoggingMetricTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#create LoggingMetric#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#delete LoggingMetric#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#update LoggingMetric#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoggingMetricTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#create LoggingMetric#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#delete LoggingMetric#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/logging_metric#update LoggingMetric#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingMetricTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoggingMetricTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@dschmidt/provider-google.loggingMetric.LoggingMetricTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LoggingMetricTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LoggingMetricTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoggingMetricTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoggingMetricTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoggingMetricTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoggingMetricTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LoggingMetric",
    "LoggingMetricBucketOptions",
    "LoggingMetricBucketOptionsExplicitBuckets",
    "LoggingMetricBucketOptionsExplicitBucketsOutputReference",
    "LoggingMetricBucketOptionsExponentialBuckets",
    "LoggingMetricBucketOptionsExponentialBucketsOutputReference",
    "LoggingMetricBucketOptionsLinearBuckets",
    "LoggingMetricBucketOptionsLinearBucketsOutputReference",
    "LoggingMetricBucketOptionsOutputReference",
    "LoggingMetricConfig",
    "LoggingMetricMetricDescriptor",
    "LoggingMetricMetricDescriptorLabels",
    "LoggingMetricMetricDescriptorLabelsList",
    "LoggingMetricMetricDescriptorLabelsOutputReference",
    "LoggingMetricMetricDescriptorOutputReference",
    "LoggingMetricTimeouts",
    "LoggingMetricTimeoutsOutputReference",
]

publication.publish()
