import streamlit as st
from langchain import PromptTemplate
from langchain.llms import CTransformers



#function to generate blog response
def blogresponce(blog_topic, num_words, tone, audience):
    # Load the model
    llm = CTransformers(model="model\llama-2-7b-chat.Q8_0.gguf",
                        model_type="llama",
                        temperature=0.7,
                        max_new_tokens=256,
                        top_p=0.95,
                        top_k=40,
                        repeat_penalty=1.1)

    # Define the prompt template
    
    # (input_variables=["blog_topic", "num_words", "tone", "audience"],
    #                                  template=("Write a {num_words}-word blog post on the topic '{blog_topic}' "
    #                                            "with a {tone} tone, targeted at {audience}.)"
    input_variables = ["blog_topic", "num_words", "tone", "audience"]
    template = ("You are an expert blog writer. Write a detailed and engaging blog post of approximately {num_words} words "
                "on the topic '{blog_topic}'. The tone should be {tone}, and the content should be tailored for {audience}. "
                "Start with a catchy introduction, provide valuable insights, and end with a strong conclusion.")
    
    prompt = PromptTemplate(input_variables=input_variables, template=template)

    # Generate the blog content
    blog_content = llm(prompt.format(blog_topic=blog_topic, num_words=num_words, tone=tone, audience=audience))
    return blog_content



# Initialize the Streamlit app
st.set_page_config(page_title="Blog Generation App",
                   page_icon=":books:",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.title("Blog Generation :orange_book:")
st.write("""
         Welcome to the Blog Generation App by @asbpintu. 
         This app allows you to generate blog posts based on your input. 
         Please enter your blog topic below:
         """) 

# Input for blog topic
blog_topic = st.text_input("Enter your blog topic:", placeholder="e.g., AI in Healthcare")

# Create columns for additional fields: number of words, tone, and type of audience
col1, col2,col3 = st.columns([1, 1, 1])

# Input for number of words
with col1:
    num_words = st.number_input("Number of words:", min_value=100, max_value=5000, value=250, step=50)
# Input for tone of the blog
with col2:
    tone = st.selectbox("Tone of the blog:", ["Informative", "Conversational", "Persuasive", "Humorous"])
# Input for type of audience
with col3:
    audience = st.selectbox("Type of audience:", ["Researchers", "College Students", "Businessmen", "Common People"])

# Button to generate blog
submit = st.button("Generate Blog")

if submit:
    if blog_topic:
        st.write(f"Generating blog on **{blog_topic}** with the following parameters:")
        st.write(f"- Number of words: {num_words}")
        st.write(f"- Tone: {tone}")
        st.write(f"- Audience: {audience}")

        st.markdown("---")
        st.write("Blog content will be generated here...")
        # Call the function to generate blog content
        st.markdown("---")

        st.write(blogresponce(blog_topic, num_words, tone, audience))
    else:
        st.error("Please enter a blog topic to generate content.")