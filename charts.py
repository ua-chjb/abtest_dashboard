from plotly.tools import FigureFactory as ff
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from plotly.offline import *
import plotly.express as px
import plotly.io as pio

from itertools import *
import pandas as pd

# from data import df, df_lst, dct_lst
from color import c


############################ line chart #################################

def fig_line(df_lst):

  color_cyc = cycle(iter(c))

  fig = go.Figure()
  for df in df_lst:
    fig.add_trace(
      go.Scatter(
      x=df["counter"],
      y=df["cumsum"],
      mode="lines",
      marker={"color": next(color_cyc)},
      name=", ".join([df.loc[0, "product"], df.loc[0, "campaign"]])
    )
  )
  return fig.update_layout({
    "xaxis": {"title": "user_id count"},
    "yaxis": {"title": "cumulative click-throughs"},
    "title": {"text": "cumulative click-throughs, unique by product & campaign"},
    "legend": {"title": "product & campaign"}
  })


############################ scatter3d #################################

def fig_bubble3d(df):

  gb1 = df.groupby(["product", "campaign", "type"]).count().iloc[:, :3].rename(
    columns={
      "conv": "count"
    }
  )

  gb1["index"] = ["_".join([k, l, o]) for k, l, o in gb1.index]
  gb1 = gb1.reset_index()
  gb1["product_campaign"] = gb1["product"] + ", " + gb1["campaign"]


  fig = px.scatter_3d(
    gb1, 
    x="product", 
    y="campaign", 
    z="type", 
    hover_data="count",
    color_discrete_sequence=c,
  ).update_layout({
    "scene": {
      "zaxis": {
        "categoryorder": "array", 
        "categoryarray": [
          "land", "click"
        ]
      }
    }
  }).update_traces({
    "marker": {
      "size": [j/10 for j in gb1["count"]],
      "color": px.colors.sequential.Greens[5],
    #   "color": [c[0]] + [c[0]] + [c[1]] + [c[1]] + [c[2]] + [c[2]] + [c[3]] + [c[3]]
    #   "symbol": "square",
    }
  }).update_layout({
    "title": {
      "text":"Product and campaign by conversion type",
    }
  })

  return fig


############################ bar chart stack #################################


def fig_barstack(df):

  fig = go.Figure()

  gb0 = df.groupby(["product", "campaign"]).agg({"conv": "sum"}).reset_index()
  color_cyc = cycle(iter(c))

  for idx in range(len(gb0)):
    color=next(color_cyc)
    fig.add_trace(
      go.Bar(
        x=[gb0.loc[idx, "product"]],
        y=[gb0.loc[idx, "conv"]],
        name=", ".join(gb0.loc[idx, "product":"campaign"].values),
        marker={"color": color},
      )
    )

  return fig.update_layout({
    "bargap": 0.5,
    "barmode": "stack",
    "legend": {"title": "product, campaign"},
    "title": "total click-throughs, by product & campaign",
    "yaxis": { "title": "conv", "range": [0, 550]},
  })

############################ bar chart group #################################

def fig_bargroup(df):

  fig = go.Figure()

  gb0 = df.groupby(["product", "campaign"]).agg({"conv": "sum"}).reset_index()
  color_cyc = cycle(iter(c))

  for idx in range(len(gb0)):
    color=next(color_cyc)
    fig.add_trace(
      go.Bar(
        y=[gb0.loc[idx, "product"]],
        x=[gb0.loc[idx, "conv"]],
        name=", ".join(gb0.loc[idx, "product":"campaign"].values),
        marker={"color": color},
        orientation="h",
      )
    )

  return fig.update_layout({
    "bargap": 0.5,
    "barmode": "group",
    "xaxis": {
      "title": "conv",
      "range": [0, 550]
    },
    "legend": {"title": "product, campaign"},
    "title": "total click-throughs, by p & c",
  })

############################ bar chart whole #################################


def fig_barwhole(df):

  gb2 = df.groupby(["product"]).agg({"conv": "sum"}).reset_index()

  fig = px.bar(
      gb2,
      y="product",
      x="conv",
      orientation="h",
      color_discrete_sequence=px.colors.sequential.Greens[4:],
  ).update_traces({
      "marker":{"line": {"width": 0}}
  }).update_layout({
      "bargap": 0.5,
      "title": "total click-throughs, by product",
      "yaxis": {"categoryorder": "array",
      "categoryarray": ["classic", "diet"]},
      "xaxis": {"title": "conv","range": [0, 550]
    },
  })

  return fig

############################ test stat #################################


def fig_teststatistic_1(modeldata_dct):

  runs = modeldata_dct["runs"]
  stats_lst = modeldata_dct["stats_lst"]
  pvals_lst = modeldata_dct["pvals_lst"]

  fig = px.scatter(
      x=stats_lst,
      y=pvals_lst,
      color_discrete_sequence=[px.colors.qualitative.T10[9]],
  )

  fig.update_layout({
      "title": {"text": f"test statistic by pvalue, modeled data, runs={runs}"},
      "xaxis": {"title": "test statistic"},
      "yaxis": {"title": "pvalue"},
  })

  return fig

def fig_teststatistic_2(fig, dct_lst):

  if not dct_lst:
    pass

  else:
    for dct in dct_lst:

        name = dct["name"]

        x=dct["test_statistic"]
        y=dct["counted_pvalue"]

        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                name=name,
                # zorder=1,
                marker={"color": dct["c"], "symbol": "diamond"}
            )
        )

        fig.add_annotation(
            x=x, y=y,
            text=name,
            ax=30, ay=-30
        )

  return fig

# fig_lst = fig_teststatistic(dct_lst)

############################ matrix #################################

def fig_matrix(df):
    gb = df.groupby(["campaign", "product"])["conv"].mean()

    summit = gb.sum(axis=0)
    gb1 = gb / summit

    gb2 = gb1.reset_index().pivot(index="campaign", columns="product")
    gb2.columns = ["_".join(j) for j in gb2.columns]
    fig = px.imshow(gb2,  color_continuous_scale="Greens", zmax=1, zmin=0)

    fig.update_layout({
        "title": {"text": "product / campaign matrix, color as CTR"},
        "xaxis": {"title": "product"},
        "coloraxis_showscale": False
    })

    return fig

# fig_matrix(df)

############################ pie, even #################################

def fig_pieeven(df):
  return px.pie(
    df.sort_values(by=["product", "campaign"], ascending=False), 
    # df,
    "product_campaign", 
    # category_orders={"product_campaign": ["classic_funny", "classic_patriotic", "diet_funny", "diet_patriotic"]},
    # color_discrete_sequence=c, 
    color_discrete_sequence=[c[2]] + [c[1]] + [c[0]] + [c[3]], 
    hole=0.5
).update_traces({"textposition": "inside"}).update_layout({
  "title": "distribution of total observed",
})

############################ pie, uneven #################################

# df1 = df[df["conv"]==1].sort_values(by=["product", "campaign"], ascending=False),

def fig_pieuneven(df):
  df1 = df[df["conv"]==1]
  return px.pie(
    # df1 = df[df["conv"]==1].sort_values(by=["product", "campaign"], ascending=False),
    # dfpdf["conv"]==1,
    # df,
    df1,
    "product_campaign", 
    # color_discrete_sequence=c, 
    color_discrete_sequence=[c[0]] + [c[3]] + [c[2]] + [c[1]], 
    hole=0.5
).update_traces({"textposition": "inside"}).update_layout({
  "title": "distribution of click-throughs observed"
})