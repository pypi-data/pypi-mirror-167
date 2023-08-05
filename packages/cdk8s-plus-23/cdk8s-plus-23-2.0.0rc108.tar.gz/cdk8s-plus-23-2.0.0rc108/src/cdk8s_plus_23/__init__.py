'''
# cdk8s+ (cdk8s-plus)

### High level constructs for Kubernetes

![Stability:Beta](https://img.shields.io/badge/stability-beta-orange)
[![cdk8s-plus-22](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.22?label=cdk8s-plus-22&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.22.yml)
[![cdk8s-plus-23](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.23?label=cdk8s-plus-23&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.23.yml)
[![cdk8s-plus-24](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.24?label=cdk8s-plus-24&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.24.yml)

| k8s version | npm (JS/TS) | PyPI (Python) | Maven (Java) | Go |
| --- | --- | --- | --- | --- |
| 1.22.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-22) | [Link](https://pypi.org/project/cdk8s-plus-22/) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-22) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.22) |
| 1.23.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-23) | [Link](https://pypi.org/project/cdk8s-plus-23/) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-23) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.23) |
| 1.24.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-24) | [Link](https://pypi.org/project/cdk8s-plus-24/) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-24) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.24) |

**cdk8s+** is a software development framework that provides high level
abstractions for authoring Kubernetes applications. Built on top of the auto
generated building blocks provided by [cdk8s](../cdk8s), this library includes a
hand crafted *construct* for each native kubernetes object, exposing richer
API's with reduced complexity.

## :books: Documentation

See [cdk8s.io](https://cdk8s.io/docs/latest/plus).

## :raised_hand: Contributing

If you'd like to add a new feature or fix a bug, please visit
[CONTRIBUTING.md](CONTRIBUTING.md)!

## :balance_scale: License

This project is distributed under the [Apache License, Version 2.0](./LICENSE).

This module is part of the [cdk8s project](https://github.com/cdk8s-team).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import cdk8s
import constructs


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AddDirectoryOptions",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "key_prefix": "keyPrefix"},
)
class AddDirectoryOptions:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ``configmap.addDirectory()``.

        :param exclude: Glob patterns to exclude when adding files. Default: - include all files
        :param key_prefix: A prefix to add to all keys in the config map. Default: ""
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddDirectoryOptions.__init__)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if key_prefix is not None:
            self._values["key_prefix"] = key_prefix

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude when adding files.

        :default: - include all files
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix to add to all keys in the config map.

        :default: ""
        '''
        result = self._values.get("key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddDirectoryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ApiResourceOptions",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "resource_type": "resourceType"},
)
class ApiResourceOptions:
    def __init__(self, *, api_group: builtins.str, resource_type: builtins.str) -> None:
        '''Options for ``ApiResource``.

        :param api_group: The group portion of the API version (e.g. ``authorization.k8s.io``).
        :param resource_type: The name of the resource type as it appears in the relevant API endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiResourceOptions.__init__)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_group": api_group,
            "resource_type": resource_type,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. ``authorization.k8s.io``).'''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The name of the resource type as it appears in the relevant API endpoint.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources

        Example::

            - "pods" or "pods/log"
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AwsElasticBlockStoreVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "fs_type": "fsType",
        "name": "name",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class AwsElasticBlockStoreVolumeOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromAwsElasticBlockStore``.

        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsElasticBlockStoreVolumeOptions.__init__)
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if name is not None:
            self._values["name"] = name
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsElasticBlockStoreVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.AzureDiskPersistentVolumeCachingMode")
class AzureDiskPersistentVolumeCachingMode(enum.Enum):
    '''Azure disk caching modes.'''

    NONE = "NONE"
    '''None.'''
    READ_ONLY = "READ_ONLY"
    '''ReadOnly.'''
    READ_WRITE = "READ_WRITE"
    '''ReadWrite.'''


@jsii.enum(jsii_type="cdk8s-plus-23.AzureDiskPersistentVolumeKind")
class AzureDiskPersistentVolumeKind(enum.Enum):
    '''Azure Disk kinds.'''

    SHARED = "SHARED"
    '''Multiple blob disks per storage account.'''
    DEDICATED = "DEDICATED"
    '''Single blob disk per storage account.'''
    MANAGED = "MANAGED"
    '''Azure managed data disk.'''


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AzureDiskVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "fs_type": "fsType",
        "kind": "kind",
        "name": "name",
        "read_only": "readOnly",
    },
)
class AzureDiskVolumeOptions:
    def __init__(
        self,
        *,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromAzureDisk``.

        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param name: The volume name. Default: - auto-generated
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzureDiskVolumeOptions.__init__)
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {}
        if caching_mode is not None:
            self._values["caching_mode"] = caching_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> typing.Optional[AzureDiskPersistentVolumeCachingMode]:
        '''Host Caching mode.

        :default: - AzureDiskPersistentVolumeCachingMode.NONE.
        '''
        result = self._values.get("caching_mode")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeCachingMode], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system.

        :default: 'ext4'
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[AzureDiskPersistentVolumeKind]:
        '''Kind of disk.

        :default: AzureDiskPersistentVolumeKind.SHARED
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeKind], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureDiskVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ClusterRolePolicyRule",
    jsii_struct_bases=[],
    name_mapping={"endpoints": "endpoints", "verbs": "verbs"},
)
class ClusterRolePolicyRule:
    def __init__(
        self,
        *,
        endpoints: typing.Sequence["IApiEndpoint"],
        verbs: typing.Sequence[builtins.str],
    ) -> None:
        '''Policy rule of a `ClusterRole.

        :param endpoints: Endpoints this rule applies to. Can be either api resources or non api resources.
        :param verbs: Verbs to allow. (e.g ['get', 'watch'])
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRolePolicyRule.__init__)
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument verbs", value=verbs, expected_type=type_hints["verbs"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints": endpoints,
            "verbs": verbs,
        }

    @builtins.property
    def endpoints(self) -> typing.List["IApiEndpoint"]:
        '''Endpoints this rule applies to.

        Can be either api resources
        or non api resources.
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.List["IApiEndpoint"], result)

    @builtins.property
    def verbs(self) -> typing.List[builtins.str]:
        '''Verbs to allow.

        (e.g ['get', 'watch'])
        '''
        result = self._values.get("verbs")
        assert result is not None, "Required property 'verbs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRolePolicyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ConfigMapVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "default_mode": "defaultMode",
        "items": "items",
        "name": "name",
        "optional": "optional",
    },
)
class ConfigMapVolumeOptions:
    def __init__(
        self,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, typing.Union["PathMapping", typing.Dict[str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the ConfigMap-based volume.

        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the ConfigMap or its keys must be defined. Default: - undocumented
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMapVolumeOptions.__init__)
            check_type(argname="argument default_mode", value=default_mode, expected_type=type_hints["default_mode"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_mode is not None:
            self._values["default_mode"] = default_mode
        if items is not None:
            self._values["items"] = items
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def default_mode(self) -> typing.Optional[jsii.Number]:
        '''Mode bits to use on created files by default.

        Must be a value between 0 and
        0777. Defaults to 0644. Directories within the path are not affected by
        this setting. This might be in conflict with other options that affect the
        file mode, like fsGroup, and the result can be other mode bits set.

        :default:

        644. Directories within the path are not affected by this
        setting. This might be in conflict with other options that affect the file
        mode, like fsGroup, and the result can be other mode bits set.
        '''
        result = self._values.get("default_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def items(self) -> typing.Optional[typing.Mapping[builtins.str, "PathMapping"]]:
        '''If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value.

        If specified, the listed keys will be projected
        into the specified paths, and unlisted keys will not be present. If a key
        is specified which is not present in the ConfigMap, the volume setup will
        error unless it is marked optional. Paths must be relative and may not
        contain the '..' path or start with '..'.

        :default: - no mapping
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "PathMapping"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its keys must be defined.

        :default: - undocumented
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigMapVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.ConnectionScheme")
class ConnectionScheme(enum.Enum):
    HTTP = "HTTP"
    '''Use HTTP request for connecting to host.'''
    HTTPS = "HTTPS"
    '''Use HTTPS request for connecting to host.'''


class Container(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Container"):
    '''A single application container that you want to run within a pod.'''

    def __init__(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env_from: typing.Optional[typing.Sequence["EnvFrom"]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, "EnvValue"]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[typing.Union["ContainerLifecycle", typing.Dict[str, typing.Any]]] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_number: typing.Optional[jsii.Number] = None,
        ports: typing.Optional[typing.Sequence[typing.Union["ContainerPort", typing.Dict[str, typing.Any]]]] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional[typing.Union["ContainerResources", typing.Dict[str, typing.Any]]] = None,
        security_context: typing.Optional[typing.Union["ContainerSecurityContextProps", typing.Dict[str, typing.Any]]] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Union["VolumeMount", typing.Dict[str, typing.Any]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env_from: List of sources to populate environment variables in the container. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by the ``envVariables`` property with a duplicate key will take precedence. Default: - No sources.
        :param env_variables: Environment variables to set in the container. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: 
        :param port_number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. This is a convinience property if all you need a single TCP numbered port. In case more advanced configuartion is required, use the ``ports`` property. This port is added to the list of ports mentioned in the ``ports`` property. Default: - Only the ports mentiond in the ``ports`` property are exposed.
        :param ports: List of ports to expose from this container. Default: - Only the port mentioned in the ``portNumber`` property is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container. Default: cpu: request: 1000 millis limit: 1500 millis memory: request: 512 mebibytes limit: 2048 mebibytes
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - If a port is provided, then knocks on that port to determine when the container is ready for readiness and liveness probe checks. Otherwise, no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        props = ContainerProps(
            image=image,
            args=args,
            command=command,
            env_from=env_from,
            env_variables=env_variables,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            port_number=port_number,
            ports=ports,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addPort")
    def add_port(
        self,
        *,
        number: jsii.Number,
        host_ip: typing.Optional[builtins.str] = None,
        host_port: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional["Protocol"] = None,
    ) -> None:
        '''Add a port to expose from this container.

        :param number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.
        :param host_ip: What host IP to bind the external port to. Default: - 127.0.0.1.
        :param host_port: Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. Most containers do not need this. Default: - auto generated by kubernetes and might change on restarts.
        :param name: If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. Default: - port is not named.
        :param protocol: Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". Default: Protocol.TCP
        '''
        port = ContainerPort(
            number=number,
            host_ip=host_ip,
            host_port=host_port,
            name=name,
            protocol=protocol,
        )

        return typing.cast(None, jsii.invoke(self, "addPort", [port]))

    @jsii.member(jsii_name="mount")
    def mount(
        self,
        path: builtins.str,
        storage: "IStorage",
        *,
        propagation: typing.Optional["MountPropagation"] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Mount a volume to a specific path so that it is accessible by the container.

        Every pod that is configured to use this container will autmoatically have access to the volume.

        :param path: - The desired path in the container.
        :param storage: - The storage to mount.
        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.mount)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
        options = MountOptions(
            propagation=propagation,
            read_only=read_only,
            sub_path=sub_path,
            sub_path_expr=sub_path_expr,
        )

        return typing.cast(None, jsii.invoke(self, "mount", [path, storage, options]))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> "Env":
        '''The environment of the container.'''
        return typing.cast("Env", jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        '''The container image.'''
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="imagePullPolicy")
    def image_pull_policy(self) -> "ImagePullPolicy":
        '''Image pull policy for this container.'''
        return typing.cast("ImagePullPolicy", jsii.get(self, "imagePullPolicy"))

    @builtins.property
    @jsii.member(jsii_name="mounts")
    def mounts(self) -> typing.List["VolumeMount"]:
        '''Volume mounts configured for this container.'''
        return typing.cast(typing.List["VolumeMount"], jsii.get(self, "mounts"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the container.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List["ContainerPort"]:
        '''Ports exposed by this containers.

        Returns a copy, use ``addPort`` to modify.
        '''
        return typing.cast(typing.List["ContainerPort"], jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> "ContainerSecurityContext":
        '''The security context of the container.'''
        return typing.cast("ContainerSecurityContext", jsii.get(self, "securityContext"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to the entrypoint.

        :return: a copy of the arguments array, cannot be modified.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "args"))

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Entrypoint array (the command to execute when the container starts).

        :return: a copy of the entrypoint array, cannot be modified
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "command"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :deprecated: - use ``portNumber``.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="portNumber")
    def port_number(self) -> typing.Optional[jsii.Number]:
        '''The port number that was configured for this container.

        If undefined, either the container doesn't expose a port, or its
        port configuration is stored in the ``ports`` field.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portNumber"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional["ContainerResources"]:
        '''Compute resources (CPU and memory requests and limits) required by the container.

        :see: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
        '''
        return typing.cast(typing.Optional["ContainerResources"], jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="workingDir")
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''The working directory inside the container.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDir"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ContainerLifecycle",
    jsii_struct_bases=[],
    name_mapping={"post_start": "postStart", "pre_stop": "preStop"},
)
class ContainerLifecycle:
    def __init__(
        self,
        *,
        post_start: typing.Optional["Handler"] = None,
        pre_stop: typing.Optional["Handler"] = None,
    ) -> None:
        '''Container lifecycle properties.

        :param post_start: This hook is executed immediately after a container is created. However, there is no guarantee that the hook will execute before the container ENTRYPOINT. Default: - No post start handler.
        :param pre_stop: This hook is called immediately before a container is terminated due to an API request or management event such as a liveness/startup probe failure, preemption, resource contention and others. A call to the PreStop hook fails if the container is already in a terminated or completed state and the hook must complete before the TERM signal to stop the container can be sent. The Pod's termination grace period countdown begins before the PreStop hook is executed, so regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. No parameters are passed to the handler. Default: - No pre stop handler.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerLifecycle.__init__)
            check_type(argname="argument post_start", value=post_start, expected_type=type_hints["post_start"])
            check_type(argname="argument pre_stop", value=pre_stop, expected_type=type_hints["pre_stop"])
        self._values: typing.Dict[str, typing.Any] = {}
        if post_start is not None:
            self._values["post_start"] = post_start
        if pre_stop is not None:
            self._values["pre_stop"] = pre_stop

    @builtins.property
    def post_start(self) -> typing.Optional["Handler"]:
        '''This hook is executed immediately after a container is created.

        However,
        there is no guarantee that the hook will execute before the container ENTRYPOINT.

        :default: - No post start handler.
        '''
        result = self._values.get("post_start")
        return typing.cast(typing.Optional["Handler"], result)

    @builtins.property
    def pre_stop(self) -> typing.Optional["Handler"]:
        '''This hook is called immediately before a container is terminated due to an API request or management event such as a liveness/startup probe failure, preemption, resource contention and others.

        A call to the PreStop hook fails if the container is already in a terminated or completed state
        and the hook must complete before the TERM signal to stop the container can be sent.
        The Pod's termination grace period countdown begins before the PreStop hook is executed,
        so regardless of the outcome of the handler, the container will eventually terminate
        within the Pod's termination grace period. No parameters are passed to the handler.

        :default: - No pre stop handler.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination
        '''
        result = self._values.get("pre_stop")
        return typing.cast(typing.Optional["Handler"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerLifecycle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ContainerPort",
    jsii_struct_bases=[],
    name_mapping={
        "number": "number",
        "host_ip": "hostIp",
        "host_port": "hostPort",
        "name": "name",
        "protocol": "protocol",
    },
)
class ContainerPort:
    def __init__(
        self,
        *,
        number: jsii.Number,
        host_ip: typing.Optional[builtins.str] = None,
        host_port: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional["Protocol"] = None,
    ) -> None:
        '''Represents a network port in a single container.

        :param number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.
        :param host_ip: What host IP to bind the external port to. Default: - 127.0.0.1.
        :param host_port: Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. Most containers do not need this. Default: - auto generated by kubernetes and might change on restarts.
        :param name: If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. Default: - port is not named.
        :param protocol: Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". Default: Protocol.TCP
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerPort.__init__)
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument host_ip", value=host_ip, expected_type=type_hints["host_ip"])
            check_type(argname="argument host_port", value=host_port, expected_type=type_hints["host_port"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "number": number,
        }
        if host_ip is not None:
            self._values["host_ip"] = host_ip
        if host_port is not None:
            self._values["host_port"] = host_port
        if name is not None:
            self._values["name"] = name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def number(self) -> jsii.Number:
        '''Number of port to expose on the pod's IP address.

        This must be a valid port number, 0 < x < 65536.
        '''
        result = self._values.get("number")
        assert result is not None, "Required property 'number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def host_ip(self) -> typing.Optional[builtins.str]:
        '''What host IP to bind the external port to.

        :default: - 127.0.0.1.
        '''
        result = self._values.get("host_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_port(self) -> typing.Optional[jsii.Number]:
        '''Number of port to expose on the host.

        If specified, this must be a valid port number, 0 < x < 65536.
        Most containers do not need this.

        :default: - auto generated by kubernetes and might change on restarts.
        '''
        result = self._values.get("host_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If specified, this must be an IANA_SVC_NAME and unique within the pod.

        Each named port in a pod must have a unique name.
        Name for the port that can be referred to by services.

        :default: - port is not named.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional["Protocol"]:
        '''Protocol for port.

        Must be UDP, TCP, or SCTP. Defaults to "TCP".

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional["Protocol"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "args": "args",
        "command": "command",
        "env_from": "envFrom",
        "env_variables": "envVariables",
        "image_pull_policy": "imagePullPolicy",
        "lifecycle": "lifecycle",
        "liveness": "liveness",
        "name": "name",
        "port": "port",
        "port_number": "portNumber",
        "ports": "ports",
        "readiness": "readiness",
        "resources": "resources",
        "security_context": "securityContext",
        "startup": "startup",
        "volume_mounts": "volumeMounts",
        "working_dir": "workingDir",
    },
)
class ContainerProps:
    def __init__(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env_from: typing.Optional[typing.Sequence["EnvFrom"]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, "EnvValue"]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[typing.Union[ContainerLifecycle, typing.Dict[str, typing.Any]]] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_number: typing.Optional[jsii.Number] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ContainerPort, typing.Dict[str, typing.Any]]]] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional[typing.Union["ContainerResources", typing.Dict[str, typing.Any]]] = None,
        security_context: typing.Optional[typing.Union["ContainerSecurityContextProps", typing.Dict[str, typing.Any]]] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Union["VolumeMount", typing.Dict[str, typing.Any]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating a container.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env_from: List of sources to populate environment variables in the container. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by the ``envVariables`` property with a duplicate key will take precedence. Default: - No sources.
        :param env_variables: Environment variables to set in the container. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: 
        :param port_number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. This is a convinience property if all you need a single TCP numbered port. In case more advanced configuartion is required, use the ``ports`` property. This port is added to the list of ports mentioned in the ``ports`` property. Default: - Only the ports mentiond in the ``ports`` property are exposed.
        :param ports: List of ports to expose from this container. Default: - Only the port mentioned in the ``portNumber`` property is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container. Default: cpu: request: 1000 millis limit: 1500 millis memory: request: 512 mebibytes limit: 2048 mebibytes
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - If a port is provided, then knocks on that port to determine when the container is ready for readiness and liveness probe checks. Otherwise, no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = ContainerLifecycle(**lifecycle)
        if isinstance(resources, dict):
            resources = ContainerResources(**resources)
        if isinstance(security_context, dict):
            security_context = ContainerSecurityContextProps(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerProps.__init__)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument env_from", value=env_from, expected_type=type_hints["env_from"])
            check_type(argname="argument env_variables", value=env_variables, expected_type=type_hints["env_variables"])
            check_type(argname="argument image_pull_policy", value=image_pull_policy, expected_type=type_hints["image_pull_policy"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument liveness", value=liveness, expected_type=type_hints["liveness"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_number", value=port_number, expected_type=type_hints["port_number"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument readiness", value=readiness, expected_type=type_hints["readiness"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument startup", value=startup, expected_type=type_hints["startup"])
            check_type(argname="argument volume_mounts", value=volume_mounts, expected_type=type_hints["volume_mounts"])
            check_type(argname="argument working_dir", value=working_dir, expected_type=type_hints["working_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if args is not None:
            self._values["args"] = args
        if command is not None:
            self._values["command"] = command
        if env_from is not None:
            self._values["env_from"] = env_from
        if env_variables is not None:
            self._values["env_variables"] = env_variables
        if image_pull_policy is not None:
            self._values["image_pull_policy"] = image_pull_policy
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if liveness is not None:
            self._values["liveness"] = liveness
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if port_number is not None:
            self._values["port_number"] = port_number
        if ports is not None:
            self._values["ports"] = ports
        if readiness is not None:
            self._values["readiness"] = readiness
        if resources is not None:
            self._values["resources"] = resources
        if security_context is not None:
            self._values["security_context"] = security_context
        if startup is not None:
            self._values["startup"] = startup
        if volume_mounts is not None:
            self._values["volume_mounts"] = volume_mounts
        if working_dir is not None:
            self._values["working_dir"] = working_dir

    @builtins.property
    def image(self) -> builtins.str:
        '''Docker image name.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided.

        Variable references $(VAR_NAME) are expanded using the container's
        environment. If a variable cannot be resolved, the reference in the input
        string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
        regardless of whether the variable exists or not.

        Cannot be updated.

        :default: []

        :see: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Entrypoint array.

        Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment.
        If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME).
        Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated.
        More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

        :default: - The docker image's ENTRYPOINT.
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env_from(self) -> typing.Optional[typing.List["EnvFrom"]]:
        '''List of sources to populate environment variables in the container.

        When a key exists in multiple sources, the value associated with
        the last source will take precedence. Values defined by the ``envVariables`` property
        with a duplicate key will take precedence.

        :default: - No sources.
        '''
        result = self._values.get("env_from")
        return typing.cast(typing.Optional[typing.List["EnvFrom"]], result)

    @builtins.property
    def env_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "EnvValue"]]:
        '''Environment variables to set in the container.

        :default: - No environment variables.
        '''
        result = self._values.get("env_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "EnvValue"]], result)

    @builtins.property
    def image_pull_policy(self) -> typing.Optional["ImagePullPolicy"]:
        '''Image pull policy for this container.

        :default: ImagePullPolicy.ALWAYS
        '''
        result = self._values.get("image_pull_policy")
        return typing.cast(typing.Optional["ImagePullPolicy"], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[ContainerLifecycle]:
        '''Describes actions that the management system should take in response to container lifecycle events.'''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[ContainerLifecycle], result)

    @builtins.property
    def liveness(self) -> typing.Optional["Probe"]:
        '''Periodic probe of container liveness.

        Container will be restarted if the probe fails.

        :default: - no liveness probe is defined
        '''
        result = self._values.get("liveness")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the container specified as a DNS_LABEL.

        Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :default: 'main'
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :deprecated: - use ``portNumber``.

        :stability: deprecated
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_number(self) -> typing.Optional[jsii.Number]:
        '''Number of port to expose on the pod's IP address.

        This must be a valid port number, 0 < x < 65536.

        This is a convinience property if all you need a single TCP numbered port.
        In case more advanced configuartion is required, use the ``ports`` property.

        This port is added to the list of ports mentioned in the ``ports`` property.

        :default: - Only the ports mentiond in the ``ports`` property are exposed.
        '''
        result = self._values.get("port_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[ContainerPort]]:
        '''List of ports to expose from this container.

        :default: - Only the port mentioned in the ``portNumber`` property is exposed.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[ContainerPort]], result)

    @builtins.property
    def readiness(self) -> typing.Optional["Probe"]:
        '''Determines when the container is ready to serve traffic.

        :default: - no readiness probe is defined
        '''
        result = self._values.get("readiness")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def resources(self) -> typing.Optional["ContainerResources"]:
        '''Compute resources (CPU and memory requests and limits) required by the container.

        :default:

        cpu:
        request: 1000 millis
        limit: 1500 millis
        memory:
        request: 512 mebibytes
        limit: 2048 mebibytes

        :see: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["ContainerResources"], result)

    @builtins.property
    def security_context(self) -> typing.Optional["ContainerSecurityContextProps"]:
        '''SecurityContext defines the security options the container should be run with.

        If set, the fields override equivalent fields of the pod's security context.

        :default:

        ensureNonRoot: false
        privileged: false
        readOnlyRootFilesystem: false

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ContainerSecurityContextProps"], result)

    @builtins.property
    def startup(self) -> typing.Optional["Probe"]:
        '''StartupProbe indicates that the Pod has successfully initialized.

        If specified, no other probes are executed until this completes successfully

        :default:

        - If a port is provided, then knocks on that port
        to determine when the container is ready for readiness and
        liveness probe checks.
        Otherwise, no startup probe is defined.
        '''
        result = self._values.get("startup")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def volume_mounts(self) -> typing.Optional[typing.List["VolumeMount"]]:
        '''Pod volumes to mount into the container's filesystem.

        Cannot be updated.
        '''
        result = self._values.get("volume_mounts")
        return typing.cast(typing.Optional[typing.List["VolumeMount"]], result)

    @builtins.property
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''Container's working directory.

        If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :default: - The container runtime's default.
        '''
        result = self._values.get("working_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ContainerResources",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "ephemeral_storage": "ephemeralStorage",
        "memory": "memory",
    },
)
class ContainerResources:
    def __init__(
        self,
        *,
        cpu: typing.Optional[typing.Union["CpuResources", typing.Dict[str, typing.Any]]] = None,
        ephemeral_storage: typing.Optional[typing.Union["EphemeralStorageResources", typing.Dict[str, typing.Any]]] = None,
        memory: typing.Optional[typing.Union["MemoryResources", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''CPU and memory compute resources.

        :param cpu: 
        :param ephemeral_storage: 
        :param memory: 
        '''
        if isinstance(cpu, dict):
            cpu = CpuResources(**cpu)
        if isinstance(ephemeral_storage, dict):
            ephemeral_storage = EphemeralStorageResources(**ephemeral_storage)
        if isinstance(memory, dict):
            memory = MemoryResources(**memory)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerResources.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage is not None:
            self._values["ephemeral_storage"] = ephemeral_storage
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def cpu(self) -> typing.Optional["CpuResources"]:
        result = self._values.get("cpu")
        return typing.cast(typing.Optional["CpuResources"], result)

    @builtins.property
    def ephemeral_storage(self) -> typing.Optional["EphemeralStorageResources"]:
        result = self._values.get("ephemeral_storage")
        return typing.cast(typing.Optional["EphemeralStorageResources"], result)

    @builtins.property
    def memory(self) -> typing.Optional["MemoryResources"]:
        result = self._values.get("memory")
        return typing.cast(typing.Optional["MemoryResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerSecurityContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ContainerSecurityContext",
):
    '''Container security attributes and settings.'''

    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        group: typing.Optional[jsii.Number] = None,
        privileged: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param group: The GID to run the entrypoint of the container process. Default: - 26000. An arbitrary number bigger than 9999 is selected here. This is so that the container is blocked to access host files even if somehow it manages to get access to host file system.
        :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Default: false
        :param read_only_root_filesystem: Whether this container has a read-only root filesystem. Default: false
        :param user: The UID to run the entrypoint of the container process. Default: - 25000. An arbitrary number bigger than 9999 is selected here. This is so that the container is blocked to access host files even if somehow it manages to get access to host file system.
        '''
        props = ContainerSecurityContextProps(
            ensure_non_root=ensure_non_root,
            group=group,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            user=user,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="ensureNonRoot")
    def ensure_non_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "ensureNonRoot"))

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "privileged"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystem")
    def read_only_root_filesystem(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "readOnlyRootFilesystem"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "user"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ContainerSecurityContextProps",
    jsii_struct_bases=[],
    name_mapping={
        "ensure_non_root": "ensureNonRoot",
        "group": "group",
        "privileged": "privileged",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "user": "user",
    },
)
class ContainerSecurityContextProps:
    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        group: typing.Optional[jsii.Number] = None,
        privileged: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``ContainerSecurityContext``.

        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param group: The GID to run the entrypoint of the container process. Default: - 26000. An arbitrary number bigger than 9999 is selected here. This is so that the container is blocked to access host files even if somehow it manages to get access to host file system.
        :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Default: false
        :param read_only_root_filesystem: Whether this container has a read-only root filesystem. Default: false
        :param user: The UID to run the entrypoint of the container process. Default: - 25000. An arbitrary number bigger than 9999 is selected here. This is so that the container is blocked to access host files even if somehow it manages to get access to host file system.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerSecurityContextProps.__init__)
            check_type(argname="argument ensure_non_root", value=ensure_non_root, expected_type=type_hints["ensure_non_root"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ensure_non_root is not None:
            self._values["ensure_non_root"] = ensure_non_root
        if group is not None:
            self._values["group"] = group
        if privileged is not None:
            self._values["privileged"] = privileged
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def ensure_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it does
        not run as UID 0 (root) and fail to start the container if it does.

        :default: false
        '''
        result = self._values.get("ensure_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        :default:

        -
        26000. An arbitrary number bigger than 9999 is selected here.
        This is so that the container is blocked to access host files even if
        somehow it manages to get access to host file system.
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged(self) -> typing.Optional[builtins.bool]:
        '''Run container in privileged mode.

        Processes in privileged containers are essentially equivalent to root on the host.

        :default: false
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only_root_filesystem(self) -> typing.Optional[builtins.bool]:
        '''Whether this container has a read-only root filesystem.

        :default: false
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        :default:

        -
        25000. An arbitrary number bigger than 9999 is selected here.
        This is so that the container is blocked to access host files even if
        somehow it manages to get access to host file system.
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerSecurityContextProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Cpu(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Cpu"):
    '''Represents the amount of CPU.

    The amount can be passed as millis or units.
    '''

    @jsii.member(jsii_name="millis")
    @builtins.classmethod
    def millis(cls, amount: jsii.Number) -> "Cpu":
        '''
        :param amount: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cpu.millis)
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
        return typing.cast("Cpu", jsii.sinvoke(cls, "millis", [amount]))

    @jsii.member(jsii_name="units")
    @builtins.classmethod
    def units(cls, amount: jsii.Number) -> "Cpu":
        '''
        :param amount: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cpu.units)
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
        return typing.cast("Cpu", jsii.sinvoke(cls, "units", [amount]))

    @builtins.property
    @jsii.member(jsii_name="amount")
    def amount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amount"))

    @amount.setter
    def amount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cpu, "amount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amount", value)


@jsii.data_type(
    jsii_type="cdk8s-plus-23.CpuResources",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit", "request": "request"},
)
class CpuResources:
    def __init__(
        self,
        *,
        limit: typing.Optional[Cpu] = None,
        request: typing.Optional[Cpu] = None,
    ) -> None:
        '''CPU request and limit.

        :param limit: 
        :param request: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CpuResources.__init__)
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if limit is not None:
            self._values["limit"] = limit
        if request is not None:
            self._values["request"] = request

    @builtins.property
    def limit(self) -> typing.Optional[Cpu]:
        result = self._values.get("limit")
        return typing.cast(typing.Optional[Cpu], result)

    @builtins.property
    def request(self) -> typing.Optional[Cpu]:
        result = self._values.get("request")
        return typing.cast(typing.Optional[Cpu], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpuResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DeploymentExposeViaServiceOptions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "ports": "ports", "service_type": "serviceType"},
)
class DeploymentExposeViaServiceOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Sequence[typing.Union["ServicePort", typing.Dict[str, typing.Any]]]] = None,
        service_type: typing.Optional["ServiceType"] = None,
    ) -> None:
        '''Options for ``Deployment.exposeViaService``.

        :param name: The name of the service to expose. If you'd like to expose the deployment multiple times, you must explicitly set a name starting from the second expose call. Default: - auto generated.
        :param ports: The ports that the service should bind to. Default: - extracted from the deployment.
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DeploymentExposeViaServiceOptions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if ports is not None:
            self._values["ports"] = ports
        if service_type is not None:
            self._values["service_type"] = service_type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service to expose.

        If you'd like to expose the deployment multiple times,
        you must explicitly set a name starting from the second expose call.

        :default: - auto generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["ServicePort"]]:
        '''The ports that the service should bind to.

        :default: - extracted from the deployment.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["ServicePort"]], result)

    @builtins.property
    def service_type(self) -> typing.Optional["ServiceType"]:
        '''The type of the exposed service.

        :default: - ClusterIP.
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional["ServiceType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentExposeViaServiceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DeploymentStrategy(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.DeploymentStrategy",
):
    '''Deployment strategies.'''

    @jsii.member(jsii_name="recreate")
    @builtins.classmethod
    def recreate(cls) -> "DeploymentStrategy":
        '''All existing Pods are killed before new ones are created.

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#recreate-deployment
        '''
        return typing.cast("DeploymentStrategy", jsii.sinvoke(cls, "recreate", []))

    @jsii.member(jsii_name="rollingUpdate")
    @builtins.classmethod
    def rolling_update(
        cls,
        *,
        max_surge: typing.Optional["PercentOrAbsolute"] = None,
        max_unavailable: typing.Optional["PercentOrAbsolute"] = None,
    ) -> "DeploymentStrategy":
        '''
        :param max_surge: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if ``maxUnavailable`` is 0. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. Default: '25%'
        :param max_unavailable: The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if ``maxSurge`` is 0. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. Default: '25%'
        '''
        options = DeploymentStrategyRollingUpdateOptions(
            max_surge=max_surge, max_unavailable=max_unavailable
        )

        return typing.cast("DeploymentStrategy", jsii.sinvoke(cls, "rollingUpdate", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DeploymentStrategyRollingUpdateOptions",
    jsii_struct_bases=[],
    name_mapping={"max_surge": "maxSurge", "max_unavailable": "maxUnavailable"},
)
class DeploymentStrategyRollingUpdateOptions:
    def __init__(
        self,
        *,
        max_surge: typing.Optional["PercentOrAbsolute"] = None,
        max_unavailable: typing.Optional["PercentOrAbsolute"] = None,
    ) -> None:
        '''Options for ``DeploymentStrategy.rollingUpdate``.

        :param max_surge: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if ``maxUnavailable`` is 0. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. Default: '25%'
        :param max_unavailable: The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if ``maxSurge`` is 0. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. Default: '25%'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DeploymentStrategyRollingUpdateOptions.__init__)
            check_type(argname="argument max_surge", value=max_surge, expected_type=type_hints["max_surge"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_surge is not None:
            self._values["max_surge"] = max_surge
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable

    @builtins.property
    def max_surge(self) -> typing.Optional["PercentOrAbsolute"]:
        '''The maximum number of pods that can be scheduled above the desired number of pods.

        Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%).
        Absolute number is calculated from percentage by rounding up.
        This can not be 0 if ``maxUnavailable`` is 0.

        Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update
        starts, such that the total number of old and new pods do not exceed 130% of desired pods.
        Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that
        total number of pods running at any time during the update is at most 130% of desired pods.

        :default: '25%'
        '''
        result = self._values.get("max_surge")
        return typing.cast(typing.Optional["PercentOrAbsolute"], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional["PercentOrAbsolute"]:
        '''The maximum number of pods that can be unavailable during the update.

        Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%).
        Absolute number is calculated from percentage by rounding down.
        This can not be 0 if ``maxSurge`` is 0.

        Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired
        pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can
        be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total
        number of pods available at all times during the update is at least 70% of desired pods.

        :default: '25%'
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional["PercentOrAbsolute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentStrategyRollingUpdateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DnsOption",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class DnsOption:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Custom DNS option.

        :param name: Option name.
        :param value: Option value. Default: - No value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DnsOption.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Option name.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Option value.

        :default: - No value.
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.DnsPolicy")
class DnsPolicy(enum.Enum):
    '''Pod DNS policies.'''

    CLUSTER_FIRST = "CLUSTER_FIRST"
    '''Any DNS query that does not match the configured cluster domain suffix, such as "www.kubernetes.io", is forwarded to the upstream nameserver inherited from the node. Cluster administrators may have extra stub-domain and upstream DNS servers configured.'''
    CLUSTER_FIRST_WITH_HOST_NET = "CLUSTER_FIRST_WITH_HOST_NET"
    '''For Pods running with hostNetwork, you should explicitly set its DNS policy "ClusterFirstWithHostNet".'''
    DEFAULT = "DEFAULT"
    '''The Pod inherits the name resolution configuration from the node that the pods run on.'''
    NONE = "NONE"
    '''It allows a Pod to ignore DNS settings from the Kubernetes environment.

    All DNS settings are supposed to be provided using the dnsConfig
    field in the Pod Spec.
    '''


@jsii.enum(jsii_type="cdk8s-plus-23.EmptyDirMedium")
class EmptyDirMedium(enum.Enum):
    '''The medium on which to store the volume.'''

    DEFAULT = "DEFAULT"
    '''The default volume of the backing node.'''
    MEMORY = "MEMORY"
    '''Mount a tmpfs (RAM-backed filesystem) for you instead.

    While tmpfs is very
    fast, be aware that unlike disks, tmpfs is cleared on node reboot and any
    files you write will count against your Container's memory limit.
    '''


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EmptyDirVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={"medium": "medium", "size_limit": "sizeLimit"},
)
class EmptyDirVolumeOptions:
    def __init__(
        self,
        *,
        medium: typing.Optional[EmptyDirMedium] = None,
        size_limit: typing.Optional[cdk8s.Size] = None,
    ) -> None:
        '''Options for volumes populated with an empty directory.

        :param medium: By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment. However, you can set the emptyDir.medium field to ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that unlike disks, tmpfs is cleared on node reboot and any files you write will count against your Container's memory limit. Default: EmptyDirMedium.DEFAULT
        :param size_limit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. Default: - limit is undefined
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EmptyDirVolumeOptions.__init__)
            check_type(argname="argument medium", value=medium, expected_type=type_hints["medium"])
            check_type(argname="argument size_limit", value=size_limit, expected_type=type_hints["size_limit"])
        self._values: typing.Dict[str, typing.Any] = {}
        if medium is not None:
            self._values["medium"] = medium
        if size_limit is not None:
            self._values["size_limit"] = size_limit

    @builtins.property
    def medium(self) -> typing.Optional[EmptyDirMedium]:
        '''By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment.

        However, you can set the emptyDir.medium field to
        ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed
        filesystem) for you instead. While tmpfs is very fast, be aware that unlike
        disks, tmpfs is cleared on node reboot and any files you write will count
        against your Container's memory limit.

        :default: EmptyDirMedium.DEFAULT
        '''
        result = self._values.get("medium")
        return typing.cast(typing.Optional[EmptyDirMedium], result)

    @builtins.property
    def size_limit(self) -> typing.Optional[cdk8s.Size]:
        '''Total amount of local storage required for this EmptyDir volume.

        The size
        limit is also applicable for memory medium. The maximum usage on memory
        medium EmptyDir would be the minimum value between the SizeLimit specified
        here and the sum of memory limits of all containers in a pod.

        :default: - limit is undefined
        '''
        result = self._values.get("size_limit")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmptyDirVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Env(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Env"):
    '''Container environment variables.'''

    def __init__(
        self,
        sources: typing.Sequence["EnvFrom"],
        variables: typing.Mapping[builtins.str, "EnvValue"],
    ) -> None:
        '''
        :param sources: -
        :param variables: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Env.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        jsii.create(self.__class__, self, [sources, variables])

    @jsii.member(jsii_name="fromConfigMap")
    @builtins.classmethod
    def from_config_map(
        cls,
        config_map: "IConfigMap",
        prefix: typing.Optional[builtins.str] = None,
    ) -> "EnvFrom":
        '''Selects a ConfigMap to populate the environment variables with.

        The contents of the target ConfigMap's Data field will represent
        the key-value pairs as environment variables.

        :param config_map: -
        :param prefix: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Env.from_config_map)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        return typing.cast("EnvFrom", jsii.sinvoke(cls, "fromConfigMap", [config_map, prefix]))

    @jsii.member(jsii_name="fromSecret")
    @builtins.classmethod
    def from_secret(cls, secr: "ISecret") -> "EnvFrom":
        '''Selects a Secret to populate the environment variables with.

        The contents of the target Secret's Data field will represent
        the key-value pairs as environment variables.

        :param secr: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Env.from_secret)
            check_type(argname="argument secr", value=secr, expected_type=type_hints["secr"])
        return typing.cast("EnvFrom", jsii.sinvoke(cls, "fromSecret", [secr]))

    @jsii.member(jsii_name="addVariable")
    def add_variable(self, name: builtins.str, value: "EnvValue") -> None:
        '''Add a single variable by name and value.

        The variable value can come from various dynamic sources such a secrets of config maps.
        Use ``EnvValue.fromXXX`` to select sources.

        :param name: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Env.add_variable)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addVariable", [name, value]))

    @jsii.member(jsii_name="copyFrom")
    def copy_from(self, from_: "EnvFrom") -> None:
        '''Add a collection of variables by copying from another source.

        Use ``Env.fromXXX`` functions to select sources.

        :param from_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Env.copy_from)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
        return typing.cast(None, jsii.invoke(self, "copyFrom", [from_]))

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List["EnvFrom"]:
        '''The list of sources used to populate the container environment, in addition to the ``variables``.

        Returns a copy. To add a source use ``container.env.copyFrom()``.
        '''
        return typing.cast(typing.List["EnvFrom"], jsii.get(self, "sources"))

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(self) -> typing.Mapping[builtins.str, "EnvValue"]:
        '''The environment variables for this container.

        Returns a copy. To add environment variables use ``container.env.addVariable()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, "EnvValue"], jsii.get(self, "variables"))


@jsii.enum(jsii_type="cdk8s-plus-23.EnvFieldPaths")
class EnvFieldPaths(enum.Enum):
    POD_NAME = "POD_NAME"
    '''The name of the pod.'''
    POD_NAMESPACE = "POD_NAMESPACE"
    '''The namespace of the pod.'''
    POD_UID = "POD_UID"
    '''The uid of the pod.'''
    POD_LABEL = "POD_LABEL"
    '''The labels of the pod.'''
    POD_ANNOTATION = "POD_ANNOTATION"
    '''The annotations of the pod.'''
    POD_IP = "POD_IP"
    '''The ipAddress of the pod.'''
    SERVICE_ACCOUNT_NAME = "SERVICE_ACCOUNT_NAME"
    '''The service account name of the pod.'''
    NODE_NAME = "NODE_NAME"
    '''The name of the node.'''
    NODE_IP = "NODE_IP"
    '''The ipAddress of the node.'''
    POD_IPS = "POD_IPS"
    '''The ipAddresess of the pod.'''


class EnvFrom(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.EnvFrom"):
    '''A collection of env variables defined in other resources.'''

    def __init__(
        self,
        config_map: typing.Optional["IConfigMap"] = None,
        prefix: typing.Optional[builtins.str] = None,
        sec: typing.Optional["ISecret"] = None,
    ) -> None:
        '''
        :param config_map: -
        :param prefix: -
        :param sec: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvFrom.__init__)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument sec", value=sec, expected_type=type_hints["sec"])
        jsii.create(self.__class__, self, [config_map, prefix, sec])


class EnvValue(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.EnvValue"):
    '''Utility class for creating reading env values from various sources.'''

    @jsii.member(jsii_name="fromConfigMap")
    @builtins.classmethod
    def from_config_map(
        cls,
        config_map: "IConfigMap",
        key: builtins.str,
        *,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Create a value by reading a specific key inside a config map.

        :param config_map: - The config map.
        :param key: - The key to extract the value from.
        :param optional: Specify whether the ConfigMap or its key must be defined. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_config_map)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        options = EnvValueFromConfigMapOptions(optional=optional)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromConfigMap", [config_map, key, options]))

    @jsii.member(jsii_name="fromFieldRef")
    @builtins.classmethod
    def from_field_ref(
        cls,
        field_path: EnvFieldPaths,
        *,
        api_version: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> "EnvValue":
        '''Create a value from a field reference.

        :param field_path: : The field reference.
        :param api_version: Version of the schema the FieldPath is written in terms of.
        :param key: The key to select the pod label or annotation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_field_ref)
            check_type(argname="argument field_path", value=field_path, expected_type=type_hints["field_path"])
        options = EnvValueFromFieldRefOptions(api_version=api_version, key=key)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromFieldRef", [field_path, options]))

    @jsii.member(jsii_name="fromProcess")
    @builtins.classmethod
    def from_process(
        cls,
        key: builtins.str,
        *,
        required: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Create a value from a key in the current process environment.

        :param key: - The key to read.
        :param required: Specify whether the key must exist in the environment. If this is set to true, and the key does not exist, an error will thrown. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_process)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        options = EnvValueFromProcessOptions(required=required)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromProcess", [key, options]))

    @jsii.member(jsii_name="fromResource")
    @builtins.classmethod
    def from_resource(
        cls,
        resource: "ResourceFieldPaths",
        *,
        container: typing.Optional[Container] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> "EnvValue":
        '''Create a value from a resource.

        :param resource: : Resource to select the value from.
        :param container: The container to select the value from.
        :param divisor: The output format of the exposed resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_resource)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        options = EnvValueFromResourceOptions(container=container, divisor=divisor)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromResource", [resource, options]))

    @jsii.member(jsii_name="fromSecretValue")
    @builtins.classmethod
    def from_secret_value(
        cls,
        secret_value: typing.Union["SecretValue", typing.Dict[str, typing.Any]],
        *,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Defines an environment value from a secret JSON value.

        :param secret_value: The secret value (secrent + key).
        :param optional: Specify whether the Secret or its key must be defined. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_secret_value)
            check_type(argname="argument secret_value", value=secret_value, expected_type=type_hints["secret_value"])
        options = EnvValueFromSecretOptions(optional=optional)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromSecretValue", [secret_value, options]))

    @jsii.member(jsii_name="fromValue")
    @builtins.classmethod
    def from_value(cls, value: builtins.str) -> "EnvValue":
        '''Create a value from the given argument.

        :param value: - The value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValue.from_value)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromValue", [value]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="valueFrom")
    def value_from(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "valueFrom"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EnvValueFromConfigMapOptions",
    jsii_struct_bases=[],
    name_mapping={"optional": "optional"},
)
class EnvValueFromConfigMapOptions:
    def __init__(self, *, optional: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an envionment variable value from a ConfigMap key.

        :param optional: Specify whether the ConfigMap or its key must be defined. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValueFromConfigMapOptions.__init__)
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[str, typing.Any] = {}
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its key must be defined.

        :default: false
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromConfigMapOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EnvValueFromFieldRefOptions",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion", "key": "key"},
)
class EnvValueFromFieldRefOptions:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to specify an environment variable value from a field reference.

        :param api_version: Version of the schema the FieldPath is written in terms of.
        :param key: The key to select the pod label or annotation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValueFromFieldRefOptions.__init__)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Version of the schema the FieldPath is written in terms of.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key to select the pod label or annotation.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromFieldRefOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EnvValueFromProcessOptions",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class EnvValueFromProcessOptions:
    def __init__(self, *, required: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an environment variable value from the process environment.

        :param required: Specify whether the key must exist in the environment. If this is set to true, and the key does not exist, an error will thrown. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValueFromProcessOptions.__init__)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the key must exist in the environment.

        If this is set to true, and the key does not exist, an error will thrown.

        :default: false
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromProcessOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EnvValueFromResourceOptions",
    jsii_struct_bases=[],
    name_mapping={"container": "container", "divisor": "divisor"},
)
class EnvValueFromResourceOptions:
    def __init__(
        self,
        *,
        container: typing.Optional[Container] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to specify an environment variable value from a resource.

        :param container: The container to select the value from.
        :param divisor: The output format of the exposed resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValueFromResourceOptions.__init__)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument divisor", value=divisor, expected_type=type_hints["divisor"])
        self._values: typing.Dict[str, typing.Any] = {}
        if container is not None:
            self._values["container"] = container
        if divisor is not None:
            self._values["divisor"] = divisor

    @builtins.property
    def container(self) -> typing.Optional[Container]:
        '''The container to select the value from.'''
        result = self._values.get("container")
        return typing.cast(typing.Optional[Container], result)

    @builtins.property
    def divisor(self) -> typing.Optional[builtins.str]:
        '''The output format of the exposed resource.'''
        result = self._values.get("divisor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EnvValueFromSecretOptions",
    jsii_struct_bases=[],
    name_mapping={"optional": "optional"},
)
class EnvValueFromSecretOptions:
    def __init__(self, *, optional: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an environment variable value from a Secret.

        :param optional: Specify whether the Secret or its key must be defined. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EnvValueFromSecretOptions.__init__)
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[str, typing.Any] = {}
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :default: false
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromSecretOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.EphemeralStorageResources",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit", "request": "request"},
)
class EphemeralStorageResources:
    def __init__(
        self,
        *,
        limit: typing.Optional[cdk8s.Size] = None,
        request: typing.Optional[cdk8s.Size] = None,
    ) -> None:
        '''Emphemeral storage request and limit.

        :param limit: 
        :param request: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EphemeralStorageResources.__init__)
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if limit is not None:
            self._values["limit"] = limit
        if request is not None:
            self._values["request"] = request

    @builtins.property
    def limit(self) -> typing.Optional[cdk8s.Size]:
        result = self._values.get("limit")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def request(self) -> typing.Optional[cdk8s.Size]:
        result = self._values.get("request")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EphemeralStorageResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ExposeServiceViaIngressOptions",
    jsii_struct_bases=[],
    name_mapping={"ingress": "ingress", "path_type": "pathType"},
)
class ExposeServiceViaIngressOptions:
    def __init__(
        self,
        *,
        ingress: typing.Optional["Ingress"] = None,
        path_type: typing.Optional["HttpIngressPathType"] = None,
    ) -> None:
        '''Options for exposing a service using an ingress.

        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        :param path_type: The type of the path. Default: HttpIngressPathType.PREFIX
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExposeServiceViaIngressOptions.__init__)
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ingress is not None:
            self._values["ingress"] = ingress
        if path_type is not None:
            self._values["path_type"] = path_type

    @builtins.property
    def ingress(self) -> typing.Optional["Ingress"]:
        '''The ingress to add rules to.

        :default: - An ingress will be automatically created.
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["Ingress"], result)

    @builtins.property
    def path_type(self) -> typing.Optional["HttpIngressPathType"]:
        '''The type of the path.

        :default: HttpIngressPathType.PREFIX
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional["HttpIngressPathType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExposeServiceViaIngressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.FsGroupChangePolicy")
class FsGroupChangePolicy(enum.Enum):
    ON_ROOT_MISMATCH = "ON_ROOT_MISMATCH"
    '''Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume.

    This could help shorten the time it takes to change ownership and permission of a volume
    '''
    ALWAYS = "ALWAYS"
    '''Always change permission and ownership of the volume when volume is mounted.'''


@jsii.data_type(
    jsii_type="cdk8s-plus-23.GCEPersistentDiskVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "fs_type": "fsType",
        "name": "name",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class GCEPersistentDiskVolumeOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromGcePersistentDisk``.

        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GCEPersistentDiskVolumeOptions.__init__)
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if name is not None:
            self._values["name"] = name
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GCEPersistentDiskVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Handler(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Handler"):
    '''Defines a specific action that should be taken.'''

    @jsii.member(jsii_name="fromCommand")
    @builtins.classmethod
    def from_command(cls, command: typing.Sequence[builtins.str]) -> "Handler":
        '''Defines a handler based on a command which is executed within the container.

        :param command: The command to execute.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Handler.from_command)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        return typing.cast("Handler", jsii.sinvoke(cls, "fromCommand", [command]))

    @jsii.member(jsii_name="fromHttpGet")
    @builtins.classmethod
    def from_http_get(
        cls,
        path: builtins.str,
        *,
        port: typing.Optional[jsii.Number] = None,
    ) -> "Handler":
        '''Defines a handler based on an HTTP GET request to the IP address of the container.

        :param path: The URL path to hit.
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Handler.from_http_get)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = HandlerFromHttpGetOptions(port=port)

        return typing.cast("Handler", jsii.sinvoke(cls, "fromHttpGet", [path, options]))

    @jsii.member(jsii_name="fromTcpSocket")
    @builtins.classmethod
    def from_tcp_socket(
        cls,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> "Handler":
        '''Defines a handler based opening a connection to a TCP socket on the container.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        options = HandlerFromTcpSocketOptions(host=host, port=port)

        return typing.cast("Handler", jsii.sinvoke(cls, "fromTcpSocket", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.HandlerFromHttpGetOptions",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class HandlerFromHttpGetOptions:
    def __init__(self, *, port: typing.Optional[jsii.Number] = None) -> None:
        '''Options for ``Handler.fromHttpGet``.

        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HandlerFromHttpGetOptions.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to use when sending the GET request.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HandlerFromHttpGetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.HandlerFromTcpSocketOptions",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class HandlerFromTcpSocketOptions:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Handler.fromTcpSocket``.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HandlerFromTcpSocketOptions.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The host name to connect to on the container.

        :default: - defaults to the pod IP
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to connect to on the container.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HandlerFromTcpSocketOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.HostAlias",
    jsii_struct_bases=[],
    name_mapping={"hostnames": "hostnames", "ip": "ip"},
)
class HostAlias:
    def __init__(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's /etc/hosts file.

        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostAlias.__init__)
            check_type(argname="argument hostnames", value=hostnames, expected_type=type_hints["hostnames"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
        self._values: typing.Dict[str, typing.Any] = {
            "hostnames": hostnames,
            "ip": ip,
        }

    @builtins.property
    def hostnames(self) -> typing.List[builtins.str]:
        '''Hostnames for the chosen IP address.'''
        result = self._values.get("hostnames")
        assert result is not None, "Required property 'hostnames' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ip(self) -> builtins.str:
        '''IP address of the host file entry.'''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.HostPathVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "type": "type"},
)
class HostPathVolumeOptions:
    def __init__(
        self,
        *,
        path: builtins.str,
        type: typing.Optional["HostPathVolumeType"] = None,
    ) -> None:
        '''Options for a HostPathVolume-based volume.

        :param path: The path of the directory on the host.
        :param type: The expected type of the path found on the host. Default: HostPathVolumeType.DEFAULT
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostPathVolumeOptions.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> builtins.str:
        '''The path of the directory on the host.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional["HostPathVolumeType"]:
        '''The expected type of the path found on the host.

        :default: HostPathVolumeType.DEFAULT
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["HostPathVolumeType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostPathVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.HostPathVolumeType")
class HostPathVolumeType(enum.Enum):
    '''Host path types.'''

    DEFAULT = "DEFAULT"
    '''Empty string (default) is for backward compatibility, which means that no checks will be performed before mounting the hostPath volume.'''
    DIRECTORY_OR_CREATE = "DIRECTORY_OR_CREATE"
    '''If nothing exists at the given path, an empty directory will be created there as needed with permission set to 0755, having the same group and ownership with Kubelet.'''
    DIRECTORY = "DIRECTORY"
    '''A directory must exist at the given path.'''
    FILE_OR_CREATE = "FILE_OR_CREATE"
    '''If nothing exists at the given path, an empty file will be created there as needed with permission set to 0644, having the same group and ownership with Kubelet.'''
    FILE = "FILE"
    '''A file must exist at the given path.'''
    SOCKET = "SOCKET"
    '''A UNIX socket must exist at the given path.'''
    CHAR_DEVICE = "CHAR_DEVICE"
    '''A character device must exist at the given path.'''
    BLOCK_DEVICE = "BLOCK_DEVICE"
    '''A block device must exist at the given path.'''


@jsii.enum(jsii_type="cdk8s-plus-23.HttpIngressPathType")
class HttpIngressPathType(enum.Enum):
    '''Specify how the path is matched against request paths.

    :see: https://kubernetes.io/docs/concepts/services-networking/ingress/#path-types
    '''

    PREFIX = "PREFIX"
    '''Matches the URL path exactly.'''
    EXACT = "EXACT"
    '''Matches based on a URL path prefix split by '/'.'''
    IMPLEMENTATION_SPECIFIC = "IMPLEMENTATION_SPECIFIC"
    '''Matching is specified by the underlying IngressClass.'''


@jsii.interface(jsii_type="cdk8s-plus-23.IApiEndpoint")
class IApiEndpoint(typing_extensions.Protocol):
    '''An API Endpoint can either be a resource descriptor (e.g /pods) or a non resource url (e.g /healthz). It must be one or the other, and not both.'''

    @jsii.member(jsii_name="asApiResource")
    def as_api_resource(self) -> typing.Optional["IApiResource"]:
        '''Return the IApiResource this object represents.'''
        ...

    @jsii.member(jsii_name="asNonApiResource")
    def as_non_api_resource(self) -> typing.Optional[builtins.str]:
        '''Return the non resource url this object represents.'''
        ...


class _IApiEndpointProxy:
    '''An API Endpoint can either be a resource descriptor (e.g /pods) or a non resource url (e.g /healthz). It must be one or the other, and not both.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IApiEndpoint"

    @jsii.member(jsii_name="asApiResource")
    def as_api_resource(self) -> typing.Optional["IApiResource"]:
        '''Return the IApiResource this object represents.'''
        return typing.cast(typing.Optional["IApiResource"], jsii.invoke(self, "asApiResource", []))

    @jsii.member(jsii_name="asNonApiResource")
    def as_non_api_resource(self) -> typing.Optional[builtins.str]:
        '''Return the non resource url this object represents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "asNonApiResource", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiEndpoint).__jsii_proxy_class__ = lambda : _IApiEndpointProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IApiResource")
class IApiResource(typing_extensions.Protocol):
    '''Represents a resource or collection of resources.'''

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. ``authorization.k8s.io``).'''
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources

        Example::

            - "pods" or "pods/log"
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceName")
    def resource_name(self) -> typing.Optional[builtins.str]:
        '''The unique, namespace-global, name of an object inside the Kubernetes cluster.

        If this is omitted, the ApiResource should represent all objects of the given type.
        '''
        ...


class _IApiResourceProxy:
    '''Represents a resource or collection of resources.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IApiResource"

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. ``authorization.k8s.io``).'''
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources

        Example::

            - "pods" or "pods/log"
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="resourceName")
    def resource_name(self) -> typing.Optional[builtins.str]:
        '''The unique, namespace-global, name of an object inside the Kubernetes cluster.

        If this is omitted, the ApiResource should represent all objects of the given type.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiResource).__jsii_proxy_class__ = lambda : _IApiResourceProxy


@jsii.interface(jsii_type="cdk8s-plus-23.INamespaceSelector")
class INamespaceSelector(constructs.IConstruct, typing_extensions.Protocol):
    '''Represents an object that can select namespaces.'''

    @jsii.member(jsii_name="toNamespaceSelectorConfig")
    def to_namespace_selector_config(self) -> "NamespaceSelectorConfig":
        '''Return the configuration of this selector.'''
        ...


class _INamespaceSelectorProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Represents an object that can select namespaces.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.INamespaceSelector"

    @jsii.member(jsii_name="toNamespaceSelectorConfig")
    def to_namespace_selector_config(self) -> "NamespaceSelectorConfig":
        '''Return the configuration of this selector.'''
        return typing.cast("NamespaceSelectorConfig", jsii.invoke(self, "toNamespaceSelectorConfig", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespaceSelector).__jsii_proxy_class__ = lambda : _INamespaceSelectorProxy


@jsii.interface(jsii_type="cdk8s-plus-23.INetworkPolicyPeer")
class INetworkPolicyPeer(constructs.IConstruct, typing_extensions.Protocol):
    '''Describes a peer to allow traffic to/from.'''

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> "NetworkPolicyPeerConfig":
        '''Return the configuration of this peer.'''
        ...

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional["IPodSelector"]:
        '''Convert the peer into a pod selector, if possible.'''
        ...


class _INetworkPolicyPeerProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Describes a peer to allow traffic to/from.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.INetworkPolicyPeer"

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> "NetworkPolicyPeerConfig":
        '''Return the configuration of this peer.'''
        return typing.cast("NetworkPolicyPeerConfig", jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional["IPodSelector"]:
        '''Convert the peer into a pod selector, if possible.'''
        return typing.cast(typing.Optional["IPodSelector"], jsii.invoke(self, "toPodSelector", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkPolicyPeer).__jsii_proxy_class__ = lambda : _INetworkPolicyPeerProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IPodSelector")
class IPodSelector(constructs.IConstruct, typing_extensions.Protocol):
    '''Represents an object that can select pods.'''

    @jsii.member(jsii_name="toPodSelectorConfig")
    def to_pod_selector_config(self) -> "PodSelectorConfig":
        '''Return the configuration of this selector.'''
        ...


class _IPodSelectorProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Represents an object that can select pods.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IPodSelector"

    @jsii.member(jsii_name="toPodSelectorConfig")
    def to_pod_selector_config(self) -> "PodSelectorConfig":
        '''Return the configuration of this selector.'''
        return typing.cast("PodSelectorConfig", jsii.invoke(self, "toPodSelectorConfig", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPodSelector).__jsii_proxy_class__ = lambda : _IPodSelectorProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IResource")
class IResource(constructs.IConstruct, typing_extensions.Protocol):
    '''Represents a resource.'''

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. "authorization.k8s.io").'''
        ...

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        '''The object's API version (e.g. "authorization.k8s.io/v1").'''
        ...

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        '''The object kind (e.g. "Deployment").'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The Kubernetes name of this resource.'''
        ...


class _IResourceProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Represents a resource.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IResource"

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. "authorization.k8s.io").'''
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        '''The object's API version (e.g. "authorization.k8s.io/v1").'''
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        '''The object kind (e.g. "Deployment").'''
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The Kubernetes name of this resource.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResource).__jsii_proxy_class__ = lambda : _IResourceProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IRole")
class IRole(IResource, typing_extensions.Protocol):
    '''A reference to any Role or ClusterRole.'''

    pass


class _IRoleProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    '''A reference to any Role or ClusterRole.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IRole"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRole).__jsii_proxy_class__ = lambda : _IRoleProxy


@jsii.interface(jsii_type="cdk8s-plus-23.ISecret")
class ISecret(IResource, typing_extensions.Protocol):
    pass


class _ISecretProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.ISecret"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecret).__jsii_proxy_class__ = lambda : _ISecretProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IServiceAccount")
class IServiceAccount(IResource, typing_extensions.Protocol):
    pass


class _IServiceAccountProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IServiceAccount"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceAccount).__jsii_proxy_class__ = lambda : _IServiceAccountProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IStorage")
class IStorage(constructs.IConstruct, typing_extensions.Protocol):
    '''Represents a piece of storage in the cluster.'''

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        ...


class _IStorageProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Represents a piece of storage in the cluster.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IStorage"

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast("Volume", jsii.invoke(self, "asVolume", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorage).__jsii_proxy_class__ = lambda : _IStorageProxy


@jsii.interface(jsii_type="cdk8s-plus-23.ISubject")
class ISubject(constructs.IConstruct, typing_extensions.Protocol):
    '''Represents an object that can be used as a role binding subject.'''

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> "SubjectConfiguration":
        '''Return the subject configuration.'''
        ...


class _ISubjectProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
):
    '''Represents an object that can be used as a role binding subject.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.ISubject"

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> "SubjectConfiguration":
        '''Return the subject configuration.'''
        return typing.cast("SubjectConfiguration", jsii.invoke(self, "toSubjectConfiguration", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubject).__jsii_proxy_class__ = lambda : _ISubjectProxy


@jsii.enum(jsii_type="cdk8s-plus-23.ImagePullPolicy")
class ImagePullPolicy(enum.Enum):
    ALWAYS = "ALWAYS"
    '''Every time the kubelet launches a container, the kubelet queries the container image registry to resolve the name to an image digest.

    If the kubelet has a container image with that exact
    digest cached locally, the kubelet uses its cached image; otherwise, the kubelet downloads
    (pulls) the image with the resolved digest, and uses that image to launch the container.

    Default is Always if ImagePullPolicy is omitted and either the image tag is :latest or
    the image tag is omitted.
    '''
    IF_NOT_PRESENT = "IF_NOT_PRESENT"
    '''The image is pulled only if it is not already present locally.

    Default is IfNotPresent if ImagePullPolicy is omitted and the image tag is present but
    not :latest
    '''
    NEVER = "NEVER"
    '''The image is assumed to exist locally.

    No attempt is made to pull the image.
    '''


class IngressBackend(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.IngressBackend"):
    '''The backend for an ingress path.'''

    @jsii.member(jsii_name="fromResource")
    @builtins.classmethod
    def from_resource(cls, resource: IResource) -> "IngressBackend":
        '''A Resource backend is an ObjectRef to another Kubernetes resource within the same namespace as the Ingress object.

        A common usage for a Resource backend is to ingress data to an object
        storage backend with static assets.

        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IngressBackend.from_resource)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast("IngressBackend", jsii.sinvoke(cls, "fromResource", [resource]))

    @jsii.member(jsii_name="fromService")
    @builtins.classmethod
    def from_service(
        cls,
        serv: "Service",
        *,
        port: typing.Optional[jsii.Number] = None,
    ) -> "IngressBackend":
        '''A Kubernetes ``Service`` to use as the backend for this path.

        :param serv: The service object.
        :param port: The port to use to access the service. - This option will fail if the service does not expose any ports. - If the service exposes multiple ports, this option must be specified. - If the service exposes a single port, this option is optional and if specified, it must be the same port exposed by the service. Default: - if the service exposes a single port, this port will be used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IngressBackend.from_service)
            check_type(argname="argument serv", value=serv, expected_type=type_hints["serv"])
        options = ServiceIngressBackendOptions(port=port)

        return typing.cast("IngressBackend", jsii.sinvoke(cls, "fromService", [serv, options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.IngressRule",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "host": "host",
        "path": "path",
        "path_type": "pathType",
    },
)
class IngressRule:
    def __init__(
        self,
        *,
        backend: IngressBackend,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> None:
        '''Represents the rules mapping the paths under a specified host to the related backend services.

        Incoming requests are first evaluated for a host match,
        then routed to the backend associated with the matching path.

        :param backend: Backend defines the referenced service endpoint to which the traffic will be forwarded to.
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. Default: - If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
        :param path: Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'. Default: - If unspecified, the path defaults to a catch all sending traffic to the backend.
        :param path_type: Specify how the path is matched against request paths. By default, path types will be matched by prefix.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IngressRule.__init__)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
        }
        if host is not None:
            self._values["host"] = host
        if path is not None:
            self._values["path"] = path
        if path_type is not None:
            self._values["path_type"] = path_type

    @builtins.property
    def backend(self) -> IngressBackend:
        '''Backend defines the referenced service endpoint to which the traffic will be forwarded to.'''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(IngressBackend, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host is the fully qualified domain name of a network host, as defined by RFC 3986.

        Note the following deviations from the "host" part of the URI as
        defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue
        can only apply to the IP in the Spec of the parent Ingress. 2. The ``:``
        delimiter is not respected because ports are not allowed. Currently the
        port of an Ingress is implicitly :80 for http and :443 for https. Both
        these may change in the future. Incoming requests are matched against the
        host before the IngressRuleValue.

        :default:

        - If the host is unspecified, the Ingress routes all traffic based
        on the specified IngressRuleValue.
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'.

        :default:

        - If unspecified, the path defaults to a catch all sending traffic
        to the backend.
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_type(self) -> typing.Optional[HttpIngressPathType]:
        '''Specify how the path is matched against request paths.

        By default, path
        types will be matched by prefix.

        :see: https://kubernetes.io/docs/concepts/services-networking/ingress/#path-types
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional[HttpIngressPathType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.IngressTls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret": "secret"},
)
class IngressTls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret: typing.Optional[ISecret] = None,
    ) -> None:
        '''Represents the TLS configuration mapping that is passed to the ingress controller for SSL termination.

        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the TLS Secret. Default: - If unspecified, it defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress.
        :param secret: Secret is the secret that contains the certificate and key used to terminate SSL traffic on 443. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Default: - If unspecified, it allows SSL routing based on SNI hostname.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IngressTls.__init__)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hosts are a list of hosts included in the TLS certificate.

        The values in
        this list must match the name/s used in the TLS Secret.

        :default:

        - If unspecified, it defaults to the wildcard host setting for
        the loadbalancer controller fulfilling this Ingress.
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret(self) -> typing.Optional[ISecret]:
        '''Secret is the secret that contains the certificate and key used to terminate SSL traffic on 443.

        If the SNI host in a listener conflicts with
        the "Host" header field used by an IngressRule, the SNI host is used for
        termination and value of the Host header is used for routing.

        :default: - If unspecified, it allows SSL routing based on SNI hostname.
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[ISecret], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LabelExpression(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.LabelExpression",
):
    '''Represents a query that can be performed against resources with labels.'''

    @jsii.member(jsii_name="doesNotExist")
    @builtins.classmethod
    def does_not_exist(cls, key: builtins.str) -> "LabelExpression":
        '''Requires label ``key`` to not exist.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelExpression.does_not_exist)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("LabelExpression", jsii.sinvoke(cls, "doesNotExist", [key]))

    @jsii.member(jsii_name="exists")
    @builtins.classmethod
    def exists(cls, key: builtins.str) -> "LabelExpression":
        '''Requires label ``key`` to exist.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelExpression.exists)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("LabelExpression", jsii.sinvoke(cls, "exists", [key]))

    @jsii.member(jsii_name="in")
    @builtins.classmethod
    def in_(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "LabelExpression":
        '''Requires value of label ``key`` to be one of ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelExpression.in_)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("LabelExpression", jsii.sinvoke(cls, "in", [key, values]))

    @jsii.member(jsii_name="notIn")
    @builtins.classmethod
    def not_in(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "LabelExpression":
        '''Requires value of label ``key`` to be none of ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelExpression.not_in)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("LabelExpression", jsii.sinvoke(cls, "notIn", [key, values]))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "values"))


class LabelSelector(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.LabelSelector"):
    '''Match a resource by labels.'''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(
        cls,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> "LabelSelector":
        '''
        :param expressions: Expression based label matchers.
        :param labels: Strict label matchers.
        '''
        options = LabelSelectorOptions(expressions=expressions, labels=labels)

        return typing.cast("LabelSelector", jsii.sinvoke(cls, "of", [options]))

    @jsii.member(jsii_name="isEmpty")
    def is_empty(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "isEmpty", []))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.LabelSelectorOptions",
    jsii_struct_bases=[],
    name_mapping={"expressions": "expressions", "labels": "labels"},
)
class LabelSelectorOptions:
    def __init__(
        self,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Options for ``LabelSelector.of``.

        :param expressions: Expression based label matchers.
        :param labels: Strict label matchers.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelSelectorOptions.__init__)
            check_type(argname="argument expressions", value=expressions, expected_type=type_hints["expressions"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expressions is not None:
            self._values["expressions"] = expressions
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def expressions(self) -> typing.Optional[typing.List[LabelExpression]]:
        '''Expression based label matchers.'''
        result = self._values.get("expressions")
        return typing.cast(typing.Optional[typing.List[LabelExpression]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Strict label matchers.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelSelectorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.LabelSelectorRequirement",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class LabelSelectorRequirement:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabelSelectorRequirement.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn, the values array
        must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic merge patch.
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelSelectorRequirement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LabeledNode(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.LabeledNode"):
    '''A node that is matched by label selectors.'''

    def __init__(self, label_selector: typing.Sequence["NodeLabelQuery"]) -> None:
        '''
        :param label_selector: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LabeledNode.__init__)
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
        jsii.create(self.__class__, self, [label_selector])

    @builtins.property
    @jsii.member(jsii_name="labelSelector")
    def label_selector(self) -> typing.List["NodeLabelQuery"]:
        return typing.cast(typing.List["NodeLabelQuery"], jsii.get(self, "labelSelector"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.MemoryResources",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit", "request": "request"},
)
class MemoryResources:
    def __init__(
        self,
        *,
        limit: typing.Optional[cdk8s.Size] = None,
        request: typing.Optional[cdk8s.Size] = None,
    ) -> None:
        '''Memory request and limit.

        :param limit: 
        :param request: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MemoryResources.__init__)
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if limit is not None:
            self._values["limit"] = limit
        if request is not None:
            self._values["request"] = request

    @builtins.property
    def limit(self) -> typing.Optional[cdk8s.Size]:
        result = self._values.get("limit")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def request(self) -> typing.Optional[cdk8s.Size]:
        result = self._values.get("request")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemoryResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.MountOptions",
    jsii_struct_bases=[],
    name_mapping={
        "propagation": "propagation",
        "read_only": "readOnly",
        "sub_path": "subPath",
        "sub_path_expr": "subPathExpr",
    },
)
class MountOptions:
    def __init__(
        self,
        *,
        propagation: typing.Optional["MountPropagation"] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for mounts.

        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountOptions.__init__)
            check_type(argname="argument propagation", value=propagation, expected_type=type_hints["propagation"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument sub_path", value=sub_path, expected_type=type_hints["sub_path"])
            check_type(argname="argument sub_path_expr", value=sub_path_expr, expected_type=type_hints["sub_path_expr"])
        self._values: typing.Dict[str, typing.Any] = {}
        if propagation is not None:
            self._values["propagation"] = propagation
        if read_only is not None:
            self._values["read_only"] = read_only
        if sub_path is not None:
            self._values["sub_path"] = sub_path
        if sub_path_expr is not None:
            self._values["sub_path_expr"] = sub_path_expr

    @builtins.property
    def propagation(self) -> typing.Optional["MountPropagation"]:
        '''Determines how mounts are propagated from the host to container and the other way around.

        When not set, MountPropagationNone is used.

        Mount propagation allows for sharing volumes mounted by a Container to
        other Containers in the same Pod, or even to other Pods on the same node.

        :default: MountPropagation.NONE
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional["MountPropagation"], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Mounted read-only if true, read-write otherwise (false or unspecified).

        Defaults to false.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sub_path(self) -> typing.Optional[builtins.str]:
        '''Path within the volume from which the container's volume should be mounted.).

        :default: "" the volume's root
        '''
        result = self._values.get("sub_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_path_expr(self) -> typing.Optional[builtins.str]:
        '''Expanded path within the volume from which the container's volume should be mounted.

        Behaves similarly to SubPath but environment variable references
        $(VAR_NAME) are expanded using the container's environment. Defaults to ""
        (volume's root).

        ``subPathExpr`` and ``subPath`` are mutually exclusive.

        :default: "" volume's root.
        '''
        result = self._values.get("sub_path_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.MountPropagation")
class MountPropagation(enum.Enum):
    NONE = "NONE"
    '''This volume mount will not receive any subsequent mounts that are mounted to this volume or any of its subdirectories by the host.

    In similar
    fashion, no mounts created by the Container will be visible on the host.

    This is the default mode.

    This mode is equal to ``private`` mount propagation as described in the Linux
    kernel documentation
    '''
    HOST_TO_CONTAINER = "HOST_TO_CONTAINER"
    '''This volume mount will receive all subsequent mounts that are mounted to this volume or any of its subdirectories.

    In other words, if the host mounts anything inside the volume mount, the
    Container will see it mounted there.

    Similarly, if any Pod with Bidirectional mount propagation to the same
    volume mounts anything there, the Container with HostToContainer mount
    propagation will see it.

    This mode is equal to ``rslave`` mount propagation as described in the Linux
    kernel documentation
    '''
    BIDIRECTIONAL = "BIDIRECTIONAL"
    '''This volume mount behaves the same the HostToContainer mount.

    In addition,
    all volume mounts created by the Container will be propagated back to the
    host and to all Containers of all Pods that use the same volume

    A typical use case for this mode is a Pod with a FlexVolume or CSI driver
    or a Pod that needs to mount something on the host using a hostPath volume.

    This mode is equal to ``rshared`` mount propagation as described in the Linux
    kernel documentation

    Caution: Bidirectional mount propagation can be dangerous. It can damage
    the host operating system and therefore it is allowed only in privileged
    Containers. Familiarity with Linux kernel behavior is strongly recommended.
    In addition, any volume mounts created by Containers in Pods must be
    destroyed (unmounted) by the Containers on termination.
    '''


class NamedNode(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.NamedNode"):
    '''A node that is matched by its name.'''

    def __init__(self, name: builtins.str) -> None:
        '''
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NamedNode.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        jsii.create(self.__class__, self, [name])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NamespaceSelectorConfig",
    jsii_struct_bases=[],
    name_mapping={"label_selector": "labelSelector", "names": "names"},
)
class NamespaceSelectorConfig:
    def __init__(
        self,
        *,
        label_selector: typing.Optional[LabelSelector] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Configuration for selecting namespaces.

        :param label_selector: A selector to select namespaces by labels.
        :param names: A list of names to select namespaces by names.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NamespaceSelectorConfig.__init__)
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument names", value=names, expected_type=type_hints["names"])
        self._values: typing.Dict[str, typing.Any] = {}
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if names is not None:
            self._values["names"] = names

    @builtins.property
    def label_selector(self) -> typing.Optional[LabelSelector]:
        '''A selector to select namespaces by labels.'''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional[LabelSelector], result)

    @builtins.property
    def names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of names to select namespaces by names.'''
        result = self._values.get("names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceSelectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INamespaceSelector, INetworkPolicyPeer)
class Namespaces(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.Namespaces",
):
    '''Represents a group of namespaces.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param expressions: -
        :param names: -
        :param labels: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Namespaces.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expressions", value=expressions, expected_type=type_hints["expressions"])
            check_type(argname="argument names", value=names, expected_type=type_hints["names"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        jsii.create(self.__class__, self, [scope, id, expressions, names, labels])

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls, scope: constructs.Construct, id: builtins.str) -> "Namespaces":
        '''Select all namespaces.

        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Namespaces.all)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("Namespaces", jsii.sinvoke(cls, "all", [scope, id]))

    @jsii.member(jsii_name="select")
    @builtins.classmethod
    def select(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "Namespaces":
        '''Select specific namespaces.

        :param scope: -
        :param id: -
        :param expressions: Namespaces must satisfy these selectors. The selectors query labels, just like the ``labels`` property, but they provide a more advanced matching mechanism. Default: - no selector requirements.
        :param labels: Labels the namespaces must have. This is equivalent to using an 'Is' selector. Default: - no strict labels requirements.
        :param names: Namespaces names must be one of these. Default: - no name requirements.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Namespaces.select)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = NamespacesSelectOptions(
            expressions=expressions, labels=labels, names=names
        )

        return typing.cast("Namespaces", jsii.sinvoke(cls, "select", [scope, id, options]))

    @jsii.member(jsii_name="toNamespaceSelectorConfig")
    def to_namespace_selector_config(self) -> NamespaceSelectorConfig:
        '''Return the configuration of this selector.

        :see: INamespaceSelector.toNamespaceSelectorConfig()
        '''
        return typing.cast(NamespaceSelectorConfig, jsii.invoke(self, "toNamespaceSelectorConfig", []))

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> "NetworkPolicyPeerConfig":
        '''Return the configuration of this peer.

        :see: INetworkPolicyPeer.toNetworkPolicyPeerConfig()
        '''
        return typing.cast("NetworkPolicyPeerConfig", jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional[IPodSelector]:
        '''Convert the peer into a pod selector, if possible.

        :see: INetworkPolicyPeer.toPodSelector()
        '''
        return typing.cast(typing.Optional[IPodSelector], jsii.invoke(self, "toPodSelector", []))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NamespacesSelectOptions",
    jsii_struct_bases=[],
    name_mapping={"expressions": "expressions", "labels": "labels", "names": "names"},
)
class NamespacesSelectOptions:
    def __init__(
        self,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for ``Namespaces.select``.

        :param expressions: Namespaces must satisfy these selectors. The selectors query labels, just like the ``labels`` property, but they provide a more advanced matching mechanism. Default: - no selector requirements.
        :param labels: Labels the namespaces must have. This is equivalent to using an 'Is' selector. Default: - no strict labels requirements.
        :param names: Namespaces names must be one of these. Default: - no name requirements.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NamespacesSelectOptions.__init__)
            check_type(argname="argument expressions", value=expressions, expected_type=type_hints["expressions"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument names", value=names, expected_type=type_hints["names"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expressions is not None:
            self._values["expressions"] = expressions
        if labels is not None:
            self._values["labels"] = labels
        if names is not None:
            self._values["names"] = names

    @builtins.property
    def expressions(self) -> typing.Optional[typing.List[LabelExpression]]:
        '''Namespaces must satisfy these selectors.

        The selectors query labels, just like the ``labels`` property, but they
        provide a more advanced matching mechanism.

        :default: - no selector requirements.
        '''
        result = self._values.get("expressions")
        return typing.cast(typing.Optional[typing.List[LabelExpression]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels the namespaces must have.

        This is equivalent to using an 'Is' selector.

        :default: - no strict labels requirements.
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Namespaces names must be one of these.

        :default: - no name requirements.
        '''
        result = self._values.get("names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespacesSelectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyAddEgressRuleOptions",
    jsii_struct_bases=[],
    name_mapping={"ports": "ports"},
)
class NetworkPolicyAddEgressRuleOptions:
    def __init__(
        self,
        *,
        ports: typing.Optional[typing.Sequence["NetworkPolicyPort"]] = None,
    ) -> None:
        '''Options for ``NetworkPolicy.addEgressRule``.

        :param ports: Ports the rule should allow outgoing traffic to. Default: - If the peer is a managed pod, take its ports. Otherwise, all ports are allowed.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyAddEgressRuleOptions.__init__)
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["NetworkPolicyPort"]]:
        '''Ports the rule should allow outgoing traffic to.

        :default: - If the peer is a managed pod, take its ports. Otherwise, all ports are allowed.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["NetworkPolicyPort"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyAddEgressRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INetworkPolicyPeer)
class NetworkPolicyIpBlock(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.NetworkPolicyIpBlock",
):
    '''Describes a particular CIDR (Ex.

    "192.168.1.1/24","2001:db9::/64") that is
    allowed to the pods matched by a network policy selector.
    The except entry describes CIDRs that should not be included within this rule.
    '''

    @jsii.member(jsii_name="anyIpv4")
    @builtins.classmethod
    def any_ipv4(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> "NetworkPolicyIpBlock":
        '''Any IPv4 address.

        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyIpBlock.any_ipv4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("NetworkPolicyIpBlock", jsii.sinvoke(cls, "anyIpv4", [scope, id]))

    @jsii.member(jsii_name="anyIpv6")
    @builtins.classmethod
    def any_ipv6(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> "NetworkPolicyIpBlock":
        '''Any IPv6 address.

        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyIpBlock.any_ipv6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("NetworkPolicyIpBlock", jsii.sinvoke(cls, "anyIpv6", [scope, id]))

    @jsii.member(jsii_name="ipv4")
    @builtins.classmethod
    def ipv4(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        cidr_ip: builtins.str,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "NetworkPolicyIpBlock":
        '''Create an IPv4 peer from a CIDR.

        :param scope: -
        :param id: -
        :param cidr_ip: -
        :param except_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyIpBlock.ipv4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument cidr_ip", value=cidr_ip, expected_type=type_hints["cidr_ip"])
            check_type(argname="argument except_", value=except_, expected_type=type_hints["except_"])
        return typing.cast("NetworkPolicyIpBlock", jsii.sinvoke(cls, "ipv4", [scope, id, cidr_ip, except_]))

    @jsii.member(jsii_name="ipv6")
    @builtins.classmethod
    def ipv6(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        cidr_ip: builtins.str,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "NetworkPolicyIpBlock":
        '''Create an IPv6 peer from a CIDR.

        :param scope: -
        :param id: -
        :param cidr_ip: -
        :param except_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyIpBlock.ipv6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument cidr_ip", value=cidr_ip, expected_type=type_hints["cidr_ip"])
            check_type(argname="argument except_", value=except_, expected_type=type_hints["except_"])
        return typing.cast("NetworkPolicyIpBlock", jsii.sinvoke(cls, "ipv6", [scope, id, cidr_ip, except_]))

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> "NetworkPolicyPeerConfig":
        '''Return the configuration of this peer.

        :see: INetworkPolicyPeer.toNetworkPolicyPeerConfig()
        '''
        return typing.cast("NetworkPolicyPeerConfig", jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional[IPodSelector]:
        '''Convert the peer into a pod selector, if possible.

        :see: INetworkPolicyPeer.toPodSelector()
        '''
        return typing.cast(typing.Optional[IPodSelector], jsii.invoke(self, "toPodSelector", []))

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        '''A string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64".'''
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="except")
    def except_(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64". Except values will be rejected if they are outside the CIDR range.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "except"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyPeerConfig",
    jsii_struct_bases=[],
    name_mapping={"ip_block": "ipBlock", "pod_selector": "podSelector"},
)
class NetworkPolicyPeerConfig:
    def __init__(
        self,
        *,
        ip_block: typing.Optional[NetworkPolicyIpBlock] = None,
        pod_selector: typing.Optional[typing.Union["PodSelectorConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''Configuration for network peers.

        A peer can either by an ip block, or a selection of pods, not both.

        :param ip_block: The ip block this peer represents.
        :param pod_selector: The pod selector this peer represents.
        '''
        if isinstance(pod_selector, dict):
            pod_selector = PodSelectorConfig(**pod_selector)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPeerConfig.__init__)
            check_type(argname="argument ip_block", value=ip_block, expected_type=type_hints["ip_block"])
            check_type(argname="argument pod_selector", value=pod_selector, expected_type=type_hints["pod_selector"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ip_block is not None:
            self._values["ip_block"] = ip_block
        if pod_selector is not None:
            self._values["pod_selector"] = pod_selector

    @builtins.property
    def ip_block(self) -> typing.Optional[NetworkPolicyIpBlock]:
        '''The ip block this peer represents.'''
        result = self._values.get("ip_block")
        return typing.cast(typing.Optional[NetworkPolicyIpBlock], result)

    @builtins.property
    def pod_selector(self) -> typing.Optional["PodSelectorConfig"]:
        '''The pod selector this peer represents.'''
        result = self._values.get("pod_selector")
        return typing.cast(typing.Optional["PodSelectorConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyPeerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyPort(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.NetworkPolicyPort",
):
    '''Describes a port to allow traffic on.'''

    @jsii.member(jsii_name="allTcp")
    @builtins.classmethod
    def all_tcp(cls) -> "NetworkPolicyPort":
        '''Any TCP traffic.'''
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "allTcp", []))

    @jsii.member(jsii_name="allUdp")
    @builtins.classmethod
    def all_udp(cls) -> "NetworkPolicyPort":
        '''Any UDP traffic.'''
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "allUdp", []))

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(
        cls,
        *,
        end_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional["NetworkProtocol"] = None,
    ) -> "NetworkPolicyPort":
        '''Custom port configuration.

        :param end_port: End port (relative to ``port``). Only applies if ``port`` is defined. Use this to specify a port range, rather that a specific one. Default: - not a port range.
        :param port: Specific port number. Default: - all ports are allowed.
        :param protocol: Protocol. Default: NetworkProtocol.TCP
        '''
        props = NetworkPolicyPortProps(end_port=end_port, port=port, protocol=protocol)

        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "of", [props]))

    @jsii.member(jsii_name="tcp")
    @builtins.classmethod
    def tcp(cls, port: jsii.Number) -> "NetworkPolicyPort":
        '''Distinct TCP ports.

        :param port: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPort.tcp)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "tcp", [port]))

    @jsii.member(jsii_name="tcpRange")
    @builtins.classmethod
    def tcp_range(
        cls,
        start_port: jsii.Number,
        end_port: jsii.Number,
    ) -> "NetworkPolicyPort":
        '''A TCP port range.

        :param start_port: -
        :param end_port: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPort.tcp_range)
            check_type(argname="argument start_port", value=start_port, expected_type=type_hints["start_port"])
            check_type(argname="argument end_port", value=end_port, expected_type=type_hints["end_port"])
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "tcpRange", [start_port, end_port]))

    @jsii.member(jsii_name="udp")
    @builtins.classmethod
    def udp(cls, port: jsii.Number) -> "NetworkPolicyPort":
        '''Distinct UDP ports.

        :param port: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPort.udp)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "udp", [port]))

    @jsii.member(jsii_name="udpRange")
    @builtins.classmethod
    def udp_range(
        cls,
        start_port: jsii.Number,
        end_port: jsii.Number,
    ) -> "NetworkPolicyPort":
        '''A UDP port range.

        :param start_port: -
        :param end_port: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPort.udp_range)
            check_type(argname="argument start_port", value=start_port, expected_type=type_hints["start_port"])
            check_type(argname="argument end_port", value=end_port, expected_type=type_hints["end_port"])
        return typing.cast("NetworkPolicyPort", jsii.sinvoke(cls, "udpRange", [start_port, end_port]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyPortProps",
    jsii_struct_bases=[],
    name_mapping={"end_port": "endPort", "port": "port", "protocol": "protocol"},
)
class NetworkPolicyPortProps:
    def __init__(
        self,
        *,
        end_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional["NetworkProtocol"] = None,
    ) -> None:
        '''Properties for ``NetworkPolicyPort``.

        :param end_port: End port (relative to ``port``). Only applies if ``port`` is defined. Use this to specify a port range, rather that a specific one. Default: - not a port range.
        :param port: Specific port number. Default: - all ports are allowed.
        :param protocol: Protocol. Default: NetworkProtocol.TCP
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyPortProps.__init__)
            check_type(argname="argument end_port", value=end_port, expected_type=type_hints["end_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {}
        if end_port is not None:
            self._values["end_port"] = end_port
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def end_port(self) -> typing.Optional[jsii.Number]:
        '''End port (relative to ``port``).

        Only applies if ``port`` is defined.
        Use this to specify a port range, rather that a specific one.

        :default: - not a port range.
        '''
        result = self._values.get("end_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specific port number.

        :default: - all ports are allowed.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional["NetworkProtocol"]:
        '''Protocol.

        :default: NetworkProtocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional["NetworkProtocol"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyPortProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyRule",
    jsii_struct_bases=[],
    name_mapping={"peer": "peer", "ports": "ports"},
)
class NetworkPolicyRule:
    def __init__(
        self,
        *,
        peer: INetworkPolicyPeer,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Describes a rule allowing traffic from / to pods matched by a network policy selector.

        :param peer: Peer this rule interacts with.
        :param ports: The ports of the rule. Default: - traffic is allowed on all ports.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyRule.__init__)
            check_type(argname="argument peer", value=peer, expected_type=type_hints["peer"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "peer": peer,
        }
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def peer(self) -> INetworkPolicyPeer:
        '''Peer this rule interacts with.'''
        result = self._values.get("peer")
        assert result is not None, "Required property 'peer' is missing"
        return typing.cast(INetworkPolicyPeer, result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[NetworkPolicyPort]]:
        '''The ports of the rule.

        :default: - traffic is allowed on all ports.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[NetworkPolicyPort]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyTraffic",
    jsii_struct_bases=[],
    name_mapping={"default": "default", "rules": "rules"},
)
class NetworkPolicyTraffic:
    def __init__(
        self,
        *,
        default: typing.Optional["NetworkPolicyTrafficDefault"] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[NetworkPolicyRule, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Describes how the network policy should configure egress / ingress traffic.

        :param default: Specifies the default behavior of the policy when no rules are defined. Default: - unset, the policy does not change the behavior.
        :param rules: List of rules to be applied to the selected pods. If empty, the behavior of the policy is dictated by the ``default`` property. Default: - no rules
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyTraffic.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def default(self) -> typing.Optional["NetworkPolicyTrafficDefault"]:
        '''Specifies the default behavior of the policy when no rules are defined.

        :default: - unset, the policy does not change the behavior.
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional["NetworkPolicyTrafficDefault"], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[NetworkPolicyRule]]:
        '''List of rules to be applied to the selected pods.

        If empty, the behavior of the policy is dictated by the ``default`` property.

        :default: - no rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[NetworkPolicyRule]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyTraffic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.NetworkPolicyTrafficDefault")
class NetworkPolicyTrafficDefault(enum.Enum):
    '''Default behaviors of network traffic in policies.'''

    DENY = "DENY"
    '''The policy denies all traffic.

    Since rules are additive, additional rules or policies can allow
    specific traffic.
    '''
    ALLOW = "ALLOW"
    '''The policy allows all traffic (either ingress or egress).

    Since rules are additive, no additional rule or policies can
    subsequently deny the traffic.
    '''


@jsii.enum(jsii_type="cdk8s-plus-23.NetworkProtocol")
class NetworkProtocol(enum.Enum):
    '''Network protocols.'''

    TCP = "TCP"
    '''TCP.'''
    UDP = "UDP"
    '''UDP.'''
    SCTP = "SCTP"
    '''SCTP.'''


class Node(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Node"):
    '''Represents a node in the cluster.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="labeled")
    @builtins.classmethod
    def labeled(cls, *label_selector: "NodeLabelQuery") -> LabeledNode:
        '''Match a node by its labels.

        :param label_selector: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Node.labeled)
            check_type(argname="argument label_selector", value=label_selector, expected_type=typing.Tuple[type_hints["label_selector"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(LabeledNode, jsii.sinvoke(cls, "labeled", [*label_selector]))

    @jsii.member(jsii_name="named")
    @builtins.classmethod
    def named(cls, node_name: builtins.str) -> NamedNode:
        '''Match a node by its name.

        :param node_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Node.named)
            check_type(argname="argument node_name", value=node_name, expected_type=type_hints["node_name"])
        return typing.cast(NamedNode, jsii.sinvoke(cls, "named", [node_name]))

    @jsii.member(jsii_name="tainted")
    @builtins.classmethod
    def tainted(cls, *taint_selector: "NodeTaintQuery") -> "TaintedNode":
        '''Match a node by its taints.

        :param taint_selector: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Node.tainted)
            check_type(argname="argument taint_selector", value=taint_selector, expected_type=typing.Tuple[type_hints["taint_selector"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("TaintedNode", jsii.sinvoke(cls, "tainted", [*taint_selector]))


class NodeLabelQuery(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.NodeLabelQuery"):
    '''Represents a query that can be performed against nodes with labels.'''

    @jsii.member(jsii_name="doesNotExist")
    @builtins.classmethod
    def does_not_exist(cls, key: builtins.str) -> "NodeLabelQuery":
        '''Requires label ``key`` to not exist.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.does_not_exist)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "doesNotExist", [key]))

    @jsii.member(jsii_name="exists")
    @builtins.classmethod
    def exists(cls, key: builtins.str) -> "NodeLabelQuery":
        '''Requires label ``key`` to exist.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.exists)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "exists", [key]))

    @jsii.member(jsii_name="gt")
    @builtins.classmethod
    def gt(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "NodeLabelQuery":
        '''Requires value of label ``key`` to greater than all elements in ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.gt)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "gt", [key, values]))

    @jsii.member(jsii_name="in")
    @builtins.classmethod
    def in_(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "NodeLabelQuery":
        '''Requires value of label ``key`` to be one of ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.in_)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "in", [key, values]))

    @jsii.member(jsii_name="is")
    @builtins.classmethod
    def is_(cls, key: builtins.str, value: builtins.str) -> "NodeLabelQuery":
        '''Requires value of label ``key`` to equal ``value``.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.is_)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "is", [key, value]))

    @jsii.member(jsii_name="lt")
    @builtins.classmethod
    def lt(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "NodeLabelQuery":
        '''Requires value of label ``key`` to less than all elements in ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.lt)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "lt", [key, values]))

    @jsii.member(jsii_name="notIn")
    @builtins.classmethod
    def not_in(
        cls,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> "NodeLabelQuery":
        '''Requires value of label ``key`` to be none of ``values``.

        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeLabelQuery.not_in)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("NodeLabelQuery", jsii.sinvoke(cls, "notIn", [key, values]))


class NodeTaintQuery(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.NodeTaintQuery"):
    '''Taint queries that can be perfomed against nodes.'''

    @jsii.member(jsii_name="any")
    @builtins.classmethod
    def any(cls) -> "NodeTaintQuery":
        '''Matches any taint.'''
        return typing.cast("NodeTaintQuery", jsii.sinvoke(cls, "any", []))

    @jsii.member(jsii_name="exists")
    @builtins.classmethod
    def exists(
        cls,
        key: builtins.str,
        *,
        effect: typing.Optional["TaintEffect"] = None,
        evict_after: typing.Optional[cdk8s.Duration] = None,
    ) -> "NodeTaintQuery":
        '''Matches a tain with any value of a specific key.

        :param key: -
        :param effect: The taint effect to match. Default: - all effects are matched.
        :param evict_after: How much time should a pod that tolerates the ``NO_EXECUTE`` effect be bound to the node. Only applies for the ``NO_EXECUTE`` effect. Default: - bound forever.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeTaintQuery.exists)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        options = NodeTaintQueryOptions(effect=effect, evict_after=evict_after)

        return typing.cast("NodeTaintQuery", jsii.sinvoke(cls, "exists", [key, options]))

    @jsii.member(jsii_name="is")
    @builtins.classmethod
    def is_(
        cls,
        key: builtins.str,
        value: builtins.str,
        *,
        effect: typing.Optional["TaintEffect"] = None,
        evict_after: typing.Optional[cdk8s.Duration] = None,
    ) -> "NodeTaintQuery":
        '''Matches a taint with a specific key and value.

        :param key: -
        :param value: -
        :param effect: The taint effect to match. Default: - all effects are matched.
        :param evict_after: How much time should a pod that tolerates the ``NO_EXECUTE`` effect be bound to the node. Only applies for the ``NO_EXECUTE`` effect. Default: - bound forever.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeTaintQuery.is_)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        options = NodeTaintQueryOptions(effect=effect, evict_after=evict_after)

        return typing.cast("NodeTaintQuery", jsii.sinvoke(cls, "is", [key, value, options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NodeTaintQueryOptions",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "evict_after": "evictAfter"},
)
class NodeTaintQueryOptions:
    def __init__(
        self,
        *,
        effect: typing.Optional["TaintEffect"] = None,
        evict_after: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Options for ``NodeTaintQuery``.

        :param effect: The taint effect to match. Default: - all effects are matched.
        :param evict_after: How much time should a pod that tolerates the ``NO_EXECUTE`` effect be bound to the node. Only applies for the ``NO_EXECUTE`` effect. Default: - bound forever.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NodeTaintQueryOptions.__init__)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument evict_after", value=evict_after, expected_type=type_hints["evict_after"])
        self._values: typing.Dict[str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if evict_after is not None:
            self._values["evict_after"] = evict_after

    @builtins.property
    def effect(self) -> typing.Optional["TaintEffect"]:
        '''The taint effect to match.

        :default: - all effects are matched.
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional["TaintEffect"], result)

    @builtins.property
    def evict_after(self) -> typing.Optional[cdk8s.Duration]:
        '''How much time should a pod that tolerates the ``NO_EXECUTE`` effect be bound to the node.

        Only applies for the ``NO_EXECUTE`` effect.

        :default: - bound forever.
        '''
        result = self._values.get("evict_after")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodeTaintQueryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IApiEndpoint)
class NonApiResource(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.NonApiResource"):
    '''Factory for creating non api resources.'''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, url: builtins.str) -> "NonApiResource":
        '''
        :param url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NonApiResource.of)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        return typing.cast("NonApiResource", jsii.sinvoke(cls, "of", [url]))

    @jsii.member(jsii_name="asApiResource")
    def as_api_resource(self) -> typing.Optional[IApiResource]:
        '''Return the IApiResource this object represents.'''
        return typing.cast(typing.Optional[IApiResource], jsii.invoke(self, "asApiResource", []))

    @jsii.member(jsii_name="asNonApiResource")
    def as_non_api_resource(self) -> typing.Optional[builtins.str]:
        '''Return the non resource url this object represents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "asNonApiResource", []))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PathMapping",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "mode": "mode"},
)
class PathMapping:
    def __init__(
        self,
        *,
        path: builtins.str,
        mode: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Maps a string key to a path within a volume.

        :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
        :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PathMapping.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def path(self) -> builtins.str:
        '''The relative path of the file to map the key to.

        May not be an absolute
        path. May not contain the path element '..'. May not start with the string
        '..'.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mode(self) -> typing.Optional[jsii.Number]:
        '''Optional: mode bits to use on this file, must be a value between 0 and 0777.

        If not specified, the volume defaultMode will be used. This might be
        in conflict with other options that affect the file mode, like fsGroup, and
        the result can be other mode bits set.
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PathMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PercentOrAbsolute(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.PercentOrAbsolute",
):
    '''Union like class repsenting either a ration in percents or an absolute number.'''

    @jsii.member(jsii_name="absolute")
    @builtins.classmethod
    def absolute(cls, num: jsii.Number) -> "PercentOrAbsolute":
        '''Absolute number.

        :param num: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PercentOrAbsolute.absolute)
            check_type(argname="argument num", value=num, expected_type=type_hints["num"])
        return typing.cast("PercentOrAbsolute", jsii.sinvoke(cls, "absolute", [num]))

    @jsii.member(jsii_name="percent")
    @builtins.classmethod
    def percent(cls, percent: jsii.Number) -> "PercentOrAbsolute":
        '''Percent ratio.

        :param percent: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PercentOrAbsolute.percent)
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        return typing.cast("PercentOrAbsolute", jsii.sinvoke(cls, "percent", [percent]))

    @jsii.member(jsii_name="isZero")
    def is_zero(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "isZero", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.enum(jsii_type="cdk8s-plus-23.PersistentVolumeAccessMode")
class PersistentVolumeAccessMode(enum.Enum):
    '''Access Modes.'''

    READ_WRITE_ONCE = "READ_WRITE_ONCE"
    '''The volume can be mounted as read-write by a single node.

    ReadWriteOnce access mode still can allow multiple pods to access
    the volume when the pods are running on the same node.
    '''
    READ_ONLY_MANY = "READ_ONLY_MANY"
    '''The volume can be mounted as read-only by many nodes.'''
    READ_WRITE_MANY = "READ_WRITE_MANY"
    '''The volume can be mounted as read-write by many nodes.'''
    READ_WRITE_ONCE_POD = "READ_WRITE_ONCE_POD"
    '''The volume can be mounted as read-write by a single Pod.

    Use ReadWriteOncePod access mode if you want to ensure that
    only one pod across whole cluster can read that PVC or write to it.
    This is only supported for CSI volumes and Kubernetes version 1.22+.
    '''


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PersistentVolumeClaimVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "read_only": "readOnly"},
)
class PersistentVolumeClaimVolumeOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for a PersistentVolumeClaim-based volume.

        :param name: The volume name. Default: - Derived from the PVC name.
        :param read_only: Will force the ReadOnly setting in VolumeMounts. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeClaimVolumeOptions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - Derived from the PVC name.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Will force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeClaimVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.PersistentVolumeMode")
class PersistentVolumeMode(enum.Enum):
    '''Volume Modes.'''

    FILE_SYSTEM = "FILE_SYSTEM"
    '''Volume is ounted into Pods into a directory.

    If the volume is backed by a block device and the device is empty,
    Kubernetes creates a filesystem on the device before mounting it
    for the first time.
    '''
    BLOCK = "BLOCK"
    '''Use a volume as a raw block device.

    Such volume is presented into a Pod as a block device,
    without any filesystem on it. This mode is useful to provide a Pod the fastest possible way
    to access a volume, without any filesystem layer between the Pod
    and the volume. On the other hand, the application running in
    the Pod must know how to handle a raw block device
    '''


@jsii.enum(jsii_type="cdk8s-plus-23.PersistentVolumeReclaimPolicy")
class PersistentVolumeReclaimPolicy(enum.Enum):
    '''Reclaim Policies.'''

    RETAIN = "RETAIN"
    '''The Retain reclaim policy allows for manual reclamation of the resource.

    When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the
    volume is considered "released". But it is not yet available for another claim
    because the previous claimant's data remains on the volume.
    An administrator can manually reclaim the volume with the following steps:

    1. Delete the PersistentVolume. The associated storage asset in external
       infrastructure (such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume) still exists after the PV is deleted.
    2. Manually clean up the data on the associated storage asset accordingly.
    3. Manually delete the associated storage asset.

    If you want to reuse the same storage asset, create a new PersistentVolume
    with the same storage asset definition.
    '''
    DELETE = "DELETE"
    '''For volume plugins that support the Delete reclaim policy, deletion removes both the PersistentVolume object from Kubernetes, as well as the associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume.

    Volumes that were dynamically provisioned inherit the reclaim policy of their StorageClass, which defaults to Delete.
    The administrator should configure the StorageClass according to users' expectations; otherwise,
    the PV must be edited or patched after it is created
    '''


class PodConnections(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.PodConnections"):
    '''Controls network isolation rules for inter-pod communication.'''

    def __init__(self, instance: "AbstractPod") -> None:
        '''
        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodConnections.__init__)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        jsii.create(self.__class__, self, [instance])

    @jsii.member(jsii_name="allowFrom")
    def allow_from(
        self,
        peer: INetworkPolicyPeer,
        *,
        isolation: typing.Optional["PodConnectionsIsolation"] = None,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Allow network traffic from the peer to this pod.

        By default, this will create an ingress network policy for this pod, and an egress
        network policy for the peer. This is required if both sides are already isolated.
        Use ``options.isolation`` to control this behavior.

        :param peer: -
        :param isolation: Which isolation should be applied to establish the connection. Default: - unset, isolates both the pod and the peer.
        :param ports: Ports to allow incoming traffic to. Default: - The pod ports.

        Example::

            // create only an egress policy that selects the 'web' pod to allow outgoing traffic
            // to the 'redis' pod. this requires the 'redis' pod to not be isolated for ingress.
            redis.connections.allowFrom(web, { isolation: Isolation.PEER })
            
            // create only an ingress policy that selects the 'redis' peer to allow incoming traffic
            // from the 'web' pod. this requires the 'web' pod to not be isolated for egress.
            redis.connections.allowFrom(web, { isolation: Isolation.POD })
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodConnections.allow_from)
            check_type(argname="argument peer", value=peer, expected_type=type_hints["peer"])
        options = PodConnectionsAllowFromOptions(isolation=isolation, ports=ports)

        return typing.cast(None, jsii.invoke(self, "allowFrom", [peer, options]))

    @jsii.member(jsii_name="allowTo")
    def allow_to(
        self,
        peer: INetworkPolicyPeer,
        *,
        isolation: typing.Optional["PodConnectionsIsolation"] = None,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Allow network traffic from this pod to the peer.

        By default, this will create an egress network policy for this pod, and an ingress
        network policy for the peer. This is required if both sides are already isolated.
        Use ``options.isolation`` to control this behavior.

        :param peer: -
        :param isolation: Which isolation should be applied to establish the connection. Default: - unset, isolates both the pod and the peer.
        :param ports: Ports to allow outgoing traffic to. Default: - If the peer is a managed pod, take its ports. Otherwise, all ports are allowed.

        Example::

            // create only an egress policy that selects the 'web' pod to allow outgoing traffic
            // to the 'redis' pod. this requires the 'redis' pod to not be isolated for ingress.
            web.connections.allowTo(redis, { isolation: Isolation.POD })
            
            // create only an ingress policy that selects the 'redis' peer to allow incoming traffic
            // from the 'web' pod. this requires the 'web' pod to not be isolated for egress.
            web.connections.allowTo(redis, { isolation: Isolation.PEER })
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodConnections.allow_to)
            check_type(argname="argument peer", value=peer, expected_type=type_hints["peer"])
        options = PodConnectionsAllowToOptions(isolation=isolation, ports=ports)

        return typing.cast(None, jsii.invoke(self, "allowTo", [peer, options]))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def _instance(self) -> "AbstractPod":
        return typing.cast("AbstractPod", jsii.get(self, "instance"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodConnectionsAllowFromOptions",
    jsii_struct_bases=[],
    name_mapping={"isolation": "isolation", "ports": "ports"},
)
class PodConnectionsAllowFromOptions:
    def __init__(
        self,
        *,
        isolation: typing.Optional["PodConnectionsIsolation"] = None,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Options for ``PodConnections.allowFrom``.

        :param isolation: Which isolation should be applied to establish the connection. Default: - unset, isolates both the pod and the peer.
        :param ports: Ports to allow incoming traffic to. Default: - The pod ports.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodConnectionsAllowFromOptions.__init__)
            check_type(argname="argument isolation", value=isolation, expected_type=type_hints["isolation"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {}
        if isolation is not None:
            self._values["isolation"] = isolation
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def isolation(self) -> typing.Optional["PodConnectionsIsolation"]:
        '''Which isolation should be applied to establish the connection.

        :default: - unset, isolates both the pod and the peer.
        '''
        result = self._values.get("isolation")
        return typing.cast(typing.Optional["PodConnectionsIsolation"], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[NetworkPolicyPort]]:
        '''Ports to allow incoming traffic to.

        :default: - The pod ports.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[NetworkPolicyPort]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodConnectionsAllowFromOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodConnectionsAllowToOptions",
    jsii_struct_bases=[],
    name_mapping={"isolation": "isolation", "ports": "ports"},
)
class PodConnectionsAllowToOptions:
    def __init__(
        self,
        *,
        isolation: typing.Optional["PodConnectionsIsolation"] = None,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Options for ``PodConnections.allowTo``.

        :param isolation: Which isolation should be applied to establish the connection. Default: - unset, isolates both the pod and the peer.
        :param ports: Ports to allow outgoing traffic to. Default: - If the peer is a managed pod, take its ports. Otherwise, all ports are allowed.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodConnectionsAllowToOptions.__init__)
            check_type(argname="argument isolation", value=isolation, expected_type=type_hints["isolation"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {}
        if isolation is not None:
            self._values["isolation"] = isolation
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def isolation(self) -> typing.Optional["PodConnectionsIsolation"]:
        '''Which isolation should be applied to establish the connection.

        :default: - unset, isolates both the pod and the peer.
        '''
        result = self._values.get("isolation")
        return typing.cast(typing.Optional["PodConnectionsIsolation"], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[NetworkPolicyPort]]:
        '''Ports to allow outgoing traffic to.

        :default: - If the peer is a managed pod, take its ports. Otherwise, all ports are allowed.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[NetworkPolicyPort]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodConnectionsAllowToOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.PodConnectionsIsolation")
class PodConnectionsIsolation(enum.Enum):
    '''Isolation determines which policies are created when allowing connections from a a pod / workload to peers.'''

    POD = "POD"
    '''Only creates network policies that select the pod.'''
    PEER = "PEER"
    '''Only creates network policies that select the peer.'''


class PodDns(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.PodDns"):
    '''Holds dns settings of the pod.'''

    def __init__(
        self,
        *,
        hostname: typing.Optional[builtins.str] = None,
        hostname_as_fqdn: typing.Optional[builtins.bool] = None,
        nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
        options: typing.Optional[typing.Sequence[typing.Union[DnsOption, typing.Dict[str, typing.Any]]]] = None,
        policy: typing.Optional[DnsPolicy] = None,
        searches: typing.Optional[typing.Sequence[builtins.str]] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: Specifies the hostname of the Pod. Default: - Set to a system-defined value.
        :param hostname_as_fqdn: If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default: false
        :param nameservers: A list of IP addresses that will be used as DNS servers for the Pod. There can be at most 3 IP addresses specified. When the policy is set to "NONE", the list must contain at least one IP address, otherwise this property is optional. The servers listed will be combined to the base nameservers generated from the specified DNS policy with duplicate addresses removed.
        :param options: List of objects where each object may have a name property (required) and a value property (optional). The contents in this property will be merged to the options generated from the specified DNS policy. Duplicate entries are removed.
        :param policy: Set DNS policy for the pod. If policy is set to ``None``, other configuration must be supplied. Default: DnsPolicy.CLUSTER_FIRST
        :param searches: A list of DNS search domains for hostname lookup in the Pod. When specified, the provided list will be merged into the base search domain names generated from the chosen DNS policy. Duplicate domain names are removed. Kubernetes allows for at most 6 search domains.
        :param subdomain: If specified, the fully qualified Pod hostname will be "...svc.". Default: - No subdomain.
        '''
        props = PodDnsProps(
            hostname=hostname,
            hostname_as_fqdn=hostname_as_fqdn,
            nameservers=nameservers,
            options=options,
            policy=policy,
            searches=searches,
            subdomain=subdomain,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addNameserver")
    def add_nameserver(self, *nameservers: builtins.str) -> None:
        '''Add a nameserver.

        :param nameservers: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodDns.add_nameserver)
            check_type(argname="argument nameservers", value=nameservers, expected_type=typing.Tuple[type_hints["nameservers"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addNameserver", [*nameservers]))

    @jsii.member(jsii_name="addOption")
    def add_option(self, *options: DnsOption) -> None:
        '''Add a custom option.

        :param options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodDns.add_option)
            check_type(argname="argument options", value=options, expected_type=typing.Tuple[type_hints["options"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addOption", [*options]))

    @jsii.member(jsii_name="addSearch")
    def add_search(self, *searches: builtins.str) -> None:
        '''Add a search domain.

        :param searches: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodDns.add_search)
            check_type(argname="argument searches", value=searches, expected_type=typing.Tuple[type_hints["searches"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addSearch", [*searches]))

    @builtins.property
    @jsii.member(jsii_name="hostnameAsFQDN")
    def hostname_as_fqdn(self) -> builtins.bool:
        '''Whether or not the pods hostname is set to its FQDN.'''
        return typing.cast(builtins.bool, jsii.get(self, "hostnameAsFQDN"))

    @builtins.property
    @jsii.member(jsii_name="nameservers")
    def nameservers(self) -> typing.List[builtins.str]:
        '''Nameservers defined for this pod.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameservers"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[DnsOption]:
        '''Custom dns options defined for this pod.'''
        return typing.cast(typing.List[DnsOption], jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> DnsPolicy:
        '''The DNS policy of this pod.'''
        return typing.cast(DnsPolicy, jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="searches")
    def searches(self) -> typing.List[builtins.str]:
        '''Search domains defined for this pod.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searches"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The configured hostname of the pod.

        Undefined means its set to a system-defined value.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="subdomain")
    def subdomain(self) -> typing.Optional[builtins.str]:
        '''The configured subdomain of the pod.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdomain"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodDnsProps",
    jsii_struct_bases=[],
    name_mapping={
        "hostname": "hostname",
        "hostname_as_fqdn": "hostnameAsFQDN",
        "nameservers": "nameservers",
        "options": "options",
        "policy": "policy",
        "searches": "searches",
        "subdomain": "subdomain",
    },
)
class PodDnsProps:
    def __init__(
        self,
        *,
        hostname: typing.Optional[builtins.str] = None,
        hostname_as_fqdn: typing.Optional[builtins.bool] = None,
        nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
        options: typing.Optional[typing.Sequence[typing.Union[DnsOption, typing.Dict[str, typing.Any]]]] = None,
        policy: typing.Optional[DnsPolicy] = None,
        searches: typing.Optional[typing.Sequence[builtins.str]] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for ``PodDns``.

        :param hostname: Specifies the hostname of the Pod. Default: - Set to a system-defined value.
        :param hostname_as_fqdn: If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default: false
        :param nameservers: A list of IP addresses that will be used as DNS servers for the Pod. There can be at most 3 IP addresses specified. When the policy is set to "NONE", the list must contain at least one IP address, otherwise this property is optional. The servers listed will be combined to the base nameservers generated from the specified DNS policy with duplicate addresses removed.
        :param options: List of objects where each object may have a name property (required) and a value property (optional). The contents in this property will be merged to the options generated from the specified DNS policy. Duplicate entries are removed.
        :param policy: Set DNS policy for the pod. If policy is set to ``None``, other configuration must be supplied. Default: DnsPolicy.CLUSTER_FIRST
        :param searches: A list of DNS search domains for hostname lookup in the Pod. When specified, the provided list will be merged into the base search domain names generated from the chosen DNS policy. Duplicate domain names are removed. Kubernetes allows for at most 6 search domains.
        :param subdomain: If specified, the fully qualified Pod hostname will be "...svc.". Default: - No subdomain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodDnsProps.__init__)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument hostname_as_fqdn", value=hostname_as_fqdn, expected_type=type_hints["hostname_as_fqdn"])
            check_type(argname="argument nameservers", value=nameservers, expected_type=type_hints["nameservers"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument searches", value=searches, expected_type=type_hints["searches"])
            check_type(argname="argument subdomain", value=subdomain, expected_type=type_hints["subdomain"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if hostname_as_fqdn is not None:
            self._values["hostname_as_fqdn"] = hostname_as_fqdn
        if nameservers is not None:
            self._values["nameservers"] = nameservers
        if options is not None:
            self._values["options"] = options
        if policy is not None:
            self._values["policy"] = policy
        if searches is not None:
            self._values["searches"] = searches
        if subdomain is not None:
            self._values["subdomain"] = subdomain

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the hostname of the Pod.

        :default: - Set to a system-defined value.
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname_as_fqdn(self) -> typing.Optional[builtins.bool]:
        '''If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default).

        In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname).
        In Windows containers, this means setting the registry value of hostname for the registry
        key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN.
        If a pod does not have FQDN, this has no effect.

        :default: false
        '''
        result = self._values.get("hostname_as_fqdn")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def nameservers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IP addresses that will be used as DNS servers for the Pod.

        There can be at most 3 IP addresses specified.
        When the policy is set to "NONE", the list must contain at least one IP address,
        otherwise this property is optional.
        The servers listed will be combined to the base nameservers generated from
        the specified DNS policy with duplicate addresses removed.
        '''
        result = self._values.get("nameservers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.List[DnsOption]]:
        '''List of objects where each object may have a name property (required) and a value property (optional).

        The contents in this property
        will be merged to the options generated from the specified DNS policy.
        Duplicate entries are removed.
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.List[DnsOption]], result)

    @builtins.property
    def policy(self) -> typing.Optional[DnsPolicy]:
        '''Set DNS policy for the pod.

        If policy is set to ``None``, other configuration must be supplied.

        :default: DnsPolicy.CLUSTER_FIRST
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[DnsPolicy], result)

    @builtins.property
    def searches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of DNS search domains for hostname lookup in the Pod.

        When specified, the provided list will be merged into the base
        search domain names generated from the chosen DNS policy.
        Duplicate domain names are removed.

        Kubernetes allows for at most 6 search domains.
        '''
        result = self._values.get("searches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subdomain(self) -> typing.Optional[builtins.str]:
        '''If specified, the fully qualified Pod hostname will be "...svc.".

        :default: - No subdomain.
        '''
        result = self._values.get("subdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodDnsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.PodManagementPolicy")
class PodManagementPolicy(enum.Enum):
    '''Controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down.

    The default policy is ``OrderedReady``, where pods are created in increasing order
    (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before
    continuing. When scaling down, the pods are removed in the opposite order.

    The alternative policy is ``Parallel`` which will create pods in parallel to match the
    desired scale without waiting, and on scale down will delete all pods at once.
    '''

    ORDERED_READY = "ORDERED_READY"
    PARALLEL = "PARALLEL"


class PodScheduling(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.PodScheduling"):
    '''Controls the pod scheduling strategy.'''

    def __init__(self, instance: "AbstractPod") -> None:
        '''
        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.__init__)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        jsii.create(self.__class__, self, [instance])

    @jsii.member(jsii_name="assign")
    def assign(self, node: NamedNode) -> None:
        '''Assign this pod a specific node by name.

        The scheduler ignores the Pod, and the kubelet on the named node
        tries to place the Pod on that node. Overrules any affinity rules of the pod.

        Some limitations of static assignment are:

        - If the named node does not exist, the Pod will not run, and in some
          cases may be automatically deleted.
        - If the named node does not have the resources to accommodate the Pod,
          the Pod will fail and its reason will indicate why, for example OutOfmemory or OutOfcpu.
        - Node names in cloud environments are not always predictable or stable.

        Will throw is the pod is already assigned to named node.

        Under the hood, this method utilizes the ``nodeName`` property.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.assign)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "assign", [node]))

    @jsii.member(jsii_name="attract")
    def attract(
        self,
        node: LabeledNode,
        *,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attract this pod to a node matched by selectors. You can select a node by using ``Node.labeled()``.

        Attracting to multiple nodes (i.e invoking this method multiple times) acts as
        an OR condition, meaning the pod will be assigned to either one of the nodes.

        Under the hood, this method utilizes the ``nodeAffinity`` property.

        :param node: -
        :param weight: Indicates the attraction is optional (soft), with this weight score. Default: - no weight. assignment is assumed to be required (hard).

        :see: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.attract)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        options = PodSchedulingAttractOptions(weight=weight)

        return typing.cast(None, jsii.invoke(self, "attract", [node, options]))

    @jsii.member(jsii_name="colocate")
    def colocate(
        self,
        selector: IPodSelector,
        *,
        topology: typing.Optional["Topology"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Co-locate this pod with a scheduling selection.

        A selection can be one of:

        - An instance of a ``Pod``.
        - An instance of a ``Workload`` (e.g ``Deployment``, ``StatefulSet``).
        - An un-managed pod that can be selected via ``Pods.select()``.

        Co-locating with multiple selections ((i.e invoking this method multiple times)) acts as
        an AND condition. meaning the pod will be assigned to a node that satisfies all
        selections (i.e runs at least one pod that satisifies each selection).

        Under the hood, this method utilizes the ``podAffinity`` property.

        :param selector: -
        :param topology: Which topology to coloate on. Default: - Topology.HOSTNAME
        :param weight: Indicates the co-location is optional (soft), with this weight score. Default: - no weight. co-location is assumed to be required (hard).

        :see: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.colocate)
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        options = PodSchedulingColocateOptions(topology=topology, weight=weight)

        return typing.cast(None, jsii.invoke(self, "colocate", [selector, options]))

    @jsii.member(jsii_name="separate")
    def separate(
        self,
        selector: IPodSelector,
        *,
        topology: typing.Optional["Topology"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Seperate this pod from a scheduling selection.

        A selection can be one of:

        - An instance of a ``Pod``.
        - An instance of a ``Workload`` (e.g ``Deployment``, ``StatefulSet``).
        - An un-managed pod that can be selected via ``Pods.select()``.

        Seperating from multiple selections acts as an AND condition. meaning the pod
        will not be assigned to a node that satisfies all selections (i.e runs at least one pod that satisifies each selection).

        Under the hood, this method utilizes the ``podAntiAffinity`` property.

        :param selector: -
        :param topology: Which topology to separate on. Default: - Topology.HOSTNAME
        :param weight: Indicates the separation is optional (soft), with this weight score. Default: - no weight. separation is assumed to be required (hard).

        :see: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.separate)
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        options = PodSchedulingSeparateOptions(topology=topology, weight=weight)

        return typing.cast(None, jsii.invoke(self, "separate", [selector, options]))

    @jsii.member(jsii_name="tolerate")
    def tolerate(self, node: "TaintedNode") -> None:
        '''Allow this pod to tolerate taints matching these tolerations.

        You can put multiple taints on the same node and multiple tolerations on the same pod.
        The way Kubernetes processes multiple taints and tolerations is like a filter: start with
        all of a node's taints, then ignore the ones for which the pod has a matching toleration;
        the remaining un-ignored taints have the indicated effects on the pod. In particular:

        - if there is at least one un-ignored taint with effect NoSchedule then Kubernetes will
          not schedule the pod onto that node
        - if there is no un-ignored taint with effect NoSchedule but there is at least one un-ignored
          taint with effect PreferNoSchedule then Kubernetes will try to not schedule the pod onto the node
        - if there is at least one un-ignored taint with effect NoExecute then the pod will be evicted from
          the node (if it is already running on the node), and will not be scheduled onto the node (if it is
          not yet running on the node).

        Under the hood, this method utilizes the ``tolerations`` property.

        :param node: -

        :see: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodScheduling.tolerate)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "tolerate", [node]))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def _instance(self) -> "AbstractPod":
        return typing.cast("AbstractPod", jsii.get(self, "instance"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodSchedulingAttractOptions",
    jsii_struct_bases=[],
    name_mapping={"weight": "weight"},
)
class PodSchedulingAttractOptions:
    def __init__(self, *, weight: typing.Optional[jsii.Number] = None) -> None:
        '''Options for ``PodScheduling.attract``.

        :param weight: Indicates the attraction is optional (soft), with this weight score. Default: - no weight. assignment is assumed to be required (hard).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSchedulingAttractOptions.__init__)
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Indicates the attraction is optional (soft), with this weight score.

        :default: - no weight. assignment is assumed to be required (hard).
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSchedulingAttractOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodSchedulingColocateOptions",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology", "weight": "weight"},
)
class PodSchedulingColocateOptions:
    def __init__(
        self,
        *,
        topology: typing.Optional["Topology"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``PodScheduling.colocate``.

        :param topology: Which topology to coloate on. Default: - Topology.HOSTNAME
        :param weight: Indicates the co-location is optional (soft), with this weight score. Default: - no weight. co-location is assumed to be required (hard).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSchedulingColocateOptions.__init__)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if topology is not None:
            self._values["topology"] = topology
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def topology(self) -> typing.Optional["Topology"]:
        '''Which topology to coloate on.

        :default: - Topology.HOSTNAME
        '''
        result = self._values.get("topology")
        return typing.cast(typing.Optional["Topology"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Indicates the co-location is optional (soft), with this weight score.

        :default: - no weight. co-location is assumed to be required (hard).
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSchedulingColocateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodSchedulingSeparateOptions",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology", "weight": "weight"},
)
class PodSchedulingSeparateOptions:
    def __init__(
        self,
        *,
        topology: typing.Optional["Topology"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``PodScheduling.separate``.

        :param topology: Which topology to separate on. Default: - Topology.HOSTNAME
        :param weight: Indicates the separation is optional (soft), with this weight score. Default: - no weight. separation is assumed to be required (hard).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSchedulingSeparateOptions.__init__)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if topology is not None:
            self._values["topology"] = topology
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def topology(self) -> typing.Optional["Topology"]:
        '''Which topology to separate on.

        :default: - Topology.HOSTNAME
        '''
        result = self._values.get("topology")
        return typing.cast(typing.Optional["Topology"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Indicates the separation is optional (soft), with this weight score.

        :default: - no weight. separation is assumed to be required (hard).
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSchedulingSeparateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.PodSecurityContext",
):
    '''Holds pod-level security attributes and common container settings.'''

    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[FsGroupChangePolicy] = None,
        group: typing.Optional[jsii.Number] = None,
        sysctls: typing.Optional[typing.Sequence[typing.Union["Sysctl", typing.Dict[str, typing.Any]]]] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param fs_group: Modify the ownership and permissions of pod volumes to this GID. Default: - Volume ownership is not changed.
        :param fs_group_change_policy: Defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Default: FsGroupChangePolicy.ALWAYS
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Default: - No sysctls
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        props = PodSecurityContextProps(
            ensure_non_root=ensure_non_root,
            fs_group=fs_group,
            fs_group_change_policy=fs_group_change_policy,
            group=group,
            sysctls=sysctls,
            user=user,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="ensureNonRoot")
    def ensure_non_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "ensureNonRoot"))

    @builtins.property
    @jsii.member(jsii_name="fsGroupChangePolicy")
    def fs_group_change_policy(self) -> FsGroupChangePolicy:
        return typing.cast(FsGroupChangePolicy, jsii.get(self, "fsGroupChangePolicy"))

    @builtins.property
    @jsii.member(jsii_name="sysctls")
    def sysctls(self) -> typing.List["Sysctl"]:
        return typing.cast(typing.List["Sysctl"], jsii.get(self, "sysctls"))

    @builtins.property
    @jsii.member(jsii_name="fsGroup")
    def fs_group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsGroup"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "user"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodSecurityContextProps",
    jsii_struct_bases=[],
    name_mapping={
        "ensure_non_root": "ensureNonRoot",
        "fs_group": "fsGroup",
        "fs_group_change_policy": "fsGroupChangePolicy",
        "group": "group",
        "sysctls": "sysctls",
        "user": "user",
    },
)
class PodSecurityContextProps:
    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[FsGroupChangePolicy] = None,
        group: typing.Optional[jsii.Number] = None,
        sysctls: typing.Optional[typing.Sequence[typing.Union["Sysctl", typing.Dict[str, typing.Any]]]] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``PodSecurityContext``.

        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param fs_group: Modify the ownership and permissions of pod volumes to this GID. Default: - Volume ownership is not changed.
        :param fs_group_change_policy: Defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Default: FsGroupChangePolicy.ALWAYS
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Default: - No sysctls
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityContextProps.__init__)
            check_type(argname="argument ensure_non_root", value=ensure_non_root, expected_type=type_hints["ensure_non_root"])
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument fs_group_change_policy", value=fs_group_change_policy, expected_type=type_hints["fs_group_change_policy"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ensure_non_root is not None:
            self._values["ensure_non_root"] = ensure_non_root
        if fs_group is not None:
            self._values["fs_group"] = fs_group
        if fs_group_change_policy is not None:
            self._values["fs_group_change_policy"] = fs_group_change_policy
        if group is not None:
            self._values["group"] = group
        if sysctls is not None:
            self._values["sysctls"] = sysctls
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def ensure_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it does
        not run as UID 0 (root) and fail to start the container if it does.

        :default: false
        '''
        result = self._values.get("ensure_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fs_group(self) -> typing.Optional[jsii.Number]:
        '''Modify the ownership and permissions of pod volumes to this GID.

        :default: - Volume ownership is not changed.
        '''
        result = self._values.get("fs_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_group_change_policy(self) -> typing.Optional[FsGroupChangePolicy]:
        '''Defines behavior of changing ownership and permission of the volume before being exposed inside Pod.

        This field will only apply to volume types which support fsGroup based ownership(and permissions).
        It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir.

        :default: FsGroupChangePolicy.ALWAYS
        '''
        result = self._values.get("fs_group_change_policy")
        return typing.cast(typing.Optional[FsGroupChangePolicy], result)

    @builtins.property
    def group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        :default: - Group configured by container runtime
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sysctls(self) -> typing.Optional[typing.List["Sysctl"]]:
        '''Sysctls hold a list of namespaced sysctls used for the pod.

        Pods with unsupported sysctls (by the container runtime) might fail to launch.

        :default: - No sysctls
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.List["Sysctl"]], result)

    @builtins.property
    def user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        :default: - User specified in image metadata
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityContextProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodSelectorConfig",
    jsii_struct_bases=[],
    name_mapping={"label_selector": "labelSelector", "namespaces": "namespaces"},
)
class PodSelectorConfig:
    def __init__(
        self,
        *,
        label_selector: LabelSelector,
        namespaces: typing.Optional[typing.Union[NamespaceSelectorConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''Configuration for selecting pods, optionally in particular namespaces.

        :param label_selector: A selector to select pods by labels.
        :param namespaces: Configuration for selecting which namepsaces are the pods allowed to be in.
        '''
        if isinstance(namespaces, dict):
            namespaces = NamespaceSelectorConfig(**namespaces)
        if __debug__:
            type_hints = typing.get_type_hints(PodSelectorConfig.__init__)
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[str, typing.Any] = {
            "label_selector": label_selector,
        }
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def label_selector(self) -> LabelSelector:
        '''A selector to select pods by labels.'''
        result = self._values.get("label_selector")
        assert result is not None, "Required property 'label_selector' is missing"
        return typing.cast(LabelSelector, result)

    @builtins.property
    def namespaces(self) -> typing.Optional[NamespaceSelectorConfig]:
        '''Configuration for selecting which namepsaces are the pods allowed to be in.'''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[NamespaceSelectorConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSelectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodSelector)
class Pods(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.Pods",
):
    '''Represents a group of pods.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespaces: typing.Optional[INamespaceSelector] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param expressions: -
        :param labels: -
        :param namespaces: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Pods.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expressions", value=expressions, expected_type=type_hints["expressions"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        jsii.create(self.__class__, self, [scope, id, expressions, labels, namespaces])

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        namespaces: typing.Optional[Namespaces] = None,
    ) -> "Pods":
        '''Select all pods.

        :param scope: -
        :param id: -
        :param namespaces: Namespaces the pods are allowed to be in. Use ``Namespaces.all()`` to allow all namespaces. Default: - unset, implies the namespace of the resource this selection is used in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Pods.all)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = PodsAllOptions(namespaces=namespaces)

        return typing.cast("Pods", jsii.sinvoke(cls, "all", [scope, id, options]))

    @jsii.member(jsii_name="select")
    @builtins.classmethod
    def select(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespaces: typing.Optional[Namespaces] = None,
    ) -> "Pods":
        '''Select pods in the cluster with various selectors.

        :param scope: -
        :param id: -
        :param expressions: Expressions the pods must satisify. Default: - no expressions requirements.
        :param labels: Labels the pods must have. Default: - no strict labels requirements.
        :param namespaces: Namespaces the pods are allowed to be in. Use ``Namespaces.all()`` to allow all namespaces. Default: - unset, implies the namespace of the resource this selection is used in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Pods.select)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = PodsSelectOptions(
            expressions=expressions, labels=labels, namespaces=namespaces
        )

        return typing.cast("Pods", jsii.sinvoke(cls, "select", [scope, id, options]))

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> NetworkPolicyPeerConfig:
        '''
        :see: INetworkPolicyPeer.toNetworkPolicyPeerConfig()
        '''
        return typing.cast(NetworkPolicyPeerConfig, jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional[IPodSelector]:
        '''
        :see: INetworkPolicyPeer.toPodSelector()
        '''
        return typing.cast(typing.Optional[IPodSelector], jsii.invoke(self, "toPodSelector", []))

    @jsii.member(jsii_name="toPodSelectorConfig")
    def to_pod_selector_config(self) -> PodSelectorConfig:
        '''Return the configuration of this selector.

        :see: IPodSelector.toPodSelectorConfig()
        '''
        return typing.cast(PodSelectorConfig, jsii.invoke(self, "toPodSelectorConfig", []))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodsAllOptions",
    jsii_struct_bases=[],
    name_mapping={"namespaces": "namespaces"},
)
class PodsAllOptions:
    def __init__(self, *, namespaces: typing.Optional[Namespaces] = None) -> None:
        '''Options for ``Pods.all``.

        :param namespaces: Namespaces the pods are allowed to be in. Use ``Namespaces.all()`` to allow all namespaces. Default: - unset, implies the namespace of the resource this selection is used in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodsAllOptions.__init__)
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[str, typing.Any] = {}
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def namespaces(self) -> typing.Optional[Namespaces]:
        '''Namespaces the pods are allowed to be in.

        Use ``Namespaces.all()`` to allow all namespaces.

        :default: - unset, implies the namespace of the resource this selection is used in.
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[Namespaces], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodsAllOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodsSelectOptions",
    jsii_struct_bases=[],
    name_mapping={
        "expressions": "expressions",
        "labels": "labels",
        "namespaces": "namespaces",
    },
)
class PodsSelectOptions:
    def __init__(
        self,
        *,
        expressions: typing.Optional[typing.Sequence[LabelExpression]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespaces: typing.Optional[Namespaces] = None,
    ) -> None:
        '''Options for ``Pods.select``.

        :param expressions: Expressions the pods must satisify. Default: - no expressions requirements.
        :param labels: Labels the pods must have. Default: - no strict labels requirements.
        :param namespaces: Namespaces the pods are allowed to be in. Use ``Namespaces.all()`` to allow all namespaces. Default: - unset, implies the namespace of the resource this selection is used in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodsSelectOptions.__init__)
            check_type(argname="argument expressions", value=expressions, expected_type=type_hints["expressions"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expressions is not None:
            self._values["expressions"] = expressions
        if labels is not None:
            self._values["labels"] = labels
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def expressions(self) -> typing.Optional[typing.List[LabelExpression]]:
        '''Expressions the pods must satisify.

        :default: - no expressions requirements.
        '''
        result = self._values.get("expressions")
        return typing.cast(typing.Optional[typing.List[LabelExpression]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels the pods must have.

        :default: - no strict labels requirements.
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[Namespaces]:
        '''Namespaces the pods are allowed to be in.

        Use ``Namespaces.all()`` to allow all namespaces.

        :default: - unset, implies the namespace of the resource this selection is used in.
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[Namespaces], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodsSelectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Probe(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Probe"):
    '''Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.'''

    @jsii.member(jsii_name="fromCommand")
    @builtins.classmethod
    def from_command(
        cls,
        command: typing.Sequence[builtins.str],
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based on a command which is executed within the container.

        :param command: The command to execute.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Probe.from_command)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        options = CommandProbeOptions(
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromCommand", [command, options]))

    @jsii.member(jsii_name="fromHttpGet")
    @builtins.classmethod
    def from_http_get(
        cls,
        path: builtins.str,
        *,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[ConnectionScheme] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based on an HTTP GET request to the IP address of the container.

        :param path: The URL path to hit.
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        :param scheme: Scheme to use for connecting to the host (HTTP or HTTPS). Default: ConnectionScheme.HTTP
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Probe.from_http_get)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = HttpGetProbeOptions(
            port=port,
            scheme=scheme,
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromHttpGet", [path, options]))

    @jsii.member(jsii_name="fromTcpSocket")
    @builtins.classmethod
    def from_tcp_socket(
        cls,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based opening a connection to a TCP socket on the container.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        options = TcpSocketProbeOptions(
            host=host,
            port=port,
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromTcpSocket", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ProbeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ProbeOptions:
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Probe options.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProbeOptions.__init__)
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.Protocol")
class Protocol(enum.Enum):
    '''Network protocols.'''

    TCP = "TCP"
    '''TCP.'''
    UDP = "UDP"
    '''UDP.'''
    SCTP = "SCTP"
    '''SCTP.'''


@jsii.implements(IResource, IApiResource, IApiEndpoint)
class Resource(
    constructs.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk8s-plus-23.Resource",
):
    '''Base class for all Kubernetes objects in stdk8s.

    Represents a single
    resource.
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Resource.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="asApiResource")
    def as_api_resource(self) -> typing.Optional[IApiResource]:
        '''Return the IApiResource this object represents.'''
        return typing.cast(typing.Optional[IApiResource], jsii.invoke(self, "asApiResource", []))

    @jsii.member(jsii_name="asNonApiResource")
    def as_non_api_resource(self) -> typing.Optional[builtins.str]:
        '''Return the non resource url this object represents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "asNonApiResource", []))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. "authorization.k8s.io").'''
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    @abc.abstractmethod
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        '''The object's API version (e.g. "authorization.k8s.io/v1").'''
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        '''The object kind (e.g. "Deployment").'''
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this API object.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "ResourcePermissions":
        return typing.cast("ResourcePermissions", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    @abc.abstractmethod
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceName")
    def resource_name(self) -> typing.Optional[builtins.str]:
        '''The unique, namespace-global, name of an object inside the Kubernetes cluster.

        If this is omitted, the ApiResource should represent all objects of the given type.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceName"))


class _ResourceProxy(Resource):
    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.'''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Resource).__jsii_proxy_class__ = lambda : _ResourceProxy


@jsii.enum(jsii_type="cdk8s-plus-23.ResourceFieldPaths")
class ResourceFieldPaths(enum.Enum):
    CPU_LIMIT = "CPU_LIMIT"
    '''CPU limit of the container.'''
    MEMORY_LIMIT = "MEMORY_LIMIT"
    '''Memory limit of the container.'''
    CPU_REQUEST = "CPU_REQUEST"
    '''CPU request of the container.'''
    MEMORY_REQUEST = "MEMORY_REQUEST"
    '''Memory request of the container.'''
    STORAGE_LIMIT = "STORAGE_LIMIT"
    '''Ephemeral storage limit of the container.'''
    STORAGE_REQUEST = "STORAGE_REQUEST"
    '''Ephemeral storage request of the container.'''


class ResourcePermissions(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ResourcePermissions",
):
    '''Controls permissions for operations on resources.'''

    def __init__(self, instance: Resource) -> None:
        '''
        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ResourcePermissions.__init__)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        jsii.create(self.__class__, self, [instance])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, *subjects: ISubject) -> "RoleBinding":
        '''Grants the list of subjects permissions to read this resource.

        :param subjects: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ResourcePermissions.grant_read)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("RoleBinding", jsii.invoke(self, "grantRead", [*subjects]))

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, *subjects: ISubject) -> "RoleBinding":
        '''Grants the list of subjects permissions to read and write this resource.

        :param subjects: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ResourcePermissions.grant_read_write)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("RoleBinding", jsii.invoke(self, "grantReadWrite", [*subjects]))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def _instance(self) -> Resource:
        return typing.cast(Resource, jsii.get(self, "instance"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ResourceProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class ResourceProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''Initialization properties for resources.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ResourceProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.RestartPolicy")
class RestartPolicy(enum.Enum):
    '''Restart policy for all containers within the pod.'''

    ALWAYS = "ALWAYS"
    '''Always restart the pod after it exits.'''
    ON_FAILURE = "ON_FAILURE"
    '''Only restart if the pod exits with a non-zero exit code.'''
    NEVER = "NEVER"
    '''Never restart the pod.'''


@jsii.implements(IRole)
class Role(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Role"):
    '''Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rules: typing.Optional[typing.Sequence[typing.Union["RolePolicyRule", typing.Dict[str, typing.Any]]]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rules: A list of rules the role should allow. Default: []
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RoleProps(rules=rules, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromRoleName")
    @builtins.classmethod
    def from_role_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> IRole:
        '''Imports a role from the cluster as a reference.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.from_role_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IRole, jsii.sinvoke(cls, "fromRoleName", [scope, id, name]))

    @jsii.member(jsii_name="allow")
    def allow(
        self,
        verbs: typing.Sequence[builtins.str],
        *resources: IApiResource,
    ) -> None:
        '''Add permission to perform a list of HTTP verbs on a collection of resources.

        :param verbs: -
        :param resources: The resource(s) to apply to.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow)
            check_type(argname="argument verbs", value=verbs, expected_type=type_hints["verbs"])
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allow", [verbs, *resources]))

    @jsii.member(jsii_name="allowCreate")
    def allow_create(self, *resources: IApiResource) -> None:
        '''Add "create" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_create)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowCreate", [*resources]))

    @jsii.member(jsii_name="allowDelete")
    def allow_delete(self, *resources: IApiResource) -> None:
        '''Add "delete" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_delete)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowDelete", [*resources]))

    @jsii.member(jsii_name="allowDeleteCollection")
    def allow_delete_collection(self, *resources: IApiResource) -> None:
        '''Add "deletecollection" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_delete_collection)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowDeleteCollection", [*resources]))

    @jsii.member(jsii_name="allowGet")
    def allow_get(self, *resources: IApiResource) -> None:
        '''Add "get" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_get)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowGet", [*resources]))

    @jsii.member(jsii_name="allowList")
    def allow_list(self, *resources: IApiResource) -> None:
        '''Add "list" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_list)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowList", [*resources]))

    @jsii.member(jsii_name="allowPatch")
    def allow_patch(self, *resources: IApiResource) -> None:
        '''Add "patch" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_patch)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowPatch", [*resources]))

    @jsii.member(jsii_name="allowRead")
    def allow_read(self, *resources: IApiResource) -> None:
        '''Add "get", "list", and "watch" permissions for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_read)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowRead", [*resources]))

    @jsii.member(jsii_name="allowReadWrite")
    def allow_read_write(self, *resources: IApiResource) -> None:
        '''Add "get", "list", "watch", "create", "update", "patch", "delete", and "deletecollection" permissions for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_read_write)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowReadWrite", [*resources]))

    @jsii.member(jsii_name="allowUpdate")
    def allow_update(self, *resources: IApiResource) -> None:
        '''Add "update" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_update)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowUpdate", [*resources]))

    @jsii.member(jsii_name="allowWatch")
    def allow_watch(self, *resources: IApiResource) -> None:
        '''Add "watch" permission for the resources.

        :param resources: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.allow_watch)
            check_type(argname="argument resources", value=resources, expected_type=typing.Tuple[type_hints["resources"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowWatch", [*resources]))

    @jsii.member(jsii_name="bind")
    def bind(self, *subjects: ISubject) -> "RoleBinding":
        '''Create a RoleBinding that binds the permissions in this Role to a list of subjects, that will only apply this role's namespace.

        :param subjects: a list of subjects to bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Role.bind)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("RoleBinding", jsii.invoke(self, "bind", [*subjects]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.List["RolePolicyRule"]:
        '''Rules associaated with this Role.

        Returns a copy, use ``allow`` to add rules.
        '''
        return typing.cast(typing.List["RolePolicyRule"], jsii.get(self, "rules"))


class RoleBinding(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.RoleBinding",
):
    '''A RoleBinding grants permissions within a specific namespace to a user or set of users.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        role: IRole,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param role: The role to bind to. A RoleBinding can reference a Role or a ClusterRole.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBinding.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RoleBindingProps(role=role, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSubjects")
    def add_subjects(self, *subjects: ISubject) -> None:
        '''Adds a subject to the role.

        :param subjects: The subjects to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBinding.add_subjects)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addSubjects", [*subjects]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> IRole:
        return typing.cast(IRole, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="subjects")
    def subjects(self) -> typing.List[ISubject]:
        return typing.cast(typing.List[ISubject], jsii.get(self, "subjects"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.RoleBindingProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "role": "role"},
)
class RoleBindingProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        role: IRole,
    ) -> None:
        '''Properties for ``RoleBinding``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param role: The role to bind to. A RoleBinding can reference a Role or a ClusterRole.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
        }
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def role(self) -> IRole:
        '''The role to bind to.

        A RoleBinding can reference a Role or a ClusterRole.
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(IRole, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleBindingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.RolePolicyRule",
    jsii_struct_bases=[],
    name_mapping={"resources": "resources", "verbs": "verbs"},
)
class RolePolicyRule:
    def __init__(
        self,
        *,
        resources: typing.Sequence[IApiResource],
        verbs: typing.Sequence[builtins.str],
    ) -> None:
        '''Policy rule of a `Role.

        :param resources: Resources this rule applies to.
        :param verbs: Verbs to allow. (e.g ['get', 'watch'])
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RolePolicyRule.__init__)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument verbs", value=verbs, expected_type=type_hints["verbs"])
        self._values: typing.Dict[str, typing.Any] = {
            "resources": resources,
            "verbs": verbs,
        }

    @builtins.property
    def resources(self) -> typing.List[IApiResource]:
        '''Resources this rule applies to.'''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[IApiResource], result)

    @builtins.property
    def verbs(self) -> typing.List[builtins.str]:
        '''Verbs to allow.

        (e.g ['get', 'watch'])
        '''
        result = self._values.get("verbs")
        assert result is not None, "Required property 'verbs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolePolicyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.RoleProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "rules": "rules"},
)
class RoleProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[RolePolicyRule, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for ``Role``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param rules: A list of rules the role should allow. Default: []
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(RoleProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[RolePolicyRule]]:
        '''A list of rules the role should allow.

        :default: []
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[RolePolicyRule]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISecret)
class Secret(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Secret"):
    '''Kubernetes Secrets let you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.

    Storing confidential information in a
    Secret is safer and more flexible than putting it verbatim in a Pod
    definition or in a container image.

    :see: https://kubernetes.io/docs/concepts/configuration/secret
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_data: stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.
        :param type: Optional type associated with the secret. Used to facilitate programmatic handling of secret data by various controllers. Default: undefined - Don't set a type.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Secret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SecretProps(
            string_data=string_data, type=type, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecretName")
    @builtins.classmethod
    def from_secret_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> ISecret:
        '''Imports a secret from the cluster as a reference.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Secret.from_secret_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(ISecret, jsii.sinvoke(cls, "fromSecretName", [scope, id, name]))

    @jsii.member(jsii_name="addStringData")
    def add_string_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a string data field to the secert.

        :param key: Key.
        :param value: Value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Secret.add_string_data)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addStringData", [key, value]))

    @jsii.member(jsii_name="getStringData")
    def get_string_data(self, key: builtins.str) -> typing.Optional[builtins.str]:
        '''Gets a string data by key or undefined.

        :param key: Key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Secret.get_string_data)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "getStringData", [key]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="immutable")
    def immutable(self) -> builtins.bool:
        '''Whether or not the secret is immutable.'''
        return typing.cast(builtins.bool, jsii.get(self, "immutable"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.SecretValue",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "secret": "secret"},
)
class SecretValue:
    def __init__(self, *, key: builtins.str, secret: ISecret) -> None:
        '''Represents a specific value in JSON secret.

        :param key: The JSON key.
        :param secret: The secret.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecretValue.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "secret": secret,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The JSON key.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> ISecret:
        '''The secret.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(ISecret, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.SecretVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "default_mode": "defaultMode",
        "items": "items",
        "name": "name",
        "optional": "optional",
    },
)
class SecretVolumeOptions:
    def __init__(
        self,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, typing.Union[PathMapping, typing.Dict[str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the Secret-based volume.

        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the secret or its keys must be defined. Default: - undocumented
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecretVolumeOptions.__init__)
            check_type(argname="argument default_mode", value=default_mode, expected_type=type_hints["default_mode"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_mode is not None:
            self._values["default_mode"] = default_mode
        if items is not None:
            self._values["items"] = items
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def default_mode(self) -> typing.Optional[jsii.Number]:
        '''Mode bits to use on created files by default.

        Must be a value between 0 and
        0777. Defaults to 0644. Directories within the path are not affected by
        this setting. This might be in conflict with other options that affect the
        file mode, like fsGroup, and the result can be other mode bits set.

        :default:

        644. Directories within the path are not affected by this
        setting. This might be in conflict with other options that affect the file
        mode, like fsGroup, and the result can be other mode bits set.
        '''
        result = self._values.get("default_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def items(self) -> typing.Optional[typing.Mapping[builtins.str, PathMapping]]:
        '''If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value.

        If specified, the listed keys will be projected
        into the specified paths, and unlisted keys will not be present. If a key
        is specified which is not present in the secret, the volume setup will
        error unless it is marked optional. Paths must be relative and may not
        contain the '..' path or start with '..'.

        :default: - no mapping
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, PathMapping]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the secret or its keys must be defined.

        :default: - undocumented
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Service(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Service"):
    '''An abstract way to expose an application running on a set of Pods as a network service.

    With Kubernetes you don't need to modify your application to use an unfamiliar service discovery mechanism.
    Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

    For example, consider a stateless image-processing backend which is running with 3 replicas. Those replicas are fungible—frontends do not care which backend they use.
    While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that,
    nor should they need to keep track of the set of backends themselves.
    The Service abstraction enables this decoupling.

    If you're able to use Kubernetes APIs for service discovery in your application, you can query the API server for Endpoints,
    that get updated whenever the set of Pods in a Service changes. For non-native applications, Kubernetes offers ways to place a network port
    or load balancer in between your application and the backend Pods.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_ip: typing.Optional[builtins.str] = None,
        external_i_ps: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        ports: typing.Optional[typing.Sequence[typing.Union["ServicePort", typing.Dict[str, typing.Any]]]] = None,
        selector: typing.Optional[IPodSelector] = None,
        type: typing.Optional["ServiceType"] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster_ip: The IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. Default: - Automatically assigned.
        :param external_i_ps: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Default: - No external IPs.
        :param external_name: The externalName to be used when ServiceType.EXTERNAL_NAME is set. Default: - No external name.
        :param load_balancer_source_ranges: A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs. More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        :param ports: The ports this service binds to. If the selector of the service is a managed pod / workload, its ports will are automatically extracted and used as the default value. Otherwise, no ports are bound. Default: - either the selector ports, or none.
        :param selector: Which pods should the service select and route to. You can pass one of the following: - An instance of ``Pod`` or any workload resource (e.g ``Deployment``, ``StatefulSet``, ...) - Pods selected by the ``Pods.select`` function. Note that in this case only labels can be specified. Default: - unset, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify.
        :param type: Determines how the Service is exposed. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types Default: ServiceType.ClusterIP
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Service.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceProps(
            cluster_ip=cluster_ip,
            external_i_ps=external_i_ps,
            external_name=external_name,
            load_balancer_source_ranges=load_balancer_source_ranges,
            ports=ports,
            selector=selector,
            type=type,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        port: jsii.Number,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configure a port the service will bind to.

        This method can be called multiple times.

        :param port: The port definition.
        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Service.bind)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        options = ServiceBindOptions(
            name=name, node_port=node_port, protocol=protocol, target_port=target_port
        )

        return typing.cast(None, jsii.invoke(self, "bind", [port, options]))

    @jsii.member(jsii_name="exposeViaIngress")
    def expose_via_ingress(
        self,
        path: builtins.str,
        *,
        ingress: typing.Optional["Ingress"] = None,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> "Ingress":
        '''Expose a service via an ingress using the specified path.

        :param path: The path to expose the service under.
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        :param path_type: The type of the path. Default: HttpIngressPathType.PREFIX

        :return: The ``Ingress`` resource that was used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Service.expose_via_ingress)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = ExposeServiceViaIngressOptions(ingress=ingress, path_type=path_type)

        return typing.cast("Ingress", jsii.invoke(self, "exposeViaIngress", [path, options]))

    @jsii.member(jsii_name="select")
    def select(self, selector: IPodSelector) -> None:
        '''Require this service to select pods matching the selector.

        Note that invoking this method multiple times acts as an AND operator
        on the resulting labels.

        :param selector: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Service.select)
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        return typing.cast(None, jsii.invoke(self, "select", [selector]))

    @jsii.member(jsii_name="selectLabel")
    def select_label(self, key: builtins.str, value: builtins.str) -> None:
        '''Require this service to select pods with this label.

        Note that invoking this method multiple times acts as an AND operator
        on the resulting labels.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Service.select_label)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "selectLabel", [key, value]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List["ServicePort"]:
        '''Ports for this service.

        Use ``bind()`` to bind additional service ports.
        '''
        return typing.cast(typing.List["ServicePort"], jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ServiceType":
        '''Determines how the Service is exposed.'''
        return typing.cast("ServiceType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="clusterIP")
    def cluster_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address of the service and is usually assigned randomly by the master.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIP"))

    @builtins.property
    @jsii.member(jsii_name="externalName")
    def external_name(self) -> typing.Optional[builtins.str]:
        '''The externalName to be used for EXTERNAL_NAME types.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalName"))


@jsii.implements(IServiceAccount, ISubject)
class ServiceAccount(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ServiceAccount",
):
    '''A service account provides an identity for processes that run in a Pod.

    When you (a human) access the cluster (for example, using kubectl), you are
    authenticated by the apiserver as a particular User Account (currently this
    is usually admin, unless your cluster administrator has customized your
    cluster). Processes in containers inside pods can also contact the apiserver.
    When they do, they are authenticated as a particular Service Account (for
    example, default).

    :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        automount_token: typing.Optional[builtins.bool] = None,
        secrets: typing.Optional[typing.Sequence[ISecret]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param automount_token: Indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. Default: true
        :param secrets: List of secrets allowed to be used by pods running using this ServiceAccount.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceAccountProps(
            automount_token=automount_token, secrets=secrets, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServiceAccountName")
    @builtins.classmethod
    def from_service_account_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> IServiceAccount:
        '''Imports a service account from the cluster as a reference.

        :param scope: -
        :param id: -
        :param name: The name of the service account resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccount.from_service_account_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IServiceAccount, jsii.sinvoke(cls, "fromServiceAccountName", [scope, id, name]))

    @jsii.member(jsii_name="addSecret")
    def add_secret(self, secr: ISecret) -> None:
        '''Allow a secret to be accessed by pods using this service account.

        :param secr: The secret.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccount.add_secret)
            check_type(argname="argument secr", value=secr, expected_type=type_hints["secr"])
        return typing.cast(None, jsii.invoke(self, "addSecret", [secr]))

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> "SubjectConfiguration":
        '''Return the subject configuration.

        :see: ISubect.toSubjectConfiguration()
        '''
        return typing.cast("SubjectConfiguration", jsii.invoke(self, "toSubjectConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="automountToken")
    def automount_token(self) -> builtins.bool:
        '''Whether or not a token is automatically mounted for this service account.'''
        return typing.cast(builtins.bool, jsii.get(self, "automountToken"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> typing.List[ISecret]:
        '''List of secrets allowed to be used by pods running using this service account.

        Returns a copy. To add a secret, use ``addSecret()``.
        '''
        return typing.cast(typing.List[ISecret], jsii.get(self, "secrets"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServiceAccountProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "automount_token": "automountToken",
        "secrets": "secrets",
    },
)
class ServiceAccountProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_token: typing.Optional[builtins.bool] = None,
        secrets: typing.Optional[typing.Sequence[ISecret]] = None,
    ) -> None:
        '''Properties for initialization of ``ServiceAccount``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_token: Indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. Default: true
        :param secrets: List of secrets allowed to be used by pods running using this ServiceAccount.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccountProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_token", value=automount_token, expected_type=type_hints["automount_token"])
            check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_token is not None:
            self._values["automount_token"] = automount_token
        if secrets is not None:
            self._values["secrets"] = secrets

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether pods running as this service account should have an API token automatically mounted.

        Can be overridden at the pod level.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def secrets(self) -> typing.Optional[typing.List[ISecret]]:
        '''List of secrets allowed to be used by pods running using this ServiceAccount.

        :see: https://kubernetes.io/docs/concepts/configuration/secret
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.List[ISecret]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceAccountTokenSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ServiceAccountTokenSecret",
):
    '''Create a secret for a service account token.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#service-account-token-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service_account: IServiceAccount,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service_account: The service account to store a secret for.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccountTokenSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceAccountTokenSecretProps(
            service_account=service_account, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServiceBindOptions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class ServiceBindOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Service.bind``.

        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceBindOptions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_port", value=node_port, expected_type=type_hints["node_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServiceIngressBackendOptions",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class ServiceIngressBackendOptions:
    def __init__(self, *, port: typing.Optional[jsii.Number] = None) -> None:
        '''Options for setting up backends for ingress rules.

        :param port: The port to use to access the service. - This option will fail if the service does not expose any ports. - If the service exposes multiple ports, this option must be specified. - If the service exposes a single port, this option is optional and if specified, it must be the same port exposed by the service. Default: - if the service exposes a single port, this port will be used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIngressBackendOptions.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use to access the service.

        - This option will fail if the service does not expose any ports.
        - If the service exposes multiple ports, this option must be specified.
        - If the service exposes a single port, this option is optional and if
          specified, it must be the same port exposed by the service.

        :default: - if the service exposes a single port, this port will be used.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIngressBackendOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServicePort",
    jsii_struct_bases=[ServiceBindOptions],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
        "port": "port",
    },
)
class ServicePort(ServiceBindOptions):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
        port: jsii.Number,
    ) -> None:
        '''Definition of a service port.

        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        :param port: The port number the service will bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePort.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_port", value=node_port, expected_type=type_hints["node_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port number the service will bind to.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServiceProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "cluster_ip": "clusterIP",
        "external_i_ps": "externalIPs",
        "external_name": "externalName",
        "load_balancer_source_ranges": "loadBalancerSourceRanges",
        "ports": "ports",
        "selector": "selector",
        "type": "type",
    },
)
class ServiceProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        cluster_ip: typing.Optional[builtins.str] = None,
        external_i_ps: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ServicePort, typing.Dict[str, typing.Any]]]] = None,
        selector: typing.Optional[IPodSelector] = None,
        type: typing.Optional["ServiceType"] = None,
    ) -> None:
        '''Properties for ``Service``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param cluster_ip: The IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. Default: - Automatically assigned.
        :param external_i_ps: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Default: - No external IPs.
        :param external_name: The externalName to be used when ServiceType.EXTERNAL_NAME is set. Default: - No external name.
        :param load_balancer_source_ranges: A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs. More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        :param ports: The ports this service binds to. If the selector of the service is a managed pod / workload, its ports will are automatically extracted and used as the default value. Otherwise, no ports are bound. Default: - either the selector ports, or none.
        :param selector: Which pods should the service select and route to. You can pass one of the following: - An instance of ``Pod`` or any workload resource (e.g ``Deployment``, ``StatefulSet``, ...) - Pods selected by the ``Pods.select`` function. Note that in this case only labels can be specified. Default: - unset, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify.
        :param type: Determines how the Service is exposed. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types Default: ServiceType.ClusterIP
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument cluster_ip", value=cluster_ip, expected_type=type_hints["cluster_ip"])
            check_type(argname="argument external_i_ps", value=external_i_ps, expected_type=type_hints["external_i_ps"])
            check_type(argname="argument external_name", value=external_name, expected_type=type_hints["external_name"])
            check_type(argname="argument load_balancer_source_ranges", value=load_balancer_source_ranges, expected_type=type_hints["load_balancer_source_ranges"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if cluster_ip is not None:
            self._values["cluster_ip"] = cluster_ip
        if external_i_ps is not None:
            self._values["external_i_ps"] = external_i_ps
        if external_name is not None:
            self._values["external_name"] = external_name
        if load_balancer_source_ranges is not None:
            self._values["load_balancer_source_ranges"] = load_balancer_source_ranges
        if ports is not None:
            self._values["ports"] = ports
        if selector is not None:
            self._values["selector"] = selector
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def cluster_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address of the service and is usually assigned randomly by the master.

        If an address is specified manually and is not in use by others, it
        will be allocated to the service; otherwise, creation of the service will
        fail. This field can not be changed through updates. Valid values are
        "None", empty string (""), or a valid IP address. "None" can be specified
        for headless services when proxying is not required. Only applies to types
        ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName.

        :default: - Automatically assigned.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
        '''
        result = self._values.get("cluster_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_i_ps(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IP addresses for which nodes in the cluster will also accept traffic for this service.

        These IPs are not managed by Kubernetes. The user
        is responsible for ensuring that traffic arrives at a node with this IP. A
        common example is external load-balancers that are not part of the
        Kubernetes system.

        :default: - No external IPs.
        '''
        result = self._values.get("external_i_ps")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_name(self) -> typing.Optional[builtins.str]:
        '''The externalName to be used when ServiceType.EXTERNAL_NAME is set.

        :default: - No external name.
        '''
        result = self._values.get("external_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_source_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs.

        More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        '''
        result = self._values.get("load_balancer_source_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[ServicePort]]:
        '''The ports this service binds to.

        If the selector of the service is a managed pod / workload,
        its ports will are automatically extracted and used as the default value.
        Otherwise, no ports are bound.

        :default: - either the selector ports, or none.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[ServicePort]], result)

    @builtins.property
    def selector(self) -> typing.Optional[IPodSelector]:
        '''Which pods should the service select and route to.

        You can pass one of the following:

        - An instance of ``Pod`` or any workload resource (e.g ``Deployment``, ``StatefulSet``, ...)
        - Pods selected by the ``Pods.select`` function. Note that in this case only labels can be specified.

        :default:

        - unset, the service is assumed to have an external process managing
        its endpoints, which Kubernetes will not modify.

        Example::

            // select the pods of a specific deployment
            const backend = new kplus.Deployment(this, 'Backend', ...);
            new kplus.Service(this, 'Service', { selector: backend });
            
            // select all pods labeled with the `tier=backend` label
            const backend = kplus.Pod.labeled({ tier: 'backend' });
            new kplus.Service(this, 'Service', { selector: backend });
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[IPodSelector], result)

    @builtins.property
    def type(self) -> typing.Optional["ServiceType"]:
        '''Determines how the Service is exposed.

        More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types

        :default: ServiceType.ClusterIP
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ServiceType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.ServiceType")
class ServiceType(enum.Enum):
    '''For some parts of your application (for example, frontends) you may want to expose a Service onto an external IP address, that's outside of your cluster.

    Kubernetes ServiceTypes allow you to specify what kind of Service you want.
    The default is ClusterIP.
    '''

    CLUSTER_IP = "CLUSTER_IP"
    '''Exposes the Service on a cluster-internal IP.

    Choosing this value makes the Service only reachable from within the cluster.
    This is the default ServiceType
    '''
    NODE_PORT = "NODE_PORT"
    '''Exposes the Service on each Node's IP at a static port (the NodePort).

    A ClusterIP Service, to which the NodePort Service routes, is automatically created.
    You'll be able to contact the NodePort Service, from outside the cluster,
    by requesting :.
    '''
    LOAD_BALANCER = "LOAD_BALANCER"
    '''Exposes the Service externally using a cloud provider's load balancer.

    NodePort and ClusterIP Services, to which the external load balancer routes,
    are automatically created.
    '''
    EXTERNAL_NAME = "EXTERNAL_NAME"
    '''Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up.

    .. epigraph::

       Note: You need either kube-dns version 1.7 or CoreDNS version 0.0.8 or higher to use the ExternalName type.
    '''


class SshAuthSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.SshAuthSecret",
):
    '''Create a secret for ssh authentication.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#ssh-authentication-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ssh_private_key: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ssh_private_key: The SSH private key to use.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SshAuthSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SshAuthSecretProps(
            ssh_private_key=ssh_private_key, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


class StatefulSetUpdateStrategy(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.StatefulSetUpdateStrategy",
):
    '''StatefulSet update strategies.'''

    @jsii.member(jsii_name="onDelete")
    @builtins.classmethod
    def on_delete(cls) -> "StatefulSetUpdateStrategy":
        '''The controller will not automatically update the Pods in a StatefulSet.

        Users must manually delete Pods to cause the controller to create new Pods
        that reflect modifications.
        '''
        return typing.cast("StatefulSetUpdateStrategy", jsii.sinvoke(cls, "onDelete", []))

    @jsii.member(jsii_name="rollingUpdate")
    @builtins.classmethod
    def rolling_update(
        cls,
        *,
        partition: typing.Optional[jsii.Number] = None,
    ) -> "StatefulSetUpdateStrategy":
        '''The controller will delete and recreate each Pod in the StatefulSet.

        It will proceed in the same order as Pod termination (from the largest ordinal to the smallest),
        updating each Pod one at a time. The Kubernetes control plane waits until an updated
        Pod is Running and Ready prior to updating its predecessor.

        :param partition: If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version. If the partition is greater than replicas, updates to the pod template will not be propagated to Pods. In most cases you will not need to use a partition, but they are useful if you want to stage an update, roll out a canary, or perform a phased roll out. Default: 0
        '''
        options = StatefulSetUpdateStrategyRollingUpdateOptions(partition=partition)

        return typing.cast("StatefulSetUpdateStrategy", jsii.sinvoke(cls, "rollingUpdate", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.StatefulSetUpdateStrategyRollingUpdateOptions",
    jsii_struct_bases=[],
    name_mapping={"partition": "partition"},
)
class StatefulSetUpdateStrategyRollingUpdateOptions:
    def __init__(self, *, partition: typing.Optional[jsii.Number] = None) -> None:
        '''Options for ``StatefulSetUpdateStrategy.rollingUpdate``.

        :param partition: If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version. If the partition is greater than replicas, updates to the pod template will not be propagated to Pods. In most cases you will not need to use a partition, but they are useful if you want to stage an update, roll out a canary, or perform a phased roll out. Default: 0
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StatefulSetUpdateStrategyRollingUpdateOptions.__init__)
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
        self._values: typing.Dict[str, typing.Any] = {}
        if partition is not None:
            self._values["partition"] = partition

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version.

        If the partition is greater than replicas, updates to the pod template will not be propagated to Pods.
        In most cases you will not need to use a partition, but they are useful if you want to stage an
        update, roll out a canary, or perform a phased roll out.

        :default: 0

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#partitions
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StatefulSetUpdateStrategyRollingUpdateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.SubjectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "api_group": "apiGroup",
        "namespace": "namespace",
    },
)
class SubjectConfiguration:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_group: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Subject contains a reference to the object or user identities a role binding applies to.

        This can either hold a direct API object reference, or a value
        for non-objects such as user and group names.

        :param kind: Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.
        :param name: Name of the object being referenced.
        :param api_group: APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
        :param namespace: Namespace of the referenced object. If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubjectConfiguration.__init__)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_group is not None:
            self._values["api_group"] = api_group
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of object being referenced.

        Values defined by this API group are
        "User", "Group", and "ServiceAccount". If the Authorizer does not
        recognized the kind value, the Authorizer should report an error.
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the object being referenced.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_group(self) -> typing.Optional[builtins.str]:
        '''APIGroup holds the API group of the referenced subject.

        Defaults to "" for
        ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User
        and Group subjects.
        '''
        result = self._values.get("api_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the referenced object.

        If the object kind is non-namespace,
        such as "User" or "Group", and this value is not empty the Authorizer
        should report an error.
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubjectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.Sysctl",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Sysctl:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Sysctl defines a kernel parameter to be set.

        :param name: Name of a property to set.
        :param value: Value of a property to set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Sysctl.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of a property to set.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of a property to set.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sysctl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-23.TaintEffect")
class TaintEffect(enum.Enum):
    '''Taint effects.'''

    NO_SCHEDULE = "NO_SCHEDULE"
    '''This means that no pod will be able to schedule onto the node unless it has a matching toleration.'''
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"
    '''This is a "preference" or "soft" version of ``NO_SCHEDULE`` -- the system will try to avoid placing a pod that does not tolerate the taint on the node, but it is not required.'''
    NO_EXECUTE = "NO_EXECUTE"
    '''This affects pods that are already running on the node as follows:.

    - Pods that do not tolerate the taint are evicted immediately.
    - Pods that tolerate the taint without specifying ``duration`` remain bound forever.
    - Pods that tolerate the taint with a specified ``duration`` remain bound for
      the specified amount of time.
    '''


class TaintedNode(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.TaintedNode"):
    '''A node that is matched by taint selectors.'''

    def __init__(self, taint_selector: typing.Sequence[NodeTaintQuery]) -> None:
        '''
        :param taint_selector: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TaintedNode.__init__)
            check_type(argname="argument taint_selector", value=taint_selector, expected_type=type_hints["taint_selector"])
        jsii.create(self.__class__, self, [taint_selector])

    @builtins.property
    @jsii.member(jsii_name="taintSelector")
    def taint_selector(self) -> typing.List[NodeTaintQuery]:
        return typing.cast(typing.List[NodeTaintQuery], jsii.get(self, "taintSelector"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.TcpSocketProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
        "host": "host",
        "port": "port",
    },
)
class TcpSocketProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Probe.fromTcpSocket()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TcpSocketProbeOptions.__init__)
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The host name to connect to on the container.

        :default: - defaults to the pod IP
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to connect to on the container.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpSocketProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TlsSecret(Secret, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.TlsSecret"):
    '''Create a secret for storing a TLS certificate and its associated key.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        tls_cert: builtins.str,
        tls_key: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param tls_cert: The TLS cert.
        :param tls_key: The TLS key.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TlsSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TlsSecretProps(
            tls_cert=tls_cert, tls_key=tls_key, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


class Topology(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Topology"):
    '''Available topology domains.'''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, key: builtins.str) -> "Topology":
        '''Custom key for the node label that the system uses to denote the topology domain.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Topology.custom)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("Topology", jsii.sinvoke(cls, "custom", [key]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HOSTNAME")
    def HOSTNAME(cls) -> "Topology":
        '''A hostname represents a single node in the cluster.

        :see: https://kubernetes.io/docs/reference/labels-annotations-taints/#kubernetesiohostname
        '''
        return typing.cast("Topology", jsii.sget(cls, "HOSTNAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REGION")
    def REGION(cls) -> "Topology":
        '''A region represents a larger domain, made up of one or more zones.

        It is uncommon
        for Kubernetes clusters to span multiple regions. While the exact definition of a
        zone or region is left to infrastructure implementations, common properties of a region
        include higher network latency between them than within them, non-zero cost for network
        traffic between them, and failure independence from other zones or regions.

        For example, nodes within a region might share power infrastructure (e.g. a UPS or generator), but
        nodes in different regions typically would not.

        :see: https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesioregion
        '''
        return typing.cast("Topology", jsii.sget(cls, "REGION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ZONE")
    def ZONE(cls) -> "Topology":
        '''A zone represents a logical failure domain.

        It is common for Kubernetes clusters to
        span multiple zones for increased availability. While the exact definition of a zone is
        left to infrastructure implementations, common properties of a zone include very low
        network latency within a zone, no-cost network traffic within a zone, and failure
        independence from other zones. For example, nodes within a zone might share a network
        switch, but nodes in different zones should not.

        :see: https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone
        '''
        return typing.cast("Topology", jsii.sget(cls, "ZONE"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))


@jsii.implements(ISubject)
class User(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.User",
):
    '''Represents a user.'''

    @jsii.member(jsii_name="fromName")
    @builtins.classmethod
    def from_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> "User":
        '''Reference a user in the cluster by name.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.from_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast("User", jsii.sinvoke(cls, "fromName", [scope, id, name]))

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> SubjectConfiguration:
        '''Return the subject configuration.

        :see: ISubect.toSubjectConfiguration()
        '''
        return typing.cast(SubjectConfiguration, jsii.invoke(self, "toSubjectConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroup"))


@jsii.implements(IStorage)
class Volume(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.Volume",
):
    '''Volume represents a named volume in a pod that may be accessed by any container in the pod.

    Docker also has a concept of volumes, though it is somewhat looser and less
    managed. In Docker, a volume is simply a directory on disk or in another
    Container. Lifetimes are not managed and until very recently there were only
    local-disk-backed volumes. Docker now provides volume drivers, but the
    functionality is very limited for now (e.g. as of Docker 1.7 only one volume
    driver is allowed per Container and there is no way to pass parameters to
    volumes).

    A Kubernetes volume, on the other hand, has an explicit lifetime - the same
    as the Pod that encloses it. Consequently, a volume outlives any Containers
    that run within the Pod, and data is preserved across Container restarts. Of
    course, when a Pod ceases to exist, the volume will cease to exist, too.
    Perhaps more importantly than this, Kubernetes supports many types of
    volumes, and a Pod can use any number of them simultaneously.

    At its core, a volume is just a directory, possibly with some data in it,
    which is accessible to the Containers in a Pod. How that directory comes to
    be, the medium that backs it, and the contents of it are determined by the
    particular volume type used.

    To use a volume, a Pod specifies what volumes to provide for the Pod (the
    .spec.volumes field) and where to mount those into Containers (the
    .spec.containers[*].volumeMounts field).

    A process in a container sees a filesystem view composed from their Docker
    image and volumes. The Docker image is at the root of the filesystem
    hierarchy, and any volumes are mounted at the specified paths within the
    image. Volumes can not mount onto other volumes
    '''

    @jsii.member(jsii_name="fromAwsElasticBlockStore")
    @builtins.classmethod
    def from_aws_elastic_block_store(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        volume_id: builtins.str,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts an Amazon Web Services (AWS) EBS volume into your pod.

        Unlike emptyDir, which is erased when a pod is removed, the contents of an EBS volume are
        persisted and the volume is unmounted. This means that an EBS volume can be pre-populated with data,
        and that data can be shared between pods.

        There are some restrictions when using an awsElasticBlockStore volume:

        - the nodes on which pods are running must be AWS EC2 instances.
        - those instances need to be in the same region and availability zone as the EBS volume.
        - EBS only supports a single EC2 instance mounting a volume.

        :param scope: -
        :param id: -
        :param volume_id: -
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_aws_elastic_block_store)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        options = AwsElasticBlockStoreVolumeOptions(
            fs_type=fs_type, name=name, partition=partition, read_only=read_only
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromAwsElasticBlockStore", [scope, id, volume_id, options]))

    @jsii.member(jsii_name="fromAzureDisk")
    @builtins.classmethod
    def from_azure_disk(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        *,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts a Microsoft Azure Data Disk into a pod.

        :param scope: -
        :param id: -
        :param disk_name: -
        :param disk_uri: -
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param name: The volume name. Default: - auto-generated
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_azure_disk)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument disk_uri", value=disk_uri, expected_type=type_hints["disk_uri"])
        options = AzureDiskVolumeOptions(
            caching_mode=caching_mode,
            fs_type=fs_type,
            kind=kind,
            name=name,
            read_only=read_only,
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromAzureDisk", [scope, id, disk_name, disk_uri, options]))

    @jsii.member(jsii_name="fromConfigMap")
    @builtins.classmethod
    def from_config_map(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        config_map: "IConfigMap",
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, typing.Union[PathMapping, typing.Dict[str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Populate the volume from a ConfigMap.

        The configMap resource provides a way to inject configuration data into
        Pods. The data stored in a ConfigMap object can be referenced in a volume
        of type configMap and then consumed by containerized applications running
        in a Pod.

        When referencing a configMap object, you can simply provide its name in the
        volume to reference it. You can also customize the path to use for a
        specific entry in the ConfigMap.

        :param scope: -
        :param id: -
        :param config_map: The config map to use to populate the volume.
        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the ConfigMap or its keys must be defined. Default: - undocumented
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_config_map)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
        options = ConfigMapVolumeOptions(
            default_mode=default_mode, items=items, name=name, optional=optional
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromConfigMap", [scope, id, config_map, options]))

    @jsii.member(jsii_name="fromEmptyDir")
    @builtins.classmethod
    def from_empty_dir(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
        *,
        medium: typing.Optional[EmptyDirMedium] = None,
        size_limit: typing.Optional[cdk8s.Size] = None,
    ) -> "Volume":
        '''An emptyDir volume is first created when a Pod is assigned to a Node, and exists as long as that Pod is running on that node.

        As the name says, it is
        initially empty. Containers in the Pod can all read and write the same
        files in the emptyDir volume, though that volume can be mounted at the same
        or different paths in each Container. When a Pod is removed from a node for
        any reason, the data in the emptyDir is deleted forever.

        :param scope: -
        :param id: -
        :param name: -
        :param medium: By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment. However, you can set the emptyDir.medium field to ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that unlike disks, tmpfs is cleared on node reboot and any files you write will count against your Container's memory limit. Default: EmptyDirMedium.DEFAULT
        :param size_limit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. Default: - limit is undefined

        :see: http://kubernetes.io/docs/user-guide/volumes#emptydir
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_empty_dir)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        options = EmptyDirVolumeOptions(medium=medium, size_limit=size_limit)

        return typing.cast("Volume", jsii.sinvoke(cls, "fromEmptyDir", [scope, id, name, options]))

    @jsii.member(jsii_name="fromGcePersistentDisk")
    @builtins.classmethod
    def from_gce_persistent_disk(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        pd_name: builtins.str,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts a Google Compute Engine (GCE) persistent disk (PD) into your Pod.

        Unlike emptyDir, which is erased when a pod is removed, the contents of a PD are
        preserved and the volume is merely unmounted. This means that a PD can be pre-populated
        with data, and that data can be shared between pods.

        There are some restrictions when using a gcePersistentDisk:

        - the nodes on which Pods are running must be GCE VMs
        - those VMs need to be in the same GCE project and zone as the persistent disk

        :param scope: -
        :param id: -
        :param pd_name: -
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_gce_persistent_disk)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
        options = GCEPersistentDiskVolumeOptions(
            fs_type=fs_type, name=name, partition=partition, read_only=read_only
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromGcePersistentDisk", [scope, id, pd_name, options]))

    @jsii.member(jsii_name="fromHostPath")
    @builtins.classmethod
    def from_host_path(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
        *,
        path: builtins.str,
        type: typing.Optional[HostPathVolumeType] = None,
    ) -> "Volume":
        '''Used to mount a file or directory from the host node's filesystem into a Pod.

        This is not something that most Pods will need, but it offers a powerful
        escape hatch for some applications.

        :param scope: -
        :param id: -
        :param name: -
        :param path: The path of the directory on the host.
        :param type: The expected type of the path found on the host. Default: HostPathVolumeType.DEFAULT

        :see: https://kubernetes.io/docs/concepts/storage/volumes/#hostpath
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_host_path)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        options = HostPathVolumeOptions(path=path, type=type)

        return typing.cast("Volume", jsii.sinvoke(cls, "fromHostPath", [scope, id, name, options]))

    @jsii.member(jsii_name="fromPersistentVolumeClaim")
    @builtins.classmethod
    def from_persistent_volume_claim(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        claim: "IPersistentVolumeClaim",
        *,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Used to mount a PersistentVolume into a Pod.

        PersistentVolumeClaims are a way for users to "claim" durable storage (such as a GCE PersistentDisk or an iSCSI volume)
        without knowing the details of the particular cloud environment.

        :param scope: -
        :param id: -
        :param claim: -
        :param name: The volume name. Default: - Derived from the PVC name.
        :param read_only: Will force the ReadOnly setting in VolumeMounts. Default: false

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_persistent_volume_claim)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
        options = PersistentVolumeClaimVolumeOptions(name=name, read_only=read_only)

        return typing.cast("Volume", jsii.sinvoke(cls, "fromPersistentVolumeClaim", [scope, id, claim, options]))

    @jsii.member(jsii_name="fromSecret")
    @builtins.classmethod
    def from_secret(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        secr: ISecret,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, typing.Union[PathMapping, typing.Dict[str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Populate the volume from a Secret.

        A secret volume is used to pass sensitive information, such as passwords, to Pods.
        You can store secrets in the Kubernetes API and mount them as files for use by pods
        without coupling to Kubernetes directly.

        secret volumes are backed by tmpfs (a RAM-backed filesystem)
        so they are never written to non-volatile storage.

        :param scope: -
        :param id: -
        :param secr: The secret to use to populate the volume.
        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the secret or its keys must be defined. Default: - undocumented

        :see: https://kubernetes.io/docs/concepts/storage/volumes/#secret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.from_secret)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument secr", value=secr, expected_type=type_hints["secr"])
        options = SecretVolumeOptions(
            default_mode=default_mode, items=items, name=name, optional=optional
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromSecret", [scope, id, secr, options]))

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast("Volume", jsii.invoke(self, "asVolume", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.VolumeMount",
    jsii_struct_bases=[MountOptions],
    name_mapping={
        "propagation": "propagation",
        "read_only": "readOnly",
        "sub_path": "subPath",
        "sub_path_expr": "subPathExpr",
        "path": "path",
        "volume": "volume",
    },
)
class VolumeMount(MountOptions):
    def __init__(
        self,
        *,
        propagation: typing.Optional[MountPropagation] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
        path: builtins.str,
        volume: Volume,
    ) -> None:
        '''Mount a volume from the pod to the container.

        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        :param path: Path within the container at which the volume should be mounted. Must not contain ':'.
        :param volume: The volume to mount.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeMount.__init__)
            check_type(argname="argument propagation", value=propagation, expected_type=type_hints["propagation"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument sub_path", value=sub_path, expected_type=type_hints["sub_path"])
            check_type(argname="argument sub_path_expr", value=sub_path_expr, expected_type=type_hints["sub_path_expr"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "volume": volume,
        }
        if propagation is not None:
            self._values["propagation"] = propagation
        if read_only is not None:
            self._values["read_only"] = read_only
        if sub_path is not None:
            self._values["sub_path"] = sub_path
        if sub_path_expr is not None:
            self._values["sub_path_expr"] = sub_path_expr

    @builtins.property
    def propagation(self) -> typing.Optional[MountPropagation]:
        '''Determines how mounts are propagated from the host to container and the other way around.

        When not set, MountPropagationNone is used.

        Mount propagation allows for sharing volumes mounted by a Container to
        other Containers in the same Pod, or even to other Pods on the same node.

        :default: MountPropagation.NONE
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional[MountPropagation], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Mounted read-only if true, read-write otherwise (false or unspecified).

        Defaults to false.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sub_path(self) -> typing.Optional[builtins.str]:
        '''Path within the volume from which the container's volume should be mounted.).

        :default: "" the volume's root
        '''
        result = self._values.get("sub_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_path_expr(self) -> typing.Optional[builtins.str]:
        '''Expanded path within the volume from which the container's volume should be mounted.

        Behaves similarly to SubPath but environment variable references
        $(VAR_NAME) are expanded using the container's environment. Defaults to ""
        (volume's root).

        ``subPathExpr`` and ``subPath`` are mutually exclusive.

        :default: "" volume's root.
        '''
        result = self._values.get("sub_path_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path within the container at which the volume should be mounted.

        Must not
        contain ':'.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> Volume:
        '''The volume to mount.'''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(Volume, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadScheduling(
    PodScheduling,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.WorkloadScheduling",
):
    '''Controls the pod scheduling strategy of this workload.

    It offers some additional API's on top of the core pod scheduling.
    '''

    def __init__(self, instance: "AbstractPod") -> None:
        '''
        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadScheduling.__init__)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        jsii.create(self.__class__, self, [instance])

    @jsii.member(jsii_name="spread")
    def spread(
        self,
        *,
        topology: typing.Optional[Topology] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Spread the pods in this workload by the topology key.

        A spread is a separation of the pod from itself and is used to
        balance out pod replicas across a given topology.

        :param topology: Which topology to spread on. Default: - Topology.HOSTNAME
        :param weight: Indicates the spread is optional, with this weight score. Default: - no weight. spread is assumed to be required.
        '''
        options = WorkloadSchedulingSpreadOptions(topology=topology, weight=weight)

        return typing.cast(None, jsii.invoke(self, "spread", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.WorkloadSchedulingSpreadOptions",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology", "weight": "weight"},
)
class WorkloadSchedulingSpreadOptions:
    def __init__(
        self,
        *,
        topology: typing.Optional[Topology] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``WorkloadScheduling.spread``.

        :param topology: Which topology to spread on. Default: - Topology.HOSTNAME
        :param weight: Indicates the spread is optional, with this weight score. Default: - no weight. spread is assumed to be required.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadSchedulingSpreadOptions.__init__)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if topology is not None:
            self._values["topology"] = topology
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def topology(self) -> typing.Optional[Topology]:
        '''Which topology to spread on.

        :default: - Topology.HOSTNAME
        '''
        result = self._values.get("topology")
        return typing.cast(typing.Optional[Topology], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Indicates the spread is optional, with this weight score.

        :default: - no weight. spread is assumed to be required.
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadSchedulingSpreadOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodSelector, INetworkPolicyPeer, ISubject)
class AbstractPod(
    Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk8s-plus-23.AbstractPod",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AbstractPod.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AbstractPodProps(
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env_from: typing.Optional[typing.Sequence[EnvFrom]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[typing.Union[ContainerLifecycle, typing.Dict[str, typing.Any]]] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_number: typing.Optional[jsii.Number] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ContainerPort, typing.Dict[str, typing.Any]]]] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[typing.Union[ContainerResources, typing.Dict[str, typing.Any]]] = None,
        security_context: typing.Optional[typing.Union[ContainerSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Union[VolumeMount, typing.Dict[str, typing.Any]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''
        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env_from: List of sources to populate environment variables in the container. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by the ``envVariables`` property with a duplicate key will take precedence. Default: - No sources.
        :param env_variables: Environment variables to set in the container. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: 
        :param port_number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. This is a convinience property if all you need a single TCP numbered port. In case more advanced configuartion is required, use the ``ports`` property. This port is added to the list of ports mentioned in the ``ports`` property. Default: - Only the ports mentiond in the ``ports`` property are exposed.
        :param ports: List of ports to expose from this container. Default: - Only the port mentioned in the ``portNumber`` property is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container. Default: cpu: request: 1000 millis limit: 1500 millis memory: request: 512 mebibytes limit: 2048 mebibytes
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - If a port is provided, then knocks on that port to determine when the container is ready for readiness and liveness probe checks. Otherwise, no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        cont = ContainerProps(
            image=image,
            args=args,
            command=command,
            env_from=env_from,
            env_variables=env_variables,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            port_number=port_number,
            ports=ports,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [cont]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env_from: typing.Optional[typing.Sequence[EnvFrom]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[typing.Union[ContainerLifecycle, typing.Dict[str, typing.Any]]] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_number: typing.Optional[jsii.Number] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ContainerPort, typing.Dict[str, typing.Any]]]] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[typing.Union[ContainerResources, typing.Dict[str, typing.Any]]] = None,
        security_context: typing.Optional[typing.Union[ContainerSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Union[VolumeMount, typing.Dict[str, typing.Any]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''
        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env_from: List of sources to populate environment variables in the container. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by the ``envVariables`` property with a duplicate key will take precedence. Default: - No sources.
        :param env_variables: Environment variables to set in the container. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: 
        :param port_number: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. This is a convinience property if all you need a single TCP numbered port. In case more advanced configuartion is required, use the ``ports`` property. This port is added to the list of ports mentioned in the ``ports`` property. Default: - Only the ports mentiond in the ``ports`` property are exposed.
        :param ports: List of ports to expose from this container. Default: - Only the port mentioned in the ``portNumber`` property is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container. Default: cpu: request: 1000 millis limit: 1500 millis memory: request: 512 mebibytes limit: 2048 mebibytes
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - If a port is provided, then knocks on that port to determine when the container is ready for readiness and liveness probe checks. Otherwise, no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        cont = ContainerProps(
            image=image,
            args=args,
            command=command,
            env_from=env_from,
            env_variables=env_variables,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            port_number=port_number,
            ports=ports,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [cont]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, vol: Volume) -> None:
        '''
        :param vol: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AbstractPod.add_volume)
            check_type(argname="argument vol", value=vol, expected_type=type_hints["vol"])
        return typing.cast(None, jsii.invoke(self, "addVolume", [vol]))

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> NetworkPolicyPeerConfig:
        '''Return the configuration of this peer.

        :see: INetworkPolicyPeer.toNetworkPolicyPeerConfig()
        '''
        return typing.cast(NetworkPolicyPeerConfig, jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional[IPodSelector]:
        '''Convert the peer into a pod selector, if possible.

        :see: INetworkPolicyPeer.toPodSelector()
        '''
        return typing.cast(typing.Optional[IPodSelector], jsii.invoke(self, "toPodSelector", []))

    @jsii.member(jsii_name="toPodSelectorConfig")
    def to_pod_selector_config(self) -> PodSelectorConfig:
        '''Return the configuration of this selector.

        :see: IPodSelector.toPodSelectorConfig()
        '''
        return typing.cast(PodSelectorConfig, jsii.invoke(self, "toPodSelectorConfig", []))

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> SubjectConfiguration:
        '''Return the subject configuration.

        :see: ISubect.toSubjectConfiguration()
        '''
        return typing.cast(SubjectConfiguration, jsii.invoke(self, "toSubjectConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="automountServiceAccountToken")
    def automount_service_account_token(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "automountServiceAccountToken"))

    @builtins.property
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> PodDns:
        return typing.cast(PodDns, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property
    @jsii.member(jsii_name="podMetadata")
    @abc.abstractmethod
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        ...

    @builtins.property
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[Volume]:
        return typing.cast(typing.List[Volume], jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="dockerRegistryAuth")
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        return typing.cast(typing.Optional["DockerConfigSecret"], jsii.get(self, "dockerRegistryAuth"))

    @builtins.property
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


class _AbstractPodProxy(
    AbstractPod,
    jsii.proxy_for(Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AbstractPod).__jsii_proxy_class__ = lambda : _AbstractPodProxy


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AbstractPodProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
    },
)
class AbstractPodProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''Properties for ``AbstractPod``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(AbstractPodProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AbstractPodProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AddDeploymentOptions",
    jsii_struct_bases=[ServiceBindOptions],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
        "port": "port",
    },
)
class AddDeploymentOptions(ServiceBindOptions):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options to add a deployment to a service.

        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        :param port: The port number the service will bind to. Default: - Copied from the first container of the deployment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddDeploymentOptions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_port", value=node_port, expected_type=type_hints["node_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will bind to.

        :default: - Copied from the first container of the deployment.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddDeploymentOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IApiResource, IApiEndpoint)
class ApiResource(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.ApiResource"):
    '''Represents information about an API resource type.'''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(
        cls,
        *,
        api_group: builtins.str,
        resource_type: builtins.str,
    ) -> "ApiResource":
        '''API resource information for a custom resource type.

        :param api_group: The group portion of the API version (e.g. ``authorization.k8s.io``).
        :param resource_type: The name of the resource type as it appears in the relevant API endpoint.
        '''
        options = ApiResourceOptions(api_group=api_group, resource_type=resource_type)

        return typing.cast("ApiResource", jsii.sinvoke(cls, "custom", [options]))

    @jsii.member(jsii_name="asApiResource")
    def as_api_resource(self) -> typing.Optional[IApiResource]:
        '''Return the IApiResource this object represents.'''
        return typing.cast(typing.Optional[IApiResource], jsii.invoke(self, "asApiResource", []))

    @jsii.member(jsii_name="asNonApiResource")
    def as_non_api_resource(self) -> typing.Optional[builtins.str]:
        '''Return the non resource url this object represents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "asNonApiResource", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_SERVICES")
    def API_SERVICES(cls) -> "ApiResource":
        '''API resource information for APIService.'''
        return typing.cast("ApiResource", jsii.sget(cls, "API_SERVICES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BINDINGS")
    def BINDINGS(cls) -> "ApiResource":
        '''API resource information for Binding.'''
        return typing.cast("ApiResource", jsii.sget(cls, "BINDINGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CERTIFICATE_SIGNING_REQUESTS")
    def CERTIFICATE_SIGNING_REQUESTS(cls) -> "ApiResource":
        '''API resource information for CertificateSigningRequest.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CERTIFICATE_SIGNING_REQUESTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLUSTER_ROLE_BINDINGS")
    def CLUSTER_ROLE_BINDINGS(cls) -> "ApiResource":
        '''API resource information for ClusterRoleBinding.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CLUSTER_ROLE_BINDINGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLUSTER_ROLES")
    def CLUSTER_ROLES(cls) -> "ApiResource":
        '''API resource information for ClusterRole.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CLUSTER_ROLES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPONENT_STATUSES")
    def COMPONENT_STATUSES(cls) -> "ApiResource":
        '''API resource information for ComponentStatus.'''
        return typing.cast("ApiResource", jsii.sget(cls, "COMPONENT_STATUSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONFIG_MAPS")
    def CONFIG_MAPS(cls) -> "ApiResource":
        '''API resource information for ConfigMap.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CONFIG_MAPS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONTROLLER_REVISIONS")
    def CONTROLLER_REVISIONS(cls) -> "ApiResource":
        '''API resource information for ControllerRevision.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CONTROLLER_REVISIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CRON_JOBS")
    def CRON_JOBS(cls) -> "ApiResource":
        '''API resource information for CronJob.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CRON_JOBS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CSI_DRIVERS")
    def CSI_DRIVERS(cls) -> "ApiResource":
        '''API resource information for CSIDriver.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CSI_DRIVERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CSI_NODES")
    def CSI_NODES(cls) -> "ApiResource":
        '''API resource information for CSINode.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CSI_NODES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CSI_STORAGE_CAPACITIES")
    def CSI_STORAGE_CAPACITIES(cls) -> "ApiResource":
        '''API resource information for CSIStorageCapacity.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CSI_STORAGE_CAPACITIES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CUSTOM_RESOURCE_DEFINITIONS")
    def CUSTOM_RESOURCE_DEFINITIONS(cls) -> "ApiResource":
        '''API resource information for CustomResourceDefinition.'''
        return typing.cast("ApiResource", jsii.sget(cls, "CUSTOM_RESOURCE_DEFINITIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DAEMON_SETS")
    def DAEMON_SETS(cls) -> "ApiResource":
        '''API resource information for DaemonSet.'''
        return typing.cast("ApiResource", jsii.sget(cls, "DAEMON_SETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEPLOYMENTS")
    def DEPLOYMENTS(cls) -> "ApiResource":
        '''API resource information for Deployment.'''
        return typing.cast("ApiResource", jsii.sget(cls, "DEPLOYMENTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ENDPOINT_SLICES")
    def ENDPOINT_SLICES(cls) -> "ApiResource":
        '''API resource information for EndpointSlice.'''
        return typing.cast("ApiResource", jsii.sget(cls, "ENDPOINT_SLICES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ENDPOINTS")
    def ENDPOINTS(cls) -> "ApiResource":
        '''API resource information for Endpoints.'''
        return typing.cast("ApiResource", jsii.sget(cls, "ENDPOINTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTS")
    def EVENTS(cls) -> "ApiResource":
        '''API resource information for Event.'''
        return typing.cast("ApiResource", jsii.sget(cls, "EVENTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FLOW_SCHEMAS")
    def FLOW_SCHEMAS(cls) -> "ApiResource":
        '''API resource information for FlowSchema.'''
        return typing.cast("ApiResource", jsii.sget(cls, "FLOW_SCHEMAS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HORIZONTAL_POD_AUTOSCALERS")
    def HORIZONTAL_POD_AUTOSCALERS(cls) -> "ApiResource":
        '''API resource information for HorizontalPodAutoscaler.'''
        return typing.cast("ApiResource", jsii.sget(cls, "HORIZONTAL_POD_AUTOSCALERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INGRESS_CLASSES")
    def INGRESS_CLASSES(cls) -> "ApiResource":
        '''API resource information for IngressClass.'''
        return typing.cast("ApiResource", jsii.sget(cls, "INGRESS_CLASSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INGRESSES")
    def INGRESSES(cls) -> "ApiResource":
        '''API resource information for Ingress.'''
        return typing.cast("ApiResource", jsii.sget(cls, "INGRESSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="JOBS")
    def JOBS(cls) -> "ApiResource":
        '''API resource information for Job.'''
        return typing.cast("ApiResource", jsii.sget(cls, "JOBS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LEASES")
    def LEASES(cls) -> "ApiResource":
        '''API resource information for Lease.'''
        return typing.cast("ApiResource", jsii.sget(cls, "LEASES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIMIT_RANGES")
    def LIMIT_RANGES(cls) -> "ApiResource":
        '''API resource information for LimitRange.'''
        return typing.cast("ApiResource", jsii.sget(cls, "LIMIT_RANGES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LOCAL_SUBJECT_ACCESS_REVIEWS")
    def LOCAL_SUBJECT_ACCESS_REVIEWS(cls) -> "ApiResource":
        '''API resource information for LocalSubjectAccessReview.'''
        return typing.cast("ApiResource", jsii.sget(cls, "LOCAL_SUBJECT_ACCESS_REVIEWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MUTATING_WEBHOOK_CONFIGURATIONS")
    def MUTATING_WEBHOOK_CONFIGURATIONS(cls) -> "ApiResource":
        '''API resource information for MutatingWebhookConfiguration.'''
        return typing.cast("ApiResource", jsii.sget(cls, "MUTATING_WEBHOOK_CONFIGURATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NAMESPACES")
    def NAMESPACES(cls) -> "ApiResource":
        '''API resource information for Namespace.'''
        return typing.cast("ApiResource", jsii.sget(cls, "NAMESPACES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_POLICIES")
    def NETWORK_POLICIES(cls) -> "ApiResource":
        '''API resource information for NetworkPolicy.'''
        return typing.cast("ApiResource", jsii.sget(cls, "NETWORK_POLICIES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NODES")
    def NODES(cls) -> "ApiResource":
        '''API resource information for Node.'''
        return typing.cast("ApiResource", jsii.sget(cls, "NODES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERSISTENT_VOLUME_CLAIMS")
    def PERSISTENT_VOLUME_CLAIMS(cls) -> "ApiResource":
        '''API resource information for PersistentVolumeClaim.'''
        return typing.cast("ApiResource", jsii.sget(cls, "PERSISTENT_VOLUME_CLAIMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERSISTENT_VOLUMES")
    def PERSISTENT_VOLUMES(cls) -> "ApiResource":
        '''API resource information for PersistentVolume.'''
        return typing.cast("ApiResource", jsii.sget(cls, "PERSISTENT_VOLUMES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POD_DISRUPTION_BUDGETS")
    def POD_DISRUPTION_BUDGETS(cls) -> "ApiResource":
        '''API resource information for PodDisruptionBudget.'''
        return typing.cast("ApiResource", jsii.sget(cls, "POD_DISRUPTION_BUDGETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POD_SECURITY_POLICIES")
    def POD_SECURITY_POLICIES(cls) -> "ApiResource":
        '''API resource information for PodSecurityPolicy.'''
        return typing.cast("ApiResource", jsii.sget(cls, "POD_SECURITY_POLICIES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POD_TEMPLATES")
    def POD_TEMPLATES(cls) -> "ApiResource":
        '''API resource information for PodTemplate.'''
        return typing.cast("ApiResource", jsii.sget(cls, "POD_TEMPLATES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PODS")
    def PODS(cls) -> "ApiResource":
        '''API resource information for Pod.'''
        return typing.cast("ApiResource", jsii.sget(cls, "PODS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PRIORITY_CLASSES")
    def PRIORITY_CLASSES(cls) -> "ApiResource":
        '''API resource information for PriorityClass.'''
        return typing.cast("ApiResource", jsii.sget(cls, "PRIORITY_CLASSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PRIORITY_LEVEL_CONFIGURATIONS")
    def PRIORITY_LEVEL_CONFIGURATIONS(cls) -> "ApiResource":
        '''API resource information for PriorityLevelConfiguration.'''
        return typing.cast("ApiResource", jsii.sget(cls, "PRIORITY_LEVEL_CONFIGURATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REPLICA_SETS")
    def REPLICA_SETS(cls) -> "ApiResource":
        '''API resource information for ReplicaSet.'''
        return typing.cast("ApiResource", jsii.sget(cls, "REPLICA_SETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REPLICATION_CONTROLLERS")
    def REPLICATION_CONTROLLERS(cls) -> "ApiResource":
        '''API resource information for ReplicationController.'''
        return typing.cast("ApiResource", jsii.sget(cls, "REPLICATION_CONTROLLERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_QUOTAS")
    def RESOURCE_QUOTAS(cls) -> "ApiResource":
        '''API resource information for ResourceQuota.'''
        return typing.cast("ApiResource", jsii.sget(cls, "RESOURCE_QUOTAS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROLE_BINDINGS")
    def ROLE_BINDINGS(cls) -> "ApiResource":
        '''API resource information for RoleBinding.'''
        return typing.cast("ApiResource", jsii.sget(cls, "ROLE_BINDINGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROLES")
    def ROLES(cls) -> "ApiResource":
        '''API resource information for Role.'''
        return typing.cast("ApiResource", jsii.sget(cls, "ROLES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RUNTIME_CLASSES")
    def RUNTIME_CLASSES(cls) -> "ApiResource":
        '''API resource information for RuntimeClass.'''
        return typing.cast("ApiResource", jsii.sget(cls, "RUNTIME_CLASSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS")
    def SECRETS(cls) -> "ApiResource":
        '''API resource information for Secret.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SECRETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SELF_SUBJECT_ACCESS_REVIEWS")
    def SELF_SUBJECT_ACCESS_REVIEWS(cls) -> "ApiResource":
        '''API resource information for SelfSubjectAccessReview.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SELF_SUBJECT_ACCESS_REVIEWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SELF_SUBJECT_RULES_REVIEWS")
    def SELF_SUBJECT_RULES_REVIEWS(cls) -> "ApiResource":
        '''API resource information for SelfSubjectRulesReview.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SELF_SUBJECT_RULES_REVIEWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_ACCOUNTS")
    def SERVICE_ACCOUNTS(cls) -> "ApiResource":
        '''API resource information for ServiceAccount.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SERVICE_ACCOUNTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICES")
    def SERVICES(cls) -> "ApiResource":
        '''API resource information for Service.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SERVICES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STATEFUL_SETS")
    def STATEFUL_SETS(cls) -> "ApiResource":
        '''API resource information for StatefulSet.'''
        return typing.cast("ApiResource", jsii.sget(cls, "STATEFUL_SETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STORAGE_CLASSES")
    def STORAGE_CLASSES(cls) -> "ApiResource":
        '''API resource information for StorageClass.'''
        return typing.cast("ApiResource", jsii.sget(cls, "STORAGE_CLASSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SUBJECT_ACCESS_REVIEWS")
    def SUBJECT_ACCESS_REVIEWS(cls) -> "ApiResource":
        '''API resource information for SubjectAccessReview.'''
        return typing.cast("ApiResource", jsii.sget(cls, "SUBJECT_ACCESS_REVIEWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TOKEN_REVIEWS")
    def TOKEN_REVIEWS(cls) -> "ApiResource":
        '''API resource information for TokenReview.'''
        return typing.cast("ApiResource", jsii.sget(cls, "TOKEN_REVIEWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VALIDATING_WEBHOOK_CONFIGURATIONS")
    def VALIDATING_WEBHOOK_CONFIGURATIONS(cls) -> "ApiResource":
        '''API resource information for ValidatingWebhookConfiguration.'''
        return typing.cast("ApiResource", jsii.sget(cls, "VALIDATING_WEBHOOK_CONFIGURATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VOLUME_ATTACHMENTS")
    def VOLUME_ATTACHMENTS(cls) -> "ApiResource":
        '''API resource information for VolumeAttachment.'''
        return typing.cast("ApiResource", jsii.sget(cls, "VOLUME_ATTACHMENTS"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        '''The group portion of the API version (e.g. ``authorization.k8s.io``).'''
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of the resource type as it appears in the relevant API endpoint.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources

        Example::

            - "pods" or "pods/log"
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


class BasicAuthSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.BasicAuthSecret",
):
    '''Create a secret for basic authentication.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#basic-authentication-secret
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        password: builtins.str,
        username: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param password: The password or token for authentication.
        :param username: The user name for authentication.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BasicAuthSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicAuthSecretProps(
            password=password,
            username=username,
            immutable=immutable,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])


class ClusterRoleBinding(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ClusterRoleBinding",
):
    '''A ClusterRoleBinding grants permissions cluster-wide to a user or set of users.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        role: "IClusterRole",
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param role: The role to bind to.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRoleBinding.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterRoleBindingProps(role=role, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSubjects")
    def add_subjects(self, *subjects: ISubject) -> None:
        '''Adds a subject to the role.

        :param subjects: The subjects to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRoleBinding.add_subjects)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addSubjects", [*subjects]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "IClusterRole":
        return typing.cast("IClusterRole", jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="subjects")
    def subjects(self) -> typing.List[ISubject]:
        return typing.cast(typing.List[ISubject], jsii.get(self, "subjects"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ClusterRoleBindingProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "role": "role"},
)
class ClusterRoleBindingProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        role: "IClusterRole",
    ) -> None:
        '''Properties for ``ClusterRoleBinding``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param role: The role to bind to.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRoleBindingProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
        }
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def role(self) -> "IClusterRole":
        '''The role to bind to.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast("IClusterRole", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRoleBindingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ClusterRoleProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "aggregation_labels": "aggregationLabels",
        "rules": "rules",
    },
)
class ClusterRoleProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        aggregation_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ClusterRolePolicyRule, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for ``ClusterRole``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param aggregation_labels: Specify labels that should be used to locate ClusterRoles, whose rules will be automatically filled into this ClusterRole's rules.
        :param rules: A list of rules the role should allow. Default: []
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRoleProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument aggregation_labels", value=aggregation_labels, expected_type=type_hints["aggregation_labels"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if aggregation_labels is not None:
            self._values["aggregation_labels"] = aggregation_labels
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def aggregation_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specify labels that should be used to locate ClusterRoles, whose rules will be automatically filled into this ClusterRole's rules.'''
        result = self._values.get("aggregation_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[ClusterRolePolicyRule]]:
        '''A list of rules the role should allow.

        :default: []
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[ClusterRolePolicyRule]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.CommandProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class CommandProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Options for ``Probe.fromCommand()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CommandProbeOptions.__init__)
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommandProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.CommonSecretProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "immutable": "immutable"},
)
class CommonSecretProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Common properties for ``Secret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(CommonSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ConfigMapProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "binary_data": "binaryData",
        "data": "data",
        "immutable": "immutable",
    },
)
class ConfigMapProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        binary_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        immutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for initialization of ``ConfigMap``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param binary_data: BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. You can also add binary data using ``configMap.addBinaryData()``.
        :param data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. You can also add data using ``configMap.addData()``.
        :param immutable: If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMapProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument binary_data", value=binary_data, expected_type=type_hints["binary_data"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if binary_data is not None:
            self._values["binary_data"] = binary_data
        if data is not None:
            self._values["data"] = data
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def binary_data(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''BinaryData contains the binary data.

        Each key must consist of alphanumeric characters, '-', '_' or '.'.
        BinaryData can contain byte sequences that are not in the UTF-8 range. The
        keys stored in BinaryData must not overlap with the ones in the Data field,
        this is enforced during validation process.

        You can also add binary data using ``configMap.addBinaryData()``.
        '''
        result = self._values.get("binary_data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Data contains the configuration data.

        Each key must consist of alphanumeric characters, '-', '_' or '.'. Values
        with non-UTF-8 byte sequences must use the BinaryData field. The keys
        stored in Data must not overlap with the keys in the BinaryData field, this
        is enforced during validation process.

        You can also add data using ``configMap.addData()``.
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigMapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerConfigSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.DockerConfigSecret",
):
    '''Create a secret for storing credentials for accessing a container image registry.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        data: typing.Mapping[builtins.str, typing.Any],
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param data: JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DockerConfigSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DockerConfigSecretProps(
            data=data, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DockerConfigSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={"metadata": "metadata", "immutable": "immutable", "data": "data"},
)
class DockerConfigSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        data: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''Options for ``DockerConfigSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param data: JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(DockerConfigSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        self._values: typing.Dict[str, typing.Any] = {
            "data": data,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def data(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.

        :see: https://docs.docker.com/engine/reference/commandline/cli/#sample-configuration-file
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerConfigSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ExposeDeploymentViaIngressOptions",
    jsii_struct_bases=[
        DeploymentExposeViaServiceOptions, ExposeServiceViaIngressOptions
    ],
    name_mapping={
        "name": "name",
        "ports": "ports",
        "service_type": "serviceType",
        "ingress": "ingress",
        "path_type": "pathType",
    },
)
class ExposeDeploymentViaIngressOptions(
    DeploymentExposeViaServiceOptions,
    ExposeServiceViaIngressOptions,
):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ServicePort, typing.Dict[str, typing.Any]]]] = None,
        service_type: typing.Optional[ServiceType] = None,
        ingress: typing.Optional["Ingress"] = None,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> None:
        '''Options for exposing a deployment via an ingress.

        :param name: The name of the service to expose. If you'd like to expose the deployment multiple times, you must explicitly set a name starting from the second expose call. Default: - auto generated.
        :param ports: The ports that the service should bind to. Default: - extracted from the deployment.
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        :param path_type: The type of the path. Default: HttpIngressPathType.PREFIX
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExposeDeploymentViaIngressOptions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if ports is not None:
            self._values["ports"] = ports
        if service_type is not None:
            self._values["service_type"] = service_type
        if ingress is not None:
            self._values["ingress"] = ingress
        if path_type is not None:
            self._values["path_type"] = path_type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service to expose.

        If you'd like to expose the deployment multiple times,
        you must explicitly set a name starting from the second expose call.

        :default: - auto generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[ServicePort]]:
        '''The ports that the service should bind to.

        :default: - extracted from the deployment.
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[ServicePort]], result)

    @builtins.property
    def service_type(self) -> typing.Optional[ServiceType]:
        '''The type of the exposed service.

        :default: - ClusterIP.
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[ServiceType], result)

    @builtins.property
    def ingress(self) -> typing.Optional["Ingress"]:
        '''The ingress to add rules to.

        :default: - An ingress will be automatically created.
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["Ingress"], result)

    @builtins.property
    def path_type(self) -> typing.Optional[HttpIngressPathType]:
        '''The type of the path.

        :default: HttpIngressPathType.PREFIX
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional[HttpIngressPathType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExposeDeploymentViaIngressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISubject)
class Group(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.Group",
):
    '''Represents a group.'''

    @jsii.member(jsii_name="fromName")
    @builtins.classmethod
    def from_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> "Group":
        '''Reference a group by name.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Group.from_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast("Group", jsii.sinvoke(cls, "fromName", [scope, id, name]))

    @jsii.member(jsii_name="toSubjectConfiguration")
    def to_subject_configuration(self) -> SubjectConfiguration:
        '''Return the subject configuration.

        :see: ISubect.toSubjectConfiguration()
        '''
        return typing.cast(SubjectConfiguration, jsii.invoke(self, "toSubjectConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroup"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.HttpGetProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
        "port": "port",
        "scheme": "scheme",
    },
)
class HttpGetProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[ConnectionScheme] = None,
    ) -> None:
        '''Options for ``Probe.fromHttpGet()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        :param scheme: Scheme to use for connecting to the host (HTTP or HTTPS). Default: ConnectionScheme.HTTP
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HttpGetProbeOptions.__init__)
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to use when sending the GET request.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[ConnectionScheme]:
        '''Scheme to use for connecting to the host (HTTP or HTTPS).

        :default: ConnectionScheme.HTTP
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[ConnectionScheme], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGetProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk8s-plus-23.IClusterRole")
class IClusterRole(IResource, typing_extensions.Protocol):
    '''Represents a cluster-level role.'''

    pass


class _IClusterRoleProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    '''Represents a cluster-level role.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IClusterRole"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRole).__jsii_proxy_class__ = lambda : _IClusterRoleProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IConfigMap")
class IConfigMap(IResource, typing_extensions.Protocol):
    '''Represents a config map.'''

    pass


class _IConfigMapProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    '''Represents a config map.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IConfigMap"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigMap).__jsii_proxy_class__ = lambda : _IConfigMapProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IPersistentVolume")
class IPersistentVolume(IResource, typing_extensions.Protocol):
    '''Contract of a ``PersistentVolumeClaim``.'''

    pass


class _IPersistentVolumeProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    '''Contract of a ``PersistentVolumeClaim``.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IPersistentVolume"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPersistentVolume).__jsii_proxy_class__ = lambda : _IPersistentVolumeProxy


@jsii.interface(jsii_type="cdk8s-plus-23.IPersistentVolumeClaim")
class IPersistentVolumeClaim(IResource, typing_extensions.Protocol):
    '''Contract of a ``PersistentVolumeClaim``.'''

    pass


class _IPersistentVolumeClaimProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    '''Contract of a ``PersistentVolumeClaim``.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-23.IPersistentVolumeClaim"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPersistentVolumeClaim).__jsii_proxy_class__ = lambda : _IPersistentVolumeClaimProxy


class Ingress(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Ingress"):
    '''Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend.

    An Ingress can be configured to give services
    externally-reachable urls, load balance traffic, terminate SSL, offer name
    based virtual hosting etc.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        default_backend: typing.Optional[IngressBackend] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[IngressRule, typing.Dict[str, typing.Any]]]] = None,
        tls: typing.Optional[typing.Sequence[typing.Union[IngressTls, typing.Dict[str, typing.Any]]]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_backend: The default backend services requests that do not match any rule. Using this option or the ``addDefaultBackend()`` method is equivalent to adding a rule with both ``path`` and ``host`` undefined.
        :param rules: Routing rules for this ingress. Each rule must define an ``IngressBackend`` that will receive the requests that match this rule. If both ``host`` and ``path`` are not specifiec, this backend will be used as the default backend of the ingress. You can also add rules later using ``addRule()``, ``addHostRule()``, ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        :param tls: TLS settings for this ingress. Using this option tells the ingress controller to expose a TLS endpoint. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = IngressProps(
            default_backend=default_backend, rules=rules, tls=tls, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDefaultBackend")
    def add_default_backend(self, backend: IngressBackend) -> None:
        '''Defines the default backend for this ingress.

        A default backend capable of
        servicing requests that don't match any rule.

        :param backend: The backend to use for requests that do not match any rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_default_backend)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
        return typing.cast(None, jsii.invoke(self, "addDefaultBackend", [backend]))

    @jsii.member(jsii_name="addHostDefaultBackend")
    def add_host_default_backend(
        self,
        host: builtins.str,
        backend: IngressBackend,
    ) -> None:
        '''Specify a default backend for a specific host name.

        This backend will be used as a catch-all for requests
        targeted to this host name (the ``Host`` header matches this value).

        :param host: The host name to match.
        :param backend: The backend to route to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_host_default_backend)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
        return typing.cast(None, jsii.invoke(self, "addHostDefaultBackend", [host, backend]))

    @jsii.member(jsii_name="addHostRule")
    def add_host_rule(
        self,
        host: builtins.str,
        path: builtins.str,
        backend: IngressBackend,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> None:
        '''Adds an ingress rule applied to requests to a specific host and a specific HTTP path (the ``Host`` header matches this value).

        :param host: The host name.
        :param path: The HTTP path.
        :param backend: The backend to route requests to.
        :param path_type: How the path is matched against request paths.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_host_rule)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        return typing.cast(None, jsii.invoke(self, "addHostRule", [host, path, backend, path_type]))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        path: builtins.str,
        backend: IngressBackend,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> None:
        '''Adds an ingress rule applied to requests sent to a specific HTTP path.

        :param path: The HTTP path.
        :param backend: The backend to route requests to.
        :param path_type: How the path is matched against request paths.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_rule)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        return typing.cast(None, jsii.invoke(self, "addRule", [path, backend, path_type]))

    @jsii.member(jsii_name="addRules")
    def add_rules(self, *rules: IngressRule) -> None:
        '''Adds rules to this ingress.

        :param rules: The rules to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_rules)
            check_type(argname="argument rules", value=rules, expected_type=typing.Tuple[type_hints["rules"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addRules", [*rules]))

    @jsii.member(jsii_name="addTls")
    def add_tls(
        self,
        tls: typing.Sequence[typing.Union[IngressTls, typing.Dict[str, typing.Any]]],
    ) -> None:
        '''
        :param tls: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ingress.add_tls)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        return typing.cast(None, jsii.invoke(self, "addTls", [tls]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.IngressProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "default_backend": "defaultBackend",
        "rules": "rules",
        "tls": "tls",
    },
)
class IngressProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        default_backend: typing.Optional[IngressBackend] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[IngressRule, typing.Dict[str, typing.Any]]]] = None,
        tls: typing.Optional[typing.Sequence[typing.Union[IngressTls, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for ``Ingress``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param default_backend: The default backend services requests that do not match any rule. Using this option or the ``addDefaultBackend()`` method is equivalent to adding a rule with both ``path`` and ``host`` undefined.
        :param rules: Routing rules for this ingress. Each rule must define an ``IngressBackend`` that will receive the requests that match this rule. If both ``host`` and ``path`` are not specifiec, this backend will be used as the default backend of the ingress. You can also add rules later using ``addRule()``, ``addHostRule()``, ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        :param tls: TLS settings for this ingress. Using this option tells the ingress controller to expose a TLS endpoint. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(IngressProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument default_backend", value=default_backend, expected_type=type_hints["default_backend"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if default_backend is not None:
            self._values["default_backend"] = default_backend
        if rules is not None:
            self._values["rules"] = rules
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def default_backend(self) -> typing.Optional[IngressBackend]:
        '''The default backend services requests that do not match any rule.

        Using this option or the ``addDefaultBackend()`` method is equivalent to
        adding a rule with both ``path`` and ``host`` undefined.
        '''
        result = self._values.get("default_backend")
        return typing.cast(typing.Optional[IngressBackend], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[IngressRule]]:
        '''Routing rules for this ingress.

        Each rule must define an ``IngressBackend`` that will receive the requests
        that match this rule. If both ``host`` and ``path`` are not specifiec, this
        backend will be used as the default backend of the ingress.

        You can also add rules later using ``addRule()``, ``addHostRule()``,
        ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[IngressRule]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.List[IngressTls]]:
        '''TLS settings for this ingress.

        Using this option tells the ingress controller to expose a TLS endpoint.
        Currently the Ingress only supports a single TLS port, 443. If multiple
        members of this list specify different hosts, they will be multiplexed on
        the same port according to the hostname specified through the SNI TLS
        extension, if the ingress controller fulfilling the ingress supports SNI.
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.List[IngressTls]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INamespaceSelector, INetworkPolicyPeer)
class Namespace(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Namespace"):
    '''In Kubernetes, namespaces provides a mechanism for isolating groups of resources within a single cluster.

    Names of resources need to be unique within a namespace, but not across namespaces.
    Namespace-based scoping is applicable only for namespaced objects (e.g. Deployments, Services, etc) and
    not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc).
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Namespace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NamespaceProps(metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="toNamespaceSelectorConfig")
    def to_namespace_selector_config(self) -> NamespaceSelectorConfig:
        '''Return the configuration of this selector.

        :see: INamespaceSelector.toNamespaceSelectorConfig()
        '''
        return typing.cast(NamespaceSelectorConfig, jsii.invoke(self, "toNamespaceSelectorConfig", []))

    @jsii.member(jsii_name="toNetworkPolicyPeerConfig")
    def to_network_policy_peer_config(self) -> NetworkPolicyPeerConfig:
        '''Return the configuration of this peer.

        :see: INetworkPolicyPeer.toNetworkPolicyPeerConfig()
        '''
        return typing.cast(NetworkPolicyPeerConfig, jsii.invoke(self, "toNetworkPolicyPeerConfig", []))

    @jsii.member(jsii_name="toPodSelector")
    def to_pod_selector(self) -> typing.Optional[IPodSelector]:
        '''Convert the peer into a pod selector, if possible.

        :see: INetworkPolicyPeer.toPodSelector()
        '''
        return typing.cast(typing.Optional[IPodSelector], jsii.invoke(self, "toPodSelector", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NAME_LABEL")
    def NAME_LABEL(cls) -> builtins.str:
        '''
        :see: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#automatic-labelling
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NAME_LABEL"))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NamespaceProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata"},
)
class NamespaceProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''Properties for ``Namespace``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(NamespaceProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicy(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.NetworkPolicy",
):
    '''Control traffic flow at the IP address or port level (OSI layer 3 or 4), network policies are an application-centric construct which allow you to specify how a pod is allowed to communicate with various network peers.

    - Outgoing traffic is allowed if there are no network policies selecting
      the pod (and cluster policy otherwise allows the traffic),
      OR if the traffic matches at least one egress rule across all of the
      network policies that select the pod.
    - Incoming traffic is allowed to a pod if there are no network policies
      selecting the pod (and cluster policy otherwise allows the traffic),
      OR if the traffic source is the pod's local node,
      OR if the traffic matches at least one ingress rule across all of
      the network policies that select the pod.

    Network policies do not conflict; they are additive.
    If any policy or policies apply to a given pod for a given
    direction, the connections allowed in that direction from
    that pod is the union of what the applicable policies allow.
    Thus, order of evaluation does not affect the policy result.

    For a connection from a source pod to a destination pod to be allowed,
    both the egress policy on the source pod and the ingress policy on the
    destination pod need to allow the connection.
    If either side does not allow the connection, it will not happen.

    :see: https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        egress: typing.Optional[typing.Union[NetworkPolicyTraffic, typing.Dict[str, typing.Any]]] = None,
        ingress: typing.Optional[typing.Union[NetworkPolicyTraffic, typing.Dict[str, typing.Any]]] = None,
        selector: typing.Optional[IPodSelector] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param egress: Egress traffic configuration. Default: - the policy doesn't change egress behavior of the pods it selects.
        :param ingress: Ingress traffic configuration. Default: - the policy doesn't change ingress behavior of the pods it selects.
        :param selector: Which pods does this policy object applies to. This can either be a single pod / workload, or a grouping of pods selected via the ``Pods.select`` function. Rules is applied to any pods selected by this property. Multiple network policies can select the same set of pods. In this case, the rules for each are combined additively. Note that Default: - will select all pods in the namespace of the policy.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NetworkPolicyProps(
            egress=egress, ingress=ingress, selector=selector, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addEgressRule")
    def add_egress_rule(
        self,
        peer: INetworkPolicyPeer,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Allow outgoing traffic to the peer.

        If ports are not passed, traffic will be allowed on all ports.

        :param peer: -
        :param ports: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicy.add_egress_rule)
            check_type(argname="argument peer", value=peer, expected_type=type_hints["peer"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        return typing.cast(None, jsii.invoke(self, "addEgressRule", [peer, ports]))

    @jsii.member(jsii_name="addIngressRule")
    def add_ingress_rule(
        self,
        peer: INetworkPolicyPeer,
        ports: typing.Optional[typing.Sequence[NetworkPolicyPort]] = None,
    ) -> None:
        '''Allow incoming traffic from the peer.

        If ports are not passed, traffic will be allowed on all ports.

        :param peer: -
        :param ports: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicy.add_ingress_rule)
            check_type(argname="argument peer", value=peer, expected_type=type_hints["peer"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        return typing.cast(None, jsii.invoke(self, "addIngressRule", [peer, ports]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.NetworkPolicyProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "egress": "egress",
        "ingress": "ingress",
        "selector": "selector",
    },
)
class NetworkPolicyProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        egress: typing.Optional[typing.Union[NetworkPolicyTraffic, typing.Dict[str, typing.Any]]] = None,
        ingress: typing.Optional[typing.Union[NetworkPolicyTraffic, typing.Dict[str, typing.Any]]] = None,
        selector: typing.Optional[IPodSelector] = None,
    ) -> None:
        '''Properties for ``NetworkPolicy``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param egress: Egress traffic configuration. Default: - the policy doesn't change egress behavior of the pods it selects.
        :param ingress: Ingress traffic configuration. Default: - the policy doesn't change ingress behavior of the pods it selects.
        :param selector: Which pods does this policy object applies to. This can either be a single pod / workload, or a grouping of pods selected via the ``Pods.select`` function. Rules is applied to any pods selected by this property. Multiple network policies can select the same set of pods. In this case, the rules for each are combined additively. Note that Default: - will select all pods in the namespace of the policy.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(egress, dict):
            egress = NetworkPolicyTraffic(**egress)
        if isinstance(ingress, dict):
            ingress = NetworkPolicyTraffic(**ingress)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPolicyProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if egress is not None:
            self._values["egress"] = egress
        if ingress is not None:
            self._values["ingress"] = ingress
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def egress(self) -> typing.Optional[NetworkPolicyTraffic]:
        '''Egress traffic configuration.

        :default: - the policy doesn't change egress behavior of the pods it selects.
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[NetworkPolicyTraffic], result)

    @builtins.property
    def ingress(self) -> typing.Optional[NetworkPolicyTraffic]:
        '''Ingress traffic configuration.

        :default: - the policy doesn't change ingress behavior of the pods it selects.
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[NetworkPolicyTraffic], result)

    @builtins.property
    def selector(self) -> typing.Optional[IPodSelector]:
        '''Which pods does this policy object applies to.

        This can either be a single pod / workload, or a grouping of pods selected
        via the ``Pods.select`` function. Rules is applied to any pods selected by this property.
        Multiple network policies can select the same set of pods.
        In this case, the rules for each are combined additively.

        Note that

        :default: - will select all pods in the namespace of the policy.
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[IPodSelector], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPersistentVolume, IStorage)
class PersistentVolume(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.PersistentVolume",
):
    '''A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes.

    It is a resource in the cluster just like a node is a cluster resource.
    PVs are volume plugins like Volumes, but have a lifecycle independent of any
    individual Pod that uses the PV. This API object captures the details of the
    implementation of the storage, be that NFS, iSCSI, or a
    cloud-provider-specific storage system.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PersistentVolumeProps(
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPersistentVolumeName")
    @builtins.classmethod
    def from_persistent_volume_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        volume_name: builtins.str,
    ) -> IPersistentVolume:
        '''Imports a pv from the cluster as a reference.

        :param scope: -
        :param id: -
        :param volume_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolume.from_persistent_volume_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument volume_name", value=volume_name, expected_type=type_hints["volume_name"])
        return typing.cast(IPersistentVolume, jsii.sinvoke(cls, "fromPersistentVolumeName", [scope, id, volume_name]))

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> Volume:
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast(Volume, jsii.invoke(self, "asVolume", []))

    @jsii.member(jsii_name="bind")
    def bind(self, claim: IPersistentVolumeClaim) -> None:
        '''Bind a volume to a specific claim.

        Note that you must also bind the claim to the volume.

        :param claim: The PVC to bind to.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolume.bind)
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
        return typing.cast(None, jsii.invoke(self, "bind", [claim]))

    @jsii.member(jsii_name="reserve")
    def reserve(self) -> "PersistentVolumeClaim":
        '''Reserve a ``PersistentVolume`` by creating a ``PersistentVolumeClaim`` that is wired to claim this volume.

        Note that this method will throw in case the volume is already claimed.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reserving-a-persistentvolume
        '''
        return typing.cast("PersistentVolumeClaim", jsii.invoke(self, "reserve", []))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> PersistentVolumeMode:
        '''Volume mode of this volume.'''
        return typing.cast(PersistentVolumeMode, jsii.get(self, "mode"))

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> PersistentVolumeReclaimPolicy:
        '''Reclaim policy of this volume.'''
        return typing.cast(PersistentVolumeReclaimPolicy, jsii.get(self, "reclaimPolicy"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Access modes requirement of this claim.'''
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], jsii.get(self, "accessModes"))

    @builtins.property
    @jsii.member(jsii_name="claim")
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''PVC this volume is bound to.

        Undefined means this volume is not yet
        claimed by any PVC.
        '''
        return typing.cast(typing.Optional[IPersistentVolumeClaim], jsii.get(self, "claim"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Mount options of this volume.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptions"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Storage size of this volume.'''
        return typing.cast(typing.Optional[cdk8s.Size], jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Storage class this volume belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassName"))


@jsii.implements(IPersistentVolumeClaim)
class PersistentVolumeClaim(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.PersistentVolumeClaim",
):
    '''A PersistentVolumeClaim (PVC) is a request for storage by a user.

    It is similar to a Pod. Pods consume node resources and PVCs consume PV resources.
    Pods can request specific levels of resources (CPU and Memory).
    Claims can request specific size and access modes
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume: typing.Optional[IPersistentVolume] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_modes: Contains the access modes the volume should support. Default: - No access modes requirement.
        :param storage: Minimum storage size the volume should have. Default: - No storage requirement.
        :param storage_class_name: Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:. - If the admission plugin is turned on, the storage class marked as default will be used. - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class. Default: - Not set.
        :param volume: The PersistentVolume backing this claim. The control plane still checks that storage class, access modes, and requested storage size on the volume are valid. Note that in order to guarantee a proper binding, the volume should also define a ``claimRef`` referring to this claim. Otherwise, the volume may be claimed be other pvc's before it gets a chance to bind to this one. If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily create a bi-directional bounded claim. Default: - No specific volume binding.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeClaim.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PersistentVolumeClaimProps(
            access_modes=access_modes,
            storage=storage,
            storage_class_name=storage_class_name,
            volume=volume,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClaimName")
    @builtins.classmethod
    def from_claim_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        claim_name: builtins.str,
    ) -> IPersistentVolumeClaim:
        '''Imports a pvc from the cluster as a reference.

        :param scope: -
        :param id: -
        :param claim_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeClaim.from_claim_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument claim_name", value=claim_name, expected_type=type_hints["claim_name"])
        return typing.cast(IPersistentVolumeClaim, jsii.sinvoke(cls, "fromClaimName", [scope, id, claim_name]))

    @jsii.member(jsii_name="bind")
    def bind(self, vol: IPersistentVolume) -> None:
        '''Bind a claim to a specific volume.

        Note that you must also bind the volume to the claim.

        :param vol: The PV to bind to.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeClaim.bind)
            check_type(argname="argument vol", value=vol, expected_type=type_hints["vol"])
        return typing.cast(None, jsii.invoke(self, "bind", [vol]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> PersistentVolumeMode:
        '''Volume mode requirement of this claim.'''
        return typing.cast(PersistentVolumeMode, jsii.get(self, "volumeMode"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Access modes requirement of this claim.'''
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], jsii.get(self, "accessModes"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Storage requirement of this claim.'''
        return typing.cast(typing.Optional[cdk8s.Size], jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Storage class requirment of this claim.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassName"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> typing.Optional[IPersistentVolume]:
        '''PV this claim is bound to.

        Undefined means the claim is not bound
        to any specific volume.
        '''
        return typing.cast(typing.Optional[IPersistentVolume], jsii.get(self, "volume"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PersistentVolumeClaimProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume": "volume",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeClaimProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume: typing.Optional[IPersistentVolume] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
    ) -> None:
        '''Properties for ``PersistentVolumeClaim``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains the access modes the volume should support. Default: - No access modes requirement.
        :param storage: Minimum storage size the volume should have. Default: - No storage requirement.
        :param storage_class_name: Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:. - If the admission plugin is turned on, the storage class marked as default will be used. - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class. Default: - Not set.
        :param volume: The PersistentVolume backing this claim. The control plane still checks that storage class, access modes, and requested storage size on the volume are valid. Note that in order to guarantee a proper binding, the volume should also define a ``claimRef`` referring to this claim. Otherwise, the volume may be claimed be other pvc's before it gets a chance to bind to this one. If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily create a bi-directional bounded claim. Default: - No specific volume binding.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeClaimProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume is not None:
            self._values["volume"] = volume
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains the access modes the volume should support.

        :default: - No access modes requirement.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Minimum storage size the volume should have.

        :default: - No storage requirement.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:.

        - If the admission plugin is turned on, the storage class marked as default will be used.
        - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class.

        :default: - Not set.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume(self) -> typing.Optional[IPersistentVolume]:
        '''The PersistentVolume backing this claim.

        The control plane still checks that storage class, access modes,
        and requested storage size on the volume are valid.

        Note that in order to guarantee a proper binding, the volume should
        also define a ``claimRef`` referring to this claim. Otherwise, the volume may be
        claimed be other pvc's before it gets a chance to bind to this one.

        If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily
        create a bi-directional bounded claim.

        :default: - No specific volume binding.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding.
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[IPersistentVolume], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeClaimProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PersistentVolumeProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
    ) -> None:
        '''Properties for ``PersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Pod(AbstractPod, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Pod"):
    '''Pod is a collection of containers that can run on a host.

    This resource is
    created by clients and scheduled onto hosts.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Pod.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PodProps(
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADDRESS_LABEL")
    def ADDRESS_LABEL(cls) -> builtins.str:
        '''This label is autoamtically added by cdk8s to any pod.

        It provides
        a unique and stable identifier for the pod.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ADDRESS_LABEL"))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> PodConnections:
        return typing.cast(PodConnections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(self) -> PodScheduling:
        return typing.cast(PodScheduling, jsii.get(self, "scheduling"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.PodProps",
    jsii_struct_bases=[AbstractPodProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
    },
)
class PodProps(AbstractPodProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''Properties for ``Pod``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(PodProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.SecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "string_data": "stringData",
        "type": "type",
    },
)
class SecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        string_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ``Secret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param string_data: stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.
        :param type: Optional type associated with the secret. Used to facilitate programmatic handling of secret data by various controllers. Default: undefined - Don't set a type.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(SecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument string_data", value=string_data, expected_type=type_hints["string_data"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable
        if string_data is not None:
            self._values["string_data"] = string_data
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def string_data(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''stringData allows specifying non-binary secret data in string form.

        It is
        provided as a write-only convenience method. All keys and values are merged
        into the data field on write, overwriting any existing values. It is never
        output when reading from the API.
        '''
        result = self._values.get("string_data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Optional type associated with the secret.

        Used to facilitate programmatic
        handling of secret data by various controllers.

        :default: undefined - Don't set a type.
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.ServiceAccountTokenSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "service_account": "serviceAccount",
    },
)
class ServiceAccountTokenSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        service_account: IServiceAccount,
    ) -> None:
        '''Options for ``ServiceAccountTokenSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param service_account: The service account to store a secret for.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceAccountTokenSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_account": service_account,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_account(self) -> IServiceAccount:
        '''The service account to store a secret for.'''
        result = self._values.get("service_account")
        assert result is not None, "Required property 'service_account' is missing"
        return typing.cast(IServiceAccount, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountTokenSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.SshAuthSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "ssh_private_key": "sshPrivateKey",
    },
)
class SshAuthSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        ssh_private_key: builtins.str,
    ) -> None:
        '''Options for ``SshAuthSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param ssh_private_key: The SSH private key to use.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(SshAuthSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument ssh_private_key", value=ssh_private_key, expected_type=type_hints["ssh_private_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "ssh_private_key": ssh_private_key,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ssh_private_key(self) -> builtins.str:
        '''The SSH private key to use.'''
        result = self._values.get("ssh_private_key")
        assert result is not None, "Required property 'ssh_private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SshAuthSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.TlsSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "tls_cert": "tlsCert",
        "tls_key": "tlsKey",
    },
)
class TlsSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        tls_cert: builtins.str,
        tls_key: builtins.str,
    ) -> None:
        '''Options for ``TlsSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param tls_cert: The TLS cert.
        :param tls_key: The TLS key.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(TlsSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument tls_cert", value=tls_cert, expected_type=type_hints["tls_cert"])
            check_type(argname="argument tls_key", value=tls_key, expected_type=type_hints["tls_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "tls_cert": tls_cert,
            "tls_key": tls_key,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_cert(self) -> builtins.str:
        '''The TLS cert.'''
        result = self._values.get("tls_cert")
        assert result is not None, "Required property 'tls_cert' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tls_key(self) -> builtins.str:
        '''The TLS key.'''
        result = self._values.get("tls_key")
        assert result is not None, "Required property 'tls_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Workload(
    AbstractPod,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk8s-plus-23.Workload",
):
    '''A workload is an application running on Kubernetes.

    Whether your workload is a single
    component or several that work together, on Kubernetes you run it inside a set of pods.
    In Kubernetes, a Pod represents a set of running containers on your cluster.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Workload.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WorkloadProps(
            pod_metadata=pod_metadata,
            select=select,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="select")
    def select(self, *selectors: LabelSelector) -> None:
        '''Configure selectors for this workload.

        :param selectors: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Workload.select)
            check_type(argname="argument selectors", value=selectors, expected_type=typing.Tuple[type_hints["selectors"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "select", [*selectors]))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> PodConnections:
        return typing.cast(PodConnections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(self) -> typing.List[LabelSelectorRequirement]:
        '''The expression matchers this workload will use in order to select pods.

        Returns a a copy. Use ``select()`` to add expression matchers.
        '''
        return typing.cast(typing.List[LabelSelectorRequirement], jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The label matchers this workload will use in order to select pods.

        Returns a a copy. Use ``select()`` to add label matchers.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @builtins.property
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''The metadata of pods in this workload.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(self) -> WorkloadScheduling:
        return typing.cast(WorkloadScheduling, jsii.get(self, "scheduling"))


class _WorkloadProxy(
    Workload,
    jsii.proxy_for(AbstractPod), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Workload).__jsii_proxy_class__ = lambda : _WorkloadProxy


@jsii.data_type(
    jsii_type="cdk8s-plus-23.WorkloadProps",
    jsii_struct_bases=[AbstractPodProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "select": "select",
    },
)
class WorkloadProps(AbstractPodProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``Workload``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument pod_metadata", value=pod_metadata, expected_type=type_hints["pod_metadata"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if select is not None:
            self._values["select"] = select

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata of this workload.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod label selector for this workload and add it to the pod metadata.

        This ensures this workload manages pods created by
        its pod template.

        :default: true
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsElasticBlockStorePersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.AwsElasticBlockStorePersistentVolume",
):
    '''Represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod.

    :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsElasticBlockStorePersistentVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AwsElasticBlockStorePersistentVolumeProps(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        '''Volume id of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> typing.Optional[jsii.Number]:
        '''Partition of this volume.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partition"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AwsElasticBlockStorePersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class AwsElasticBlockStorePersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``AwsElasticBlockStorePersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(AwsElasticBlockStorePersistentVolumeProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "volume_id": volume_id,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume).

        More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsElasticBlockStorePersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AzureDiskPersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.AzureDiskPersistentVolume",
):
    '''AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param disk_name: The Name of the data disk in the blob storage.
        :param disk_uri: The URI the data disk in the blob storage.
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzureDiskPersistentVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AzureDiskPersistentVolumeProps(
            disk_name=disk_name,
            disk_uri=disk_uri,
            caching_mode=caching_mode,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="azureKind")
    def azure_kind(self) -> AzureDiskPersistentVolumeKind:
        '''Azure kind of this volume.'''
        return typing.cast(AzureDiskPersistentVolumeKind, jsii.get(self, "azureKind"))

    @builtins.property
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> AzureDiskPersistentVolumeCachingMode:
        '''Caching mode of this volume.'''
        return typing.cast(AzureDiskPersistentVolumeCachingMode, jsii.get(self, "cachingMode"))

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        '''Disk name of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @builtins.property
    @jsii.member(jsii_name="diskUri")
    def disk_uri(self) -> builtins.str:
        '''Disk URI of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "diskUri"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.AzureDiskPersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "disk_name": "diskName",
        "disk_uri": "diskUri",
        "caching_mode": "cachingMode",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class AzureDiskPersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``AzureDiskPersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param disk_name: The Name of the data disk in the blob storage.
        :param disk_uri: The URI the data disk in the blob storage.
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(AzureDiskPersistentVolumeProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument disk_uri", value=disk_uri, expected_type=type_hints["disk_uri"])
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "disk_name": disk_name,
            "disk_uri": disk_uri,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if caching_mode is not None:
            self._values["caching_mode"] = caching_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.'''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.'''
        result = self._values.get("disk_uri")
        assert result is not None, "Required property 'disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_mode(self) -> typing.Optional[AzureDiskPersistentVolumeCachingMode]:
        '''Host Caching mode.

        :default: - AzureDiskPersistentVolumeCachingMode.NONE.
        '''
        result = self._values.get("caching_mode")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeCachingMode], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system.

        :default: 'ext4'
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[AzureDiskPersistentVolumeKind]:
        '''Kind of disk.

        :default: AzureDiskPersistentVolumeKind.SHARED
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeKind], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureDiskPersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-23.BasicAuthSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "password": "password",
        "username": "username",
    },
)
class BasicAuthSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Options for ``BasicAuthSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param password: The password or token for authentication.
        :param username: The user name for authentication.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(BasicAuthSecretProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument immutable", value=immutable, expected_type=type_hints["immutable"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password or token for authentication.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name for authentication.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicAuthSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IClusterRole, IRole)
class ClusterRole(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.ClusterRole",
):
    '''ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        aggregation_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ClusterRolePolicyRule, typing.Dict[str, typing.Any]]]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param aggregation_labels: Specify labels that should be used to locate ClusterRoles, whose rules will be automatically filled into this ClusterRole's rules.
        :param rules: A list of rules the role should allow. Default: []
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterRoleProps(
            aggregation_labels=aggregation_labels, rules=rules, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterRoleName")
    @builtins.classmethod
    def from_cluster_role_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> IClusterRole:
        '''Imports a role from the cluster as a reference.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.from_cluster_role_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IClusterRole, jsii.sinvoke(cls, "fromClusterRoleName", [scope, id, name]))

    @jsii.member(jsii_name="aggregate")
    def aggregate(self, key: builtins.str, value: builtins.str) -> None:
        '''Aggregate rules from roles matching this label selector.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.aggregate)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "aggregate", [key, value]))

    @jsii.member(jsii_name="allow")
    def allow(
        self,
        verbs: typing.Sequence[builtins.str],
        *endpoints: IApiEndpoint,
    ) -> None:
        '''Add permission to perform a list of HTTP verbs on a collection of resources.

        :param verbs: -
        :param endpoints: The endpoints(s) to apply to.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow)
            check_type(argname="argument verbs", value=verbs, expected_type=type_hints["verbs"])
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allow", [verbs, *endpoints]))

    @jsii.member(jsii_name="allowCreate")
    def allow_create(self, *endpoints: IApiEndpoint) -> None:
        '''Add "create" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_create)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowCreate", [*endpoints]))

    @jsii.member(jsii_name="allowDelete")
    def allow_delete(self, *endpoints: IApiEndpoint) -> None:
        '''Add "delete" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_delete)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowDelete", [*endpoints]))

    @jsii.member(jsii_name="allowDeleteCollection")
    def allow_delete_collection(self, *endpoints: IApiEndpoint) -> None:
        '''Add "deletecollection" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_delete_collection)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowDeleteCollection", [*endpoints]))

    @jsii.member(jsii_name="allowGet")
    def allow_get(self, *endpoints: IApiEndpoint) -> None:
        '''Add "get" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_get)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowGet", [*endpoints]))

    @jsii.member(jsii_name="allowList")
    def allow_list(self, *endpoints: IApiEndpoint) -> None:
        '''Add "list" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_list)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowList", [*endpoints]))

    @jsii.member(jsii_name="allowPatch")
    def allow_patch(self, *endpoints: IApiEndpoint) -> None:
        '''Add "patch" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_patch)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowPatch", [*endpoints]))

    @jsii.member(jsii_name="allowRead")
    def allow_read(self, *endpoints: IApiEndpoint) -> None:
        '''Add "get", "list", and "watch" permissions for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_read)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowRead", [*endpoints]))

    @jsii.member(jsii_name="allowReadWrite")
    def allow_read_write(self, *endpoints: IApiEndpoint) -> None:
        '''Add "get", "list", "watch", "create", "update", "patch", "delete", and "deletecollection" permissions for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_read_write)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowReadWrite", [*endpoints]))

    @jsii.member(jsii_name="allowUpdate")
    def allow_update(self, *endpoints: IApiEndpoint) -> None:
        '''Add "update" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_update)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowUpdate", [*endpoints]))

    @jsii.member(jsii_name="allowWatch")
    def allow_watch(self, *endpoints: IApiEndpoint) -> None:
        '''Add "watch" permission for the resources.

        :param endpoints: The resource(s) to apply to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.allow_watch)
            check_type(argname="argument endpoints", value=endpoints, expected_type=typing.Tuple[type_hints["endpoints"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "allowWatch", [*endpoints]))

    @jsii.member(jsii_name="bind")
    def bind(self, *subjects: ISubject) -> ClusterRoleBinding:
        '''Create a ClusterRoleBinding that binds the permissions in this ClusterRole to a list of subjects, without namespace restrictions.

        :param subjects: a list of subjects to bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.bind)
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(ClusterRoleBinding, jsii.invoke(self, "bind", [*subjects]))

    @jsii.member(jsii_name="bindInNamespace")
    def bind_in_namespace(
        self,
        namespace: builtins.str,
        *subjects: ISubject,
    ) -> RoleBinding:
        '''Create a RoleBinding that binds the permissions in this ClusterRole to a list of subjects, that will only apply to the given namespace.

        :param namespace: the namespace to limit permissions to.
        :param subjects: a list of subjects to bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.bind_in_namespace)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument subjects", value=subjects, expected_type=typing.Tuple[type_hints["subjects"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(RoleBinding, jsii.invoke(self, "bindInNamespace", [namespace, *subjects]))

    @jsii.member(jsii_name="combine")
    def combine(self, rol: "ClusterRole") -> None:
        '''Combines the rules of the argument ClusterRole into this ClusterRole using aggregation labels.

        :param rol: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterRole.combine)
            check_type(argname="argument rol", value=rol, expected_type=type_hints["rol"])
        return typing.cast(None, jsii.invoke(self, "combine", [rol]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.List[ClusterRolePolicyRule]:
        '''Rules associaated with this Role.

        Returns a copy, use ``allow`` to add rules.
        '''
        return typing.cast(typing.List[ClusterRolePolicyRule], jsii.get(self, "rules"))


@jsii.implements(IConfigMap)
class ConfigMap(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.ConfigMap"):
    '''ConfigMap holds configuration data for pods to consume.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        binary_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param binary_data: BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. You can also add binary data using ``configMap.addBinaryData()``.
        :param data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. You can also add data using ``configMap.addData()``.
        :param immutable: If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ConfigMapProps(
            binary_data=binary_data, data=data, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigMapName")
    @builtins.classmethod
    def from_config_map_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> IConfigMap:
        '''Represents a ConfigMap created elsewhere.

        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.from_config_map_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IConfigMap, jsii.sinvoke(cls, "fromConfigMapName", [scope, id, name]))

    @jsii.member(jsii_name="addBinaryData")
    def add_binary_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a binary data entry to the config map.

        BinaryData can contain byte
        sequences that are not in the UTF-8 range.

        :param key: The key.
        :param value: The value.

        :throws: if there is either a ``data`` or ``binaryData`` entry with the same key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.add_binary_data)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addBinaryData", [key, value]))

    @jsii.member(jsii_name="addData")
    def add_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a data entry to the config map.

        :param key: The key.
        :param value: The value.

        :throws: if there is either a ``data`` or ``binaryData`` entry with the same key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.add_data)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addData", [key, value]))

    @jsii.member(jsii_name="addDirectory")
    def add_directory(
        self,
        local_dir: builtins.str,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a directory to the ConfigMap.

        :param local_dir: A path to a local directory.
        :param exclude: Glob patterns to exclude when adding files. Default: - include all files
        :param key_prefix: A prefix to add to all keys in the config map. Default: ""
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.add_directory)
            check_type(argname="argument local_dir", value=local_dir, expected_type=type_hints["local_dir"])
        options = AddDirectoryOptions(exclude=exclude, key_prefix=key_prefix)

        return typing.cast(None, jsii.invoke(self, "addDirectory", [local_dir, options]))

    @jsii.member(jsii_name="addFile")
    def add_file(
        self,
        local_file: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a file to the ConfigMap.

        :param local_file: The path to the local file.
        :param key: The ConfigMap key (default to the file name).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigMap.add_file)
            check_type(argname="argument local_file", value=local_file, expected_type=type_hints["local_file"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(None, jsii.invoke(self, "addFile", [local_file, key]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="binaryData")
    def binary_data(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The binary data associated with this config map.

        Returns a copy. To add data records, use ``addBinaryData()`` or ``addData()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "binaryData"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The data associated with this config map.

        Returns an copy. To add data records, use ``addData()`` or ``addBinaryData()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @builtins.property
    @jsii.member(jsii_name="immutable")
    def immutable(self) -> builtins.bool:
        '''Whether or not this config map is immutable.'''
        return typing.cast(builtins.bool, jsii.get(self, "immutable"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


class DaemonSet(Workload, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.DaemonSet"):
    '''A DaemonSet ensures that all (or some) Nodes run a copy of a Pod.

    As nodes are added to the cluster, Pods are added to them.
    As nodes are removed from the cluster, those Pods are garbage collected.
    Deleting a DaemonSet will clean up the Pods it created.

    Some typical uses of a DaemonSet are:

    - running a cluster storage daemon on every node
    - running a logs collection daemon on every node
    - running a node monitoring daemon on every node

    In a simple case, one DaemonSet, covering all nodes, would be used for each type of daemon.
    A more complex setup might use multiple DaemonSets for a single type of daemon,
    but with different flags and/or different memory and cpu requests for different hardware types.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        min_ready_seconds: typing.Optional[jsii.Number] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param min_ready_seconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Default: 0
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DaemonSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DaemonSetProps(
            min_ready_seconds=min_ready_seconds,
            pod_metadata=pod_metadata,
            select=select,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="minReadySeconds")
    def min_ready_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReadySeconds"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DaemonSetProps",
    jsii_struct_bases=[WorkloadProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "select": "select",
        "min_ready_seconds": "minReadySeconds",
    },
)
class DaemonSetProps(WorkloadProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        min_ready_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``DaemonSet``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param min_ready_seconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Default: 0
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(DaemonSetProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument pod_metadata", value=pod_metadata, expected_type=type_hints["pod_metadata"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
            check_type(argname="argument min_ready_seconds", value=min_ready_seconds, expected_type=type_hints["min_ready_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if select is not None:
            self._values["select"] = select
        if min_ready_seconds is not None:
            self._values["min_ready_seconds"] = min_ready_seconds

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata of this workload.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod label selector for this workload and add it to the pod metadata.

        This ensures this workload manages pods created by
        its pod template.

        :default: true
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_ready_seconds(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available.

        :default: 0
        '''
        result = self._values.get("min_ready_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DaemonSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Deployment(
    Workload,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.Deployment",
):
    '''A Deployment provides declarative updates for Pods and ReplicaSets.

    You describe a desired state in a Deployment, and the Deployment Controller changes the actual
    state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove
    existing Deployments and adopt all their resources with new Deployments.
    .. epigraph::

       Note: Do not manage ReplicaSets owned by a Deployment. Consider opening an issue in the main Kubernetes repository if your use case is not covered below.

    Use Case

    The following are typical use cases for Deployments:

    - Create a Deployment to rollout a ReplicaSet. The ReplicaSet creates Pods in the background.
      Check the status of the rollout to see if it succeeds or not.
    - Declare the new state of the Pods by updating the PodTemplateSpec of the Deployment.
      A new ReplicaSet is created and the Deployment manages moving the Pods from the old ReplicaSet to the new one at a controlled rate.
      Each new ReplicaSet updates the revision of the Deployment.
    - Rollback to an earlier Deployment revision if the current state of the Deployment is not stable.
      Each rollback updates the revision of the Deployment.
    - Scale up the Deployment to facilitate more load.
    - Pause the Deployment to apply multiple fixes to its PodTemplateSpec and then resume it to start a new rollout.
    - Use the status of the Deployment as an indicator that a rollout has stuck.
    - Clean up older ReplicaSets that you don't need anymore.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        min_ready: typing.Optional[cdk8s.Duration] = None,
        progress_deadline: typing.Optional[cdk8s.Duration] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[DeploymentStrategy] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param min_ready: Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Zero means the pod will be considered available as soon as it is ready. Default: Duration.seconds(0)
        :param progress_deadline: The maximum duration for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Default: Duration.seconds(600)
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Specifies the strategy used to replace old Pods by new ones. Default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Deployment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DeploymentProps(
            min_ready=min_ready,
            progress_deadline=progress_deadline,
            replicas=replicas,
            strategy=strategy,
            pod_metadata=pod_metadata,
            select=select,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="exposeViaIngress")
    def expose_via_ingress(
        self,
        path: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ServicePort, typing.Dict[str, typing.Any]]]] = None,
        service_type: typing.Optional[ServiceType] = None,
        ingress: typing.Optional[Ingress] = None,
        path_type: typing.Optional[HttpIngressPathType] = None,
    ) -> Ingress:
        '''Expose a deployment via an ingress.

        This will first expose the deployment with a service, and then expose the service via an ingress.

        :param path: The ingress path to register under.
        :param name: The name of the service to expose. If you'd like to expose the deployment multiple times, you must explicitly set a name starting from the second expose call. Default: - auto generated.
        :param ports: The ports that the service should bind to. Default: - extracted from the deployment.
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        :param path_type: The type of the path. Default: HttpIngressPathType.PREFIX
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Deployment.expose_via_ingress)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = ExposeDeploymentViaIngressOptions(
            name=name,
            ports=ports,
            service_type=service_type,
            ingress=ingress,
            path_type=path_type,
        )

        return typing.cast(Ingress, jsii.invoke(self, "exposeViaIngress", [path, options]))

    @jsii.member(jsii_name="exposeViaService")
    def expose_via_service(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Sequence[typing.Union[ServicePort, typing.Dict[str, typing.Any]]]] = None,
        service_type: typing.Optional[ServiceType] = None,
    ) -> Service:
        '''Expose a deployment via a service.

        This is equivalent to running ``kubectl expose deployment <deployment-name>``.

        :param name: The name of the service to expose. If you'd like to expose the deployment multiple times, you must explicitly set a name starting from the second expose call. Default: - auto generated.
        :param ports: The ports that the service should bind to. Default: - extracted from the deployment.
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        '''
        options = DeploymentExposeViaServiceOptions(
            name=name, ports=ports, service_type=service_type
        )

        return typing.cast(Service, jsii.invoke(self, "exposeViaService", [options]))

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="minReady")
    def min_ready(self) -> cdk8s.Duration:
        '''Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available.'''
        return typing.cast(cdk8s.Duration, jsii.get(self, "minReady"))

    @builtins.property
    @jsii.member(jsii_name="progressDeadline")
    def progress_deadline(self) -> cdk8s.Duration:
        '''The maximum duration for a deployment to make progress before it is considered to be failed.'''
        return typing.cast(cdk8s.Duration, jsii.get(self, "progressDeadline"))

    @builtins.property
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> jsii.Number:
        '''Number of desired pods.'''
        return typing.cast(jsii.Number, jsii.get(self, "replicas"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> DeploymentStrategy:
        return typing.cast(DeploymentStrategy, jsii.get(self, "strategy"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.DeploymentProps",
    jsii_struct_bases=[WorkloadProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "select": "select",
        "min_ready": "minReady",
        "progress_deadline": "progressDeadline",
        "replicas": "replicas",
        "strategy": "strategy",
    },
)
class DeploymentProps(WorkloadProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        min_ready: typing.Optional[cdk8s.Duration] = None,
        progress_deadline: typing.Optional[cdk8s.Duration] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[DeploymentStrategy] = None,
    ) -> None:
        '''Properties for ``Deployment``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param min_ready: Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Zero means the pod will be considered available as soon as it is ready. Default: Duration.seconds(0)
        :param progress_deadline: The maximum duration for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Default: Duration.seconds(600)
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Specifies the strategy used to replace old Pods by new ones. Default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(DeploymentProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument pod_metadata", value=pod_metadata, expected_type=type_hints["pod_metadata"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
            check_type(argname="argument min_ready", value=min_ready, expected_type=type_hints["min_ready"])
            check_type(argname="argument progress_deadline", value=progress_deadline, expected_type=type_hints["progress_deadline"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if select is not None:
            self._values["select"] = select
        if min_ready is not None:
            self._values["min_ready"] = min_ready
        if progress_deadline is not None:
            self._values["progress_deadline"] = progress_deadline
        if replicas is not None:
            self._values["replicas"] = replicas
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata of this workload.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod label selector for this workload and add it to the pod metadata.

        This ensures this workload manages pods created by
        its pod template.

        :default: true
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_ready(self) -> typing.Optional[cdk8s.Duration]:
        '''Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available.

        Zero means the pod will be considered available as soon as it is ready.

        :default: Duration.seconds(0)

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#min-ready-seconds
        '''
        result = self._values.get("min_ready")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def progress_deadline(self) -> typing.Optional[cdk8s.Duration]:
        '''The maximum duration for a deployment to make progress before it is considered to be failed.

        The deployment controller will continue
        to process failed deployments and a condition with a ProgressDeadlineExceeded
        reason will be surfaced in the deployment status.

        Note that progress will not be estimated during the time a deployment is paused.

        :default: Duration.seconds(600)

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#progress-deadline-seconds
        '''
        result = self._values.get("progress_deadline")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''Number of desired pods.

        :default: 1
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional[DeploymentStrategy]:
        '''Specifies the strategy used to replace old Pods by new ones.

        :default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[DeploymentStrategy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GCEPersistentDiskPersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.GCEPersistentDiskPersistentVolume",
):
    '''GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod.

    Provisioned by an admin.

    :see: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE.
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GCEPersistentDiskPersistentVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GCEPersistentDiskPersistentVolumeProps(
            pd_name=pd_name,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        '''PD resource in GCE of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> typing.Optional[jsii.Number]:
        '''Partition of this volume.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partition"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.GCEPersistentDiskPersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class GCEPersistentDiskPersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``GCEPersistentDiskPersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE.
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(GCEPersistentDiskPersistentVolumeProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "pd_name": pd_name,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE.

        Used to identify the disk in GCE.

        :see: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GCEPersistentDiskPersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Job(Workload, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-23.Job"):
    '''A Job creates one or more Pods and ensures that a specified number of them successfully terminate.

    As pods successfully complete,
    the Job tracks the successful completions. When a specified number of successful completions is reached, the task (ie, Job) is complete.
    Deleting a Job will clean up the Pods it created. A simple case is to create one Job object in order to reliably run one Pod to completion.
    The Job object will start a new Pod if the first Pod fails or is deleted (for example due to a node hardware failure or a node reboot).
    You can also use a Job to run multiple Pods in parallel.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        active_deadline: typing.Optional[cdk8s.Duration] = None,
        backoff_limit: typing.Optional[jsii.Number] = None,
        ttl_after_finished: typing.Optional[cdk8s.Duration] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param active_deadline: Specifies the duration the job may be active before the system tries to terminate it. Default: - If unset, then there is no deadline.
        :param backoff_limit: Specifies the number of retries before marking this job failed. Default: - If not set, system defaults to 6.
        :param ttl_after_finished: Limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the ``TTLAfterFinished`` feature. Default: - If this field is unset, the Job won't be automatically deleted.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Job.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = JobProps(
            active_deadline=active_deadline,
            backoff_limit=backoff_limit,
            ttl_after_finished=ttl_after_finished,
            pod_metadata=pod_metadata,
            select=select,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="activeDeadline")
    def active_deadline(self) -> typing.Optional[cdk8s.Duration]:
        '''Duration before job is terminated.

        If undefined, there is no deadline.
        '''
        return typing.cast(typing.Optional[cdk8s.Duration], jsii.get(self, "activeDeadline"))

    @builtins.property
    @jsii.member(jsii_name="backoffLimit")
    def backoff_limit(self) -> typing.Optional[jsii.Number]:
        '''Number of retries before marking failed.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backoffLimit"))

    @builtins.property
    @jsii.member(jsii_name="ttlAfterFinished")
    def ttl_after_finished(self) -> typing.Optional[cdk8s.Duration]:
        '''TTL before the job is deleted after it is finished.'''
        return typing.cast(typing.Optional[cdk8s.Duration], jsii.get(self, "ttlAfterFinished"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.JobProps",
    jsii_struct_bases=[WorkloadProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "select": "select",
        "active_deadline": "activeDeadline",
        "backoff_limit": "backoffLimit",
        "ttl_after_finished": "ttlAfterFinished",
    },
)
class JobProps(WorkloadProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        active_deadline: typing.Optional[cdk8s.Duration] = None,
        backoff_limit: typing.Optional[jsii.Number] = None,
        ttl_after_finished: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Properties for ``Job``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param active_deadline: Specifies the duration the job may be active before the system tries to terminate it. Default: - If unset, then there is no deadline.
        :param backoff_limit: Specifies the number of retries before marking this job failed. Default: - If not set, system defaults to 6.
        :param ttl_after_finished: Limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the ``TTLAfterFinished`` feature. Default: - If this field is unset, the Job won't be automatically deleted.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(JobProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument pod_metadata", value=pod_metadata, expected_type=type_hints["pod_metadata"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
            check_type(argname="argument active_deadline", value=active_deadline, expected_type=type_hints["active_deadline"])
            check_type(argname="argument backoff_limit", value=backoff_limit, expected_type=type_hints["backoff_limit"])
            check_type(argname="argument ttl_after_finished", value=ttl_after_finished, expected_type=type_hints["ttl_after_finished"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if select is not None:
            self._values["select"] = select
        if active_deadline is not None:
            self._values["active_deadline"] = active_deadline
        if backoff_limit is not None:
            self._values["backoff_limit"] = backoff_limit
        if ttl_after_finished is not None:
            self._values["ttl_after_finished"] = ttl_after_finished

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata of this workload.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod label selector for this workload and add it to the pod metadata.

        This ensures this workload manages pods created by
        its pod template.

        :default: true
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def active_deadline(self) -> typing.Optional[cdk8s.Duration]:
        '''Specifies the duration the job may be active before the system tries to terminate it.

        :default: - If unset, then there is no deadline.
        '''
        result = self._values.get("active_deadline")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def backoff_limit(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of retries before marking this job failed.

        :default: - If not set, system defaults to 6.
        '''
        result = self._values.get("backoff_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ttl_after_finished(self) -> typing.Optional[cdk8s.Duration]:
        '''Limits the lifetime of a Job that has finished execution (either Complete or Failed).

        If this field is set, after the Job finishes, it is eligible to
        be automatically deleted. When the Job is being deleted, its lifecycle
        guarantees (e.g. finalizers) will be honored. If this field is set to zero,
        the Job becomes eligible to be deleted immediately after it finishes. This
        field is alpha-level and is only honored by servers that enable the
        ``TTLAfterFinished`` feature.

        :default: - If this field is unset, the Job won't be automatically deleted.
        '''
        result = self._values.get("ttl_after_finished")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StatefulSet(
    Workload,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-23.StatefulSet",
):
    '''StatefulSet is the workload API object used to manage stateful applications.

    Manages the deployment and scaling of a set of Pods, and provides guarantees
    about the ordering and uniqueness of these Pods.

    Like a Deployment, a StatefulSet manages Pods that are based on an identical
    container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity
    for each of their Pods. These pods are created from the same spec, but are not
    interchangeable: each has a persistent identifier that it maintains across any
    rescheduling.

    If you want to use storage volumes to provide persistence for your workload, you
    can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet
    are susceptible to failure, the persistent Pod identifiers make it easier to match existing
    volumes to the new Pods that replace any that have failed.


    Using StatefulSets

    StatefulSets are valuable for applications that require one or more of the following.

    - Stable, unique network identifiers.
    - Stable, persistent storage.
    - Ordered, graceful deployment and scaling.
    - Ordered, automated rolling updates.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service: Service,
        min_ready: typing.Optional[cdk8s.Duration] = None,
        pod_management_policy: typing.Optional[PodManagementPolicy] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[StatefulSetUpdateStrategy] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service: Service to associate with the statefulset.
        :param min_ready: Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Zero means the pod will be considered available as soon as it is ready. This is an alpha field and requires enabling StatefulSetMinReadySeconds feature gate. Default: Duration.seconds(0)
        :param pod_management_policy: Pod management policy to use for this statefulset. Default: PodManagementPolicy.ORDERED_READY
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. Default: - RollingUpdate with partition set to 0
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StatefulSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StatefulSetProps(
            service=service,
            min_ready=min_ready,
            pod_management_policy=pod_management_policy,
            replicas=replicas,
            strategy=strategy,
            pod_metadata=pod_metadata,
            select=select,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns=dns,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property
    @jsii.member(jsii_name="minReady")
    def min_ready(self) -> cdk8s.Duration:
        '''Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available.'''
        return typing.cast(cdk8s.Duration, jsii.get(self, "minReady"))

    @builtins.property
    @jsii.member(jsii_name="podManagementPolicy")
    def pod_management_policy(self) -> PodManagementPolicy:
        '''Management policy to use for the set.'''
        return typing.cast(PodManagementPolicy, jsii.get(self, "podManagementPolicy"))

    @builtins.property
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> jsii.Number:
        '''Number of desired pods.'''
        return typing.cast(jsii.Number, jsii.get(self, "replicas"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The name of a resource type as it appears in the relevant API endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> StatefulSetUpdateStrategy:
        '''The update startegy of this stateful set.'''
        return typing.cast(StatefulSetUpdateStrategy, jsii.get(self, "strategy"))


@jsii.data_type(
    jsii_type="cdk8s-plus-23.StatefulSetProps",
    jsii_struct_bases=[WorkloadProps],
    name_mapping={
        "metadata": "metadata",
        "automount_service_account_token": "automountServiceAccountToken",
        "containers": "containers",
        "dns": "dns",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "select": "select",
        "service": "service",
        "min_ready": "minReady",
        "pod_management_policy": "podManagementPolicy",
        "replicas": "replicas",
        "strategy": "strategy",
    },
)
class StatefulSetProps(WorkloadProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        automount_service_account_token: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        dns: typing.Optional[typing.Union[PodDnsProps, typing.Dict[str, typing.Any]]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Union[HostAlias, typing.Dict[str, typing.Any]]]] = None,
        init_containers: typing.Optional[typing.Sequence[typing.Union[ContainerProps, typing.Dict[str, typing.Any]]]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[typing.Union[PodSecurityContextProps, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[typing.Union[cdk8s.ApiObjectMetadata, typing.Dict[str, typing.Any]]] = None,
        select: typing.Optional[builtins.bool] = None,
        service: Service,
        min_ready: typing.Optional[cdk8s.Duration] = None,
        pod_management_policy: typing.Optional[PodManagementPolicy] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[StatefulSetUpdateStrategy] = None,
    ) -> None:
        '''Properties for initialization of ``StatefulSet``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param automount_service_account_token: Indicates whether a service account token should be automatically mounted. Default: true
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param dns: DNS settings for the pod. Default: policy: DnsPolicy.CLUSTER_FIRST hostnameAsFQDN: false
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata of this workload.
        :param select: Automatically allocates a pod label selector for this workload and add it to the pod metadata. This ensures this workload manages pods created by its pod template. Default: true
        :param service: Service to associate with the statefulset.
        :param min_ready: Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Zero means the pod will be considered available as soon as it is ready. This is an alpha field and requires enabling StatefulSetMinReadySeconds feature gate. Default: Duration.seconds(0)
        :param pod_management_policy: Pod management policy to use for this statefulset. Default: PodManagementPolicy.ORDERED_READY
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. Default: - RollingUpdate with partition set to 0
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(dns, dict):
            dns = PodDnsProps(**dns)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(StatefulSetProps.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument automount_service_account_token", value=automount_service_account_token, expected_type=type_hints["automount_service_account_token"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument docker_registry_auth", value=docker_registry_auth, expected_type=type_hints["docker_registry_auth"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument init_containers", value=init_containers, expected_type=type_hints["init_containers"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument pod_metadata", value=pod_metadata, expected_type=type_hints["pod_metadata"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument min_ready", value=min_ready, expected_type=type_hints["min_ready"])
            check_type(argname="argument pod_management_policy", value=pod_management_policy, expected_type=type_hints["pod_management_policy"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if automount_service_account_token is not None:
            self._values["automount_service_account_token"] = automount_service_account_token
        if containers is not None:
            self._values["containers"] = containers
        if dns is not None:
            self._values["dns"] = dns
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if select is not None:
            self._values["select"] = select
        if min_ready is not None:
            self._values["min_ready"] = min_ready
        if pod_management_policy is not None:
            self._values["pod_management_policy"] = pod_management_policy
        if replicas is not None:
            self._values["replicas"] = replicas
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def automount_service_account_token(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a service account token should be automatically mounted.

        :default: true

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server
        '''
        result = self._values.get("automount_service_account_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def dns(self) -> typing.Optional[PodDnsProps]:
        '''DNS settings for the pod.

        :default:

        policy: DnsPolicy.CLUSTER_FIRST
        hostnameAsFQDN: false

        :see: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[PodDnsProps], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata of this workload.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod label selector for this workload and add it to the pod metadata.

        This ensures this workload manages pods created by
        its pod template.

        :default: true
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service(self) -> Service:
        '''Service to associate with the statefulset.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(Service, result)

    @builtins.property
    def min_ready(self) -> typing.Optional[cdk8s.Duration]:
        '''Minimum duration for which a newly created pod should be ready without any of its container crashing, for it to be considered available.

        Zero means the pod will be considered available as soon as it is ready.

        This is an alpha field and requires enabling StatefulSetMinReadySeconds feature gate.

        :default: Duration.seconds(0)

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#min-ready-seconds
        '''
        result = self._values.get("min_ready")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def pod_management_policy(self) -> typing.Optional[PodManagementPolicy]:
        '''Pod management policy to use for this statefulset.

        :default: PodManagementPolicy.ORDERED_READY
        '''
        result = self._values.get("pod_management_policy")
        return typing.cast(typing.Optional[PodManagementPolicy], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''Number of desired pods.

        :default: 1
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional[StatefulSetUpdateStrategy]:
        '''Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.

        :default: - RollingUpdate with partition set to 0
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[StatefulSetUpdateStrategy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StatefulSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AbstractPod",
    "AbstractPodProps",
    "AddDeploymentOptions",
    "AddDirectoryOptions",
    "ApiResource",
    "ApiResourceOptions",
    "AwsElasticBlockStorePersistentVolume",
    "AwsElasticBlockStorePersistentVolumeProps",
    "AwsElasticBlockStoreVolumeOptions",
    "AzureDiskPersistentVolume",
    "AzureDiskPersistentVolumeCachingMode",
    "AzureDiskPersistentVolumeKind",
    "AzureDiskPersistentVolumeProps",
    "AzureDiskVolumeOptions",
    "BasicAuthSecret",
    "BasicAuthSecretProps",
    "ClusterRole",
    "ClusterRoleBinding",
    "ClusterRoleBindingProps",
    "ClusterRolePolicyRule",
    "ClusterRoleProps",
    "CommandProbeOptions",
    "CommonSecretProps",
    "ConfigMap",
    "ConfigMapProps",
    "ConfigMapVolumeOptions",
    "ConnectionScheme",
    "Container",
    "ContainerLifecycle",
    "ContainerPort",
    "ContainerProps",
    "ContainerResources",
    "ContainerSecurityContext",
    "ContainerSecurityContextProps",
    "Cpu",
    "CpuResources",
    "DaemonSet",
    "DaemonSetProps",
    "Deployment",
    "DeploymentExposeViaServiceOptions",
    "DeploymentProps",
    "DeploymentStrategy",
    "DeploymentStrategyRollingUpdateOptions",
    "DnsOption",
    "DnsPolicy",
    "DockerConfigSecret",
    "DockerConfigSecretProps",
    "EmptyDirMedium",
    "EmptyDirVolumeOptions",
    "Env",
    "EnvFieldPaths",
    "EnvFrom",
    "EnvValue",
    "EnvValueFromConfigMapOptions",
    "EnvValueFromFieldRefOptions",
    "EnvValueFromProcessOptions",
    "EnvValueFromResourceOptions",
    "EnvValueFromSecretOptions",
    "EphemeralStorageResources",
    "ExposeDeploymentViaIngressOptions",
    "ExposeServiceViaIngressOptions",
    "FsGroupChangePolicy",
    "GCEPersistentDiskPersistentVolume",
    "GCEPersistentDiskPersistentVolumeProps",
    "GCEPersistentDiskVolumeOptions",
    "Group",
    "Handler",
    "HandlerFromHttpGetOptions",
    "HandlerFromTcpSocketOptions",
    "HostAlias",
    "HostPathVolumeOptions",
    "HostPathVolumeType",
    "HttpGetProbeOptions",
    "HttpIngressPathType",
    "IApiEndpoint",
    "IApiResource",
    "IClusterRole",
    "IConfigMap",
    "INamespaceSelector",
    "INetworkPolicyPeer",
    "IPersistentVolume",
    "IPersistentVolumeClaim",
    "IPodSelector",
    "IResource",
    "IRole",
    "ISecret",
    "IServiceAccount",
    "IStorage",
    "ISubject",
    "ImagePullPolicy",
    "Ingress",
    "IngressBackend",
    "IngressProps",
    "IngressRule",
    "IngressTls",
    "Job",
    "JobProps",
    "LabelExpression",
    "LabelSelector",
    "LabelSelectorOptions",
    "LabelSelectorRequirement",
    "LabeledNode",
    "MemoryResources",
    "MountOptions",
    "MountPropagation",
    "NamedNode",
    "Namespace",
    "NamespaceProps",
    "NamespaceSelectorConfig",
    "Namespaces",
    "NamespacesSelectOptions",
    "NetworkPolicy",
    "NetworkPolicyAddEgressRuleOptions",
    "NetworkPolicyIpBlock",
    "NetworkPolicyPeerConfig",
    "NetworkPolicyPort",
    "NetworkPolicyPortProps",
    "NetworkPolicyProps",
    "NetworkPolicyRule",
    "NetworkPolicyTraffic",
    "NetworkPolicyTrafficDefault",
    "NetworkProtocol",
    "Node",
    "NodeLabelQuery",
    "NodeTaintQuery",
    "NodeTaintQueryOptions",
    "NonApiResource",
    "PathMapping",
    "PercentOrAbsolute",
    "PersistentVolume",
    "PersistentVolumeAccessMode",
    "PersistentVolumeClaim",
    "PersistentVolumeClaimProps",
    "PersistentVolumeClaimVolumeOptions",
    "PersistentVolumeMode",
    "PersistentVolumeProps",
    "PersistentVolumeReclaimPolicy",
    "Pod",
    "PodConnections",
    "PodConnectionsAllowFromOptions",
    "PodConnectionsAllowToOptions",
    "PodConnectionsIsolation",
    "PodDns",
    "PodDnsProps",
    "PodManagementPolicy",
    "PodProps",
    "PodScheduling",
    "PodSchedulingAttractOptions",
    "PodSchedulingColocateOptions",
    "PodSchedulingSeparateOptions",
    "PodSecurityContext",
    "PodSecurityContextProps",
    "PodSelectorConfig",
    "Pods",
    "PodsAllOptions",
    "PodsSelectOptions",
    "Probe",
    "ProbeOptions",
    "Protocol",
    "Resource",
    "ResourceFieldPaths",
    "ResourcePermissions",
    "ResourceProps",
    "RestartPolicy",
    "Role",
    "RoleBinding",
    "RoleBindingProps",
    "RolePolicyRule",
    "RoleProps",
    "Secret",
    "SecretProps",
    "SecretValue",
    "SecretVolumeOptions",
    "Service",
    "ServiceAccount",
    "ServiceAccountProps",
    "ServiceAccountTokenSecret",
    "ServiceAccountTokenSecretProps",
    "ServiceBindOptions",
    "ServiceIngressBackendOptions",
    "ServicePort",
    "ServiceProps",
    "ServiceType",
    "SshAuthSecret",
    "SshAuthSecretProps",
    "StatefulSet",
    "StatefulSetProps",
    "StatefulSetUpdateStrategy",
    "StatefulSetUpdateStrategyRollingUpdateOptions",
    "SubjectConfiguration",
    "Sysctl",
    "TaintEffect",
    "TaintedNode",
    "TcpSocketProbeOptions",
    "TlsSecret",
    "TlsSecretProps",
    "Topology",
    "User",
    "Volume",
    "VolumeMount",
    "Workload",
    "WorkloadProps",
    "WorkloadScheduling",
    "WorkloadSchedulingSpreadOptions",
]

publication.publish()
