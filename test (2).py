package pgm5;
import java.util.Scanner;

public class zz {
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	
    	System.out.println("Enter age");
    	int age =sc.nextInt();
        
        if(age>18)
        {
        	System.out.println("Elder one");
        }else if(age<60) {
        	System.out.println("older one");
        }
        else if(age>10)
        {
        	System.out.println("Younger one");
        }
    }
}

 
