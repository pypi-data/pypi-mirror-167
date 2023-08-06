from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.data_import_response import DataImportResponse
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    data_import_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/DataImport/workspace/{workspaceId}/dataImport/{dataImportId}".format(
        client.base_url, workspaceId=workspace_id, dataImportId=data_import_id
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


def _parse_response(*, response: httpx.Response) -> Optional[DataImportResponse]:
    if response.status_code == 200:
        response_200 = DataImportResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DataImportResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace_id: str,
    data_import_id: str,
    *,
    client: Client,
) -> Response[DataImportResponse]:
    """
    Args:
        workspace_id (str):
        data_import_id (str):

    Returns:
        Response[DataImportResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_import_id=data_import_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: str,
    data_import_id: str,
    *,
    client: Client,
) -> Optional[DataImportResponse]:
    """
    Args:
        workspace_id (str):
        data_import_id (str):

    Returns:
        Response[DataImportResponse]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        data_import_id=data_import_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    data_import_id: str,
    *,
    client: Client,
) -> Response[DataImportResponse]:
    """
    Args:
        workspace_id (str):
        data_import_id (str):

    Returns:
        Response[DataImportResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_import_id=data_import_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: str,
    data_import_id: str,
    *,
    client: Client,
) -> Optional[DataImportResponse]:
    """
    Args:
        workspace_id (str):
        data_import_id (str):

    Returns:
        Response[DataImportResponse]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            data_import_id=data_import_id,
            client=client,
        )
    ).parsed
