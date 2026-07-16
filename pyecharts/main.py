import pyecharts.options as opts
from pyecharts.charts import Line 
from pyecharts.options import TitleOpts, LegendOpts

line = Line()

line.add_xaxis(["China", "America", "Britain"])

line.add_yaxis("GDP", [30, 20, 10])

line.set_global_opts(
    # title_opts=opts.TitleOpts(title="GDP Show", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True)
)

line.set_series_opts(
    linestyle_opts=opts.LineStyleOpts(opacity=1),
)

line.render("render.html")

# pyecharts 2.x 默认将 lineStyle.show 设为 false，折线不可见
# 后处理：将 series 中的 lineStyle.show 强制改为 true
# with open("render.html", "rb") as f:
#     html = f.read()

# html = html.replace(
#     b'"lineStyle": {\r\n                "show": false',
#     b'"lineStyle": {\r\n                "show": true',
# )

# with open("render.html", "wb") as f:
#     f.write(html)

# print("render.html generated successfully")