"""Streamlit dashboard for the X Creator Insights Engine."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from ai_strategist import generate_strategy
from processor import ENGAGEMENT_COLUMN, process_tweet_data
from scraper import get_recent_tweets

st.set_page_config(
    page_title="X Creator Insights Engine",
    page_icon="📊",
    layout="wide",
)

st.title("X Creator Insights Engine")
st.caption(
    "Pull recent posts via the X API (Tweepy), compute True Engagement Rate, "
    "and get an AI-powered content plan."
)

DEFAULT_LIMIT = 50

with st.sidebar:
    st.header("Settings")
    tweet_limit = st.slider(
        "Tweets to analyze",
        min_value=10,
        max_value=100,
        value=DEFAULT_LIMIT,
        step=10,
        help="Number of recent tweets to fetch from the X API (paginated, up to 100 per request).",
    )
    st.markdown("---")
    st.markdown(
        "**True Engagement Rate**  \n"
        "`((Likes + Retweets + Replies) / Views) × 100`"
    )

username = st.text_input(
    "X handle",
    placeholder="e.g. elonmusk or @elonmusk",
    help="Enter the profile handle without needing the full URL.",
)

analyze = st.button("Analyze", type="primary", use_container_width=True)

if analyze:
    if not username or not username.strip():
        st.warning("Please enter an X handle to analyze.")
    else:
        handle_display = username.strip().lstrip("@")
        with st.spinner("Pulling data and generating insights..."):
            try:
                raw_tweets = get_recent_tweets(username, limit=tweet_limit)
                df, summary = process_tweet_data(raw_tweets)
                strategy = generate_strategy(summary)
            except Exception as exc:
                st.error(str(exc))
                st.stop()

        st.success(f"Analysis complete for @{handle_display} ({summary['tweet_count']} tweets)")

        col1, col2, col3 = st.columns(3)
        col1.metric(
            "Avg True Engagement",
            f"{summary['average_true_engagement_rate']:.2f}%",
        )
        col2.metric(
            "Total Views",
            f"{summary['total_views']:,}",
        )
        col3.metric(
            "Tweets Analyzed",
            summary["tweet_count"],
        )

        st.subheader("True Engagement Rate Over Time")
        chart_df = df.set_index("created_at")[[ENGAGEMENT_COLUMN]].sort_index()
        chart_df.columns = ["True Engagement Rate (%)"]
        st.line_chart(chart_df)

        with st.expander("Top performing tweets", expanded=False):
            for i, tweet in enumerate(summary["top_performing_tweets"], start=1):
                st.markdown(
                    f"**#{i}** — {tweet['true_engagement_rate']:.2f}% TER · "
                    f"{tweet['views']:,} views · {tweet.get('media_type') or 'text'}"
                )
                st.write(tweet["tweet_text"])

        st.subheader("Your 3-step content strategy")
        st.markdown(
            f"""
<div style="
    border-left: 4px solid #1d9bf0;
    background: rgba(29, 155, 240, 0.08);
    padding: 1.25rem 1.5rem;
    border-radius: 0.5rem;
    margin-top: 0.5rem;
">

{strategy}

</div>
""",
            unsafe_allow_html=True,
        )

        with st.expander("Raw metrics sent to the strategist"):
            st.json(summary)

else:
    st.info("Enter a handle and click **Analyze** to start.")
