import requests
import os
import json

class Class_QuoteAPI:
    def __init__(self, json_file='Quote_Data.json'):
        self.json_file = json_file
        self.content = None
        self.author = None
        self.last_error = None

    def get_quote(self):
        """Lấy quote mới từ API và cập nhật thuộc tính content, author"""
        url = "https://api.quotable.io/random"
        try:
            response = requests.get(url, timeout=5, verify=False)
            data = response.json()
            self.content = data.get("content")
            self.author = data.get("author")
            self.last_error = None
            return self.content, self.author
        except Exception as e:
            self.content = None
            self.author = None
            self.last_error = str(e)
            return "Không thể lấy dữ liệu danh ngôn.", self.last_error

    def save_to_json(self):
        """Lưu quote hiện tại vào file json, chỉ khi đã có content và author"""
        if not self.content or not self.author:
            return False
        quote = {
            "content": self.content,
            "author": self.author
        }
        quotes = []
        # Đọc dữ liệu cũ nếu file đã tồn tại
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r", encoding="utf-8") as f:
                    quotes = json.load(f)
            except Exception:
                quotes = []
        # Thêm quote mới nếu chưa trùng
        if quote not in quotes:
            quotes.append(quote)
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(quotes, f, ensure_ascii=False, indent=2)
            return True
        return False
    