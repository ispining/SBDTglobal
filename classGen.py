import datetime

import openai, os, sys, random

api_keys = [
    "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",
    "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",
    "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"
    ]



class Error:
    connection = openai.error.APIConnectionError
    overload = openai.error.RateLimitError


def generateTableClass(table, new_file=None):
    
    openai.api_key = random.choice(api_keys)
    
    # Определяем промпт и модель, которую будем использовать
    prompt = f"""напиши класс python который создает 
таблицу {table}, редактирует ее (по одному столбцу), 
создает новые записи и читает, возвращая список словарей. 

если в коде нужна база данных - требуется использовать 
базу данных postgresql. <|endoftext|>"""
    
    model = "text-davinci-003"
    
    # Определяем параметры запроса к API
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2040-len(prompt),
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Извлекаем сгенерированный текст из ответа API
    message = completions.choices[0].text.strip()
    
    
    if "generated" not in os.listdir():
        os.mkdir("generated")
    table_name = "generated/" + table.split("(")[0]+".py"
    
    if new_file != None:
        table_name = new_file
        
    with open(table_name, "w") as file:
        file.write(message)
    
    
    
    # Выводим сгенерированный текст
    return table_name

filename = None
req = sys.argv[1]
if len(sys.argv) == 3:
    filename = sys.argv[2]


print(f"[+] Start generation")
t1 = datetime.datetime.now()
res = generateTableClass(req, filename)
t2 = datetime.datetime.now()
print(f"[+] File {res} generated")
print(f"[+] Time: " + str(t2 - t1).split(":")[-1])

