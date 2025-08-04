---
layout: post
title: LLM에이전트가 도구를 방법
image: 
  path: https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b5b3_664c8772c80586fb49458bb3_llm-agent-structure.webp
description: >
  LLM이 도구를 호출 하는 방법
categories: llm

---
# LLM 에이전트와 Tool Calling 작동 원리

최근 자연어 처리 분야에서 가장 주목받는 개념 중 하나는 **LLM 에이전트(Large Language Model Agent)**입니다. 단순히 텍스트만 생성하던 LLM에서 나아가, 외부 도구를 호출하고 실행 결과를 기반으로 추론을 이어가는 능동적 시스템으로 발전하고 있습니다.

이 글에서는
- LLM 에이전트란 무엇인지,
- 어떻게 Tool Calling(도구 호출)이 작동하는지,
에 대해 설명하겠습니다.

## LLM 에이전트란?
LLM 에이전트는 말 그대로, “언어 모델이 외부 도구를 활용하여 작업을 수행하는 에이전트”입니다. GPT나 Claude 같은 LLM은 강력한 자연어 처리 능력을 갖추고 있지만, 실제 계산, 검색, API 호출 같은 작업은 직접 수행하지 못합니다.

따라서 LLM 에이전트는 다음과 같은 구성을 갖습니다:
- LLM: 언제 도구를 써야 할지, 어떤 도구를 어떤 인자로 호출해야 할지를 판단
- 도구 목록 (Tool): 모델이 호출할 수 있는 외부 기능들
- 오케스트레이터(Orchestrator): 모델이 요청한 도구를 실제 실행하고, 결과를 모델에게 다시 전달

## Orchestrator / Framework
- LLM과 도구 사이 요청과 결과를 전달해주는 매체를 오케스트레이터, 또는 프레임워크라 부릅니다.

LangChain은 대표적인 LLM 프레임워크입니다. LLM이 내보낸 tool call 정보를 읽고, 실제 도구를 실행하며, 결과를 다시 모델에 넘기는 역할을 합니다.

LangChain의 역할:
1.	도구 정의 및 등록 (@tool 등으로)
2.	모델에 도구 목록과 스키마 전달
3.	모델이 도구 호출을 요청하면 이를 실제로 실행
4.	결과를 받아서 모델에게 다시 전달하여 후속 추론 유도

즉, LangChain은 LLM 에이전트를 실제 작동 가능하게 만드는 연결고리입니다.


## LLM과 tool

그렇다면, LLM은 어떤 도구를 언제 사용해야 될지 어떻게 알 수 있을까요? 단계별로 차근차근 살펴보겠습니다

### System Prompt

LLM Agent에서 System Prompt는 LLM과의 대화에서 모델의 전반적인 행동을 설정하는 고정된 메시지입니다. 예를 들어 다음과 같은 형식으로 구성됩니다:

```
"당신은 다양한 외부 도구(tool)를 활용할 수 있는 지능형 AI 어시스턴트입니다.  
사용자의 질문에 따라 아래에 나열된 도구들 중 가장 적절한 것을 선택하여 호출할 수 있어야 합니다.

## 도구 목록:
  {
    "name": "SearchWeb",
    "description": "웹에서 정보를 검색합니다.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {"type": "string", "description": "검색할 키워드"}
      },
      "required": ["query"]
    }
  },
  {
    "name": "Calculator",
    "description": "간단한 수학 계산을 수행합니다.",
    "parameters": {
      "type": "object",
      "properties": {
        "expr": {"type": "string", "description": "계산 식, ex: '12 * 8 + 3'"}
      },
      "required": ["expr"]
    }
  }

### 도구 호출 방식:
• “Action:” 항목에 JSON 포맷으로 단 하나의 action 도구 호출만 지정하세요.  
• JSON 객체는 반드시 아래 형식이어야 합니다:
```json
{
  "action": "<도구이름>",
  "action_input": { /* 도구에 전달할 파라미터 */ }
}"

```

LLM에게 도구 종류와 사용법을 알려주는 방법은 SystemPrompt에 도구에 대한 설명을 string 형태로 삽입합니다. 이때, LLM이 도구에 대해 잘 이해할 수 있도록, 도구 설명에는 적어도 아래 요소들을 포함해야 합니다
- 도구 이름
- 도구 설명
- 도구 입력 변수와 입력 변수 data type
- 도구 필수 입력 변수

###  사용자 입력 처리

사용자가 LLM에게 system prompt와 원하는 질문을 입력하면, LLM은 System prompt애 있는 도구 리스트를 참조하여, 도구 사용 JSON 응답을 자연어 형식 (string)으로 반환합니다. 예를 들어, 사용자가 Agent에게 `오늘 OpenAI 에서 어떤 새로운 모델이 나왔어?` 라고 질문한다면, LLM은 이런 답변을 반환합니다.

```json
[{
    "type": "function_call",
    "action": "SearchWeb",
    "action_input": "{\"query\":\"OpenAI 최신 모델\"}"
}]
```

### Franework 처리
- LLM 프레임워크 (ex. Langchain)은 LLM의 응답을 받아, LLM이 요청한 도구(함수)를 불러, LLM이 생성한 함수 입력 변수를 삽입해 도구 결과를 도출합니다. 도구에서 생성된 결과는 다시 LLM의 시스템 프롬프트, 사용자 질문과 함꼐 입력되어 최종 답변을 도출합니다. 아래 도표를 참조하여 플로우가 어떤 식으로 흐르는지 파악할 수 있습니다.


![llm_memory](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif)

## 정리
LLM이 도구를 호출하는 방식은 아래 도표로 정리해볼 수 있습니다. 다음 포스팅으로는, LLM이 도구 호출을 위해 어떤 식으로 학습이 되는지, 어떤 데이터셋을 사용하는지에 대해 포스팅해보겠습니다.

![llm_toolcall](https://cdn.openai.com/API/docs/images/function-calling-diagram-steps.png)



