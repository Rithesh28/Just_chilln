//package arrays;
public class anagram{
        public static void main(String[] args) {
                String strs []={"tea","eat","ate","tan","nat","bat"};
                //String temp="";
                for(int i=0;i<=strs.length-1;i++){
                        for(int j=0;j<=strs.length-1;j++){
                    char ch=strs[i].charAt(j);
                    System.out.println(ch);
                    /**if(ch>='a' && ch<='z' || ch>='A' && ch<='Z'){
                        strs[i]=temp;
                    }
                                **/
                        }
                }
        }
}