# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun, RunValidatorFlowerRun


class RunSpecFlowerServerBuild(RunSpecFlowerRun):
    """
    RunSpecFlowerServerBuild specifications.
    """

    def __init__(
        self,
        task: str,
        function: str | None = None,
        workflow: str | None = None,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        instructions: list[str] | None = None,
        image: str | None = None,
        base_image: str | None = None,
        requirements: list[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            task=task,
            function=function,
            workflow=workflow,
            volumes=volumes,
            resources=resources,
            envs=envs,
            secrets=secrets,
            profile=profile,
            **kwargs,
        )
        self.instructions = instructions
        self.image = image
        self.base_image = base_image
        self.requirements = requirements


class RunValidatorFlowerServerBuild(RunValidatorFlowerRun):
    """
    RunValidatorFlowerServerBuild validator.
    """

    # Function parameters
    image: str | None = None
    base_image: str | None = None
    requirements: list[str] | None = None

    # Task parameters
    instructions: list[str] | None = None
