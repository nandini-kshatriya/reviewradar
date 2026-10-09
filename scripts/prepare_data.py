"""Build ReviewRadar's real-data bundle from public Play Store reviews.

Source: github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence (data/*.csv),
itself derived from Kaggle 'saloni1712/zomato-and-swiggy-play-store-reviews'. No license is stated
upstream; the bundle is used for a non-commercial portfolio demo with attribution and is not
redistributed beyond what the demo needs. No reviewer names or images exist in these files.

Usage: python3 prepare_data.py zomato.csv swiggy.csv ../data/zomato_swiggy_2023.json
"""
import sys, json, pandas as pd

WEEKS = 26          # most recent N weeks, Monday-aligned
MAXLEN = 400        # keep payload small; 96%+ of reviews are shorter

def main(paths, out):
    d = pd.concat([pd.read_csv(p) for p in paths], ignore_index=True)
    d["t"] = pd.to_datetime(d["review_date"], errors="coerce")
    d = d.dropna(subset=["t", "review_description", "rating"])
    end = d["t"].max().normalize()
    # keep complete Monday-Sunday weeks only, so a partial final week cannot fake a drop
    end_sunday = end if end.weekday() == 6 else end - pd.Timedelta(days=end.weekday() + 1)
    start = end_sunday - pd.Timedelta(days=7 * WEEKS - 1)
    d = d[(d["t"] >= start) & (d["t"] < end_sunday + pd.Timedelta(days=1))].sort_values("t")
    rows = []
    for r in d.itertuples():
        ver = r.appVersion if isinstance(r.appVersion, str) else ""
        rows.append([r.App, r.t.strftime("%Y-%m-%d"), int(r.rating),
                     str(r.review_description)[:MAXLEN], ver,
                     int(r.thumbsUpCount) if pd.notna(r.thumbsUpCount) else 0])
    meta = {
        "name": "Zomato vs Swiggy · Google Play reviews",
        "source": "Public Play Store reviews, compiled in github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence (from Kaggle saloni1712/zomato-and-swiggy-play-store-reviews)",
        "start": start.strftime("%Y-%m-%d"), "weeks": WEEKS, "rows": len(rows),
        "caveats": [
            "Collection method upstream is not documented; English-language scrape likely (Hindi script appears in under 0.1% of reviews).",
            "Swiggy file is 64% one-star across its full range vs 43% for Zomato, which suggests different sampling, so compare complaint rates within rating bands where possible.",
            "Reviews are a self-selected, negatively skewed sample of users, not a population estimate."],
        "cols": ["app", "date", "rating", "text", "version", "thumbs"],
    }
    json.dump({"meta": meta, "rows": rows}, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
    print(out, len(rows), start.date(), "to", end_sunday.date())

if __name__ == "__main__":
    main(sys.argv[1:-1], sys.argv[-1])
