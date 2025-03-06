'''~/lx/lx14/public/py/groqq.py'''

'''
Sends a request to groq using groq package.

Demo:
. gemini2.bash
pip install groq
python groqq.py
python groqq.py /tmp/prompt.txt 
python groqq.py /tmp/prompt.txt gemma2-9b-it
python groqq.py /tmp/prompt.txt llama-3.2-1b-preview
python groqq.py /tmp/prompt.txt llama-3.2-3b-preview
python groqq.py /tmp/prompt.txt llama-3.1-8b-instant
python groqq.py /tmp/prompt.txt llama3-8b-8192
python groqq.py /tmp/prompt.txt llama-3.3-70b-specdec
python groqq.py /tmp/prompt.txt llama-3.3-70b-versatile
python groqq.py /tmp/prompt.txt deepseek-r1-distill-llama-70b
'''

import datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import requests, groq

from groq import Groq

myts = str(datetime.datetime.now()).replace(' ','_')

llm_s_l = ['gemma2-9b-it', 'llama3-8b-8192', 'llama-3.3-70b-specdec', 'mixtral-8x7b-32768']

if len(sys.argv) > 1:
    promptfn_s = os.path.expanduser(sys.argv[1])
else:
    promptfn_s = os.path.expanduser('~/prompt.txt')

if len(sys.argv) > 2:
    model_s = sys.argv[2]
else:
    model_s = 'gemma2-9b-it'

with open(os.path.expanduser(promptfn_s), 'r') as pf:
    prompt_s = pf.read()
if prompt_s == '':
    prompt_s = 'a'

charlim_i = int(15000 * 1.5)

def groq1(prompt_s, model_s):
    # Initialize the Groq client
    client = Groq(
        api_key=os.environ["GROQ_API_KEY"]
    )
    # Create a chat completion with a limited context:
    charlim_i = int(15000 * 1.5)
    max_retries = 3
    retry_delay = 0  # initial delay
    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system",
                     "content": "You are terse but, you answer in full simple sentences which are helpful, informative, and complete."
                     },
                    {"role": "user", "content": prompt_s[:charlim_i] }
                ], model=model_s 
            )
            return chat_completion
        except groq.RateLimitError as e:
            time.sleep(2)
            return f'groq.RateLimitError as e: {str(e)}'



groq1_l = groq1(prompt_s, model_s)
chat_completion = groq1_l[0]
prompt_s = groq1_l[1]

'''
# groq_models.txt
gemma2-9b-it
llama-3.1-8b-instant
llama3-8b-8192
# 
expensive:
llama3-70b-8192
llama-3.3-70b-specdec
llama-3.3-70b-versatile
deepseek-r1-distill-llama-70b
'''

print(chat_completion.choices[0].message.content)

str_token_ratio_f = len(prompt_s[:charlim_i]) / chat_completion.usage.total_tokens

groq_usage_info_s = f'{datetime.datetime.now()}\n{chat_completion.usage}\nstr_token_ratio_f is {str_token_ratio_f} [approx num of chars per token]'

with open('/tmp/groq_usage_info.txt','w') as gf:
    gf.write(f'{groq_usage_info_s}\nPrompt:\n{prompt_s[:charlim_i]}\nchat_completion.choices[0].message.content:\n{chat_completion.choices[0].message.content}')

'done'


'''
>>>
print(chat_completion)

ChatCompletion(id='chatcmpl-948da1eb-296e-4df0-9df8-a5f519dd834a',
choices=[Choice(finish_reason='stop', index=0, logprobs=None,
message=ChatCompletionMessage(content='Hello!  \n\n',
role='assistant', function_call=None, reasoning=None,
tool_calls=None))], created=1741037788, model='gemma2-9b-it',
object='chat.completion', system_fingerprint='fp_10c08bf97d',
usage=CompletionUsage(completion_tokens=7, prompt_tokens=30,
total_tokens=37, completion_time=0.012727273, prompt_time=0.002307576,
queue_time=0.017778152000000002, total_time=0.015034849),
x_groq={'id': 'req_01jnez0pyhf9nv4szc8jz73brj'})

>>>

>>> print(chat_completion.usage)

CompletionUsage(completion_tokens=7, prompt_tokens=30,
total_tokens=37, completion_time=0.012727273, prompt_time=0.002307576,
queue_time=0.017778152000000002, total_time=0.015034849)

>>> print(chat_completion.usage.total_tokens)
37
>>> 

>>> help(chat_completion)
Help on ChatCompletion in module groq.types.chat.chat_completion object:

class ChatCompletion(groq.BaseModel)
 |  ChatCompletion(**data: 'Any') -> 'None'
 |
 |  Method resolution order:
 |      ChatCompletion
 |      groq.BaseModel
 |      pydantic.main.BaseModel
 |      builtins.object
 |
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  __annotations__ = {'choices': typing.List[groq.types.chat.chat_complet...
 |
 |  __class_vars__ = set()
 |
 |  __private_attributes__ = {}
 |
 |  __pydantic_complete__ = True
 |
 |  __pydantic_computed_fields__ = {}
 |
 |  __pydantic_core_schema__ = {'cls': <class 'groq.types.chat.chat_comple...
 |
 |  __pydantic_custom_init__ = False
 |
 |  __pydantic_decorators__ = DecoratorInfos(validators={}, field_validato...
 |
 |  __pydantic_fields__ = {'choices': FieldInfo(annotation=List[Choice], r...
 |
 |  __pydantic_generic_metadata__ = {'args': (), 'origin': None, 'paramete...
 |
 |  __pydantic_parent_namespace__ = None
 |
 |  __pydantic_post_init__ = None
 |
 |  __pydantic_serializer__ = SchemaSerializer(serializer=Model(
 |      Model...
 |
 |  __pydantic_validator__ = SchemaValidator(title="ChatCompletion", valid...
 |
 |  model_config = {'defer_build': True, 'extra': 'allow'}
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from groq.BaseModel:
 |
 |  __str__(self) -> 'str'
 |      Return str(self).
 |
 |  to_dict(self, *, mode: "Literal['json', 'python']" = 'python', use_api_names: 'bool' = True, exclude_unset: 'bool' = True, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, warnings: 'bool' = True) -> 'dict[str, object]'
 |      Recursively generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
 |
 |      By default, fields that were not set by the API will not be included,
 |      and keys will match the API response, *not* the property names from the model.
 |
 |      For example, if the API responds with `"fooBar": true` but we've defined a `foo_bar: bool` property,
 |      the output will use the `"fooBar"` key (unless `use_api_names=False` is passed).
 |
 |      Args:
 |          mode:
 |              If mode is 'json', the dictionary will only contain JSON serializable types. e.g. `datetime` will be turned into a string, `"2024-3-22T18:11:19.117000Z"`.
 |              If mode is 'python', the dictionary may contain any Python objects. e.g. `datetime(2024, 3, 22)`
 |
 |          use_api_names: Whether to use the key that the API responded with or the property name. Defaults to `True`.
 |          exclude_unset: Whether to exclude fields that have not been explicitly set.
 |          exclude_defaults: Whether to exclude fields that are set to their default value from the output.
 |          exclude_none: Whether to exclude fields that have a value of `None` from the output.
 |          warnings: Whether to log warnings when invalid fields are encountered. This is only supported in Pydantic v2.
 |
 |  to_json(self, *, indent: 'int | None' = 2, use_api_names: 'bool' = True, exclude_unset: 'bool' = True, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, warnings: 'bool' = True) -> 'str'
 |      Generates a JSON string representing this model as it would be received from or sent to the API (but with indentation).
 |
 |      By default, fields that were not set by the API will not be included,
 |      and keys will match the API response, *not* the property names from the model.
 |
 |      For example, if the API responds with `"fooBar": true` but we've defined a `foo_bar: bool` property,
 |      the output will use the `"fooBar"` key (unless `use_api_names=False` is passed).
 |
 |      Args:
 |          indent: Indentation to use in the JSON output. If `None` is passed, the output will be compact. Defaults to `2`
 |          use_api_names: Whether to use the key that the API responded with or the property name. Defaults to `True`.
 |          exclude_unset: Whether to exclude fields that have not been explicitly set.
 |          exclude_defaults: Whether to exclude fields that have the default value.
 |          exclude_none: Whether to exclude fields that have a value of `None`.
 |          warnings: Whether to show any warnings that occurred during serialization. This is only supported in Pydantic v2.
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from groq.BaseModel:
 |
 |  construct(_fields_set: 'set[str] | None' = None, **values: 'object') -> 'ModelT' from pydantic._internal._model_construction.ModelMetaclass
 |      # Override the 'construct' method in a way that supports recursive parsing without validation.
 |      # Based on https://github.com/samuelcolvin/pydantic/issues/1168#issuecomment-817742836.
 |
 |  model_construct = construct(_fields_set: 'set[str] | None' = None, **values: 'object') -> 'ModelT' from pydantic._internal._model_construction.ModelMetaclass
 |      # Override the 'construct' method in a way that supports recursive parsing without validation.
 |      # Based on https://github.com/samuelcolvin/pydantic/issues/1168#issuecomment-817742836.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from groq.BaseModel:
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from pydantic.main.BaseModel:
 |
 |  __copy__(self) -> 'Self'
 |      Returns a shallow copy of the model.
 |
 |  __deepcopy__(self, memo: 'dict[int, Any] | None' = None) -> 'Self'
 |      Returns a deep copy of the model.
 |
 |  __delattr__(self, item: 'str') -> 'Any'
 |      Implement delattr(self, name).
 |
 |  __eq__(self, other: 'Any') -> 'bool'
 |      Return self==value.
 |
 |  __getattr__(self, item: 'str') -> 'Any'
 |
 |  __getstate__(self) -> 'dict[Any, Any]'
 |      Helper for pickle.
 |
 |  __init__(self, /, **data: 'Any') -> 'None'
 |      Create a new model by parsing and validating input data from keyword arguments.
 |
 |      Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
 |      validated to form a valid model.
 |
 |      `self` is explicitly positional-only to allow `self` as a field name.
 |
 |  __iter__(self) -> 'TupleGenerator'
 |      So `dict(model)` works.
 |
 |  __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'
 |      Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.
 |
 |  __replace__(self, **changes: 'Any') -> 'Self'
 |      # Because we make use of `@dataclass_transform()`, `__replace__` is already synthesized by
 |      # type checkers, so we define the implementation in this `if not TYPE_CHECKING:` block:
 |
 |  __repr__(self) -> 'str'
 |      Return repr(self).
 |
 |  __repr_args__(self) -> '_repr.ReprArgs'
 |
 |  __repr_name__(self) -> 'str'
 |      Name of the instance's class, used in __repr__.
 |
 |  __repr_recursion__(self, object: 'Any') -> 'str'
 |      Returns the string representation of a recursive object.
 |
 |  __repr_str__(self, join_str: 'str') -> 'str'
 |
 |  __rich_repr__(self) -> 'RichReprResult'
 |      Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.
 |
 |  __setattr__(self, name: 'str', value: 'Any') -> 'None'
 |      Implement setattr(self, name, value).
 |
 |  __setstate__(self, state: 'dict[Any, Any]') -> 'None'
 |
 |  copy(self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'
 |      Returns a copy of the model.
 |
 |      !!! warning "Deprecated"
 |          This method is now deprecated; use `model_copy` instead.
 |
 |      If you need `include` or `exclude`, use:
 |
 |      ```python {test="skip" lint="skip"}
 |      data = self.model_dump(include=include, exclude=exclude, round_trip=True)
 |      data = {**data, **(update or {})}
 |      copied = self.model_validate(data)
 |      ```
 |
 |      Args:
 |          include: Optional set or mapping specifying which fields to include in the copied model.
 |          exclude: Optional set or mapping specifying which fields to exclude in the copied model.
 |          update: Optional dictionary of field-value pairs to override field values in the copied model.
 |          deep: If True, the values of fields that are Pydantic models will be deep-copied.
 |
 |      Returns:
 |          A copy of the model with included, excluded and updated fields as specified.
 |
 |  dict(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'
 |
 |  json(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'
 |
 |  model_copy(self, *, update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'
 |      Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#model_copy
 |
 |      Returns a copy of the model.
 |
 |      Args:
 |          update: Values to change/add in the new model. Note: the data is not validated
 |              before creating the new model. You should trust this data.
 |          deep: Set to `True` to make a deep copy of the model.
 |
 |      Returns:
 |          New model instance.
 |
 |  model_dump(self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'
 |      Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump
 |
 |      Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
 |
 |      Args:
 |          mode: The mode in which `to_python` should run.
 |              If mode is 'json', the output will only contain JSON serializable types.
 |              If mode is 'python', the output may contain non-JSON-serializable Python objects.
 |          include: A set of fields to include in the output.
 |          exclude: A set of fields to exclude from the output.
 |          context: Additional context to pass to the serializer.
 |          by_alias: Whether to use the field's alias in the dictionary key if defined.
 |          exclude_unset: Whether to exclude fields that have not been explicitly set.
 |          exclude_defaults: Whether to exclude fields that are set to their default value.
 |          exclude_none: Whether to exclude fields that have a value of `None`.
 |          round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
 |          warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
 |              "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
 |          serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
 |
 |      Returns:
 |          A dictionary representation of the model.
 |
 |  model_dump_json(self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'
 |      Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json
 |
 |      Generates a JSON representation of the model using Pydantic's `to_json` method.
 |
 |      Args:
 |          indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
 |          include: Field(s) to include in the JSON output.
 |          exclude: Field(s) to exclude from the JSON output.
 |          context: Additional context to pass to the serializer.
 |          by_alias: Whether to serialize using field aliases.
 |          exclude_unset: Whether to exclude fields that have not been explicitly set.
 |          exclude_defaults: Whether to exclude fields that are set to their default value.
 |          exclude_none: Whether to exclude fields that have a value of `None`.
 |          round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
 |          warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
 |              "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
 |          serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
 |
 |      Returns:
 |          A JSON string representation of the model.
 |
 |  model_post_init(self, _BaseModel__context: 'Any') -> 'None'
 |      Override this method to perform additional initialization after `__init__` and `model_construct`.
 |      This is useful if you want to do some validation that requires the entire model to be initialized.
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from pydantic.main.BaseModel:
 |
 |  __class_getitem__(typevar_values: 'type[Any] | tuple[type[Any], ...]') -> 'type[BaseModel] | _forward_ref.PydanticRecursiveRef' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  __get_pydantic_core_schema__(source: 'type[BaseModel]', handler: 'GetCoreSchemaHandler', /) -> 'CoreSchema' from pydantic._internal._model_construction.ModelMetaclass
 |      Hook into generating the model's CoreSchema.
 |
 |      Args:
 |          source: The class we are generating a schema for.
 |              This will generally be the same as the `cls` argument if this is a classmethod.
 |          handler: A callable that calls into Pydantic's internal CoreSchema generation logic.
 |
 |      Returns:
 |          A `pydantic-core` `CoreSchema`.
 |
 |  __get_pydantic_json_schema__(core_schema: 'CoreSchema', handler: 'GetJsonSchemaHandler', /) -> 'JsonSchemaValue' from pydantic._internal._model_construction.ModelMetaclass
 |      Hook into generating the model's JSON schema.
 |
 |      Args:
 |          core_schema: A `pydantic-core` CoreSchema.
 |              You can ignore this argument and call the handler with a new CoreSchema,
 |              wrap this CoreSchema (`{'type': 'nullable', 'schema': current_schema}`),
 |              or just call the handler with the original schema.
 |          handler: Call into Pydantic's internal JSON schema generation.
 |              This will raise a `pydantic.errors.PydanticInvalidForJsonSchema` if JSON schema
 |              generation fails.
 |              Since this gets called by `BaseModel.model_json_schema` you can override the
 |              `schema_generator` argument to that function to change JSON schema generation globally
 |              for a type.
 |
 |      Returns:
 |          A JSON schema, as a Python object.
 |
 |  __pydantic_init_subclass__(**kwargs: 'Any') -> 'None' from pydantic._internal._model_construction.ModelMetaclass
 |      This is intended to behave just like `__init_subclass__`, but is called by `ModelMetaclass`
 |      only after the class is actually fully initialized. In particular, attributes like `model_fields` will
 |      be present when this is called.
 |
 |      This is necessary because `__init_subclass__` will always be called by `type.__new__`,
 |      and it would require a prohibitively large refactor to the `ModelMetaclass` to ensure that
 |      `type.__new__` was called in such a manner that the class would already be sufficiently initialized.
 |
 |      This will receive the same `kwargs` that would be passed to the standard `__init_subclass__`, namely,
 |      any kwargs passed to the class definition that aren't used internally by pydantic.
 |
 |      Args:
 |          **kwargs: Any keyword arguments passed to the class definition that aren't used internally
 |              by pydantic.
 |
 |  from_orm(obj: 'Any') -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]' from pydantic._internal._model_construction.ModelMetaclass
 |      Generates a JSON schema for a model class.
 |
 |      Args:
 |          by_alias: Whether to use attribute aliases or not.
 |          ref_template: The reference template.
 |          schema_generator: To override the logic used to generate the JSON schema, as a subclass of
 |              `GenerateJsonSchema` with your desired modifications
 |          mode: The mode in which to generate the schema.
 |
 |      Returns:
 |          The JSON schema for the given model class.
 |
 |  model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str' from pydantic._internal._model_construction.ModelMetaclass
 |      Compute the class name for parametrizations of generic classes.
 |
 |      This method can be overridden to achieve a custom naming scheme for generic BaseModels.
 |
 |      Args:
 |          params: Tuple of types of the class. Given a generic class
 |              `Model` with 2 type variables and a concrete model `Model[str, int]`,
 |              the value `(str, int)` would be passed to `params`.
 |
 |      Returns:
 |          String representing the new class where `params` are passed to `cls` as type variables.
 |
 |      Raises:
 |          TypeError: Raised when trying to generate concrete names for non-generic models.
 |
 |  model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None' from pydantic._internal._model_construction.ModelMetaclass
 |      Try to rebuild the pydantic-core schema for the model.
 |
 |      This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
 |      the initial attempt to build the schema, and automatic rebuilding fails.
 |
 |      Args:
 |          force: Whether to force the rebuilding of the model schema, defaults to `False`.
 |          raise_errors: Whether to raise errors, defaults to `True`.
 |          _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
 |          _types_namespace: The types namespace, defaults to `None`.
 |
 |      Returns:
 |          Returns `None` if the schema is already "complete" and rebuilding was not required.
 |          If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
 |
 |  model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None) -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |      Validate a pydantic model instance.
 |
 |      Args:
 |          obj: The object to validate.
 |          strict: Whether to enforce types strictly.
 |          from_attributes: Whether to extract data from object attributes.
 |          context: Additional context to pass to the validator.
 |
 |      Raises:
 |          ValidationError: If the object could not be validated.
 |
 |      Returns:
 |          The validated model instance.
 |
 |  model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |      Usage docs: https://docs.pydantic.dev/2.10/concepts/json/#json-parsing
 |
 |      Validate the given JSON data against the Pydantic model.
 |
 |      Args:
 |          json_data: The JSON data to validate.
 |          strict: Whether to enforce types strictly.
 |          context: Extra variables to pass to the validator.
 |
 |      Returns:
 |          The validated Pydantic model.
 |
 |      Raises:
 |          ValidationError: If `json_data` is not a JSON string or the object could not be validated.
 |
 |  model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |      Validate the given object with string data against the Pydantic model.
 |
 |      Args:
 |          obj: The object containing string data to validate.
 |          strict: Whether to enforce types strictly.
 |          context: Extra variables to pass to the validator.
 |
 |      Returns:
 |          The validated Pydantic model.
 |
 |  parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  parse_obj(obj: 'Any') -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  update_forward_refs(**localns: 'Any') -> 'None' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  validate(value: 'Any') -> 'Self' from pydantic._internal._model_construction.ModelMetaclass
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from pydantic.main.BaseModel:
 |
 |  __fields_set__
 |
 |  model_computed_fields
 |      Get metadata about the computed fields defined on the model.
 |
 |      Deprecation warning: you should be getting this information from the model class, not from an instance.
 |      In V3, this property will be removed from the `BaseModel` class.
 |
 |      Returns:
 |          A mapping of computed field names to [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
 |
 |  model_extra
 |      Get extra fields set during validation.
 |
 |      Returns:
 |          A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
 |
 |  model_fields
 |      Get metadata about the fields defined on the model.
 |
 |      Deprecation warning: you should be getting this information from the model class, not from an instance.
 |      In V3, this property will be removed from the `BaseModel` class.
 |
 |      Returns:
 |          A mapping of field names to [`FieldInfo`][pydantic.fields.FieldInfo] objects.
 |
 |  model_fields_set
 |      Returns the set of fields that have been explicitly set on this model instance.
 |
 |      Returns:
 |          A set of strings representing the fields that have been set,
 |              i.e. that were not filled from defaults.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from pydantic.main.BaseModel:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __pydantic_extra__
 |
 |  __pydantic_fields_set__
 |
 |  __pydantic_private__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from pydantic.main.BaseModel:
 |
 |  __hash__ = None
 |
 |  __pydantic_root_model__ = False

>>>
'''
