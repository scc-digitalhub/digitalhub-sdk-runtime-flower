# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import LocalExecutionSpecMixin

from digitalhub_runtime_flower.entities._mixin.execution.spec import FlowerConnectionSpecMixin, FlowerTrainSpecMixin
from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun


class RunSpecFlowerAppTrain(
    RunSpecFlowerRun,
    FlowerConnectionSpecMixin,
    FlowerTrainSpecMixin,
    LocalExecutionSpecMixin,
):
    """Specification for a Flower application training run."""

    fab_source: dict | None = None
    parameters: dict | None = None
    federation: str | None = None
