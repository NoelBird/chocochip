# -*- coding: utf-8 -*-

# tensorflow 패키지 불러오기
import tensorflow as tf

# 텐서플로우에서 MNIST 데이터 로드하기
from tensorflow.examples.tutorials.mnist import input_data

# 레이블이 정수 형태로 저장되어있지만 훈련을 위해서 원-핫 인코딩으로 로드해야한다.
# mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)
f = open('train.csv', 'r')
f.readline()
data = f.readlines()
f.close()
train_labels = []
train_images = []
for line in data:
    l = list(map(int, line.split(',')))
    tmp = [0 for i in range(10)]
    tmp[l[0]] = 1
    train_labels.append(tmp)
    train_images.append(l[1:])


# 퍼셉트론 입력 크기, 클래스 수, 배치 크기, 반복 또는 배치의 총 개수 선언
input_size = len(train_images[0])
no_classes = 10
batch_size = 200
total_batches = len(train_images) // 200

# 입력데이터와 타깃을 위한 플레이스홀더 정의 (None은 어떤 크기든 될 수 있음을 의미)
x_input = tf.placeholder(tf.float32, shape=[None, input_size])
y_input = tf.placeholder(tf.float32, shape=[None, no_classes])

# 단순한 선형 분류자 또는 퍼셉트론을 정의
weights = tf.Variable(tf.random_normal([input_size, no_classes]))
bias = tf.Variable(tf.random_normal([no_classes]))
logits = tf.matmul(x_input, weights) + bias

# 퍼셉트론으로 생성된 로짓과 원-핫 레비을의 y_input을 비교
# 비교는 교차 엔트로피와 함께 소프트맥스를 사용
softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
    labels=y_input, logits=logits)
loss_operation = tf.reduce_mean(softmax_cross_entropy)
optimiser = tf.train.GradientDescentOptimizer(
    learning_rate=0.5).minimize(loss_operation)

# 모델 훈련을 위한 세션 시작
session = tf.Session()

# 전역 변수 초기화 함수를 이용해 변수를 초기화
session.run(tf.global_variables_initializer())

# 배치의 데이터를 반복해서 읽고 모델을 훈련시킨다.
for epoch in range(total_batches):
    train_image = train_images[epoch*batch_size:(epoch+1)*batch_size]
    train_label = train_labels[epoch*batch_size:(epoch+1)*batch_size]
    # mnist_batch = mnist_data.train.next_batch(batch_size)
    _, loss_value = session.run([optimiser, loss_operation], feed_dict={
    x_input: train_image,
    y_input: train_label
    })
    print(loss_value)

# predictions = tf.argmax(logits, 1)

f = open('test.csv', 'r')
f.readline()
data = f.readlines()
test_label = []
test_image = []
for line in data:
    l = list(map(int, line.split(',')))
    # tmp = [0 for i in range(10)]
    # tmp[l[0]] = 1
    # test_label.append(tmp)
    test_image.append(l)

predictions = tf.argmax(logits, 1)
ans = session.run(predictions, feed_dict={x_input: test_image})

with open('result.txt','w') as f_result:
    idx = 1
    f_result.write('ImageId,Label')
    for i in ans:
        f_result.write('%d,%d\n' % (idx, i))
        idx+=1
    session.close()