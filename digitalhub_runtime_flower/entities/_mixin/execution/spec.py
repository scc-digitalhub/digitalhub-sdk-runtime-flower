# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Spec


class FlowerConnectionSpecMixin(Spec):
    """Connection fields shared by Flower application and client specs."""

    superlink: str | None = None
    root_certificates: str | None = None


class FlowerClientSpecMixin(FlowerConnectionSpecMixin):
    """Specification fields shared by Flower client tasks and runs."""

    node_config: dict | None = None
    private_key_secret: str | None = None
    public_key_secret: str | None = None
    isolation: str | None = None


class FlowerServerSpecMixin(Spec):
    """Specification fields shared by Flower server tasks and runs."""

    auth_public_keys: list[str] | None = None
    insecure: bool = False


class FlowerTrainSpecMixin(Spec):
    """Specification fields shared by Flower training tasks and runs."""

    schedule: str | None = None
