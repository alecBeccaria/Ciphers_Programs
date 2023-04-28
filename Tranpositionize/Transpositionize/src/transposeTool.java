public class transposeTool {
    // [][]
    // X Y

    public static String encrypt(String message, int key) {
        // message = message.replaceAll("?", "");
        message = message.replaceAll(" ", "");
        //System.out.println(message);
        int colums = calculateColumnNumber(key, message.length());
        
        char[][] transposeGrid = new char[key][colums];

        char[] encryptedMessage = encryptLeftRight(message, transposeGrid, colums, key);
        StringBuilder sb = new StringBuilder();
        for (char c : encryptedMessage) {
            sb.append(c);
        }

        return sb.toString();
    }

    public static String decrypt(String message, int key) {
        // message = message.replaceAll("?", "");
        message = message.replaceAll(" ", "");
        int colums = calculateColumnNumber(key, message.length());
        
        char[][] transposeGrid = new char[key][colums];

        char[] decryptedMessage = decryptUpDown(message, transposeGrid, colums, key);
        StringBuilder sb = new StringBuilder();
        for (char c : decryptedMessage) {
            sb.append(c);
        }

        return sb.toString();
    }

    public static int calculateColumnNumber(int key, int messageLength) {
        int columns = 1;
        while (columns * key < messageLength) {
            columns++;
        }
        return columns;
    }

    private static char[] encryptLeftRight(String message, char[][] transposeGrid, int colums, int rows) {
        char[] messageChars = message.toCharArray();
        int _row = 0;
        int _column = 0;
        for (char c : messageChars) {
            transposeGrid[_row][_column] = c;
            
            if(_column == colums - 1){
                _column = 0;
                _row++;
            }else {
                _column++;
            }
            
        }
        char[] encryptedMessage = new char[messageChars.length + 1];
        int encryptIndex = 0;
        for (int column = 0; column < colums; column++) {
            for (int row = 0; row < rows; row++) {
                encryptedMessage[encryptIndex] = transposeGrid[row][column];
                encryptIndex++;
            }
        }
        return encryptedMessage;
    }

    private static char[] decryptUpDown(String message, char[][] transposeGrid, int colums, int rows) {
        char[] messageChars = message.toCharArray();
        int _row = 0;
        int _column = 0;
        for (char c : messageChars) {
            transposeGrid[_row][_column] = c;
            
            if(_row == rows - 1){
                _row = 0;
                _column++;
            }else {
                _row++;
            }
            
        }
        char[] encryptedMessage = new char[messageChars.length + 1];
        int encryptIndex = 0;
        for (int row = 0; row < rows; row++) {
            for (int column = 0; column < colums; column++) {
                encryptedMessage[encryptIndex] = transposeGrid[row][column];
                encryptIndex++;
            }
        }
        return encryptedMessage;
    }
}
