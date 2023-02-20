import openai, os, sys
import subprocess, random

api_keys = [
    "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",
    "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"
    ]



class Error:
    connection = openai.error.APIConnectionError
    overload = openai.error.RateLimitError
    
def tableClass(table, new_file=None):
    
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
    return message

filename = None
req = sys.argv[1]
if len(sys.argv) == 3:
    filename = sys.argv[2]



res = tableClass(req, filename)
print(res)


