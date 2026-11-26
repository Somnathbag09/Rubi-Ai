import json
import os
from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

APP_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(APP_DIR, "rubi_memory.json")

KV = """
<RubiRoot>:
    orientation: "vertical"
    padding: "12dp"
    spacing: "8dp"
    canvas.before:
        Color:
            rgba: 0.035, 0.055, 0.11, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size_hint_y: None
        height: "58dp"
        Label:
            text: "[b]RUBI AI[/b]"
            markup: True
            font_size: "24sp"
            color: 0.35, 0.85, 1, 1
        Label:
            text: "PERSONAL ASSISTANT"
            font_size: "11sp"
            color: 0.65, 0.75, 0.9, 1
    Label:
        id: orb
        text: "◉"
        font_size: "72sp"
        color: 0.2, 0.75, 1, 1
        size_hint_y: None
        height: "105dp"
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            id: messages
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            spacing: "8dp"
            padding: "4dp"
    BoxLayout:
        size_hint_y: None
        height: "52dp"
        spacing: "6dp"
        TextInput:
            id: entry
            hint_text: "RUBI-কে কিছু লিখুন..."
            multiline: False
            on_text_validate: root.send_message()
        Button:
            text: "Send"
            size_hint_x: None
            width: "82dp"
            on_release: root.send_message()
    BoxLayout:
        size_hint_y: None
        height: "44dp"
        spacing: "6dp"
        Button:
            text: "সময়"
            on_release: root.quick("সময়")
        Button:
            text: "তারিখ"
            on_release: root.quick("তারিখ")
        Button:
            text: "History"
            on_release: root.quick("আগের কথা")
"""

class RubiRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.welcome, 0.2)

    def welcome(self, *_):
        self.add_message("RUBI", "হ্যালো! আমি RUBI AI। কীভাবে সাহায্য করতে পারি?")

    def add_message(self, who, message):
        from kivy.uix.label import Label
        label = Label(
            text=f"[b]{who}:[/b] {message}",
            markup=True,
            size_hint_y=None,
            halign="left",
            valign="middle",
            color=(0.92, 0.95, 1, 1),
        )
        label.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
        label.bind(texture_size=lambda inst, size: setattr(inst, "height", size[1] + 16))
        self.ids.messages.add_widget(label)
        Clock.schedule_once(lambda *_: setattr(self.ids.messages.parent, "scroll_y", 0), 0.1)

    def quick(self, text):
        self.ids.entry.text = text
        self.send_message()

    def send_message(self):
        text = self.ids.entry.text.strip()
        if not text:
            return
        self.ids.entry.text = ""
        self.add_message("You", text)
        answer = self.reply(text)
        self.add_message("RUBI", answer)
        self.save_memory(text, answer)

    def reply(self, text):
        msg = text.lower().strip()
        if any(x in msg for x in ["হ্যালো", "হাই", "hello", "hi"]):
            return "হ্যালো! তোমার সঙ্গে কথা বলতে ভালো লাগছে।"
        if "তোমার নাম" in msg or "your name" in msg:
            return "আমার নাম RUBI AI।"
        if "সময়" in msg or "time" in msg:
            return "এখন সময়: " + datetime.now().strftime("%I:%M %p")
        if "তারিখ" in msg or "date" in msg:
            return "আজকের তারিখ: " + datetime.now().strftime("%d-%m-%Y")
        if "আগের কথা" in msg or "history" in msg:
            history = self.load_memory()
            if not history:
                return "এখনও কোনো কথোপকথন সংরক্ষিত নেই।"
            return "তোমার শেষ বলা কথা: " + history[-1].get("user", "")
        if "সাহায্য" in msg or "help" in msg:
            return "আমি এখন সময়, তারিখ, সাধারণ greeting এবং chat history দেখাতে পারি। উন্নত AI উত্তরের জন্য নিরাপদ backend/API সংযোগ পরের ধাপে যোগ করতে হবে।"
        return "আমি এখন একটি starter assistant। এই প্রশ্নের উন্নত উত্তর দিতে AI backend সংযোগ প্রয়োজন।"

    def load_memory(self):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return []

    def save_memory(self, user, rubi):
        history = self.load_memory()
        history.append({"user": user, "rubi": rubi, "time": datetime.now().isoformat()})
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(history[-500:], f, ensure_ascii=False, indent=2)
        except OSError:
            pass

class RubiApp(App):
    def build(self):
        Builder.load_string(KV)
        self.title = "RUBI AI"
        return RubiRoot()

if __name__ == "__main__":
    RubiApp().run()
