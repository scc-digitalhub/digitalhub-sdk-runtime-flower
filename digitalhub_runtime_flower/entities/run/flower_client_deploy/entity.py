# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Run, RunStatus

from digitalhub_runtime_flower.entities.run.flower_client_deploy.spec import RunSpecFlowerClientDeploy


class RunFlowerClientDeploy(Run):
    """
    RunFlowerClientDeploy class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecFlowerClientDeploy
        self.status: RunStatus
