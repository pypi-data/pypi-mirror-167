from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.data_source_response import DataSourceResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    data_source_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/DataSource/workspace/{workspaceId}/dataSource/{dataSourceId}".format(
        client.base_url, workspaceId=workspace_id, dataSourceId=data_source_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[DataSourceResponse, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = DataSourceResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DataSourceResponse, ProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace_id: str,
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[DataSourceResponse, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_source_id (str):

    Returns:
        Response[Union[DataSourceResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_source_id=data_source_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: str,
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[DataSourceResponse, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_source_id (str):

    Returns:
        Response[Union[DataSourceResponse, ProblemDetails]]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        data_source_id=data_source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[DataSourceResponse, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_source_id (str):

    Returns:
        Response[Union[DataSourceResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_source_id=data_source_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: str,
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[DataSourceResponse, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_source_id (str):

    Returns:
        Response[Union[DataSourceResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            data_source_id=data_source_id,
            client=client,
        )
    ).parsed
