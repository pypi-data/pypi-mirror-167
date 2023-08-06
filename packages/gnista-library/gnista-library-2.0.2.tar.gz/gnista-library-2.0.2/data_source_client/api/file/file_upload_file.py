from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.file_upload_file_multipart_data import FileUploadFileMultipartData
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
    multipart_data: FileUploadFileMultipartData,
) -> Dict[str, Any]:
    url = "{}/File/workspace/{workspaceId}/file/{fileId}".format(
        client.base_url, workspaceId=workspace_id, fileId=file_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ProblemDetails]:
    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[ProblemDetails]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
    multipart_data: FileUploadFileMultipartData,
) -> Response[ProblemDetails]:
    """
    Args:
        workspace_id (str):
        file_id (str):
        multipart_data (FileUploadFileMultipartData):

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
    multipart_data: FileUploadFileMultipartData,
) -> Optional[ProblemDetails]:
    """
    Args:
        workspace_id (str):
        file_id (str):
        multipart_data (FileUploadFileMultipartData):

    Returns:
        Response[ProblemDetails]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
    multipart_data: FileUploadFileMultipartData,
) -> Response[ProblemDetails]:
    """
    Args:
        workspace_id (str):
        file_id (str):
        multipart_data (FileUploadFileMultipartData):

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
    multipart_data: FileUploadFileMultipartData,
) -> Optional[ProblemDetails]:
    """
    Args:
        workspace_id (str):
        file_id (str):
        multipart_data (FileUploadFileMultipartData):

    Returns:
        Response[ProblemDetails]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            file_id=file_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
