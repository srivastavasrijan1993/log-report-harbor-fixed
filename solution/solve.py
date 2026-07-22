import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

with open("/app/access.log", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        total += 1
        ips.add(line.split()[0])

        match = re.search(
            r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH)\s+(\S+)\s+HTTP/[\d.]+"',
            line,
        )
        if match:
            paths[match.group(1)] += 1

report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": paths.most_common(1)[0][0] if paths else None,
}

with open("/app/report.json", "w", encoding="utf-8") as out:
    json.dump(report, out)

print("wrote /app/report.json")
