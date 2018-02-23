function populate() {
    if (test.isEnded()) {
        
        var url = document.URL;
        var request = url+"/" + test.score;
        location.href = request;


    } else {
        var element = document.getElementById("question");

        element.innerHTML = test.getquestionindex().question;

        var choices = test.getquestionindex().option;
        for (var i = 0; i < choices.length; i++) {
            var element2 = document.getElementById("option_" + i);

            element2.innerHTML = choices[i];
            Guess("option_" + i, choices[i])
        }
        showProgress();
    }
   

}

function Guess(id, guess) {
    var button = document.getElementById(id);
    button.onclick = function() {
        test.guess(guess);
        populate();
    }

}

function showProgress() {
    var current = test.questionIndex + 1;
    var element3 = document.getElementById("progress");
    element3.innerHTML = "Qustion " + current + " of " + test.questions.length;
}

var question1 = "Find out the missing character in the following sequence \nV, U, T, S, P, O, N, M ";
var question2 = ['<div class=" col-md-10 text-center">','<div class="thumbnail"> <img src="http://www.puzzlesandriddles.com/Pics/PerceptualPuzzle06.gif">','<div class="caption">'
,'<h3>How many squares are there</h3>','</div></div></div>'].join('');
var question3 = "Find out the missing number in the following seqence 1, 1, 2, 3, 5, X, 12";
var question4 = "Find out the result of the Equation? 8*9+7-3"
var question5 = "Find out the next term in this sequence 5c3 7f6 9i9 11l12 ?"



var questions = [
    new Test(question1, ["X", "L", "Q", "N"], "Q"),
    new Test(question2, ["12", "40", "36", "54"], "40"),
    new Test(question3, ["7", "4", "8", "9"], "7"),
    new Test(question4, ["76", "73", "79", "84"], "76"),
    new Test(question5, ["12p7", "14x15", "13o17", "13o15"], "13o15")

];
var test = new Controller(questions);
populate();