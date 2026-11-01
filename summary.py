# %%
import csv
def read_rows(mywards):
    with open(mywards, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values
def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }
# %%
#rows = read_rows("mywards.csv")
#values = clean_values(rows, "area_km2")
#result = summarise(values)
#print(result)
# %%
def  summarise_all(mywards, columns):
    rows = read_rows(mywards)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report
report = summarise_all("mywards.csv", ["area_km2", "population_2006"])
for column, stats in report.items():
    print(column, "->", stats)