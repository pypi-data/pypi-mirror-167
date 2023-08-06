"""This module provides an easy possibility to collect and push metrics to an InfluxDB.

Just add your :class:`datatypes.Datapoint`s to the :func:`get_metric_queue` and the :class:`Comitter` will take care of
it.
"""
from .committer import Committer as Committer
from .delta import Calculator as Calculator
from .delta import DeltaCollector as DeltaCollector
