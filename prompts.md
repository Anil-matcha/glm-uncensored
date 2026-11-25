# Prompt templates for GLM models

Starting templates only; they are not tested outputs or benchmark prompts. Replace bracketed text and use only fields supported by the chosen route.

## Long context

```text
From the supplied notes, return a timeline, main decisions, and three unresolved questions: [notes].
```

## Structured analysis

```text
Analyze this proposal using the headings Goal, Assumptions, Risks, Alternatives, Recommendation: [proposal].
```

## Vision

```text
Inspect the image for layout issues. Report visible evidence and rank the three most important issues: [image].
```

## Image prompts

For a route that accepts image_url, provide the image as a separate request field and refer to it in prompt. Do not assume a text-only route can fetch or inspect an image URL.
