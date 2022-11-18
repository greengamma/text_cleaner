---
date: 17. September 2022 #2022-09-17
description: "Data driven long/short trading"
featured_image: "/images/HedgeInvest.png"
title: "Project 1: HedgeInvest"
---
17. September 2022:

* An app predicting the most promising long/short pairs (ratios) based on “mean average percentage error” (MAPE).
* Extracts S&P 500 Friday closing prices.
* Creates >250,000 ratios (pairs of stocks).
* Selects the ratios with a positive trend in the last 6 weeks.
* Builds and fits the models on the selected data.
* Models used: ARIMA/SARIMA, FB Prophet, LSTM, CNN
* Compares model accuracy based on (MAPE).
* Data upload.

&nbsp;


  ► Tools used: ![image alt >](/images/python.png) ![image alt <](/images/pandas.png) ![image alt <](/images/streamlit.png)
  ![image alt <](/images/numpy2.png) ![image alt <](/images/vscode.png) ![image alt <](/images/jupyter.png) ![image alt <](/images/keras2.png)

{{< figure src="/images/HedgeInvest.png" >}}

[▸ Link to GitHub repository](https://github.com/greengamma/long-short-trade-ideas-generator) \
[▸ Link to presentation on YouTube](https://www.youtube.com/watch?v=dOFYbkQLTVQ&t=19s)
