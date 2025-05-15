import httpx


class Slack:
    """Slack message sender that supports multiple bots and channels."""

    def __init__(self, bot_tokens: dict, channel_ids: dict):
        self.bot_tokens = bot_tokens  # e.g., {"GHOST": "xoxb-..."}
        self.channel_ids = channel_ids  # e.g., {"CRITICAL": "C1234", "ALL_KAIROS": "C5678"}

    async def send_message(self, bot_name: str, channel_name: str, text: str):
        bot_token = self.bot_tokens.get(bot_name)
        channel_id = self.channel_ids.get(channel_name)

        if not bot_token or not channel_id:
            raise ValueError(f"Invalid bot or channel name: {bot_name}, {channel_name}")

        url = "https://slack.com/api/chat.postMessage"
        headers = {"Authorization": f"Bearer {bot_token}"}
        data = {"channel": channel_id, "text": f"```{text}```"}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, data=data)

        if response.status_code != 200 or not response.json().get("ok"):
            raise Exception(f"Error sending message: {response.text}")
        return response.json()

    async def send_file(self, bot_name: str, channel_name: str, file_path: str):
        bot_token = self.bot_tokens.get(bot_name)
        channel_id = self.channel_ids.get(channel_name)

        if not bot_token or not channel_id:
            raise ValueError(f"Invalid bot or channel name: {bot_name}, {channel_name}")

        url = "https://slack.com/api/files.upload"
        headers = {"Authorization": f"Bearer {bot_token}"}
        data = {"channels": channel_id}

        async with httpx.AsyncClient() as client:
            with open(file_path, "rb") as file:
                files = {"file": (file_path, file, "application/octet-stream")}
                response = await client.post(url, headers=headers, data=data, files=files)

        if response.status_code != 200 or not response.json().get("ok"):
            raise Exception(f"Error uploading file: {response.text}")
        return response.json()
