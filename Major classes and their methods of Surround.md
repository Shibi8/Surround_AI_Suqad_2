### Classes and their Methods

Classes are used to create Objects.

Methods are a special kind of function that are defined within a class. Method cannot be called by its name only, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.


#### 1. class Stage(ABC):

    class Stage(ABC):
        
        def dump_output(self, surround_data, config):

The method is used to dump the output of each stage.
1. parameter surround_data is used to store intermediate data from each stage in the pipeline
2. surround_data must be an instance or child of the SurroundData class
3. parameter config is the Config of the pipeline
4. type config: <class 'surround.config.Config'>


        @abstractmethod
        def operate(self, surround_data, config):

A stage in a surround pipeline.
1. parameter surround_data is used to store intermediate data from each stage in the pipeline
2. surround_data must be an instance or child of the SurroundData class
3. the parameter config contains the settings for each stage
4. type config: <class 'surround.config.Config'>


        def init_stage(self, config):

This method is used to Initialise stage with some data
1. the parameter config contains the settings for each stage
2. type config: <class 'surround.config.Config'>


#### 2. class Surround(ABC):

    class Surround(ABC):

        def __init__(self, surround_stages=None, module=None):
            self.surround_stages = surround_stages

The collections module has some concrete classes that derive from ABCs; these can be further derived. In addition, the collections.abc submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, for example, is it hashable or a mapping.

Each abstract base class (ABC) in the collections module provides a common feature (or set of features) with the method functions that are required to implement that feature. In some cases, the features build on each other, and a number of method functions are required.

Since each of the ABC classes is abstract, they’re missing the implementation of one or more methods. To use these classes, you’ll have to provide the necessary methods.

One very important consequence of using the collections base classes is that it creates standardized names for the various features. This simplifies the assertions that might be required when checking the argument values to a function or method function.

Here, this method is used to carryout initialisation of the class and it can also be used to initialize objects of the class. An instance is created using surround_stages which is assigned to self.surround_stages.

            if module:
               # Module already imported and has a file attribute
               mod = sys.modules.get(module)
              if mod is not None and hasattr(mod, '__file__'):
                    package_path = os.path.dirname(os.path.abspath(mod.__file__))
                    root_path = os.path.dirname(package_path)
                else:
                    raise ValueError("Invalid Python module %s" % module)

                self.set_config(Config(root_path))

If the module has an attribute, the defined package path is called or accessed, and root_path is set to the package_path. Else, a ValueError is thrown with the message "Invalid Python module %s" % module.



#### 3. class Wrapper():

    class Wrapper():
        
        def __init__(self, surround, type_of_uploaded_object=None):
            self.surround = surround
            self.actual_type_of_uploaded_object = None
            
A wrapper class wraps an object which it then proxies unhandled calls. Wrapper functions can be used as an interface to adapt to the existing codes, to save from changing current codes back and forth. 


#### 4. class AllowedTypes(Enum):

    class AllowedTypes(Enum):
        JSON = ["application/json"]
        FILE = ["file"]
        
An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

Here, an Enum class `AllowedTypes` has been created which specifies the types, with attributes `JSON` and `FILE` called enumeration members. These members are constants. If we try and modify any of the members, we will get an error saying `AttributeError`.
