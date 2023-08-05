# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_deb.configuration import Configuration


class AptRepositorySyncURL(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'remote': 'str',
        'mirror': 'bool',
        'optimize': 'bool'
    }

    attribute_map = {
        'remote': 'remote',
        'mirror': 'mirror',
        'optimize': 'optimize'
    }

    def __init__(self, remote=None, mirror=False, optimize=True, local_vars_configuration=None):  # noqa: E501
        """AptRepositorySyncURL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remote = None
        self._mirror = None
        self._optimize = None
        self.discriminator = None

        if remote is not None:
            self.remote = remote
        if mirror is not None:
            self.mirror = mirror
        if optimize is not None:
            self.optimize = optimize

    @property
    def remote(self):
        """Gets the remote of this AptRepositorySyncURL.  # noqa: E501

        A remote to sync from. This will override a remote set on repository.  # noqa: E501

        :return: The remote of this AptRepositorySyncURL.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this AptRepositorySyncURL.

        A remote to sync from. This will override a remote set on repository.  # noqa: E501

        :param remote: The remote of this AptRepositorySyncURL.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def mirror(self):
        """Gets the mirror of this AptRepositorySyncURL.  # noqa: E501

        If ``True``, synchronization will remove all content that is not present in the remote repository. If ``False``, sync will be additive only.  # noqa: E501

        :return: The mirror of this AptRepositorySyncURL.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this AptRepositorySyncURL.

        If ``True``, synchronization will remove all content that is not present in the remote repository. If ``False``, sync will be additive only.  # noqa: E501

        :param mirror: The mirror of this AptRepositorySyncURL.  # noqa: E501
        :type: bool
        """

        self._mirror = mirror

    @property
    def optimize(self):
        """Gets the optimize of this AptRepositorySyncURL.  # noqa: E501

        Using optimize sync, will skip the processing of metadata if the checksum has not changed since the last sync. This greately improves re-sync performance in such situations. If you feel the sync is missing something that has changed about the remote repository you are syncing, try using optimize=False for a full re-sync. Consider opening an issue on why we should not optimize in your use case.  # noqa: E501

        :return: The optimize of this AptRepositorySyncURL.  # noqa: E501
        :rtype: bool
        """
        return self._optimize

    @optimize.setter
    def optimize(self, optimize):
        """Sets the optimize of this AptRepositorySyncURL.

        Using optimize sync, will skip the processing of metadata if the checksum has not changed since the last sync. This greately improves re-sync performance in such situations. If you feel the sync is missing something that has changed about the remote repository you are syncing, try using optimize=False for a full re-sync. Consider opening an issue on why we should not optimize in your use case.  # noqa: E501

        :param optimize: The optimize of this AptRepositorySyncURL.  # noqa: E501
        :type: bool
        """

        self._optimize = optimize

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AptRepositorySyncURL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AptRepositorySyncURL):
            return True

        return self.to_dict() != other.to_dict()
