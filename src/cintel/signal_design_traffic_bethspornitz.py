"""
signal_design_traffic_bethspornitz.py - Website traffic signal design project.

Author: Beth Spornitz
Date: 2026-03

Website Traffic Data

- Data is taken from a website traffic event dataset.
- The data is structured and static for this example.
- Each row represents one website event.
- The CSV file includes columns such as:
  - event
  - date
  - country
  - city
  - artist
  - album
  - track
  - isrc
  - linkid

Purpose

- Read website traffic events from a CSV file.
- Aggregate the raw events into daily traffic signals.
- Create useful derived signals from the aggregated metrics.
- Save the resulting signals as a new CSV artifact.
- Log the pipeline process to assist with debugging and transparency.

Paths (relative to repo root)

    INPUT FILE: data/traffic_sample.csv
    OUTPUT FILE: artifacts/traffic_signals_bethspornitz.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.signal_design_traffic_bethspornitz

OBS:
  This file is my custom signal design project using a real-world dataset.
  I transformed raw website events into daily traffic signals that are easier
  to monitor and interpret.
"""

import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

LOG: logging.Logger = get_logger("P3", level="DEBUG")

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "traffic_sample_bethspornitz.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "traffic_signals_bethspornitz.csv"


def main() -> None:
    """Run the pipeline."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ THE RAW WEBSITE TRAFFIC DATA
    # ----------------------------------------------------
    df: pl.DataFrame = pl.read_csv(DATA_FILE)

    LOG.info(f"Loaded {df.height} website traffic event records")

    # ----------------------------------------------------
    # STEP 2: AGGREGATE RAW EVENTS INTO DAILY METRICS
    # ----------------------------------------------------
    # We convert event-level data into daily monitoring signals.
    # This makes the data easier to interpret and compare over time.
    daily_df: pl.DataFrame = (
        df.group_by("date")
        .agg(
            [
                pl.len().alias("clicks"),
                pl.col("country").n_unique().alias("unique_countries"),
                pl.col("city").n_unique().alias("unique_cities"),
                pl.col("linkid").n_unique().alias("unique_links"),
            ]
        )
        .sort("date")
    )

    LOG.info(f"Created aggregated daily table with {daily_df.height} rows")

    # ----------------------------------------------------
    # STEP 3: DESIGN SIGNALS FROM THE DAILY METRICS
    # ----------------------------------------------------
    LOG.info("Designing signals from daily website traffic metrics...")

    # Thresholds chosen from the observed daily activity levels.
    HIGH_TRAFFIC_THRESHOLD: Final[int] = 33000
    GLOBAL_REACH_THRESHOLD: Final[int] = 175

    LOG.info(f"HIGH_TRAFFIC_THRESHOLD: {HIGH_TRAFFIC_THRESHOLD}")
    LOG.info(f"GLOBAL_REACH_THRESHOLD: {GLOBAL_REACH_THRESHOLD}")

    # Share of links relative to total clicks.
    # This provides a simple ratio-based signal.
    link_diversity_signal_recipe: pl.Expr = (
        pl.col("unique_links") / pl.col("clicks")
    ).alias("link_diversity_ratio")

    # Flag days with especially high click volume.
    traffic_flag_signal_recipe: pl.Expr = (
        pl.when(pl.col("clicks") > HIGH_TRAFFIC_THRESHOLD)
        .then(pl.lit("high_traffic"))
        .otherwise(pl.lit("normal"))
        .alias("traffic_flag")
    )

    # Flag days with broad international reach.
    global_reach_flag_signal_recipe: pl.Expr = (
        pl.when(pl.col("unique_countries") > GLOBAL_REACH_THRESHOLD)
        .then(pl.lit("global_reach"))
        .otherwise(pl.lit("normal"))
        .alias("reach_flag")
    )

    # Combine multiple conditions into one higher-level monitoring signal.
    performance_flag_signal_recipe: pl.Expr = (
        pl.when(
            (pl.col("clicks") > HIGH_TRAFFIC_THRESHOLD)
            | (pl.col("unique_countries") > GLOBAL_REACH_THRESHOLD)
        )
        .then(pl.lit("needs_attention"))
        .otherwise(pl.lit("normal"))
        .alias("traffic_attention_flag")
    )

    # ----------------------------------------------------
    # STEP 3.1: DEFINE A TRAFFIC SCORE SIGNAL RECIPE
    # ----------------------------------------------------
    # This combines click volume and country reach into
    # one simple composite signal.
    traffic_score_signal_recipe: pl.Expr = (
        (pl.col("clicks") / 10000) + (pl.col("unique_countries") / 100)
    ).alias("traffic_score")

    # ----------------------------------------------------
    # STEP 3.2: DEFINE A TRAFFIC LEVEL SIGNAL RECIPE
    # ----------------------------------------------------
    # This classifies daily traffic into levels instead
    # of just using a binary high/normal flag.
    traffic_level_signal_recipe: pl.Expr = (
        pl.when(pl.col("clicks") > 34000)
        .then(pl.lit("very_high"))
        .when(pl.col("clicks") > 30000)
        .then(pl.lit("high"))
        .otherwise(pl.lit("normal"))
        .alias("traffic_level")
    )

    signals_df: pl.DataFrame = daily_df.with_columns(
        [
            link_diversity_signal_recipe,
            traffic_flag_signal_recipe,
            global_reach_flag_signal_recipe,
            performance_flag_signal_recipe,
            traffic_score_signal_recipe,
            traffic_level_signal_recipe,
        ]
    )

    LOG.info(
        "Created signal columns: link_diversity_ratio, traffic_flag, reach_flag, traffic_attention_flag, traffic_score, traffic_level"
    )

    # ----------------------------------------------------
    # STEP 4: SELECT THE COLUMNS WE WANT TO SAVE
    # ----------------------------------------------------
    output_df: pl.DataFrame = signals_df.select(
        [
            "date",
            "clicks",
            "unique_countries",
            "unique_cities",
            "unique_links",
            "link_diversity_ratio",
            "traffic_flag",
            "reach_flag",
            "traffic_attention_flag",
            "traffic_score",
            "traffic_level",
        ]
    )

    LOG.info(f"Enhanced traffic signals table has {output_df.height} rows")

    # ----------------------------------------------------
    # STEP 5: SAVE THE SIGNALS TABLE AS AN ARTIFACT
    # ----------------------------------------------------
    output_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote signals file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


if __name__ == "__main__":
    main()
