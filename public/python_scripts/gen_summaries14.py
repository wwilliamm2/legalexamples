'''~/lx/lx14/public/py/gen_summaries14.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Ref:
gen_summaries10.py
gen_summaries11.py
~dan/lc17/rt20.py

Demo:
ll ~/anaconda3/envs/
. ~/lx/lx14/public/lx14b_env.bash
python gen_summaries14.py

'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["GROQ_API_KEY"]



LLM_NAME = 'llama-3.1-8b-instant'
LLM_NAME = 'llama-3.3-70b-versatile'

# works
LLM_NAME = 'llama3-8b-8192'
LLM_NAME = 'gemma2-9b-it'
LLM_NAME = 'mixtral-8x7b-32768'
LLM_NAME = 'llama-3.3-70b-specdec'

# nope:
notLLM_NAME = 'deepseek-r1-distill-llama-70b-specdec'



'''
gpt, On the groq website I see two LLM models which might interest me: "llama-3.3-70b-versatile" and "llama-3.3-70b-specdec".
(https://console.groq.com/docs/models)
The website categorizes "llama-3.3-70b-versatile" as a Production model.
The website categorizes "llama-3.3-70b-specdec" as a Preview model.
Please search the web for discussions and information about these two models.
I understand the dictionary meaning of "versatile".
Please describe why groq might be using "specdec" as a descriptive token.
I have never seen the word "specdec" so I don't know what information it should convey to model users like me.
Thanks!
'''

'''
google:
https://groq.com/groq-first-generation-14nm-chip-just-got-a-6x-speed-boost-introducing-llama-3-1-70b-speculative-decoding-on-groqcloud/
'''


'''
llama-3.3-70b-versatile Answer1:

After conducting a search, I found that the term "specdec" is not a widely used or recognized term in the context of Large Language Models (LLMs). However, I can provide some insights based on the information available.

The term "specdec" is likely derived from the phrase "specialized decoder." In the context of LLMs, a decoder refers to the component of the model responsible for generating text based on the input or context. A specialized decoder would imply that the model is designed to excel in specific tasks or domains, potentially at the expense of more general language understanding capabilities.

Groq's use of "specdec" as a descriptive token for the "llama-3.3-70b-specdec" model suggests that this model might be optimized for specific use cases or applications, such as:

1. Improved performance on certain benchmark datasets or tasks.
2. Enhanced ability to generate text in specific styles or formats (e.g., more formal, technical, or creative writing).
3. Better handling of domain-specific terminology, jargon, or concepts.

In contrast, the "llama-3.3-70b-versatile" model, categorized as a Production model, is likely designed to be more general-purpose and adaptable to a wide range of tasks and applications. The term "versatile" implies that this model can handle various language-related tasks, such as conversational dialogue, text summarization, and language translation, with a balanced level of proficiency.

While I couldn't find specific discussions or comparisons between these two models, the distinction between "versatile" and "specdec" suggests that Groq is offering users a choice between:

* A more general-purpose model ("llama-3.3-70b-versatile") suitable for a broad range of applications, and
* A specialized model ("llama-3.3-70b-specdec") that might excel in specific areas, but potentially at the cost of reduced performance in other domains.

Keep in mind that the "specdec" model is labeled as a Preview model, which might indicate that it is still under development, testing, or refinement. As such, the performance and capabilities of this model may not be as polished as those of the Production model.
'''


'''
gemini:
You're right to be curious about the difference between "versatile" and "specdec" in the context of LLMs.  Unfortunately, "specdec" isn't a standard, widely recognized term in the LLM world.  This makes finding specific discussions about *these particular Groq models* difficult.  Groq likely uses it as an internal or product-specific abbreviation.

Here's a breakdown of what we *can* infer and how to approach understanding these models:

* **Versatile:** As you noted, "versatile" means adaptable and capable of handling a wide range of tasks.  In the context of an LLM, this suggests the model is trained for general-purpose use, suitable for various applications like text generation, translation, question answering, etc.  A "production" model designation reinforces this, implying it's stable, well-tested, and ready for real-world deployments.

* **Specdec:**  This is the mystery.  Here's how we can try to decode it:

    * **Speculation:**  "Spec" might be short for "specialized" or "specification."  "Dec" could potentially stand for "decoder," "decision," or even a shortened "dedicated."
    * **Inference:**  Given that it's a "preview" model, it's likely still under development or experimental.  It might be specialized for a particular task or have a different architecture or training approach compared to the versatile model.  Perhaps it uses a specialized decoding method or is designed for specific types of data.
    * **Groq's Documentation:** The best place to find a definitive answer is Groq's official documentation or support.  Look for release notes, model cards, or any information about the specific characteristics of the `llama-3.3-70b-specdec` model.  Since it's a preview model, information might be limited, but any details they do provide will be helpful.
    * **Contact Groq:** If you can't find the answer in their documentation, consider reaching out to Groq's support or sales team directly.  They should be able to explain the meaning of "specdec" and the differences between the two models.

* **General Approach:** Since "specdec" is likely Groq-specific, comparing it to other models outside of their platform is difficult.  Focus on understanding the differences *between* the `versatile` and `specdec` versions within the Groq ecosystem.  Look for benchmarks, performance metrics, or any examples Groq provides that demonstrate the unique strengths of each.

In summary, "versatile" tells you the model is designed for general-purpose use.  "Specdec" is a term you'll need to clarify with Groq directly.  It likely refers to some specialized characteristic of the model, and being a "preview" model suggests it's still evolving.

'''

'''
perplexity:
I apologize, but I'm unable to search the web for additional information about these models beyond what's provided in the search results. However, I can analyze the information given and offer some insights based on the Groq website data.

Regarding the two models you're interested in:

1. llama-3.3-70b-versatile (Production model):
   - This model is categorized as a Production model, which means it's intended for use in production environments.
   - It has a large context window of 128k tokens and can generate up to 32,768 tokens as output.
   - The "versatile" in its name suggests it's designed for a wide range of tasks and applications.

2. llama-3.3-70b-specdec (Preview model):
   - This model is categorized as a Preview model, meant for evaluation purposes only and not recommended for production use.
   - It has a smaller context window of 8,192 tokens.
   - The term "specdec" in its name is not a common term, and its meaning isn't immediately clear.

Regarding the term "specdec":

While I can't search for additional information, I can offer an educated guess about what "specdec" might mean:

- It could be an abbreviation or portmanteau of "specification decoder" or "specialized decoder."
- The "spec" part might refer to "specification," suggesting this model might be tailored for understanding or working with specific types of data or formats.
- The "dec" part could stand for "decoder," which in the context of language models often refers to the part of the model that generates output.

Groq might be using "specdec" as a descriptive token to indicate that this model has been fine-tuned or specialized for a particular type of task or data format. It could potentially be more focused or optimized for certain applications compared to the "versatile" model.

However, without official documentation or explanation from Groq, the exact meaning and implications of "specdec" remain speculative. If you need to understand the specific capabilities or use cases for this model, I would recommend contacting Groq directly or looking for any additional documentation they might provide about their preview models.

Citations:
[1] https://console.groq.com/docs/models

---
Answer from Perplexity: https://www.perplexity.ai/search/gpt-on-the-groq-website-i-see-aw0TePXnT5yli0RQ_5PkAg?utm_source=copy_output

............
Based on the search results, there are several key differences between the "llama-3.3-70b-versatile" and "llama-3.3-70b-specdec" models:

1. Context Window Size:
   - "llama-3.3-70b-versatile" has a large context window of 128k tokens[1].
   - "llama-3.3-70b-specdec" has a smaller context window of 8,192 tokens[1].

2. Model Status:
   - "llama-3.3-70b-versatile" is categorized as a Production model, intended for use in production environments[4].
   - "llama-3.3-70b-specdec" is categorized as a Preview model, meant for evaluation purposes only and not recommended for production use[4].

3. Specialization:
   - "llama-3.3-70b-versatile" is designed for a wide range of tasks and applications, as suggested by its "versatile" designation[1][4].
   - "llama-3.3-70b-specdec" appears to be more specialized, possibly for specific tasks or decision-making scenarios, as indicated by the "specdec" in its name[4].

4. Output Generation:
   - "llama-3.3-70b-versatile" can generate up to 32,768 tokens as output[1].
   - There is no specific information provided about the output generation capacity of "llama-3.3-70b-specdec".

5. Use Cases:
   - "llama-3.3-70b-versatile" is recommended for general use across various applications, including coding, reasoning, math, general knowledge tasks, instruction following, and tool use[1].
   - "llama-3.3-70b-specdec" might be tailored for more specific applications or specialized decision-making tasks, though exact details are not provided in the search results.

Both models are part of the Llama 3.3 70B family, which offers improvements in performance across various tasks compared to their 3.1 counterparts[1][2]. However, the "versatile" model appears to be the more general-purpose option, while the "specdec" model may be more specialized for certain applications.

Citations:
[1] https://groq.com/a-new-scaling-paradigm-metas-llama-3-3-70b-challenges-death-of-scaling-law/
[2] https://console.groq.com/docs/deprecations
[3] https://docs.meetneura.ai/what-is-neura/releases/neura-ai-v0.5.97-llama-3.3-70b-versatile-and-llama-3.3-70b-specdec-integrations-and-azure-blob
[4] https://www.promptfoo.dev/docs/providers/groq/
[5] https://rivalsense.co/intel/groq-latest-news-updates-dec-13-2024-release/
[6] https://x.com/ozenhati/highlights
[7] https://www.linkedin.com/posts/fdaudens_llms-ai-opensource-activity-7256643398227431424-J0Vf
[8] https://ai.plainenglish.io/rag-techniques-part-2-of-5-implementing-5-effective-methods-31ecbfe9c79c?gi=3591b5382904

---
Answer from Perplexity: https://www.perplexity.ai/search/gpt-on-the-groq-website-i-see-aw0TePXnT5yli0RQ_5PkAg?utm_source=copy_output

'''





myllm_model = langchain_groq.ChatGroq(model=LLM_NAME)

parser = langchain_core.output_parsers.StrOutputParser()

# create prompt list of tpls acting as messages
prompt_s = '''Please write a simple summary in YAML format of a legal document, a
"tentative ruling", written by a Judge about a future Court Hearing. 
The legal document describes the Judge's thinking based on infomation presented 
to the Judge before today.
In YAML format, please write: Case Number, Plaintiff's Name, Defendant's Name,
People-Names, Company-Names, Places, Dates, Events, Money, 
Intentions, Facts, Disputes, Acts, Agreements, Laws, Case Citations, 
Statutes, Roles and Signifcant Statements.
I really appreciate your help!
Oh, also please write English-text to summarize this judge's tentative ruling: '''

# Use this in except block:
prompt2_s = '''Please summarize: '''

user_tpl = ("user", prompt_s + "\n[[{tent_ruling}]]")
user2_tpl = ("user", prompt2_s + "\n[[{tent_ruling}]]")

messages_l = [user_tpl]
messages2_l = [user2_tpl]

prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)
prompt2 = langchain_core.prompts.ChatPromptTemplate.from_messages(messages2_l)

'I use this to connect prompt to groq myllm_model:'
chain = prompt | myllm_model | parser
chain2 = prompt2 | myllm_model | parser

'''Use tenttext_lacourt14.txt, 
a file full of tr-file-names to drive a loop 
which calls LLM to summarize each tr file.'''

with open('tenttext_lacourt14.txt') as txtf:
    tr_files_s = txtf.read()
tr_fn_s_l = sorted(tr_files_s.split('\n')[:-1]) # skip last 1

for tr_fn_s in tr_fn_s_l[-3:]:
    summ_fn_s = tr_fn_s.replace('/tent_ruling_','/summary_')
    with open(tr_fn_s) as txtf:
        tr_pln_txt_s = txtf.read()
    if len(tr_pln_txt_s) > 700: # It interests me
        'Note the file name:'
        print(f'Summarizing this file: {tr_fn_s}')
        print(f'Its length in chars: {len(tr_pln_txt_s)}')
        print('Busy with API ...')
        'I shd call LLM here.'
        context_i = 199011 # large-ish
        'Prep a dict to help me call invoke():'
        invoke_d = {'tent_ruling': tr_pln_txt_s[:context_i]}
        'Rubber meets road:'
        try:
            summary_s = chain.invoke(invoke_d)
            with open(f'{summ_fn_s}', 'a') as sumf:
                top_s = f'..................... ..................... ..................... ......\nThe summary displayed below was created by an LLM named "{LLM_NAME}":\n'
                sumf.write(f'{top_s}{summary_s}\n')
                print(f'New summary: {summ_fn_s}')
            # Make note of invoke_d
            with open(f'/tmp/invoke_d.txt', 'w') as invdf:
                invdf.write(str(prompt.invoke(invoke_d)))
            'remem to throttle API calls:'
            print('Busy with API ...')
            time.sleep(6) # seconds
        except Exception as myex:
            print(f'Exception on 1st-try. I am sleeping it off.\n{str(myex)}')
            time.sleep(400)
            try: # 2nd try
                summary_s = chain2.invoke(invoke_d)
                with open(f'{summ_fn_s}', 'a') as sumf:
                    top_s = f'..................... ..................... ..................... ......\nThe summary displayed below was created by an LLM named "{LLM_NAME}":\n'
                    sumf.write(f'{top_s}{summary_s}\n')
                    print(f'New summary 2nd try: {summ_fn_s}')
                    # Make note of invoke_d
                with open(f'/tmp/invoke_d2.txt', 'w') as invdf:
                    invdf.write(str(prompt.invoke(invoke_d)))
                'remem to throttle API calls:'
                print('Busy with API ...')
                time.sleep(6) # seconds
            except:
                print(f'Exception on 2nd-try.\nI gave up on {summ_fn_s}\nI am sleeping it off.\n{str(myex)}')
                time.sleep(400)
