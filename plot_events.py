import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/road_category_summary.csv")

road_names = {
    "A01": "Milan–Rome",
    "A14": "Bologna–Taranto",
    "A12": "Genova–Rosignano",
    "A22": "Modena–Brennero",
    "A11": "Florence–Pisa",
    "A04": "Turin–Trieste",
    "A23": "Palmanova–Udine",
    "A10": "Genova–Ventimiglia",
    "A07": "Milan–Genova",
    "A08": "Varese Connection",
    # ADD THESE
    "TR1": "Mont Blanc Tunnel",
    "A27": "Venice–Belluno",
    "A26": "Genova–Gravellona",
}

pivot_df = df.pivot(
    index="road",
    columns="category",
    values="events_count"
).fillna(0)

pivot_df["total"] = pivot_df.sum(axis=1)

pivot_df = (
    pivot_df
    .sort_values("total", ascending=True)
    .tail(10)
)

totals = pivot_df["total"]
pivot_df = pivot_df.drop(columns="total")

pivot_df.index = [
    f"{road} — {road_names.get(road, '')}"
    for road in pivot_df.index
]

ax = pivot_df.plot(
    kind="barh",
    stacked=True,
    figsize=(13, 7)
)

plt.title("Traffic Issues Composition by Road", fontsize=16)
plt.xlabel("Events Count", fontsize=12)
plt.ylabel("Road", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.5)

for i, total in enumerate(totals):
    ax.text(
        total + 0.2,
        i,
        str(int(total)),
        va="center"
    )

plt.legend(title="Category", loc="lower right")
plt.tight_layout()

plt.savefig("charts/stacked_traffic_issues_horizontal.png", dpi=300)
plt.show()

print("Saved: charts/stacked_traffic_issues_horizontal.png")