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

# Suppress the startup message when running in non-interactive/test environments
# (avoids cluttering pytest output)
import os
if os.environ.get("AGENTSCOPE_QUIET") or not sys.stderr.isatty():
    pass  # message already printed above; could conditionally suppress in future

__all__ = [
    "__version__",
    "models",
    "agents",
    "utils",
    "pipelines",
]
