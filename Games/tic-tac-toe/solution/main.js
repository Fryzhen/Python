const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const emptyCellValue = '_';
const gameSize = 3; // 3 x 3
const allowedPawns = ['X', 'O'];

// current game array
let game = [
  [emptyCellValue, emptyCellValue, emptyCellValue],
  [emptyCellValue, emptyCellValue, emptyCellValue],
  [emptyCellValue, emptyCellValue, emptyCellValue]
];

// index for current player's pawn based on allowedPawns
let currentPlayerPawnIndex = 0;

/**
 * print the current game
 * @param {*} game : the current game array
 */
function printGame(game) {
  // clean screen
  console.clear();

  // title of the checkbord
  console.log('  1 2 3');

  for (let i = 0; i < 3; i++) {
    let str = `${i + 1}|`;

    for (let j = 0; j < 3; j++) {
      str += game[i][j] + '|';
    }

    console.log(str);
  }
}

function printInputRequest() {
  console.log(`Input for player '${allowedPawns[currentPlayerPawnIndex]}': `);
}

/**
 * check if a new user input is valid for the current game
 * @param {*} input : a new user input from terminal
 * @param {*} currGame : the current game array
 * @returns bool value indicating whether the incoming new user input is valid for the current game
 */
function isInputValid(input, currGame) {
  // check if input is a validate number
  if (isNaN(input) || input.length !== 2) {
    return false;
  }

  const ch = input.split('');
  const x = parseInt(ch[0]) - 1;
  const y = parseInt(ch[1]) - 1;

  // check if the input value is in the allowed range
  // check if the input cell is still empty
  if (x < 0 || x >= gameSize
    || y < 0 || y >= gameSize
    || currGame[x][y] === undefined
    || currGame[x][y] !== emptyCellValue) {
    return false;
  }

  return true;
}

/**
 * Update and return a game array based on the latest user input
 * @param {*} input a new user input
 * @param {*} curPlayer the current player's pawn
 * @param {*} currGame the current game
 * @returns a new game array (without modifying the original game array 'currGame')
 */
function updateGame(input, curPlayer, currGame) {
  // make a array copy
  const updatedGame = currGame.slice();

  const ch = input.split('');
  const x = parseInt(ch[0]) - 1, y = parseInt(ch[1]) - 1;
  updatedGame[x][y] = curPlayer;

  return updatedGame;
}

/**
 * Check and end the current game if necessary
 * @param {*} currGame the latest game array
 * @returns bool indicating where the game is end
 */
function endGame(currGame) {
  // all possible win situations
  const winCases = [
    [[0, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[2, 0], [1, 1], [0, 2]],
  ];

  // detect if there is a win case
  for (let i = 0; i < winCases.length; i++) {
    const cell1 = winCases[i][0], cell2 = winCases[i][1], cell3 = winCases[i][2];

    if (currGame[cell1[0]][cell1[1]] !== emptyCellValue
      && currGame[cell1[0]][cell1[1]] === currGame[cell2[0]][cell2[1]]
      && currGame[cell1[0]][cell1[1]] === currGame[cell3[0]][cell3[1]]) {
      // play wins the game
      console.log(`Winner is player '${currGame[cell1[0]][cell1[1]]}'`);
      return true;
    }
  }

  // detect if there is still empty cells
  for (let i = 0; i < currGame.length; i++) {
    if (currGame[i].includes(emptyCellValue)) {
      return false;
    }
  }

  // checkbord is full
  console.log('Draw game');
  return true;
}

function main() {
  // start with an empty game
  printGame(game);
  printInputRequest();

  rl.on('line', function (input) {
    const valid = isInputValid(input, game);

    if (!valid) {
      // reask for input if not valid
      printInputRequest();
      return;
    }

    // update
    game = updateGame(input, allowedPawns[currentPlayerPawnIndex], game);
    currentPlayerPawnIndex = currentPlayerPawnIndex === 0 ? 1 : 0;

    // print the latest game array
    printGame(game);

    // check if should end the game
    if (endGame(game)) {
      rl.close();
    } else {
      printInputRequest();
    }
  });
}

main();
