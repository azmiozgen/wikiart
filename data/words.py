class WordDict:

    ## Words to exclude. Useless, meaningless words (nicknames etc.)
    EXCLUDING_WORDS = ['a', 'an', 'the', 'and', 'this', 'that', 'of']

    ## Special meaning or not-in-dictionary words. Not to exclude. (character names, urban words etc.)
    INCLUDING_WORDS = ['post-impressionism', 'ukiyo-e', 'st. james the greater',
                       ]

    MAPPING_WORDS = {'valenciaspain' : ['valencia', 'spain'],
                     'pericope-adulterae' : ['pericope adulterae'],
                     'prodigal-son' : ['prodigal son'],
                     'parables-of-jesus' : ['parables of jesus'],
                     'st.-martha' : ['st. martha'],
                     'amsterdamnetherlands' : ['amsterdam', 'netherlands'],
                     'petit dallesfrance' : ['petit-dalles', 'france'],
                     'eugene-delacroix' : ['eugene delacroix'],
                     'colin-alexander' : ['colin alexander'],
                     'marie-de-medici' : ["marie de' medici"],
                     'theodore-gericault' : ['theodore gericault'],
                     'old-testament' : ['old testament'],
                     'saint petersburgrussian federation' : ['saint petersburg', 'russian federation'],
                     'abramtsevorussian federation' : ['abramtsevo', 'russian federation'],
                     'allegheny city, pennsylvaniaunited states' : ['allegheny city', 'pennsylvania', 'united states'],
                     'alten / dessau-altengermany' : ['alten', 'dessau-alten', 'germany'],
                     'amagerbro / copenhagen / amagerbrodenmark' : ['amagerbro', 'copenhagen', 'denmark'],
                     'angeac / angeac-charentefrance' : ['angeac', 'angeac-charente', 'france'],
                     'antwerpbelgium' : ['antwerp', 'belgium'],
                     'antwerpnetherlands' : ['antwerp', 'netherlands'],
                     'arcachonfrance' : ['arcachon', 'france'],
                     }
