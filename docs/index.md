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

## Custom Project - Module 3

### Dataset
I worked with two datasets for this project.

The first dataset was our provided dataset and it contained system performance metrics with columns for requests, errors, and total latency. Each row represented one observation.

The second dataset was a real world website traffic dataset. The original file contained raw event level records, so I aggregated the data by date to create daily traffic metrics. Because the full dataset was too large to commit to the repo, I used a sample version of the file for the project.

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

### Experiments
For the system metrics project, I added new derived signals and flag columns. I adjusted thresholds so that the output would more clearly identify rows with higher error behavior or performance concerns.

For the website traffic project, I applied the same process to a different kind of dataset. Since the traffic data was event level, I first grouped it by date to create daily metrics. Then I added ratio signals, flags, and a composite score to make the daily traffic patterns easier to understand.

### Results
The system metrics signals made it easier to identify observations with relatively high error rates or latency instead of relying only on raw counts.

The website traffic signals showed how daily activity could be summarized into more meaningful indicators such as traffic levels, geographic reach, and link diversity.

Because I used a sample version of the dataset, the overall values for clicks and countries were lower than the full dataset. This affected how some of the signals behaved. For example, the flags such as `traffic_flag` and `reach_flag` were triggered more often due to the thresholds, while the `traffic_level` stayed pretty much the same.

This difference highlighted how signal thresholds can significantly impact the interpretation of results depending on the scale of the data.

### Interpretation
This project demonstrated how signal design can be applied to real world data, even when the structure differs. By aggregating raw event level data into daily metrics, I was able to create meaningful signals that describe system behavior.

The project also showed that different types of signals provide different levels of insight. Binary flags are useful for quick identification of potential issues, while multi-level classifications and composite scores provide more nuanced interpretations.

Additionally, working with a sample dataset emphasized the importance of choosing appropriate thresholds. Signals must be calibrated to the scale of the data to produce meaningful and accurate insights.

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
