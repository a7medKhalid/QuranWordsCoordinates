def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts
    # print('Texts:')

    # for text in texts:
    #     print('\n"{}"'.format(text.description))

    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

    #     print('bounds: {}'.format(','.join(vertices)))


# prepare sqlite database
import sqlite3
conn = sqlite3.connect('quranlines.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS words (page_number integer, line_number integer, word text, bound1 text, bound2 text, bound3 text, bound4 text, error boolean)''')

    
dir_name = 'quranlines'

# loop through pages
for p in range(1, 604):

    page_number = p

    # https://api.quran.com/api/v4/verses/by_page/1?language=en&words=true&page=232&per_page=10

    # get expected line words count from quran.com
    import requests
    url = 'https://api.quran.com/api/v4/verses/by_page/'+ str(page_number) + '?language=en&words=true'
    r = requests.get(url)
    data = r.json()
    verses = data['verses']
    lines = []

    # CP:numbers of lines in a page is not always the same 
    line_counter = verses[0]['words'][0]['line_number']
    print(line_counter)
    for verse in verses:
        words = verse['words']
        line_words = []
        for word in words:

            if word['line_number'] > line_counter:
                lines.append(line_words)
                line_words = []
                line_counter += 1
            
            line_words.append(word)

    print(lines)
    print(len(lines))
    # exit application
    exit()





    # loop through lines
    for l in range(1, 15):
            
        line_number = l

        # get image file name
        file_name = dir_name + '/' + str(page_number) + '/' + str(line_number) + '.png'

        # detect text
        texts = detect_text(file_name)

        




        # save text


        


