"""This module provides a single registry for the whole system.

With it you can find every node that provides a function to others in the system. One of the main uses for the registry
is the implementation of the graceful shutdown via the :class:`RegisterAble`-Interface. If you use the helpers
:class:`interfaces.SandNode` or :class:`interfaces.ShutdownAble` you are already using this interface. Generally it is
recommended to use those wrappers and only fall back on :class:`RegisterAble` if absolutely necessary.
"""

from .registry import RegisterAble as RegisterAble
from .registry import get_node_count as get_node_count
from .registry import get_nodes as get_nodes
from .registry import get_singleton_node as get_singleton_node
