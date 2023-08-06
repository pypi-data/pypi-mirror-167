CLI utility for reading RSS news from given URL


Provides rss-reader command that receives single positional argument "source",
that should be the URL for rss news. Utility will collect data from that URL and
print out collected data in human readable format.


Usage example:

rss-reader "https://news.yahoo.com/rss/" --limit 1


Output:

Feed: Yahoo News - Latest News & Headlines 

Title: Woman whose rape DNA led to her arrest sues San Francisco 
Date: 2022-09-12T20:58:22Z 
Link: https://news.yahoo.com/woman-whose-rape-dna-led-205822755.html 


Optional arguments:

--limit [LIMIT]  Set the maximum amount of output messages

--verbose        Increase output verbosity

--version        Show current version

--json           Set output format to JSON. 

Example of JSON output:

{"Feed": "Yahoo News - Latest News & Headlines",
"Entries": [{"Title": "Woman whose rape DNA led to her arrest sues San Francisco",
"Date": "2022-09-12T20:58:22Z",
"Link": "https://news.yahoo.com/woman-whose-rape-dna-led-205822755.html"},]}
