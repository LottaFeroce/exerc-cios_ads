package exercs_nao_relac;
public class funcoes {
    public static void main(String[] args) {
        clear();
        hello();
        world("World");
        neighbor("neighbor", 3);
        int resultado = soma(10, 10);
        System.out.println(resultado);
        String nome = meu_nome();
        System.out.printf("->nome digitado: %s<-\n", nome);

        double imc_calc = imc(75, 1.77);
        System.out.printf("Imc calculado: %.2f\n", imc_calc);

        classifyIMC(imc_calc);
    }

    public static void clear() {
        try {
            String sistema = System.getProperty("os.name");
            if (sistema.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void hello() {
        System.out.println("Hello");
    }

    public static void world(String nome) {
        System.out.printf("Hello %s!\n", nome);
    }

    public static void neighbor(String nome, int messages) {
        System.out.printf("Hello %s you have %d new messages(s)\n", nome, messages);
    }

    public static Integer soma(int num1, int num2) {
        int soma = num1 + num2;
        return soma;
    }

    public static String meu_nome() {
        return "Nome aqui";
    }

    public static double imc(double peso, double altura) {
        double meu_imc = peso / (altura * altura);
        return meu_imc;
    }

    public static void classifyIMC(double imc) {
        if (imc >= 18.5 && imc <= 24.9) {
            System.out.println("Peso normal");
        } else if (imc >= 25 && imc <= 29.9) {
            System.out.println("Acima do peso (sobrepeso)");
        } else if (imc >= 30 && imc <= 34.9) {
            System.out.println("Obesidade I");
        } else if (imc >= 35 && imc <= 39.9) {
            System.out.println("Obesidade II");
        } else if (imc > 40) {
            System.out.println("Obesidade III");
        }
    }
}
