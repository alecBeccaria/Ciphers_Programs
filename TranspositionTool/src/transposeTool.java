public class transposeTool {
    // [][]
    // X Y

    public static String encrypt(String message, int key)
    {
        message = message.replaceAll(" ", "");
        message = message.replaceAll(",", "");
        char[] encrypted = new char[message.length()];
        int k = 0;

        for (int start = 0; start < key; start++) {
            for (int letter = start; letter < message.length(); letter += key) {
                encrypted[k] = message.charAt(letter);
                k++;
            }
        }

        return String.copyValueOf(encrypted);
    }

    public static String decrypt(String message, int key)
    {
        message = message.replaceAll(" ", "");
        char[] res = new char[message.length()];
        int k = 0;

        for (int j = 0; j < key; j++) {
            for (int i = j; i < message.length(); i += key) {
                res[i] = message.charAt(k++);
            }
        }

        return String.copyValueOf(res);
    }

}
