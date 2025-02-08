import openai

client = openai.OpenAI(api_key="ysk-proj-oOiUwrz5mtlUv8P2upGCTbxZOsHpSHynBBZGrf2M7Uyym7kdnWJsKuCAzNoMggslj4rjN_ln2AT3BlbkFJFPyhYV9azWdrc0kX9GDqfPc7jJPGvoNSKXcMEioHJI9yO3Kp57OIfx99a3O-NbgdMvux5I0PEA")
models = client.models.list()

for model in models.data:
    print(model.id)
