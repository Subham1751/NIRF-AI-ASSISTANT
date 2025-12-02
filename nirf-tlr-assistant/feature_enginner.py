import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:

    return pd.read_excel(path)


def compute_nt_features(df: pd.DataFrame) -> pd.DataFrame:
    
    ug4_cols = ["UG4_2023-24", "UG4_2022-23", "UG4_2021-22", "UG4_2020-21", "UG4_2019-20", "UG4_2018-19"]
    df["NT_UG4_total"] = df[ug4_cols].sum(axis=1)

    ug5_cols = ["UG5_2023-24", "UG5_2022-23", "UG5_2021-22", "UG5_2020-21", "UG5_2019-20", "UG5_2018-19"]
    df["NT_UG5_total"] = df[ug5_cols].sum(axis=1)

    pg2_cols = ["PG2_2023-24", "PG2_2022-23", "PG2_2021-22", "PG2_2020-21", "PG2_2019-20", "PG2_2018-19"]
    df["NT_PG2_total"] = df[pg2_cols].sum(axis=1)
    
    pg3_cols = ["PG3_2023-24", "PG3_2022-23", "PG3_2021-22", "PG3_2020-21", "PG3_2019-20", "PG3_2018-19"]
    df["NT_PG3_total"] = df[pg3_cols].sum(axis=1)
    
    pg_integrated_cols = ["PG_INTEGRATED_2023-24", "PG_INTEGRATED_2022-23", "PG_INTEGRATED_2021-22",
                          "PG_INTEGRATED_2020-21", "PG_INTEGRATED_2019-20", "PG_INTEGRATED_2018-19"]
    df["NT_PG_INTEGRATED_total"] = df[pg_integrated_cols].sum(axis=1)

    df["NT_total"] = df["NT_UG4_total"] + df["NT_UG5_total"] + df["NT_PG2_total"] + df["NT_PG3_total"] + df["NT_PG_INTEGRATED_total"]

    return df


def compute_ne_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df["NE_total"] = (
        df["NE_UG4_Total"] +
        df["NE_UG5_Total"] +
        df["NE_PG2_Total"] +
        df["NE_PG3_Total"] +
        df["NE_PG_INTEGRATED_Total"]
    )

    df["Occupancy"] = df["NE_total"] / df["NT_total"]

    df["Female_total"] = (
        df["NE_UG4_Female"] + df["NE_UG5_Female"] + df["NE_PG2_Female"] + df["NE_PG3_Female"] + df["NE_PG_INTEGRATED_Female"]
    )

    df["OutsideState_total"] = (
        df["NE_UG4_OutsideState"] +
        df["NE_UG5_OutsideState"] +
        df["NE_PG2_OutsideState"] +
        df["NE_PG3_OutsideState"] +
        df["NE_PG_INTEGRATED_OutsideState"]
    )

    df["OutsideCountry_total"] = (
        df["NE_UG4_OutsideCountry"] +
        df["NE_UG5_OutsideCountry"] +
        df["NE_PG2_OutsideCountry"] +
        df["NE_PG3_OutsideCountry"] +
        df["NE_PG_INTEGRATED_OutsideCountry"]
    )

    df["EWS_total"] = (
        df["NE_UG4_EconomicallyBackward"] +
        df["NE_UG5_EconomicallyBackward"] +
        df["NE_PG2_EconomicallyBackward"] +
        df["NE_PG3_EconomicallyBackward"] +
        df["NE_PG_INTEGRATED_EconomicallyBackward"]
    )

    df["SCSTOBC_total"] = (
        df["NE_UG4_SociallyChallenged"] +
        df["NE_UG5_SociallyChallenged"] +
        df["NE_PG2_SociallyChallenged"] +
        df["NE_PG3_SociallyChallenged"] +
        df["NE_PG_INTEGRATED_SociallyChallenged"]
    )

    df["FeeReimb_total"] = (
        df["NE_UG4_FeeReimb_State"] +
        df["NE_UG4_FeeReimb_Institute"] +
        df["NE_UG4_FeeReimb_Private"] +
        df["NE_UG5_FeeReimb_State"] +
        df["NE_UG5_FeeReimb_Institute"] +
        df["NE_UG5_FeeReimb_Private"] +
        df["NE_PG2_FeeReimb_State"] +
        df["NE_PG2_FeeReimb_Institute"] +
        df["NE_PG2_FeeReimb_Private"] +
        df["NE_PG3_FeeReimb_State"] +
        df["NE_PG3_FeeReimb_Institute"] +
        df["NE_PG3_FeeReimb_Private"] +
        df["NE_PG_INTEGRATED_FeeReimb_State"] +
        df["NE_PG_INTEGRATED_FeeReimb_Institute"] +
        df["NE_PG_INTEGRATED_FeeReimb_Private"]
    )

    df["Female_ratio"] = df["Female_total"] / df["NE_total"]
    df["Outside_state_ratio"] = df["OutsideState_total"] / df["NE_total"]
    df["International_ratio"] = df["OutsideCountry_total"] / df["NE_total"]
    df["EWS_ratio"] = df["EWS_total"] / df["NE_total"]
    df["SCSTOBC_ratio"] = df["SCSTOBC_total"] / df["NE_total"]
    df["FeeReimb_ratio"] = df["FeeReimb_total"] / df["NE_total"]

    return df


def compute_phd_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df["NP_total"] = df["PhD_Grad_FT_2023-24"] + df["PhD_Grad_PT_2023-24"]
    return df

def engineer_features(input_path: str, output_path: str):

    df = load_raw_data(input_path)

    df = compute_nt_features(df)
    df = compute_ne_features(df)
    df = compute_phd_features(df)

    df.to_csv(output_path, index=False)
    print(f"Feature-engineered dataset saved to: {output_path}")

if __name__ == "__main__":
    engineer_features(
        input_path="data/MasterData.xlsx",
        output_path="data/nirf_feature_engineered.csv"
    )