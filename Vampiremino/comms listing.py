from pymino import Client

client = Client(
    command_prefix="!",
    console_enabled=True,
    device_id='0136a754f2e4de68cbb2a5f94632bb04bafc0c0c4d73b364af2c9e1b0d2da51b840416c96592cabb7e',
    device_key='c1caaf081376b4bc83df15ef7deda917a4b56f55',
    signature_key='a5200a71589409a4629dda94c5ae9ee91bd7a2d0',
    service_key='c22b5523-e67e-4460-8bb1-92a8cb3b0112',
    intents=True,
    online_status=True,
    proxy="http://127.0.0.1:8000"
    )
client.login(email="kikikhristine@hotmail.com", password="TheHuntress4nn4")


async def on_ready():
    communities = client.sub_clients()
    for community in communities:
        print(f"Community Name: {community.name}, ID: {community.id}")
