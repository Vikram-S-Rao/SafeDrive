function Test(question, option, answer) {
    this.question = question;
    this.option = option;
    this.answer = answer;

}

Test.prototype.correct_answer = function(option) {
    return option === this.answer;
}