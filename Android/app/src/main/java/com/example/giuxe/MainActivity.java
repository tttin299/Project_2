package com.example.giuxe;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    String urlGetData = "http://192.168.43.63:81/androidwebservice/getdata.php";
    private EditText edtSearch;
    private ImageView imgA1, imgA2, imgA3, imgA4, imgA5, imgB1, imgB2, imgB3, imgB4, imgB5, imgC1, imgC2, imgC3, imgC4, imgC5,
            imgD1, imgD2, imgD3, imgD4, imgD5;
    ArrayList<DauXe> arrayDauXe;
    String[] arrayChoDau;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        AnhXa();
        GetData(urlGetData);
        init();
        handler.post(TimerUpdate);
    }

    Handler handler = new Handler();

    final Runnable TimerUpdate = new Runnable() {
        @Override
        public void run() {
            handler.postDelayed(TimerUpdate, 2000);
            GetData(urlGetData);
        }
    };

    private void AnhXa() {
        edtSearch = findViewById(R.id.edtSearch);
        imgA1 = findViewById(R.id.imgA1);
        imgA2 = findViewById(R.id.imgA2);
        imgA3 = findViewById(R.id.imgA3);
        imgA4 = findViewById(R.id.imgA4);
        imgA5 = findViewById(R.id.imgA5);

        imgB1 = findViewById(R.id.imgB1);
        imgB2 = findViewById(R.id.imgB2);
        imgB3 = findViewById(R.id.imgB3);
        imgB4 = findViewById(R.id.imgB4);
        imgB5 = findViewById(R.id.imgB5);

        imgC1 = findViewById(R.id.imgC1);
        imgC2 = findViewById(R.id.imgC2);
        imgC3 = findViewById(R.id.imgC3);
        imgC4 = findViewById(R.id.imgC4);
        imgC5 = findViewById(R.id.imgC5);

        imgD1 = findViewById(R.id.imgD1);
        imgD2 = findViewById(R.id.imgD2);
        imgD3 = findViewById(R.id.imgD3);
        imgD4 = findViewById(R.id.imgD4);
        imgD5 = findViewById(R.id.imgD5);
    }

    private void GetData(String url){
        RequestQueue requestQueue = Volley.newRequestQueue(this);
        arrayChoDau = new String[]{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"};
        arrayDauXe = new ArrayList<>();
            
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(Request.Method.GET, url, null, new Response.Listener<JSONArray>() {
            @Override
            public void onResponse(JSONArray response) {
//                Toast.makeText(MainActivity.this, response.toString(), Toast.LENGTH_SHORT).show();


                for(int i = 0; i < response.length(); i++){
                    try {
                        JSONObject object = response.getJSONObject(i);

                        arrayDauXe.add(new DauXe(
                                object.getString("ID"),
                                object.getString("BienSo"),
                                object.getString("ChoDau")
                        ));
                        KiemTra(object.getString("ChoDau"));

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
            }
        },
            new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(MainActivity.this, "Lỗi!", Toast.LENGTH_SHORT).show();
            }
        });

        requestQueue.add(jsonArrayRequest);
    }


    private void KiemTra(String choDau){
 //       Toast.makeText(MainActivity.this, choDau, Toast.LENGTH_SHORT).show();
//        int a = choDau.length();
//        edtSearch.setText(a.);
//        Toast.makeText(MainActivity.this, String.valueOf((int)choDau.length()), Toast.LENGTH_SHORT).show();
        if(choDau.equals("A1")){
            arrayChoDau[0] = "A1";
        }
        if(choDau.equals("A2")){
            arrayChoDau[1] = "A2";
        }
        if(choDau.equals("A3")){
            arrayChoDau[2] = "A3";
        }
        if(choDau.equals("A4")){
            arrayChoDau[3] = "A4";
        }
        if(choDau.equals("A5")){
            arrayChoDau[4] = "A5";
        }


        if(choDau.equals("B1")){
            arrayChoDau[5] = "B1";
        }
        if(choDau.equals("B2")){
            arrayChoDau[6] = "B2";
        }
        if(choDau.equals("B3")){
            arrayChoDau[7] = "B3";
        }
        if(choDau.equals("B4")){
            arrayChoDau[8] = "B4";
        }
        if(choDau.equals("B5")){
            arrayChoDau[9] = "B5";
        }


        if(choDau.equals("C1")){
            arrayChoDau[10] = "C1";
        }
        if(choDau.equals("C2")){
            arrayChoDau[11] = "C2";
        }
        if(choDau.equals("C3")){
            arrayChoDau[12] = "C3";
        }
        if(choDau.equals("C4")){
            arrayChoDau[13] = "C4";
        }
        if(choDau.equals("C5")){
          //  Toast.makeText(MainActivity.this, "choDau", Toast.LENGTH_SHORT).show();
            arrayChoDau[14] = "C5";
        }



        if(choDau.equals("D1")){
            arrayChoDau[15] = "D1";
        }
        if(choDau.equals("D2")){
            arrayChoDau[16] = "D2";
        }
        if(choDau.equals("D3")){
            arrayChoDau[17] = "D3";
        }
        if(choDau.equals("D4")){
            arrayChoDau[18] = "D4";
        }
        if(choDau.equals("D5")){
            arrayChoDau[19] = "D5";
        }


        HienThi(arrayChoDau);
    }


    private void HienThi(String[] arrchoDau){

        if(arrchoDau[0].equals("A1")){
            this.imgA1.setImageResource(R.drawable.car);
        }else{
            this.imgA1.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[1].equals("A2")){
            this.imgA2.setImageResource(R.drawable.car);
        }else{
            this.imgA2.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[2].equals("A3")){
            this.imgA3.setImageResource(R.drawable.car);
        }else{
            this.imgA3.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[3].equals("A4")){
            this.imgA4.setImageResource(R.drawable.car);
        }else{
            this.imgA4.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[4].equals("A5")){
            this.imgA5.setImageResource(R.drawable.car);
        }else{
            this.imgA5.setImageResource(R.drawable.nocar);
        }



        if(arrchoDau[5].equals("B1")){
            this.imgB1.setImageResource(R.drawable.car);
        }else{
            this.imgB1.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[6].equals("B2")){
            this.imgB2.setImageResource(R.drawable.car);
        }else{
            this.imgB2.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[7].equals("B3")){
            this.imgB3.setImageResource(R.drawable.car);
        }else{
            this.imgB3.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[8].equals("B4")){
            this.imgB4.setImageResource(R.drawable.car);
        }else{
            this.imgB4.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[9].equals("B5")){
            this.imgB5.setImageResource(R.drawable.car);
        }else{
            this.imgB5.setImageResource(R.drawable.nocar);
        }




        if(arrchoDau[10].equals("C1")){
            this.imgC1.setImageResource(R.drawable.car);
        }else{
            this.imgC1.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[11].equals("C2")){
            this.imgC2.setImageResource(R.drawable.car);
        }else{
            this.imgC2.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[12].equals("C3")){
            this.imgC3.setImageResource(R.drawable.car);
        }else{
            this.imgC3.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[13].equals("C4")){
            this.imgC4.setImageResource(R.drawable.car);
        }else{
            this.imgC4.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[14].equals("C5")){
            this.imgC5.setImageResource(R.drawable.car);
        }else{
            this.imgC5.setImageResource(R.drawable.nocar);
        }



        if(arrchoDau[15].equals("D1")){
            this.imgD1.setImageResource(R.drawable.car);
        }else{
            this.imgD1.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[16].equals("D2")){
            this.imgD2.setImageResource(R.drawable.car);
        }else{
            this.imgD2.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[17].equals("D3")){
            this.imgD3.setImageResource(R.drawable.car);
        }else{
            this.imgD3.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[18].equals("D4")){
            this.imgD4.setImageResource(R.drawable.car);
        }else{
            this.imgD4.setImageResource(R.drawable.nocar);
        }

        if(arrchoDau[19].equals("D5")){
            this.imgD5.setImageResource(R.drawable.car);
        }else{
            this.imgD5.setImageResource(R.drawable.nocar);
        }
    }

    public void init() {
        // bên layout thanh edtSearch phải set imeOptions="actionSearch" để hiện nút tìm kiểm trên bàn phím khi nhập
        edtSearch.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView textView, int actionId, KeyEvent keyEvent) { //lắng nghe sự kiện
                if (actionId == EditorInfo.IME_ACTION_SEARCH //nếu nhấn nút có hình dạng tìm kiếm (nút kính lúp)
                        //hai cái dưới có thể không cần vì đã set nút V thành hình kính lúp
                        || actionId == EditorInfo.IME_ACTION_DONE //hoặc nút xác nhận (nút V)
                        || keyEvent.getAction() == KeyEvent.KEYCODE_ENTER
                ) { //hoặc phím Enter của bàn phím khi mô phỏng trên máy ảo
                    // tạo phương thức tìm kiếm
//                    GetData(urlGetData);
                    
                    TimKiem();
                }
                return false;
            }
        });
    }

    private void TimKiem() { // hàm để tìm điểm địa điểm
        String searchString = edtSearch.getText().toString();
        int j = arrayDauXe.size();

        for (int i = 0; i < j; i++) {
            String bienSo = arrayDauXe.get(i).getBienSo();
            if (bienSo.equals(searchString)){
                HienThiTimKiem(arrayDauXe.get(i).getChoDau());
                break;
            }
//            Toast.makeText(this, bienSo, Toast.LENGTH_SHORT).show();
        }
    }

    private void HienThiTimKiem(String choDau){


        if(choDau.equals("A1")){
            this.imgA1.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("A2")){
            this.imgA2.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("A3")){
            this.imgA3.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("A4")){
            this.imgA4.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("A5")){
            this.imgA5.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("B1")){
            this.imgB1.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("B2")){
            this.imgB2.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("B3")){
            this.imgB3.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("B4")){
            this.imgB4.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("B5")){
            this.imgB5.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("C1")){
            this.imgC1.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("C2")){
            this.imgC2.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("C3")){
            this.imgC3.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("C4")){
            this.imgC4.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("C5")){
            this.imgC5.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("D1")){
            this.imgD1.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("D2")){
            this.imgD2.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("D3")){
            this.imgD3.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("D4")){
            this.imgD4.setImageResource(R.drawable.mycar);
        }

        if(choDau.equals("D5")){
            this.imgD5.setImageResource(R.drawable.mycar);
        }


    }

    public void Update(View view) {
        GetData(urlGetData);
    }
//    private void showImgCar() { this.img.setImageResource(R.drawable.car); }
//
//    private void showImglNoCar() {
//        this.imgl.setImageResource(R.drawable.nocar);
//    }
//
//    private void showImgfMyCar() {
//        this.imgf.setImageResource(R.drawable.mycar);
//    }
}