# Log Report – Harbor TB2 Fixed Task

This repository contains the corrected version of the **Log Report** Terminal-Bench 2 (Harbor) task.

## Objective

The task parses an Apache-style access log and generates a JSON report containing:

- Total number of requests
- Number of unique client IP addresses
- Most frequently requested path

The generated report is written to:

```
/app/report.json
```

## Project Structure

```
log-report/
├── task.toml
├── instruction.md
├── environment/
│   ├── Dockerfile
│   └── access.log
├── solution/
│   ├── solve.py
│   └── solve.sh
└── tests/
    ├── test_outputs.py
    └── test.sh
```

## Expected Output

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

## Defects Fixed

The original task contained multiple authoring issues. The following were corrected:

- Fixed `task.toml` artifacts declaration (array instead of string)
- Corrected artifact path to `/app/report.json`
- Added proper TB2 task metadata
- Rewrote `instruction.md` with clear numbered success criteria
- Removed leaked reference solution from the Docker image
- Updated Dockerfile to use an approved pinned base image
- Improved verifier to validate JSON contents instead of only checking file existence
- Updated `test.sh` to write:
  - `/logs/verifier/reward.txt`
  - `/logs/verifier/ctrf.json`
- Ensured consistency between:
  - instructions
  - verifier
  - task.toml
  - oracle solution

## Running

### Oracle

```bash
harbor run -p log-report -a oracle
```

Expected reward:

```
1
```

### No-op Agent

```bash
harbor run -p log-report --agent nop
```

Expected reward:

```
0
```

## Requirements

- Docker
- Harbor (TB2)

Install Harbor:

```bash
uv tool install harbor
```

Verify installation:

```bash
harbor --version
docker --version
```

## Notes

This task follows the Harbor TB2 task format and produces a deterministic JSON artifact suitable for automated verification.
