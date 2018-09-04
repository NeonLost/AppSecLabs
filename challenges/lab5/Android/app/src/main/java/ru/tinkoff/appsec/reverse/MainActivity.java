package ru.tinkoff.appsec.reverse;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.util.Arrays;

public class MainActivity extends AppCompatActivity {

    private EditText secretKey;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        secretKey = findViewById(R.id.secret_key);
    }

    public void checkKey(View v){
        String hash = getString(R.string.hash);
        int length = hash.length();
        String slice1 = hash.substring(0, length/2);
        String slice2 = hash.substring(length/2, length);
        String xored = xorWithKey(slice1.getBytes(), slice2.getBytes());

        StringBuilder theKey = new StringBuilder("R");
        theKey.append("V");
        theKey.append(xored.substring(0, length/4));
        theKey.append("N");
        theKey.reverse();
        theKey.append("2");

        String checkKey = secretKey.getText().toString();
        if (checkKey.contentEquals(theKey)) {
            Toast.makeText(this, "Valid Key",
                    Toast.LENGTH_LONG).show();
        }
        else {
            Toast.makeText(this, "Invalid Key",
                    Toast.LENGTH_LONG).show();
        }
    }

    private String xorWithKey(byte[] a, byte[] key) {
        byte[] out = new byte[a.length];
        for (int i = 0; i < a.length; i++) {
            out[i] = (byte) (a[i] ^ key[i%key.length]);
        }
        return byteArrayToHex(out);
    }

    public static String byteArrayToHex(byte[] a) {
        StringBuilder sb = new StringBuilder(a.length * 2);
        for(byte b: a)
            sb.append(String.format("%02x", b));
        return sb.toString();
    }
}
