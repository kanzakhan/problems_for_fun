'''
JSON Serializer

JSON is a format that encodes objects in a string. Serialization means to 
convert an object into that string, and deserialization is its inverse operation
(convert string -> object).

When transmitting data or storing them in a file, the data are required to be 
byte strings, but complex objects are seldom in this format. Serialization can
convert these complex objects into byte strings for such use. After the byte 
strings are transmitted, the receiver will have to recover the original object
from the byte string. This is known as deserialization.

Valid Data Types:
1. In JSON, values must be one of the following data types:
    - a string
    - a number
    - an object (JSON object)
    - an array
    - a boolean - true or false
    - null

2. JSON values cannot be one of the following data types:
    - a function
    - a date
    - undefined

Say, you have an object:

                    {foo: [1, 4, 7, 10], bar: "baz"}

serializing into JSON will convert it into a string:

                    '{"foo":[1,4,7,10],"bar":"baz"}'

which can be stored or sent through wire to anywhere. The receiver can then 
deserialize this string to get back the original object:

                    {foo: [1, 4, 7, 10], bar: "baz"}.

TODO LATER: Add a JSON Deserializer
'''

def flattened_json(json_obj):
    '''
    This method takes in a json and flattens it so that it is not nested
    input: json object (aka python dict), assumes keys for the input are immutable
    output: json object (aka python dict), flattened
    '''
    output = {}

    def flatten(obj, name = ''):
        '''
        Helper method to recursively flatten nested object
        '''
        if type(obj) is dict:
            for key in obj:
                flatten(obj[key], name + key + '_')
        elif type(obj) is list:
            for i,element in enumerate(obj):
                flatten(element, name + str(i) + '_')
        else:
            output[name[:-1]] = obj

    flatten(json_obj)
    return output

def serialize_json(json_obj):
    '''
    This method takes in any object then serializes it in the JSON format
    input: object - can be anything
    output: string - encodes the object
    '''
    output = []

    # edge cases
    if not json_obj:
        if type(json_obj) is dict:
            return stringify_array(['{', '}'])
        elif type(json_obj) is list:
            return stringify_array(['[', ']'])
        elif type(json_obj) is None:
            return stringify_array(['null'])

    def serialize(obj):
        '''
        Helper method to recursively serialize nested object
        '''
        # if obj is dict, add each key to output, then recurse over value of key
        if type(obj) is dict:
            output.append('{')
            for i,key in enumerate(obj):
                # add the '"key":' to output
                output.append('"{}":'.format(key))
                serialize(obj[key])
                if i != len(obj) - 1:
                    output.append(',')
            output.append('}')

        # obj is list or tuple, iterate over elements and add each one
        elif type(obj) is list or type(obj) is tuple:
            output.append('[') if type(obj) is list else output.append('(')
            for i,element in enumerate(obj):
                serialize(element)
                if i != len(obj) - 1:
                    output.append(',')
            output.append(']') if type(obj) is list else output.append(')')
        
        # base case: obj is boolean, string, num, float, or None
        else:
            if type(obj) is str:
                output.append('"{}"'.format(obj))
            elif type(obj) is None:
                output.append('null')
            elif type(obj) is bool:
                output.append(str(obj).lower())
            else:
                output.append(obj)
    
    # flatten it
    serialize(json_obj)
    return stringify_array(output)

def stringify_array(input_arr):
    '''
    This is a helper method that takes in an input array and outputs a string
    that has all the elements concatenated.
    input: list of any type of element
    output: string
    '''
    return "".join(map(str,input_arr))

# ----------------------------- Test Cases: ------------------------------------
json1 = {}

json2 = []

json3 = {
    "key1": [1,2,3],
    "key2": (4,5,6),
    "key3": 999,
    "key4": "testing",
    "key5": None
}

json4 = {
    "age": 45,
    "cars": [ {
        "model": "Audi A1", 
        "mpg": 15.1
    },
    {
        "model": "Zeep Compass", 
        "mpg": 18.1
    }
    ],
    "children": [ "Alice",
		  "Bob"
	],
    "married": True,
    "name": "Ken",
    "pets": [ 
		"Dog"
	]
}
print(serialize_json(json1))
print(serialize_json(json2))
print(serialize_json(json3))
print(serialize_json(json4))

# Test stringify
arr = ['{', '"key1":', '[', 1, ',', 2, ',', 3, ']', ',', '"key2":', 5, '}']
print(stringify_array(arr))