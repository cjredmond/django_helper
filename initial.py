import os

model_name = input('Name of model?')


filename = '{}_detail.html'.format(model_name)
os.makedirs('dummy_templates/{}/'.format(model_name))
path = 'dummy_templates/{}'.format(model_name)

with open(os.path.join(path, filename), 'w') as temp_file:
    temp_file.write('<h2> {} detail page </h2>'.format(model_name))

filename = '{}_form.html'.format(model_name)
with open(os.path.join(path, filename), 'w') as temp_file:
    temp_file.write("""<h2> form page </h2> \n <form class="" method="post">\n
    {% csrf_token %} \n {{ form.as_p }} \n <input type="submit" value="submit" \n
    </form> """)
