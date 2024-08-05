import pandas as pd


file_path = "data.csv"

system_content = input("System content: ")
output_file = open("fine-tuning.jsonl", "w")
dataframe = pd.read_csv(file_path)

for index, row in dataframe.iterrows():
    question = row["prompt"]
    answer = row["completion"]
    answer = (str(answer)).rstrip("\n")
    # row_object = ('{"messages":[{"role":"system","content":"' + system_content + '"},{"role":"user","content":"'
    # + question
    #               + '"},{"role":"assistant","content":"' + answer + '"}]}\n')
    row_object = (f"""{{"messages":[{{"role":"system","content":"{system_content}"}},""" +
                  f"""{{"role":"user","content":"{question}"}},{{"role":"assistant","content":"{answer}"}}]}}\n""")

    output_file.write(row_object)

output_file.close()

