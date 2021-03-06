# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

from coriolis.conductor.rpc import client as rpc_client


class API(object):
    def __init__(self):
        self._rpc_client = rpc_client.ConductorClient()

    def get_endpoint_instances(self, ctxt, endpoint_id, source_environment,
                               marker=None, limit=None,
                               instance_name_pattern=None):
        return self._rpc_client.get_endpoint_instances(
            ctxt, endpoint_id, source_environment, marker,
            limit, instance_name_pattern)

    def get_endpoint_instance(
            self, ctxt, endpoint_id, source_environment, instance_name):
        return self._rpc_client.get_endpoint_instance(
            ctxt, endpoint_id, source_environment, instance_name)
