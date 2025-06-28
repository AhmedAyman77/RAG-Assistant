from string import Template

#### RAG PROMPTS ####

#### System ####

system_prompt = Template("\n".join([
    "You are an assistant to generate a response for the user.",
    "You will be provided by a set of docuemnts associated with the user's query.",
    "You have to generate a response based on the documents provided.",
    "if the documents do not have the answer try to generate the answer yourself."
    "Ignore the documents that are not relevant to the user's query.",
    "do not mention anything about the documents in your response. the user must not know that you are using documents to generate the answer.",
    "You have to generate response in the same language as the user's query.",
    "Be polite and respectful to the user.",
    "Be precise and concise in your response. Avoid unnecessary information.",
]))

#### Document ####
document_prompt = Template(
    "\n".join([
        "## Document No: $doc_num",
        "### Content: $chunk_text",
    ])
)

#### Footer ####
footer_prompt = Template("\n".join([
    "Based only on the above documents, please generate an answer for the user.",
    "## Question:",
    "$query",
    "",
    "## Answer:",
]))