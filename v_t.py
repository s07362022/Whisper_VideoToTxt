import whisper
from googletrans import Translator

# 載入 Whisper 模型
model = whisper.load_model("medium")

# 轉寫影片中的音訊
result = model.transcribe("7years.mp4")

# 將結果轉換成句子列表
transcription = result["text"]
sentences = transcription.split('. ')

# 初始化翻譯器
translator = Translator()

# 將每個句子翻譯成中文並寫入文件
with open('7years_ly.txt', 'w', encoding='utf-8') as f:
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:  # 確保句子非空
            translated_sentence = translator.translate(sentence, src='en', dest='zh-tw').text
            f.write(sentence + '.\n')  # 寫入英文句子
            f.write(translated_sentence + '\n')  # 寫入對應的中文翻譯
