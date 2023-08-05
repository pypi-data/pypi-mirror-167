class MissingFieldError(Exception):
    """Raised when fields are missing from mlops_settings.yaml"""


class TestError(Exception):
    """Raised when tests are failing"""


class DeploymentError(Exception):
    """Raised when deployment fails"""
