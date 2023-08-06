"""
Seldon deployment exception handler module.
"""
from kubernetes.client import ApiException


class SeldonDeploymentException(ApiException):
    """
    Seldon Deployment Exception Class Handler.
    """

    def __init__(self, *, status=None, reason=None, http_resp=None):
        """_summary_
        The constructor for the exception class handler.

        Args:
            status (_type_, optional): _description_. Defaults to None. The exception status code.
            reason (_type_, optional): _description_. Defaults to None. The exception elaborated reason.
            http_resp (_type_, optional): _description_. Defaults to None. The HTTP response.
        """
        self.status = status
        self.reason = reason
        self.http_resp = http_resp
        self.body = http_resp.data
        self.headers = http_resp.getheaders()
        super(SeldonDeploymentException, self).__init__(
            status, reason, http_resp)
