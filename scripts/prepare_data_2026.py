"""Build ReviewRadar's 2026 real-data bundle from public Play Store reviews.

Source: github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews (commit 019dae4, files data/raw/swiggy.csv.gz
and data/raw/zomato.csv.gz). The authors collected every English review posted in India between 1 April and
20 September 2026 with the google-play-scraper package (Sort.NEWEST, lang=en, country=in). Their DATA_SOURCES.md
documents the method and known gaps. No license is stated upstream, so the bundle is used for a non-commercial
portfolio demo with attribution. The files contain no reviewer names or images.

Usage: python3 prepare_data_2026.py swiggy.csv.gz zomato.csv.gz ../data/zomato_swiggy_2026.json
"""
import sys, json, pandas as pd

MAXLEN = 400  # keeps the payload small, and almost every review is shorter

def main(paths, out):
    d = pd.concat([pd.read_csv(p) for p in paths], ignore_index=True)
    raw_n = len(d)
    d["t"] = pd.to_datetime(d["review_date"], errors="coerce")
    d = d.dropna(subset=["t", "score"])
    dropped = {"no date or rating": raw_n - len(d)}
    # a few source reviews contain U+FFFD replacement characters from broken encoding upstream, so drop them
    d["content"] = d["content"].fillna("").astype(str).str.replace("\ufffd", "", regex=False).str.strip()
    n = len(d); d = d[d["content"].str.len() > 0]; dropped["empty text"] = n - len(d)
    n = len(d); d = d.drop_duplicates("review_id"); dropped["duplicate review id"] = n - len(d)
    n = len(d)
    # complete Monday to Sunday weeks only, so a partial first or last week cannot fake a change
    first = d["t"].min().normalize()
    start = first + pd.Timedelta(days=(7 - first.weekday()) % 7)
    end = d["t"].max().normalize()
    end_sunday = end if end.weekday() == 6 else end - pd.Timedelta(days=end.weekday() + 1)
    d = d[(d["t"] >= start) & (d["t"] < end_sunday + pd.Timedelta(days=1))].sort_values("t")
    dropped["outside complete weeks"] = n - len(d)
    weeks = int(((end_sunday - start).days + 1) // 7)
    last_partial = start - pd.Timedelta(days=1)
    partial = f"{first.day} {first:%b} to {last_partial.day} {last_partial:%b %Y}" if start > first else ""
    # upstream flags 21 Apr to 5 May 2026 as a Play Store feed gap where positive reviews went missing
    gap0, gap1 = pd.Timestamp("2026-04-21"), pd.Timestamp("2026-05-05")
    gap_weeks = sorted({int((t - start).days // 7) for t in pd.date_range(gap0, gap1)})
    # compact rows: app index, day offset from start, rating, text, version index, upvotes
    apps = sorted(d["app_name"].unique())
    vers = sorted({v for v in d["app_version"].dropna().astype(str)})
    vi = {v: i + 1 for i, v in enumerate(vers)}
    rows = [[apps.index(r.app_name), int((r.t.normalize() - start).days), int(r.score), r.content[:MAXLEN],
             vi.get(r.app_version, 0) if isinstance(r.app_version, str) else 0,
             int(r.thumbs_up) if pd.notna(r.thumbs_up) else 0] for r in d.itertuples()]
    counts = d.groupby("app_name").size().to_dict()
    meta = {
        "name": "Zomato vs Swiggy · Google Play reviews, Apr to Sep 2026",
        "source": "github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews (data/raw, commit 019dae4)",
        "method": "google-play-scraper, every English review from India posted 1 Apr to 20 Sep 2026, sorted newest first",
        "start": start.strftime("%Y-%m-%d"), "end": end_sunday.strftime("%Y-%m-%d"), "weeks": weeks,
        "rows": len(rows), "raw_rows": raw_n, "dropped": dropped, "partial_week": partial, "per_app": counts, "gap_weeks": gap_weeks,
        "caveats": [
            f"{dropped['outside complete weeks']:,} raw reviews from {partial} are left out because they fall in a partial week. Every week in the app runs Monday to Sunday." if partial else "No partial weeks were dropped.",
            "Two thirds of reviews are three words or fewer, so topic tags cover a minority of reviews.",
            "Upstream reports a Play Store feed gap from 21 Apr to 5 May 2026 in which positive reviews dropped sharply for Swiggy. Those weeks are shaded in charts and left out of spike baselines, release checks and the metrics that compare windows or apps.",
            "Written reviews are harsher than the public store rating, which also counts ratings without text.",
            "Zomato has no reviews for 24 Jul 2026 in the source.",
            "Reviews were requested in English, so feedback written in Devanagari is missing. Hinglish in Latin script still appears."],
        "format": "compact", "apps": apps, "versions": [""] + vers,
        "cols": ["app index", "days since start", "rating", "text", "version index", "thumbs"],
    }
    json.dump({"meta": meta, "rows": rows}, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(out, len(rows), counts, start.date(), "to", end_sunday.date(), "weeks", weeks, "gap", gap_weeks, "dropped", dropped)

if __name__ == "__main__":
    main(sys.argv[1:-1], sys.argv[-1])
