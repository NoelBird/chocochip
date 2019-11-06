import java.util.PriorityQueue; // import는 ctrl + shift + o 로 임포트하는 것이지, 수동으로 임포트 하는 것이 아닙니다.
import java.util.Queue;
import java.util.Scanner;


class Node extends Object{  // 상속받는 예제
	int x =0;
	int y =0;
}

public class linear{
	public static int search(int[] arr, int x) {
//		구현
		return -1;
	}
	public static void main(String[] args) {
//		main
		
		Scanner sc = new Scanner(System.in); //ctrl +shift + o
		int T = sc.nextInt();  // ctrl + space. 숫자 입력받기
		String s = sc.next();  // 문자 입력받기
		Queue queue = new PriorityQueue<Integer>(); // template 사용하기
		Node node = new Node();     // class 사용법
		node.x = 20;
		 
	}
}