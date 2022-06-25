from tabula import read_pdf
import pandas as pd
import matplotlib.pyplot as plt


def read_from_pdf():
    dfs = read_pdf("MVP01-6_Cars_by_make.pdf", pages="all")
    df = pd.concat(dfs)  # concat all pages
    df.reset_index(drop=True, inplace=True)  # reset index
    df = df[:-1]  # remove the last row
    df.to_csv("cars.csv")  # save to csv
    return


def main():
    df = pd.read_csv("cars.csv", index_col=0)
    df.sort_values(by="2021", inplace=True, ascending=False)
    df = df[df["Make"] != "TOTAL"]
    df = df[df["2021"] != 0]
    df = df[df["2021"].notna()]
    df.reset_index(drop=True, inplace=True)
    df.to_csv("cars_sorted.csv")
    return


def luxury_car_graph():
    LUXURY_MAEKS = [
        # "MERCEDES BENZ",
        # "B.M.W.",
        # "AUDI",
        "PORSCHE",
        # "LAND ROVER",
        "MASERATI",
        # "TESLA",
        "BENTLEY",
        "FERRARI",
        "ROLLS ROYCE",
        "LAMBORGHINI",
        "ASTON MARTIN",
        "Mclaren",
    ]

    df = pd.read_csv("cars_sorted.csv", index_col=0)
    df = df[df["Make"].isin(LUXURY_MAEKS)]
    df.sort_values(by="2021", inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)

    x = [str(x) for x in range(2011, 2022)]
    # plot line chart
    fig, ax = plt.subplots(figsize=(12, 9))
    for row in df.itertuples():
        ax.plot(x, row[2:], label=row[1])
    ax.set_xlabel("End of Year")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Luxury Cars in Singapore by Make")
    ax.legend()
    plt.savefig("luxury_cars_line.png")

    # plot bar chart
    fig, ax = plt.subplots(figsize=(12, 9))
    for row in df.itertuples():
        ax.bar(x, row[2:], 0.35, label=row[1])
    ax.set_xlabel("End of Year")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Luxury Cars in Singapore by Make")
    ax.legend()
    plt.savefig("luxury_cars_bar.png")
    return


MAKES = [
    "TOYOTA",
    "HONDA",
    "MERCEDES BENZ",
    "B.M.W.",
    "MAZDA",
    "HYUNDAI",
    "NISSAN",
    "KIA",
    "VOLKSWAGEN",
    "AUDI",
    "MITSUBISHI",
    "SUBARU",
    "VOLVO",
    "PORSCHE",
    "MINI",
    "LAND ROVER",
    "FORD",
    "INFINITI",
    "MASERATI",
    "TESLA",
    "BENTLEY",
    "FERRARI",
    "ROLLS ROYCE",
    "LAMBORGHINI",
    "ASTON MARTIN",
    "Mclaren",
]


def yearly_increase():
    df = pd.read_csv("cars_sorted.csv", index_col=0)
    # df = df[df["Make"].isin(MAKES)]
    df["2021"] = df["2021"] - df["2020"]
    df["2020"] = df["2020"] - df["2019"]
    df["2019"] = df["2019"] - df["2018"]
    df["2018"] = df["2018"] - df["2017"]
    df["2017"] = df["2017"] - df["2016"]
    df["2016"] = df["2016"] - df["2015"]
    df["2015"] = df["2015"] - df["2014"]
    df["2014"] = df["2014"] - df["2013"]
    df["2013"] = df["2013"] - df["2012"]
    df["2012"] = df["2012"] - df["2011"]
    df.drop(columns=["2011"], inplace=True)
    df.sort_values(by="2021", inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.to_csv("cars_yearly_delta.csv")


if __name__ == "__main__":
    main()
    yearly_increase()
