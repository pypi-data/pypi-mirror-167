"""Mixin for BaseAioPool with async generator features, python3.6+"""

import asyncio as aio
from .results import getres


async def iterwait(
    futures,
    *,
    flat=True,
    get_result=getres.flat,
    timeout=None,
    yield_when=aio.ALL_COMPLETED
):
    """Wraps `asyncio.wait` into asynchronous generator, accessible with
    `async for` syntax. May be useful in conjunction with `spawn_n`.

    `timeout` and `yield_when` parameters are passed to `asyncio.wait`, see
    documentation for this great instrument.

    Returns results for provided futures, as soon as results are ready. If
    `flat` is True -- generates one result at a time (per `async for`). If
    `flat` is False -- generates a list of ready results.
    """
    _futures = futures[:]
    while _futures:
        done, _futures = await aio.wait(
            _futures, timeout=timeout, return_when=yield_when
        )
        if flat:
            for fut in done:
                yield get_result(fut)
        else:
            yield [get_result(fut) for fut in done]
