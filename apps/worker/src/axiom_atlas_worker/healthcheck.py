from __future__ import annotations

import sys

from redis import Redis

from axiom_atlas_worker.settings import settings


def main() -> int:
    client = Redis.from_url(settings.redis_url)
    client.ping()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        raise SystemExit(1) from None
