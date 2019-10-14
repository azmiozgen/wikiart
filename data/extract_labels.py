import glob
import os
import string

import enchant
from collections import OrderedDict
import numpy as np
import pandas as pd

from chars import CharDict
from words import WordDict

def lookup_dictionary(s, dictionary=WordDict):
    ## 1 : In dictionary, include it. Do not split
    ## 0 : In dictionary but exclude it.
    ## -1 : Not in dictionary.
    
    if s == '':
        return 0
    
    ## English check
    enchantment = enchant.Dict("en_US")
    is_english = enchantment.check(s)
    
    if s in dictionary.INCLUDING_WORDS or is_english:
        return 1
    if s in dictionary.EXCLUDING_WORDS:
        return 0
    if s not in dictionary.INCLUDING_WORDS and is_english and s not in dictionary.EXCLUDING_WORDS:
        return -1
    
def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def split_scriptiocontinua(s):
    lookup_result = lookup_dictionary(s)
    if lookup_result == 1:
        return s
    elif lookup_result == 0:
        return ''
    else:
        return ' '.join(wordninja.split(s))
    
def handle_numerals(s, dictionary=WordDict):
    if s in dictionary.INCLUDING_WORDS:
        return s
    else:
        for num in range(10):
            s = s.replace(str(num), '')
        return s

def is_fully_printable(s):
    return all([i in string.printable for i in s])

def replace_chars(s, dictionary=CharDict):
    ## Replace punctuation
    s = "".join(list(map(lambda x: dictionary.PUNCTUATION_REPLACEMENT_DICT.get(x, x), s)))
    
    ## Replace letters
    s = "".join(list(map(lambda x: dictionary.LETTER_REPLACEMENTS_DICT.get(x, x), s)))
    return s

def strip_brackets(s, brackets=[('(', ')'), ('{', '}'), ('[', ']')]):
    bracket_points = []
    for bracket_pair in brackets:
        p1, p2 = bracket_pair
        if p1 in s and p2 in s:
            bracket_points.append((s.find(p1), s.find(p2)))
        
    return contents

# brackets=[('(', ')'), ('{', '}'), ('[', ']')]
def extract_words(s, delimiter='@@@'):
    for punct in string.punctuation:
        s = s.replace(punct, delimiter)
        
    tokens = s.split(delimiter)
    tokens = remove_duplicates(tokens)

    tokens = list(map(lambda s: s.strip(), tokens))
    tokens = list(filter(lambda s: s not in string.punctuation, tokens))
        
    return tokens

if __name__ == "__main__":

    IMAGES_DIR = './images/'
    OUTPUT_TAGS_FILE = './tags.txt'

    labels_df = pd.read_csv("metadata.txt", delimiter='|')
    labels_df = labels_df.replace(np.nan, '', regex=True)
    n_paintings = len(labels_df.index)

    for i, row in enumerate(np.array(labels_df[['Filename', 'Title', 'Artist', 'Location', 'Serie', 'Genre', 'Style', 'Tags']])):
        
        filename, title, artist, location, serie, genres, styles, tags = row
        
        image_file = os.path.join(IMAGES_DIR, filename)
        if not os.path.isfile(image_file):
            print("{} is not found".format(image_file))
            continue

        print("{}/{}".format(i + 1, n_paintings))
        labels = []

        ## Location
        if location:
            location = location.strip()
            location = replace_chars(location)
            location = location.lower()
            if location in WordDict.EXCLUDING_WORDS:
                location = "<REMOVED>"
            elif location in WordDict.INCLUDING_WORDS:
                pass
            elif location in WordDict.MAPPING_WORDS:
                location = WordDict.MAPPING_WORDS[location]
            else:
                locations = extract_words(location)
                location = " ".join(locations)
                labels.extend(location)
            print("\tLocation:", location)

        ## Serie
        if serie:
            serie = replace_chars(serie)
            serie = serie.lower()
            if serie in WordDict.EXCLUDING_WORDS:
                serie = "<REMOVED>"
            elif serie in WordDict.INCLUDING_WORDS:
                pass
            elif serie in WordDict.MAPPING_WORDS:
                serie = WordDict.MAPPING_WORDS[serie]
            else:
                series = extract_words(serie)
                serie = series
                labels.extend(serie)
            print("\tSerie:", serie)

        ## Genre
        if genres:
            genres = replace_chars(genres)
            genres = genres.lower()
            genres_now = []
            for genre in genres.split(','):
                genre = genre.strip()
                if genre in WordDict.EXCLUDING_WORDS:
                    genre = "<REMOVED>"
                    genres_now.append(genre)
                elif genre in WordDict.INCLUDING_WORDS:
                    genres_now.append(genre)
                elif genre in WordDict.MAPPING_WORDS:
                    genre = WordDict.MAPPING_WORDS[genre]
                    genres_now.extend(genre)
                else:
                    genres = extract_words(genre)
                    genre = " ".join(genres)
                    genres_now.append(genre)
            print("\tGenres:", genres_now)
            labels.extend(genres_now)

        ## Style
        if styles:
            styles = replace_chars(styles)
            styles = styles.lower()
            styles_now = []
            for style in styles.split(','):
                style = style.strip()
                if style in WordDict.EXCLUDING_WORDS:
                    style = "<REMOVED>"
                    styles_now.append(style)
                elif style in WordDict.INCLUDING_WORDS:
                    styles_now.append(style)
                elif style in WordDict.MAPPING_WORDS:
                    style = WordDict.MAPPING_WORDS[style]
                    styles_now.extend(style)
                else:
                    styles = extract_words(style)
                    style = " ".join(styles)
                    styles_now.append(style)
            print("\tStyles:", styles_now)
            labels.extend(styles_now)

        ## Tags
        if tags:
            tags = replace_chars(tags)
            tags = tags.lower()
            tags_org = tags
            tags_now = []
            for tag in tags.split(','):

                tag = tag.strip()

                if tag in WordDict.EXCLUDING_WORDS:
                    pass
                elif tag in WordDict.INCLUDING_WORDS:
                    tags_now.append(tag)
                elif tag in WordDict.MAPPING_WORDS:
                    tag = WordDict.MAPPING_WORDS[tag]
                    tags_now.extend(tag)
                else:
                    if '"' in tag:
                        parts = []
                        for i in tag.split('"'):
                            i = i.replace('-', ' ').strip()
                            if i != '':
                                parts.append(i)
                        tag = parts
                    elif '-and-' in tag:
                        tag = tag.split('-and-')
                        tag = list(map(lambda s: s.replace('-', ' '), tag))
                    elif '/' in tag:
                        tag = tag.split('/')
                    else:
                        tag = tag.replace('-', ' ')
                    tags_now.append(tag)
            print("\tTags:", tags_now)
            labels.extend(tags_now)

        # print('\t\tLabels:', labels)
        print("------")