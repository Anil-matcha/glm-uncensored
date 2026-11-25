# GLM 4.6 Derestricted v5 on Muapi

A text-only GLM 4.6 v5 route with a 131K-token context window.

| Catalog detail | Value |
|---|---|
| Muapi endpoint | <code>glm-4-6-derestricted-v5</code> |
| Context shown in Muapi catalog | 131K tokens |
| Input | Text |
| Input price | $0.80 per million tokens |
| Output price | $3.00 per million tokens |
| Maximum output tokens in current schema | 32768 |

## When to consider this route

Choose when the GLM 4.6 v5 route fits your task and its smaller context is sufficient.

Context is the advertised total input window; max_tokens separately limits generated output. The live Muapi model page is the source of truth if a schema or price changes.

## Request fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| <code>prompt</code> | string | Yes | Prompt text sent to the model. |
| <code>system_prompt</code> | string | No | Optional system-level instruction. |
| <code>max_tokens</code> | integer | No | Optional output cap; route maximum is 32768. |

The input object requires prompt. Other fields listed above are optional in the current schema. Include image_url only when this route lists Text + image.

## Submit and poll

Set MUAPI_KEY, submit to the endpoint, save the returned request ID, then poll the result endpoint:

```bash
curl -X POST https://api.muapi.ai/api/v1/glm-4-6-derestricted-v5 \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Summarize the design trade-offs in this proposal.", "system_prompt": "Be concise and separate facts from assumptions.", "max_tokens": 1024}'

curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: $MUAPI_KEY"
```

The submit response contains a request_id. Poll until the job reaches a terminal status and inspect the returned result payload. Handle failed and cancelled separately from completed.

## Streaming

Muapi provides streaming on supported text-generation endpoints. Use POST /api/v1/glm-4-6-derestricted-v5/stream when the live model page confirms streaming for this route. See the [Muapi streaming guide](https://muapi.ai/docs/streaming) and this repository's [streaming example](../../examples/stream.py).

## Pricing

Muapi's catalog currently lists $0.80/M input tokens and $3.00/M output tokens. Actual charge depends on request usage. Verify the live [Muapi catalog](https://muapi.ai/abliterated-llm-api) before budgeting.

## Links

- [Muapi model page](https://muapi.ai/abliterated-llm-api)
- [Muapi API reference](https://muapi.ai/docs/api-reference)
- [Family selection guide](../model-selection.md)
