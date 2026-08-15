class Solution {

    public String encode(List<String> strs) {
        String specialSymbol = "#";
        StringBuilder sb = new StringBuilder();
        for (String str: strs) {
            sb.append(str.length());
            sb.append(specialSymbol);
            sb.append(str);
        }
        System.out.println(sb.toString());
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        Stack<Character> resStack = new Stack<>();
        for (int i = str.length() - 1; i >=0; i--) {
            resStack.push(str.charAt(i));
        }
        System.out.println("Stack is" + resStack);

        while (!resStack.isEmpty()) {
            StringBuilder sb = new StringBuilder("");
            int size = getSize(resStack);
            // int size = resStack.pop() - '0';
            Character symbol = resStack.pop();
            System.out.println("size" + size + "symbol" + symbol);
            if (symbol.equals('#')) {
                while (size-- > 0 && !resStack.isEmpty()) {
                    sb.append(resStack.pop());
                }
            } else {
                System.out.println("not a correct encoded value");
            }
            System.out.println("word: " + sb.toString());
            res.add(sb.toString());
        }
        return res;
    }

    public int getSize(Stack<Character> resStack) {
        int size = 0;
        while (Character.isDigit(resStack.peek())) {
            int digit = resStack.pop() - '0';
            size = size*10 + digit;
        }
        return size;
    }
}
