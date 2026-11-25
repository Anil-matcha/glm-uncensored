# Pricing

The figures below are Muapi catalog rates per million tokens, checked on 2026-11-25. Input and output rates can differ. These values are a dated snapshot; verify the live Muapi page before budgeting.

| Model | Input / 1M | Output / 1M | Context | Input type |
|---|---:|---:|---:|---|
| <code>glm-5-3-flash-abliterated</code> | $0.40 | $1.60 | 1M | Text + image |
| <code>glm-5-3-abliterated</code> | $2.50 | $4.50 | 1M | Text |
| <code>glm-4-6-derestricted-v5</code> | $0.80 | $3.00 | 131K | Text |

## Estimate a request

A rough estimate is:

```text
estimated cost = (input tokens × input rate + output tokens × output rate) ÷ 1,000,000
```

Actual charges depend on usage and Muapi's current billing rules. Check the response usage or cost fields and your Muapi dashboard for account totals.

## Price changes

Model availability, context limits, fields, and rates can change. Verify the live [Muapi model page](https://muapi.ai/glm-abliterated-api) or the [Muapi catalog](https://muapi.ai/models).
