# Stablecoin Flow Intelligence

## Overview
End-to-end analytics system for analyzing large stablecoin transfers on Ethereum.
Identifies institutional flow patterns, market concentration, and anomalies.

## Live App
🚀 [Open Streamlit App](https://stablecoin-flow-analysis-mzabq8hjfpk5dupizme28g.streamlit.app/)

## Tableau Dashboard
📊 [Open Tableau Dashboard](https://public.tableau.com/app/profile/anna.versens/viz/StablecoinFlowDashboard/Dashboard1?publish=yes)

## Key Findings
- Total volume analyzed: $798B over 30 days
- USDC dominates with 91% of transactions
- HHI = 0.1869 — moderate market concentration
- Gini = 0.8998 — extreme inequality in transfer distribution
- Top 5 wallets control 72.4% of total volume
- 88 anomalous transfers detected via Z-score analysis

## Statistical Methods
- HHI (Herfindahl-Hirschman Index) — market concentration
- Gini Coefficient — distribution inequality
- Z-score anomaly detection
- Pearson correlation (r=0.9576, p=0.0000)
- Autocorrelation analysis (lag 1d and 7d)
- T-test — segment comparison

## Tools
Python, Pandas, NumPy, SciPy, Streamlit, Tableau, Dune Analytics API

## Data
5,000 stablecoin transfers ≥ $100,000 on Ethereum — last 30 days
Source: Dune Analytics
