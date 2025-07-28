def serialize_to_csv(value):
    if isinstance(value, list):
        return ",".join(str(v) for v in value)
    return value

def remove_empty_values(data):
    return {k: v for k, v in data.items() if v is not None}