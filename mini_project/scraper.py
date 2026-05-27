"""Fetch recent tweets for an X (Twitter) user via the official X API (Tweepy)."""

from __future__ import annotations

import os
from typing import Any

import tweepy
from dotenv import load_dotenv
from tweepy.errors import TweepyException

load_dotenv()

PLACEHOLDER_VALUES = {
    "",
    "your_bearer_token_here",
    "your_api_key_here",
    "your_api_secret_here",
    "your_access_token_here",
    "your_access_token_secret_here",
}

TWEET_FIELDS = [
    "created_at",
    "public_metrics",
    "non_public_metrics",
    "organic_metrics",
    "attachments",
]
MEDIA_FIELDS = ["type"]
EXPANSIONS = ["attachments.media_keys"]


def _env(name: str) -> str | None:
    value = os.getenv(name)
    if not value or value.strip() in PLACEHOLDER_VALUES:
        return None
    return value.strip()


def _get_client() -> tweepy.Client:
    bearer_token = _env("TWITTER_BEARER_TOKEN")
    api_key = _env("TWITTER_API_KEY")
    api_secret = _env("TWITTER_API_SECRET")
    access_token = _env("TWITTER_ACCESS_TOKEN")
    access_token_secret = _env("TWITTER_ACCESS_TOKEN_SECRET")

    oauth_complete = all([api_key, api_secret, access_token, access_token_secret])

    if not bearer_token and not oauth_complete:
        raise ValueError(
            "X API credentials are missing. Set TWITTER_BEARER_TOKEN and/or "
            "TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, and "
            "TWITTER_ACCESS_TOKEN_SECRET in your .env file. "
            "See https://docs.tweepy.org/en/stable/authentication.html"
        )

    return tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True,
    )


def _normalize_handle(username: str) -> str:
    handle = username.strip()
    if handle.startswith("@"):
        handle = handle[1:]
    if not handle:
        raise ValueError("Username cannot be empty.")
    return handle


def _media_lookup(includes: dict[str, Any] | None) -> dict[str, str]:
    if not includes:
        return {}
    lookup: dict[str, str] = {}
    for item in includes.get("media") or []:
        media_key = getattr(item, "media_key", None) or (
            item.get("media_key") if isinstance(item, dict) else None
        )
        media_type = getattr(item, "type", None) or (
            item.get("type") if isinstance(item, dict) else None
        )
        if media_key and media_type:
            lookup[str(media_key)] = str(media_type)
    return lookup


def _extract_media_type(tweet: Any, media_by_key: dict[str, str]) -> str | None:
    attachments = getattr(tweet, "attachments", None)
    if not attachments:
        return None

    media_keys = getattr(attachments, "media_keys", None) or []
    types = {media_by_key[key] for key in media_keys if key in media_by_key}
    if types:
        return ", ".join(sorted(types))
    return "media" if media_keys else None


def _extract_views(tweet: Any) -> int:
    public = getattr(tweet, "public_metrics", None) or {}
    if hasattr(public, "get"):
        views = public.get("impression_count")
        if views is not None:
            return int(views)

    for attr in ("non_public_metrics", "organic_metrics"):
        block = getattr(tweet, attr, None)
        if block and hasattr(block, "get"):
            views = block.get("impression_count")
            if views is not None:
                return int(views)

    return 0


def _map_tweet(tweet: Any, media_by_key: dict[str, str]) -> dict[str, Any] | None:
    text = (getattr(tweet, "text", None) or "").strip()
    if not text:
        return None

    public = getattr(tweet, "public_metrics", None) or {}
    created_at = getattr(tweet, "created_at", None)

    return {
        "tweet_text": text,
        "created_at": created_at.isoformat() if created_at else "",
        "likes": int(public.get("like_count", 0)),
        "retweets": int(public.get("retweet_count", 0)),
        "replies": int(public.get("reply_count", 0)),
        "views": _extract_views(tweet),
        "media_type": _extract_media_type(tweet, media_by_key),
    }


def get_recent_tweets(username: str, limit: int = 50) -> list[dict[str, Any]]:
    """
    Fetch recent tweets for the given X username using Tweepy (X API v2).

    Returns a list of dicts with keys:
    tweet_text, created_at, likes, retweets, replies, views, media_type.

    Requires credentials from https://developer.x.com — see .env template.
    OAuth 1.0a user context is recommended for impression (view) counts.
    """
    handle = _normalize_handle(username)
    max_items = max(1, min(int(limit), 3200))

    try:
        client = _get_client()

        user_response = client.get_user(
            username=handle,
            user_fields=["public_metrics"],
        )
        if not user_response.data:
            raise RuntimeError(f"User @{handle} was not found.")

        user_id = user_response.data.id
        per_request = min(100, max_items)

        tweets: list[dict[str, Any]] = []
        paginator = tweepy.Paginator(
            client.get_users_tweets,
            id=user_id,
            max_results=per_request,
            tweet_fields=TWEET_FIELDS,
            expansions=EXPANSIONS,
            media_fields=MEDIA_FIELDS,
        )

        for page in paginator:
            media_by_key = _media_lookup(
                page.includes if hasattr(page, "includes") else None
            )
            for tweet in page.data or []:
                mapped = _map_tweet(tweet, media_by_key)
                if mapped:
                    tweets.append(mapped)
                if len(tweets) >= max_items:
                    break
            if len(tweets) >= max_items:
                break

        if not tweets:
            raise RuntimeError(
                f"No tweets returned for @{handle}. The account may be private, "
                "have no posts, or your API access tier may not include timelines."
            )

        return tweets[:max_items]

    except ValueError:
        raise
    except TweepyException as exc:
        raise RuntimeError(
            f"X API error while fetching tweets for @{handle}: {exc}"
        ) from exc
    except Exception as exc:
        raise RuntimeError(
            f"Failed to fetch tweets for @{handle}: {exc}"
        ) from exc
