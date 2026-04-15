# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec, RunValidator


class RunSpecFlowerRun(RunSpec):
    """
    RunSpecFlowerRun specifications.
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


class RunValidatorFlowerRun(RunValidator):
    """
    RunValidatorFlowerRun validator.
    """
