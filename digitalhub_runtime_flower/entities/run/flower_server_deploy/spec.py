# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun


class RunSpecFlowerServerDeploy(RunSpecFlowerRun):
    """Specification for a Flower server deployment run."""

    auth_public_keys: list[str] | None = None
    """Authentication public keys."""

    insecure: bool = False
    """Disable TLS verification."""
