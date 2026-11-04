from llm_api import get_llm


llm=get_llm()


while(True):
    x=input("You : ")
    if x.lower()=='exit':
        break
    response=llm.invoke(x)
    # print(type(response.content[0]['text']))
    print("AI:",response.content[0]['text'])