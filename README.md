# Stablecoin Flow Intelligence

## Overview
End-to-end analytics system for analyzing large stablecoin transfers on Ethereum.
Identifies institutional flow patterns, market concentration, and anomalies in $798B+ of on-chain activity.

## Live App
[Open Streamlit App](https://stablecoin-flow-analysis-mzabq8hjfpk5dupizme28g.streamlit.app/)

## Tableau Dashboard
[Open Tableau Dashboard](https://public.tableau.com/app/profile/anna.versens/viz/StablecoinFlowDashboard/Dashboard1?publish=yes)


## Business Context
Large stablecoin transfers (≥$100,000) are primarily driven by institutional players —
hedge funds, market makers, and DeFi protocols moving liquidity between platforms.
Understanding these flows provides early signals of market activity and liquidity shifts.

## Key Findings

### 1. Market is dominated by a handful of wallets
- Top 5 wallets control **72.4% of total volume**
- Gini coefficient = **0.8998** — more unequal than the world's most unequal economies
- 120 unique senders moved $798B in 30 days — average $6.6B per wallet

### 2. USDC is the institutional stablecoin of choice
- USDC accounts for **91% of all transactions** and the majority of volume
- USDT follows at $40B — used for large single transfers
- DAI shows only 207 transactions but $61B volume — very large average transfer size
- PYUSD (PayPal) is emerging with 9 transactions — early institutional adoption signal

### 3. Market concentration is moderate but volume is highly skewed
- HHI = **0.1869** — moderate concentration by traditional financial standards
- However Gini tells a different story — volume distribution is extremely unequal
- This means many wallets participate but a few dominate the actual flow

### 4. Anomaly detection revealed 88 suspicious transfers
- Z-score threshold of 3 identified **88 anomalous transfers**
- Largest anomaly: **$1B USDT transfer** with Z-score of 12.6
- All top anomalies are in USDT — suggesting USDT is used for the largest single moves

### 5. Transfers follow traditional market hours
- Peak activity aligns with **NYSE opening hours (16:00 UTC)**
- Low activity during Asian night hours
- This confirms institutional rather than retail behavior

### 6. Strong correlation between volume and transaction count
- Pearson correlation = **0.9576** (p-value = 0.0000)
- High activity days see both more transactions AND larger sizes simultaneously
- Classic institutional behavior — coordinated liquidity movements

### 7. Weekly cyclicality detected
- Autocorrelation lag 7 days = **-0.32**
- Active weeks tend to be followed by quieter weeks
- Suggests institutional rebalancing cycles rather than continuous activity

## Conclusion
The Ethereum stablecoin market is controlled by a small number of institutional players
moving billions of dollars in coordinated patterns. Monitoring these wallets and their
activity cycles can provide actionable signals for market participants.

## Statistical Methods
- HHI — market concentration index
- Gini Coefficient — distribution inequality
- Z-score anomaly detection
- Pearson correlation analysis
- Autocorrelation (lag 1d and 7d)
- T-test for segment comparison (t=37.89, p=0.000000)
- 99th percentile segmentation

## Tools
Python, Pandas, NumPy, SciPy, Streamlit, Tableau, Dune Analytics API, SQL

## Data
5,000 stablecoin transfers ≥ $100,000 on Ethereum — last 30 days
Source: Dune Analytics (on-chain data)
