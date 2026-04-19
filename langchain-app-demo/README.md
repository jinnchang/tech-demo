# LangChain Agent Tool Calling Demo

## 场景示例

Demonstrates how a LangChain Agent can autonomously select and execute tools (time query, math calculation) based on user questions.

## 环境准备

```bash
pip install -r requirements.txt
```

## 文件结构

```
langchain-app-demo/
├── README.md
├── requirements.txt
└── main.py
```

## 运行测试

1. 设置环境变量：

```bash
export OPENAI_BASE_URL=""
export OPENAI_API_KEY=""
export MODEL_NAME=""
```

2. 启动交互：

```bash
python main.py
```

3. 输入测试问题：
   - "现在几点？"
   - "计算 2 + 3 * 4 等于多少"

## 预期输出

```
=== LangChain Agent Demo ===
Agent tools: get_current_time, calculator
Type 'quit' to exit

You: 现在几点？

Agent thinking...
... (verbose output showing tool call)

Agent: 现在是 2026-04-19 15:30:00
```