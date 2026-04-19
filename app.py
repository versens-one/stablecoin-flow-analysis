import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('stablecoin_data.csv')
df['amount_usd'] = df['amount_usd'].astype(float)
df['block_time'] = pd.to_datetime(df['block_time'])

st.title('💵 Stablecoin Flow Intelligence')
st.markdown('Analysis of large stablecoin transfers on Ethereum — last 30 days')

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Transactions', f"{len(df):,}")
col2.metric('Total Volume', f"${df['amount_usd'].sum()/1e9:.1f}B")
col3.metric('Avg Transfer', f"${df['amount_usd'].mean()/1e6:.0f}M")
col4.metric('Unique Senders', f"{df['sender'].nunique():,}")

st.subheader('Filters')
col1, col2 = st.columns(2)
selected_symbol = col1.multiselect('Stablecoin', df['symbol'].unique(), default=list(df['symbol'].unique()))
min_amount = col2.slider('Min transfer size ($M)', 0, 1000, 100)

df_filtered = df[
    (df['symbol'].isin(selected_symbol)) &
    (df['amount_usd'] >= min_amount * 1e6)
]

st.subheader('Volume by Stablecoin')
symbol_vol = df_filtered.groupby('symbol')['amount_usd'].sum() / 1e9
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(symbol_vol.index, symbol_vol.values, color=['#00BFFF', '#FF6B6B', '#98FB98', '#FFD700'])
ax.set_ylabel('Volume ($B)')
plt.tight_layout()
st.pyplot(fig)

st.subheader('Top 10 Senders')
top_senders = df_filtered.groupby('sender')['amount_usd'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh([s[:12]+'...' for s in top_senders.index], top_senders.values/1e9, color='steelblue')
ax2.set_xlabel('Volume ($B)')
plt.tight_layout()
st.pyplot(fig2)

st.subheader('Daily Volume Trend')
daily = df_filtered.groupby([df_filtered['block_time'].dt.date, 'symbol'])['amount_usd'].sum().unstack(fill_value=0) / 1e9
fig3, ax3 = plt.subplots(figsize=(12, 4))
daily.plot(ax=ax3)
ax3.set_ylabel('Volume ($B)')
plt.tight_layout()
st.pyplot(fig3)

st.subheader('Market Concentration')
wallet_volume = df_filtered.groupby('sender')['amount_usd'].sum()
total_volume = wallet_volume.sum()
market_shares = wallet_volume / total_volume
hhi = (market_shares ** 2).sum()

sorted_vals = np.sort(wallet_volume.values)
n = len(sorted_vals)
gini_val = (2 * np.sum(np.arange(1, n+1) * sorted_vals) / (n * sorted_vals.sum())) - (n + 1) / n

top5 = market_shares.nlargest(5).sum()

col1, col2, col3 = st.columns(3)
col1.metric('HHI', f"{hhi:.4f}")
col2.metric('Gini Coefficient', f"{gini_val:.4f}")
col3.metric('Top 5 Wallets Share', f"{top5*100:.1f}%")
