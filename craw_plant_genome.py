#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
import urllib.request
import json


urls = 'https://www.plabipd.de/json/genomes_timeline.json'


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


with urllib.request.urlopen(urls) as url:
    data = json.loads(url.read().decode())
    # print(data)
	print("俗名\t拉丁名\t基因组大小M\t单位或作者\t文章标题\t期刊名称\t文章DOI\tPUBMED号\t发表年份\t开始年份\t分类\t分组")	
    for temp_dict in data['genomes']:
        common = temp_dict['common'] if 'common' in temp_dict else 'NA'
        stfname = temp_dict['ScientificName'] if 'ScientificName' in temp_dict else 'NA'
        gsize = temp_dict['GenomeSize'] if 'GenomeSize' in temp_dict else 'NA'
        author = temp_dict['Authorship'] if 'Authorship' in temp_dict else 'NA'
        title = temp_dict['Title'] if 'Title' in temp_dict else 'NA'
        source = temp_dict['Source'] if 'Source' in temp_dict else 'NA'
        doi = temp_dict['PubDoi'] if 'PubDoi' in temp_dict else 'NA'
        pubmed = temp_dict['PubMed'] if 'PubMed' in temp_dict else 'NA'
        year = temp_dict['PubYear'] if 'PubYear' in temp_dict else 'NA'
        start = temp_dict['start'] if 'start' in temp_dict else 'NA'
        classname = temp_dict['className'] if 'className' in temp_dict else 'NA'
        group = temp_dict['group'] if 'group' in temp_dict else 'NA'
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            common,stfname,gsize,author,title,source,doi,pubmed,year,start,classname,group
        ))




