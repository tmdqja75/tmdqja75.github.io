---
layout: post
title: Considerations When Developing LLM Agents
image:
  path: https://substackcdn.com/image/fetch/$s_!P0zV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7db78ee-7613-4d92-8859-5b60de7bcaa4_2000x1214.png
description: >
  This article outlines important factors to consider while developing LLM agents, based on recent project experiences. It focuses on tips for developing branching nodes using DSPy, simplifying database integrations using MCP Toolbox for Databases, and establishing observability centered around Langfuse. Each section is structured around immediately applicable methods to enhance the quality and deployment speed of your team’s agents.

categories: llm
sitemap:
  changefreq: weekly
comments: true
---

## Considerations When Developing Agents

When creating LLM agents in a professional setting, elements such as branching logic design, database integration, and observability can often be overlooked. Drawing from recent project experience, this article consolidates practical tips that have proven valuable, such as developing branching nodes using DSPy, streamlining database integration with MCP Toolbox for Databases, and building observability focused on Langfuse. Each section is organized around actionable methods, making it a great reference for elevating both the quality and deployment speed of your team’s agents.

### Developing Branching Nodes with DSPy

![prompt_engineering](/assets/img/2025-10-25-llm-agent-considerations/prompt-engineering.png)

Image generated using ChatGPT
{:.figcaption}

When developing an agent using LangGraph, it's common to use conditional edges to handle flows. For example, determining whether a user's question in a chatbot is related to the topic or not. Typically, branching logic involves a LangGraph node code and process like the following:

1. Compose a classification prompt.
2. Classify user input using the LLM and the crafted prompt.
3. Review results and manually adjust the prompt as necessary.

```python
def classification_node(state: LangGraphState) -> dict:

    message = state.messages[-1]  # Retrieve the latest message

    classification_prompt = f"""
    You are a question classifier. Please read the user's question, determine whether it is related to the topic, and return the result along with a confidence score in the JSON format below:
    {{
        "label": "positive" | "negative",
        "score": 0.44
    }}

    Here are some examples:
    "How's the weather today?" -> "negative"
    "Can you check this month's MAU?" -> "positive"
    """
    
    # Initialize the classifier pipeline
    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = llm | JsonOutputParser()

    # Run classification
    result = chain.invoke(message)

    # Return structured result
    return {
        "label": result["label"],
        "score": round(result["score"], 2)
    }
```

While experimenting in the initial prototyping stage, this approach might suffice, but creating a more accurate and maintainable version quickly becomes inefficient.

As you develop the nodes, you'll find yourself painstakingly testing each expected question to assess node accuracy, which prolongs the debugging process and fails to guarantee the accuracy of the final deployment.

To address this, I sought out more systematic prompt engineering techniques and discovered a Python package called DSPy. (For more information on DSPy, refer to my post on DSPy [here](https://tmdqja75.github.io/llm/2025-09-14-prompt-eng-dspy/) and the [official DSPy documentation](https://dspy.ai/tutorials/).) 

DSPy helps move beyond guess-work prompting methods, allowing for systematic prompt design based on data. Furthermore, DSPy supports experiment tracking with MLFlow, providing transparency in the prompt optimization process. After discovering DSPy, I moved away from traditional prompting engineering techniques and adopted the following process for developing branching nodes in LangGraph:

1. Draft about 5-10 expected questions or extract expected questions from past experiment logs.
2. Use ChatGPT to generate additional question data as needed (about 40-60 questions).
3. Label each question.
4. Divide the dataset into training and test datasets for prompt optimization.
5. Optimize prompts using the generated dataset and DSPy’s `MiPROv2` algorithm.
6. Track classification accuracy with MLFlow.

![dspy_mlflow tracking](</assets/img/2025-10-25-llm-agent-considerations/Screenshot 2025-10-14 at 12.04.57.png>)

Classification accuracy tracked with MLFlow for the prompt engineering 
{:.figcaption}

Using this approach allows for quantifiable verification of prompt effectiveness, and I observed that the nodes operated with considerable accuracy for new questions upon deployment.

### Simplifying Agent Database Integration with MCP Toolbox for Databases

![mcp toolbox for database](https://github.com/googleapis/genai-toolbox/raw/main/docs/en/getting-started/introduction/architecture.png)

Source: Official MCP Toolbox for Databases Documentation
{:.figcaption}

The MCP Toolbox for Databases (hereafter referred to as MtD) is a tool developed by Google for generating database MCP servers. It supports various databases, including PostgreSQL, making it applicable to a wide range of projects. MtD significantly simplifies the existing MCP server development process involving code writing to create a server, allowing for deployment with just a simple `yaml` file and a single line of bash script, eliminating boilerplate code.

```yaml
sources:
  my-pg-source:
    kind: postgres
    host: ${DB_HOST}
    port: ${DB_PORT}
    database: postgres
    user: ${USER_NAME}
    password: ${PASSWORD}
tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source
    description: Search for hotels based on name.
    parameters:
      - name: name
        type: string
        description: The name of the hotel.
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
  search-hotels-by-location:
    kind: postgres-sql
    source: my-pg-source
    description: Search for hotels based on location.
    parameters:
      - name: location
        type: string
        description: The location of the hotel.
    statement: SELECT * FROM hotels WHERE location ILIKE '%' || $1 || '%';
```

After drafting the YAML file, server deployment is just a single command line away:

```bash
toolbox --tools-file "tools.yaml" --ui

INFO "Toolbox UI is up and running at: http://localhost:5000/ui"
```

Once deployment is complete, check the logs, and accessing the provided URL for the MCP server will display the list of available tools through the UI.

![toolbox-ui](https://googleapis.github.io/genai-toolbox/how-to/toolbox-ui/tools.png)

MCP Toolbox for Databases UI
{:.figcaption}

The advantages of this tool are twofold. Firstly, it drastically reduces the time required for developing database-related MCP servers. With just a YAML file containing the necessary queries and a single line of Bash script, you can easily deploy an MCP server, making it an attractive option for project implementation.

Additionally, it minimizes the time needed for the agent to retrieve data related to questions or topics. Typically, when integrating agents with databases, text-to-SQL techniques are commonly utilized. However, even for simple queries, the processes of RAG application, query validation, and rewriting can accumulate latency before delivering the final response. With MCP Toolbox for Databases, frequently used queries can be toolified, allowing LLM agents to call only the necessary tools and directly extract relevant data from the database, significantly reducing response times.

### Observability

![observability](/assets/img/2025-10-25-llm-agent-considerations/observability.jpg)

Image generated using Google Nano Banana
{:.figcaption}

In agent development and debugging, observability, or the ability to check intermediate states, is crucial, just as it is for other software development tasks. In particular, when developing agents using LangGraph, the complexity increases as the number of nodes and edges grows. Without a straightforward way to verify how the agent generates responses, understanding why the agent provided a particular answer or identifying malfunctioning nodes becomes challenging.

Moreover, having an observability system that records the questions and answers utilized in the LLM agent during development and deployment can accumulate valuable data for future model enhancements.

When tracing agents built with LangChain or LangGraph, LangSmith is often utilized. Developed by the LangChain team, it offers convenient integration and a variety of supplementary functionalities. However, after the initial 5,000 traces, additional costs arise, and data is purged after 14 or 400 days, depending on the plan. Moreover, handling sensitive data adds the risk of exposure.

If you need to maintain data for an extended period or prioritize data security and privacy, I recommend using an open-source LLM logging platform. I frequently use a tool called Langfuse during projects. The setup is fairly manageable, and compared to other open-source LLM observability tools, it has a larger community, enhancing debugging convenience.

![langfuse ui](https://langfuse.com/images/docs/tracing-overview.png)

Source: Official Langfuse Documentation
{:.figcaption}

## Conclusion

In this article, we covered how to systematically optimize branching nodes with DSPy, streamline database integration with MCP Toolbox for Databases, and enhance observability using Langfuse. These three aspects do not stand alone; rather, they form a cohesive loop that accelerates rapid experimentation, learning, and improvement. I recommend implementing a couple of small improvements and gradually expanding while monitoring the metrics.

If you glean any insights or have questions while applying these concepts, please leave a comment. In the next article, I will outline methods to further extend prompt/tool/observability design based on a wider range of use cases.