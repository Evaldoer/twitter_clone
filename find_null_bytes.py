import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            try:
                with open(path, "rb") as f:
                    content = f.read()
                    if b"\x00" in content:
                        print("❌ NULL BYTE ENCONTRADO EM:", path)
            except Exception as e:
                print("⚠️ ERRO AO LER:", path, e)