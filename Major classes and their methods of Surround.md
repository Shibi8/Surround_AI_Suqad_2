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

The collecions module has some concrete classes that derive from ABCs; these can be further derived. In addition, the collections.abc submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, for example, is it hashable or a mapping.

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

                    if not os.path.exists(self.config["output_path"]):
                    os.makedirs(self.config["output_path"])
            else:
                self.set_config(Config())

        def set_config(self, config):
           if not config or not isinstance(config, Config):
                raise TypeError("config should be of class Config")
            self.config = config
            if self.config["surround"]["stages"]:
                self.surround_stages = []
                result = self.config.get_path(self.config["surround"]["stages"])
                if not isinstance(result, list):
                    result = [result]
                for stage in filter(None, result):
                    parts = stage.split(".")
                    module = import_module("." + parts[-2], ".".join(parts[:-2]))
                    klass = getattr(module, parts[-1])
                    self.surround_stages.append(klass())

        def _execute_stage(self, stage, stage_data):
            stage_start = datetime.now()
            stage.operate(stage_data, self.config)

            if self.config["surround"]["enable_stage_output_dump"]:
                stage.dump_output(stage_data, self.config)

            # Calculate and log stage duration
            stage_execution_time = datetime.now() - stage_start
            stage_data.stage_metadata.append({type(stage).__name__: str(stage_execution_time)})
            LOGGER.info("Stage %s took %s secs", type(stage).__name__, stage_execution_time)

        def init_stages(self):
            for stage in self.surround_stages:
                stage.init_stage(self.config)

        def process(self, surround_data):
            assert isinstance(surround_data, SurroundData), \
                "Input must be a SurroundData object or inherit from SurroundData"

            surround_data.freeze()
            start_time = datetime.now()

            try:
                for stage in self.surround_stages:
                    assert isinstance(stage, Stage), \
                        "A stage must be an instance of the Stage class"
                    self._execute_stage(stage, surround_data)
                    if surround_data.errors:
                        LOGGER.error("Error during processing")
                        LOGGER.error(surround_data.errors)
                        break
                execution_time = datetime.now() - start_time
                surround_data.execution_time = str(execution_time)
                LOGGER.info("Surround took %s secs", execution_time)
            except Exception:
                LOGGER.exception("Failed processing Surround")

            surround_data.thaw()



#### 3. class Wrapper():

A wrapper class wraps an object which it then proxies unhandled calls. Wrapper functions can be used as an interface to adapt to the existing codes, to save from changing current codes back and forth. 

    class Wrapper():
        
        def __init__(self, surround, type_of_uploaded_object=None):
            self.surround = surround
            self.actual_type_of_uploaded_object = None
            if type_of_uploaded_object:
                self.type_of_uploaded_object = type_of_uploaded_object
            else:
                self.type_of_uploaded_object = AllowedTypes.JSON
            self.surround.init_stages()

        def run(self, input_data):
            if self.validate() is False:
                sys.exit()

        def validate(self):
            return self.validate_type_of_uploaded_object()
            # TODO: Find a way to validate_actual_type_of_uploaded_object(), probably using mime type # pylint: disable=fixme

        def validate_actual_type_of_uploaded_object(self):
            for type_ in self.type_of_uploaded_object.value:
                if self.actual_type_of_uploaded_object == type_:
                    return True
            print("error: you selected input type as " + str(self.type_of_uploaded_object).split(".")[1])
            print("error: input file is not " + str(self.type_of_uploaded_object).split(".")[1])
            return False

        def validate_type_of_uploaded_object(self):
            for type_ in AllowedTypes:
                if self.type_of_uploaded_object == type_:
                    return True
            LOGGER.info("error: selected upload type not allowed")
            LOGGER.info("Choose from: ")
            for type_ in AllowedTypes:
                LOGGER.info(type_)
            return False

        def process(self, input_data):
            Wrapper.run(self, input_data)
            return self.run(input_data)

        def get_config(self):
            return self.surround.config


#### 4. class AllowedTypes(Enum):

    class AllowedTypes(Enum):
        JSON = ["application/json"]
        FILE = ["file"]
        
An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

Here, an Enum class `AllowedTypes` has been created which specifies the types, with attributes `JSON` and `FILE` called enumeration members. These members are constants. If we try and modify any of the members, we will get an error saying `AttributeError`.
