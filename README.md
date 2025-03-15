# Portfolio Analytics Dashboard

A comprehensive portfolio analytics dashboard built with Streamlit that provides detailed analysis and classification of investment portfolios. The system uses a predefined Excel-based classification system to categorize assets and provide detailed portfolio composition analysis.

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

- Asset classification based on predefined Excel mappings:
  - Traditional vs Alternative assets
  - Public vs Private markets
  - Liquidity levels (Highly Liquid, Moderately Liquid, Illiquid)
- Interactive pie charts for portfolio composition
- Downloadable classification data
- Summary statistics and detailed breakdowns
- Excel-based classification system for easy updates

## Asset Classifications

The dashboard uses the following classification system (defined in `classified_dataset.xlsx`):

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
4. View the generated classification charts and analysis:
   - Traditional vs Alternative breakdown
   - Public vs Private distribution
   - Liquidity analysis
5. Download classification data as needed

## Data Structure

The classification system uses an Excel file (`classified_dataset.xlsx`) with the following structure:

- Asset Name
- Category (Traditional/Alternative)
- Access Type (Public/Private)
- Liquidity Level (Highly Liquid/Moderately Liquid/Illiquid)

## Contributing

Feel free to submit issues and enhancement requests! To contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
