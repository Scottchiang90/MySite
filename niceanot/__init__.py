import os
import markovify

from mysite.settings import BASE_DIR

site_title = 'Eh Nice A Not?'

with open(os.path.join(BASE_DIR, 'model.json'), 'r') as model_json:
    reconstituted_model = markovify.Text.from_json(model_json.read())
