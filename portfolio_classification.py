import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Tuple

def extract_asset_classifications(file_path, sheet_name="Sheet1"):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    asset_classifications = {
        row["Asset"]: (row["Traditional/Alternative"], row["Public/Private"], row["Liquidity"])
        for _, row in df.iterrows()
    }
    
    return asset_classifications

file_path = "classified_dataset.xlsx" 
ASSET_CLASSIFICATIONS = extract_asset_classifications(file_path)

def classify_asset(asset_name: str) -> Tuple[str, str, str]:
    """
    Classify an asset based on the predefined classifications.
    Returns (traditional/alternative, public/private, liquidity level)
    """
    if asset_name in ASSET_CLASSIFICATIONS:
        return ASSET_CLASSIFICATIONS[asset_name]
    return ('Alternative', 'Private', 'Illiquid')

def create_classification_charts(assets: Dict[str, float]):
    """Create classification charts based on asset data"""
    # Prepare data
    df = pd.DataFrame([
        {
            'Asset': name,
            'Allocation': value,
            'Type': classify_asset(name)[0],
            'Access': classify_asset(name)[1],
            'Liquidity': classify_asset(name)[2]
        }
        for name, value in assets.items()
    ])
    fig_type = px.pie(
        df, 
        values='Allocation', 
        names='Type',
        title='Portfolio Distribution: Traditional vs Alternative',
        color_discrete_map={'Traditional': 'rgb(102, 197, 204)', 'Alternative': 'rgb(248, 156, 116)'}
    )
    
    fig_access = px.pie(
        df, 
        values='Allocation', 
        names='Access',
        title='Portfolio Distribution: Public vs Private',
        color_discrete_map={'Public': 'rgb(102, 197, 204)', 'Private': 'rgb(248, 156, 116)'}
    )
    
    fig_liquidity = px.pie(
        df, 
        values='Allocation', 
        names='Liquidity',
        title='Portfolio Distribution by Liquidity',
        color_discrete_map={
            'Highly Liquid': 'rgb(102, 197, 204)',
            'Moderately Liquid': 'rgb(248, 156, 116)',
            'Illiquid': 'rgb(220, 176, 242)'
        }
    )

    summary_df = pd.DataFrame([
        df.groupby('Type')['Allocation'].sum(),
        df.groupby('Access')['Allocation'].sum(),
        df.groupby('Liquidity')['Allocation'].sum()
    ], index=['By Type', 'By Access', 'By Liquidity'])

    return fig_type, fig_access, fig_liquidity, summary_df, df

def main():
    st.title("Portfolio Classification Analysis")
    
    st.write("""
    This tool helps you analyze your portfolio composition based on:
    - Traditional vs Alternative assets
    - Public vs Private markets
    - Liquidity levels
    
    Enter your assets and their allocations below.
    """)

    if 'assets' not in st.session_state:
        st.session_state.assets = {}

    with st.form("asset_input_form"):
        col1, col2 = st.columns(2)
        with col1:
            asset_name = st.selectbox(
                "Asset Name",
                options=list(ASSET_CLASSIFICATIONS.keys()),
                help="Select an asset from the predefined list"
            )
        with col2:
            allocation = st.number_input("Allocation (%)", min_value=0.0, max_value=100.0, value=0.0)
        
        submitted = st.form_submit_button("Add Asset")
        if submitted and asset_name and allocation:
            st.session_state.assets[asset_name] = allocation

    if st.session_state.assets:
        st.subheader("Current Portfolio")
        portfolio_df = pd.DataFrame([
            {"Asset": k, "Allocation (%)": v} 
            for k, v in st.session_state.assets.items()
        ])
        st.dataframe(portfolio_df)

        asset_to_remove = st.selectbox(
            "Select asset to remove",
            ["None"] + list(st.session_state.assets.keys())
        )
        if asset_to_remove != "None" and st.button("Remove Selected Asset"):
            del st.session_state.assets[asset_to_remove]
            st.experimental_rerun()

        total_allocation = sum(st.session_state.assets.values())
        if abs(total_allocation - 100) > 0.01:  # Allow for small floating-point differences
            st.warning(f"Total allocation ({total_allocation}%) does not equal 100%")
        
        fig_type, fig_access, fig_liquidity, summary_df, classification_df = create_classification_charts(st.session_state.assets)

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_type, use_container_width=True)
            st.plotly_chart(fig_liquidity, use_container_width=True)
        with col2:
            st.plotly_chart(fig_access, use_container_width=True)

        st.subheader("Portfolio Classification Summary (%)")
        st.dataframe(summary_df)

        st.subheader("Detailed Asset Classification")
        st.dataframe(classification_df)

        csv = classification_df.to_csv(index=False)
        st.download_button(
            label="Download Portfolio Classification Data",
            data=csv,
            file_name="portfolio_classification.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main() 