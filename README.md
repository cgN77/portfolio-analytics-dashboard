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
- Interactive pie charts and visualizations
- Excel-based classification system
- Downloadable classification data
- Summary statistics

## Classification System

The dashboard uses a predefined classification system stored in `classified_dataset.xlsx`. Assets are classified according to:

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

The following dependencies are required:

- streamlit>=1.31.0
- pandas>=2.2.0
- plotly>=5.18.0
- numpy>=1.26.0
- openpyxl>=3.1.2 (for Excel file handling)

## Usage

1. Launch the application using `streamlit run app.py`
2. Navigate to the Portfolio Classification tab
3. Add assets and their allocations using the input form
4. View the generated charts and analysis
5. Download classification data as needed

### Classification Data

The system uses a predefined Excel file (`classified_dataset.xlsx`) to maintain consistent asset classifications. This ensures:

- Standardized categorization across the application
- Consistent liquidity assessments
- Reliable public/private market classification
- Clear distinction between traditional and alternative assets

## Contributing

Feel free to submit issues and enhancement requests!
