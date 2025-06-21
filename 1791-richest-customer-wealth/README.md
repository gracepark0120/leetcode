<h2><a href="https://leetcode.com/problems/richest-customer-wealth">1791. Richest Customer Wealth</a></h2><h3>Easy</h3><hr><p>You are given an <code>m x n</code> integer grid <code>accounts</code> where <code>accounts[i][j]</code> is the amount of money the <code>i​​​​​<sup>​​​​​​th</sup>​​​​</code> customer has in the <code>j​​​​​<sup>​​​​​​th</sup></code>​​​​ bank. Return<em> the <strong>wealth</strong> that the richest customer has.</em></p>

<p>A customer&#39;s <strong>wealth</strong> is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum <strong>wealth</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[1,2,3],[3,2,1]]
<strong>Output:</strong> 6
<strong>Explanation</strong><strong>:</strong>
<code>1st customer has wealth = 1 + 2 + 3 = 6
</code><code>2nd customer has wealth = 3 + 2 + 1 = 6
</code>Both customers are considered the richest with a wealth of 6 each, so return 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[1,5],[7,3],[3,5]]
<strong>Output:</strong> 10
<strong>Explanation</strong>: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[2,8,7],[7,1,3],[1,9,5]]
<strong>Output:</strong> 17
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;accounts.length</code></li>
	<li><code>n ==&nbsp;accounts[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= accounts[i][j] &lt;= 100</code></li>
</ul>


### 회고
이 문제는 map 같은 generator 를 사용해서 메모리를 줄이는 게 관건

#### map(function, iterable)
- function: 각 요소에 적용할 함수
- iterable: 리스트, 튜플, 문자열 등 반복 가능한 것

결과는 map 객체 → 메모리를 아끼기 위한 lazy evaluation (generator 비슷)

#### lazy 평가란?
값을 바로 계산하지 않고, 요청이 있을 때 계산하는 방식. 전부 메모리에 저장하지 않음.