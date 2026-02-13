import pandas as pd

def analyze():
    df = pd.read_csv("output/shadow_tankers.csv")

    print(f"📊 Total vessels: {len(df)}\n")

    print("🚩 Top flags:")
    print(df["flag"].value_counts().head(10), "\n")

    print("🛢️ Vessel types:")
    print(df["vessel_type"].value_counts().head(10), "\n")

    print("📜 Sanction programs:")
    print(df["programs"].value_counts().head(10))

if __name__ == "__main__":
    analyze()
