# telugumovieswiki
A simple python script to parse telugu movies by year from wikipedia
Accepts range of years and constructs a json with list of movies and writes them to a file.
Output file name : `movies.json`

Example

```
telugumovies: mymac $ pip install -r requirements.txt

telugumovies: mymac $ python parse.py

Enter min year: 1999
Enter max year: 2005

Fetch movies for year : 1999, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_1999
Fetch movies for year : 2000, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2000
Fetch movies for year : 2001, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2001
Fetch movies for year : 2002, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2002
Fetch movies for year : 2003, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2003
Fetch movies for year : 2004, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2004
Fetch movies for year : 2005, URL : http://en.wikipedia.org/wiki/List_of_Telugu_films_of_2005
telugumovies: mymac $
```

Sample output file data:

```
[  
   {  
      "director":"Kodi Ramakrishna",
      "cast":[  
         "Prakash Raj",
         " Ramya Krishna"
      ],
      "name":"Aavide Shyamala",
      "year":1999
   },
   {  
      "director":"",
      "cast":[  
         "Siva Krishna",
         " Ragini"
      ],
      "name":"Ammo Polisollu",
      "year":1999
   },
   {  
      "director":"Ramesh Sarangan",
      "cast":[  
         "Srikanth",
         " Soundarya",
         " Abbas",
         " Raghuvaran"
      ],
      "name":"Anaganaga Oka Ammai",
      "year":1999
   }
]

```
