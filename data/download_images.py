import glob
import json
import os
import time

import imghdr
import requests

if __name__ == "__main__":

    INPUT_JSONS_DIR = "./meta/"
    OUTPUT_IMAGES_DIR = "./images/"
    os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)
    OUTPUT_LABELS_FILE = "./metadata.txt"
    OUTPUT_LABELS_HEADER = "Filename|Title|Artist|Year|Location|Serie|Genre|Style|Tags|Image_url\n"
    if os.path.isfile(OUTPUT_LABELS_FILE):
        print("{} exists. Exiting.".format(OUTPUT_LABELS_FILE))
        exit()
    else:        
        fp = open(OUTPUT_LABELS_FILE, 'a')
        fp.write(OUTPUT_LABELS_HEADER)

    INDEX_STR_LENGTH = 7
    DELIMITER = '|'
    
    json_files = glob.glob(os.path.join(INPUT_JSONS_DIR, '*json'))
    print("# of json_files (# of painters):", len(json_files))
    time.sleep(1)

    index = 1
    for json_file in json_files:

        if os.path.basename(json_file) == 'artists.json':
            continue

        with open(json_file, 'r') as f:
            json_obj = json.load(f)

        print(json_file)
        print("\t# of arts:", len(json_obj))

        for art in json_obj:
            index_str = str(index).zfill(INDEX_STR_LENGTH)
            image_name_wo_ext = index_str

            ## Download all only with non-empty tags
            if art.get('tags'):
                image_large_url = art.get('image')        ## Smaller than alt version
                image_alt_url = image_large_url.split('!')[0]   ## Original larger version
                image_url_candidates = [image_large_url, image_alt_url]

                for image_url_candidate in image_url_candidates:
                    # try:
                    image_file = os.path.join(OUTPUT_IMAGES_DIR, image_name_wo_ext)
                    with open(image_file, 'wb') as f:
                        f.write(requests.get(image_url_candidate).content)
                    ext = imghdr.what(image_file)
                    print(image_url_candidate, ext)
                    if ext:
                        image_name = image_name_wo_ext + '.' + ext 
                    else:
                        continue    ## Image url could not be downloaded

                    image_file_w_ext = os.path.join(OUTPUT_IMAGES_DIR, image_name)
                    os.rename(image_file, image_file_w_ext)
                    image_file = image_file_w_ext
                    print("\t{} saved.".format(image_file))
                    image_used_url = image_url_candidate
                    index += 1
                    break
                    # except Exception as e:
                    #     print("\t{}. Passing".format(e))
                    #     continue
                else:
                    continue

                title = art.get('title')
                artist = art.get('artistName')
                year = art.get('yearAsString')
                location = art.get('location')
                serie = art.get('serie')
                genre = art.get('genre')
                style = art.get('style')
                tags = art.get('tags')
                image_url = image_used_url

                row_str = ""
                row_elements = [image_name, title, artist, year, location, serie, genre, style, tags, image_url]
                for row_element in row_elements:
                    if row_element:
                        row_str += row_element + DELIMITER
                    else:
                        row_str += DELIMITER
                row_str = row_str.strip().strip(DELIMITER) + '\n'
                # print(row_str)
                fp.write(row_str)
    fp.close()
