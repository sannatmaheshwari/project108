import pandas as p
import plotly.figure_factory as pf

df = p.read_csv("project.csv")
figure = pf.create_distplot([df["Avg Rating"].tolist()],["average"],show_curve=True)
figure.show()