from openai import OpenAI

client = OpenAI(api_key='')

assistant = client.beta.assistants.retrieve("asst_k5znPftzQtXVBdLNC5SSTuF5")
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Quais são os parâmetros que tenho que passar para gerar um qrCode pela api da SuitPay?" # Exemplo de input para o ChatBot
)
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    tools=[{"type": "file_search"}],
)
if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print(run.status)
