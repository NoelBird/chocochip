/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner sc=new Scanner(System.in);
		int T = sc.nextInt();
		for(int i=0; i<T; i++){
		    String a = sc.next();
		    int b = sc.nextInt();
		    int c = sc.nextInt();
		    System.out.println(a.substring(b,c+1));
		}
	}
}