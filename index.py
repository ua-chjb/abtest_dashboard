from dash import html, dcc, _dash_renderer
import dash_mantine_components as dmc
from dash_iconify import DashIconify
_dash_renderer._set_react_version('18.2.0')


from charts import fig_line, fig_bubble3d, fig_matrix, fig_barstack, fig_pieeven, fig_pieuneven, fig_bargroup, fig_barwhole
from data import df, df_lst, dct_lst, summ_table
from color import c, sm_lay


# # # # # # # # # # # # # # # # above the fold blockn1 # # # # # # # # # # # # # # # # # # #

comp_card_nsize = dmc.Card(
    [
        dmc.Text(
            f"{2000}",
            size="xl",
            fw=500,
            className="cc_u"
        ),
        dmc.Paper(
            "",
            className="sl"
        ),
        dmc.Text(
            "sample size",
            size="xl",
            className="cc_l"
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="q comp_card_nsize"
)

comp_card_groups = dmc.Card(
    [
        dmc.Text(
            f"{4}",
            size="xl",
            fw=500,
            className="cc_u"
        ),
        dmc.Paper(
            "",
            className="sl"
        ),
        dmc.Text(
            "groups tested",
            size="xl",
            className="cc_l"
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="q comp_card_groups"
)

comp_card_ctr = dmc.Card(
    [
        dmc.Text(
            f"{37.4}%",
            size="xl",
            fw=500,
            className="cc_u"
        ),
        dmc.Paper(
            "",
            className="sl"
        ),
        dmc.Text(
            "avg CTR",
            size="xl",
            className="cc_l"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="q comp_card_ctr"
)

comp_card_mult = dmc.Card(
    [
        dmc.Text(
            f"{4}x",
            size="xl",
            fw=500,
            className="cc_u"
        ),
        dmc.Paper(
            "",
            className="sl"
        ),
        dmc.Text(
            "higher CTR",
            size="xl",
            className="cc_l"
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="q comp_card_mult"
)



blockn1 = html.Div(
    [
        comp_card_nsize,
        comp_card_groups,
        comp_card_ctr,
        comp_card_mult,
    ],
    className="d dn1"
)

# # # # # # # # # # # # # # # # above the fold block0 # # # # # # # # # # # # # # # # # # #


comp_writing_hypothesis = dmc.Card(
    [
        dmc.Text(
            "Summary",
            fw=500,
            size="xs"
        ),

        dmc.Text(
            "This AB test consisted of 4 hypothesis tests, each considering whether the observed count of click-throughs deviated from the norm. In these tests, the norm is considered the approximate mode of the CTR 23.48% - 76.52%, multiplied by the number of observations in that category.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 1: Classic, funny",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "H0: The data are distributed as expected.",
            size="xs"
        ),
        dmc.Text(
            "Ha: The data are not distributed as such.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 2: Classic, patriotic",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "H0: The data are distributed as expected.",      
            size="xs"
        ),
        dmc.Text(
            "Ha: The data are not distributed as such,",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 3: Diet, funny",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "H0: The data are distributed as expected.",
            size="xs"
        ),
        dmc.Text(
            "Ha: The data are not disitributed as such.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 4: Diet, patriotic",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "H0: The data are distributed as expected.",
            size="xs"
        ),
        dmc.Text(
            "Ha: The data are not distributed as such.",
            size="xs"
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_wr_hyp"
)

comp_fig_line = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_line(df_lst)), 
            className="g", id="FIG_LINE")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_line"
)

comp_inle_hyp = html.Div(
    [
        comp_writing_hypothesis
    ],
    className="inline"
)

block0 = html.Div(
    [
        comp_inle_hyp,
        comp_fig_line
    ],
    className="d d0"
)

# # # # # # # # # # # # # # # # block1 # # # # # # # # # # # # # # # # # # #

comp_fig_barstack = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_barstack(df)), 
            className="g", id="FIG_BARSTK")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_barstack"
)


comp_fig_matrix = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_matrix(df)), 
            className="g", id="FIG_MTX")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_matrix"
)

comp_writing_square = dmc.Card(
    [
        dmc.Text(
            "Product",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            """
            There are two products: "classic" and "diet". These products are independent of the campaigns. Between the two products, "classc" had a better CTR, on the whole. To see the the CTR of each campaign by product, hover over the bar chart to the left.
            """,
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Campaign",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            """
            Two campaigns were also tested, across both products: "funny" and "patriotic". The result is a 2x2 matrix as seen in the green figure to the left. The darker color of green represents a higher CTR.
            """,
            size="xs"
        )

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_wr_square"
)

comp_inle_wr = html.Div(
    [
        comp_writing_square
    ],
    className="inline"
)


block1 = html.Div(
    [
        comp_fig_matrix,
        comp_fig_barstack,
        comp_inle_wr
    ],
    className="d d1"
)

# # # # # # # # # # # # # # # # # block 2 # # # # # # # # # # # # # # # # # # #


comp_fig_3d = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_bubble3d(df)), 
            className="g", id="FIG_3D")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_3d"
)


comp_fig_peven = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_pieeven(df)), 
            className="g", id="FIG_PIEV")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_peven"
)

comp_fig_puneven = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_pieuneven(df)), 
            className="g", id="FIG_PIEUNV")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_puneven"
)

comp_fig_bargroup = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_bargroup(df)), 
            className="g", id="FIG_BARGR")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_bargroup"
)


comp_fig_barwhole = dmc.Card(
    [
        dcc.Graph(figure=sm_lay(fig_barwhole(df)), 
            className="g", id="FIG_BARWH")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_barwhole"
)


block2 = html.Div(
    [
        comp_fig_peven,
        comp_fig_puneven,
        comp_fig_3d,
        comp_fig_bargroup,
        comp_fig_barwhole
    ],
    className="d d2"
)


# # # # # # # # # # # # # # # # block3 # # # # # # # # # # # # # # # # # # #

comp_fig_tstat = dmc.Card(
    [
        dcc.Graph(
            figure={}, 
            className="g",
            id="FIG_TSTAT"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_fig_tstat"
)

comp_call_tstat = dmc.Card(
    [
        dmc.Text(
            "Calculated test statistics, observed data",
            size="xs",
            fw=500
        ),
        dmc.Text(
            "Click to see test statistic and manually calculated pvalue",
            size="xs",
        ),
        dmc.Stack(
            [
                dmc.Checkbox(
                    checked=False, label="Classic, patriotic", 
                    id="CP", size="xs"),
                dmc.Checkbox(
                    checked=False, label="Classic, funny", 
                    id="CF", size="xs"),
                dmc.Checkbox(
                    checked=False, label="Diet, patriotic", 
                    id="DP", size="xs"),
                dmc.Checkbox(
                    checked=False, label="Diet, funny", 
                    id="DF", size="xs"),
            ],
            id="CALL_CHK",
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_call_tstat"
)

comp_writing_simulation = dmc.Card(
    [
        dmc.Text(
            "statistical simulation",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "simulation summary @ runs=1,000",
            size="xs"
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_wr_sim"


)

comp_inle_tstat = html.Div(
    [
        comp_call_tstat,
        comp_writing_simulation
    ],
    className="inline"
)

block3 = html.Div(
    [
        comp_fig_tstat,
        comp_inle_tstat
    ],
    className="d d3"
)


# # # # # # # # # # # # # # # # block4 # # # # # # # # # # # # # # # # # # #
comp_writing_conclusion = dmc.Card(
    [
        dmc.Text(
            "Conclusion",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "In 2/4 of the tests, we failed to reject the null hypothesis based on the test statistic and associated pvalue.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 1: Classic, funny",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "We reject the null hypothesis in favor of the alternative with a test statistic of 854.5 and a pvalue of 0.0000.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 2: Classic, patriotic",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "We fail to reject the null hypothesis with a test statistic of 4.6 and a pvalue of 0.0450.",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 3: Diet, funny",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "We fail to reject the null hypothesis with a test statistic of 2.1 and a pvalue of 0.1700",
            size="xs"
        ),
        dmc.Text(
            """
            .  
            .
            """,
            c="white",
            size="xs"
        ),
        dmc.Text(
            "Test 4: Diet, patriotic",
            fw=500,
            size="xs"
        ),
        dmc.Text(
            "We reject the null hypothesis in favor of the alternative, with a test statistic of 14.1 and a pvalue of 0.0002.",
            size="xs"
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_wr_concl"
)

res_df = summ_table(dct_lst)
res_df["variant"] = res_df.index
res_df = res_df[["variant", "runs", "table_pvalue", "counted_pvalue", "test_statistic"]]
head = res_df.columns
body = res_df.values


comp_table_res = dmc.Card(
    [
        dmc.Table(
            striped=True,
            highlightOnHover=True,
            withTableBorder=True,
            withColumnBorders=True,
            data={
                "head": head,
                "body": body
            },
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp_table_res"
)

comp_inle_tbl = html.Div(
    [
        comp_table_res
    ],
    className="inline"
)

block4 = html.Div(
    [
        comp_writing_conclusion,
        comp_inle_tbl
    ],
    className="dnull d4"
)

# # # # # # # # # # # # # # # footer # # # # # # # # # # # # # #

color = "white"

icon_github = DashIconify(icon="simple-icons:github", width=30, color=color, className="bb")
link_github = "https://www.github.com/ua-chjb"
icon_linkedin = DashIconify(icon="devicon-plain:linkedin", width=30, color=color, className="bb")
link_linkedin = "https://linkedin.com/in/benjaminbnoyes"
icon_email = DashIconify(icon="mdi:email", width=30, color=color, className="bb")
link_email = "mailto:noyesbenjamin7@gmail.com"
icon_spotify = DashIconify(icon="cib:spotify", width=30, color=color, className="bb")
link_spotify = "https://open.spotify.com/playlist/7GlI9taOWvrjokuxt7U4ME?si=Xe2oszntQZ2VD9yfO6uQCw"
icon_soundcloud = DashIconify(icon="cib:soundcloud", width=40, color=color, className="bb")
link_soundcloud = "https://soundcloud.com/bennoyes-onb"  


comp20_footer0_github = dmc.Anchor(
    icon_github, href=link_github, target="_blank", 
    size="xl",
    className="footnt comp20_footer0_github"
)

comp21_footer1_linkedin = dmc.Anchor(
    icon_linkedin, href=link_linkedin, target="_blank", 
    size="xl",
    className="footnt comp21_footer1_linkedin"
)

comp22_footer2_email = dmc.Anchor(
    icon_email, href=link_email, target="_blank", 
    size="sm",
    className="footnt comp22_footer2_email"
)

comp23_footer3_spotify = dmc.Anchor(
    icon_spotify, href=link_spotify, target="_blank", 
    size="xl",
    className="footnt comp23_footer3_spotify"
)

comp24_footer4_soundcloud = dmc.Anchor(
    icon_soundcloud, href=link_soundcloud, target="_blank",
    size="xl",
    className="footnt comp24_footer4_soundcloud"
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2024 all rights reserved",
    className="footertinytext"
)

footer = dmc.Card(
    [
        comp20_footer0_github,
        comp21_footer1_linkedin,
        comp22_footer2_email,
        comp23_footer3_spotify,
        comp24_footer4_soundcloud,
        comp25_copyrightfooter
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f"
)

# # # # # # # # # # # # # # title # # # # # # # # # # # # # #


title = dmc.Card(
    [
        dmc.Text(
            "AB Test: Click-Through Rate (CTR)",
            size="xl",
            fw=600
            )
    ],
    className="t tit",
    withBorder=True,
    shadow="sm",
    radius="md",
)

comp_mob_all = html.Div(
    [
        blockn1,
        block0,
        block1,
        block2, 
        block3,
        block4
    ],
    className="m"
)

# # # # # # # # # # # # # # # # composition # # # # # # # # # # # # # # # # # # #


lyt = dmc.MantineProvider(
    [
        title,
        comp_mob_all,
        footer
    ]
)
