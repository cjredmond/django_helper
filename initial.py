import os

def ask_model_name():
    model_name = input('Name of model?')
    return model_name

def detail_template_create(model_name):
    if not os.path.isdir('dummy_templates/{}/'.format(model_name)):
        os.makedirs('dummy_templates/{}/'.format(model_name))
    path = 'dummy_templates/{}/'.format(model_name)
    filename = '{}_detail.html'.format(model_name)
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write('<h2> {} detail page </h2>'.format(model_name))


def form_template_create(model_name):
    if not os.path.isdir('dummy_templates/{}/'.format(model_name)):
        os.makedirs('dummy_templates/{}/'.format(model_name))
    path = 'dummy_templates/{}/'.format(model_name)
    filename = '{}_form.html'.format(model_name)
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write("<h2> form page </h2>" + "\n" + '<form class="" method="post">'
        + "\n" + "{% csrf_token %}" + "\n" + "{{ form.as_p }}" + "\n" +
        '<input type="submit" value="submit"' + "\n" + "</form>")

def list_view_create(model_name):
    if not os.path.isdir('dummy_templates/{}/'.format(model_name)):
        os.makedirs('dummy_templates/{}/'.format(model_name))
    path = 'dummy_templates/{}/'.format(model_name)
    filename = '{}_list.html'.format(model_name)
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write("<h2> {} list page".format(model_name) + "\n" +
        "{% for object in object_list %}" + "\n" +
        "<a href='#'>" + "\n" + "{% endfor %}")

choice = ask_model_name()
detail_template_create(choice)
form_template_create(choice)
list_view_create(choice)

with open('dummy_models.py') as models_file:
    pass
