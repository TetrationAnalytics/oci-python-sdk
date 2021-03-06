# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIdentityProviderDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIdentityProviderDetails object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.identity.models.UpdateSaml2IdentityProviderDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this UpdateIdentityProviderDetails.
            Allowed values for this property are: "SAML2"
        :type protocol: str

        :param description:
            The value to assign to the description property of this UpdateIdentityProviderDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIdentityProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIdentityProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'protocol': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._protocol = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['protocol']

        if type == 'SAML2':
            return 'UpdateSaml2IdentityProviderDetails'
        else:
            return 'UpdateIdentityProviderDetails'

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this UpdateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`

        Allowed values for this property are: "SAML2"


        :return: The protocol of this UpdateIdentityProviderDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`


        :param protocol: The protocol of this UpdateIdentityProviderDetails.
        :type: str
        """
        allowed_values = ["SAML2"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def description(self):
        """
        Gets the description of this UpdateIdentityProviderDetails.
        The description you assign to the `IdentityProvider`. Does not have to
        be unique, and it's changeable.


        :return: The description of this UpdateIdentityProviderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateIdentityProviderDetails.
        The description you assign to the `IdentityProvider`. Does not have to
        be unique, and it's changeable.


        :param description: The description of this UpdateIdentityProviderDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateIdentityProviderDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateIdentityProviderDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateIdentityProviderDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateIdentityProviderDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateIdentityProviderDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this UpdateIdentityProviderDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateIdentityProviderDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this UpdateIdentityProviderDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
