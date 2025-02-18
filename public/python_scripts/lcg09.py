'''~/di/py/lcg09.py'''

'''
Lists Google GenerativeAI models available via the Google GenerativeAI API.
'''

import google.generativeai as genai

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print('........................................')
        print(m.name, ':')
        print(m)
'done'

'''
ini2) dan@hpsda6:~/di/py$ 
(gemini2) dan@hpsda6:~/di/py$ python -i lcg09.py 
........................................
models/gemini-1.0-pro-latest :
Model(name='models/gemini-1.0-pro-latest',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro Latest',
      description=('The original Gemini 1.0 Pro model. This model will be discontinued on '
                   'February 15th, 2025. Move to a newer Gemini version.'),
      input_token_limit=30720,
      output_token_limit=2048,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.9,
      max_temperature=None,
      top_p=1.0,
      top_k=None)
........................................
models/gemini-1.0-pro :
Model(name='models/gemini-1.0-pro',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro',
      description='The best model for scaling across a wide range of tasks',
      input_token_limit=30720,
      output_token_limit=2048,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.9,
      max_temperature=None,
      top_p=1.0,
      top_k=None)
........................................
models/gemini-pro :
Model(name='models/gemini-pro',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro',
      description='The best model for scaling across a wide range of tasks',
      input_token_limit=30720,
      output_token_limit=2048,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.9,
      max_temperature=None,
      top_p=1.0,
      top_k=None)
........................................
models/gemini-1.0-pro-001 :
Model(name='models/gemini-1.0-pro-001',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro 001 (Tuning)',
      description=('The original Gemini 1.0 Pro model version that supports tuning. Gemini 1.0 '
                   'Pro will be discontinued on February 15th, 2025. Move to a newer Gemini '
                   'version.'),
      input_token_limit=30720,
      output_token_limit=2048,
      supported_generation_methods=['generateContent', 'countTokens', 'createTunedModel'],
      temperature=0.9,
      max_temperature=None,
      top_p=1.0,
      top_k=None)
........................................
models/gemini-1.0-pro-vision-latest :
Model(name='models/gemini-1.0-pro-vision-latest',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro Vision',
      description=('The original Gemini 1.0 Pro Vision model version which was optimized for '
                   'image understanding. Gemini 1.0 Pro Vision was deprecated on July 12, 2024. '
                   'Move to a newer Gemini version.'),
      input_token_limit=12288,
      output_token_limit=4096,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.4,
      max_temperature=None,
      top_p=1.0,
      top_k=32)
........................................
models/gemini-pro-vision :
Model(name='models/gemini-pro-vision',
      base_model_id='',
      version='001',
      display_name='Gemini 1.0 Pro Vision',
      description=('The original Gemini 1.0 Pro Vision model version which was optimized for '
                   'image understanding. Gemini 1.0 Pro Vision was deprecated on July 12, 2024. '
                   'Move to a newer Gemini version.'),
      input_token_limit=12288,
      output_token_limit=4096,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.4,
      max_temperature=None,
      top_p=1.0,
      top_k=32)
........................................
models/gemini-1.5-pro-latest :
Model(name='models/gemini-1.5-pro-latest',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Pro Latest',
      description=('Alias that points to the most recent production (non-experimental) release '
                   'of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 '
                   'million tokens.'),
      input_token_limit=2000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-pro-001 :
Model(name='models/gemini-1.5-pro-001',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Pro 001',
      description=('Stable version of Gemini 1.5 Pro, our mid-size multimodal model that '
                   'supports up to 2 million tokens, released in May of 2024.'),
      input_token_limit=2000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createCachedContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-1.5-pro-002 :
Model(name='models/gemini-1.5-pro-002',
      base_model_id='',
      version='002',
      display_name='Gemini 1.5 Pro 002',
      description=('Stable version of Gemini 1.5 Pro, our mid-size multimodal model that '
                   'supports up to 2 million tokens, released in September of 2024.'),
      input_token_limit=2000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createCachedContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-pro :
Model(name='models/gemini-1.5-pro',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Pro',
      description=('Stable version of Gemini 1.5 Pro, our mid-size multimodal model that '
                   'supports up to 2 million tokens, released in May of 2024.'),
      input_token_limit=2000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-latest :
Model(name='models/gemini-1.5-flash-latest',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash Latest',
      description=('Alias that points to the most recent production (non-experimental) release '
                   'of Gemini 1.5 Flash, our fast and versatile multimodal model for scaling '
                   'across diverse tasks.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-001 :
Model(name='models/gemini-1.5-flash-001',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash 001',
      description=('Stable version of Gemini 1.5 Flash, our fast and versatile multimodal model '
                   'for scaling across diverse tasks, released in May of 2024.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createCachedContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-1.5-flash-001-tuning :
Model(name='models/gemini-1.5-flash-001-tuning',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash 001 Tuning',
      description=('Version of Gemini 1.5 Flash that supports tuning, our fast and versatile '
                   'multimodal model for scaling across diverse tasks, released in May of 2024.'),
      input_token_limit=16384,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createTunedModel'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-1.5-flash :
Model(name='models/gemini-1.5-flash',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash',
      description=('Alias that points to the most recent stable version of Gemini 1.5 Flash, our '
                   'fast and versatile multimodal model for scaling across diverse tasks.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-002 :
Model(name='models/gemini-1.5-flash-002',
      base_model_id='',
      version='002',
      display_name='Gemini 1.5 Flash 002',
      description=('Stable version of Gemini 1.5 Flash, our fast and versatile multimodal model '
                   'for scaling across diverse tasks, released in September of 2024.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createCachedContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-8b :
Model(name='models/gemini-1.5-flash-8b',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash-8B',
      description=('Stable version of Gemini 1.5 Flash-8B, our smallest and most cost effective '
                   'Flash model, released in October of 2024.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['createCachedContent', 'generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-8b-001 :
Model(name='models/gemini-1.5-flash-8b-001',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash-8B 001',
      description=('Stable version of Gemini 1.5 Flash-8B, our smallest and most cost effective '
                   'Flash model, released in October of 2024.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['createCachedContent', 'generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-8b-latest :
Model(name='models/gemini-1.5-flash-8b-latest',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash-8B Latest',
      description=('Alias that points to the most recent production (non-experimental) release '
                   'of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model, '
                   'released in October of 2024.'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['createCachedContent', 'generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-8b-exp-0827 :
Model(name='models/gemini-1.5-flash-8b-exp-0827',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash 8B Experimental 0827',
      description=('Experimental release (August 27th, 2024) of Gemini 1.5 Flash-8B, our '
                   'smallest and most cost effective Flash model. Replaced by '
                   'Gemini-1.5-flash-8b-001 (stable).'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-1.5-flash-8b-exp-0924 :
Model(name='models/gemini-1.5-flash-8b-exp-0924',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash 8B Experimental 0924',
      description=('Experimental release (September 24th, 2024) of Gemini 1.5 Flash-8B, our '
                   'smallest and most cost effective Flash model. Replaced by '
                   'Gemini-1.5-flash-8b-001 (stable).'),
      input_token_limit=1000000,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-2.0-flash-exp :
Model(name='models/gemini-2.0-flash-exp',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Flash Experimental',
      description='Gemini 2.0 Flash Experimental',
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'bidiGenerateContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-2.0-flash :
Model(name='models/gemini-2.0-flash',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Flash',
      description='Gemini 2.0 Flash',
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-2.0-flash-001 :
Model(name='models/gemini-2.0-flash-001',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Flash 001',
      description=('Stable version of Gemini 2.0 Flash, our fast and versatile multimodal model '
                   'for scaling across diverse tasks, released in January of 2025.'),
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
........................................
models/gemini-2.0-flash-lite-preview :
Model(name='models/gemini-2.0-flash-lite-preview',
      base_model_id='',
      version='preview-02-05',
      display_name='Gemini 2.0 Flash-Lite Preview',
      description='Preview release (February 5th, 2025) of Gemini 2.0 Flash Lite',
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-flash-lite-preview-02-05 :
Model(name='models/gemini-2.0-flash-lite-preview-02-05',
      base_model_id='',
      version='preview-02-05',
      display_name='Gemini 2.0 Flash-Lite Preview 02-05',
      description='Preview release (February 5th, 2025) of Gemini 2.0 Flash Lite',
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-pro-exp :
Model(name='models/gemini-2.0-pro-exp',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Pro Experimental',
      description='Experimental release (February 5th, 2025) of Gemini 2.0 Pro',
      input_token_limit=2097152,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-pro-exp-02-05 :
Model(name='models/gemini-2.0-pro-exp-02-05',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Pro Experimental 02-05',
      description='Experimental release (February 5th, 2025) of Gemini 2.0 Pro',
      input_token_limit=2097152,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-exp-1206 :
Model(name='models/gemini-exp-1206',
      base_model_id='',
      version='2.0',
      display_name='Gemini Experimental 1206',
      description='Experimental release (February 5th, 2025) of Gemini 2.0 Pro',
      input_token_limit=2097152,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-flash-thinking-exp-01-21 :
Model(name='models/gemini-2.0-flash-thinking-exp-01-21',
      base_model_id='',
      version='2.0-exp-01-21',
      display_name='Gemini 2.0 Flash Thinking Experimental 01-21',
      description='Experimental release (January 21st, 2025) of Gemini 2.0 Flash Thinking',
      input_token_limit=1048576,
      output_token_limit=65536,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.7,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-flash-thinking-exp :
Model(name='models/gemini-2.0-flash-thinking-exp',
      base_model_id='',
      version='2.0-exp-01-21',
      display_name='Gemini 2.0 Flash Thinking Experimental 01-21',
      description='Experimental release (January 21st, 2025) of Gemini 2.0 Flash Thinking',
      input_token_limit=1048576,
      output_token_limit=65536,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.7,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/gemini-2.0-flash-thinking-exp-1219 :
Model(name='models/gemini-2.0-flash-thinking-exp-1219',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Flash Thinking Experimental',
      description='Gemini 2.0 Flash Thinking Experimental',
      input_token_limit=1048576,
      output_token_limit=65536,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.7,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
........................................
models/learnlm-1.5-pro-experimental :
Model(name='models/learnlm-1.5-pro-experimental',
      base_model_id='',
      version='001',
      display_name='LearnLM 1.5 Pro Experimental',
      description=('Alias that points to the most recent stable version of Gemini 1.5 Pro, our '
                   'mid-size multimodal model that supports up to 2 million tokens.'),
      input_token_limit=32767,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
>>>
'''
