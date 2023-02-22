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
c.execute('''CREATE TABLE words (page_number integer, line_number integer, word text, bounding_box text)''')

    
dir_name = 'quranlines'

# loop through pages
for p in range(1, 604):

    page_number = p

    # loop through lines
    for l in range(1, 15):
            
        line_number = l

        # get image file name
        file_name = dir_name + '/' + str(page_number) + '/' + str(line_number) + '.png'

        # detect text
        texts = detect_text(file_name)

        # get text
        text = texts[0].description

        # print text
        print(text)

        # save text

        


