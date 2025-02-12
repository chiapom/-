
import streamlit as st

# アルファベットを数字に変換する対応表
alphabet_to_number = {
    'a': 1, 'j': 1, 's': 1,
    'b': 2, 'k': 2, 't': 2,
    'c': 3, 'l': 3, 'u': 3,
    'd': 4, 'm': 4, 'v': 4,
    'e': 5, 'n': 5, 'w': 5,
    'f': 6, 'o': 6, 'x': 6,
    'g': 7, 'p': 7, 'y': 7,
    'h': 8, 'q': 8, 'z': 8,
    'i': 9, 'r': 9
}

# 共通の縮約処理関数
def reduce_number(total, allowed_masters):
    while total > 9 and total not in allowed_masters:
        total = sum(int(digit) for digit in str(total))
    return total

# ライフパスナンバー：生年月日の数字すべてを足す
def calculate_life_path_number(birthdate):
    total = sum(int(digit) for digit in birthdate if digit.isdigit())
    return reduce_number(total, [11, 22, 33])

# ディスティニーナンバー：名前のアルファベットを数字に変換して足す
def calculate_destiny_number(name):
    total = sum(alphabet_to_number[char] for char in name.lower() if char in alphabet_to_number)
    return reduce_number(total, [11, 22, 33])

# ソウルナンバー：名前の母音のみを足す
def calculate_soul_number(name):
    vowels = "aeiou"
    total = sum(alphabet_to_number[char] for char in name.lower() if char in vowels and char in alphabet_to_number)
    return reduce_number(total, [11, 22, 33])

# パーソナリティーナンバー：名前の子音のみを足す
def calculate_personality_number(name):
    vowels = "aeiou"
    total = sum(alphabet_to_number[char] for char in name.lower() if char not in vowels and char in alphabet_to_number)
    return reduce_number(total, [22, 33])

import streamlit as st

# 共通の縮約処理関数（例）
def reduce_number(total, allowed_masters):
    while total > 9 and total not in allowed_masters:
        total = sum(int(digit) for digit in str(total))
    return total

# バースデーナンバーの計算関数
def calculate_birthday_number(day):
    # day は整数として扱う
    return reduce_number(day, [11, 22])


# Streamlitの表示部分

st.title("数秘術自動計算ツール")

st.header("生年月日からの計算")
birthdate = st.text_input("生年月日を西暦8桁で入力してください:")
if birthdate:
    try:
        life_path = calculate_life_path_number(birthdate)
        st.write(f"【ライフパスナンバー】 {life_path}")
    except Exception as e:
        st.error(f"ライフパスナンバー計算中にエラーが発生しました: {e}")

st.header("誕生日からの計算")
# st.number_input ではなく st.text_input を使って初期は空欄にする
birthday_str = st.text_input("誕生日の日付を入力してください (例: 15):")

if birthday_str:
    try:
        day = int(birthday_str)
        # 入力値が 1～31 の範囲かどうかチェック（必要に応じて）
        if 1 <= day <= 31:
            birthday_num = calculate_birthday_number(day)
            st.write(f"【バースデーナンバー】 {birthday_num}")
        else:
            st.error("1から31までの数字を入力してください。")
    except ValueError:
        st.error("有効な数字を入力してください。")


st.header("お名前からの計算（ローマ字）")
name = st.text_input("名前（ローマ字、例: Sato）を入力してください:")
if name:
    destiny = calculate_destiny_number(name)
    soul = calculate_soul_number(name)
    personality = calculate_personality_number(name)
    st.write(f"【ディスティニーナンバー】 {destiny}")
    st.write(f"【ソウルナンバー】 {soul}")
    st.write(f"【パーソナリティーナンバー】 {personality}")
    import streamlit as st






