import pecan
from pecan import rest
import wsmeext.pecan as wsme_pecan

class ClusterController(rest.RestController):
    """Manages operations on specific Cluster of RabbitMQ nodes"""
    def __init__(self, tenant_id, cluster_id):
        self._tenantId = tenant_id
        self._clusterId = cluster_id

    @pecan.expose()
    def get(self):
        return "GET cluster ID: " + self._clusterId + " in tenant ID: " + self._tenantId

class ClustersController(rest.RestController):
    """Manages operations on Clusters of RabbitMQ nodes within specified tenant"""
    _custom_actions = {
        'clusters': ['POST', 'GET']
    }

    def __init__(self, tenant_id):
        self._tenantId = tenant_id

    @pecan.expose()
    def post_clusters(self):
        return "Creating new cluster within Tenant ID: " + self._tenantId

    @pecan.expose()
    def get_clusters(self):
        return "Retrieving clusters within Tenant ID: " + self._tenantId

    @pecan.expose()
    def _lookup(self, cluster_id, *remainder):
        return ClusterController(self._tenantId, cluster_id), remainder

class V1Controller(object):
    """Version 1 MSGaaS API controller root."""
    @pecan.expose()
    def _lookup(self, tenant_id, *remainder):
        return ClustersController(tenant_id), remainder

