import pandas as pd
from typing import Dict

def extract_asset_classifications(file_path, sheet_name="Sheet1"):
    """
    Reads the classification data from Excel and returns a dict
    mapping asset -> classification details.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    asset_classifications = {
        row["Asset"]: {
            "Classification": row["Classification"],
            "Asset Class": row["Asset Class"],
            "Sub-Asset Class": row["Sub-Asset Class"],
            "Liquidity": row["Liquidity"],
            "Instrument/Manager": row["Instrument/Manager"],
        }
        for _, row in df.iterrows()
    }
    return asset_classifications


def create_sunburst_table(assets: Dict[str, float], 
                           total_portfolio_value: float, 
                           asset_classifications: Dict[str, Dict]) -> pd.DataFrame:
    """
    Create a hierarchical portfolio breakdown structured like a sunburst chart.
    """
    data = []
    for asset, alloc_pct in assets.items():
        classification = asset_classifications.get(asset, {})
        data.append({
            "Classification": classification.get("Classification", "Alternative"),
            "Asset Class": classification.get("Asset Class", ""),
            "Sub-Asset Class": classification.get("Sub-Asset Class", ""),
            "Liquidity": classification.get("Liquidity", "Illiquid"),
            "Instrument/Manager": classification.get("Instrument/Manager", asset),
            "Allocation (%)": alloc_pct,
            "Allocation ($)": (alloc_pct / 100.0) * total_portfolio_value,
        })
    
    df = pd.DataFrame(data)
    groups = [
        ["Classification"],
        ["Classification", "Asset Class"],
        ["Classification", "Asset Class", "Sub-Asset Class"],
        ["Classification", "Asset Class", "Sub-Asset Class", "Liquidity"],
        ["Classification", "Asset Class", "Sub-Asset Class", "Liquidity", "Instrument/Manager"],
    ]
    
    hierarchical_data = []
    for level in groups:
        group_df = (
            df.groupby(level)
              .agg({"Allocation (%)": "sum", "Allocation ($)": "sum"})
              .reset_index()
        )
        for _, row in group_df.iterrows():
            hierarchical_data.append(row.to_dict())
    
    hierarchical_df = pd.DataFrame(hierarchical_data)
    hierarchical_df = hierarchical_df[[
        "Classification", "Asset Class", "Sub-Asset Class",
        "Liquidity", "Instrument/Manager", "Allocation (%)", "Allocation ($)"
    ]]
    hierarchical_df = hierarchical_df.sort_values(by=["Classification", "Asset Class", "Sub-Asset Class", "Liquidity"]).reset_index(drop=True)
    hierarchical_df = hierarchical_df.dropna(subset=["Instrument/Manager"])
    
    return hierarchical_df

