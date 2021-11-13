#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<malloc.h>

//첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다.이 문자열은 영어 소문자로만 이루어져 있으며, 길이는 100, 000을 넘지 않는다.둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 N(1≤N≤500, 000)이 주어진다.셋째 줄부터 N개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다.명령어는 위의 네 가지 중 하나의 형태로만 주어진다.


typedef struct _st{
	char ch;
	_st* prev;
	_st* next;
} st;

st* append(st* head, char value);
st* insert(st* head, char value);
st* erase(st* head);

st Head;
st* head;

int main() {

	head = &Head;

	// 문자열 받아서 초기화
	char ch;
	while (1) {
		scanf("%c", &ch);
		if (ch == '\n') {
			break;
		}
		head = append(head, ch);
	}

	int cnt;
	scanf("%d", &cnt);

	char p[5];
	for (int i = 0; i < cnt; i++) {
		scanf("%s", p);
		if (p[0] == 'L') { //done
			if (head->prev != NULL) {
				head = head->prev;
			}
		}
		else if (p[0] == 'D') {
			if (head->next != NULL) {
				head = head->next;
			}
		}
		else if (p[0] == 'B') {
			head = erase(head);
		}
		else if (p[0] == 'P') {
			scanf(" %c", &ch);
			head = insert(head, ch);
		}
	}
	

	

	head = &Head;
	head = head->next;
	while (1) {
		printf("%c", head->ch);
		if (head->next == NULL) {
			break;
		}
		head = head->next;
	}
	printf("\n");
	
	return 0;
}

st* insert(st* head, char value) {
	st* new_block = (st*)calloc(1, sizeof(st));
	new_block->ch = value;
	new_block->next = head->next;
	new_block->prev = head;
	if (head->next != NULL) {
		head->next->prev = new_block;
	}
	head->next = new_block;
	head = head->next;
	return head;
}

st* append(st* head, char value) {
	st* new_block = (st*)calloc(1, sizeof(st));
	new_block->ch = value;
	new_block->prev = head;
	head->next = new_block;
	head = head->next;
	return head;
}

void right(st* head) {
	if (head->next != NULL) {
		head = head->next;
	}
}

void left(st* head) {
	if (head->prev != NULL) {
		head = head->prev;
	}
}

st* erase(st* head) {
	if (head->prev == NULL) {
		return head;
	}
	if (head->next == NULL) {
		st* tmp = head;
		head = head->prev;
		head->next = NULL;
		free(tmp);
	}
	else {
		st* tmp = head;
		head->prev->next = head->next;
		head->next->prev = head->prev;
		head = head->prev;
		free(tmp);
	}
	return head;
}