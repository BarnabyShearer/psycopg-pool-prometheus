"""Expose psycopg pool's metrics to Prometheus."""

from __future__ import annotations

from typing import Iterator

from prometheus_client.core import REGISTRY, GaugeMetricFamily
from prometheus_client.registry import Collector
from psycopg_pool import AsyncConnectionPool, ConnectionPool


def register(pool: ConnectionPool | AsyncConnectionPool) -> None:
    """Register a posycopg_pool.Pool with prometheus_client."""

    class _PoolCollector(Collector):
        def collect(self) -> Iterator[GaugeMetricFamily]:
            """Expose psycopg Pool metrics to Prometheus."""
            for key, value in pool.get_stats().items():
                yield GaugeMetricFamily(
                    f"psycopg_pool_{key}", "See psycopg Pool metrics", value=value
                )

    REGISTRY.register(_PoolCollector())
