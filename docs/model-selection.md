# Choosing a GLM route

This guide compares three hosted GLM routes. GLM 5.3 Flash accepts optional image input; the full-size GLM 5.3 and GLM 4.6 Derestricted v5 schemas are text-only.

## Compare the current routes

| Route | Context | Input | Input / output per 1M tokens | Maximum output | Selection note |
|---|---:|---|---:|---:|---|
| <code>glm-5-3-flash-abliterated</code> | 1M | Text + image | $0.40 / $1.60 | 32768 | Choose for a lower-priced GLM 5.3 option when image input is needed. |
| <code>glm-5-3-abliterated</code> | 1M | Text | $2.50 / $4.50 | 32768 | Choose when you want the full-size GLM 5.3 route and text input is sufficient. |
| <code>glm-4-6-derestricted-v5</code> | 131K | Text | $0.80 / $3.00 | 32768 | Choose when the GLM 4.6 v5 route fits your task and its smaller context is sufficient. |

The table is a shortlist by documented interface, context, and price. It is not a quality ranking.

## A practical selection process

1. Start with input type. Use image_url only on a route whose Muapi schema lists image input.
2. Match the advertised context window to the total prompt size and leave room for the generated answer.
3. Set max_tokens to the output length your task needs; the cap varies by endpoint.
4. Estimate cost from expected input and output token counts using the separate rates.
5. For close choices, run the same prompts on each route and score them against your own criteria. This repository publishes no comparative benchmark scores.

## Model cards

- [GLM 5.3 Flash Abliterated](models/glm-5-3-flash-abliterated.md) — Choose for a lower-priced GLM 5.3 option when image input is needed.
- [GLM 5.3 Abliterated](models/glm-5-3-abliterated.md) — Choose when you want the full-size GLM 5.3 route and text input is sufficient.
- [GLM 4.6 Derestricted v5](models/glm-4-6-derestricted-v5.md) — Choose when the GLM 4.6 v5 route fits your task and its smaller context is sufficient.

Check the [Muapi live page](https://muapi.ai/glm-abliterated-api) for current availability and pricing.
