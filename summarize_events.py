import pandas as pd

# 1. Read raw traffic events
df = pd.read_csv("data/events_raw.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

# 2. Create structured event categories
df["category"] = "other"

df.loc[
    df["t_des_en"].str.contains("queue", case=False, na=False),
    "category"
] = "queue"

df.loc[
    df["t_des_en"].str.contains("roadworks", case=False, na=False),
    "category"
] = "roadworks"

df.loc[
    df["t_des_en"].str.contains("closed", case=False, na=False),
    "category"
] = "closure"

df.loc[
    df["t_des_en"].str.contains("wind|winds", case=False, na=False),
    "category"
] = "weather"

df.loc[
    df["t_des_en"].str.contains(
        "breakdown|equipment|No Water|No Power|out of methane",
        case=False,
        na=False
    ),
    "category"
] = "service disruption"

# 3. Events by road
road_summary = df["c_str"].value_counts().reset_index()
road_summary.columns = ["road", "events_count"]

# 4. Example message for each road
road_messages = (
    df[["c_str", "t_des_en"]]
    .dropna()
    .groupby("c_str")
    .first()
    .reset_index()
)

road_messages.columns = ["road", "example_message"]

road_summary_with_messages = road_summary.merge(
    road_messages,
    on="road",
    how="left"
)

# 5. Category summary
category_summary = df["category"].value_counts().reset_index()
category_summary.columns = ["category", "events_count"]

# 6. Road + category summary
road_category_summary = (
    df.groupby(["c_str", "category"])
    .size()
    .reset_index(name="events_count")
    .sort_values("events_count", ascending=False)
)

road_category_summary.columns = [
    "road",
    "category",
    "events_count"
]

# 7. Main issue by road
main_issue_by_road = (
    road_category_summary
    .sort_values(
        ["road", "events_count"],
        ascending=[True, False]
    )
    .groupby("road")
    .first()
    .reset_index()
    .sort_values("events_count", ascending=False)
)

# 8. Create readable label
main_issue_by_road["label"] = (
    main_issue_by_road["road"]
    + " — "
    + main_issue_by_road["category"]
)

# 9. Raw message type summary
type_summary = df["t_des_en"].value_counts().reset_index()
type_summary.columns = ["event_type", "events_count"]

# 10. Print summaries
print("\nEvents by road:")
print(road_summary.head(20))

print("\nEvents by category:")
print(category_summary)

print("\nRoad + category summary:")
print(road_category_summary.head(20))

print("\nMain issue by road:")
print(main_issue_by_road.head(20))

# 11. Save results
df.to_csv("data/events_enriched.csv", index=False)

road_summary.to_csv(
    "data/events_by_road.csv",
    index=False
)

road_summary_with_messages.to_csv(
    "data/events_by_road_with_messages.csv",
    index=False
)

category_summary.to_csv(
    "data/events_by_category.csv",
    index=False
)

road_category_summary.to_csv(
    "data/road_category_summary.csv",
    index=False
)

main_issue_by_road.to_csv(
    "data/main_issue_by_road.csv",
    index=False
)

type_summary.to_csv(
    "data/events_by_type.csv",
    index=False
)

print("\nSaved:")
print("data/events_enriched.csv")
print("data/events_by_road.csv")
print("data/events_by_road_with_messages.csv")
print("data/events_by_category.csv")
print("data/road_category_summary.csv")
print("data/main_issue_by_road.csv")
print("data/events_by_type.csv")
