import asyncio

async def subscribe_to_events():
    while True:
        event = await get_next_event_from_your_pipeline()
        yield event