placement = {"Python":30, "Java":21, "Testing":40, "PowerBI":25, ".Net":28}

srt = sorted(placement, key=lambda key:placement.get(key), reverse=True)
print(srt)