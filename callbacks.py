from dash import Input, Output

from data import dct_lst, modeldata_dct
from charts import fig_teststatistic_1, fig_teststatistic_2
from color import sm_lay


def callbacks_baby(app):
    @app.callback(
        Output("FIG_TSTAT", "figure"),        
        Input("CP", "checked"),
        Input("CF", "checked"),
        Input("DP", "checked"),
        Input("DF", "checked")
    )
    def thrutheportal(cp, cf, dp, df):

        fig = sm_lay(fig_teststatistic_1(modeldata_dct))

        full_dct_dct = {}

        full_dct_dct["cf"] = dct_lst[0]
        full_dct_dct["cp"] = dct_lst[1]
        full_dct_dct["df"] = dct_lst[2]
        full_dct_dct["dp"] = dct_lst[3]

        if not cf:
            full_dct_dct.pop("cf")
        else:
            full_dct_dct["cf"] = dct_lst[0]
        
        if not cp:
            full_dct_dct.pop("cp")
        else:
            full_dct_dct["cp"] = dct_lst[1]

        if not df:
            full_dct_dct.pop("df")
        else:
            full_dct_dct["df"] = dct_lst[2]

        if not dp:
            full_dct_dct.pop("dp")
        else:
            full_dct_dct["dp"] = dct_lst[3]

        fig = sm_lay(fig_teststatistic_2(fig, list(full_dct_dct.values())))

        return fig