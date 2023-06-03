import streamlit as st

# タイトルの表示
st.title("Streamlitサンプルアプリ")

# テキストの表示
st.text("これはサンプルのテキストです。")

# ヘッダーの表示
st.header("これはヘッダーです。")

# サブヘッダーの表示
st.subheader("これはサブヘッダーです。")

# テキスト入力の表示
user_input = st.text_input("テキストを入力してください。")

# ボタンの表示とクリック時の処理
if st.button("クリック"):
    st.write("ボタンがクリックされました！")

# チェックボックスの表示と選択状態の取得
checkbox_state = st.checkbox("チェックボックス")
if checkbox_state:
    st.write("チェックボックスが選択されています。")

# ラジオボタンの表示と選択状態の取得
radio_option = st.radio("ラジオボタン", ("オプション1", "オプション2"))
st.write("選択されたオプション:", radio_option)

# セレクトボックスの表示と選択状態の取得
select_option = st.selectbox("セレクトボックス", ("オプションA", "オプションB"))
st.write("選択されたオプション:", select_option)

# スライダーの表示と選択状態の取得
slider_value = st.slider("スライダー", 0, 100, 50)
st.write("選択された値:", slider_value)

# サイドバーの表示
st.sidebar.title("サイドバー")
sidebar_option = st.sidebar.selectbox("オプション", ("A", "B", "C"))
st.sidebar.write("選択されたオプション:", sidebar_option)
