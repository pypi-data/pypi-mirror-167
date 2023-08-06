class CapturMLError(Exception):
    def __init__(self, status, message, source):
        self.status = status
        self.message = message
        self.source = source

    def get_error_callback(self, request_id):
        return {
            "request_id": request_id,
            "status": self.status,
            "message": self.message
        }

# ============ PubSub Exceptions ============ #
class GoogleCloudPubSubTopicDoesNotExistError(Exception):
    pass

# ============ Google Cloud Storage Exceptions ============ #
class GoogleCloudStoragePermissionError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def get_error_callback(self, request_id):
        return {
            "request_id": request_id,
            "status": self.status,
            "message": self.message
        }

    pass
class GoogleCloudStorageResourceNotFoundError(Exception):
    pass
class GoogleCloudStorageBucketNotFoundError(Exception):
    pass

# ============ Google Cloud Vertex AI Endpoint Exceptions ============ #
class GoogleCloudVertexAIEndpointDoesNotExistError(Exception):
    pass
class GoogleCloudVertexAIEndpointImageTooLargeError(Exception):
    pass
class GoogleCloudVertexAIEndpointNoModelDeployedError(Exception):
    pass

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
