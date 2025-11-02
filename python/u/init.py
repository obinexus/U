"""
U – Open-Sensor Framework
Consciousness-preservation before commodification.
"""

__version__ = "0.1.0-alpha.0"
__author__  = "Nnamdi M. Okpala (Father of Consciousness)"

from .record import record_session
from .dag   import migrate_state

__all__ = ["record_session", "migrate_state"]
