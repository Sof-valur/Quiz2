/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.quiz2;

/**
 *
 * @author 50684
 */
public class ConfigSingleton {
    private String AdminEmail;
    private static final ConfigSingleton instance = new ConfigSingleton();
    private ConfigSingleton(){
        this.AdminEmail = "sofia.vu@estudiantec.cr";
    }
    public static ConfigSingleton getInstace(){
        return instance;
    }
    public String getGoogleURL(){
        return "www.Google.com";
    }
    public String getAdminEmail(){
        return this.AdminEmail;
    }
    public void setAdminEmail(String adminemail){
        this.AdminEmail = adminemail;
    }
}
