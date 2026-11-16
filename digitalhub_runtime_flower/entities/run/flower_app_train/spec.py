# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import LocalExecutionSpecMixin

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun
from digitalhub_runtime_flower.entities.task.flower_app_train.spec import FlowerTrainSpecMixin


class RunSpecFlowerAppTrain(RunSpecFlowerRun, FlowerTrainSpecMixin, LocalExecutionSpecMixin):
    """Specification for a Flower application training run."""

    fab_source: dict | None = None
    parameters: dict | None = None
    federation: str | None = None
    superlink: str | None = None
    root_certificates: str | None = None
