from textx.metamodel import metamodel_from_file
from textx.export import model_export
from textx.export import metamodel_export

hello_meta = metamodel_from_file('./hello.tx')

#export to a file for visualizing
metamodel_export(hello_meta, './hello_meta.dot')

#instantiate a HelloWorld object
example_hello_model = hello_meta.model_from_file('./example1.hello')

#visualize an instantiated model
model_export(example_hello_model, './example1.dot')

#use an instantiated model
greeting_list = example_hello_model.to_greet[0].name
#print "We are Greeting: {0}".format(",".join(example_hello_model.to_greet))
for greetee in example_hello_model.to_greet:
    print "Hello, {0}!".format(greetee.name.rstrip())



