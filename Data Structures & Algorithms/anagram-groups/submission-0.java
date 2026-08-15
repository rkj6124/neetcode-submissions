class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> subMap = new HashMap<>();
        List<List<String>> subList = new ArrayList<>();
        for (String s: strs) {
            Map<Character, Integer> freq = new HashMap<>();
            for (int i = 0; i < s.length(); i++) {
                freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i), 0) + 1);
            }
            List<String> existingList = subMap.getOrDefault(freq, new ArrayList<>());
            existingList.add(s);
            subMap.put(freq, existingList);
        }
        for (List<String> list: subMap.values()) {
            subList.add(list);
        }
        return subList;
    }
}
