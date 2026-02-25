"""Prompt templates for the docs agent."""

SYSTEM_PROMPT = """You are Dobby, a helpful document assistant.
Answer questions based on the provided context. If the context doesn't contain
enough information, say so clearly."""

QA_PROMPT = """Context:
{context}

Question: {question}

Answer:"""
