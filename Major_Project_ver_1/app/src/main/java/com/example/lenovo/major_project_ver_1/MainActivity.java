package com.example.lenovo.major_project_ver_1;

import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends Activity {

    EditText UsernameText,PasswordText;
    Button LoginButton;
    String Username,Password;
    TextView reg;
    MyDatabase mdb = new MyDatabase(MainActivity.this);
    Cursor cursor;

    String StrUrl,StrResponse;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        UsernameText = (EditText) findViewById(R.id.Username);
        PasswordText = (EditText) findViewById(R.id.Password);
        LoginButton = (Button) findViewById(R.id.Login_button);
        reg = findViewById(R.id.Register);
        mdb.open();

        LoginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Username = UsernameText.getText().toString();
                Password = PasswordText.getText().toString();
                new AsnycLogin().execute();

            }
        });

        reg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this,RegisterActivity.class);
                startActivity(intent);
            }
        });
    }

    public class AsnycLogin extends AsyncTask<String,String,String>
    {

        HttpURLConnection httpURLConnection = null;
        @Override
        protected String doInBackground(String... strings) {
            try {
                URL url = new URL(StrUrl);
                httpURLConnection = (HttpURLConnection) url.openConnection();
                httpURLConnection.setRequestMethod("GET");
                httpURLConnection.connect();

                BufferedReader reader = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
                StrResponse = reader.readLine();
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            Log.e("TAG", result); // this is expecting a response code to be sent from your server upon receiving the POST data
        }


    }
}

