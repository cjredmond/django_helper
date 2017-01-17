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
        temp_file.write("<h2> {} list page <h2>".format(model_name) + "\n" +
        "{% for object in object_list %}" + "\n" +
        "<a href='#'>" + "\n" + "{% endfor %}")

def ask_model_fields():
    fields = []
    answer = input("write field names and types: ").replace(' ','')
    chopped = answer.split(',')
    nested = [i.split(':') for i in chopped]

    for item in nested:
        if item[1] == 'string':
            item[1] = 'models.CharField(max_length=200)'
        elif item[1] == 'int':
            item[1] = 'models.IntegerField()'
        elif item[1] == 'boolean':
            item[1] = 'models.BooleanField()'
    return nested

def model_add(model_name, details):
    with open('dummy_models.py', 'a') as models_file:
        models_file.write('class {}():'.format(model_name.title()) + '\n')
        for field in details:
            models_file.write('\t{} = {}\n'.format(field[0],field[1]))

def ask_views():
    answer = []
    detail = input('Do you want a detail view? Y/n :')
    listv = input('Do you want a list view? Y/n :')
    create_v = input('Do you want a create view? Y/n :')
    if detail != "n":
        answer.append('DetailView')
    if listv != "n":
        answer.append('ListView')
    if create_v != "n":
        answer.append('CreateView')
    return answer

def view_add(model_name, details):
    with open('dummy_views.py', 'a') as views_file:
        for view in details:
            views_file.write('\nclass {}{}():'.format(model_name.title(), view) + '\n'
            + '\tmodel = {}'.format(model_name.title())+ '\n')


model = ask_model_name()
choices = ask_views()

if 'DetailView' in choices:
    detail_template_create(model)
if 'CreateView' in choices:
    form_template_create(model)
if 'ListView' in choices:
    list_view_create(model)

model_add(model, ask_model_fields())
view_add(model, choices)
