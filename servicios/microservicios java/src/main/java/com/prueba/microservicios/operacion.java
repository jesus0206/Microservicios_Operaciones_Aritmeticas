/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.prueba.microservicios;

public class operacion {
 private int n1;
 private int n2;
 private int result;
 
 public operacion(int a,int b){
     super();
     this.n1=a;
     this.n2=b;
 }
 public operacion(){
     super();
 }
 public void setN1(int a){
     this.n1=a;
 }
 public void setN2(int b){
     this.n2=b;
 } 
 public int getN1(){
     return this.n1;
 }
 public int getN2(){
     return this.n2;
 }
 public void setResultado(){
     this.result=this.getN1()*this.getN2();
 }
 public int getResultado(){
     return this.result;
 } 
}
