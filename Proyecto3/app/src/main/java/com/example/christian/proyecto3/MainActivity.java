package com.example.christian.proyecto3;

import android.content.Intent;
import android.support.annotation.Nullable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.method.HideReturnsTransformationMethod;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.EmptyStackException;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    Button Siguiente;

    Button button;
    Button button2;
    Button button3;
    EditText editText;
    EditText prueba;
    EditText editText2;
    String server_url = "http://192.168.56.1:5000/c";
    String server_url2 = "http://192.168.56.1:5000/prueba";

    private RequestQueue webService;

    Boolean validar(String text){
        return text!= null && text.trim().length()>0 ;
    }

    //TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
////////////////////////////////////////////////////////////////////////////////////
        // ---------------------------- GET Flask -------------------------------
        button = (Button)findViewById(R.id.btn2);
        button2 = (Button)findViewById(R.id.btn3);
        editText = (EditText)findViewById(R.id.usuario);
        prueba = (EditText)findViewById(R.id.pruebatxt);
        editText2 = (EditText)findViewById(R.id.contrasena);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                final RequestQueue requestQueue = Volley.newRequestQueue(MainActivity.this);
                StringRequest stringRequest = new StringRequest(Request.Method.GET, server_url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {

                                editText.setText(response);
                                requestQueue.stop();
                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError volleyError) {
                        editText.setText("Algo Salio Mal");
                        volleyError.printStackTrace();
                        requestQueue.stop();
                    }
                });
                requestQueue.add(stringRequest);

            }
        });
        ///// -------------------------------------------- Post --------------------------
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                final RequestQueue requestQueue = Volley.newRequestQueue(MainActivity.this);
                StringRequest stringRequest = new StringRequest(Request.Method.POST, server_url2,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {

                                editText.setText(response);
                                requestQueue.stop();

                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError volleyError) {
                        editText.setText("Algo Salio Mal");
                        volleyError.printStackTrace();
                        requestQueue.stop();
                    }
                }){
                    @Override
                    protected Map<String, String> getParams(){
                        Map<String, String> params = new HashMap<String, String>();
                        params.put("dato", editText.getText().toString());
                        params.put("password", editText2.getText().toString());

                        return  params;
                    }
                };
                requestQueue.add(stringRequest);

            }
        });

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
       ///----------------------------- cambio de form -------------------------
        Siguiente = (Button)findViewById(R.id.btn1);
        Siguiente.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent Siguiente = new Intent(MainActivity.this,Main3Activity.class);
                String Usuario = editText.getText().toString();
                String Contrasena = editText2.getText().toString();
                String pp = prueba.getText().toString();




                if (validar(Usuario)&& validar(Contrasena)){
                    Toast toast = Toast.makeText(getApplicationContext(), "true", Toast.LENGTH_SHORT);
                                  toast.show();
                    startActivity(Siguiente);
                } else{
                    Toast toast = Toast.makeText(getApplicationContext(), "false" , Toast.LENGTH_SHORT);
                                  toast.show();
                }

//
            }
        });
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
        webService = Volley.newRequestQueue(MainActivity.this);

        //Toast toast = Toast.makeText(getApplicationContext(), "hola", Toast.LENGTH_SHORT);
        //toast.show();

        // Aca esta el StringRequest

        StringRequest request = new StringRequest(Request.Method.POST, "http://192.168.56.1", new Response.Listener<String>() {
            @Override
            public void onResponse(String s) {
                //Aca que aparece si se conecto
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError volleyError) {
                //Aca van los errores por no conectarse
            }
        }
        )
        {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                //Aca se crea un Map (hashmap) para conectar todos los parametros
                //return super.getParams();
                Map<String, String> parametros = new HashMap<String, String>();
                //Se agregan los parametros

                parametros.put("usuario","root");
                parametros.put("password","123456");
                // Con esto php recibe: $this->input->post("usuario"); //Su valor es "root"

                return parametros;
            }
        };
        // Se debe de agregar al final el StringRequest a nuestro websevice de volley
        webService.add(request);
    }
}
