import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Question: {question}
Answer: Let me answer based solely on the provided context.
"""

def query_rag(query_text: str):
    embedding_function = get_embedding_function()

    try:
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_function
        )
    except Exception as e:
        raise Exception(f"Failed to initialize Chroma database: {e}")

    try:
        results = db.similarity_search_with_score(query_text, k=5)
    except Exception as e:
        raise Exception(f"Failed to perform similarity search: {e}")

    if not results:
        return "No relevant information found in the database."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    try:
        model = Ollama(model="mistral")
        response_text = model.invoke(prompt)
    except Exception as e:
        raise Exception(f"Failed to get response from language model: {e}")

    sources = [doc.metadata.get("source", "Unknown") + f" (score: {score:.2f})"
              for doc, score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"

    print(formatted_response)
    return response_text

def main():
    print("Hi, I am A.R.T.E.M.I.S, your personal football assistant.")
    query_text = input("How can I help you today?: ")

    while True:
        try:
            response = query_rag(query_text)
            print(response)
            query_text = input("What else would you like to know? (type 'exit' to quit): ")
            if query_text.lower() == 'exit':
                print("Thank you for using A.R.T.E.M.I.S. Goodbye!")
                break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()