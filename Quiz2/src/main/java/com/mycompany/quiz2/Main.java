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
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println(ConfigSingleton.getInstace().getAdminEmail());
        ConfigSingleton.getInstace().setAdminEmail("sofia.21.v.u@gmail.com");
        System.out.println(ConfigSingleton.getInstace().getAdminEmail());
    }
    
}
