from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...types import File, Response


def _get_kwargs(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Files/workspace/{workspaceId}/file/{fileId}/raw".format(
        client.base_url, workspaceId=workspace_id, fileId=file_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[File, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[File, ProblemDetails]]:
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
) -> Response[Union[File, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        file_id (str):

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
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
) -> Optional[Union[File, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        file_id (str):

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
) -> Response[Union[File, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        file_id (str):

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        file_id=file_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: str,
    file_id: str,
    *,
    client: Client,
) -> Optional[Union[File, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        file_id (str):

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
