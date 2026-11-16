# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import BuildSpecMixin

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun


class RunSpecFlowerClientBuild(RunSpecFlowerRun, BuildSpecMixin):
    """Specification for a Flower client build run."""

    superlink: str | None = None
    node_config: dict | None = None
    root_certificates: str | None = None
    private_key_secret: str | None = None
    public_key_secret: str | None = None
    isolation: str | None = None
