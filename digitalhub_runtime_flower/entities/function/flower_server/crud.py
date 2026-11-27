# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_flower.entities._commons.enums import EntityKinds

if typing.TYPE_CHECKING:
    from digitalhub_runtime_flower.entities.function._base.entity import FunctionFlowerBuild


def new_function_flower_server(
    project: str,
    name: str,
    image: str | None = None,
    base_image: str | None = None,
    requirements: list[str] | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionFlowerBuild:
    """
    Create a Flower server function entity.

    Examples
    --------
    Create a server function using a prebuilt image:

    ```python
    import digitalhub as dh

    function = dh.new_function_flower_server(
        project="my-project",
        name="flower-server",
        image="ghcr.io/example/flower-server:latest",
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=EntityKinds.FUNCTION_FLOWER_SERVER.value,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        image=image,
        base_image=base_image,
        requirements=requirements,
    )
