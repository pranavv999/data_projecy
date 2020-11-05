import csv
import matplotlib.pyplot as plt

# Following are the ASEAN countries
asean_countries = [
    "Brunei",
    "Combodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
]
# We are refering data from year 2004 to 2014
over_years = [
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
]


def extract_data(file):
    """Return the population data for ASEAN countries in a Dictionery"""
    data = {
        "Brunei Darussalam": [],
        "Cambodia": [],
        "Indonesia": [],
        "Lao People's Democratic Republic": [],
        "Malaysia": [],
        "Myanmar": [],
        "Philippines": [],
        "Singapore": [],
        "Thailand": [],
        "Viet Nam": [],
    }
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        for row in csv_reader:
            if row["Region"] in data and row["Year"] in over_years:
                value = int(float(row["Population"]))
                data[row["Region"]].append(value)

    return data


def graph_plot():
    # Data
    values = extract_data("population-estimates.csv")
    # width of the bar
    width = 0.37
    # Label Locations
    bar1 = [(i * 4) for i in range(len(over_years))]
    bar2 = [(i + width) for i in bar1]
    bar3 = [(i + width * 2) for i in bar1]
    bar4 = [(i + width * 3) for i in bar1]
    bar5 = [(i + width * 4) for i in bar1]
    bar6 = [(i + width * 5) for i in bar1]
    bar7 = [(i + width * 6) for i in bar1]
    bar8 = [(i + width * 7) for i in bar1]
    bar9 = [(i + width * 8) for i in bar1]
    bar10 = [(i + width * 9) for i in bar1]

    fig, ax = plt.subplots()
    ax.bar(
        bar1,
        values["Brunei Darussalam"],
        width,
        edgecolor="blue",
        label="Brunei",
        zorder=2,
    )
    ax.bar(
        bar2,
        values["Cambodia"],
        width,
        edgecolor="blue",
        label="Combodia",
        zorder=2,
    )
    ax.bar(
        bar3,
        values["Indonesia"],
        width,
        edgecolor="blue",
        label="Indonesia",
        zorder=2,
    )
    ax.bar(
        bar4,
        values["Lao People's Democratic Republic"],
        width,
        edgecolor="blue",
        label="Laos",
        zorder=2,
    )
    ax.bar(
        bar5,
        values["Malaysia"],
        width,
        edgecolor="blue",
        label="Malaysia",
        zorder=2,
    )
    ax.bar(
        bar6,
        values["Myanmar"],
        width,
        edgecolor="blue",
        label="Myanmar",
        zorder=2,
    )
    ax.bar(
        bar7,
        values["Philippines"],
        width,
        edgecolor="blue",
        label="Philippins",
        zorder=2,
    )
    ax.bar(
        bar8,
        values["Singapore"],
        width,
        edgecolor="blue",
        label="Singapore",
        zorder=2,
    )
    ax.bar(
        bar9,
        values["Thailand"],
        width,
        edgecolor="blue",
        label="Thailand",
        zorder=2,
    )
    ax.bar(
        bar10,
        values["Viet Nam"],
        width,
        edgecolor="blue",
        label="Vietnam",
        zorder=2,
    )

    # Add some Labels, Title and x-axis tick
    ax.set_title(
        "Population Growth in ASEAN Countries for years 2004 - 2014",
        {"size": 20, "color": "b"},
    )
    ax.set_ylabel(
        "Population",
        {"size": 20, "color": "k"},
        labelpad=10,
        alpha=0.5,
    )
    ax.spines["top"].set_linewidth(1.7)
    ax.spines["right"].set_linewidth(1.7)
    ax.spines["bottom"].set_linewidth(1.7)
    ax.spines["left"].set_linewidth(1.7)
    ax.grid(axis="y")
    ax.set_xlabel("Years", {"size": 20, "color": "k"}, labelpad=10, alpha=0.5)
    ax.set_xticks(bar5)
    ax.set_xticklabels(over_years)
    ax.legend(shadow=True, loc="upper right", bbox_to_anchor=(1.001, 1.009))
    fig.set_figwidth(8)
    return plt.show()


if __name__ == "__main__":
    graph_plot()
