# ADR-001: Integrate an observability backend rather than build one

Date: 2026-08-28
Author: Engineer A
Status: accepted

## Context

We need to capture per-agent traces from the claims pipeline. Established tools already exist for this purpose, including Langfuse, LangSmith, and Arize.

## Decision

Define a thin `TraceBackend` interface.

Ship a local SQLite implementation as the default, plus one adapter to a hosted observability tool.

## Rejected alternative

Building our own tracing store as the only implementation.

Although it appears simpler initially, it creates a long-term maintenance obligation and increases implementation risk.

## Consequences

A small abstraction cost is introduced.

In return, the solution can integrate with existing customer observability platforms rather than replacing them.