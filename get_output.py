import json
import os

import pandas as pd


def get_json(x, product_data):
    b = []
    if "json_data" not in os.listdir():
        os.mkdir("json_data")
    r = [b.append(i) for i in product_data if i not in b]
    with open(
        f"json_data/amazon-data-{''.join([x + '-' for x in x.split()[:-1]] + x.split()[-1:])}.json",
        "w",
    ) as f:
        json.dump(b, f, indent=4)


def get_csv(x, product_data):
    if "csv_data" not in os.listdir():
        os.mkdir("csv_data")
    df = pd.DataFrame([d for d in product_data])
    df.drop_duplicates(subset="PRODUCT_NAME", inplace=True)
    df.to_csv(
        f"csv_data/amazon-data-{''.join([x + '-' for x in x.split()[:-1]] + x.split()[-1:])}.csv",
        index=False,
    )


def get_html(soup):
    if "last_page" not in os.listdir():
        os.mkdir("last_page")
    with open(f"last_page/amazon_last.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
