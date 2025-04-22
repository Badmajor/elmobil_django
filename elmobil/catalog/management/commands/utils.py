from datetime import timedelta


def normalize_time(input_str):
    if not input_str or input_str == "-":
        return None
    total_minutes = 0
    if "hour" in input_str or "min" in input_str:
        parts = input_str.split()
        for i in range(0, len(parts), 2):
            value = int(parts[i])
            unit = parts[i + 1].lower()
            if unit.startswith("hour"):
                total_minutes += value * 60
            elif unit.startswith("min"):
                total_minutes += value
            return timedelta(minutes=total_minutes)
    elif "h" in input_str:
        parts = input_str.split("h")
        hours = int(parts[0]) if parts[0] else 0
        minutes = int(parts[1].rstrip("m")) if len(parts) > 1 else 0
        return timedelta(hours=hours, minutes=minutes)


def normalize_data(data: dict) -> dict:
    copy_data = dict()
    for key, value in data.items():
        if "\\t" in key or "*" in key:
            copy_data[key.split("\\")[0].replace("*", "").strip()] = value
        else:
            copy_data[key.strip()] = value
    return copy_data
