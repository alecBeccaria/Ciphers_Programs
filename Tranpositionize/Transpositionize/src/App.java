public class App {
    public static void main(String[] args) throws Exception {
        boolean exit = false;
        StringBuilder menu = new StringBuilder("Tranposition Cypher Tool!\n");
        menu.append("1. Transpose Message\n");
        menu.append("2. Decrypt Message\n");
        menu.append("3. Exit\n");

        while (!exit) {
            System.out.println(menu.toString());
            try {
                int selection = Integer.parseInt(System.console().readLine());
                String result = "potato";
                switch (selection) {
                    case 1:
                        System.out.println("Enter a message:\n");
                        String message = System.console().readLine();
                        System.out.println("Enter a key:\n");
                        int key = Integer.parseInt(System.console().readLine());
                        result = transposeTool.encrypt(message, key);
                        break;
                    case 2:
                        System.out.println("Enter a message:\n");
                        message = System.console().readLine();
                        System.out.println("Enter a key:\n");
                        key = Integer.parseInt(System.console().readLine());
                        result = transposeTool.encrypt(message, key);
                        break;
                    case 3:
                        exit = true;
                        break;
                    default:
                        System.out.println("Not a valid input");
                }
                System.out.println(result);

            } catch (Exception e) {
                System.out.println("Must be a valid number!");
            }

        }
    }

}
