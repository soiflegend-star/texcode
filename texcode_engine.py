"""
texcode_engine.py

TexCode — The Coding Genius.
A specialized coding assistant that can work standalone or as a personality.
Handles: code generation, debugging, optimization, explanation, architecture review.
Works offline via pattern matching + can route to API for frontier code quality.
"""

import re


_CODING_KEYWORDS = [
    "code", "program", "function", "class", "bug", "error", "debug",
    "python", "javascript", "java", "c++", "cpp", "rust", "go", "kotlin",
    "swift", "sql", "html", "css", "react", "vue", "angular", "node",
    "django", "flask", "fastapi", "api", "database", "query", "algorithm",
    "sort", "loop", "recursion", "regex", "json", "xml", "yaml",
    "git", "docker", "kubernetes", "aws", "cloud", "server", "client",
    "frontend", "backend", "fullstack", "devops", "compile", "runtime",
    "exception", "stack trace", "null pointer", "segmentation", "memory leak",
    "refactor", "optimize", "performance", "complexity", "o(n)", "big o",
    "unit test", "integration test", "ci/cd", "pipeline", "deploy",
]

_CODING_PATTERNS = [
    r"\bwrite\s+(a\s+)?(code|program|script|function|class)\b",
    r"\bhow\s+(do|can|to)\s+(i|you)\s+(write|create|make|build)\b",
    r"\bfix\s+(this|my|the)\s+(code|bug|error)\b",
    r"\bdebug\s+(this|my|the)\b",
    r"\bexplain\s+(this|the)\s+(code|algorithm|function)\b",
    r"\boptimize\s+(this|the|my)\b",
    r"\brefactor\s+(this|the|my)\b",
    r"\bwhat\s+(is|does)\s+(wrong|happening)\s+(with|in)\b",
]


class TexCodeEngine:
    def __init__(self):
        self._patterns = [re.compile(p, re.IGNORECASE) for p in _CODING_PATTERNS]

    def is_coding_query(self, text):
        lowered = text.lower()
        for kw in _CODING_KEYWORDS:
            if kw in lowered:
                return True
        for pat in self._patterns:
            if pat.search(text):
                return True
        return False

    def answer(self, query):
        lowered = query.lower()

        if any(w in lowered for w in ["write", "create", "make", "build", "generate"]):
            return self._generate_code(query)

        if any(w in lowered for w in ["bug", "error", "fix", "debug", "wrong", "broken"]):
            return self._debug_help(query)

        if any(w in lowered for w in ["explain", "how does", "what does", "why"]):
            return self._explain_concept(query)

        if any(w in lowered for w in ["optimize", "refactor", "improve", "better", "faster"]):
            return self._optimize_help(query)

        return self._general_coding_advice(query)

    def _generate_code(self, query):
        lang = self._detect_language(query)
        return (
            f"**TexCode** — Code Generation Mode\n\n"
            f"Language detected: **{lang or 'pseudocode'}**\n\n"
            f"I'd love to write that for you. Since I'm in offline mode, here's my approach:\n\n"
            f"1. **Break the problem down** — identify inputs, outputs, and edge cases\n"
            f"2. **Choose the right data structures** — they determine your complexity\n"
            f"3. **Write clean, commented code** — future-you will thank present-you\n"
            f"4. **Handle errors gracefully** — never trust user input\n"
            f"5. **Test with edge cases** — empty inputs, max values, weird strings\n\n"
            f"**Go /online** or use `/texcode` with an API key for full, runnable code generation.\n\n"
            f"What specifically are you building? I'll guide you through the architecture."
        )

    def _debug_help(self, query):
        return (
            f"**TexCode** — Debug Mode\n\n"
            f"Debugging is the art of being wrong systematically. Let's find your bug.\n\n"
            f"**My debug checklist:**\n"
            f"1. Read the error message carefully — it usually tells you exactly where\n"
            f"2. Check your assumptions — the bug is where you *didn't* look\n"
            f"3. Add print statements or use a debugger — see the state at each step\n"
            f"4. Isolate the problem — comment out half the code, then half again\n"
            f"5. Check for off-by-one errors, null values, and type mismatches\n"
            f"6. Did you change something 'unrelated' recently? That's probably it\n\n"
            f"**Paste your code and error message** — I'll trace it with you."
        )

    def _explain_concept(self, query):
        return (
            f"**TexCode** — Explanation Mode\n\n"
            f"The best explanations start with the 'why', not the 'what'.\n\n"
            f"Here's how I break down technical concepts:\n"
            f"1. **The metaphor** — relate it to something you already know\n"
            f"2. **The mechanics** — how it actually works under the hood\n"
            f"3. **The tradeoffs** — when to use it, when to avoid it\n"
            f"4. **The code** — a minimal, runnable example\n"
            f"5. **The gotchas** — the things that bite you at 2 AM\n\n"
            f"What concept are you wrestling with? I'll build you a mental model that sticks."
        )

    def _optimize_help(self, query):
        return (
            f"**TexCode** — Optimization Mode\n\n"
            f"Premature optimization is the root of all evil. But *measured* optimization is the root of all fast software.\n\n"
            f"**My optimization framework:**\n"
            f"1. **Profile first** — measure before you change (don't guess)\n"
            f"2. **Algorithmic wins** — O(n²) → O(n log n) beats micro-optimizations\n"
            f"3. **Data structure choice** — the right structure makes the algorithm trivial\n"
            f"4. **Memory vs CPU** — sometimes trading one for the other is the right call\n"
            f"5. **Parallelism** — can you do multiple things at once?\n"
            f"6. **Caching** — don't recompute what you already know\n\n"
            f"**Share your code and target** — I'll find the bottleneck."
        )

    def _general_coding_advice(self, query):
        return (
            f"**TexCode** — General Coding Mode\n\n"
            f"Code is read more often than it's written. Write for the human who maintains it.\n\n"
            f"**Core principles:**\n"
            f"• Naming is documentation — `processData()` vs `validateUserEmail()`\n"
            f"• Functions should do one thing — if 'and' is in the name, split it\n"
            f"• Comments explain 'why', not 'what' — the code shows the what\n"
            f"• Fail fast, fail loud — silent failures are nightmares\n"
            f"• Test at boundaries — empty, single, many, max, invalid\n"
            f"• Version control everything — if it's not committed, it doesn't exist\n\n"
            f"What are you working on? I'll help you think through it."
        )

    def _detect_language(self, text):
        lowered = text.lower()
        langs = [
            ("python", ["python", "py ", "django", "flask", "pandas", "numpy"]),
            ("javascript", ["javascript", "js ", "node", "react", "vue", "angular"]),
            ("typescript", ["typescript", "ts ", "tsx"]),
            ("java", ["java", "spring", "android"]),
            ("c++", ["c++", "cpp"]),
            ("rust", ["rust", "cargo"]),
            ("go", [" go ", "golang"]),
            ("sql", ["sql", "mysql", "postgres", "sqlite"]),
            ("html/css", ["html", "css", "bootstrap", "tailwind"]),
        ]
        for name, keywords in langs:
            for kw in keywords:
                if kw in lowered:
                    return name
        return None
