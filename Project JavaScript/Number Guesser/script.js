let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => Math.floor(Math.random() * 10);

const compareGuesses = (userGuess, computerGuess, secretTarget) => {
    distanceUser = Math.abs(secretTarget - userGuess);
    distanceComputer = Math.abs(secretTarget - computerGuess);

    if (distanceUser <= distanceComputer) return true;
    else return false;
};

const updateScore = winner => {
    switch (winner) {
        case 'human':
            humanScore++;
            break;
        case 'computer':
            computerScore++;
            break;
        default:
            console.log('There is a problem !');
            break;
    }
};

const advanceRound = () => currentRoundNumber++;

// je fais un test
// je fais un autre test222
