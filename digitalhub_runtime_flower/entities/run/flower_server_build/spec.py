# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import BuildSpecMixin

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun


class RunSpecFlowerServerBuild(RunSpecFlowerRun, BuildSpecMixin):
    """Specification for a Flower server build run."""

    auth_public_keys: list[str] | None = None
    """List of public keys for authentication."""

    insecure: bool = False
    """Flag to allow insecure connections."""
