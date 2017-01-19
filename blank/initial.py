import os
import fileinput

def ask_model_name():
    model_name = input('Name of model?')
    return model_name

def detail_template_create(model_name):
    if not os.path.isdir('templates/{}/'.format(model_name)):
        os.makedirs('templates/{}/'.format(model_name))
    path = 'templates/{}/'.format(model_name)
    filename = '{}_detail.html'.format(model_name)
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write('<h2> {} detail page </h2>'.format(model_name))


def form_template_create(model_name):
    if not os.path.isdir('templates/{}/'.format(model_name)):
        os.makedirs('templates/{}/'.format(model_name))
    path = 'templates/{}/'.format(model_name)
    filename = '{}_form.html'.format(model_name)
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write("<h2> form page </h2>" + "\n" + '<form class="" method="post">'
        + "\n" + "{% csrf_token %}" + "\n" + "{{ form.as_p }}" + "\n" +
        '<input type="submit" value="submit"' + "\n" + "</form>")

def list_template_create(model_name):
    if not os.path.isdir('templates/{}/'.format(model_name)):
        os.makedirs('templates/{}/'.format(model_name))
    path = 'templates/{}/'.format(model_name)
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
        fields.append(item[0])
        if item[1] == 'string':
            item[1] = 'models.CharField(max_length=200)'
        elif item[1] == 'int':
            item[1] = 'models.IntegerField()'
        elif item[1] == 'boolean':
            item[1] = 'models.BooleanField()'
    return nested, fields



def model_add(model_name, details):
    app_name = input('App name? ')
    with open('{}/models.py'.format(app_name), 'a') as models_file:
        models_file.write('class {}(models.Model):'.format(model_name.title()) + '\n')
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

def generic_view_add(model_name, app_name, view):
    with open('{}/views.py'.format(app_name), 'a') as views_file:
        views_file.write('\nclass {}{}({}):'.format(model_name.title(), view, view) + '\n'
        + '\tmodel = {}'.format(model_name.title())+ '\n')

def create_view_add(model_name, app_name, model_fields, view):
    with open('{}/views.py'.format(app_name), 'a') as views_file:
        views_file.write('\nclass {}{}({}):'.format(model_name.title(), view, view) + '\n'
        + '\tmodel = {}'.format(model_name.title())+ '\n'
        + '\tfields = ({})'.format([str(x) for x in model_fields]) + '\n'
        + '\tdef form_valid(self,form):' + '\n'
        + '\t\tinstance = form.save(commit=False)' + '\n'
        + '\t\treturn super().form_valid(form)' + '\n'
        + '\tdef get_success_url(self):' + '\n'
        + '\t\treturn "/"')

def view_add(model_name, details, model_fields):
    app_name = input('App name? ')
    with open('{}/views.py'.format(app_name), 'a') as views_file:
        for view in details:
            if view == 'DetailView' or view == 'ListView':
                generic_view_add(model_name, app_name, view)
            else:
                create_view_add(model_name, app_name, model_fields, view)

def total():
    model = ask_model_name()
    choices = ask_views()
    if 'DetailView' in choices:
        detail_template_create(model)
    if 'CreateView' in choices:
        form_template_create(model)
    if 'ListView' in choices:
        list_template_create(model)
    model_details = ask_model_fields()
    for_models = model_details[0]
    for_views = model_details[1]
    model_add(model, for_models)
    view_add(model, choices, for_views)
    proj = project_name()
    detail_url_adder(model, proj)
    create_url_adder(model, proj)
    list_url_adder(model, proj)


def project_name():
    proj = input('Proj name? ')
    return proj

def detail_url_adder(model_name, project):
    f = open('{}/urls.py'.format(project), 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].endswith(')\n'):
            lines[i] = lines[i].replace('\n', ',\n')
        if lines[i].endswith(']\n'):
            lines.insert(i,"""\turl(r'^{}/(?P<pk>\d+)$', {}DetailView.as_view(), name="{}_detail_view")
            """.format(model_name,model_name.title(),model_name))
    l = open('{}/urls.py'.format(project), 'w')
    for line in lines:
        l.write(line)


def create_url_adder(model_name, project):
    f = open('{}/urls.py'.format(project), 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].endswith(')\n'):
            lines[i] = lines[i].replace('\n', ',\n')
        if lines[i].endswith(']\n'):
            lines.insert(i,"""\turl(r'^{}/new/$', {}CreateView.as_view(), name="{}_create_view")
            """.format(model_name,model_name.title(),model_name))
    l = open('{}/urls.py'.format(project), 'w')
    for line in lines:
        l.write(line)

def list_url_adder(model_name, project):
    f = open('{}/urls.py'.format(project), 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].endswith(')\n'):
            lines[i] = lines[i].replace('\n', ',\n')
        if lines[i].endswith(']\n'):
            lines.insert(i,"""\turl(r'^{}s/$', {}ListView.as_view(), name="{}_list_view")
            """.format(model_name,model_name.title(),model_name))
    l = open('{}/urls.py'.format(project), 'w')
    for line in lines:
        l.write(line)

total()
