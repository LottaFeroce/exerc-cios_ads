package lista1;
import java.util.ArrayList;
import java.util.List;
public class arraylist_em {
    public static void main(String[] args) {
        
            List<String> lista_nomeada = new ArrayList<>();
                lista_nomeada.add("ajerroi");
                lista_nomeada.add("yelon");
                lista_nomeada.add("Ipzeick");
                lista_nomeada.add("8445-  u d");
                lista_nomeada.add("qwert");

            System.out.println(lista_nomeada.size());
            lista_nomeada.remove(3);
            System.out.println(lista_nomeada.size());
            System.out.println(lista_nomeada.get(3));

            int tamanho_lista = lista_nomeada.size();
            System.out.println(tamanho_lista);
                String name = lista_nomeada.get(2);
            System.out.println(name);
                lista_nomeada.set(3, "Prinz Eugen");
                String name_update = lista_nomeada.get(3);
            System.out.println(name_update);

            List<Double> notas = new ArrayList<>();
            notas.add(8.8);
            notas.add(8.9);
            notas.add(8.91);
            notas.add(8.92);
            notas.add(8.93);
            notas.add(8.94);
            notas.add(8.95);
            notas.add(8.96);
            notas.add(8.97);
            notas.add(8.98);
            notas.add(8.99);
                int tamanho_int = notas.size();
               //double notaz = notas.get(0);
            System.out.println("Tamanho vetorado: "+tamanho_int);
    }
    
}
