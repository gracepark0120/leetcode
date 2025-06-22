<h2><a href="https://leetcode.com/problems/fizz-buzz">412. Fizz Buzz</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em>a string array </em><code>answer</code><em> (<strong>1-indexed</strong>) where</em>:</p>

<ul>
	<li><code>answer[i] == &quot;FizzBuzz&quot;</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.</li>
	<li><code>answer[i] == &quot;Fizz&quot;</code> if <code>i</code> is divisible by <code>3</code>.</li>
	<li><code>answer[i] == &quot;Buzz&quot;</code> if <code>i</code> is divisible by <code>5</code>.</li>
	<li><code>answer[i] == i</code> (as a string) if none of the above conditions are true.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

### 회고
- 우선 절대 리스트를 미리 할당해두고 인덱스로 하나하나 다시 넣는 방법은 금지. 
- 최대한 in-place generator 로 해결하려하고, 안되면 append() 사용하기
- 이 문제 같은 경우는 3 5 의 최대공약수 인 15 가 힌트 였음. if-else 문을 사용하게 되면 두 번 연산인 거를 두고 생각의 전환이 필요함.
- 문자열을 합친다 는 것도 힌트
- 3의 배수 먼저 확인, 문자열 부여, 5의 배수 확인, 문자열 부여 이 순서인 걸 알아챘으면 해결 

#### or 문법
A or B 이면
A 가 거짓이면(빈 문자열이면) B, A 가 참이면(빈 문자열이 아니면) A 를 반환함.
