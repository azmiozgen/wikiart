class CharDict:

    PUNCTUATION_REPLACEMENT_DICT = {'_' : ' ',
                                    '#' : '',
                                    u'\xa0' : u' ',
                               }     ## Incomplete
    LETTER_REPLACEMENTS_DICT = {'á' : 'a',
                                'à' : 'a',
                                'ā' : 'a',
                                'ă' : 'a',
                                'Ă' : 'A',
                                'Ā' : 'A',
                                'â' : 'a',
                                'ã' : 'a',
                                'ä' : 'a',
                                'å' : 'a',
                                'é' : 'e',
                                'è' : 'e',
                                'É' : 'E',
                                'ò' : 'o',
                                'ó' : 'o',
                                'ô' : 'o',
                                'ō' : 'o',
                                'ù' : 'u',
                                'ú' : 'u',
                                'ý' : 'y',
                                'ç' : 'c',
                                'Ç' : 'C',
                                'ğ' : 'g',
                                'Ğ' : 'G',
                                'ı' : 'i',
                                'İ' : 'I',
                                'ï' : 'i',
                                'î' : 'i',
                                'ş' : 's',
                                'Ş' : 'S',
                                'ö' : 'o',
                                'Ö' : 'O',
                                'ü' : 'u',
                                'Ü' : 'U',
                                'Т' : 'T',
                                'œ' : 'oe',
                                }          ## Incomplete