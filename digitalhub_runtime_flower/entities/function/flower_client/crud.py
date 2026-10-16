# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_flower.entities.function.flower_client.builder import FunctionFlowerClientBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_flower.entities.function.flower_client.entity import FunctionFlowerClient


def new_function_flower_client(
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
) -> FunctionFlowerClient:
    """
    Create a Flower client function entity.

    Examples
    --------
    Create a client function using a prebuilt image:

    ```python
    import digitalhub as dh

    function = dh.new_function_flower_client(
        project="my-project",
        name="flower-client",
        image="ghcr.io/example/flower-client:latest",
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=FunctionFlowerClientBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        image=image,
        base_image=base_image,
        requirements=requirements,
    )
