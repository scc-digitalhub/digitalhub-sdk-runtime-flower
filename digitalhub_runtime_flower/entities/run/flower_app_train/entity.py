# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import LocalExecutionRunMixin, Run, RunStatus

from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain


class RunFlowerAppTrain(LocalExecutionRunMixin, Run):
    """
    RunFlowerAppTrain class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecFlowerAppTrain
        self.status: RunStatus
