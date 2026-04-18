# -*- coding: utf-8 -*-
"""AgentScope: A flexible multi-agent framework."""

from .version import __version__

# Personal fork - adding commonly used modules to top-level imports for convenience
from . import models
from . import agents

__all__ = [
    "__version__",
    "models",
    "agents",
]
