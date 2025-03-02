from keys import aki, sak
from color import c
import pandas as pd
import numpy as np
import boto3
import json
import os

os.environ['AWS_ACCESS_KEY_ID'] = aki
os.environ['AWS_SECRET_ACCESS_KEY'] = sak

# # # # # # # # # # # # # # # # # simulation results # # # # # # # # # # # # # # ## 

s3_resource = boto3.resource("s3")

get_object = s3_resource.Bucket("samplestats").Object("CTR_dashboard/cf_pc.json").get()
cf_pc_dct = dict(json.loads(get_object['Body'].read()))

get_object = s3_resource.Bucket("samplestats").Object("CTR_dashboard/cp_pc.json").get()
cp_pc_dct = dict(json.loads(get_object['Body'].read()))

get_object = s3_resource.Bucket("samplestats").Object("CTR_dashboard/cf_pd.json").get()
cf_pd_dct = dict(json.loads(get_object['Body'].read()))

get_object = s3_resource.Bucket("samplestats").Object("CTR_dashboard/cp_pd.json").get()
cp_pd_dct = dict(json.loads(get_object['Body'].read()))

runs = cf_pc_dct["runs"]
stats_lst = cf_pc_dct["stats_lst"]
pvals_lst = cf_pc_dct["pvals_lst"]

cf_pc_dct["c"] = c[0]
cp_pc_dct["c"] = c[1]
cf_pd_dct["c"] = c[2]
cp_pd_dct["c"] = c[3]

modeldata_dct = {
  "runs": runs,
  "stats_lst": stats_lst,
  "pvals_lst": pvals_lst
}

def summ_table(dct_lst):
  data = [list(dct_lst[j].values())[:5] for j in range(len(dct_lst))]
  columns = list(dct_lst[0].keys())[:5]

  scores=pd.DataFrame(
    data=data, 
    columns=columns
  ).set_index("name")

  return scores[["runs", "test_statistic", "table_pvalue", "counted_pvalue"]].round(4)

dct_lst = [cf_pc_dct, cp_pc_dct, cf_pd_dct, cp_pd_dct]

# # # # # # # # # # # # # # # # # main dataframe, s3fs # # # # # # # # # # # # # # ## 

df = pd.read_csv("s3://samplestats/CTR_dashboard/adclicks.csv")

cf_pc_mk = (df["campaign"] == "funny" ) & ( df["product"] == "classic" )
cf_pd_mk = (df["campaign"] == "funny" ) & ( df["product"] == "diet" )
cp_pc_mk = (df["campaign"] == "patriotic" ) & ( df["product"] == "classic" )
cp_pd_mk = (df["campaign"] == "patriotic" ) & ( df["product"] == "diet" )

df["cumsum"] = np.nan

cf_pc_df = df[cf_pc_mk].reset_index(drop=True).reset_index(drop=False).rename(columns={"index": "counter"})
cf_pd_df = df[cf_pd_mk].reset_index(drop=True).reset_index(drop=False).rename(columns={"index": "counter"})
cp_pc_df = df[cp_pc_mk].reset_index(drop=True).reset_index(drop=False).rename(columns={"index": "counter"})
cp_pd_df = df[cp_pd_mk].reset_index(drop=True).reset_index(drop=False).rename(columns={"index": "counter"})

cf_pc_df["cumsum"] = cf_pc_df["conv"].cumsum()
cf_pd_df["cumsum"] = cf_pd_df["conv"].cumsum()
cp_pc_df["cumsum"] = cp_pc_df["conv"].cumsum()
cp_pd_df["cumsum"] = cp_pd_df["conv"].cumsum()

df_lst = [cf_pc_df, cp_pc_df, cf_pd_df, cp_pd_df]