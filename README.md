# GLM Abliterated API with Muapi

Call Muapi's hosted GLM abliterated and derestricted variants with a stable REST interface. This guide provides the model IDs, a cURL quick start, and a Python example for async submission and polling.

## Related Projects

- [Muapi Uncensored AI API guide](https://github.com/Anil-matcha/Uncensored-AI-API) — broader API setup and examples for Muapi's abliterated LLM endpoints.
- [Awesome Abliterated LLMs](https://github.com/Anil-matcha/awesome-abliterated-llms) — model comparison and evaluation notes.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — a creative AI workspace connected to Muapi.

## Muapi GLM routes

| Model | Muapi endpoint |
|---|---|
| GLM 5.3 Flash Abliterated | **glm-5-3-flash-abliterated** |
| GLM 5.3 Abliterated | **glm-5-3-abliterated** |
| GLM 4.6 Derestricted v5 | **glm-4-6-derestricted-v5** |

The word “uncensored” in this repository name is a search label, not a guarantee about every route or response. These routes are described by Muapi as abliterated or derestricted variants; behavior can vary. Evaluate the exact model and follow Muapi's terms.

## Quick start

Create a key at [Muapi API Keys](https://muapi.ai/access-keys), then set it in your shell:

~~~bash
export MUAPI_KEY="your-muapi-key"
~~~

Submit a prompt to GLM 5.3 Flash Abliterated:

~~~bash
curl -X POST https://api.muapi.ai/api/v1/glm-5-3-flash-abliterated \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explain how to design a reliable background job system."}'
~~~

Poll the returned request:

~~~bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: $MUAPI_KEY"
~~~

The other variants use the endpoint IDs in the table. Check the [GLM Abliterated API page](https://muapi.ai/glm-abliterated-api) for current model details, request fields, availability, and pricing.

## Python example

Requires Python 3.9+ and **requests**.

~~~bash
python -m pip install -r requirements.txt
python examples/submit.py "Explain how to review a pull request."
python examples/submit.py --model glm-5-3-abliterated "Outline a migration from REST to event-driven processing."
~~~

## Links

- [GLM Abliterated API on Muapi](https://muapi.ai/glm-abliterated-api)
- [Muapi API reference](https://muapi.ai/docs/api-reference)
- [Create or manage an API key](https://muapi.ai/access-keys)
- [Muapi](https://muapi.ai)

Model availability, request fields, and pricing can change. Confirm them on the live Muapi page.
