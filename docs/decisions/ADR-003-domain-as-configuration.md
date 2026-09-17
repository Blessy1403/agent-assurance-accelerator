# ADR-003: Domain as Configuration

## Status

Accepted

## Date

2026-09-07

## Context

The Agent Assurance Accelerator (AAA) is intended to be reusable across multiple business domains rather than being limited to insurance claims processing.

The platform needs to support domain-specific concepts such as:

- Case types
- Field definitions
- Validation ranges
- Consistency-testing attributes
- Outcome mappings

If this information is embedded directly into Python code, every new domain would require application code changes, additional testing, and redeployment.

Examples of future domains may include:

- Insurance
- Banking
- Telecommunications
- Customer service operations

The project therefore requires a mechanism that separates business-domain definitions from application logic.

## Decision

Domain knowledge will be stored in YAML configuration files rather than hardcoded in Python.

For the reference implementation, the insurance domain is represented by:

```text
aaa/domain/insurance.yaml