<template>
  <div class="hello">
    <h1>{{ msg }}</h1> 
    <h3>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</h3>

    <div class="footer" id="footer">
		<div class="FooterCtn">
			<a href="https://www.facebook.com/lifescienceyoungcamp/" target="_blank" rel="noopener">					
				<div class="fblogo" src="../assets/FB.png"></div>	
				<div class="fblink">Facebook連結</div>		
			</a>
		</div>
	</div> 

    <div class="welcome" id="welcome">
      <h1 >2017生命科學小學營《生生不息》報名已經開始囉！</h1>
		<p>想知道生物學家們平常在做些甚麼嗎？</p>
		<p>想知道地球上的生物身體裡藏著什麼樣的奧秘嗎？</p>
        <p>那就一定來參加生科小學營吧！</p>
		<p>由台大生命科學系的大哥哥、大姊姊，帶著小朋友一起體驗</p>
        <p>精彩刺激的闖關活動、益智趣味的DIY實作以及豐富充實的生物課程</p>
		<p>大家記得告訴自己的朋友，一起變成小小生物學家吧！</p>
        <p v-html="bodyText"></p>
		<p>
        為了推廣生命科學知識、培養小學生對生物的熱忱以及讓社會大眾對於生命科學有<br>
		更多的理解，透過舉辦此營隊教育新一代的學員對生命的尊重與探索，同時也能讓<br>
        更多家長理解本領域科系的相關應用與發展。
        </p>
		<p v-html="bodyText"></p>
		<p>
        *營期：2017年2月8日至2017年2月10日 每天早8:30~下午5:00<br>
		*地點：台灣大學生命科學館、台灣大學總校區、台北市立動物園<br>
		*招生對象:小學四年級到六年級<br>
		*費用:3500元/人(含DIY材料費)<br>
		*報名日期:即日起至12/15截止(請點選本業上方”我要報名”按鈕，並填寫報名表，按下確認送出後即可。)
        </p>
		<p v-html="bodyText"></p>
	  	<p>
        總召：黃柏超 聯絡電話：0918-260598<br>
        副召：施乙漢 聯絡電話：0923-557756
        </p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Homepage',
  data() {
    return {
      bodyText: '<br>'
    }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b9b3;
}
.hello{
  background-color: #456ec4;
}

.welcome{
  margin: 23px;
  padding: 20px;
  font-family: 'SetoFont', 'Baloo Paaji', sans-serif;
  background-color: #f6f7f4;
}
.welcome h1{ 
  font-size: 45px;
}

.welcome p {
  text-align: center;
  font-size: 20px;
}

#footer {
  height: 40px;
  padding: 20px;
  background-color:#456ec4;
  font-family: 'SetoFont', 'Baloo Paaji', sans-serif;
}
.FooterCtn{
  width: 210px;
  height: 10px;
  display: block;
}

.FooterCtn:hover .fblogo{
  background: url("~@/assets/FB.png");
  background-size: cover;
  background-repeat: no-repeat;
}
.FooterCtn:hover .fblink{
  color: #686C5C;
  text-decoration: none
}
.fblogo {
  display: inline-block;
  width: 30px;
  height: 30px;
  background: url("~@/assets/FBhover.png");
  background-size: cover;
  background-repeat: no-repeat;
  text-indent: -9999px;
}

.fblink{
  height: 10px;
  padding: 20px;
  display: inline-block;
  vertical-align: sub;
  background-color: #456ec4;
}

</style>
