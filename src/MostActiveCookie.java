public class MostActiveCookie {
    public static void main(String[] args) {
        String filename = "";
        String date = "";
        try {
            filename = args[0];
            date = args[2];
            //TODO check if formats valid by checking .csv and date format
        } catch (ArrayIndexOutOfBoundsException e){
            System.out.println("not enough CLI arguments passed");
            return;
        }
        System.out.println(filename+"\n"+date);

    }
}
