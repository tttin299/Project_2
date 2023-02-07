package com.example.giuxe;

public class DauXe {
    private String ID;
    private String BienSo;
    private String ChoDau;

    public DauXe() {

    }

    public DauXe(String ID, String bienSo, String choDau) {
        this.ID = ID;
        BienSo = bienSo;
        ChoDau = choDau;
    }

    public String getID() {
        return ID;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public String getBienSo() {
        return BienSo;
    }

    public void setBienSo(String bienSo) {
        BienSo = bienSo;
    }

    public String getChoDau() {
        return ChoDau;
    }

    public void setChoDau(String choDau) {
        ChoDau = choDau;
    }
}
