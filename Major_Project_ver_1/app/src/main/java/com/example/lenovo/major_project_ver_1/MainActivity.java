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

    EditText EmailText,PasswordText;
    Button LoginButton;
    String Email,Password;
    TextView reg;
    String StrUrl,StrResponse="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EmailText = (EditText) findViewById(R.id.Username);
        PasswordText = (EditText) findViewById(R.id.Password);
        LoginButton = (Button) findViewById(R.id.Login_button);
        reg = findViewById(R.id.Register);


        LoginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Email = EmailText.getText().toString();
                Password = PasswordText.getText().toString();
                StrUrl = "http://192.168.43.225:5000/login/"+Email+"/"+Password ;

                User user = (User)getApplicationContext();
                user.setEmail(Email);
                /*Intent intent = new Intent(MainActivity.this,MenuActivity.class);
                intent.putExtra(HomeActivity.User,Email);
                startActivity(intent);*/
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
        protected void onPostExecute(String results)
        {
            if(StrResponse.equals("Success"))
            {
                Intent intent = new Intent(MainActivity.this,MenuActivity.class);
                intent.putExtra(HomeActivity.User,Email);
                startActivity(intent);
            }
            else {
                Toast.makeText(getApplicationContext(),"Something Went Wrong",Toast.LENGTH_LONG).show();
            }

        }




    }
}

