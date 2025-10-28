---
layout: post
title: LLM Agent 개발 할 때 고려해야 할 점
image:
  path: https://miro.medium.com/v2/resize:fit:2000/1*5bWUR3N5ki5mE5D6aGZLQA.png
description: >
  
categories: llm
sitemap:
  changefreq: weekly
comments: true
---

## 에이전트 개발할 때 고려해야 할 점

오늘은 그동안 LLM 에이전트를 개발하면서 느끼 점들을 공유하려 합니다.

###  DSPy로 LangGraph 분기 노드 개발

![prompt_engineering](/assets/img/2025-10-25-llm-agent-considerations/prompt-engineering.png)

ChatGPT를 사용한 이미지 생성
{:.figcaption}

LangGraph로 에이전트 개발을 할 때, 분기 처리 엣지 ([Conditional Edge](https://langchain-ai.github.io/langgraph/concepts/low_level/#conditional-edges))를 사용하여 플로우를 처리는 경우가 많습니다. 예를 들어 챗봇에서 사용자의 질문이 주제와 관련 있는 질문인지, 아닌지 판단할 때와 같은 경우죠. 이때 보통 아래와 같은 LangGraph 노드 코드와 프로세스로 분기 처리를 진행하는데요,

1. 분류 프롬프트를 작성한다
2. LLM  + 작성된 프롬프트로 사용자 입력을 분류한다.
3. 결과를 확인하면서, 프로프트를 수동으로 수정한다.

```python
def classification_node(state: LangGraphState) -> dict:

    message = state.messages[-1] #  가장 최근 메세지 불러오기

    classification_prompt = f"""
    당신은 질문 분류가입니다. 사용자의 질문을 읽고, 질문이 주제와 관련 있는지 판단하고, 결과와 confidence score을 아래 json 형식으로 반환해주세요
    {
        "label": "positive" | "negative",
        "score": 0.44
    }

    아래는 몇 가지 예시입니다.
    "오늘 날씨 어때?" -> "negative"
    "이번달 MAU 조회해줘" -> "positive"
    """
    
    # Initialize the classifier pipeline
    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = llm | JsonOutputParser()

    # Run classification
    result =  chain.invoke(message)

    # Return structured result
    return {
        "label": result["label"],
        "score": round(result["score"], 2)
    }
```
처음 프로토타이핑 단계에서는 이렇게 실험을 해도 괜찮았지만, 좀 더 정확도 높고 유지보수 가능한 버전을 만드러 보려 하니 프로세스가 많이 비효율적이라 느껴졌습니다.

이렇게 노드를 개발하게 되면, 예상 질문을 하나하나 테스팅 하면서 노드 정확도를 판단해야 하기 때문에 디버깅 프로세스가 오래 걸리고, 실제 배포했을 때의 정확도을 보장할 수 없게 됩니다.

그래서 이 문제를 해결하기 위해 좀 더 체계적인 프롬프트 엔지니어링 기법을 찾다가 DSPy라는 파이썬 패키지를 발견했습니다. (DSPy에 대한 자세한 정보는 [제가 작성한 DSPy 포스팅](https://tmdqja75.github.io/llm/2025-09-14-prompt-eng-dspy/)과 [DSPy 공식 문서](https://dspy.ai/tutorials/)를 참조하세요.) 

DSPy는 guess-work 프롬프팅 기법에서 벗어나 데이터 기반으로 체계적으로 프롬프팅을 설계할 수 있도록 도와줍니다. 또한, DSPy는 MLFlow로 실험 트래킹도 지원하여, 프롬프트 최적화 프로세스를 투명하게 파악할 수 있습니다. DSPy를 발견한 이후 LangGraph에서 이런 분기 노드를 개발할 때, 기존 프롬프팅 엔지니어링 기법에서 벗어나 다음과 같은 프로세스를 사용했습니다

1. 예상 질문 (또는 input)을 5-10개 정도 작성하거나 과거 실험 로그 기록에서 예상 질문을 추출한다.
2. ChatGPT로 원하는 만큼 추가 질문 데이터 생성 (40~60개 정도)
3. 각 질문마다 라벨 적용
4. 생성된 데이터셋과 DSPy의 `MiPROv2` 알고리즘으로 프롬프트 최적화 진행
5. MLFlow로 분류 정확도 트래킹

![dspy_mlflow tracking](</assets/img/2025-10-25-llm-agent-considerations/Screenshot 2025-10-14 at 12.04.57.png>)

이런 식으로 개발하니, 프롬프트가 잘 작동하는지를 수치화해서 확인할 수 있고, 실제 배포했을 때도 새로운 질문에도 꽤 높은 정확도로 노드가 작동하는 것을 확인하였습니다.

### MCP toolbox for Databases로 에이전트 DB 연동 프로세스 간소화

![mcp toolbox for database](https://github.com/googleapis/genai-toolbox/raw/main/docs/en/getting-started/introduction/architecture.png)

MCP toolbox for Databases (이하 MtD)는 구글에서 개발한 (이름이 좀 많이 긴) 데이터베이스 MCP연동 툴입니다. MtD는 기존 코드를 작성해야 하는 데이터베이스 MCP서버 개발 프로세스를 최소한 단순화해서 boilerplate 코드 없이 아래와 같이 간단한 `yaml`파일 작성과 `bash`스크립트 한 줄이면 바로 MCP서버를 배포할 수 있게 해주는 유용한 툴입니다.



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

다양한 데이터베이스(PostgreSQL 포함)를 지원해서 폭넓은 프로젝트에 작용이 가능합니다.  자주 조회하는 데이터나 반복되는 질의는 미리 SQL 쿼리를 작성하여 MtD yaml 파일에 정의해 둘 수 있습니다. 이를 MtD를 활용해 에이전트의 도구로 등록하면, 에이전트가 복잡한 쿼리를 직접 작성하지 않고도 자연어로 데이터베이스에서 원하는 정보를 바로 조회할 수 있습니다.

데이터베이스에서 text-to-sql를 사용하여 원하는 데이터를 가져오려면, 에이전트가 먼저 sql 쿼리문을 작성하고 수정한 뒤 데이터를 가져올 수 있게 되는데, 보통 sql 쿼리를 작성/수정하는 과정이 꽤 오랜 시간이 걸립니다. MtD를 활용하면, 자주 사용하는 쿼리를 도구화해놓았기 때문에 데이터를 좀 더 빠르게 가져올 수 있다는 장점도 추가로 있습니다. 

###  Observability

![observability](/assets/img/2025-10-25-llm-agent-considerations/observability.jpg)

Google Nano Banana를 사용한 이미지 생성
{:.figcaption}

에이전트 개발/디버깅에서도, 다른 개발 작업과 마찬가지로 중간 상태를 확인하는 observability가 중요합니다. 특히 LangGraph로 에이전트를 개발할 때 에이전트가 고도화될수록 노드와 엣지가 많이 늘어나게 됩니다. 이떄, 에에전트가 답변을 생성하는 과정을 손쉽게 확인할 방법이 없다면, 에이전트가 왜 특정 답변은 내놓았는지, 어떤 노드가 잘 동작을 안하는지를 파악하기 수월하지 않습니다.

또한, LLM Agent 개발/배포하면서 질문과 답변을 

LangSmith는 무료버전에서는 데이터 리텐션 기간이 최대 30일정도 밖에 되지 않아서 유료 플랜으로 이전하거나 다른 오픈소스 LLM 로깅 플랫폼을 사용하는 것을 추천합니다. 저는 프로젝트할 때 Langfuse라는 툴을 잘 쓰는 편입니다. 초기 설정도 비교적 편하고, 

![langfuse ui](https://langfuse.com/images/docs/tracing-overview.png)

출저: Langfuse 공식 문서
{:.figcaption}


## 
앞으로 지속적으로 여러 use cases에서 에이전트를 개발해볼 예정입니다. 추후 또 에이전트 개발 유용한 정보가 있다면, 2편으로 정리해서 돌아오겠습니다!