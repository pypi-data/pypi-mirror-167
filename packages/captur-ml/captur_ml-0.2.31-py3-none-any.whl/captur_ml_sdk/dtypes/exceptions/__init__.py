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
class GoogleCloudVertexAIEndpointDoesNotExistError(Exception):
    def __init__(self, code, endpoint_id):
        self.code = code
        self.message = f"Endpoint {endpoint_id} not found."

class GoogleCloudVertexAIEndpointImageTooLargeError(Exception):
    def __init__(self, code, size_limit):
        self.code = code
        self.message = f"Image greater than {size_limit}."

class GoogleCloudVertexAIEndpointNoModelDeployedError(Exception):
    def __init__(self, code, endpoint_id):
        self.code = code
        self.message = f"No model is deployed at endpoint {endpoint_id}."

class GoogleCloudVertexAIEndpointCorruptedImageError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

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
