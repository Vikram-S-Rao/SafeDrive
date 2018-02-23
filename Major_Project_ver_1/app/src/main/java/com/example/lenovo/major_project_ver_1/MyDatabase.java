package com.example.lenovo.major_project_ver_1;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteException;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

/**
 * Created by Lenovo on 08-02-2018.
 */

public class MyDatabase {

    private static final String DB_Name = "Safedrive";
    Context mycontext;
    Myhelper myhelper;
    SQLiteDatabase sdb;
    public MyDatabase(Context context){
        this.mycontext = context;
        myhelper = new Myhelper(mycontext,DB_Name,null,1);

    }
    public void open()
    {
        sdb = myhelper.getWritableDatabase();
    }
    public void UserInsert(ContentValues cv) {
        sdb.insert("Users",null,cv);
        Log.i("Safedrive","Values Inserted");
    }
    public Cursor getUser(){
        sdb = myhelper.getReadableDatabase();
        try {
            Cursor c = sdb.query("Users", null,null, null, null, null, null, null);
            //c.moveToFirst();
            Log.i("Safedrive","User registered successfully");
            return c;

        }
        catch (SQLiteException sql)
        {

            Log.e("Safedrive",sql.getStackTrace().toString());
        }
        return null;
    }

    public  class Myhelper extends SQLiteOpenHelper {
        public Myhelper(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
            super(context, name, factory, version);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            db.execSQL("create table Users(_id integer primary key, Email text,Username text,Password text,Phone text,Device text,Emergency text );");
            Log.i("Safedrive","Table Created");
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {

        }


    }
}