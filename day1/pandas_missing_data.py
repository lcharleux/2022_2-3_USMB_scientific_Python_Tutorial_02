import pandas as pd

data = pd.read_csv("grades.csv", sep = "\s*,\s*", engine = "python")

# SHOW MISSING DATA
grid = data.groupby(["name", "course"]).mean().unstack()