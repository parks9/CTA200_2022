#imports

import numpy as np
import ads

#First function

def top_cite(keyword, start_year, end_year, search_in):
    """
    Finds the number citations of papers with a keyword in the title/abstract
    for a given time span.





    Arguments
    ----------
    keyword : string
        Keyword that is searched in the title/abstract.

    start_year : int
        The initial year for the desired time frame.

    end_year : int
        The final year for the desired time frame.

    search_in : string ('title', 'abstract' or 'both')
        Specifies where the keyword is being searched.


    Returns
    ---------

    citations : array_like (float)
        Total number of citations found in each time division
        of the time frame

    titles : array_like (string)
        Name of each time division. (e.g. ['1990-2000', '2000-2010'])


    """

    #Creating arrays that will be populated after the query and ultimately
    #returned.

    decades = np.arange(start_year, end_year, 10)
    citations = np.zeros(len(decades)-1)
    titles = []


    #Requesting a query of the ADS, passing in the keyword and decade.


    for i in range(len(decades)-1):

        if search_in == 'title':
            test = ads.SearchQuery(q='title: %s year: %s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                        rows=50, sort='citation_count', fl=['citation_count'])

        elif search_in == 'abstract':
            test = ads.SearchQuery(q='abstract: %s year: %s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                            rows=50, sort='citation_count', fl=['citation_count'])

        elif search_in == 'both':
            test = ads.SearchQuery(q='title: %s abstract: %s year: %s' % (keyword,keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                rows=50, sort='citation_count', fl=['citation_count'])

        else:
            test = ads.SearchQuery(q='title: %s year:%s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                rows=50, sort='citation_count', fl=['citation_count'])




        titles.append(str(decades[i]) + '-' +str(decades[i+1]))
        count = []

        for paper in test:
            count.append(paper.citation_count)


        citations[i] = np.sum(count)


    return citations, titles



#Second function



def num_papers(keyword, start_year, end_year, search_in):
    """
    Finds the number of papers published with a keyword in the title/abstract
    for a given time span.




    Arguments
    ----------
    keyword : string
        Keyword that is searched in the title/abstract.

    start_year : int
        The initial year for the desired time frame.

    end_year : int
        The final year for the desired time frame.

    search_in : string ('title', 'abstract' or 'both')
        Specifies where the keyword is being searched.


    Returns
    ---------

    num_papers : array_like (float)
        Total number of papers published with 'keyword' in title/abstract for each time division
        of the time frame

    titles : array_like (string)
        Name of each time division. (e.g. ['1990-2000', '2000-2010'])


    """


    #Creating arrays that will be populated by the results of the search.
    

    decades = np.arange(start_year, end_year, 10)
    num_papers = np.zeros(len(decades)-1)
    titles = []


    #Requesting a query of the ADS, given the keyword input and the decade.


    for i in range(len(decades)-1):

        if search_in == 'title':
            test = ads.SearchQuery(q='title: %s year:%s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                    rows=2000, sort='citation_count', fl=['citation_count'])

        elif search_in == 'abstract':
            test = ads.SearchQuery(q='abstract: %s year: %s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                            rows=2000, sort='citation_count', fl=['citation_count'])

        elif search_in == 'both':
            test = ads.SearchQuery(q='title: %s abstract: %s, year: %s' % (keyword,keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                rows=2000, sort='citation_count', fl=['citation_count'])

        else:
            test = ads.SearchQuery(q='title: %s year: %s' % (keyword, (str(decades[i]) + '-' +str(decades[i+1]))), \
                                rows=2000, sort='citation_count', fl=['citation_count'])



        titles.append(str(decades[i]) + '-' +str(decades[i+1]))

        #Running a count of the length of the "list" of papers returned.
        
        count = 0

        for paper in test:
            count += 1

        num_papers[i] = count



    return num_papers, titles



#Third function


﻿def cite_count(keyword, search_in):
    
    """
    Ranks the top cited papers of all time given a specific keyword searched in the title/abstract.
    
    
    
    
    
    Arguments
    ----------
    keyword : string
        Keyword that is searched in the title/abstract.
        
    search_in : string ('title', 'abstract' or 'both')
        Specifies where the keyword is being searched.
        
   
        
    Returns
    ---------
    
    order : array_like (int)
        Ranks of the top cited papers, starting from #1 and counting up.
        
    citations : array_like (int)
        Number of citations for each paper, ordered from highest to lowest.
        
    
    """

    #Initializing the array that will collect the number of citations
    
    citations = []

    #Requesting a query of the ADS, sorted by citation count, given a keyword.
    
    if search_in == 'title':
    
        test = ads.SearchQuery(q='title: %s' % (keyword), \
                            rows=1000, sort='citation_count', fl=['citation_count'])
        
    elif search_in == 'abstract':
    
        test = ads.SearchQuery(q='abstract: %s' % (keyword), \
                            rows=1000, sort='citation_count', fl=['citation_count'])
        
    elif search_in == 'both':
        test = ads.SearchQuery(q='title: %s abstract: %s' % (keyword, keyword), \
                            rows=1000, sort='citation_count', fl=['citation_count'])
        
    else:
        test = ads.SearchQuery(q='title: %s' % (keyword), \
                            rows=1000, sort='citation_count', fl=['citation_count'])
        

    num = 0
    for paper in test:
        citations.append(paper.citation_count)
        num += 1
        
    
    #Array that will give the rank of the papers, from most cited to least.


    order = np.arange(1, num+1, 1)
    
    return order, citations



#Fourth function


def read_count(keyword, search_in):
    """
    Ranks the top read papers of all time given a specific keyword searched in the title/abstract.
    
    
    
    Arguments
    ----------
    keyword : string
        Keyword that is searched in the title/abstract.
        
    search_in : string ('title', 'abstract' or 'both')
        Specifies where the keyword is being searched.
   
        
    Returns
    ---------
    
    order : array_like (int)
        Ranks of the top cited papers, starting from #1 and counting up.
        
    reads : array_like (int)
        Number of reads for each paper, ordered from highest to lowest.
        
    
    """
    
    #Initializing the array that will store the read count values

    reads = []
    

    #Requesting a search of the ADS, sorted by read count, given a keyword.
    
    if search_in == 'title':
    
        test = ads.SearchQuery(q='title: %s' % (keyword), \
                        rows=1000, sort='read_count', fl=['read_count'])
        
    elif search_in == 'abstract':
    
        test = ads.SearchQuery(q='abstract: %s' % (keyword), \
                            rows=1000, sort='read_count', fl=['read_count'])
        
    elif search_in == 'both':
        test = ads.SearchQuery(q='title: %s abstract: %s' % (keyword, keyword), \
                            rows=1000, sort='read_count', fl=['read_count'])
        
    else:
        test = ads.SearchQuery(q='title: %s' % (keyword), \
                            rows=1000, sort='read_count', fl=['read_count'])

    num = 0
    for paper in test:
        reads.append(paper.read_count)
        num += 1
        
    #Creating array that will give the positional rank of the papers, from highest
    #to lowest read count.

    order = np.arange(1, num+1, 1)
    
    return order, reads
