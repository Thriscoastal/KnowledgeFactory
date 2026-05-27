"""Transform raw tweet records into engagement metrics and summaries."""

from __future__ import annotations

from typing import Any

import pandas as pd

NUMERIC_COLUMNS = ("likes", "retweets", "replies", "views")
ENGAGEMENT_COLUMN = "true_engagement_rate"


def _to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").fillna(0).astype(float)


def _parse_created_at(series: pd.Series) -> pd.Series:
    parsed = pd.to_datetime(series, errors="coerce", utc=True)
    if parsed.isna().all():
        parsed = pd.to_datetime(series, format="%a %b %d %H:%M:%S %z %Y", errors="coerce", utc=True)
    return parsed


def _tweet_preview(text: str, max_len: int = 120) -> str:
    cleaned = " ".join(str(text).split())
    if len(cleaned) <= max_len:
        return cleaned
    return cleaned[: max_len - 3] + "..."


def process_tweet_data(
    raw_data: list[dict[str, Any]],
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """
    Clean tweet data, compute True Engagement Rate, and build a summary.

    True Engagement Rate = ((Likes + Retweets + Replies) / Views) * 100

    Returns:
        (cleaned DataFrame for charts, summary dict for the LLM)
    """
    if not raw_data:
        raise ValueError("No tweet data to process.")

    df = pd.DataFrame(raw_data).copy()

    rename_map = {
        "tweet_text": "tweet_text",
        "text": "tweet_text",
        "created_at": "created_at",
        "likes": "likes",
        "retweets": "retweets",
        "replies": "replies",
        "views": "views",
        "media_type": "media_type",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    required = {"tweet_text", "created_at", "likes", "retweets", "replies", "views"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Raw data is missing required fields: {sorted(missing)}")

    for col in NUMERIC_COLUMNS:
        df[col] = _to_numeric(df[col])

    df["created_at"] = _parse_created_at(df["created_at"])
    df = df.dropna(subset=["created_at"])
    df = df[df["views"] > 0].copy()

    if df.empty:
        raise ValueError(
            "No tweets with view counts greater than zero. "
            "Cannot compute engagement rates."
        )

    interactions = df["likes"] + df["retweets"] + df["replies"]
    df[ENGAGEMENT_COLUMN] = (interactions / df["views"]) * 100.0
    df = df.sort_values("created_at").reset_index(drop=True)

    avg_rate = float(df[ENGAGEMENT_COLUMN].mean())
    total_views = int(df["views"].sum())

    top_df = df.nlargest(3, ENGAGEMENT_COLUMN)
    top_tweets: list[dict[str, Any]] = []
    for _, row in top_df.iterrows():
        top_tweets.append(
            {
                "tweet_text": _tweet_preview(row["tweet_text"]),
                "created_at": row["created_at"].isoformat(),
                "true_engagement_rate": round(float(row[ENGAGEMENT_COLUMN]), 4),
                "likes": int(row["likes"]),
                "retweets": int(row["retweets"]),
                "replies": int(row["replies"]),
                "views": int(row["views"]),
                "media_type": row.get("media_type"),
            }
        )

    media_breakdown: dict[str, int] = {}
    if "media_type" in df.columns:
        filled = df["media_type"].fillna("none")
        media_breakdown = filled.value_counts().to_dict()

    summary: dict[str, Any] = {
        "tweet_count": int(len(df)),
        "average_true_engagement_rate": round(avg_rate, 4),
        "total_views": total_views,
        "top_performing_tweets": top_tweets,
        "median_likes": round(float(df["likes"].median()), 2),
        "median_views": int(df["views"].median()),
        "media_type_breakdown": media_breakdown,
    }

    return df, summary
