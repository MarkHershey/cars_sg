from tabula import read_pdf
import pandas as pd


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
    df.to_csv("cars2.csv")
    return


if __name__ == "__main__":
    main()
