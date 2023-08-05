import uvicorn

import aiords



service = aiords.Port(
    name="test",
    display_name="Test Service",
    description="A test port to review interface integration.",
    implements=["metadata"],
    transfer_mode=aiords.FileTransferMode.active,
    archive=aiords.FileTransferArchive.zip,
    info_url="https://example.com/info",
    help_url="https://example.com/help"
)


if __name__ == '__main__':
    uvicorn.run('__main__:service') # type: ignore