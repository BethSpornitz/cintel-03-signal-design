# Continuous Intelligence - Module 3

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

---

## Custom Project - Module 3

### Dataset
I worked with two datasets for this project.  The first dataset was our required dataset and the second dataset was just for fun.

The first dataset was our provided system_metrics dataset and it contained system performance metrics with columns for requests, errors, and total latency. Each row represented one observation.

The second dataset was a real world website traffic dataset. The original file contained raw event level records, so I aggregated the data by date to create daily traffic metrics. Because the full dataset was too large to commit to the repo, I used a sample version of the file for the project.

---

### Signals
For the system metrics dataset, I created and used these signals:
- `error_rate`
- `avg_latency_ms`
- `throughput`
- `error_flag`
- `performance_flag`

For the website traffic dataset, I created and used these signals:
- `clicks`
- `unique_countries`
- `unique_cities`
- `unique_links`
- `link_diversity_ratio`
- `traffic_flag`
- `reach_flag`
- `traffic_attention_flag`
- `traffic_score`
- `traffic_level`

These signals were useful because they turned raw values into indicators that were easier to interpret and compare.

---

### What the Signals Mean

For the system metrics dataset, each added signal helps describe system behavior in a more practical way.

- `error_rate` shows the proportion of requests that failed. In real terms, this helps show how often the system is having problems, rather than only showing the raw number of errors.
- `avg_latency_ms` shows the average response time per request. This matters because a system with slow response times may create a poor user experience even if it is still functioning.
- `throughput` represents the amount of request activity being handled. In practice, this helps show workload volume.
- `error_flag` is a simple label that identifies when error rates exceed a defined threshold.
  For example, if the error rate rises above 2%, the row may be labeled as `high_error`.
  This allows someone monitoring the system to quickly spot problem periods without needing to manually calculate or review error rates for each observation.
- `performance_flag` combines multiple conditions, such as high error rate or high latency, into a single signal.
  For example, even if the error rate is low, very high latency could still trigger a `needs_attention` label.
  In real-world monitoring, this is important because performance issues are often caused by more than one factor. This signal helps highlight situations where the system may not be failing outright but is still performing poorly.

For the website traffic dataset, the added signals help translate raw event data into daily patterns that are easier to understand.

- `clicks` represents total daily traffic activity. This gives a basic picture of how busy the site was on a given day.
- `unique_countries` and `unique_cities` show how geographically broad the traffic was. This helps describe reach, not just volume.
- `unique_links` shows how many different links were involved in the day’s traffic, which gives some sense of content variety or user interest spread.
- `link_diversity_ratio` compares unique links to total clicks. In practical terms, this helps show whether traffic was concentrated on a few links or spread across many.
- `traffic_flag` marks days with especially high traffic volume, which can help identify spikes in attention.
- `reach_flag` marks days with broader international reach, which may suggest wider audience engagement.
- `traffic_attention_flag` combines volume and reach into one quick signal for days that may deserve review.
  For example, if a day has unusually high clicks or traffic coming from many countries, this flag will mark it as `needs_attention`.
  In a real-world scenario, this could help an analyst quickly identify a viral event, a successful campaign, or even suspicious traffic patterns without having to manually review every metric.
- `traffic_score` provides a simple combined measure of traffic and geographic reach.
  For example, a day with both high click volume and a large number of countries would produce a higher score than a day with only high clicks.  This helps summarize multiple aspects of performance into a single number that can be tracked over time or compared across days.
- `traffic_level` groups days into broader categories such as normal, high, or very high traffic, which makes patterns easier to communicate to others.
  For example, instead of reporting exact click counts, you could say “traffic was very high on this day,” which is easier for non-technical stakeholders to understand.
  This is especially useful for reporting trends or summarizing performance in dashboards or presentations.

#### Real World Example:  A company like Best Buy could use these signals to monitor activity on their website.
If a new product launch or promotion drives a spike in clicks, the `traffic_flag` and `traffic_level` would quickly highlight that increase in activity. At the same time, `unique_countries` and `reach_flag` could show whether the promotion is reaching a broader international audience.

---

### Experiments
For the system metrics project, I added new derived signals and flag columns. I adjusted thresholds so that the output would more clearly identify rows with higher error behavior or performance concerns.

For the website traffic project, I applied the same process to a different kind of dataset. Since the traffic data was event level, I first grouped it by date to create daily metrics. Then I added ratio signals, flags, and a composite score to make the daily traffic patterns easier to understand.

---

### Results
The system metrics signals made it easier to identify observations with relatively high error rates or latency instead of relying only on raw counts.

The website traffic signals showed how daily activity could be summarized into more meaningful indicators such as traffic levels, geographic reach, and link diversity.

Because I used a sample version of the dataset, the overall values for clicks and countries were lower than the full dataset. This affected how some of the signals behaved. For example, the flags such as `traffic_flag` and `reach_flag` were triggered more often due to the thresholds, while the `traffic_level` stayed pretty much the same.

This difference highlighted how signal thresholds can significantly impact the interpretation of results depending on the scale of the data.

---

### Interpretation
This project demonstrated how signal design can be applied to real world data, even when the structure differs. By aggregating raw event level data into daily metrics, I was able to create meaningful signals that describe system behavior.

The project also showed that different types of signals provide different levels of insight. Binary flags are useful for quick identification of potential issues, while multi-level classifications and composite scores provide more nuanced interpretations.

Additionally, working with a sample dataset emphasized the importance of choosing appropriate thresholds. Signals must be calibrated to the scale of the data to produce meaningful and accurate insights.

---

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
