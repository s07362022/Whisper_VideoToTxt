Using Whisper to Convert Voice to Text in Videos

# Install package

```cmd
pip install git+https://github.com/openai/whisper.git
pip install setuptools-rust
pip install PyQt5 moviepy googletrans==4.0.0-rc1
```

```cmd
# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg
```

# Start

```cmd
python v_t.py
```

Generting an file as ".txt" is translated En to Chinese like as : 

![image](https://github.com/user-attachments/assets/af60a1e5-56c6-468f-aa67-12c2688bccd0)

# Create UI interface 

by using PyQt5 Designer 

![image](https://github.com/user-attachments/assets/706db279-ded5-4571-aa9b-cef59646b74f)

and the code as "ui.ui", need to cover to python code:
```
pyuic5 ui.ui -o main_window.py
```
# Run UI and connect with previous code

```cmd
python main_window.py
```

# result
![image](https://github.com/user-attachments/assets/d775f512-4cf1-464a-807d-cb08025fb977)


