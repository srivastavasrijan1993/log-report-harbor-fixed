Parse the Apache access log located at /app/access.log and write a JSON report to /app/report.json.

The JSON object must contain exactly these keys:

- total_requests
- unique_ips
- top_path

Success criteria:

1. Read every non-empty line in /app/access.log.
2. Set total_requests to the total number of requests in the log.
3. Set unique_ips to the number of distinct client IP addresses.
4. Set top_path to the request path that appears most frequently.
5. Write valid JSON to /app/report.json.
