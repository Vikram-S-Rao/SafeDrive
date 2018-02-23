package com.example.lenovo.major_project_ver_1;

import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.os.AsyncTask;
import android.os.Looper;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.apache.http.params.HttpConnectionParams;
import org.json.JSONException;
import org.json.JSONObject;
import java.net.URL;

import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;

import static android.provider.ContactsContract.CommonDataKinds.Website.URL;
import static java.net.Proxy.Type.HTTP;

public class RegisterActivity extends AppCompatActivity {

    EditText User, Email, Pass, Addr, Ph_no, device, Emergency;
    Button RegisterBtn;
    String Username, Email_id, Password, Address, Phone_no, Device_id, Emergency_no;
    MyDatabase mdb = new MyDatabase(this);
    Cursor cursor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        User = (EditText) findViewById(R.id.UsernameReg);
        Email = (EditText) findViewById(R.id.EmailReg);
        Pass = (EditText) findViewById(R.id.PasswordReg);
        Addr = (EditText) findViewById(R.id.AddressReg);
        Ph_no = (EditText) findViewById(R.id.PhoneReg);
        Emergency = (EditText) findViewById(R.id.EmergencyNumReg);
        device = (EditText) findViewById(R.id.DeviceIdReg);
        RegisterBtn = (Button) findViewById(R.id.buttonReg);
        mdb.open();


        RegisterBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Username = User.getText().toString();
                Email_id = Email.getText().toString();
                Password = Pass.getText().toString();
                Address = Addr.getText().toString();
                Phone_no = Ph_no.getText().toString();
                Device_id = device.getText().toString();
                Emergency_no = Emergency.getText().toString();

                ContentValues cv = new ContentValues();
                cv.put("Email", Email_id);
                cv.put("Username", Username);
                cv.put("Password", Password);
                cv.put("Phone", Phone_no);
                cv.put("Device", Device_id);
                cv.put("Emergency", Emergency_no);


                mdb.UserInsert(cv);

                Toast.makeText(getApplicationContext(), "Sign up Successful", Toast.LENGTH_LONG).show();
                Intent intent = new Intent(RegisterActivity.this, MainActivity.class);
                startActivity(intent);

            }
        });

    }

    public void SendData()
    {
        JSONObject postData = new JSONObject();
        try {
            postData.put("Email", Email_id);
            postData.put("Username", Username);
            postData.put("Password", Password);
            postData.put("Phone", Phone_no);
            postData.put("Device", Device_id);
            postData.put("Emergency", Emergency_no);

            new AsyncRegister().execute("http://52.88.194.67:8080/IOTProjectServer/registerDevice", postData.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }




    private class AsyncRegister extends AsyncTask<String, Void, String> {

        @Override
        protected void onPreExecute() {
        }
        @Override
        protected String doInBackground(String... params) {

            String data = "";

            HttpURLConnection httpURLConnection = null;
            try {

                httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
                httpURLConnection.setRequestMethod("POST");

                httpURLConnection.setDoOutput(true);

                DataOutputStream wr = new DataOutputStream(httpURLConnection.getOutputStream());
                wr.writeBytes("PostData=" + params[1]);
                wr.flush();
                wr.close();

                InputStream in = httpURLConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(in);

                int inputStreamData = inputStreamReader.read();
                while (inputStreamData != -1) {
                    char current = (char) inputStreamData;
                    inputStreamData = inputStreamReader.read();
                    data += current;
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (httpURLConnection != null) {
                    httpURLConnection.disconnect();
                }
            }

            return data;
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            Log.e("TAG", result); // this is expecting a response code to be sent from your server upon receiving the POST data
        }
    }


}