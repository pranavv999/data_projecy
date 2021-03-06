import csv
import matplotlib.pyplot as plt

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
    """Return the population data for India for year 2004 to 2014"""
    data = []
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row["Region"] == "India" and row["Year"] in over_years:
                value = int(float(row["Population"]))
                data.append(value)

    return data


def graph_plot():
    # Data
    values = extract_data("population-estimates.csv")
    # width for each coloumn is different
    width = [0.45, 0.45, 0.45, 0.45, 0.5, 0.55, 0.57, 0.59, 0.61, 0.63, 0.65]
    fig, ax = plt.subplots()
    plt.bar(
        over_years,
        values,
        width,
        color="orange",
        edgecolor="blue",
        zorder=2,
        )
    # Add Title and x-axis tick, set frame dimensions etc.
    plt.grid(axis="y")
    plt.xlabel(
        "Year",
        {"size": 20, "color": "k"},
        labelpad=10,
        alpha=0.5,
        )
    plt.ylabel(
        "Population 1 x 10^6",
        {"size": 20, "color": "k"},
        labelpad=10,
        alpha=0.5,
    )
    plt.title(
        "Indian population from year 2004 to 2014",
        {"size": 20, "color": "b"},
    )
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=12)
    ax.spines["top"].set_linewidth(1.7)
    ax.spines["right"].set_linewidth(1.7)
    ax.spines["bottom"].set_linewidth(1.7)
    ax.spines["left"].set_linewidth(1.7)
    return plt.show()


if __name__ == "__main__":
    graph_plot()
