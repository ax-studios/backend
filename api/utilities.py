import uuid


def isValidUUID(uuid_string: str) -> bool:
    try:
        x = "{" + uuid_string + "}"
        uuid.UUID(x)
        return True
    except ValueError:
        return False
