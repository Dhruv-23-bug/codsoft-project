const boardEl = document.getElementById("board");
let board = Array(9).fill("");
let gameOver = false;

function renderBoard() {
    boardEl.innerHTML = "";
    board.forEach((val, i) => {
        const cell = document.createElement("div");
        cell.className = "cell";
        cell.textContent = val;
        cell.onclick = () => handleClick(i);
        boardEl.appendChild(cell);
    });
}

function handleClick(index) {
    if (board[index] !== "" || gameOver) return;
    board[index] = "X";
    renderBoard();
    const result = checkWinner();
    if (result) return showResult(result);

    fetch("/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ board }),
    })
    .then(res => res.json())
    .then(data => {
        if (data.move !== null && board[data.move] === "") {
            board[data.move] = "O";
            renderBoard();
            const result = checkWinner();
            if (result) return showResult(result);
        }
    });
}

function checkWinner() {
    const lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    for (let [a, b, c] of lines) {
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            return board[a];
        }
    }
    if (!board.includes("")) return "draw";
    return null;
}

function showResult(result) {
    gameOver = true;
    setTimeout(() => {
        alert(result === "draw" ? "It's a Draw!" : `${result} wins!`);
    }, 100);
}

function resetGame() {
    board = Array(9).fill("");
    gameOver = false;
    renderBoard();
}

renderBoard();
