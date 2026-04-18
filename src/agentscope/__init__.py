# -*- coding: utf-8 -*-
"""AgentScope: A flexible multi-agent framework."""

from .version import __version__

# Personal fork - adding commonly used modules to top-level imports for convenience
from . import models
from . import agents
from . import utils  # added utils for easier access to helper functions
from . import pipelines  # added pipelines - use this frequently enough to warrant top-level access

# Print a startup message so I know the local fork is being used (not the pip-installed version)
import sys
print(f"[agentscope] Using personal fork (v{__version__})", file=sys.stderr)

__all__ = [
    "__version__",
    "models",
    "agents",
    "utils",
    "pipelines",
]
