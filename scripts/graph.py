import requests
import statistics
import matplotlib.pyplot as plt
import queryTracker

endpoint = "https://codeforces.com/api/problemset.problems"

def getData():
    data = requests.get(endpoint).json()
    queryTracker.snapshot(data)
    data = data["result"]["problems"]

    ratings = [p['rating'] for p in data if "rating" in p]

    print(f"Total problems: {len(data)}")
    print(f"Total rated problems: {len(ratings)}")
    print(f"Percentage of problems accounted for: {round(100*len(ratings)/len(data), 2)}%")
    print(f"Median difficulty: {statistics.median(ratings)}")
    print(f"Mean difficulty: {round(statistics.mean(ratings), 2)}")
    return ratings

def graph(ratings):
    difficulties = range(800, 3501, 100)

    problems = [
        sum(rating >= difficulty for rating in ratings)
        for difficulty in difficulties
    ]

    p25 = statistics.quantiles(ratings, n=4)[0]
    p50 = statistics.median(ratings)
    p75 = statistics.quantiles(ratings, n=4)[2]

    percentiles = [
        ("25th percentile", p25, "#2196F3"),
        ("50th percentile", p50, "#FF9800"),
        ("75th percentile", p75, "#F44336"),
    ]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(
        difficulties,
        problems,
        marker="o",
        linewidth=2,
        color="black"
    )

    for label, percentile, color in percentiles:
        count = sum(rating >= percentile for rating in ratings)

        ax.vlines(
            percentile,
            0,
            count,
            color=color,
            linewidth=2
        )

        ax.hlines(
            count,
            0,
            percentile,
            color=color,
            linewidth=2
        )

        ax.scatter(
            percentile,
            count,
            color=color,
            s=80,
            zorder=5
        )

        ax.annotate(
            f"{label}\n{percentile:.0f} rating\n{count:,} problems",
            xy=(percentile, count),
            xytext=(10, 10),
            textcoords="offset points",
            color=color,
            fontsize=10,
            fontweight="bold"
        )

    ax.set_xlabel("Difficulty rating")
    ax.set_ylabel("Number of problems ≥ rating")
    ax.set_title("Codeforces Problem Difficulty Distribution")

    ax.set_xticks(range(800, 3501, 200))
    ax.set_xlim(800, 3500)
    ax.set_ylim(bottom=0)

    ax.grid(alpha=0.25)

    plt.tight_layout()
    queryTracker.snapshotFigure("CF Difficulty Distribution", fig, ax)
    plt.show()

graph(getData())