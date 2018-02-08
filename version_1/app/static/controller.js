function Controller(questions) {
    this.score = 0;
    this.questions = questions;
    this.questionIndex = 0;


}

Controller.prototype.getquestionindex = function() {

    return this.questions[this.questionIndex];
}

Controller.prototype.isEnded = function() {

    return this.questions.length === this.questionIndex;
}

Controller.prototype.guess = function(answer) {


    if (this.getquestionindex().correct_answer(answer)) {
        this.score++
    }
    this.questionIndex++;
}