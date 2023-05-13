#
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""The arg spec for the ioscm facts module."""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


class FactsArgs:
    """The arg spec for the ioscm facts module."""

    def __init__(self, **kwargs) -> None:
        pass

    argument_spec = {
        "gather_subset": {"default": ["min"], "type": "list", "elements": "str"},
        "gather_network_resources": {"type": "list", "elements": "str"},
        "available_network_resources": {"type": "bool", "default": False},
    }
