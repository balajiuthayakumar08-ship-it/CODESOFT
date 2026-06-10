import streamlit as st
import random

st.title("🎮 Tic-Tac-Toe AI")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

board = st.session_state.board

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for win in wins:
        a, b, c = win
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None

def ai_move():
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = "O"

winner = check_winner(board)

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col

        if cols[col].button(
            board[idx] if board[idx] else " ",
            key=idx,
            use_container_width=True
        ):
            if board[idx] == "" and winner is None:
                board[idx] = "X"

                winner = check_winner(board)

                if winner is None:
                    ai_move()

winner = check_winner(board)

if winner == "X":
    st.success("🎉 You Win!")
elif winner == "O":
    st.error("🤖 AI Wins!")
elif winner == "Draw":
    st.warning("🤝 Match Draw!")

if st.button("🔄 Reset Game"):
    st.session_state.board = [""] * 9
    st.rerun()
