import os

from azure.storage.blob import ContainerClient

from mlflow.exceptions import MlflowException
from mlflow.store.artifact.azure_blob_artifact_repo import AzureBlobArtifactRepository


class KozaiArtifactRepository(AzureBlobArtifactRepository):
    """
    Stores artifacts on Azure Blob Storage.
    For the most part this uses the functionality of `AzureBlobArtifactRepository`, but
    parses simple "kozai://" scheme uris
    """

    def __init__(self, artifact_uri):
        """
        We override init, as we have different setup/parsing to do
        """

        # Confusingly, this is the notation to call the __init__ method on the base
        # ArtifactRepository class, and avoid the __init__ method of the AzureBlobArtifactRepository
        super(AzureBlobArtifactRepository, self).__init__(artifact_uri)

        if not artifact_uri.startswith("kozai://"):
            raise MlflowException(
                f"Unknown kozai artifact repository uri: {artifact_uri}"
            )

        container_client = ContainerClient.from_container_url(
            container_url=os.environ["MLFLOW_ARTIFACTS_AZURE_STORAGE_SAS_URI"],
        )

        class ServiceClientMock:
            def get_container_client(self, container):
                return container_client

        self.client = ServiceClientMock()

    @staticmethod
    def parse_wasbs_uri(artifact_uri: str):
        """
        We override parse_wasbs_uri as we have different url parsing to do.
        Overriding this means all the other functionality we can rely on from AzureBlobArtifactRepository.

        However, we assume that only the 1st and 3rd returned values are ever used. This matches
        the current AzureBlobArtifactRepository but is something to be aware of. AzureBlobArtifactRepository
        only uses the 2nd and 4th values within it's __init__, which we override.

        For kozai, uris are of the form: kozai://<container>/<path-with-/s>
        So we can do a simple split on / to parse the components.
        """
        split = artifact_uri.split("/")
        container_name = split[2]  # split[0] = "kozai" and split[1] = "" (as //)
        artifact_path = "/".join(
            split[3:]
        )  # rejoin all beyond 3 as path may contain more slashes
        return container_name, None, artifact_path, None
