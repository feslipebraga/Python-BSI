package com.mycompany.projetouniversidade;

public class Departamento {
    private String nome;
    
    public Departamento(String nome) {
        this.nome = nome;
        }

    public String getNome() {
        return nome;
        }

    @Override
    public String toString() {
        return nome;
    }
    
    
}
