# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RuntimeBuilder

from digitalhub_runtime_flower.runtimes.runtime import RuntimeFlower, RuntimeFlowerApp


class RuntimeFlowerBuilder(RuntimeBuilder):
    """RuntaimeFlowerBuilder class."""

    RUNTIME_CLASS = RuntimeFlower


class RuntimeFlowerAppBuilder(RuntimeBuilder):
    """RuntaimeFlowerAppBuilder class."""

    RUNTIME_CLASS = RuntimeFlowerApp
