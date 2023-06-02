package com.example.firebase2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;


public class HomeActivity extends AppCompatActivity {

     //db variable
    public FirebaseDatabase db = FirebaseDatabase.getInstance();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        Intent intent = getIntent();
        TextView email1 = findViewById(R.id.editCuenta);
        String emailget = intent.getStringExtra("email");
        String provider = intent.getStringExtra("provider");
        email1.setText(emailget);
        //save data persistently
        SharedPreferences preferences = getSharedPreferences("checkbox", MODE_PRIVATE);
        preferences.edit().putString("email", emailget).apply();
        preferences.edit().putString("provider", provider).apply();

        onclick();
        onclick1();
        guardar();
    }
    public void onclick1(){
        Button btn1 = findViewById(R.id.btnSave);
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomeActivity.this, LunesActivity.class);
                startActivity(intent);
            }
        });
    }

    public void onclick(){
        Button btnSalir = findViewById(R.id.btnSalir);
        btnSalir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences preferences = getSharedPreferences("checkbox", MODE_PRIVATE);
                preferences.edit().putString("email", null).apply();
                preferences.edit().putString("provider", null).apply();

                FirebaseAuth.getInstance().signOut();
                Intent intent = new Intent(HomeActivity.this, AuthActivity.class);
                startActivity(intent);
            }
        });
    }

    public void guardar() {
        Button btnSave = findViewById(R.id.btnSave);
        btnSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                //create collection and document
                db.getReference().child("users").child("email").setValue("email");

                //save in db
                //db.getReference().child("users").child(FirebaseAuth.getInstance().getCurrentUser().getUid()).child("email").setValue(FirebaseAuth.getInstance().getCurrentUser().getEmail());
                //db.getReference().child("users").child(FirebaseAuth.getInstance().getCurrentUser().getUid()).child("provider").setValue(FirebaseAuth.getInstance().getCurrentUser().getProviderId());

            }
        });

    }
}