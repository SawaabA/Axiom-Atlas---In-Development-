# Security

## Current Controls

- environment-variable based configuration
- no secrets committed
- server-side only API and ML service tokens
- parameterized route handling with typed validation
- bounded graph neighborhood limits

## Required Next Steps

- auth provider integration
- role-based access control
- query timeouts for graph and search backends
- CSP and CORS hardening
- dependency and container scanning in CI
