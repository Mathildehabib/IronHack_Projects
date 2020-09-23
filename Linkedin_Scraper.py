# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:55:43 2020

@author: mathi
"""

import pandas as pd
from bs4 import BeautifulSoup as BS
import requests as r
import re
import time as t
from sqlalchemy import create_engine
import pymysql

database_username = 'root'
database_password = '***********'
database_ip       = 'localhost'
database_name     = 'linkedin_jobs'

database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(database_username, database_password,
                                                                             database_ip, database_name))

def scrape_linkedin_job_search(keywords,data=None):
    if data is None:   #Create it
        columns = ['Title', 'Company', 'Location','Link', 'Job Level','Job Type','Function', 'Sector','Description','Short Description']
        data = pd.DataFrame(columns=columns)
        
    data_all=data.copy()

    for i in range(4):
        titles = []
        companies = []
        locations = []
        links = []
        linkss=[]
        linksss=[]
        job_level=[]
        job_type=[]
        function=[]
        sector=[]
        description=[]
        
        url=f'https://www.linkedin.com/jobs/search/?keywords={keywords}&location=France&start={i*25}'
        page = r.get(url)
        soup = BS(page.content,features="lxml")

        for i in soup.select("div.result-card__contents"):
            title = i.findChild("h3", recursive=False)
            company = i.findChild("h4", recursive=False)
            location = i.findChild("span", attrs={"class": "job-result-card__location"}, recursive=True)
            titles.append(title.string)
            companies.append(company.string)
            locations.append(location.string)

        links=soup.find_all(href=True)
        for i in links:
            if '/jobs/view' in str(i):
                linkss.append(i)
                
        for i in linkss:
            linksss.append(''.join(re.findall('href="(.+)"><span',str(i))))

        for i in range(len(linksss)):
            url=linksss[i]
            if i%5==0:
                t.sleep(1)
            page=r.get(linksss[i]).content
            soup=BS(page,features="lxml")
            job_level.append(' '.join([j.text for j in soup.select('.description > ul > li:nth-child(1) > span')]))
            job_type.append(' '.join([j.text for j in soup.select('.description > ul > li:nth-child(2) > span')]))
            function.append(' '.join([j.text for j in soup.select('.description > ul > li:nth-child(3) > span')]))
            sector.append(' '.join([j.text for j in soup.select('.description > ul > li:nth-child(4) > span')]))
            description.append(' '.join([j.text for j in soup.select('section.description > div')]))


        zipped = zip(titles, companies, locations, linksss, job_level, job_type, function, sector, description)
        for i in list(zipped):
            data_all=data_all.append({'Title' : i[0] , 'Company' : i[1], 'Location': i[2],'Link':i[3], 'Job Level': i[4], 'Job Type': i[5], 'Function': i[6], 'Sector': i[7], 'Description':i[8]} , ignore_index=True)
        
    data_all=data_all.drop_duplicates(keep='first',subset=['Company','Description']).reset_index(drop=True)
    data_new=data_all.copy()
    if data_all.shape[0]>data.shape[0]:
        rows_to_drop=[i for i in range(data.shape[0])]
        data_new=data_new.drop(rows_to_drop).reset_index(drop=True)
    data_new['Description']=data_new['Description'].apply(lambda x:x.lower())
    
    data_new['Short Description']=''

    for i in range(data_new.shape[0]):
        if 'sql' in data_new['Description'][i]:
            data_new['Short Description'][i]='SQL, '
        if 'python' in data_new['Description'][i]:
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'Python, '
        if 'tableau' in data_new['Description'][i]:
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'Tableau, '
        if 'scikit' in data_new['Description'][i] or 'sklearn' in data_new['Description'][i]:
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'SkLearn, '
        if 'git' in data_new['Description'][i] :
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'git, '
        if 'pandas' in data_new['Description'][i] :
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'Pandas, '
        if 'numpy' in data_new['Description'][i] :
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'Numpy, '
        if 'seaborn' in data_new['Description'][i] or 'matplolib' in data_new['Description'][i] or 'visualization' in data_new['Description'][i] or 'visualisation' in data_new['Description'][i]:
            data_new['Short Description'][i]=str(data_new['Short Description'][i])+'Data Viz, ' 
            
    data_all.to_sql('data_all',database_connection, if_exists='replace', index=False)
    data_new.to_sql('data_new',database_connection, if_exists='replace', index=False)
    
    return data_new


DATA=pd.read_sql('data_all',database_connection)

scrape_linkedin_job_search("data%20analyst",DATA)
