package com.example.lenovo.major_project_ver_1;

import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.Resources;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.AsyncTask;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class QuizActivity extends AppCompatActivity {
    TextView Question;
    Button Option_1, Option_2, Option_3, Option_4;
    int Score = 0;
    int Qno = 0;
    ImageView image;
    String StrResponse;
    ArrayList<QuizQuestion> AppQuestions;
    LocationManager locationManager;
    double latitude, longitude;
    String Country, Locality, City;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quiz);
        Question = (TextView) findViewById(R.id.question);
        Option_1 = (Button) findViewById(R.id.opt_1);
        Option_2 = (Button) findViewById(R.id.opt_2);
        Option_3 = (Button) findViewById(R.id.opt_3);
        Option_4 = (Button) findViewById(R.id.opt_4);
        image = (ImageView) findViewById(R.id.imageView);
        AppQuestions = new ArrayList<QuizQuestion>();
        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);

        Create_Questions();
        UpdateUi(Qno);


        if (locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)) {
            if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                // TODO: Consider calling
                //    ActivityCompat#requestPermissions
                // here to request the missing permissions, and then overriding
                //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                //                                          int[] grantResults)
                // to handle the case where the user grants the permission. See the documentation
                // for ActivityCompat#requestPermissions for more details.
                return;
            }
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, new LocationListener() {
                @Override
                public void onLocationChanged(Location location) {
                    latitude = location.getLatitude();
                    longitude = location.getLongitude();


                    Geocoder geocoder = new Geocoder(getApplicationContext());
                    try {
                        List<Address> addressList = geocoder.getFromLocation(latitude, longitude, 1);
                        Country = addressList.get(0).getCountryName();
                        Locality = addressList.get(0).getLocality();

                        City = addressList.get(0).getAddressLine(0);


                        //mMarker.setPosition(latLng);

                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }

                @Override
                public void onStatusChanged(String s, int i, Bundle bundle) {

                }

                @Override
                public void onProviderEnabled(String s) {

                }

                @Override
                public void onProviderDisabled(String s) {

                }
            });} else if (locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, new LocationListener() {
                @Override
                public void onLocationChanged(Location location) {

                    latitude = location.getLatitude();
                    longitude = location.getLongitude();

                    Geocoder geocoder = new Geocoder(getApplicationContext());
                    try {
                        List<Address> addressList = geocoder.getFromLocation(latitude, longitude, 1);
                        // mMarker.setPosition(latLng);

                        Country = addressList.get(0).getCountryName();
                        Locality = addressList.get(0).getLocality();
                        City = addressList.get(0).getSubAdminArea();

                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
                @Override
                public void onStatusChanged(String s, int i, Bundle bundle) {

                }

                @Override
                public void onProviderEnabled(String s) {

                }

                @Override
                public void onProviderDisabled(String s) {

                }
            });}




        Option_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Option_1.getText().equals(AppQuestions.get(Qno).get_answer1()))
                {
                    Score++;
                }
                else if(Option_1.getText().equals(AppQuestions.get(Qno).get_answer2()))
                {
                    Score+=2;
                }
                else{

                }
                if(Qno < AppQuestions.size()-1)
                {
                    Qno++;
                    UpdateUi(Qno);
                }
                else {
                    FinalizeQuiz();
                }
            }
        });
        Option_2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Option_2.getText().equals(AppQuestions.get(Qno).get_answer1()))
                {
                    Score++;
                }
                else if (Option_2.getText().equals(AppQuestions.get(Qno).get_answer2()))
                {
                    Score+=2;
                }
                else {

                }
                if(Qno < AppQuestions.size()-1)
                {
                    Qno++;
                    UpdateUi(Qno);
                }
                else {
                    FinalizeQuiz();
                }
            }
        });

        Option_3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Option_3.getText().toString().equals(AppQuestions.get(Qno).get_answer1()))
                {
                    Score++;
                }
                else if(Option_3.getText().equals(AppQuestions.get(Qno).get_answer2()))
                {
                    Score+=2;
                }
                else
                {

                }
                if(Qno < AppQuestions.size()-1)
                {
                    Qno++;
                    UpdateUi(Qno);
                }
                else {
                    FinalizeQuiz();
                }
            }
        });

        Option_4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Option_4.getText().equals(AppQuestions.get(Qno).get_answer1()))
                {
                    Score++;
                }
                else if(Option_4.getText().equals(AppQuestions.get(Qno).get_answer2()))
                {
                    Score+=2;
                }
                {

                }
                if(Qno < AppQuestions.size()-1)
                {
                    Qno++;
                    UpdateUi(Qno);
                }
                else {
                    FinalizeQuiz();
                }
            }
        });


    }

    void Create_Questions()
    {
        AppQuestions.add(new QuizQuestion("How Many Drinks Did You Have?","None","One or Two Glass","More than Five","I Lost Count","One or Two Glass","None","None"));
        AppQuestions.add(new QuizQuestion("It is 3 am in the night, Do you think it is appropriate to call some one ?","No, It is inappropriate","Only if it is an Emergency","It is Fine","Did i change my time zone again","No, It is inappropriate","Only if it is an Emergency","None"));
        AppQuestions.add(new QuizQuestion("What is 11 x 11 ?","133","111","22","121","None","121","None"));
        AppQuestions.add(new QuizQuestion("What Animal is this ?","It's not an Animal","Monkey","Dog","Cat","Dog","Monkey","qimg2"));
        AppQuestions.add(new QuizQuestion("Which of the following sounds like a great idea ?","Having an early night","Sliding a mattress down stairs","Having a good cry","Throwing up","None","Having an early night","None"));
        AppQuestions.add(new QuizQuestion("Is This Text Blurry","Yes,Obviously","Possibly","No, its Perfectly fine","No You're Blurry","Possibly","Yes,Obviously","qimg1"));

    }

    void UpdateUi(int index)
    {
        Question.setText(AppQuestions.get(index).get_question());
        if(AppQuestions.get(index).get_image().equals("None"))
        {
            image.setVisibility(View.GONE);
        }
        else
        {
            Resources res = getResources();
            int resID = res.getIdentifier( AppQuestions.get(index).get_image(), "drawable", getPackageName());
            image.setImageResource(resID);
            image.setVisibility(View.VISIBLE);
        }
        Option_1.setText(AppQuestions.get(index).option1);
        Option_2.setText(AppQuestions.get(index).option2);
        Option_3.setText(AppQuestions.get(index).option3);
        Option_4.setText(AppQuestions.get(index).option4);
    }

    void FinalizeQuiz()
    {
        if(Score < 6)
        {
            Intent intent = new Intent(getApplicationContext(),LocationUpdateActivity.class);
            SendData();
            //Toast.makeText(getApplicationContext(),"You have failed the Test!!!!\nYour Location is being sent please restrain from driving vehicle\nThank You",Toast.LENGTH_LONG).show();
           // Toast.makeText(getApplicationContext(),Country+Locality+City,Toast.LENGTH_LONG).show();
            startActivity(intent);
        }
        else
        {
            User user = (User)getApplicationContext();
            Toast.makeText(getApplicationContext(),user.getEmail(),Toast.LENGTH_LONG).show();
            Intent intent = new Intent(getApplicationContext(),MenuActivity.class);
            startActivity(intent);
        }
    }

    public void SendData()
    {
        User user = (User)getApplicationContext();

        JSONObject postData = new JSONObject();
        try {
            postData.put("Email",user.getEmail());
            postData.put("Score", Score);
            postData.put("Country",Country);
            postData.put("City",Locality);
            postData.put("Locality",City);
            postData.put("Latitude",latitude);
            postData.put("Longitude",longitude);


            new QuizActivity.AsyncScore().execute("http://192.168.43.225:5000/user/testresult", postData.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private class AsyncScore extends AsyncTask<String, Void, String> {

        @Override
        protected void onPreExecute() {
        }
        @Override
        protected String doInBackground(String... params) {



            HttpURLConnection httpURLConnection = null;
            try {

                httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
                httpURLConnection.setRequestMethod("POST");
                httpURLConnection.setRequestProperty("Content-Type", "application/json");
                httpURLConnection.setRequestProperty("Accept", "application/json");

                httpURLConnection.setDoOutput(true);
                Writer writer = new BufferedWriter(new OutputStreamWriter(httpURLConnection.getOutputStream(), "UTF-8"));
                writer.write(params[1]);
// json data
                writer.close();



                InputStream in = httpURLConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(in);

                int inputStreamData = inputStreamReader.read();
                while (inputStreamData != -1) {
                    char current = (char) inputStreamData;
                    inputStreamData = inputStreamReader.read();
                    StrResponse += current;
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (httpURLConnection != null) {
                    httpURLConnection.disconnect();
                }
            }

            return StrResponse;
        }



    }


}


