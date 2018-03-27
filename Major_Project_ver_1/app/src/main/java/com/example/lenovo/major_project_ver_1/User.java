package com.example.lenovo.major_project_ver_1;

import android.app.Application;

/**
 * Created by Lenovo on 19-03-2018.
 */

public class User extends Application {
    private  String UserEmail;
    public  String getEmail()
    {
        return  UserEmail;
    }
    public  void setEmail(String mail)
    {
        UserEmail = mail;
    }
}
