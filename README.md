# AIFreelanceWebsite

## Features

- Secure code execution runner using Docker
- FastAPI endpoint `/runner/exec` for sandboxed code runs
- Kubernetes job controller example for at-scale execution of code snippets
- Firecracker microVM setup guide for ultimate isolation
- All services require strict authentication and rate-limiting!
- See `backend/services/runner.py`, `backend/routers/runner.py`, `backend/k8s_controller.py`, and `docs/firecracker_setup.md` for details

**Security note:** Never expose execution endpoints (runner/k8s controller) to the public internet. Audit all code execution and enforce limits.

## Usage

See source files above for implementation and integration instructions.