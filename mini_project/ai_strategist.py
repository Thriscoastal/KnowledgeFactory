"""Generate a data-driven X content strategy using an LLM."""

from __future__ import annotations

import json
import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SYSTEM_PROMPT = """You are an expert X (Twitter) growth strategist for creators and brands.

Your job is to analyze quantitative engagement metrics and produce a concise,
actionable content strategy. Rules:
- Base every recommendation strictly on the metrics provided—no generic advice.
- Reference specific numbers from the data when making a point.
- Output exactly three numbered steps (1., 2., 3.), each 2–4 sentences.
- Focus on content format, posting patterns, and engagement tactics implied by the data.
- Do not invent metrics or tweets that are not in the input.
- Do not use markdown headings; use plain numbered steps only."""


def _get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key.strip() in {"", "your_openai_api_key_here"}:
        raise ValueError(
            "OPENAI_API_KEY is missing or still a placeholder. "
            "Set it in your .env file."
        )
    return OpenAI(api_key=api_key)


def generate_strategy(summary_metrics: dict[str, Any]) -> str:
    """
    Call the LLM with engagement summary metrics and return a 3-step strategy.
    """
    if not summary_metrics:
        raise ValueError("summary_metrics cannot be empty.")

    metrics_json = json.dumps(summary_metrics, indent=2, default=str)
    user_prompt = f"""Analyze these X creator engagement metrics and write a personalized
3-step content strategy. Use only the data below.

METRICS:
{metrics_json}
"""

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    try:
        client = _get_openai_client()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
            max_tokens=800,
        )
    except ValueError:
        raise
    except Exception as exc:
        raise RuntimeError(f"LLM strategy generation failed: {exc}") from exc

    content = response.choices[0].message.content
    if not content or not content.strip():
        raise RuntimeError("LLM returned an empty strategy response.")

    return content.strip()
