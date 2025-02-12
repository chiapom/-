import streamlit as st

def calculate_life_path_number(birthdate):
    total = sum(int(digit) for digit in birthdate if digit.isdigit())
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(digit) for digit in str(total))
    return total

st.title("数秘術自動計算ツール")

birthdate = st.text_input("生年月日をYYYYMMDD形式で入力してください:")

if birthdate:
    try:
        life_path_number = calculate_life_path_number(birthdate)
        st.write(f"ライフパスナンバーは: {life_path_number}")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
