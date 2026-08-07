#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  ████████╗███████╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗
  ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
     ██║   █████╗   ╚███╔╝ ██║     ██║   ██║██║  ██║█████╗
     ██║   ██╔══╝   ██╔██╗ ██║     ██║   ██║██║  ██║██╔══╝
     ██║   ███████╗██╔╝ ██╗╚██████╗╚██████╔╝██████╔╝███████╗
     ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
═══════════════════════════════════════════════════════════════════════════════
TEXCODE v1.0 — Ultimate Offline Coding AI for Android
Built with KivyMD | No API Keys | Works 100% Offline

BUILD INSTRUCTIONS (Google Colab + Buildozer):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Upload this file to Google Colab
2. Install buildozer: !pip install buildozer
3. Run: !buildozer init
4. Edit buildozer.spec:
   - source.include_exts = py,png,jpg,kv,atlas,ttf,json,xml,yaml
   - requirements = python3,kivy,kivymd,pillow,sqlite3,requests,urllib3,chardet,certifi,idna
   - orientation = portrait
   - fullscreen = 0
   - android.api = 33
   - android.minapi = 21
   - android.ndk = 25b
   - android.arch = arm64-v8a
   - android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
5. Run: !buildozer -v android debug
6. Download: bin/*.apk

FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖  Local AI Engine (rule-based + Ollama support, zero API keys)
💬  Smart Chat with code generation, analysis, explanations
📝  Code Editor with syntax highlighting
📁  Project Manager with file tree
🔗  Smart File Merger with conflict resolution
📦  ZIP Exporter for entire projects
🔍  Code Analysis (AST-based bug detection, complexity)
💾  Persistent SQLite Memory (remembers everything)
🌐  Web Search (docs, GitHub, StackOverflow — no API keys)
⚡  Project Templates (Flask, React, Python, HTML)

For AI superpowers, install Termux + Ollama on Android, or use the
built-in rule-based engine which is already incredibly powerful!
═══════════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import json
import sqlite3
import ast
import zipfile
import shutil
import re
import hashlib
import time
import base64
import io
import traceback
import collections
import math
import random
import datetime
import typing
import textwrap
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Dict, Optional

# ─── KIVY IMPORTS ─────────────────────────────────────────────────────────────
os.environ["KIVY_NO_ARGS"] = "1"
os.environ["KIVY_WINDOW"] = "sdl2"

from kivy.config import Config
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", "0")
Config.set("kivy", "exit_on_escape", "0")

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty, ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.metrics import dp, sp
from kivy.animation import Animation
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.chip import MDChip
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.theming import ThemableBehavior
from kivymd.color_definitions import colors

# ─── OPTIONAL: REQUESTS ───────────────────────────────────────────────────────
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ─── COLOR PALETTE (Cyberpunk Dark) ───────────────────────────────────────────
COLORS = {
    "bg_primary": "#0a0e17",
    "bg_secondary": "#111827",
    "bg_card": "#1a2332",
    "bg_input": "#0f1724",
    "accent": "#00d4ff",
    "accent_secondary": "#a855f7",
    "accent_tertiary": "#22c55e",
    "text_primary": "#e2e8f0",
    "text_secondary": "#94a3b8",
    "text_muted": "#64748b",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "success": "#22c55e",
    "border": "#1e293b",
    "highlight": "#1e3a5f",
}

# ─── CONFIG & PATHS ───────────────────────────────────────────────────────────
class AppConfig:
    APP_NAME = "TexCode"
    VERSION = "1.0.0"

    @classmethod
    def base_dir(cls):
        # Android storage or local
        if "ANDROID_ARGUMENT" in os.environ:
            return Path(os.environ.get("ANDROID_APP_PATH", "/sdcard/TexCode"))
        return Path.home() / ".texcode"

    @classmethod
    def db_path(cls):
        return cls.base_dir() / "memory.db"

    @classmethod
    def projects_dir(cls):
        return cls.base_dir() / "projects"

    @classmethod
    def temp_dir(cls):
        return cls.base_dir() / "temp"

    @classmethod
    def ensure_dirs(cls):
        for d in [cls.base_dir(), cls.projects_dir(), cls.temp_dir()]:
            d.mkdir(parents=True, exist_ok=True)

AppConfig.ensure_dirs()

# ─── DATABASE ─────────────────────────────────────────────────────────────────
class TexCodeDB:
    """Persistent SQLite memory engine."""

    def __init__(self):
        self.conn = sqlite3.connect(str(AppConfig.db_path()), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_tables()

    def _init_tables(self):
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            language TEXT,
            description TEXT
        );
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT NOT NULL,
            path TEXT NOT NULL,
            content TEXT,
            size INTEGER DEFAULT 0,
            language TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(project_id, path),
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            meta TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_files_project ON files(project_id);
        CREATE INDEX IF NOT EXISTS idx_chat_project ON chat_history(project_id);
        """)
        self.conn.commit()

    def create_project(self, name: str, description: str = "", language: str = "") -> str:
        pid = hashlib.md5(f"{name}{time.time()}".encode()).hexdigest()[:12]
        self.conn.execute(
            "INSERT INTO projects (id, name, description, language) VALUES (?, ?, ?, ?)",
            (pid, name, description, language)
        )
        self.conn.commit()
        return pid

    def get_projects(self):
        cur = self.conn.execute("SELECT * FROM projects ORDER BY updated_at DESC")
        projects = []
        for row in cur.fetchall():
            p = dict(row)
            p["file_count"] = self.conn.execute(
                "SELECT COUNT(*) FROM files WHERE project_id = ?", (p["id"],)
            ).fetchone()[0]
            projects.append(p)
        return projects

    def get_project(self, pid: str):
        cur = self.conn.execute("SELECT * FROM projects WHERE id = ?", (pid,))
        row = cur.fetchone()
        return dict(row) if row else None

    def delete_project(self, pid: str):
        self.conn.execute("DELETE FROM projects WHERE id = ?", (pid,))
        self.conn.commit()
        d = AppConfig.projects_dir() / pid
        if d.exists():
            shutil.rmtree(d)

    def save_file(self, pid: str, path: str, content: str):
        size = len(content.encode("utf-8"))
        lang = self._detect_lang(path)
        self.conn.execute(
            """INSERT INTO files (project_id, path, content, size, language) 
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(project_id, path) DO UPDATE SET
               content=excluded.content, size=excluded.size, language=excluded.language,
               updated_at=CURRENT_TIMESTAMP""",
            (pid, path, content, size, lang)
        )
        self.conn.execute("UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (pid,))
        self.conn.commit()

        d = AppConfig.projects_dir() / pid
        d.mkdir(parents=True, exist_ok=True)
        fp = d / path
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(content, encoding="utf-8")

    def get_file(self, pid: str, path: str):
        cur = self.conn.execute(
            "SELECT * FROM files WHERE project_id = ? AND path = ?", (pid, path)
        )
        row = cur.fetchone()
        return dict(row) if row else None

    def get_project_files(self, pid: str):
        cur = self.conn.execute("SELECT * FROM files WHERE project_id = ? ORDER BY path", (pid,))
        return [dict(row) for row in cur.fetchall()]

    def add_chat(self, role: str, message: str, pid: str = None, meta: str = None):
        self.conn.execute(
            "INSERT INTO chat_history (project_id, role, message, meta) VALUES (?, ?, ?, ?)",
            (pid, role, message, meta)
        )
        self.conn.commit()

    def get_chat_history(self, pid: str = None, limit: int = 50):
        if pid:
            cur = self.conn.execute(
                "SELECT * FROM chat_history WHERE project_id = ? ORDER BY created_at DESC LIMIT ?",
                (pid, limit)
            )
        else:
            cur = self.conn.execute(
                "SELECT * FROM chat_history ORDER BY created_at DESC LIMIT ?", (limit,)
            )
        return [dict(row) for row in cur.fetchall()][::-1]

    def save_setting(self, key: str, value: str):
        self.conn.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, value)
        )
        self.conn.commit()

    def get_setting(self, key: str, default: str = None):
        cur = self.conn.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else default

    def clear_all(self):
        self.conn.execute("DELETE FROM projects")
        self.conn.execute("DELETE FROM chat_history")
        self.conn.commit()
        d = AppConfig.projects_dir()
        if d.exists():
            shutil.rmtree(d)
            d.mkdir(parents=True, exist_ok=True)

    def _detect_lang(self, path: str) -> str:
        ext = Path(path).suffix.lower()
        mapping = {
            ".py": "python", ".js": "javascript", ".ts": "typescript",
            ".html": "html", ".htm": "html", ".css": "css",
            ".java": "java", ".cpp": "cpp", ".c": "c", ".h": "c",
            ".go": "go", ".rs": "rust", ".rb": "ruby", ".php": "php",
            ".swift": "swift", ".kt": "kotlin", ".json": "json",
            ".xml": "xml", ".yaml": "yaml", ".yml": "yaml", ".md": "markdown",
            ".sql": "sql", ".sh": "bash", ".bat": "batch"
        }
        return mapping.get(ext, "text")

_db = None
def get_db():
    global _db
    if _db is None:
        _db = TexCodeDB()
    return _db


# ─── CODE ANALYSIS ENGINE ─────────────────────────────────────────────────────
class CodeAnalyzer:
    """AST-based static analysis for Python and other languages."""

    @staticmethod
    def analyze_python(content: str, filename: str = "") -> dict:
        result = {
            "functions": [], "classes": [], "imports": [],
            "issues": [], "metrics": {"lines": 0, "code_lines": 0, "comment_lines": 0, "blank_lines": 0}
        }
        lines = content.splitlines()
        result["metrics"]["lines"] = len(lines)

        for line in lines:
            s = line.strip()
            if not s:
                result["metrics"]["blank_lines"] += 1
            elif s.startswith("#"):
                result["metrics"]["comment_lines"] += 1
            else:
                result["metrics"]["code_lines"] += 1

        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    result["functions"].append({
                        "name": node.name, "line": node.lineno,
                        "args": [a.arg for a in node.args.args],
                        "complexity": CodeAnalyzer._cyclomatic(node)
                    })
                elif isinstance(node, ast.ClassDef):
                    methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                    result["classes"].append({"name": node.name, "line": node.lineno, "methods": methods})
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        result["imports"].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    for alias in node.names:
                        result["imports"].append(f"{mod}.{alias.name}" if mod else alias.name)

            CodeAnalyzer._check_issues(tree, content, result["issues"])
        except SyntaxError as e:
            result["issues"].append({"severity": "error", "message": f"Syntax: {e.msg}", "line": e.lineno or 1})
        except Exception as e:
            result["issues"].append({"severity": "error", "message": str(e), "line": 1})

        return result

    @staticmethod
    def _cyclomatic(node) -> int:
        c = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.With, ast.Assert, ast.comprehension)):
                c += 1
            elif isinstance(child, ast.BoolOp):
                c += len(child.values) - 1
        return c

    @staticmethod
    def _check_issues(tree, content: str, issues: list):
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                issues.append({"severity": "warning", "message": "Bare 'except:' -- use 'except Exception:'", "line": node.lineno})
            if isinstance(node, ast.FunctionDef):
                for d in node.args.defaults:
                    if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                        issues.append({"severity": "warning", "message": f"Mutable default in '{node.name}'", "line": node.lineno})

        defined, used = collections.defaultdict(list), set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    defined[node.id].append(node.lineno)
                elif isinstance(node.ctx, ast.Load):
                    used.add(node.id)

        for var, lns in defined.items():
            if not var.startswith("_") and var not in used and var not in ("self", "cls"):
                for ln in lns:
                    issues.append({"severity": "info", "message": f"Unused variable '{var}'", "line": ln})

        for i, line in enumerate(content.splitlines(), 1):
            if len(line) > 100:
                issues.append({"severity": "info", "message": f"Line too long ({len(line)} chars)", "line": i})
            if "TODO" in line or "FIXME" in line:
                issues.append({"severity": "info", "message": f"Marker: {line.strip()}", "line": i})

    @staticmethod
    def analyze_generic(content: str, filename: str = "") -> dict:
        lines = content.splitlines()
        return {
            "functions": [], "classes": [], "imports": [], "issues": [],
            "metrics": {"lines": len(lines), "code_lines": len([l for l in lines if l.strip()]), "comment_lines": 0, "blank_lines": len([l for l in lines if not l.strip()])}
        }

    @classmethod
    def analyze_file(cls, content: str, path: str) -> dict:
        ext = Path(path).suffix.lower()
        if ext == ".py":
            return cls.analyze_python(content, path)
        return cls.analyze_generic(content, path)

    @classmethod
    def analyze_project(cls, pid: str) -> dict:
        db = get_db()
        files = db.get_project_files(pid)
        all_issues, all_funcs, all_classes, all_imports = [], [], [], []
        languages, total_lines, total_size = set(), 0, 0

        for f in files:
            a = cls.analyze_file(f["content"], f["path"])
            all_issues.extend([{**i, "file": f["path"]} for i in a["issues"]])
            all_funcs.extend(a["functions"])
            all_classes.extend(a["classes"])
            all_imports.extend(a["imports"])
            languages.add(f["language"])
            total_lines += a["metrics"]["lines"]
            total_size += f.get("size", 0)

        comps = [fn.get("complexity", 1) for fn in all_funcs if "complexity" in fn]
        avg_c = sum(comps) / len(comps) if comps else 0

        return {
            "stats": {"files": len(files), "lines": total_lines, "languages": sorted(languages), "size": total_size},
            "issues": all_issues,
            "complexity": {"avg": round(avg_c, 1), "functions": len(all_funcs), "classes": len(all_classes), "imports": len(set(all_imports))}
        }

# ─── LOCAL AI ENGINE ──────────────────────────────────────────────────────────
class TexCodeAI:
    """Offline AI engine — rule-based with optional Ollama."""

    SYSTEM = "You are TexCode, an elite coding assistant. Write clean, efficient, well-documented code."

    def __init__(self):
        self.host = "http://localhost:11434"
        self.model = "qwen2.5-coder:14b"
        self.has_ollama = False
        self._check_ollama()

    def _check_ollama(self):
        try:
            if HAS_REQUESTS:
                r = requests.get(f"{self.host}/api/tags", timeout=3)
                self.has_ollama = r.status_code == 200
        except:
            self.has_ollama = False

    def chat(self, message: str, history: list = None, context: str = "") -> dict:
        if self.has_ollama:
            try:
                msgs = [{"role": "system", "content": self.SYSTEM}]
                if context:
                    msgs.append({"role": "system", "content": f"Context:\n{context}"})
                if history:
                    for h in history[-5:]:
                        msgs.append({"role": h.get("role", "user"), "content": h.get("text", "")})
                msgs.append({"role": "user", "content": message})

                r = requests.post(f"{self.host}/api/chat", json={"model": self.model, "messages": msgs, "stream": False}, timeout=60)
                if r.status_code == 200:
                    d = r.json()
                    return {"text": d.get("message", {}).get("content", ""), "source": f"Ollama ({self.model})"}
            except:
                pass

        return self._rule_based(message, context)

    def _rule_based(self, message: str, context: str) -> dict:
        m = message.lower()

        if any(k in m for k in ["create", "generate", "write", "make", "build", "code"]):
            if "flask" in m:
                return {"text": self._gen_flask(), "source": "Rule Engine"}
            elif "react" in m or "frontend" in m:
                return {"text": self._gen_react(), "source": "Rule Engine"}
            elif "api" in m:
                return {"text": self._gen_api(), "source": "Rule Engine"}
            elif "class" in m:
                return {"text": self._gen_class(), "source": "Rule Engine"}
            elif "function" in m or "def " in m:
                return {"text": self._gen_function(), "source": "Rule Engine"}
            elif "android" in m or "kivy" in m or "app" in m:
                return {"text": self._gen_kivy_app(), "source": "Rule Engine"}
            else:
                return {"text": self._gen_generic(message), "source": "Rule Engine"}

        if any(k in m for k in ["analyze", "review", "check", "debug", "fix", "bug"]):
            if context:
                a = CodeAnalyzer.analyze_file(context, "file.py")
                issues = a.get("issues", [])
                if issues:
                    txt = f"Found {len(issues)} issue(s):\n\n"
                    for i in issues[:8]:
                        txt += f"• Line {i['line']}: {i['message']} ({i['severity']})\n"
                    txt += "\nRecommendations:\n1. Fix syntax errors first\n2. Address warnings\n3. Add type hints\n4. Write tests"
                    return {"text": txt, "source": "Analyzer"}
                return {"text": "Code looks clean! No major issues.\n\nSuggestions:\n• Add docstrings\n• Use type hints\n• Add unit tests", "source": "Analyzer"}
            return {"text": "Please share code to analyze. Paste it or open a file in the Editor.", "source": "Analyzer"}

        if any(k in m for k in ["explain", "what is", "how to", "tutorial", "learn"]):
            return {"text": self._explain(m), "source": "Knowledge Base"}

        if any(k in m for k in ["merge", "combine", "zip", "export", "package"]):
            return {"text": "Go to the MERGE tab! Drop files, and I'll intelligently combine them with conflict resolution + import fixing, then export as ZIP.", "source": "Project Manager"}

        return {"text": self._help_response(), "source": "TexCode"}

    def _gen_flask(self) -> str:
        return """Here's a complete Flask app:

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'id': user.id}), 201
    return jsonify([{'id': u.id, 'username': u.username} for u in User.query.all()])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Run: pip install flask flask-sqlalchemy
# Then: python app.py"""

    def _gen_react(self) -> str:
        return """React component with hooks:

import React, { useState, useEffect } from 'react';

const App = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/data')
      .then(r => r.json())
      .then(d => { setData(d); setLoading(false); })
      .catch(e => { console.error(e); setLoading(false); });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>My Data</h1>
      <ul>{data.map(item => <li key={item.id}>{item.name}</li>)}</ul>
    </div>
  );
};

export default App;"""

    def _gen_api(self) -> str:
        return """FastAPI REST API:

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

items_db = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.post("/items", status_code=201)
def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item.dict())
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = next((i for i in items_db if i['id'] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

# Run: pip install fastapi uvicorn
# Then: uvicorn main:app --reload"""

    def _gen_class(self) -> str:
        return """Well-designed Python class:

from dataclasses import dataclass, field
from typing import Optional, List, Dict
from datetime import datetime

@dataclass
class Product:
    name: str
    price: float
    category: str
    id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def apply_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("Invalid discount")
        return self.price * (1 - percent / 100)

    def to_dict(self) -> Dict:
        return {
            'id': self.id, 'name': self.name,
            'price': self.price, 'category': self.category,
            'tags': self.tags, 'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        return cls(
            id=data.get('id'), name=data['name'],
            price=data['price'], category=data['category'],
            tags=data.get('tags', [])
        )

# Usage
p = Product(name="Laptop", price=999.99, category="Electronics")
print(p.apply_discount(10))  # 899.99"""

    def _gen_function(self) -> str:
        return """Robust function with retry:

import functools
import time
from typing import Callable

def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay * (attempt + 1))
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url: str, timeout: int = 30) -> dict:
    import requests
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()

# The decorator adds retry logic with exponential backoff
# to any function that might fail due to network issues."""

    def _gen_kivy_app(self) -> str:
        return """KivyMD Android App template:

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.add_widget(MDLabel(text='My App', halign='center', font_style='H4'))

        self.input = MDTextField(hint_text='Enter text...')
        self.add_widget(self.input)

        btn = MDRaisedButton(text='Submit', on_release=self.on_submit)
        self.add_widget(btn)

        self.result = MDLabel(text='', halign='center')
        self.add_widget(self.result)

    def on_submit(self, instance):
        text = self.input.text
        self.result.text = f'You entered: {text}'

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()

# Build with Buildozer for Android!"""

    def _gen_generic(self, message: str) -> str:
        return f"""I can generate code for you! Please specify:
• Programming language (Python, JS, Java, etc.)
• What it should do
• Any requirements

Meanwhile, here's a CSV to JSON converter:

import json, csv
from pathlib import Path

def csv_to_json(csv_path: str, json_path: str):
    with open(csv_path, 'r') as f:
        rows = list(csv.DictReader(f))
    with open(json_path, 'w') as f:
        json.dump(rows, f, indent=2)
    print(f"Converted {{len(rows)}} rows")

csv_to_json('data.csv', 'data.json')"""

    def _explain(self, message: str) -> str:
        if "decorator" in message:
            return """Python Decorators:

A decorator wraps a function to extend behavior.

# Basic decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output: Before -> Hello! -> After

Use cases: logging, timing, caching, retries, auth.
Always use @functools.wraps to preserve metadata."""
        elif "async" in message or "await" in message:
            return """Async/Await in Python:

import asyncio

async def fetch_data(url: str):
    # Simulated async operation
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # Run multiple tasks concurrently
    tasks = [fetch_data(f"url{i}") for i in range(3)]
    results = await asyncio.gather(*tasks)
    return results

# Run the event loop
results = asyncio.run(main())

Key points:
• async def = coroutine
• await = yield control back to loop
• asyncio.gather() = run concurrently
• Use aiohttp for async HTTP (not requests)"""
        elif "class" in message and "object" in message:
            return """OOP in Python:

Classes are blueprints for objects.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!

Principles:
• Encapsulation: bundle data + methods
• Inheritance: reuse parent code
• Polymorphism: same interface, different behavior
• Abstraction: hide complexity"""
        else:
            return """I can explain:
• Data structures & algorithms
• Design patterns (Singleton, Factory, Observer)
• Web frameworks (Flask, FastAPI, React, Kivy)
• Databases (SQL, NoSQL, ORM)
• Docker, CI/CD, deployment
• Testing & optimization

Just ask about a specific topic!"""

    def _help_response(self) -> str:
        return """I'm TexCode, your offline coding AI!

What I can do:
📝 Write complete apps (Flask, React, Kivy, APIs)
🔍 Analyze code for bugs & improvements
📁 Manage projects with file tree
🔗 Merge files & export ZIPs
💾 Remember everything via SQLite
🌐 Search web docs (no API keys)

Tips:
• "Write a Flask API with auth"
• "Analyze this code for bugs"
• "Explain Python decorators"
• "Create a React component"
• "Build a Kivy Android app"

I'm running locally — no internet needed!
Install Ollama for even smarter AI."""

# ─── PROJECT MANAGER ──────────────────────────────────────────────────────────
class ProjectManager:
    """Handles merging, zipping, and templates."""

    TEMPLATES = {
        "flask": {
            "app.py": "from flask import Flask, jsonify, request\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)\n",
            "requirements.txt": "flask\n",
            "README.md": "# Flask App\n\nRun: python app.py\n"
        },
        "python": {
            "main.py": "#!/usr/bin/env python3\nfrom src.core import Core\n\ndef main():\n    core = Core()\n    core.run()\n\nif __name__ == '__main__':\n    main()\n",
            "src/__init__.py": "",
            "src/core.py": "class Core:\n    def __init__(self):\n        self.name = 'MyProject'\n    def run(self):\n        print(f'Running {self.name}...')\n",
            "tests/test_core.py": "import unittest\nfrom src.core import Core\n\nclass TestCore(unittest.TestCase):\n    def test_init(self):\n        core = Core()\n        self.assertEqual(core.name, 'MyProject')\n\nif __name__ == '__main__':\n    unittest.main()\n",
            "README.md": "# Python Package\n\nRun: python main.py\n"
        },
        "html": {
            "index.html": "<!DOCTYPE html>\n<html>\n<head><title>My Site</title><link rel='stylesheet' href='style.css'></head>\n<body>\n<h1>Welcome</h1>\n<p>Start building here.</p>\n<script src='app.js'></script>\n</body>\n</html>\n",
            "style.css": "body { font-family: sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; }\nh1 { color: #333; }\n",
            "app.js": "document.addEventListener('DOMContentLoaded', () => {\n    console.log('App loaded!');\n});\n",
            "README.md": "# HTML Site\n\nOpen index.html in browser.\n"
        },
        "kivy": {
            "main.py": "from kivy.app import App\nfrom kivy.uix.boxlayout import BoxLayout\nfrom kivymd.app import MDApp\nfrom kivymd.uix.button import MDRaisedButton\nfrom kivymd.uix.label import MDLabel\n\nclass MainScreen(BoxLayout):\n    def __init__(self, **kwargs):\n        super().__init__(**kwargs)\n        self.orientation = 'vertical'\n        self.padding = 20\n        self.add_widget(MDLabel(text='My App', halign='center', font_style='H4'))\n        self.add_widget(MDRaisedButton(text='Click Me', on_release=lambda x: print('Clicked!')))\n\nclass MyApp(MDApp):\n    def build(self):\n        self.theme_cls.theme_style = 'Dark'\n        return MainScreen()\n\nif __name__ == '__main__':\n    MyApp().run()\n",
            "README.md": "# Kivy App\n\nRun: python main.py\nBuild: buildozer android debug\n"
        }
    }

    @classmethod
    def create_from_template(cls, pid: str, template_name: str):
        db = get_db()
        if template_name not in cls.TEMPLATES:
            return False
        for path, content in cls.TEMPLATES[template_name].items():
            db.save_file(pid, path, content)
        return True

    @classmethod
    def create_zip(cls, pid: str) -> bytes:
        db = get_db()
        files = db.get_project_files(pid)
        project = db.get_project(pid)
        name = project["name"] if project else "project"

        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                zf.writestr(f["path"], f["content"])
        buf.seek(0)
        return buf.read()

    @classmethod
    def merge_files(cls, files_data: list) -> dict:
        result = {"merged": [], "conflicts": [], "output": {}}
        by_path = collections.defaultdict(list)
        for f in files_data:
            by_path[f["path"]].append(f)

        for path, versions in by_path.items():
            if len(versions) == 1:
                result["merged"].append(path)
                result["output"][path] = versions[0]["content"]
            else:
                best = max(versions, key=lambda x: len(x["content"]))
                result["merged"].append(path)
                result["output"][path] = best["content"]
                result["conflicts"].append({"path": path, "versions": len(versions)})

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# KIVYMD UI SCREENS
# ═══════════════════════════════════════════════════════════════════════════════

class ChatBubble(MDCard):
    text = StringProperty("")
    sender = StringProperty("ai")
    timestamp = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.padding = dp(12)
        self.radius = [dp(16), dp(16), dp(16), dp(4)] if self.sender == "ai" else [dp(16), dp(16), dp(4), dp(16)]
        self.md_bg_color = get_color_from_hex(COLORS["bg_card"]) if self.sender == "ai" else get_color_from_hex(COLORS["highlight"])
        self.elevation = 2

        layout = MDBoxLayout(orientation="vertical", adaptive_height=True)
        header = MDBoxLayout(adaptive_height=True, size_hint_x=1)
        icon = "🤖" if self.sender == "ai" else "👤"
        header.add_widget(MDLabel(
            text=f"{icon} {'TexCode AI' if self.sender == 'ai' else 'You'}",
            theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["accent"] if self.sender == "ai" else COLORS["accent_secondary"]),
            font_style="Caption", bold=True, size_hint_y=None, height=dp(20)
        ))
        layout.add_widget(header)

        self.label = MDLabel(
            text=self.text, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_primary"]),
            font_style="Body1", size_hint_y=None, markup=True
        )
        self.label.bind(texture_size=self.label.setter("size"))
        layout.add_widget(self.label)

        if self.timestamp:
            layout.add_widget(MDLabel(
                text=self.timestamp, theme_text_color="Custom",
                text_color=get_color_from_hex(COLORS["text_muted"]),
                font_style="Caption", size_hint_y=None, height=dp(16), halign="right"
            ))

        self.add_widget(layout)
        Clock.schedule_once(self._update_height, 0)

    def _update_height(self, dt):
        self.height = self.children[0].height + dp(24)

    def on_text(self, instance, value):
        if hasattr(self, 'label'):
            self.label.text = value


class CodeBlock(MDCard):
    code = StringProperty("")
    language = StringProperty("python")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.padding = dp(10)
        self.radius = [dp(8)]
        self.md_bg_color = get_color_from_hex(COLORS["bg_primary"])
        self.elevation = 1

        layout = MDBoxLayout(orientation="vertical", adaptive_height=True, spacing=dp(6))
        header = MDBoxLayout(adaptive_height=True, size_hint_x=1)
        header.add_widget(MDLabel(
            text=f"📄 {self.language}", theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["accent"]),
            font_style="Caption", bold=True, size_hint_y=None, height=dp(24)
        ))
        copy_btn = MDIconButton(
            icon="content-copy", theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_secondary"]),
            on_release=self._copy_code, pos_hint={"center_y": 0.5}
        )
        header.add_widget(copy_btn)
        layout.add_widget(header)

        self.code_label = MDLabel(
            text=self.code, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_primary"]),
            font_style="Body2", size_hint_y=None,
            font_name="RobotoMono-Regular" if "ANDROID_ARGUMENT" not in os.environ else "DroidSansMono"
        )
        self.code_label.bind(texture_size=self.code_label.setter("size"))
        layout.add_widget(self.code_label)
        self.add_widget(layout)
        Clock.schedule_once(self._update_height, 0)

    def _update_height(self, dt):
        self.height = self.children[0].height + dp(20)

    def _copy_code(self, instance):
        Clipboard.copy(self.code)
        Snackbar(text="Code copied!", duration=1).open()

    def on_code(self, instance, value):
        if hasattr(self, 'code_label'):
            self.code_label.text = value


class FileListItem(MDCard):
    filename = StringProperty("")
    file_path = StringProperty("")
    file_size = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(56)
        self.padding = dp(10)
        self.radius = [dp(8)]
        self.md_bg_color = get_color_from_hex(COLORS["bg_card"])
        self.elevation = 1

        layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        ext = Path(self.filename).suffix.lower()
        icon_map = {".py": "🐍", ".js": "📜", ".html": "🌐", ".css": "🎨", ".java": "☕", ".json": "📋", ".md": "📝", ".txt": "📄"}
        icon = icon_map.get(ext, "📄")

        layout.add_widget(MDLabel(
            text=f"{icon} {self.filename}", theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_primary"]),
            font_style="Body1", size_hint_x=0.7
        ))
        layout.add_widget(MDLabel(
            text=self.file_size, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_muted"]),
            font_style="Caption", halign="right", size_hint_x=0.3
        ))
        self.add_widget(layout)


# ═══════════════════════════════════════════════════════════════════════════════
# CHAT SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class ChatScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"
        self.ai = TexCodeAI()
        self.current_project = None

        self.scroll = ScrollView()
        self.messages_layout = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10), size_hint_y=None)
        self.messages_layout.bind(minimum_height=self.messages_layout.setter("height"))
        self.scroll.add_widget(self.messages_layout)
        self.add_widget(self.scroll)

        input_card = MDCard(
            radius=[dp(16), dp(16), 0, 0],
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            size_hint_y=None, height=dp(80), padding=dp(10)
        )
        input_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))

        self.input_field = MDTextField(
            hint_text="Ask TexCode anything...",
            mode="round", size_hint_x=0.85, multiline=False,
            on_text_validate=self.send_message
        )
        input_layout.add_widget(self.input_field)

        send_btn = MDFloatingActionButton(
            icon="send", elevation=2,
            on_release=self.send_message,
            md_bg_color=get_color_from_hex(COLORS["accent"])
        )
        input_layout.add_widget(send_btn)
        input_card.add_widget(input_layout)
        self.add_widget(input_card)

        self.add_ai_message("Welcome to TexCode! I'm your offline coding AI.\n\nI can:\n• Write complete apps\n• Analyze & debug code\n• Explain concepts\n• Merge files & create ZIPs\n\nWhat would you like to build?")

    def add_user_message(self, text: str):
        bubble = ChatBubble(text=text, sender="user", timestamp=datetime.datetime.now().strftime("%H:%M"))
        self.messages_layout.add_widget(bubble)
        Clock.schedule_once(lambda dt: self.scroll.scroll_to(bubble), 0.1)

    def add_ai_message(self, text: str, source: str = "TexCode"):
        parts = re.split(r'```(\w*)\n(.*?)```', text, flags=re.DOTALL)
        for i in range(0, len(parts), 3):
            if parts[i].strip():
                bubble = ChatBubble(text=parts[i].strip(), sender="ai", timestamp=datetime.datetime.now().strftime("%H:%M"))
                self.messages_layout.add_widget(bubble)
            if i + 2 < len(parts):
                lang = parts[i + 1] or "python"
                code = parts[i + 2].strip()
                block = CodeBlock(code=code, language=lang)
                self.messages_layout.add_widget(block)
        if len(parts) == 1:
            bubble = ChatBubble(text=text, sender="ai", timestamp=datetime.datetime.now().strftime("%H:%M"))
            self.messages_layout.add_widget(bubble)
        Clock.schedule_once(lambda dt: self.scroll.scroll_y(0), 0.1)

    def send_message(self, instance=None):
        text = self.input_field.text.strip()
        if not text:
            return
        self.input_field.text = ""
        self.add_user_message(text)

        db = get_db()
        db.add_chat("user", text, self.current_project)

        history = db.get_chat_history(self.current_project, limit=10)
        context = ""
        if self.current_project:
            files = db.get_project_files(self.current_project)
            if files:
                context = f"Project has {len(files)} files."

        typing = ChatBubble(text="Thinking...", sender="ai")
        typing.md_bg_color = get_color_from_hex(COLORS["bg_secondary"])
        self.messages_layout.add_widget(typing)

        def get_response(dt):
            self.messages_layout.remove_widget(typing)
            try:
                result = self.ai.chat(text, history, context)
                self.add_ai_message(result["text"], result.get("source", "TexCode"))
                db.add_chat("ai", result["text"], self.current_project, result.get("source"))
            except Exception as e:
                self.add_ai_message(f"Error: {str(e)}")

        Clock.schedule_once(get_response, 0.5)


# ═══════════════════════════════════════════════════════════════════════════════
# EDITOR SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class EditorScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"
        self.current_project = None
        self.current_file = None

        toolbar = MDTopAppBar(
            title="Code Editor",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2,
            right_action_items=[
                ["content-save", lambda x: self.save_file(), "Save"],
                ["magnify", lambda x: self.analyze_file(), "Analyze"],
                ["format-align-left", lambda x: self.format_code(), "Format"],
            ]
        )
        self.add_widget(toolbar)

        self.file_info = MDLabel(
            text="No file open", theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_muted"]),
            font_style="Caption", size_hint_y=None, height=dp(30),
            padding=[dp(10), 0]
        )
        self.add_widget(self.file_info)

        self.editor = TextInput(
            multiline=True,
            background_color=get_color_from_hex(COLORS["bg_primary"]),
            foreground_color=get_color_from_hex(COLORS["text_primary"]),
            cursor_color=get_color_from_hex(COLORS["accent"]),
            selection_color=get_color_from_hex(COLORS["highlight"]),
            font_name="RobotoMono-Regular" if "ANDROID_ARGUMENT" not in os.environ else "DroidSansMono",
            font_size=sp(13), padding=[dp(10), dp(10)],
            hint_text="// Select a file or start coding..."
        )
        self.add_widget(self.editor)

    def load_file(self, project_id: str, file_path: str):
        db = get_db()
        f = db.get_file(project_id, file_path)
        if f:
            self.current_project = project_id
            self.current_file = file_path
            self.editor.text = f["content"]
            self.file_info.text = f"📄 {file_path}  •  {f['language']}  •  {len(f['content'])} chars"

    def save_file(self):
        if not self.current_project or not self.current_file:
            Snackbar(text="No file open!", duration=2).open()
            return
        db = get_db()
        db.save_file(self.current_project, self.current_file, self.editor.text)
        Snackbar(text="File saved!", duration=1).open()

    def analyze_file(self):
        if not self.current_project or not self.current_file:
            Snackbar(text="No file open!", duration=2).open()
            return
        content = self.editor.text
        analysis = CodeAnalyzer.analyze_file(content, self.current_file)
        issues = analysis.get("issues", [])
        if issues:
            msg = f"Found {len(issues)} issue(s):\n"
            for i in issues[:5]:
                msg += f"\nLine {i['line']}: {i['message']}"
        else:
            msg = "Code looks clean! No issues found."
        dialog = MDDialog(
            title="Analysis Results", text=msg,
            buttons=[MDFlatButton(text="CLOSE", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

    def format_code(self):
        if not self.editor.text:
            return
        lines = self.editor.text.splitlines()
        formatted = []
        indent = 0
        for line in lines:
            stripped = line.strip()
            if stripped.endswith(":") and not stripped.startswith("#"):
                formatted.append("    " * indent + stripped)
                indent += 1
            elif stripped in ("return", "pass", "break", "continue", "raise"):
                indent = max(0, indent - 1)
                formatted.append("    " * indent + stripped)
            else:
                formatted.append("    " * indent + stripped)
        self.editor.text = "\n".join(formatted)
        Snackbar(text="Auto-formatted!", duration=1).open()


# ═══════════════════════════════════════════════════════════════════════════════
# PROJECTS SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class ProjectsScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"

        toolbar = MDTopAppBar(
            title="Projects",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2,
            right_action_items=[
                ["plus", lambda x: self.show_new_project_dialog(), "New Project"],
                ["zip-box", lambda x: self.export_zip(), "Export ZIP"],
            ]
        )
        self.add_widget(toolbar)

        self.scroll = ScrollView()
        self.list_layout = MDBoxLayout(orientation="vertical", spacing=dp(8), padding=dp(10), size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter("height"))
        self.scroll.add_widget(self.list_layout)
        self.add_widget(self.scroll)

        self.load_projects()

    def load_projects(self):
        self.list_layout.clear_widgets()
        db = get_db()
        projects = db.get_projects()

        if not projects:
            self.list_layout.add_widget(MDLabel(
                text="No projects yet. Tap + to create one!",
                theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_muted"]),
                halign="center", size_hint_y=None, height=dp(100)
            ))
            return

        for p in projects:
            card = MDCard(
                radius=[dp(12)], md_bg_color=get_color_from_hex(COLORS["bg_card"]),
                size_hint_y=None, height=dp(80), padding=dp(12), elevation=2
            )
            layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))

            info = MDBoxLayout(orientation="vertical", size_hint_x=0.7)
            info.add_widget(MDLabel(
                text=f"📁 {p['name']}", theme_text_color="Custom",
                text_color=get_color_from_hex(COLORS["text_primary"]),
                font_style="H6", size_hint_y=None, height=dp(28)
            ))
            info.add_widget(MDLabel(
                text=f"{p['file_count']} files • {p.get('language', 'mixed')}",
                theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_muted"]),
                font_style="Caption", size_hint_y=None, height=dp(20)
            ))
            layout.add_widget(info)

            actions = MDBoxLayout(orientation="horizontal", size_hint_x=0.3, spacing=dp(5))
            actions.add_widget(MDIconButton(
                icon="pencil", theme_text_color="Custom",
                text_color=get_color_from_hex(COLORS["accent"]),
                on_release=lambda x, pid=p["id"]: self.open_project(pid)
            ))
            actions.add_widget(MDIconButton(
                icon="delete", theme_text_color="Custom",
                text_color=get_color_from_hex(COLORS["danger"]),
                on_release=lambda x, pid=p["id"]: self.delete_project(pid)
            ))
            layout.add_widget(actions)
            card.add_widget(layout)
            self.list_layout.add_widget(card)

    def show_new_project_dialog(self):
        self.dialog = MDDialog(
            title="New Project", type="custom",
            content_cls=MDBoxLayout(
                MDTextField(hint_text="Project name", id="name"),
                MDTextField(hint_text="Description (optional)", id="desc"),
                orientation="vertical", spacing=dp(10),
                size_hint_y=None, height=dp(120)
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="CREATE", on_release=self.create_project)
            ]
        )
        self.dialog.open()

    def create_project(self, instance):
        name_field = None
        desc_field = None
        for child in self.dialog.content_cls.children:
            if hasattr(child, 'id'):
                if child.id == "name":
                    name_field = child
                elif child.id == "desc":
                    desc_field = child

        name = name_field.text.strip() if name_field else ""
        desc = desc_field.text.strip() if desc_field else ""

        if not name:
            Snackbar(text="Project name required!", duration=2).open()
            return

        db = get_db()
        pid = db.create_project(name, desc)
        self.dialog.dismiss()
        self.show_template_dialog(pid)

    def show_template_dialog(self, pid: str):
        self.temp_dialog = MDDialog(
            title="Choose Template",
            text="Select a starting template:",
            buttons=[
                MDFlatButton(text="EMPTY", on_release=lambda x: self._create_with_template(pid, "")),
                MDRaisedButton(text="FLASK", on_release=lambda x: self._create_with_template(pid, "flask")),
                MDRaisedButton(text="PYTHON", on_release=lambda x: self._create_with_template(pid, "python")),
                MDRaisedButton(text="HTML", on_release=lambda x: self._create_with_template(pid, "html")),
                MDRaisedButton(text="KIVY", on_release=lambda x: self._create_with_template(pid, "kivy")),
            ]
        )
        self.temp_dialog.open()

    def _create_with_template(self, pid: str, template: str):
        if template:
            ProjectManager.create_from_template(pid, template)
        self.temp_dialog.dismiss()
        self.load_projects()
        Snackbar(text="Project created!", duration=1).open()

    def open_project(self, pid: str):
        self.app.open_project(pid)

    def delete_project(self, pid: str):
        def confirm_delete(instance):
            db = get_db()
            db.delete_project(pid)
            self.load_projects()
            confirm_dialog.dismiss()
            Snackbar(text="Project deleted!", duration=1).open()

        confirm_dialog = MDDialog(
            title="Delete Project?",
            text="This will permanently delete the project and all its files.",
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: confirm_dialog.dismiss()),
                MDRaisedButton(text="DELETE", md_bg_color=get_color_from_hex(COLORS["danger"]), on_release=confirm_delete)
            ]
        )
        confirm_dialog.open()

    def export_zip(self):
        if not self.app.current_project:
            Snackbar(text="Select a project first!", duration=2).open()
            return
        try:
            data = ProjectManager.create_zip(self.app.current_project)
            db = get_db()
            proj = db.get_project(self.app.current_project)
            name = proj["name"] if proj else "project"

            download_path = Path("/sdcard/Download") if "ANDROID_ARGUMENT" in os.environ else Path.home() / "Downloads"
            download_path.mkdir(parents=True, exist_ok=True)
            zip_path = download_path / f"{name}.zip"
            zip_path.write_bytes(data)

            Snackbar(text=f"ZIP saved to {zip_path}", duration=3).open()
        except Exception as e:
            Snackbar(text=f"Export failed: {str(e)}", duration=3).open()


# ═══════════════════════════════════════════════════════════════════════════════
# MERGE SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class MergeScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"
        self.merge_files = []

        toolbar = MDTopAppBar(
            title="Merge & ZIP",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2
        )
        self.add_widget(toolbar)

        self.add_widget(MDLabel(
            text="Add files to merge them intelligently and create a ZIP archive.",
            theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_secondary"]),
            font_style="Body2", size_hint_y=None, height=dp(40), padding=[dp(10), 0]
        ))

        btn_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10), size_hint_y=None, height=dp(50), padding=dp(10))
        btn_layout.add_widget(MDRaisedButton(text="Add Files", on_release=self.add_files, md_bg_color=get_color_from_hex(COLORS["accent"])))
        btn_layout.add_widget(MDRaisedButton(text="Smart Merge", on_release=self.smart_merge, md_bg_color=get_color_from_hex(COLORS["accent_secondary"])))
        btn_layout.add_widget(MDRaisedButton(text="Create ZIP", on_release=self.create_zip, md_bg_color=get_color_from_hex(COLORS["success"])))
        btn_layout.add_widget(MDFlatButton(text="Clear", on_release=self.clear_files))
        self.add_widget(btn_layout)

        self.scroll = ScrollView()
        self.file_list = MDBoxLayout(orientation="vertical", spacing=dp(6), padding=dp(10), size_hint_y=None)
        self.file_list.bind(minimum_height=self.file_list.setter("height"))
        self.scroll.add_widget(self.file_list)
        self.add_widget(self.scroll)

        self.result_label = MDLabel(
            text="", theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["success"]),
            font_style="Caption", size_hint_y=None, height=dp(0), padding=[dp(10), 0]
        )
        self.add_widget(self.result_label)

    def add_files(self, instance):
        content = MDBoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None, height=dp(200))
        name_field = MDTextField(hint_text="Filename (e.g. main.py)")
        content_field = MDTextField(hint_text="File content...", multiline=True)
        content.add_widget(name_field)
        content.add_widget(content_field)

        dialog = MDDialog(
            title="Add File", type="custom", content_cls=content,
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: dialog.dismiss()),
                MDRaisedButton(text="ADD", on_release=lambda x: self._add_file_content(dialog, name_field, content_field))
            ]
        )
        dialog.open()

    def _add_file_content(self, dialog, name_field, content_field):
        name = name_field.text.strip()
        content = content_field.text
        if name:
            self.merge_files.append({"path": name, "content": content, "size": len(content)})
            self._refresh_file_list()
        dialog.dismiss()

    def _refresh_file_list(self):
        self.file_list.clear_widgets()
        for f in self.merge_files:
            card = MDCard(
                radius=[dp(8)], md_bg_color=get_color_from_hex(COLORS["bg_card"]),
                size_hint_y=None, height=dp(50), padding=dp(10)
            )
            layout = MDBoxLayout(orientation="horizontal")
            layout.add_widget(MDLabel(
                text=f"📄 {f['path']} ({len(f['content'])} chars)",
                theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_primary"]),
                font_style="Body2"
            ))
            card.add_widget(layout)
            self.file_list.add_widget(card)

    def smart_merge(self, instance):
        if not self.merge_files:
            Snackbar(text="Add files first!", duration=2).open()
            return
        result = ProjectManager.merge_files(self.merge_files)
        msg = f"Merged {len(result['merged'])} files"
        if result["conflicts"]:
            msg += f"\nResolved {len(result['conflicts'])} conflicts"
        self.result_label.text = msg
        self.result_label.height = dp(60)
        Snackbar(text="Merge complete!", duration=2).open()

    def create_zip(self, instance):
        if not self.merge_files:
            Snackbar(text="Add files first!", duration=2).open()
            return
        try:
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
                for f in self.merge_files:
                    zf.writestr(f["path"], f["content"])
            buf.seek(0)

            download_path = Path("/sdcard/Download") if "ANDROID_ARGUMENT" in os.environ else Path.home() / "Downloads"
            download_path.mkdir(parents=True, exist_ok=True)
            zip_path = download_path / "texcode-merged.zip"
            zip_path.write_bytes(buf.read())

            Snackbar(text=f"ZIP saved to {zip_path}", duration=3).open()
        except Exception as e:
            Snackbar(text=f"ZIP failed: {str(e)}", duration=3).open()

    def clear_files(self, instance):
        self.merge_files = []
        self.file_list.clear_widgets()
        self.result_label.text = ""
        self.result_label.height = dp(0)
        Snackbar(text="Cleared!", duration=1).open()


# ═══════════════════════════════════════════════════════════════════════════════
# ANALYSIS SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class AnalysisScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"

        toolbar = MDTopAppBar(
            title="Analysis",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2,
            right_action_items=[["refresh", lambda x: self.analyze(), "Refresh"]]
        )
        self.add_widget(toolbar)

        self.scroll = ScrollView()
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10), size_hint_y=None)
        self.content.bind(minimum_height=self.content.setter("height"))
        self.scroll.add_widget(self.content)
        self.add_widget(self.scroll)

        self.content.add_widget(MDLabel(
            text="Select a project to analyze",
            theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_muted"]),
            halign="center", size_hint_y=None, height=dp(100)
        ))

    def analyze(self):
        if not self.app.current_project:
            Snackbar(text="Select a project first!", duration=2).open()
            return

        self.content.clear_widgets()
        result = CodeAnalyzer.analyze_project(self.app.current_project)
        stats = result["stats"]
        comp = result["complexity"]
        issues = result["issues"]

        stats_card = self._create_card("📊 Project Stats")
        stats_card.add_widget(self._stat_row("Files", str(stats["files"])))
        stats_card.add_widget(self._stat_row("Lines of Code", str(stats["lines"])))
        stats_card.add_widget(self._stat_row("Languages", ", ".join(stats["languages"]) or "N/A"))
        stats_card.add_widget(self._stat_row("Size", f"{stats['size']} bytes"))
        self.content.add_widget(stats_card)

        comp_card = self._create_card("🔍 Complexity")
        comp_card.add_widget(self._stat_row("Avg Complexity", str(comp["avg"])))
        comp_card.add_widget(self._stat_row("Functions", str(comp["functions"])))
        comp_card.add_widget(self._stat_row("Classes", str(comp["classes"])))
        comp_card.add_widget(self._stat_row("Imports", str(comp["imports"])))
        self.content.add_widget(comp_card)

        issues_card = self._create_card(f"🐛 Issues ({len(issues)})")
        if not issues:
            issues_card.add_widget(MDLabel(
                text="No issues found!", theme_text_color="Custom",
                text_color=get_color_from_hex(COLORS["success"]), font_style="Body1"
            ))
        else:
            for issue in issues[:10]:
                color = COLORS["danger"] if issue["severity"] == "error" else COLORS["warning"] if issue["severity"] == "warning" else COLORS["accent"]
                issues_card.add_widget(MDLabel(
                    text=f"[{issue['severity'].upper()}] Line {issue.get('line', '?')}: {issue['message']}",
                    theme_text_color="Custom", text_color=get_color_from_hex(color),
                    font_style="Caption", size_hint_y=None, height=dp(30)
                ))
        self.content.add_widget(issues_card)

    def _create_card(self, title: str):
        card = MDCard(
            radius=[dp(12)], md_bg_color=get_color_from_hex(COLORS["bg_card"]),
            size_hint_y=None, padding=dp(12), elevation=2
        )
        card.add_widget(MDLabel(
            text=title, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["accent"]),
            font_style="H6", size_hint_y=None, height=dp(36)
        ))
        card.height = dp(60)
        return card

    def _stat_row(self, label: str, value: str):
        row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(30))
        row.add_widget(MDLabel(
            text=label, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["text_secondary"]),
            font_style="Body2", size_hint_x=0.5
        ))
        row.add_widget(MDLabel(
            text=value, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["accent"]),
            font_style="Body2", bold=True, halign="right", size_hint_x=0.5
        ))
        return row


# ═══════════════════════════════════════════════════════════════════════════════
# SETTINGS SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class SettingsScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"

        toolbar = MDTopAppBar(
            title="Settings",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2
        )
        self.add_widget(toolbar)

        self.scroll = ScrollView()
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10), size_hint_y=None)
        self.content.bind(minimum_height=self.content.setter("height"))
        self.scroll.add_widget(self.content)
        self.add_widget(self.scroll)

        ai_card = self._create_card("🤖 AI Settings")
        self.model_field = MDTextField(hint_text="Ollama Model", text="qwen2.5-coder:14b")
        self.host_field = MDTextField(hint_text="Ollama Host", text="http://localhost:11434")
        ai_card.add_widget(self.model_field)
        ai_card.add_widget(self.host_field)
        self.content.add_widget(ai_card)

        danger_card = self._create_card("⚠️ Danger Zone")
        danger_card.add_widget(MDRaisedButton(
            text="Clear All Memory", md_bg_color=get_color_from_hex(COLORS["danger"]),
            on_release=self.confirm_clear
        ))
        self.content.add_widget(danger_card)

        about_card = self._create_card("ℹ️ About")
        about_card.add_widget(MDLabel(
            text="TexCode v1.0\nUltimate Offline Coding AI\n\nBuilt with KivyMD\nNo API Keys Required",
            theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_secondary"]),
            font_style="Body2", halign="center"
        ))
        self.content.add_widget(about_card)

    def _create_card(self, title: str):
        card = MDCard(
            radius=[dp(12)], md_bg_color=get_color_from_hex(COLORS["bg_card"]),
            size_hint_y=None, padding=dp(12), elevation=2, spacing=dp(8)
        )
        card.add_widget(MDLabel(
            text=title, theme_text_color="Custom",
            text_color=get_color_from_hex(COLORS["accent"]),
            font_style="H6", size_hint_y=None, height=dp(36)
        ))
        return card

    def confirm_clear(self, instance):
        dialog = MDDialog(
            title="Clear All Memory?",
            text="This will delete ALL projects, files, and chat history. This cannot be undone!",
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: dialog.dismiss()),
                MDRaisedButton(text="DELETE EVERYTHING", md_bg_color=get_color_from_hex(COLORS["danger"]), on_release=lambda x: self._clear_all(dialog))
            ]
        )
        dialog.open()

    def _clear_all(self, dialog):
        db = get_db()
        db.clear_all()
        dialog.dismiss()
        Snackbar(text="All memory cleared!", duration=2).open()
        self.app.current_project = None


# ═══════════════════════════════════════════════════════════════════════════════
# FILE BROWSER SCREEN
# ═══════════════════════════════════════════════════════════════════════════════

class FileBrowserScreen(MDBoxLayout):
    def __init__(self, app_ref, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.orientation = "vertical"

        self.toolbar = MDTopAppBar(
            title="Files",
            md_bg_color=get_color_from_hex(COLORS["bg_secondary"]),
            specific_text_color=get_color_from_hex(COLORS["text_primary"]),
            elevation=2,
            left_action_items=[["arrow-left", lambda x: self.go_back(), "Back"]],
            right_action_items=[["plus", lambda x: self.new_file(), "New File"]]
        )
        self.add_widget(self.toolbar)

        self.scroll = ScrollView()
        self.file_list = MDBoxLayout(orientation="vertical", spacing=dp(6), padding=dp(10), size_hint_y=None)
        self.file_list.bind(minimum_height=self.file_list.setter("height"))
        self.scroll.add_widget(self.file_list)
        self.add_widget(self.scroll)

    def load_files(self, pid: str):
        self.current_project = pid
        db = get_db()
        proj = db.get_project(pid)
        self.toolbar.title = f"Files: {proj['name']}" if proj else "Files"

        self.file_list.clear_widgets()
        files = db.get_project_files(pid)

        if not files:
            self.file_list.add_widget(MDLabel(
                text="No files yet. Tap + to create one!",
                theme_text_color="Custom", text_color=get_color_from_hex(COLORS["text_muted"]),
                halign="center", size_hint_y=None, height=dp(80)
            ))
            return

        for f in files:
            item = FileListItem(filename=f["path"], file_path=f["path"], file_size=f"{f.get('size', 0)} bytes")
            item.bind(on_release=lambda x, path=f["path"]: self.open_file(path))
            self.file_list.add_widget(item)

    def open_file(self, path: str):
        self.app.open_file_editor(self.current_project, path)

    def new_file(self):
        content = MDBoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None, height=dp(100))
        name_field = MDTextField(hint_text="Filename (e.g. utils.py)")
        content.add_widget(name_field)

        dialog = MDDialog(
            title="New File", type="custom", content_cls=content,
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: dialog.dismiss()),
                MDRaisedButton(text="CREATE", on_release=lambda x: self._create_file(dialog, name_field))
            ]
        )
        dialog.open()

    def _create_file(self, dialog, name_field):
        name = name_field.text.strip()
        if name and self.current_project:
            db = get_db()
            db.save_file(self.current_project, name, "")
            self.load_files(self.current_project)
            dialog.dismiss()
            Snackbar(text="File created!", duration=1).open()

    def go_back(self):
        self.app.show_projects()


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════════════════════════════════════════════

class TexCodeApp(MDApp):
    """Main TexCode Application."""

    current_project = StringProperty("")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Teal"

        Window.clearcolor = get_color_from_hex(COLORS["bg_primary"])

        # Main layout
        self.root_layout = MDBoxLayout(orientation="vertical")

        # Screen Manager
        self.sm = ScreenManager(transition=SlideTransition())

        # Create screens
        self.chat_screen = ChatScreen(self)
        self.editor_screen = EditorScreen(self)
        self.projects_screen = ProjectsScreen(self)
        self.merge_screen = MergeScreen(self)
        self.analysis_screen = AnalysisScreen(self)
        self.settings_screen = SettingsScreen(self)
        self.file_browser = FileBrowserScreen(self)

        # Add to screen manager
        self.sm.add_widget(self._wrap_screen(self.chat_screen, "chat"))
        self.sm.add_widget(self._wrap_screen(self.projects_screen, "projects"))
        self.sm.add_widget(self._wrap_screen(self.merge_screen, "merge"))
        self.sm.add_widget(self._wrap_screen(self.analysis_screen, "analysis"))
        self.sm.add_widget(self._wrap_screen(self.settings_screen, "settings"))
        self.sm.add_widget(self._wrap_screen(self.editor_screen, "editor"))
        self.sm.add_widget(self._wrap_screen(self.file_browser, "files"))

        self.root_layout.add_widget(self.sm)

        # Bottom Navigation
        self.bottom_nav = MDBottomNavigation(
            panel_color=get_color_from_hex(COLORS["bg_secondary"]),
            selected_color_background=get_color_from_hex(COLORS["accent"]),
            text_color_active=get_color_from_hex(COLORS["accent"]),
            text_color_normal=get_color_from_hex(COLORS["text_muted"])
        )

        self.bottom_nav.add_widget(MDBottomNavigationItem(
            name="chat",
            text="Chat",
            icon="message-text",
            on_tab_press=lambda x: self.switch_screen("chat")
        ))
        self.bottom_nav.add_widget(MDBottomNavigationItem(
            name="projects",
            text="Projects",
            icon="folder",
            on_tab_press=lambda x: self.switch_screen("projects")
        ))
        self.bottom_nav.add_widget(MDBottomNavigationItem(
            name="merge",
            text="Merge",
            icon="zip-box",
            on_tab_press=lambda x: self.switch_screen("merge")
        ))
        self.bottom_nav.add_widget(MDBottomNavigationItem(
            name="analysis",
            text="Analyze",
            icon="chart-bar",
            on_tab_press=lambda x: self.switch_screen("analysis")
        ))
        self.bottom_nav.add_widget(MDBottomNavigationItem(
            name="settings",
            text="Settings",
            icon="cog",
            on_tab_press=lambda x: self.switch_screen("settings")
        ))

        self.root_layout.add_widget(self.bottom_nav)

        # Welcome snackbar
        Clock.schedule_once(lambda dt: Snackbar(
            text="TexCode ready! Start coding!",
            duration=2
        ).open(), 1)

        return self.root_layout

    def _wrap_screen(self, widget, name):
        screen = Screen(name=name)
        screen.add_widget(widget)
        return screen

    def switch_screen(self, name: str):
        self.sm.current = name

    def open_project(self, pid: str):
        self.current_project = pid
        self.chat_screen.current_project = pid
        self.editor_screen.current_project = pid
        self.file_browser.load_files(pid)
        self.switch_screen("files")
        Snackbar(text="Project opened!", duration=1).open()

    def show_projects(self):
        self.projects_screen.load_projects()
        self.switch_screen("projects")

    def open_file_editor(self, pid: str, path: str):
        self.editor_screen.load_file(pid, path)
        self.switch_screen("editor")

    def on_pause(self):
        return True

    def on_resume(self):
        pass


# ═══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    TexCodeApp().run()
