package com.prueba.microservicios;

import javax.enterprise.inject.Produces;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class MicroserviciosApplication {

	public static void main(String[] args) {
		SpringApplication.run(MicroserviciosApplication.class, args);
	}

        @RequestMapping("multiplicar")
        public operacion multiplicar1(int n1,int n2){
            operacion op=new operacion();
            op.setN1(n1);
            op.setN2(n2);
            op.setResultado();
            return op;
        }
}
