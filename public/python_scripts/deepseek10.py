'''~/lx/lx14/public/py/deepseek10.py'''

'''
Helps me study groq + llama3.

Demo:
ll ~/anaconda3/envs/
. ~/lx/lx14/public/lx14b_env.bash
python deepseek10.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["GROQ_API_KEY"]

LLAMA3 = 'llama3-8b-8192'

llama3_model = langchain_groq.ChatGroq(model=LLAMA3)

parser = langchain_core.output_parsers.StrOutputParser()

# create prompt list of tpls acting as messages
prompt_s = '''Please write a simple comparison of Python 3.12 to Python 3.11: '''

user_tpl = ("user", prompt_s + "\n[[{tent_ruling}]]")

messages_l = [user_tpl]

prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

'I use this to connect prompt to groq llama3_model:'
chain = prompt | llama3_model | parser

'Prep a dict to help me call invoke():'

invoke_d = {'tent_ruling': 'And please include dates.'}

'Rubber meets road:'
summary_s = chain.invoke(invoke_d)
print(summary_s)

'done'

'''
(lx14b) dan@hpsda6:~/lx/lx14/public/py$ python -i deepseek10.py 
Busy ...
Python 3.12 was released on October 24, 2022, and Python 3.11 was released on October 25, 2021. Here's a simple comparison of the two versions:

**New Features in Python 3.12:**

1. **PEP 649: Deprecation of cleatool**: The `cleartool` module has been deprecated and is no longer available in Python 3.12.
2. **PEP 654: Error Handling in Async Generators**: The `try`-`except` block in async generators now works as expected, allowing for more robust error handling.
3. **PEP 655: Dict Sort Order**: Dictionaries are now sorted alphabetically by key, regardless of the platform's locale.
4. **PEP 656: Type Hinting for Generic Aliases**: Type hints can now be used for generic aliases, making it easier to specify types for generic types.
5. **PEP 657: Improved Error Messages for Type Hints**: Error messages for type hints have been improved to provide more useful information.

**New Features in Python 3.11:**

1. **PEP 649: Deprecation of cleartool**: The `cleartool` module was deprecated in Python 3.11, and will be removed in a future version.
2. **PEP 648: Improved Error Messages for asyncio**: Error messages for asyncio have been improved to provide more useful information.
3. **PEP 644: Type Hinting for Union Types**: Type hints can now be used for union types, making it easier to specify types for union types.
4. **PEP 637: dict | collections.abc.MutableMapping**: The `dict` class now implements the `MutableMapping` protocol, making it easier to use dictionaries with other libraries.

**Changes in Python 3.12:**

1. **Deprecation of cleartool**: The `cleartool` module has been deprecated and is no longer available in Python 3.12.
2. **Changes to error handling in async generators**: The `try`-`except` block in async generators now works as expected, allowing for more robust error handling.

**Changes in Python 3.11:**

1. **Deprecation of cleartool**: The `cleartool` module was deprecated in Python 3.11, and will be removed in a future version.

**Backward Incompatible Changes:**

1. **Python 3.12**: None
2. **Python 3.11**: None

Overall, Python 3.12 includes several new features and improvements, including better error handling and type hinting. Python 3.11, on the other hand, mainly focused on deprecating the `cleartool` module and improving error messages.
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> 
(lx14b) dan@hpsda6:~/lx/lx14/public/py$
'''
