package com.example.lenovo.major_project_ver_1;

/**
 * Created by Lenovo on 28-02-2018.
 */


public class QuizQuestion {
    String question;
    String image;
    public String option1;
    public String option2;
    public String option3;
    public String option4;
    String answer1;
    String answer2;

    public QuizQuestion(String q, String o1, String o2, String o3, String o4, String a1,String a2,String i)
    {
        this.question = q;
        this.option1 = o1;
        this.option2 = o2;
        this.option3 = o3;
        this.option4 = o4;
        this.answer1 = a1;
        this.answer2 = a2;
        this.image = i;
    }

    public  String get_question()
    {
        return  this.question;
    }

    public String get_image(){return  this.image;}

    public  String get_answer1()
    {
        return  this.answer1;
    }
    public String get_answer2(){return this.answer2;}
}

