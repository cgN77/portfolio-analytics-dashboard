# Portfolio Analytics Dashboard

A comprehensive portfolio analytics dashboard built with Streamlit that provides detailed analysis and classification of investment portfolios.

## Features

### 1. Portfolio Analysis

- Performance metrics and analytics
- Risk assessment
- Return analysis
- Benchmark comparisons

### 2. Individual Asset Metrics

- Detailed analysis of individual assets
- Performance tracking
- Risk metrics

### 3. Portfolio Classification

- Asset classification based on:
  - Traditional vs Alternative assets
  - Public vs Private markets
  - Liquidity levels
- Interactive pie charts
- Downloadable classification data
- Summary statistics

## Asset Classifications

The dashboard uses the following classification system:

| Asset Type             | Category    | Access  | Liquidity         |
| ---------------------- | ----------- | ------- | ----------------- |
| US Stock ETF           | Traditional | Public  | Highly Liquid     |
| Corporate Bond Fund    | Traditional | Public  | Highly Liquid     |
| Treasury Bond ETF      | Traditional | Public  | Highly Liquid     |
| Cryptocurrency         | Alternative | Public  | Highly Liquid     |
| Real Estate Investment | Alternative | Private | Moderately Liquid |
| Hedge Fund             | Alternative | Private | Moderately Liquid |
| Private Equity Fund    | Alternative | Private | Illiquid          |
| Venture Capital Fund   | Alternative | Private | Illiquid          |
| Art Collection         | Alternative | Private | Illiquid          |
| Infrastructure Fund    | Alternative | Private | Illiquid          |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/cgn77/portfolio-analytics-dashboard.git
cd portfolio-analytics-dashboard
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Requirements

Create a requirements.txt file with the following dependencies:

- streamlit
- pandas
- plotly
- numpy

## Usage

1. Launch the application using `streamlit run app.py`
2. Navigate to the Portfolio Classification tab
3. Add assets and their allocations using the input form
4. View the generated charts and analysis
5. Download classification data as needed

## Contributing

Feel free to submit issues and enhancement requests!
