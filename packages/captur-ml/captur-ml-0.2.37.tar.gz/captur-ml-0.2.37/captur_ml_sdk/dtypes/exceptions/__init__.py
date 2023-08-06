class CapturException(Exception):
    def __init__(self):
        self.captur_code = "400"

# ============ PubSub Exceptions ============ #
class GoogleCloudPubSubTopicDoesNotExistError(Exception):
    pass

# ============ Google Cloud Storage Exceptions ============ #
class GoogleCloudStoragePermissionError(Exception):
    pass
class GoogleCloudStorageResourceNotFoundError(Exception):
    pass
class GoogleCloudStorageBucketNotFoundError(Exception):
    pass

# ============ Google Cloud Vertex AI Endpoint Exceptions ============ #
class GoogleCloudVertexAIEndpointDoesNotExistError(CapturException):
    def __init__(self, code, endpoint_id):
        super().__init__()
        self.captur_message = f"Endpoint {endpoint_id} not found. Google Error Code <{code}>"

class GoogleCloudVertexAIEndpointImageTooLargeError(CapturException):
    def __init__(self, code, size_limit):
        super().__init__()
        self.captur_message = f"Image greater than {size_limit}. Google Error Code <{code}>"

class GoogleCloudVertexAIEndpointNoModelDeployedError(CapturException):
    def __init__(self, code, endpoint_id):
        super().__init__()
        self.captur_message = f"No model is deployed at endpoint {endpoint_id}. Google Error Code <{code}>"

class GoogleCloudVertexAIEndpointCorruptedImageError(CapturException):
    def __init__(self, code, message):
        super().__init__()
        self.captur_message = f"{message} Google Error Code <{code}>"

# ============ Google Cloud Vertex AI General Exceptions ============ #
class GoogleCloudVertexAIModelDoesNotExistError(Exception):
    pass
class GoogleCloudVertexAIDatasetDoesNotExistError(Exception):
    pass
class GoogleCloudVertexAIResourceDoesNotExistError(Exception):
    pass
class GoogleCloudVertexAICompatibilityError(Exception):
    pass

# ============ Sentry Errors ============ #
class SentryDSNNotProvidedError(Exception):
    pass
