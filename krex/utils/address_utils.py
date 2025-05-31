def address_to_bytes(address):
    return bytes.fromhex(address[2:] if address.startswith("0x") else address)
