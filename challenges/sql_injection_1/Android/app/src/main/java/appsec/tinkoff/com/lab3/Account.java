package appsec.tinkoff.com.lab3;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class Account extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_account);
        Bundle extras = getIntent().getExtras();
        if(extras !=null) {
            String loginValue = extras.getString("login");
            final TextView welcomeText = findViewById(R.id.welcomeText);
            welcomeText.setText("Hello " + loginValue);
        }
    }
}
