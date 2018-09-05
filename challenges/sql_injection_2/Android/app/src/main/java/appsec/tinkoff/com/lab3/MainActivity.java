package appsec.tinkoff.com.lab3;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.okhttp.Call;
import com.squareup.okhttp.Callback;
import com.squareup.okhttp.ConnectionPool;
import com.squareup.okhttp.HttpUrl;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import org.json.JSONObject;

import java.io.IOException;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText serverAddr = findViewById(R.id.url);
        final EditText login = findViewById(R.id.login);
        final EditText pass = findViewById(R.id.pass);

        Button button = findViewById(R.id.loginButton);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!login.getText().toString().isEmpty() && !pass.getText().toString().isEmpty()){
                    String endpointPath = serverAddr.getText().toString()+"/lab3/auth";

                    OkHttpClient client = new OkHttpClient();
                    HttpUrl.Builder urlBuilder = HttpUrl.parse(endpointPath).newBuilder();
                    urlBuilder.addQueryParameter("login", login.getText().toString());
                    urlBuilder.addQueryParameter("password", pass.getText().toString());
                    String url = urlBuilder.build().toString();

                    try {
                        Request request = new Request.Builder().url(url).build();
                        client.newCall(request)
                                .enqueue(new Callback() {
                                    @Override
                                    public void onFailure(Request request, IOException e) {
                                        runOnUiThread(new Runnable() {
                                            @Override
                                            public void run() {
                                                // For the example, you can show an error dialog or a toast
                                                // on the main UI thread
                                                Toast t = Toast.makeText(MainActivity.this, "Error: Network problem.", Toast.LENGTH_SHORT);
                                                t.show();
                                            }
                                        });
                                    }

                                    @Override
                                    public void onResponse(Response response) throws IOException {
                                        String res = response.body().string();
                                        if (res.contains("login")){
                                            try {
                                                JSONObject jsonObject = new JSONObject(res);
                                                res = jsonObject.getString("login");
                                                Intent account = new Intent(MainActivity.this, Account.class);
                                                account.putExtra("login", res);
                                                startActivity(account);
                                            }
                                            catch (Exception e){
                                                login.post(new Runnable() {
                                                    @Override
                                                    public void run() {
                                                        Toast t = Toast.makeText(MainActivity.this, "Error: Response error.", Toast.LENGTH_SHORT);
                                                        t.show();
                                                    }
                                                });
                                            }
                                        }
                                        else{
                                            login.post(new Runnable() {
                                                @Override
                                                public void run() {
                                                    Toast t = Toast.makeText(MainActivity.this, "Error: Invalid credentials.", Toast.LENGTH_SHORT);
                                                    t.show();
                                                }
                                            });
                                        }
                                    }
                                });
                        // Do something with the response.
                    } catch (Exception e) {
                        login.post(new Runnable() {
                            @Override
                            public void run() {
                                Toast t = Toast.makeText(MainActivity.this, "Error: Network problem.", Toast.LENGTH_SHORT);
                                t.show();
                            }
                        });
                    }
                }
                else{
                    login.post(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(MainActivity.this, "Error: Invalid credentials.", Toast.LENGTH_SHORT);
                        }
                    });
                }
            }
        });
    }


}
