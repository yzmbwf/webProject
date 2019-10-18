//登录输入框提示
function focu(){
	var use = document.getElementById('user');
	var pro_user = use.value;
	if(pro_user=='请输入用户名'){
		use.value='';
	}
}
function blurs(){
	var tag = document.getElementById('user');
	var val = tag.value;
	if(val.length==0){
		tag.value='请输入用户名';
	}
}
function focuspwd(){
	var tag = document.getElementById('pwd')
	var val = tag.value
	if(val=='请输入密码'){
		tag.value = ''
		tag.type = 'password'
	}
}
function blurpwd(){
	var tag = document.getElementById('pwd')
	var val = tag.value
	if(val==''){
		tag.value='请输入密码'
		tag.type = 'text'
	}
}

//忘记密码弹框
function ForgotPwd(){
	document.getElementById('mk').classList.remove('hide');
	document.getElementById('bc').classList.remove('hide');
}
function cancelup(){
	document.getElementById('mk').classList.add('hide');
	document.getElementById('bc').classList.add('hide');
}