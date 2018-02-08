function populate() {
    if (test.isEnded()) {
        
        var url = document.URL;
        var request = url + "/" + test.score;
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

var questions = [
    new Test("Question 1", ["option1", "option2", "option3", "option4"], "option3"),
    new Test("Question 2", ["option1", "option2", "option3", "option4"], "option2"),
    new Test("Question 3", ["option1", "option2", "option3", "option4"], "option4"),
    new Test("Question 4", ["option1", "option2", "option3", "option4"], "option1")
];
var test = new Controller(questions);
populate();