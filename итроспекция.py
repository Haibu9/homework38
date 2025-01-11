import inspect

def introspection_info(obj):
    attributes = []
    methods = []
    for i in dir(obj):
        if i[0] == '_':
            methods.append(i)
        else:
            attributes.append(i)

    try:
        module = str(inspect.getmodule(obj)).split()[1]
    except:
        module = '__main__'

    return {'type': type(obj), 'attributes': attributes, 'methods': methods, 'module': module}


number_info = introspection_info(42)
print(number_info)
