# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import typing
from pathlib import Path

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.file_utils import eval_py_type
from digitalhub.utils.generic_utils import encode_source, encode_string
from digitalhub.utils.uri_utils import has_git_scheme, has_local_scheme

if typing.TYPE_CHECKING:
    from digitalhub_runtime_flower.entities.function.flower_app.entity import FunctionFlowerApp


def source_check(**kwargs) -> dict:
    """
    Check source code.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    dict
        Checked source.
    """
    fab_source: dict = kwargs.pop("fab_source", None)
    source: str = kwargs.pop("source", None)
    client_src: str = kwargs.pop("client_src", None)
    server_src: str = kwargs.pop("server_src", None)
    client_app: str = kwargs.pop("client_app", None)
    server_app: str = kwargs.pop("server_app", None)

    client_base64 = None
    server_base64 = None

    if fab_source is not None:
        source = fab_source.get("source")
        client_app = fab_source.get("clientapp")
        server_app = fab_source.get("serverapp")
        client_base64 = fab_source.get("clientbase64")
        server_base64 = fab_source.get("serverbase64")
        # No src in fab_source

    kwargs["fab_source"] = _check_params(
        source=source,
        client_src=client_src,
        server_src=server_src,
        client_app=client_app,
        server_app=server_app,
        client_base64=client_base64,
        server_base64=server_base64,
    )
    return kwargs


def _check_params(
    source: str | None = None,
    client_src: str | None = None,
    server_src: str | None = None,
    client_app: str | None = None,
    server_app: str | None = None,
    client_base64: str | None = None,
    server_base64: str | None = None,
) -> dict:
    """
    Check source code.

    Parameters
    ----------
    source : str | None
        Github repository URL.
    client_src : str | None
        Client application str source code.
    server_src : str | None
        Server application str source code.
    clientapp : str | None
        Local client application path.
    serverapp : str | None
        Local server application path.
    clientbase64 : str | None
        Client application base64.
    serverbase64 : str | None
        Server application base64.

    Returns
    -------
    dict
        Checked source.
    """
    fab_source = {}

    if source is not None:
        fab_source["source"] = source

    if client_app is not None:
        fab_source["clientapp"] = client_app

    if server_app is not None:
        fab_source["serverapp"] = server_app

    if client_src is not None or client_base64 is not None:
        if client_src is not None:
            fab_source["clientbase64"] = encode_string(client_src)
        else:
            fab_source["clientbase64"] = client_base64

    if server_src is not None or server_base64 is not None:
        if server_src is not None:
            fab_source["serverbase64"] = encode_string(server_src)
        else:
            fab_source["serverbase64"] = server_base64

    return fab_source


def source_post_check(exec: FunctionFlowerApp) -> FunctionFlowerApp:
    """
    Post check source.

    Parameters
    ----------
    exec : FunctionFlowerApp
        Executable.

    Returns
    -------
    FunctionFlowerApp
        Updated executable.
    """
    if exec.spec.fab_source is None:
        return exec

    # Get clientapp and serverapp
    clientapp = exec.spec.fab_source.get("clientapp", None)
    serverapp = exec.spec.fab_source.get("serverapp", None)
    if clientapp is None or serverapp is None:
        raise EntityError("Either source or both clientapp and serverapp must be provided.")

    # Return if git source
    git_source = exec.spec.fab_source.get("source", None)
    if git_source is not None:
        if not has_git_scheme(git_source):
            raise EntityError("Source must be a valid git URL.")
        return exec

    # Return if already encoded
    clientappbase64 = exec.spec.fab_source.get("clientbase64", None)
    serverappbase64 = exec.spec.fab_source.get("serverbase64", None)
    if clientappbase64 is not None and serverappbase64 is not None:
        return exec

    # Encode clientapp and serverapp
    try:
        clientapp = _validate_handler(clientapp)
        serverapp = _validate_handler(serverapp)

        clientapp_path = _parse_local_app(clientapp)
        if has_local_scheme(clientapp_path) and Path(clientapp_path).is_file():
            exec.spec.fab_source["clientappbase64"] = encode_source(clientapp_path)

        serverapp_path = _parse_local_app(serverapp)
        if has_local_scheme(serverapp_path) and Path(serverapp_path).is_file():
            exec.spec.fab_source["serverappbase64"] = encode_source(serverapp_path)

    except Exception as e:
        raise EntityError(f"Error encoding source: {e}")

    return exec


def _parse_local_app(handler: str) -> str:
    """
    Parse local app.

    Parameters
    ----------
    handler : str
        Handler.

    Returns
    -------
    str
        Parsed handler.
    """
    return handler.split(":")[0].replace(".", os.sep) + ".py"


def _validate_handler(handler: str) -> None:
    """
    Validate handler.

    Parameters
    ----------
    handler : str
        Handler.
    """
    if not isinstance(handler, str):
        raise EntityError("Handler must be a string.")
    if ":" not in handler or len(handler.split(":")) != 2:
        raise EntityError("Handler must be in the form 'module.path:callable'.")
    if not eval_py_type(handler.split(":")[0].replace(".", os.sep) + ".py"):
        raise EntityError("Handler must be a valid Python file.")
    return handler
