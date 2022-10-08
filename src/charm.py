#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""NFS node operator.
"""

import logging

from ops.main import main

from hpctinterfaces.relation import interface_registry
from hpctops.charm.node import NodeCharm


logger = logging.getLogger(__name__)


class HpctNfsNodeCharm(NodeCharm):
    """Operator for cluster nfs node."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.interfaces = {
            "ldap-client-ready": interface_registry.load(
                "relation-subordinate-ready", self, "ldap-client-ready"
            ),
        }

        self.setup_subordinate_relations_and_syncs(["ldap-client-ready"])


if __name__ == "__main__":
    main(HpctNfsNodeCharm)
