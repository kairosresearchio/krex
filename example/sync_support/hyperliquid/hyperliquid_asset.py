from krex.hyperliquid.client import Client


client = Client()

result = client.user_vault_equities(user="0x8C41a1cB41bbEC8108E5E421007E17b8336E17dE")
print(result)
