# ADR-004: Pair Semantics

## Status

Accepted

## Date

2026-09-15

## Context

AAA measures consistency by comparing a base case with one or more variants.

A variant differs from the base case in exactly one attribute.

Examples include:

- Region changed
- Customer tenure changed
- Claim value changed
- Supporting documents changed

The framework requires a consistent representation of relationships between base cases, variants, and comparison pairs.

## Decision

A pair consists of:

- One base case
- One variant

The base case represents the original claim.

The variant represents a modified version of the same claim where exactly one field differs.

## Base Case Structure

Base cases contain:

```text
pair_id = None
variant_of = None
varied_field = None