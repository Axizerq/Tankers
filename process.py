import pandas as pd

def analyze():
    df = pd.read_csv("output/shadow_tankers.csv")

    print(f"📊 Total sanctioned vessels: {len(df)}\n")

    # --- Ключевые слова, связанные с РФ ---
    russia_keywords = [
        "russia",
        "russian federation",
        "moscow",
        "rosneft",
        "sovcomflot",
        "scf",
        "gazprom",
        "paо",
        "pao"
    ]

    def contains_keywords(text):
        if pd.isna(text):
            return False
        text = text.lower()
        return any(keyword in text for keyword in russia_keywords)

    russia_mask = (
        df["remarks"].apply(contains_keywords)
        | df["vessel_owner"].apply(contains_keywords)
    )

    russian_vessels = df[russia_mask]

    print(f"🇷🇺 Russian-linked vessels found: {len(russian_vessels)}\n")

    if len(russian_vessels) > 0:
        print("🛢️ Russian vessel types:")
        print(russian_vessels["vessel_type"].value_counts().head(10), "\n")

    russian_vessels.to_csv(
        "output/russian_shadow_tankers.csv",
        index=False
    )

    print("✅ Saved output/russian_shadow_tankers.csv")

if __name__ == "__main__":
    analyze()

