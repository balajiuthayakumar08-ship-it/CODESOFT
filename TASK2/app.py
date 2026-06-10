import streamlit as st

st.title("🎮 Tic-Tac-Toe")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

board = st.session_state.board

def check_winner(b):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for win in wins:
        a,b1,c = win
        if board[a] == board[b1] == board[c] != "":
            return board[a]
    return None

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        if cols[col].button(board[idx] if board[idx] else " ", key=idx):
            if board[idx] == "":
                board[idx] = "X"

winner = check_winner(board)

if winner:
    st.success(f"🏆 Winner: {winner}")

if st.button("Reset Game"):
    st.session_state.board = [""] * 9
    st.rerun()
