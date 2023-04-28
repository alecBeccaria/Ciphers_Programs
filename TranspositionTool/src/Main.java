import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

        boolean exit = false;
        StringBuilder menu = new StringBuilder("Tranposition Cypher Tool!\n");
        menu.append("1. Transpose Message\n");
        menu.append("2. Decrypt Message\n");
        menu.append("3. Exit\n");

        while (!exit) {

            System.out.println(menu.toString());
            try {
                int selection = readConsoleInt();
                String result = "potato";
                int key;
                String message;
                switch (selection) {
                    case 1 -> {
                        System.out.println("Enter a message:\n");
                        message = readConsoleString();
                        System.out.println("Enter a key:\n");
                        key = readConsoleInt();
                        result = transposeTool.encrypt(message, key);
                    }
                    case 2 -> {
                        System.out.println("Enter a message:\n");
                        message = readConsoleString();
                        System.out.println("Enter a key:\n");
                        key = readConsoleInt();
                        result = transposeTool.decrypt(message, key);
                    }
                    case 3 -> exit = true;
                    default -> System.out.println("Not a valid input");
                }
                System.out.println(result);

            } catch (Exception e) {
                System.out.println("Must be a valid number!");
            }

        }
    }

    private static String readConsoleString() {
        Scanner readConsole = new Scanner(System.in);
        return readConsole.nextLine();
    }

    private static int readConsoleInt() {
        Scanner readConsole = new Scanner(System.in);
        return readConsole.nextInt();
    }

}
