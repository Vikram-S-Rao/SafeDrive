package com.example.lenovo.major_project_ver_1;

import android.os.AsyncTask;
import android.util.Log;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import static android.content.ContentValues.TAG;

/**
 * Created by Lenovo on 19-03-2018.
 */

public class MyFireBaseInstanceId extends FirebaseInstanceIdService {
    String StrResponse,StrUrl;


    @Override
    public void onTokenRefresh() {
        // Get updated InstanceID token.
        String refreshedToken = FirebaseInstanceId.getInstance().getToken();
       // Log.d(TAG, "Refreshed token: " + refreshedToken);

        // TODO: Implement this method to send any registration to your app's servers.
        //sendRegistrationToServer(refreshedToken);

    }

    private void sendRegistrationToServer(String refreshedToken) {
        User user = (User)getApplicationContext();
        StrUrl = "http://192.168.43.225:5000/token/"+user.getEmail()+"/"+refreshedToken;
        new AsnycToken().execute();

    }

    public class AsnycToken extends AsyncTask<String,String,String>
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




    }
}
