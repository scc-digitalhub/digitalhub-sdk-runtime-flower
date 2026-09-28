# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_flower.entities.function.flower_app.builder import FunctionFlowerAppBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_flower.entities.function.flower_app.entity import FunctionFlowerApp


def new_function_flower_app(
    project: str,
    name: str,
    git_source: str | None = None,
    client_code: str | None = None,
    server_code: str | None = None,
    client_src: str | None = None,
    server_src: str | None = None,
    client_app: str | None = None,
    server_app: str | None = None,
    fab_source: dict | None = None,
    image: str | None = None,
    base_image: str | None = None,
    requirements: list[str] | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionFlowerApp:
    """Create a Flower application function entity."""
    if client_code is not None and client_src is not None:
        raise ValueError("Only one of 'client_code' or 'client_src' can be provided.")
    if server_code is not None and server_src is not None:
        raise ValueError("Only one of 'server_code' or 'server_src' can be provided.")

    return new_function(
        project=project,
        name=name,
        kind=FunctionFlowerAppBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        git_source=git_source,
        client_code=client_code,
        server_code=server_code,
        client_src=client_src,
        server_src=server_src,
        client_app=client_app,
        server_app=server_app,
        fab_source=fab_source,
        image=image,
        base_image=base_image,
        requirements=requirements,
    )
