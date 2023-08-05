# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InfraEnvCreateParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'proxy': 'Proxy',
        'additional_ntp_sources': 'str',
        'ssh_authorized_key': 'str',
        'pull_secret': 'str',
        'static_network_config': 'list[HostStaticNetworkConfig]',
        'image_type': 'ImageType',
        'ignition_config_override': 'str',
        'cluster_id': 'str',
        'openshift_version': 'str',
        'cpu_architecture': 'str'
    }

    attribute_map = {
        'name': 'name',
        'proxy': 'proxy',
        'additional_ntp_sources': 'additional_ntp_sources',
        'ssh_authorized_key': 'ssh_authorized_key',
        'pull_secret': 'pull_secret',
        'static_network_config': 'static_network_config',
        'image_type': 'image_type',
        'ignition_config_override': 'ignition_config_override',
        'cluster_id': 'cluster_id',
        'openshift_version': 'openshift_version',
        'cpu_architecture': 'cpu_architecture'
    }

    def __init__(self, name=None, proxy=None, additional_ntp_sources=None, ssh_authorized_key=None, pull_secret=None, static_network_config=None, image_type=None, ignition_config_override=None, cluster_id=None, openshift_version=None, cpu_architecture='x86_64'):  # noqa: E501
        """InfraEnvCreateParams - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._proxy = None
        self._additional_ntp_sources = None
        self._ssh_authorized_key = None
        self._pull_secret = None
        self._static_network_config = None
        self._image_type = None
        self._ignition_config_override = None
        self._cluster_id = None
        self._openshift_version = None
        self._cpu_architecture = None
        self.discriminator = None

        self.name = name
        if proxy is not None:
            self.proxy = proxy
        if additional_ntp_sources is not None:
            self.additional_ntp_sources = additional_ntp_sources
        if ssh_authorized_key is not None:
            self.ssh_authorized_key = ssh_authorized_key
        self.pull_secret = pull_secret
        if static_network_config is not None:
            self.static_network_config = static_network_config
        if image_type is not None:
            self.image_type = image_type
        if ignition_config_override is not None:
            self.ignition_config_override = ignition_config_override
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if openshift_version is not None:
            self.openshift_version = openshift_version
        if cpu_architecture is not None:
            self.cpu_architecture = cpu_architecture

    @property
    def name(self):
        """Gets the name of this InfraEnvCreateParams.  # noqa: E501

        Name of the infra-env.  # noqa: E501

        :return: The name of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfraEnvCreateParams.

        Name of the infra-env.  # noqa: E501

        :param name: The name of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def proxy(self):
        """Gets the proxy of this InfraEnvCreateParams.  # noqa: E501


        :return: The proxy of this InfraEnvCreateParams.  # noqa: E501
        :rtype: Proxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this InfraEnvCreateParams.


        :param proxy: The proxy of this InfraEnvCreateParams.  # noqa: E501
        :type: Proxy
        """

        self._proxy = proxy

    @property
    def additional_ntp_sources(self):
        """Gets the additional_ntp_sources of this InfraEnvCreateParams.  # noqa: E501

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :return: The additional_ntp_sources of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._additional_ntp_sources

    @additional_ntp_sources.setter
    def additional_ntp_sources(self, additional_ntp_sources):
        """Sets the additional_ntp_sources of this InfraEnvCreateParams.

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :param additional_ntp_sources: The additional_ntp_sources of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._additional_ntp_sources = additional_ntp_sources

    @property
    def ssh_authorized_key(self):
        """Gets the ssh_authorized_key of this InfraEnvCreateParams.  # noqa: E501

        SSH public key for debugging the installation.  # noqa: E501

        :return: The ssh_authorized_key of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ssh_authorized_key

    @ssh_authorized_key.setter
    def ssh_authorized_key(self, ssh_authorized_key):
        """Sets the ssh_authorized_key of this InfraEnvCreateParams.

        SSH public key for debugging the installation.  # noqa: E501

        :param ssh_authorized_key: The ssh_authorized_key of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._ssh_authorized_key = ssh_authorized_key

    @property
    def pull_secret(self):
        """Gets the pull_secret of this InfraEnvCreateParams.  # noqa: E501

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :return: The pull_secret of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """Sets the pull_secret of this InfraEnvCreateParams.

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :param pull_secret: The pull_secret of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """
        if pull_secret is None:
            raise ValueError("Invalid value for `pull_secret`, must not be `None`")  # noqa: E501

        self._pull_secret = pull_secret

    @property
    def static_network_config(self):
        """Gets the static_network_config of this InfraEnvCreateParams.  # noqa: E501


        :return: The static_network_config of this InfraEnvCreateParams.  # noqa: E501
        :rtype: list[HostStaticNetworkConfig]
        """
        return self._static_network_config

    @static_network_config.setter
    def static_network_config(self, static_network_config):
        """Sets the static_network_config of this InfraEnvCreateParams.


        :param static_network_config: The static_network_config of this InfraEnvCreateParams.  # noqa: E501
        :type: list[HostStaticNetworkConfig]
        """

        self._static_network_config = static_network_config

    @property
    def image_type(self):
        """Gets the image_type of this InfraEnvCreateParams.  # noqa: E501


        :return: The image_type of this InfraEnvCreateParams.  # noqa: E501
        :rtype: ImageType
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this InfraEnvCreateParams.


        :param image_type: The image_type of this InfraEnvCreateParams.  # noqa: E501
        :type: ImageType
        """

        self._image_type = image_type

    @property
    def ignition_config_override(self):
        """Gets the ignition_config_override of this InfraEnvCreateParams.  # noqa: E501

        JSON formatted string containing the user overrides for the initial ignition config.  # noqa: E501

        :return: The ignition_config_override of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ignition_config_override

    @ignition_config_override.setter
    def ignition_config_override(self, ignition_config_override):
        """Sets the ignition_config_override of this InfraEnvCreateParams.

        JSON formatted string containing the user overrides for the initial ignition config.  # noqa: E501

        :param ignition_config_override: The ignition_config_override of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._ignition_config_override = ignition_config_override

    @property
    def cluster_id(self):
        """Gets the cluster_id of this InfraEnvCreateParams.  # noqa: E501

        If set, all hosts that register will be associated with the specified cluster.  # noqa: E501

        :return: The cluster_id of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this InfraEnvCreateParams.

        If set, all hosts that register will be associated with the specified cluster.  # noqa: E501

        :param cluster_id: The cluster_id of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def openshift_version(self):
        """Gets the openshift_version of this InfraEnvCreateParams.  # noqa: E501

        Version of the OpenShift cluster (used to infer the RHCOS version - temporary until generic logic implemented).  # noqa: E501

        :return: The openshift_version of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._openshift_version

    @openshift_version.setter
    def openshift_version(self, openshift_version):
        """Sets the openshift_version of this InfraEnvCreateParams.

        Version of the OpenShift cluster (used to infer the RHCOS version - temporary until generic logic implemented).  # noqa: E501

        :param openshift_version: The openshift_version of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._openshift_version = openshift_version

    @property
    def cpu_architecture(self):
        """Gets the cpu_architecture of this InfraEnvCreateParams.  # noqa: E501

        The CPU architecture of the image (x86_64/arm64/etc).  # noqa: E501

        :return: The cpu_architecture of this InfraEnvCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """Sets the cpu_architecture of this InfraEnvCreateParams.

        The CPU architecture of the image (x86_64/arm64/etc).  # noqa: E501

        :param cpu_architecture: The cpu_architecture of this InfraEnvCreateParams.  # noqa: E501
        :type: str
        """

        self._cpu_architecture = cpu_architecture

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InfraEnvCreateParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InfraEnvCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
