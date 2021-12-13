#import requests
#api_url = "https://jsonplaceholder.typicode.com/todos/1"
#response = requests.get(api_url)
#response.json()
#print(response.status_code)
#print(response.json().keys())

import streamlit as st
import pandas as pd
#import folium

df = pd.read_csv("people_testdata.csv")
#print(df.describe())
#print(df.info())
#print(df.head())
#print(df.tail())
#print(df.columns)

#(['uuid', 'name', 'type', 'permalink', 'cb_url', 'rank', 'created_at',
 #      'updated_at', 'first_name', 'last_name', 'gender', 'country_code',
  #     'state_code', 'region', 'city', 'featured_job_organization_uuid',
   #    'featured_job_organization_name', 'featured_job_title', 'facebook_url',
    #   'linkedin_url', 'twitter_url', 'logo_url'],
     # dtype='object')

#remove duplicates
df = df.drop_duplicates(subset=None,keep="first",inplace=False)

#create subset of dataframe with important columns
df_imp = df.drop(['uuid', 'type', 'permalink', 'cb_url', 'rank', 'created_at', 'updated_at', 'state_code',
                  'region', 'city', 'featured_job_organization_uuid','logo_url'], axis=1)
#print(df_imp.info())

# select rows where featured_job_title = founder or co-founder
# the testdata contains manually adjusted job titles
founders = df_imp.loc[(df_imp["featured_job_title"]=="Founder") | (df_imp["featured_job_title"]=="Co-Founder")]
#print(founders.info())
#print(founders)

# create table containing the following information:
# name, role (founder, co-founder), company name, country, email address, number of followers
# sort by number of followers
founders_view = founders.drop(['first_name','last_name','gender','facebook_url','linkedin_url'], axis=1)
#print(founders_view.columns)
#'twitter_url'

#json1 = f"world.geojson"
#m = folium.Map(location=[4.2215, 51.368], tiles="CartoDB positron", name = "Founders Map", zoom_start=5)
#folium.Choropleth(geo_data ='json1',name = "choropleth",data = founders)
st.set_page_config(page_title="Founders of companies", initial_sidebar_state="auto", layout="wide")
title = """
             <h1 style = "color: 332E34; text-align: center" >Founders of companies with the most followers on social media</h1>
             <h5 style = "color: #2F2523; text-align: center" > </h5>
             """

option = st.sidebar.selectbox("Please select a country:", ["USA", "Australia", "Vietnam", "Denmark", "India","England"])
#st.sidebar.markdown(" ")
if option == "USA":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in USA")
   usa = founders_view.loc[founders_view["country_code"] == "USA"]
   usa = usa.drop(["country_code"], axis = 1)
   st.table(usa)

if option == "Australia":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in Australia")
   aus = founders_view.loc[founders_view["country_code"] == "AUS"]
   aus = aus.drop(["country_code"], axis = 1)
   st.table(aus)

if option == "Vietnam":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in Vietnam")
   vnm = founders_view.loc[founders_view["country_code"] == "VNM"]
   vnm = vnm.drop(["country_code"], axis = 1)
   st.table(vnm)

if option == "Denmark":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in Denmark")
   dnk = founders_view.loc[founders_view["country_code"] == "DNK"]
   dnk = dnk.drop(["country_code"], axis = 1)
   st.table(dnk)

if option == "India":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in India")
   ind = founders_view.loc[founders_view["country_code"] == "IND"]
   ind = ind.drop(["country_code"], axis = 1)
   st.table(ind)
   
if option == "England":
   st.markdown(title, unsafe_allow_html=True)
   st.text("Founders in England")
   gbr = founders_view.loc[founders_view["country_code"] == "GBR"]
   gbr = gbr.drop(["country_code"], axis = 1)
   st.table(gbr)



