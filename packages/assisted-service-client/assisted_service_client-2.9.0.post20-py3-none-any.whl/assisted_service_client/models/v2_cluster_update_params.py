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


class V2ClusterUpdateParams(object):
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
        'base_dns_domain': 'str',
        'cluster_network_cidr': 'str',
        'platform': 'Platform',
        'cluster_network_host_prefix': 'int',
        'service_network_cidr': 'str',
        'api_vip': 'str',
        'ingress_vip': 'str',
        'api_vip_dns_name': 'str',
        'machine_network_cidr': 'str',
        'pull_secret': 'str',
        'ssh_public_key': 'str',
        'vip_dhcp_allocation': 'bool',
        'http_proxy': 'str',
        'https_proxy': 'str',
        'no_proxy': 'str',
        'user_managed_networking': 'bool',
        'additional_ntp_source': 'str',
        'olm_operators': 'list[OperatorCreateParams]',
        'hyperthreading': 'str',
        'network_type': 'str',
        'schedulable_masters': 'bool',
        'cluster_networks': 'list[ClusterNetwork]',
        'service_networks': 'list[ServiceNetwork]',
        'machine_networks': 'list[MachineNetwork]',
        'disk_encryption': 'DiskEncryption',
        'ignition_endpoint': 'IgnitionEndpoint',
        'tags': 'str'
    }

    attribute_map = {
        'name': 'name',
        'base_dns_domain': 'base_dns_domain',
        'cluster_network_cidr': 'cluster_network_cidr',
        'platform': 'platform',
        'cluster_network_host_prefix': 'cluster_network_host_prefix',
        'service_network_cidr': 'service_network_cidr',
        'api_vip': 'api_vip',
        'ingress_vip': 'ingress_vip',
        'api_vip_dns_name': 'api_vip_dns_name',
        'machine_network_cidr': 'machine_network_cidr',
        'pull_secret': 'pull_secret',
        'ssh_public_key': 'ssh_public_key',
        'vip_dhcp_allocation': 'vip_dhcp_allocation',
        'http_proxy': 'http_proxy',
        'https_proxy': 'https_proxy',
        'no_proxy': 'no_proxy',
        'user_managed_networking': 'user_managed_networking',
        'additional_ntp_source': 'additional_ntp_source',
        'olm_operators': 'olm_operators',
        'hyperthreading': 'hyperthreading',
        'network_type': 'network_type',
        'schedulable_masters': 'schedulable_masters',
        'cluster_networks': 'cluster_networks',
        'service_networks': 'service_networks',
        'machine_networks': 'machine_networks',
        'disk_encryption': 'disk_encryption',
        'ignition_endpoint': 'ignition_endpoint',
        'tags': 'tags'
    }

    def __init__(self, name=None, base_dns_domain=None, cluster_network_cidr=None, platform=None, cluster_network_host_prefix=None, service_network_cidr=None, api_vip=None, ingress_vip=None, api_vip_dns_name=None, machine_network_cidr=None, pull_secret=None, ssh_public_key=None, vip_dhcp_allocation=None, http_proxy=None, https_proxy=None, no_proxy=None, user_managed_networking=None, additional_ntp_source=None, olm_operators=None, hyperthreading=None, network_type=None, schedulable_masters=False, cluster_networks=None, service_networks=None, machine_networks=None, disk_encryption=None, ignition_endpoint=None, tags=None):  # noqa: E501
        """V2ClusterUpdateParams - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._base_dns_domain = None
        self._cluster_network_cidr = None
        self._platform = None
        self._cluster_network_host_prefix = None
        self._service_network_cidr = None
        self._api_vip = None
        self._ingress_vip = None
        self._api_vip_dns_name = None
        self._machine_network_cidr = None
        self._pull_secret = None
        self._ssh_public_key = None
        self._vip_dhcp_allocation = None
        self._http_proxy = None
        self._https_proxy = None
        self._no_proxy = None
        self._user_managed_networking = None
        self._additional_ntp_source = None
        self._olm_operators = None
        self._hyperthreading = None
        self._network_type = None
        self._schedulable_masters = None
        self._cluster_networks = None
        self._service_networks = None
        self._machine_networks = None
        self._disk_encryption = None
        self._ignition_endpoint = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if base_dns_domain is not None:
            self.base_dns_domain = base_dns_domain
        if cluster_network_cidr is not None:
            self.cluster_network_cidr = cluster_network_cidr
        if platform is not None:
            self.platform = platform
        if cluster_network_host_prefix is not None:
            self.cluster_network_host_prefix = cluster_network_host_prefix
        if service_network_cidr is not None:
            self.service_network_cidr = service_network_cidr
        if api_vip is not None:
            self.api_vip = api_vip
        if ingress_vip is not None:
            self.ingress_vip = ingress_vip
        if api_vip_dns_name is not None:
            self.api_vip_dns_name = api_vip_dns_name
        if machine_network_cidr is not None:
            self.machine_network_cidr = machine_network_cidr
        if pull_secret is not None:
            self.pull_secret = pull_secret
        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if vip_dhcp_allocation is not None:
            self.vip_dhcp_allocation = vip_dhcp_allocation
        if http_proxy is not None:
            self.http_proxy = http_proxy
        if https_proxy is not None:
            self.https_proxy = https_proxy
        if no_proxy is not None:
            self.no_proxy = no_proxy
        if user_managed_networking is not None:
            self.user_managed_networking = user_managed_networking
        if additional_ntp_source is not None:
            self.additional_ntp_source = additional_ntp_source
        if olm_operators is not None:
            self.olm_operators = olm_operators
        if hyperthreading is not None:
            self.hyperthreading = hyperthreading
        if network_type is not None:
            self.network_type = network_type
        if schedulable_masters is not None:
            self.schedulable_masters = schedulable_masters
        if cluster_networks is not None:
            self.cluster_networks = cluster_networks
        if service_networks is not None:
            self.service_networks = service_networks
        if machine_networks is not None:
            self.machine_networks = machine_networks
        if disk_encryption is not None:
            self.disk_encryption = disk_encryption
        if ignition_endpoint is not None:
            self.ignition_endpoint = ignition_endpoint
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this V2ClusterUpdateParams.  # noqa: E501

        OpenShift cluster name.  # noqa: E501

        :return: The name of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2ClusterUpdateParams.

        OpenShift cluster name.  # noqa: E501

        :param name: The name of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 54:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `54`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def base_dns_domain(self):
        """Gets the base_dns_domain of this V2ClusterUpdateParams.  # noqa: E501

        Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.  # noqa: E501

        :return: The base_dns_domain of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._base_dns_domain

    @base_dns_domain.setter
    def base_dns_domain(self, base_dns_domain):
        """Sets the base_dns_domain of this V2ClusterUpdateParams.

        Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.  # noqa: E501

        :param base_dns_domain: The base_dns_domain of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._base_dns_domain = base_dns_domain

    @property
    def cluster_network_cidr(self):
        """Gets the cluster_network_cidr of this V2ClusterUpdateParams.  # noqa: E501

        IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The cluster_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_network_cidr

    @cluster_network_cidr.setter
    def cluster_network_cidr(self, cluster_network_cidr):
        """Sets the cluster_network_cidr of this V2ClusterUpdateParams.

        IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param cluster_network_cidr: The cluster_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._cluster_network_cidr = cluster_network_cidr

    @property
    def platform(self):
        """Gets the platform of this V2ClusterUpdateParams.  # noqa: E501


        :return: The platform of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: Platform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this V2ClusterUpdateParams.


        :param platform: The platform of this V2ClusterUpdateParams.  # noqa: E501
        :type: Platform
        """

        self._platform = platform

    @property
    def cluster_network_host_prefix(self):
        """Gets the cluster_network_host_prefix of this V2ClusterUpdateParams.  # noqa: E501

        The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The cluster_network_host_prefix of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: int
        """
        return self._cluster_network_host_prefix

    @cluster_network_host_prefix.setter
    def cluster_network_host_prefix(self, cluster_network_host_prefix):
        """Sets the cluster_network_host_prefix of this V2ClusterUpdateParams.

        The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param cluster_network_host_prefix: The cluster_network_host_prefix of this V2ClusterUpdateParams.  # noqa: E501
        :type: int
        """
        if cluster_network_host_prefix is not None and cluster_network_host_prefix > 128:  # noqa: E501
            raise ValueError("Invalid value for `cluster_network_host_prefix`, must be a value less than or equal to `128`")  # noqa: E501
        if cluster_network_host_prefix is not None and cluster_network_host_prefix < 1:  # noqa: E501
            raise ValueError("Invalid value for `cluster_network_host_prefix`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cluster_network_host_prefix = cluster_network_host_prefix

    @property
    def service_network_cidr(self):
        """Gets the service_network_cidr of this V2ClusterUpdateParams.  # noqa: E501

        The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The service_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._service_network_cidr

    @service_network_cidr.setter
    def service_network_cidr(self, service_network_cidr):
        """Sets the service_network_cidr of this V2ClusterUpdateParams.

        The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param service_network_cidr: The service_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._service_network_cidr = service_network_cidr

    @property
    def api_vip(self):
        """Gets the api_vip of this V2ClusterUpdateParams.  # noqa: E501

        The virtual IP used to reach the OpenShift cluster's API.  # noqa: E501

        :return: The api_vip of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._api_vip

    @api_vip.setter
    def api_vip(self, api_vip):
        """Sets the api_vip of this V2ClusterUpdateParams.

        The virtual IP used to reach the OpenShift cluster's API.  # noqa: E501

        :param api_vip: The api_vip of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._api_vip = api_vip

    @property
    def ingress_vip(self):
        """Gets the ingress_vip of this V2ClusterUpdateParams.  # noqa: E501

        The virtual IP used for cluster ingress traffic.  # noqa: E501

        :return: The ingress_vip of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._ingress_vip

    @ingress_vip.setter
    def ingress_vip(self, ingress_vip):
        """Sets the ingress_vip of this V2ClusterUpdateParams.

        The virtual IP used for cluster ingress traffic.  # noqa: E501

        :param ingress_vip: The ingress_vip of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._ingress_vip = ingress_vip

    @property
    def api_vip_dns_name(self):
        """Gets the api_vip_dns_name of this V2ClusterUpdateParams.  # noqa: E501

        The domain name used to reach the OpenShift cluster API.  # noqa: E501

        :return: The api_vip_dns_name of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._api_vip_dns_name

    @api_vip_dns_name.setter
    def api_vip_dns_name(self, api_vip_dns_name):
        """Sets the api_vip_dns_name of this V2ClusterUpdateParams.

        The domain name used to reach the OpenShift cluster API.  # noqa: E501

        :param api_vip_dns_name: The api_vip_dns_name of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._api_vip_dns_name = api_vip_dns_name

    @property
    def machine_network_cidr(self):
        """Gets the machine_network_cidr of this V2ClusterUpdateParams.  # noqa: E501

        A CIDR that all hosts belonging to the cluster should have an interfaces with IP address that belongs to this CIDR. The api_vip belongs to this CIDR.  # noqa: E501

        :return: The machine_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._machine_network_cidr

    @machine_network_cidr.setter
    def machine_network_cidr(self, machine_network_cidr):
        """Sets the machine_network_cidr of this V2ClusterUpdateParams.

        A CIDR that all hosts belonging to the cluster should have an interfaces with IP address that belongs to this CIDR. The api_vip belongs to this CIDR.  # noqa: E501

        :param machine_network_cidr: The machine_network_cidr of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._machine_network_cidr = machine_network_cidr

    @property
    def pull_secret(self):
        """Gets the pull_secret of this V2ClusterUpdateParams.  # noqa: E501

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :return: The pull_secret of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """Sets the pull_secret of this V2ClusterUpdateParams.

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :param pull_secret: The pull_secret of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._pull_secret = pull_secret

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this V2ClusterUpdateParams.  # noqa: E501

        SSH public key for debugging OpenShift nodes.  # noqa: E501

        :return: The ssh_public_key of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this V2ClusterUpdateParams.

        SSH public key for debugging OpenShift nodes.  # noqa: E501

        :param ssh_public_key: The ssh_public_key of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def vip_dhcp_allocation(self):
        """Gets the vip_dhcp_allocation of this V2ClusterUpdateParams.  # noqa: E501

        Indicate if virtual IP DHCP allocation mode is enabled.  # noqa: E501

        :return: The vip_dhcp_allocation of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._vip_dhcp_allocation

    @vip_dhcp_allocation.setter
    def vip_dhcp_allocation(self, vip_dhcp_allocation):
        """Sets the vip_dhcp_allocation of this V2ClusterUpdateParams.

        Indicate if virtual IP DHCP allocation mode is enabled.  # noqa: E501

        :param vip_dhcp_allocation: The vip_dhcp_allocation of this V2ClusterUpdateParams.  # noqa: E501
        :type: bool
        """

        self._vip_dhcp_allocation = vip_dhcp_allocation

    @property
    def http_proxy(self):
        """Gets the http_proxy of this V2ClusterUpdateParams.  # noqa: E501

        A proxy URL to use for creating HTTP connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :return: The http_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """Sets the http_proxy of this V2ClusterUpdateParams.

        A proxy URL to use for creating HTTP connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :param http_proxy: The http_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._http_proxy = http_proxy

    @property
    def https_proxy(self):
        """Gets the https_proxy of this V2ClusterUpdateParams.  # noqa: E501

        A proxy URL to use for creating HTTPS connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :return: The https_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._https_proxy

    @https_proxy.setter
    def https_proxy(self, https_proxy):
        """Sets the https_proxy of this V2ClusterUpdateParams.

        A proxy URL to use for creating HTTPS connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :param https_proxy: The https_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._https_proxy = https_proxy

    @property
    def no_proxy(self):
        """Gets the no_proxy of this V2ClusterUpdateParams.  # noqa: E501

        An \"*\" or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying.  # noqa: E501

        :return: The no_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._no_proxy

    @no_proxy.setter
    def no_proxy(self, no_proxy):
        """Sets the no_proxy of this V2ClusterUpdateParams.

        An \"*\" or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying.  # noqa: E501

        :param no_proxy: The no_proxy of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._no_proxy = no_proxy

    @property
    def user_managed_networking(self):
        """Gets the user_managed_networking of this V2ClusterUpdateParams.  # noqa: E501

        Indicate if the networking is managed by the user.  # noqa: E501

        :return: The user_managed_networking of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._user_managed_networking

    @user_managed_networking.setter
    def user_managed_networking(self, user_managed_networking):
        """Sets the user_managed_networking of this V2ClusterUpdateParams.

        Indicate if the networking is managed by the user.  # noqa: E501

        :param user_managed_networking: The user_managed_networking of this V2ClusterUpdateParams.  # noqa: E501
        :type: bool
        """

        self._user_managed_networking = user_managed_networking

    @property
    def additional_ntp_source(self):
        """Gets the additional_ntp_source of this V2ClusterUpdateParams.  # noqa: E501

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :return: The additional_ntp_source of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._additional_ntp_source

    @additional_ntp_source.setter
    def additional_ntp_source(self, additional_ntp_source):
        """Sets the additional_ntp_source of this V2ClusterUpdateParams.

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :param additional_ntp_source: The additional_ntp_source of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._additional_ntp_source = additional_ntp_source

    @property
    def olm_operators(self):
        """Gets the olm_operators of this V2ClusterUpdateParams.  # noqa: E501

        List of OLM operators to be installed.  # noqa: E501

        :return: The olm_operators of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: list[OperatorCreateParams]
        """
        return self._olm_operators

    @olm_operators.setter
    def olm_operators(self, olm_operators):
        """Sets the olm_operators of this V2ClusterUpdateParams.

        List of OLM operators to be installed.  # noqa: E501

        :param olm_operators: The olm_operators of this V2ClusterUpdateParams.  # noqa: E501
        :type: list[OperatorCreateParams]
        """

        self._olm_operators = olm_operators

    @property
    def hyperthreading(self):
        """Gets the hyperthreading of this V2ClusterUpdateParams.  # noqa: E501

        Enable/disable hyperthreading on master nodes, worker nodes, or all nodes.  # noqa: E501

        :return: The hyperthreading of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._hyperthreading

    @hyperthreading.setter
    def hyperthreading(self, hyperthreading):
        """Sets the hyperthreading of this V2ClusterUpdateParams.

        Enable/disable hyperthreading on master nodes, worker nodes, or all nodes.  # noqa: E501

        :param hyperthreading: The hyperthreading of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["masters", "workers", "all", "none"]  # noqa: E501
        if hyperthreading not in allowed_values:
            raise ValueError(
                "Invalid value for `hyperthreading` ({0}), must be one of {1}"  # noqa: E501
                .format(hyperthreading, allowed_values)
            )

        self._hyperthreading = hyperthreading

    @property
    def network_type(self):
        """Gets the network_type of this V2ClusterUpdateParams.  # noqa: E501

        The desired network type used.  # noqa: E501

        :return: The network_type of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this V2ClusterUpdateParams.

        The desired network type used.  # noqa: E501

        :param network_type: The network_type of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["OpenShiftSDN", "OVNKubernetes"]  # noqa: E501
        if network_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_type` ({0}), must be one of {1}"  # noqa: E501
                .format(network_type, allowed_values)
            )

        self._network_type = network_type

    @property
    def schedulable_masters(self):
        """Gets the schedulable_masters of this V2ClusterUpdateParams.  # noqa: E501

        Schedule workloads on masters  # noqa: E501

        :return: The schedulable_masters of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._schedulable_masters

    @schedulable_masters.setter
    def schedulable_masters(self, schedulable_masters):
        """Sets the schedulable_masters of this V2ClusterUpdateParams.

        Schedule workloads on masters  # noqa: E501

        :param schedulable_masters: The schedulable_masters of this V2ClusterUpdateParams.  # noqa: E501
        :type: bool
        """

        self._schedulable_masters = schedulable_masters

    @property
    def cluster_networks(self):
        """Gets the cluster_networks of this V2ClusterUpdateParams.  # noqa: E501

        Cluster networks that are associated with this cluster.  # noqa: E501

        :return: The cluster_networks of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: list[ClusterNetwork]
        """
        return self._cluster_networks

    @cluster_networks.setter
    def cluster_networks(self, cluster_networks):
        """Sets the cluster_networks of this V2ClusterUpdateParams.

        Cluster networks that are associated with this cluster.  # noqa: E501

        :param cluster_networks: The cluster_networks of this V2ClusterUpdateParams.  # noqa: E501
        :type: list[ClusterNetwork]
        """

        self._cluster_networks = cluster_networks

    @property
    def service_networks(self):
        """Gets the service_networks of this V2ClusterUpdateParams.  # noqa: E501

        Service networks that are associated with this cluster.  # noqa: E501

        :return: The service_networks of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: list[ServiceNetwork]
        """
        return self._service_networks

    @service_networks.setter
    def service_networks(self, service_networks):
        """Sets the service_networks of this V2ClusterUpdateParams.

        Service networks that are associated with this cluster.  # noqa: E501

        :param service_networks: The service_networks of this V2ClusterUpdateParams.  # noqa: E501
        :type: list[ServiceNetwork]
        """

        self._service_networks = service_networks

    @property
    def machine_networks(self):
        """Gets the machine_networks of this V2ClusterUpdateParams.  # noqa: E501

        Machine networks that are associated with this cluster.  # noqa: E501

        :return: The machine_networks of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: list[MachineNetwork]
        """
        return self._machine_networks

    @machine_networks.setter
    def machine_networks(self, machine_networks):
        """Sets the machine_networks of this V2ClusterUpdateParams.

        Machine networks that are associated with this cluster.  # noqa: E501

        :param machine_networks: The machine_networks of this V2ClusterUpdateParams.  # noqa: E501
        :type: list[MachineNetwork]
        """

        self._machine_networks = machine_networks

    @property
    def disk_encryption(self):
        """Gets the disk_encryption of this V2ClusterUpdateParams.  # noqa: E501

        Installation disks encryption mode and host roles to be applied.  # noqa: E501

        :return: The disk_encryption of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: DiskEncryption
        """
        return self._disk_encryption

    @disk_encryption.setter
    def disk_encryption(self, disk_encryption):
        """Sets the disk_encryption of this V2ClusterUpdateParams.

        Installation disks encryption mode and host roles to be applied.  # noqa: E501

        :param disk_encryption: The disk_encryption of this V2ClusterUpdateParams.  # noqa: E501
        :type: DiskEncryption
        """

        self._disk_encryption = disk_encryption

    @property
    def ignition_endpoint(self):
        """Gets the ignition_endpoint of this V2ClusterUpdateParams.  # noqa: E501

        Explicit ignition endpoint overrides the default ignition endpoint.  # noqa: E501

        :return: The ignition_endpoint of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: IgnitionEndpoint
        """
        return self._ignition_endpoint

    @ignition_endpoint.setter
    def ignition_endpoint(self, ignition_endpoint):
        """Sets the ignition_endpoint of this V2ClusterUpdateParams.

        Explicit ignition endpoint overrides the default ignition endpoint.  # noqa: E501

        :param ignition_endpoint: The ignition_endpoint of this V2ClusterUpdateParams.  # noqa: E501
        :type: IgnitionEndpoint
        """

        self._ignition_endpoint = ignition_endpoint

    @property
    def tags(self):
        """Gets the tags of this V2ClusterUpdateParams.  # noqa: E501

        A comma-separated list of tags that are associated to the cluster.  # noqa: E501

        :return: The tags of this V2ClusterUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V2ClusterUpdateParams.

        A comma-separated list of tags that are associated to the cluster.  # noqa: E501

        :param tags: The tags of this V2ClusterUpdateParams.  # noqa: E501
        :type: str
        """

        self._tags = tags

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
        if issubclass(V2ClusterUpdateParams, dict):
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
        if not isinstance(other, V2ClusterUpdateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
